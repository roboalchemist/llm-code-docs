# Source: https://docs.nexus.xyz/trading/perpetuals/margining.md

# Margining

Margining on the Nexus Exchange will be executed natively inside NexusCore, the enshrined financial co-processor suite that powers the Exchange. Nexus Layer 1 is designed to support both cross and isolated margin.&#x20;

#### Initial Margin Requirements

When opening a leveraged position, traders must post initial margin, defined by the maximum leverage allowed for a given market.&#x20;

Initial margin ensures sufficient collateral at entry and will be verified atomically by the Exchange Co-processor before an order is accepted into the orderbook. The initial margin calculation will follow the formula:

$$
initial\_margin = \frac{position\_size \times mark\_price}{leverage}
$$

Because margin validation will run inside NexusCore, traders benefit from:

* **Deterministic enforcement** (no race conditions from asynchronous contract calls)
* **Sub-second execution** aligned with block times
* **Atomic settlement** with order placement

This will ensure both speed and safety at the protocol level.

#### **Maintenance Margin**

Maintenance margin is the minimum margin that must be preserved to keep a position open. Falling below this threshold makes a position eligible for liquidation. Each market will have its own maintenance margin fraction, calculated as:

$$
maintenance\_margin = \frac{1}{max\_\_leverage \times 2}
$$

#### **Liquidation Process**

Positions will be liquidated when the mark price from the Nexus Oracle System causes equity to fall below maintenance margin. Refer to the ***Liquidations*** page to learn more.
