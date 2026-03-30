# Source: https://docs.nexus.xyz/trading/perpetuals/price-oracles.md

# Price Oracles

Nexus' oracle will provide fast, reliable, manipulation-resistant spot index prices for all perpetual markets on the Exchange.&#x20;

Oracle prices are a foundational component of the NexusCore risk engine and will be used for:

* **Mark price calculation**
* **Funding rate computation**
* **Margin requirements**
* **Liquidation triggers**
* **Triggering TP/SL and conditional orders**

Oracle updates will be published every **\~3 seconds**, ensuring accurate and timely tracking of global spot markets.

#### **Design Overview**

Nexus will use a validator-published, multi-source, volume-weighted oracle for spot pricing in the ***Exchange Alpha***.

This design draws inspiration from validator-driven mechanisms but replaces stake-based weighting with market volume-based weighting, creating a more market-neutral and liquidity-reflective system.

Every validator will independently compute a spot oracle price for each supported asset using aggregated data from major centralized exchanges and, when appropriate, Nexus-native markets.

#### Validator Responsibilities

Each validator will continuously:

1. **Fetch spot mid-prices** for each asset from supported exchanges
2. **Compute a volume-weighted median** across these sources
3. **Publish an updated oracle price** roughly every 3 seconds
4. **Sign and broadcast** the price to other validators and the network

These prices are then aggregated into a final L1 oracle price consumed by NexusCore.

#### External Data Sources

Validators will query spot mid-prices from a diverse set of high-liquidity exchanges, including:

* **Binance**
* **OKX**
* **Bybit**
* **Kraken**
* **KuCoin**
* **Gate.io**
* **MEXC**

Each source will contribute to the oracle calculation using a predefined **volume-based weight**, reflecting the global liquidity share of each venue for that asset.

#### Final Calculation

1. Validators gather spot mid-prices
2. Volume-based weights applied
3. Validators compute a weighted median and each broadcast to the network
4. NexusCore aggregates all validator submissions
5. NexusCore computes the final L1 oracle price as a volume-weighted median
