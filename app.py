from flask import Flask, request, jsonify
import anthropic
import json
import os
import requests

app = Flask(__name__)
client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
DISCORD_WEBHOOK = os.environ.get("DISCORD_WEBHOOK")

def send_discord(message):
    if not DISCORD_WEBHOOK:
        print("ERROR: DISCORD_WEBHOOK env variable not set")
        return
    requests.post(DISCORD_WEBHOOK, json={"content": message})

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json(force=True, silent=True) or json.loads(request.get_data(as_text=True) or "{}")

    prompt = f"""You are a professional futures trader. Given this TradingView alert, return ONLY the following block — no extra text, no reasoning:

Alert data: {data}

Format exactly like this:
📈 LONG  (or 📉 SHORT)
Entry: [price]
SL: [price]
TP1: [price]
TP2: [price]
TP3: [price]
Mgmt: [one line — e.g. "Move SL to BE after TP1. Trail to TP2."]
"""

    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}]
    )

    trade_setup = message.content[0].text
    send_discord(f"**Trade Alert - {data.get('symbol', 'Unknown')}**\n{trade_setup}")

    return jsonify({"trade_setup": trade_setup})

@app.route("/debug", methods=["GET"])
def debug():
    return jsonify({
        "DISCORD_WEBHOOK_set": DISCORD_WEBHOOK is not None,
        "ANTHROPIC_API_KEY_set": os.environ.get("ANTHROPIC_API_KEY") is not None
    })

@app.route("/", methods=["GET"])
def home():
    return "TradingView-Claude server is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
