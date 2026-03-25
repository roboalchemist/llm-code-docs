# Source: https://docs.nexus.xyz/trading/perpetuals/positions.md

# Positions

Positions represent your active exposure in markets on the Nexus Exchange. Each position will maintain a live state within the NexusCore risk engine, tracking your entry price, size, collateral usage, funding, fees, and real-time profit and loss.

Positions will be updated every Core block, ensuring near-instant feedback on risk, margin, and liquidation thresholds.

#### **Open Positions**

Your open positions panel will display continuously updated metrics derived from the Exchange Co-processor’s real-time risk engine:

* **Unrealized PnL** — shown in both USD value and percentage
* **Position Size** — total notional exposure (long or short)
* **Average Entry Price** — volume-weighted entry across fills
* **Margin Usage** — collateral allocated to maintain the position
* **Liquidation Price** — the estimated price at which the risk engine will liquidate your position
* **Funding Payments** — funding paid or received since opening

All calculations will follow the deterministic margin and funding rules enforced inside NexusCore’s financial state machine.

#### **Modifying Positions**

Active positions can be managed through various methods to adjust your exposure or exit trades. Updates will be applied atomically via the Core matching engine.

* **Adjusting Position Size**
  * You can increase or decrease your position size via market or limit orders using the standard trading modal.&#x20;
  * Orders in the opposite direction exceeding your current position size will automatically "flip" your positions.&#x20;
    * For example, if you have 1 BTC active long and place a market sell for 2 BTC, you'll end up with 1 BTC active short.
* **Closing Positions**
  * Exit a position partially or in full from the Positions tab.&#x20;
  * Closing executes a market or limit order on the opposite side and immediately realizes PnL after the fill.

#### **Position History**

Track and review trading activity with transparent historical data through the Position History tab.
