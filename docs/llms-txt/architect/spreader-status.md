# Source: https://docs.architect.co/algos-book/spreader/spreader-status.md

# Spreader Status

### SpreaderStatus

| Parameter                | Description                                                                                                                    |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| leg1\_fill\_quantity     | Signed, filled quantity on leg 1                                                                                               |
| leg2\_fill\_quantity     | Signed, filled quantity on leg 2                                                                                               |
| implied\_spread\_vwap    | The average filled price of completed spread units so far                                                                      |
| current\_spreader\_phase | [SpreaderPhase](#spreaderphase)                                                                                                |
| leg1\_quote\_order\_id   | The [QuoteOneSide](https://docs.architect.co/algos-book/quoteoneside) order ID for Leg1, if Leg1 has a quote out in the market |
| leg2\_quote\_order\_id   | The [QuoteOneSide](https://docs.architect.co/algos-book/quoteoneside) order ID for Leg1, if Leg1 has a quote out in the market |
| spread\_price            | The current spread taking price (the price to cross the implied market)                                                        |

### SpreaderPhase

| Parameter              | Description                                                                                                                                                                   |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **NoBbo**              | Either the bid or the ask does not exist. Usually this means the market is closed, or you caught the algo before it fully subscribed to market data (common in paper trading) |
| **Waiting**            | Algo order is live, but no orders in any of the legs are in the market                                                                                                        |
| **OrdersInMarket**     | Algo order is live, with orders in at least one of the legs live in the market                                                                                                |
| **DoneNotFullyFilled** | Algo order has halted (generally from **MissedTakePolicy.Halt**) but the original spreader quantity is not fully complete                                                     |
| **Done**               | Algo order has completed                                                                                                                                                      |
