# Source: https://docs.nexus.xyz/trading/perpetuals.md

# Perpetuals

Perpetual futures on the Nexus Exchange will be fully onchain, high-performance derivative markets built directly into the Nexus Layer 1.

Perpetual futures are derivative contracts that track the price of an underlying asset without requiring ownership of the asset itself. Traders gain continuous exposure by posting collateral, opening a leveraged position, and paying or receiving funding depending on market conditions.

These markets allow traders to take leveraged long or short positions on supported assets without expirations, while benefiting from deterministic execution, transparent accounting, and cryptographic verifiability at every step.

Unlike traditional perpetual DEXs that simulate a decentralized exchange on top of a general-purpose VM, Nexus will integrate financial primitives *natively at the protocol layer*. Matching, liquidation, margining, and funding rate calculations will run inside **NexusCore**, a high-throughput co-processor suite designed specifically for Internet-scale markets.

{% content-ref url="perpetuals/margining" %}
[margining](https://docs.nexus.xyz/trading/perpetuals/margining)
{% endcontent-ref %}

{% content-ref url="perpetuals/order-types" %}
[order-types](https://docs.nexus.xyz/trading/perpetuals/order-types)
{% endcontent-ref %}

{% content-ref url="perpetuals/positions" %}
[positions](https://docs.nexus.xyz/trading/perpetuals/positions)
{% endcontent-ref %}

{% content-ref url="perpetuals/funding-rates" %}
[funding-rates](https://docs.nexus.xyz/trading/perpetuals/funding-rates)
{% endcontent-ref %}

{% content-ref url="perpetuals/liquidations" %}
[liquidations](https://docs.nexus.xyz/trading/perpetuals/liquidations)
{% endcontent-ref %}

{% content-ref url="perpetuals/price-oracles" %}
[price-oracles](https://docs.nexus.xyz/trading/perpetuals/price-oracles)
{% endcontent-ref %}
