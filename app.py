from flask import Flask, request, jsonify
import anthropic
import os

app = Flask(__name__)
client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json

    prompt = f"""You are a professional trader. Analyze this TradingView alert data and give me a clear trade setup:

Alert data: {data}

Include:
- Trade direction (Long/Short)
- Entry price
- Stop loss
- Take profit targets (TP1, TP2, TP3)
- Brief reasoning
"""

    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}]
    )

    return jsonify({"trade_setup": message.content[0].text})

@app.route("/", methods=["GET"])
def home():
    return "TradingView-Claude server is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
