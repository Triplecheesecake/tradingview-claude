# MES Trading Strategy Log

## BEST STRATEGY: v4 - VWAP Pullback + W Formation
**File:** strategy.pine
**Results:** 128 trades | 32.0% win rate | $3,721 net PnL | PF 1.561
**Avg win:** $252 | **Avg loss:** $76 | **Worst day:** $246 (safe for TopStep)
**With 3 contracts:** ~$11,163 over 3 years | Worst day $738 (under $1,000 TopStep limit)

### How it works
1. Price is in uptrend (EMA20 > EMA50, above EMA200)
2. SPX above 200-day EMA (bull market confirmed)
3. Price was above VWAP, dips to touch VWAP (pullback)
4. Price closes back above VWAP (W formation - higher low)
5. RSI 50-72 (momentum, not overbought)
6. Volume 1.5x average (institutional participation)
7. Enter long, stop below VWAP (ATR x1.0), target 50 EMA or 3:1 R:R

### Session
9:30 AM - 1:30 PM ET (best quality window)

### TopStep 50k Risk
- Zero days exceeded $1,000 daily loss limit in 3 years
- Scale to 3 contracts to pass combine faster
- Worst day on 3 contracts: ~$738 (still safe)

---

## VERSION HISTORY

| Version | Trades | Win Rate | Net PnL | Profit Factor | Notes |
|---------|--------|----------|---------|---------------|-------|
| v1 EMA crossover | 18 | 22.2% | -$331 | 0.913 | Too many shorts, lagging |
| v2 ORB breakout | 203 | 21.7% | -$2,117 | 0.709 | False breakouts, shorts killed it |
| v3 VWAP pullback | 155 | 33.5% | $4,365 | 1.566 | First profitable strategy |
| **v4 + W formation** | **173** | **34.1%** | **$4,814** | **1.510** | **BEST OVERALL** |
| v5 longs only + skip | 155 | 31.0% | $4,099 | 1.510 | Skip 10-10:30 didn't help |
| v6 + news + VIX filter | 80 | 30.0% | $2,673 | 1.655 | Filters too tight |
| v7 loosened filters | 117 | 29.9% | $3,333 | 1.528 | Good quality, less trades |
| v8 liquidity sweep | 76 | 30.3% | $1,223 | 1.325 | Concept right, needs work |
| v9 combined | 80 | 31.2% | $1,284 | 1.363 | Breakout = 43.8% win rate! |
| v10 breakout only | 53 | 35.8% | $1,038 | 1.427 | Inconsistent |
| v11 best combined | 111 | 27.9% | $2,299 | 1.413 | Breakout hurt overall |

---

## WHAT WORKS
- VWAP as key level
- Triple EMA uptrend (EMA20 > EMA50, above EMA200)
- W formation (higher low at VWAP)
- Bull market filter (SPX > 200 EMA)
- ATR-based stops
- 50 EMA as target
- Session 9:30 AM - 1:30 PM ET
- Longs only (MES is a bull market instrument)

## WHAT DOESN'T WORK
- Shorts (MES is in long-term uptrend)
- EMA crossover entries (too laggy)
- ORB breakouts (too many fakeouts)
- Fixed time blackouts (cuts good trades)
- 5min timeframe (too noisy)
- Too many filters (reduces trade count more than it helps)

## KEY INSIGHTS
- Market makers create fake moves below VWAP to hunt stops, then reverse
- The W formation captures this: price dips below VWAP (wick), closes back above = institutional entry
- 75% of losing longs would have been profitable as shorts - but shorts lose in bull market
- Win rate ceiling on 15min MES appears to be 34-35% with this approach
- Profit factor of 1.5+ is sustainable and professional grade
- Best win rate seen: 43.8% on VWAP momentum breakout (v9) - needs more development

---

## BEST GOLD STRATEGY: v6 - Institutional + VWAP Hybrid
**File:** gold_strategy.pine
**Results:** 42 trades | 40.5% win rate | $11,647 net PnL | PF 3.448
**Avg win:** $965 | **Avg loss:** $190 | **Worst day:** $524 (safe)
**With 2 contracts:** ~$23,294 over 3 years

### Signals
- **Institutional (overnight):** Previous day low swept in London/Asia killzone → reclaims VWAP → strong bar → enter long, target next $100 round number
- **VWAP Pullback (US session):** Same W formation logic as MES, 9:30-1:30 ET

### Sessions
- London: 2-9 AM ET | Asia: 8 PM-2 AM ET | US: 9:30 AM-1:30 PM ET
- Dead zone blocked: 3-8 PM ET

---

## COMBINED SYSTEM PERFORMANCE
| Strategy | Trades/mo | Net PnL (3yr) | 3 contracts |
|----------|-----------|---------------|-------------|
| MES v4   | 3.6       | $3,721        | $11,163     |
| Gold v6  | 1.2       | $11,647       | $34,941     |
| **Total**| **4.8**   | **$15,368**   | **$46,104** |

**$46,104 / 36 months = $1,280/month on 3 contracts** ✅

## NEXT STEPS
1. Run MES v4 live on TopStep combine (3 contracts)
2. Set up Gold v6 alerts on MGC 15min chart
3. Push win rate toward 70% goal
4. Add more daily trade frequency
