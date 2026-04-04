# Source: https://docs.nexus.xyz/trading/perpetuals/liquidations.md

# Liquidations

Liquidations will protect the Nexus Exchange from insolvency by ensuring that traders maintain sufficient margin to support their leveraged positions.&#x20;

When a trader’s account equity falls below the required maintenance margin, NexusCore’s liquidation engine will automatically intervene and close the position at the current mark price, preventing negative balances and preserving system-wide solvency.

#### How Liquidation Works

**Mark Price & Equity**

Nexus will use a mark price derived from the oracle. A trader’s equity will be computed from:

$$
equity = collateral + unrealized\_-pnl(mark\_-price)
$$

**Margin Requirements**

* Initial Margin

$$
initial\_-margin = (position\_-size × entry\_-price) / leverage
$$

* Maintenance Margin

$$
maintenance\_-margin = 1 / (max\_-leverage × 2)
$$

**Liquidation Trigger**

A position will be liquidated when equity falls below maintenance margin.

**Liquidation Process**

1. Trigger: Equity falls below maintenance margin.
2. Execution: A dedicated on-chain liquidator sub-account closes the position at or near mark price.
3. Bankruptcy Protection: A price cap prevents negative balances.
4. Insurance Fund: Covers any remaining shortfall if the position cannot be closed in time.
