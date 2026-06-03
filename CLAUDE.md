# TradingView-Claude Project Context

## What This Is
Automated trading alert system: TradingView sends alerts → Flask server → Claude API analyzes → Discord webhook notification. Live and deployed.

## Infrastructure
- **Flask server:** https://web-production-d93ef.up.railway.app
- **GitHub:** https://github.com/Triplecheesecake/tradingview-claude
- **Local files:** `C:\Users\Marq\OneDrive - University of Central Florida\Desktop\tradingview-claude`
- **Platform:** Railway (Procfile deployment)
- **Env vars on Railway:** `ANTHROPIC_API_KEY`, `DISCORD_WEBHOOK`
- **TradingView:** Premium subscription + CME/COMEX real-time data feeds
- **Broker/Platform:** TopStep 50k Combine

## Trading Plan
- **Account:** TopStep 50k combine
- **Contracts:** 3 per signal
- **Daily stop:** -$500 (buffer before TopStep's $1,000 hard limit)
- **Goal:** Pass combine in 1-2 weeks, then scale to multiple funded accounts
- **Long-term:** Add BTC strategy after combine passed, scale to multiple accounts

## MES Strategy (v4 — BEST)
**File:** `strategy.pine` / **Indicator:** `indicator.pine`
- VWAP pullback + W formation, 15min chart, MES1!
- Session: 9:30 AM – 1:30 PM ET
- Longs only (MES is a bull market instrument — shorts consistently lose)
- Wednesday blocked (FOMC/Fed days)
- **Backtest (3 years):** 173 trades | 34.1% win rate | $4,814 net PnL | PF 1.510
- **3 contracts:** ~$11,163 net | Worst day $738 (under $1,000 TopStep limit)

### Entry Logic
1. EMA20 > EMA50, price above EMA200 (uptrend)
2. SPX above 200-day EMA (bull market confirmed)
3. Price dips to touch VWAP then closes back above (W formation)
4. RSI 50–72 (momentum, not overbought)
5. Volume 1.5x average
6. Stop: ATR x1.0 below VWAP | Target: 50 EMA or 3:1 R:R

## MGC Gold Strategy (v6 — BEST)
**File:** `gold_strategy.pine` / **Indicator:** `gold_indicator.pine`
- Institutional sweep + VWAP hybrid, 15min chart, MGC1!
- Wednesday blocked
- **Backtest:** 42 trades | 40.5% win rate | $11,647 net PnL | PF 3.448

### Signal 1 — Institutional (London/Asia sessions)
- Previous day low swept in London (2–9 AM ET) or Asia (8 PM–2 AM ET) killzone
- Price reclaims VWAP → strong bar → enter long
- Target: next $100 round number

### Signal 2 — VWAP Pullback (US session)
- Same W formation logic as MES
- Session: 9:30 AM – 1:30 PM ET
- Dead zone blocked: 3–8 PM ET

## Combined System Performance (3 contracts)
| Strategy | Net PnL (3yr) | 3 Contracts |
|----------|--------------|-------------|
| MES v4   | $4,814       | $11,163     |
| Gold v6  | $11,647      | $34,941     |
| **Total**| **$16,461**  | **$46,104** |

**$46,104 / 36 months = $1,280/month**

## What Works / Doesn't Work
**Works:** VWAP as key level, triple EMA uptrend, W formation (higher low), bull market filter, ATR stops, 50 EMA target, longs only, 15min timeframe
**Doesn't work:** Shorts, EMA crossover entries, ORB breakouts, fixed time blackouts, 5min TF, too many filters

## Key Insight
Market makers sweep below VWAP to hunt stops, then reverse. The W formation captures institutional re-entry after the sweep. Win rate ceiling on 15min MES appears to be ~34–35% with this approach. Profit factor 1.5+ is sustainable.

## app.py Summary
- `/webhook` POST — receives TradingView JSON alert, sends to Claude for analysis, posts formatted trade setup to Discord
- `/debug` GET — checks env vars are set
- Model: `claude-sonnet-4-6`, max_tokens: 1024

## Next Steps (as of last session)
1. Run MES v4 + Gold v6 live on TopStep combine (3 contracts each)
2. Push win rate toward 70% goal
3. Add BTC strategy after combine passed
4. Add more sessions for daily signal frequency
5. Scale to multiple funded accounts
