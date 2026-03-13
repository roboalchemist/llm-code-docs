# Nexus Documentation

Source: https://docs.nexus.xyz/llms-full.txt

---

# Introduction

Nexus will be a high-performance Exchange Layer 1 blockchain purpose-built for verifiable finance. Our vision is to create a decentralized Internet Exchange — a global, Layer 1 platform where every asset, market, and stream of information is instantly tradable with extreme performance and low latency, powered by a foundation of high-performance verifiable computation based on zero-knowledge proofs. We believe finance is the most important application of verifiable computation, forming the foundation for a new programmable economy.

Nexus targets the $1T+ in daily exchange TradFi volume market across global spot, perps, derivatives, options, RWAs, treasuries, FX, and prediction markets, bringing programmable and composable exchange markets to the Internet’s financial layer.

#### Technical Overview

Nexus presents a high-performance Layer 1 blockchain optimized from first principles for verifiable, high-throughput and low-latency exchange computation.&#x20;

The Nexus Layer 1 will introduce a custom parallelized co-processor architecture that will extend the NexusEVM with **NexusCore**: a bundle of high-performance, exchange-optimized computational engines enshrined directly at the protocol level.

These native co-processors will provide developers with:

* High-throughput matching engines
* Real-time price oracles and data feeds
* Automated liquidation systems
* Other specialized financial primitives

This design will enable the permissionless deployment of high-performance Internet markets (perpetual futures, options, prediction markets, etc.) with CEX-level throughput and latency.

Additionally, Nexus co-processors will expose CEX-like APIs directly at the L1 node level, allowing high-frequency trading strategies to be migrated onchain with minimal changes.

**Co-Designed for Performance and Verifiability**

* NexusBFT consensus will deliver sub-second block times with deterministic (instant) finality.
* The parallelized NexusEVM + NexusCore execution environment will run independent orderbook engines concurrently, eliminating head-of-line blocking.
* Every order, cancel, trade, settlement, and liquidation will be executed and verified fully onchain and transparently.

**Long-term Scalability via Verifiable Computation**

At the core of the system will be the Nexus zkVM – a high-performance zero-knowledge virtual machine designed to horizontally scale the network through distributed proof generation.

The Nexus zkVM:

* Is already deployed and running on millions of devices through the Nexus Network distributed prover network
* Is currently experimental but production-ready for select workloads
* Will enable millions of devices to collaboratively validate financial computations, pushing Nexus toward Internet-scale throughput while preserving full cryptographic verifiability

<figure><img src="https://1928578818-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fmi9nUlZMKVkCp0Tab0VD%2Fuploads%2Fjl37gd9UBVVuoAvlDqTX%2F1.png?alt=media&#x26;token=cb94c17f-38d0-418a-928a-3c2327cc638b" alt=""><figcaption><p>The Nexus blockchain consists of two parallel state-machines, NexusEVM and NexusCore, <br>and a three-layer architecture, featuring Execution, Verification and Consensus.<br><br>*Stack-based visualization, showing NexusEVM and NexusCore as two parallel state-machines.</p></figcaption></figure>

### Architecture Overview

Nexus Layer 1 will be made up of the following components:

* **Execution Layer:** Processes all transactions and state transitions across two synchronized execution environments
  * **NexusCore**: High-performance execution environment that hosts *enshrined co-processors* with deterministic, sub-500 ms latency for specialized financial operations.
  * **NexusEVM:**  An Ethereum-compatible virtual machine providing general-purpose programmability, composability, and full EVM tooling support for decentralized applications.
* Consensus Layer:
  * **NexusBFT:** A custom Byzantine Fault Tolerant consensus protocol that finalizes dual-execution blocks, coordinates validators, and manages the on-chain registry of co-processors.
* Verification Layer:
  * **NexuszkVM:** A verifiable compute engine that generates zero-knowledge proofs attesting to the correctness of all Layer-1 execution,
  * **NexusNetwork:** Distributed proving network where nodes contribute computational power to produce and aggregate zkVM proofs, progressively moving the system toward a single *Universal Proof* of global state.

This unified system will enable users to build and access institutional-grade financial infrastructure onchain, with sub-second latency, shared native liquidity, and cryptographic proof of correctness, bringing the speed, depth, and reliability of traditional markets into a verifiable and composable blockchain environment.

<figure><img src="https://1928578818-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fmi9nUlZMKVkCp0Tab0VD%2Fuploads%2F5aBoOFkDXlAJzSuvsetC%2F2.png?alt=media&#x26;token=a7b8a514-43b0-4be7-bb46-1b5facc68556" alt=""><figcaption><p>Each layer is independently optimizable, and co-designed for high end-to-end performance.<br><br>*Stack-based visualization, showing each of the three layers in the Nexus blockchain <br>as independently optimizable, yet co-designed, components.</p></figcaption></figure>

### Product Overview

* **Perpetual futures** – the Alpha release for the Nexus Exchange offers perpetuals trading&#x20;
* **High-performance APIs -** Nexus will offer native trading APIs for submitting trades to the Exchange&#x20;
* **High-throughput, low latency** – order matching will be handled inside NexusCore, the Exchange coprocessor engine, for CEX-like speed with onchain security guarantees
* **The Internet Exchange -** spot, perps, options, RWAs, treasuries, FX, and other verifiable finance products and assets will roll out in subsequent product releases


# Nexus Exchange Alpha

#### Nexus Exchange Alpha

The Nexus Exchange Alpha will be live at app.nexus.xyz/trade on Testnet, providing users with early access to explore the platform's features in a risk-free environment. This is the Alpha version of the Nexus Exchange. We actively encourage community feedback and engagement to help shape the product's evolution.<br>

The Nexus Exchange Alpha features a test environment to trade BTC-USD perpetual futures contracts with up to 50x leverage.

#### Architecture

The current Nexus Layer 1 Testnet represents an early Alpha release of the network. It is designed to demonstrate the foundational architecture and experience that will be core to the Nexus ecosystem. However, not all planned features are available at this stage. Many components will be progressively introduced over the coming months as performance and feedback are validated.<br>

This environment should be considered experimental and subject to rapid iteration. Performance characteristics, APIs, and system parameters may change without notice during this phase.

<figure><img src="https://1928578818-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fmi9nUlZMKVkCp0Tab0VD%2Fuploads%2FAhS929Yd6wwME6QzL9eV%2F5.png?alt=media&#x26;token=dbd03af8-1dd7-465a-9c0a-218c6a2ea114" alt=""><figcaption><p>The Exchange Engine within NexusCore sits at the core of the Layer-1 and provides the center of all liquidity.<br><br>*Equivalent stack-based visualization, showing NexusEVM and NexusCore as two composable state-machines, <br>with NexusCore and the Nexus Exchange being shown at the center to highlight their central role in the Nexus Layer-1.</p></figcaption></figure>

### Onboarding Flow

#### Gain Access

Access codes will be released in tranches to the Nexus community, and interested users of the Exchange. Sign up to the waitlist at [app.nexus.xyz/trade](http://app.nexus.xyz/trade). You will be notified via email when you are assigned an access code.

#### Testnet USDX

Testnet USDX is an ERC-20 token on Nexus Layer 1 Testnet that enables trading on the DEX, and via the Exchange. Testnet USDX has no monetary value.

**Claim Testnet USDX**

You can claim Testnet USDX at app.nexus.xyz/trade . Get 500 USDX on your first claim. Claim 50 USDX once every 24h from NexusOS during the Alpha.

#### Explore Resources

We will release educational materials on our blog and socials over the coming weeks.

### Disclaimers

The Nexus Exchange Alpha is not available to users located in, residents of, or accessing the service from regions subject to sanctions by the U.S. Office of Foreign Assets Control ("OFAC") or other applicable sanctions regimes. Additionally, Nexus reserves the right to block access to the Nexus Exchange Alpha in jurisdictions where such access would violate applicable laws or regulations, including but not limited to jurisdictions that prohibit or restrict access to digital asset trading platforms or decentralized exchange services.

Nexus reserves the right to implement additional geographic restrictions as required by law, regulation, or compliance considerations, and may block access from additional jurisdictions without prior notice. Users are solely responsible for ensuring their use of the Nexus Exchange Alpha complies with all applicable laws and regulations in their jurisdiction.

By accessing or using the Nexus Exchange Alpha, you represent and warrant that you are not located in, a resident of, or accessing the service from any restricted jurisdiction.

### Support

For questions, feedback, or bug reports, join the Nexus discord server!

<br>


# NexusCore

NexusCore will be the high-performance, specialized execution environment within the Nexus Layer 1. NexusCore is designed for financial primitives that demand deterministic performance and sub-100 ms latency. It will host *enshrined co-processors;* native execution engines built directly into the protocol that provide the performance and extensibility that give rise to new kinds of high-frequency trading, lending, payments, and other markets and market operations.

### Overview

Traditional smart contract environments like the EVM are flexible but limited by latency and gas constraints. NexusCore will extend the capability of an EVM Layer 1 by introducing engines optimized for specialized financial workloads.

Each co-processor will be an independent state machine with its own logic, memory, and data models, enabling CEX-level performance while part of a decentralized and transparent on-chain ecosystem.

**Key characteristics**

* Deterministic execution across validators
* Resource isolation for consistent performance
* Native protocol integration (enshrined within consensus)
* Dual interfaces for both EVM contracts and external systems

<figure><img src="https://1928578818-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fmi9nUlZMKVkCp0Tab0VD%2Fuploads%2FgjODU6ptEUONHbFz1Aud%2F4.png?alt=media&#x26;token=c7b242ab-4fe5-461d-99a2-e52010fe84b4" alt=""><figcaption><p>NexusCore is home to extensible, special-purpose, execution cores.</p></figcaption></figure>

### Architecture

#### Co-Processor Model

A *co-processor* will be a native module integrated into NexusCore to perform a specific category of financial computation. Unlike contracts that interpret bytecode, co-processors will execute pre-compiled logic with direct access to protocol resources.

Each will operate through three layers of state management:

| Layer             | Function                                                                                   |
| ----------------- | ------------------------------------------------------------------------------------------ |
| **State Layer**   | Maintains isolated data structures and deterministic state transitions                     |
| **Machine Layer** | Executes specialized algorithms for the co-processor’s function                            |
| **I/O Layer**     | Manages dual interfaces — native APIs and EVM precompiles — for cross-domain communication |

<figure><img src="https://1928578818-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fmi9nUlZMKVkCp0Tab0VD%2Fuploads%2FjnLdcYfJ6O9gxnpuHyre%2F8.png?alt=media&#x26;token=bbac8d31-6dcb-4632-ae83-d8c3e790ad0a" alt=""><figcaption><p>Co-processors within NexusCore, such as the Exchange Engine, <br>are independent state-machines enshrined directly into the blockchain.<br><br>Each co-processor is isolated and independently executable, parallelizable, and optimizable.</p></figcaption></figure>

#### State Machine Independence

Every co-processor in NexusCore will operate independently but under shared consensus validation, via NexusBFT. State isolation, modular execution, and resource separation allow:

* Parallel processing across co-processors
* Safe upgrades and new module introduction
* Consensus safety and determinism under load

### Dual Interface Architecture

Co-processors will be accessed via:

* **Native APIs:** enabling direct, low-latency off-chain integration (e.g., through REST or WebSocket endpoints).
* **EVM Precompiles:** allowing on-chain smart contracts to trigger co-processor functions atomically within a single transaction.

This dual access model will enable *both high-frequency trading strategies and DeFi composability* to coexist within the same network.

<figure><img src="https://1928578818-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fmi9nUlZMKVkCp0Tab0VD%2Fuploads%2FuUsOsFhprYMKHvqJ3En7%2F3.png?alt=media&#x26;token=2e6c5f7d-b338-4268-8b8f-baa2e2026d6a" alt=""><figcaption><p>The Execution Layer is comprised of a parallel dual-core architecture, <br>featuring both general-purpose and special-purpose financial state-machines.</p></figcaption></figure>

### Core Example: Exchange Co-Processor

The first co-processor implemented in NexusCore will be the **Exchange**, a high-performance perpetual futures exchange integrated directly into the Layer 1. <br>

The Nexus Exchange will feature:

* Performance capabilities exceeding 100,000 orders per second
* Real-time risk management and liquidation mechanisms
* CCXT-compatible APIs for migrating existing trading infrastructure
* On-chain EVM precompiles for composable DeFi integrations

### Modular Expansion

NexusCore will support a modular co-processor ecosystem, enabling incremental growth of Layer 1 capabilities through the expansion of NexusCore.

<figure><img src="https://1928578818-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fmi9nUlZMKVkCp0Tab0VD%2Fuploads%2F8b9EKPlGF7RPqbd1MZ8y%2F7.png?alt=media&#x26;token=e0d60baf-f633-4b26-aef1-7ba345edb00f" alt=""><figcaption><p>NexusCore: A Modular Exchange Engine — Enabling Verifiable Markets for Anything<br><br>NexusCore’s co-processor architecture enables developers to deploy permissionless, revenue-generating DEXs for any asset class — leveraging shared engines for margining, risk, and order execution to compose high-frequency financial applications within NexusEVM.</p></figcaption></figure>


# NexusEVM

NexusEVM will be the general-purpose execution environment of the Nexus Layer 1. It will maintain full Ethereum compatibility while integrating natively with NexusCore and a dual-block architecture.\
NexusEVM will provide developers with a familiar toolchain but will operate within a system capable of sub-second block times and atomic integration with high-frequency co-processors. This system is designed to marry the capabilites of specialized and general-purpose computation in one unified environment.

### Architecture

#### EVM Compatibility

NexusEVM will adhere to the Ethereum Virtual Machine standard:

* Same contract bytecode and gas semantics
* Compatible with standard RPCs and developer tools
* Supports Solidity and Vyper contract deployment without modification

This will ensure that existing Ethereum contracts can migrate directly onto Nexus with minimal refactoring.

#### Dual Execution Integration

In the dual execution model, NexusEVM will operate in parallel with NexusCore. Contracts deployed on NexusEVM will be able to call Core-level co-processors through EVM precompiles or cross-domain messages.

**Cross-domain guarantees**

* **Atomicity:** If either side fails, the transaction reverts globally
* **Determinism:** Ordered processing ensures consistent state transitions across validators
* **Predictability:** EVM block intervals occur deterministically (every 4–10 Core blocks)

#### Developer Experience

Developers on NexusEVM will be able to:

* Build standard EVM contracts and integrate with NexusCore co-processors via library precompiles
* Compose financial logic that leverage the speed and liquidity of Core modules
* Use familiar deployment flows with added access to native on-chain APIs and cross-domain event hooks

### Role in the System

NexusEVM will provide the expressive layer of the Nexus architecture. While NexusCore will deliver raw execution power, NexusEVM will ensure programmability, composability, and developer accessibility, allowing any contract to interact with financial co-processors and verifiable computation through atomic cross-domain transactions.

<figure><img src="https://1928578818-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fmi9nUlZMKVkCp0Tab0VD%2Fuploads%2FtK3Sdcw4Vznd2mNwRErt%2F9.png?alt=media&#x26;token=b2057354-8c15-4bc9-8f96-08aad2f5c2cb" alt=""><figcaption><p>NexusCore capabilities are accessible to NexusEVM applications, enabling developers <br>to compose and extend NexusCore with custom logic</p></figcaption></figure>


# Dual-Block Execution

### Dual-Block Execution

To achieve predictable performance, NexusCore will participate in a dual-block architecture:

* NexusCore blocks will execute continuously at 50–100 ms intervals for real-time trading and risk operations.
* NexusEVM blocks will occur every 4–10 Core blocks, providing synchronization and composability between NexusCore and NexusEVM.

This scheduling will ensure that NexusCore operations never wait for EVM overhead, maintaining deterministic latency across financial workloads.

<figure><img src="https://1928578818-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fmi9nUlZMKVkCp0Tab0VD%2Fuploads%2FXw9RXWHQi0nPP0ks1adY%2F10.png?alt=media&#x26;token=947e214d-6e30-400f-aee3-9af22438a84d" alt=""><figcaption><p>To achieve high performance, Nexus introduces a high-frequency dual-block architecture. <br>It features fast NexusCore mini-blocks providing high-frequency and low-latency orderbook transactions, <br>and slower NexusEVM blocks featuring the full programmability of the EVM.</p></figcaption></figure>

### Benefits

* Sub-100 ms latency for trading and risk computation
* Parallelized throughput scaling with hardware cores
* Native economic integration with validator and fee rewards
* Composable APIs bridging high-frequency execution with programmable contracts

NexusCore will transform the base chain into a verifiable financial engine, capable of supporting institutional-grade market infrastructure on-chain.


# Perpetuals

Perpetual futures on the Nexus Exchange will be fully onchain, high-performance derivative markets built directly into the Nexus Layer 1.

Perpetual futures are derivative contracts that track the price of an underlying asset without requiring ownership of the asset itself. Traders gain continuous exposure by posting collateral, opening a leveraged position, and paying or receiving funding depending on market conditions.

These markets allow traders to take leveraged long or short positions on supported assets without expirations, while benefiting from deterministic execution, transparent accounting, and cryptographic verifiability at every step.

Unlike traditional perpetual DEXs that simulate a decentralized exchange on top of a general-purpose VM, Nexus will integrate financial primitives *natively at the protocol layer*. Matching, liquidation, margining, and funding rate calculations will run inside **NexusCore**, a high-throughput co-processor suite designed specifically for Internet-scale markets.

{% content-ref url="perpetuals/margining" %}
[margining](https://docs.nexus.xyz/exchange-layer-1/trading/perpetuals/margining)
{% endcontent-ref %}

{% content-ref url="perpetuals/order-types" %}
[order-types](https://docs.nexus.xyz/exchange-layer-1/trading/perpetuals/order-types)
{% endcontent-ref %}

{% content-ref url="perpetuals/positions" %}
[positions](https://docs.nexus.xyz/exchange-layer-1/trading/perpetuals/positions)
{% endcontent-ref %}

{% content-ref url="perpetuals/funding-rates" %}
[funding-rates](https://docs.nexus.xyz/exchange-layer-1/trading/perpetuals/funding-rates)
{% endcontent-ref %}

{% content-ref url="perpetuals/liquidations" %}
[liquidations](https://docs.nexus.xyz/exchange-layer-1/trading/perpetuals/liquidations)
{% endcontent-ref %}

{% content-ref url="perpetuals/price-oracles" %}
[price-oracles](https://docs.nexus.xyz/exchange-layer-1/trading/perpetuals/price-oracles)
{% endcontent-ref %}


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


# Order Types

Orders are instructions to buy or sell assets at specified conditions. They define what, when, and how trades should execute on the exchange.

Nexus will support a diverse range of order types and configurations:

* **Market:** Executes immediately against resting liquidity; any unfilled size is canceled.
* **Limit:** Placed at a specific price and stays on the order book until filled or cancelled. Filled at selected limit price or better
  * GTD (Good-Till-Date): Stays live until the chosen expiry or when the order fills.
  * IOC (Immediate-or-Cancel): Fills what it can instantly, cancels the rest.
* **Stop:**
  * Stop Market: A market order that is executed at the best market price when mark price reaches selected market price
  * Stop Limit: A limit order that is only executed at selected limit price after mark price reaches selected trigger price.
* **Market close orders:** Automatically-size to fully close your current position, canceling any resting or untriggered orders before closing automatically.
* **Reduce-only orders:** Ensures the order can only decrease your current open position size.
  * Limit: Limit reduce-only orders automatically adjust if a subsequent order reduces your current position


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


# Funding Rates

Funding rates are a core mechanism in perpetual futures markets designed to keep the price of the perpetual contract aligned with its underlying spot index. On Nexus, funding will be computed and settled natively inside the **NexusCore** Exchange Co-processor, ensuring deterministic, transparent, and protocol-level enforcement of payments between longs and shorts.

#### How Funding Works

Funding reflects the **basis** between the perpetual mid-price and the underlying index price:

* **Positive funding** → longs pay shorts
* **Negative funding** → shorts pay longs

Each market will display its current hourly funding rate at the top of the trading interface.

#### Timing and Frequency

Nexus will use the EVM block height schedule to approximate hourly funding intervals during the Exchange Alpha. As the network progresses through mainnet phases, the cadence becomes increasingly consistent due to more stable block timing and a maturing dual-block architecture.

* **Funding accrues continuously throughout the hour**
* **Settlement occurs at the end of each hourly window**

All calculations and settlements will occur within NexusCore.

#### Implementation

The Nexus Exchange funding mechanism will charge roughly every hour, with the calculation period spanning the full hour and settlement occurring at the end of each hour.&#x20;

**Basis Calculation**

The system will calculate the basis (premium or discount) by comparing the market's mid-price (average of best bid and ask) with the underlying spot price provided by Nexus' oracle.

$$
basis = \frac{\text{mid\_price} - \text{spot\_price}}{\text{spot\_price}}
$$

These samples will be taken at fixed intervals to capture representative market conditions.

**Rate Determination**

At the end of each hour, the collected basis measurements will be averaged to form the hourly rate.&#x20;

For positive rates:

$$
rate=min⁡(clamp(average\_basis)+baseline\_rate,cap)
$$

For negative rates:

$$
rate=max⁡(clamp(average\_basis)+baseline\_rate,−cap)
$$

**Settlement Logic**

Funding payments are exchanged between longs and shorts based on the final computed rate:

* Positive Funding (Market Trading Above Index)
  * Longs pay shorts proportional to position size, rate, and index price
* Negative Funding (Market Trading Below Index)
  * Shorts pay longs using the same proportional model

All settlements will occur atomically within the Core block processing the end-of-interval boundary.


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


# Spot

*Coming Soon.*


# Vaults

*Coming soon.*


# Introduction

### Introduction

Nexus is a Layer 1 blockchain purpose-built to support the next generation of verifiable, high-performance computation. Nexus introduces a new network architecture where execution, consensus, and verification operate as coordinated layers of a single, scalable system.

At its foundation, the Nexus Network unifies compute from nodes around the world into one verifiable system state. Every node contributes to processing, validating, and ultimately proving the chain’s execution. Over time, this network will evolve toward the creation of a single, zero-knowledge proof that represents the complete computation of the Layer 1 — a concept referred to as the **Universal Proof**.

#### Network Purpose

The Nexus Network forms the backbone of the Nexus Layer 1 blockchain.\
It connects validators, co-processor nodes, and verifiers into a synchronized system that:

* **Processes transactions** through a dual execution layer (NexusEVM + NexusCore)
* **Secures the ledger** using NexusBFT, a custom Byzantine Fault Tolerant consensus
* **Generates cryptographic proofs** of execution through the Nexus zkVM and the distributed compute network

Together, these systems create a *planet-scale financial coordination layer* capable of running high-frequency applications that interacts with machine intelligence with extreme performance and mathematical verifiability.

#### Design Principles

The network is designed for:

* **Global unification of compute:** A single cryptographically verifiable chain aggregates the world’s compute power
* **Horizontal scaling:** Every new node increases throughput across the network
* **Vertical scaling:** Each upgrade to the Nexus zkVM enhances the system’s ability to prove complex computation
* **Autonomous coordination:** Programmatic intelligence can interact securely with assets, information and applications, autonomously
* **The Universal Proof:** All computation is compressed into a single, verifiable proof that serves as a global source of truth

![Nexus Layer 1](https://content.gitbook.com/content/PUemy5iDAcT0e1cZJm4f/blobs/GupMTR9P3o8r0cN1V4eM/NexusLayer1.png)

### The Universal Proof

The ultimate goal of Nexus is to achieve the Universal Proof. This is a breakthrough in trustless computing where:

* All verifiable computation is compressed into a single, succinct proof
* Chains, agents, and applications on Nexus are integrated into one coherent system
* Nexus transforms into a global, verifiable supercomputer, where performance, verifiability and accessibility converge

### Why Proofs Matter

In a world increasingly run by opaque algorithms and black-box AI systems, cryptographic proofs help us move from assumptions to guarantees. Zero-knowledge proofs (ZKPs) let one party prove that a computation was performed correctly, without revealing the inputs or repeating the work. This unlocks a new primitive for a verifiable internet: trust in computation itself, secured by cryptography.

With ZKPs, we can:

* Prove that smart contracts executed correctly
* Verify off-chain work from on-chain environments
* Build systems that are private and provable

Nexus makes this real at scale. It turns zero-knowledge proofs from theoretical research into practical infrastructure.

### The Nexus 1.0 Whitepaper

The foundational vision for the Nexus zkVM, the Nexus Network, and the search for a verifiable Internet is outlined in the Nexus zkVM 1.0 whitepaper:\
<https://whitepaper.nexus.xyz> (published January 2024)


# System Overview

## System Overview

Nexus is a Layer 1 blockchain that integrates high-performance execution, deterministic consensus, and verifiable computation into a unified protocol architecture.&#x20;

The system will be structured as a three-layer model (Execution, Consensus, and Verification) which cleanly separates runtime computation from block production and long-term trust minimization.

### Three-Layer Architecture

#### Execution Layer

The execution layer will consist of two parallel state machines:

* **NexusEVM** — an Ethereum-compatible environment for general-purpose smart contracts, and composable application development.
* **NexusCore** — a high-performance runtime hosting *enshrined co-processors*, each implemented as an independent, deterministic state machine optimized for specialized financial operations.

Both environments will execute concurrently and communicate via atomic cross-domain message passing, ensuring a single, globally consistent execution state across **NexusEVM, NexusCore** and **Cross-Domain** states. &#x20;

This dual-execution model will resolve the programmability–performance trade-off by allowing developers to retain full EVM flexibility while leveraging CEX-grade computational paths for latency-sensitive logic.

#### Consensus Layer

The **NexusBFT** protocol will finalize blocks, validates execution commitments, and governs the activation and evolution of co-processors.&#x20;

Each block will contain:

* A Merkle commitment to the execution state
* Validator signatures and metadata
* Optional registry updates that modify the set of active co-processors via **CPregistry**

Nexus will enable protocol-level extensibility without hard forks or execution-layer disruption, by placing co-processor registration and lifecycle management in the consensus layer.

#### Verification Layer

The verification layer will provide trustless validation of the entire chain through the **Nexus zkVM**, a zero-knowledge virtual machine.&#x20;

The **Nexus Network** will generate these proofs, progressively compressing chain execution into a single recursive Universal Proof. This architecture enables horizontally scalable validation where even low-resource devices can independently verify the chain.

### Design Goals

The system is engineered to achieve:

* **High-frequency execution:** Sub-100 ms Core latency and sub-second EVM confirmation.
* **Composable programmability:** Seamless integration between general smart contracts and specialized co-processors.
* **Deterministic coordination:** Predictable block timing and atomic cross-domain operations.
* **Progressive verifiability:** zkVM integration enables recursive proof aggregation for full-chain validation.
* **Scalable decentralization:** Performance scales with hardware and validator participation, not fragmentation across rollups.

### Summary

Nexus will unify execution, consensus, and verifiable computation into a single architecture capable of delivering high-performance financial computation with mathematically provable correctness. By embedding verifiability directly at the base layer and enabling deterministic, parallel execution through co-processors, Nexus will provide a foundation for globally scalable applications, markets, and autonomous agents


# FAQ

### Getting Started

<details>

<summary><strong>What is Nexus?</strong></summary>

Nexus is building a Layer 1 blockchain for the AI era – a world supercomputer that gets more powerful with each connected device. Nexus makes it easy for anyone to contribute compute power from any device, even a laptop or phone. With just one click, users can connect at [app.nexus.xyz](https://app.nexus.xyz) to start earning rewards and help scale a verifiable network built for the AI economy.

</details>

<details>

<summary><strong>What are the Nexus Testnet and Nexus Devnet?</strong></summary>

Testnet is the public testing environment for the Nexus ecosystem. When available, Devnet is a public-facing environment used for testing under development features.

There have been several testnets and one devnet so far:

* **Testnet 0:** October 8 – 28, 2024
* **Testnet I:** December 9 – 13, 2024
* **Testnet II:** February 18 – 22, 2025
* **Devnet:** February 23 - June 22, 2025
* **Testnet III:** Started June 23, 2025

</details>

<details>

<summary><strong>Can I participate in the Nexus testnet?</strong></summary>

Yes, anyone can participate by creating and logging into a Nexus account at [app.nexus.xyz](https://app.nexus.xyz) or by registering a CLI node at [app.nexus.xyz/nodes](https://app.nexus.xyz/nodes) and running the Nexus CLI with that node id. In doing so, your device becomes a node, contributing compute power to the network.

Nexus is designed to scale verifiable computation through a unique architecture where our servers assign workloads—programs and inputs to be proved—to each connected node. Every node operates a Nexus zero knowledge virtual machine (zkVM), which uses cryptographic techniques to verify computations.

Unlike other blockchains, the Nexus testnet gets more powerful with each connected device, so your contributions matter.

</details>

<details>

<summary><strong>Why should I contribute compute power?</strong></summary>

By participating in the Nexus testnet, you're helping develop and test a world supercomputer to make the internet verifiable – where every action can be proven, every AI model audited, and every interaction verified.

Users play an essential role in helping develop and test the Nexus ecosystem. They equip the Nexus blockchain with the speed and scalability required to support AI systems at global scale.

Also, if you log in to your Nexus account, you can earn rewards, such as points and tokens, for your contributions. More on that below.

</details>

<details>

<summary>How do I create a Nexus account?</summary>

To create a Nexus account, simply follow the steps to connect your email or wallet. Once your account is set up and you connect to the network, you'll automatically start earning NEX Testnet Points and appearing on leaderboards.

</details>

<details>

<summary><strong>Can I use multiple devices to contribute compute power?</strong></summary>

You can link and manage multiple devices including desktops, laptops, mobile phones, and servers all from a single account. There's no need to create separate accounts for each device. You can even prove computations in multiple browser tabs at once, with each tab utilizing one CPU core.

</details>

<details>

<summary><strong>What is happening when I am contributing compute power?</strong></summary>

Your device proves computations in the form of software programs assigned by Nexus's server. These computations verify the integrity of each program. Here's what happens step by step:

1. Your device connects to the Nexus network, and runs its own instance of the zkVM.
2. The Nexus network sends a program and its input data to your device.
3. The Nexus zkVM, which is running on your device, executes the program, generating a proof.
4. Your proof is submitted to the network, along with performance metrics.
5. Your account will earn rewards such as points and tokens for your contributions. More on this below in Points and Tokens.
6. The process repeats as long as your device remains connected.

</details>

<details>

<summary><strong>What's the difference between connecting my device through the Nexus web app and running the CLI from my device terminal?</strong></summary>

Logging into a Nexus account at app.nexus.xyz enables users to contribute compute power from their device to the network effortlessly via a web browser—with no technical knowledge required. It is also the main dashboard for managing and overseeing all your contributions across devices. The Command Line Interface (CLI) is designed for more advanced users running provers on dedicated machines looking to customize compute power contribution by device.

</details>

<details>

<summary><strong>Can I buy a pre-installed prover from a third-party provider?</strong></summary>

Yes, there are a number of third-party providers that provide one-click setup to users. However, because these are third-party vendors, Nexus will not be able to provide assistance with setup or troubleshooting.

</details>

<details>

<summary><strong>What is the maximum amount of nodes I can create?</strong></summary>

Users cannot create more than 100 existing nodes. Delete existing nodes or create a new account if you need more than 100. Users are rate limited to creating 50 nodes per day.

</details>

### Nexus Exchange Alpha

<details>

<summary><strong>What is the Nexus Exchange Alpha?</strong></summary>

The Nexus Exchange Alpha is Nexus's testing environment for decentralized exchange functionality, allowing users to test trading, liquidity provision, and other exchange features using testnet tokens with no real economic value.

</details>

<details>

<summary><strong>How do I access the Nexus Exchange Alpha?</strong></summary>

Nexus Exchange Alpha access may be provided through your existing Nexus account at [app.nexus.xyz](http://app.nexus.xyz) or through separate Exchange-specific interfaces. Specific access instructions will be provided when the Nexus Exchange Alpha becomes available.

</details>

<details>

<summary><strong>Can I use real money or tokens in the Nexus Exchange Alpha?</strong></summary>

No. The Nexus Exchange Alpha uses only testnet tokens with no monetary value. No real assets can be traded or at risk in the Nexus Exchange Alpha environment.

</details>

<details>

<summary><strong>What happens to my Nexus Exchange Alpha positions?</strong></summary>

All Nexus Exchange Alpha positions, test tokens, and trading history are temporary and for testing purposes only. They may be reset, modified, or eliminated at any time without notice.

</details>

<details>

<summary><strong>Are there rewards for Nexus Exchange Alpha participation?</strong></summary>

Nexus Exchange Alpha may include its own reward system separate from compute testnet rewards. Any such rewards are for testing purposes only and have no monetary value.

</details>

### Points and Tokens

<details>

<summary><strong>What are NEX Testnet Points and NEX Testnet Tokens?</strong></summary>

NEX Testnet Points and NEX Testnet Tokens are Nexus's native reward system for recognizing user and developer participation during testnet phases.

</details>

<details>

<summary><strong>How do I earn NEX Testnet Points and NEX Testnet Tokens?</strong></summary>

Once Testnet III begins, logged in users will begin to earn NEX Testnet Points for contributing compute power, and will be able to claim NEX Testnet Tokens from the NEX Testnet Points they earn. The ratio of NEX Testnet Points to NEX Testnet Tokens may vary during Testnet III. The system is for testing purposes only and is subject to change.

* NEX Testnet Points and NEX Testnet Tokens during Testnet III are distinct from those accumulated in earlier testnets and devnets.
* To view NEX Testnet Points from previous testnets, log in to your Nexus account with the original email that you used to register.

Users cannot use NEX Testnet Points from previous testnets to claim NEX Testnet Tokens during Testnet III.

In the future, you may be able to earn points and tokens in a variety of other ways through your on-going participation in the Nexus ecosystem.

</details>

<details>

<summary><strong>What are NEX Devnet Points and NEX Devnet Tokens?</strong></summary>

NEX Devnet Points and NEX Devnet Tokens are Nexus's native reward system for recognizing user and developer participation during a devnet phase. The system is for testing purposes only and is subject to change.

Once Testnet III begins, current NEX Devnet Points and NEX Devnet Tokens will reset so that users can begin earning NEX Testnet Points and NEX Testnet Tokens.

</details>

<details>

<summary><strong>How do I earn NEX Devnet Points and NEX Devnet Tokens?</strong></summary>

You can earn NEX Devnet Points and NEX Devnet Tokens by contributing compute power via the Nexus web app or Nexus CLI during a devnet period. Like other devnet activity, these points and tokens may not be tracked.

</details>

<details>

<summary><strong>What happened to my previous NEX Devnet Points and NEX Testnet Tokens?</strong></summary>

Once Testnet III begins, prior NEX Devnet Points and NEX Testnet Tokens will reset so that users can begin earning NEX Testnet Points and NEX Testnet Tokens.

</details>

### Troubleshooting

<details>

<summary><strong>Is the Nexus devnet or testnet stable?</strong></summary>

The Nexus devnet and testnet are currently undergoing testing, and stability improvements are ongoing. Bugs may occur and should not cause alarm. The goal of the devnet and testnet is to eliminate bugs before the mainnet is up and running. We appreciate community feedback to help improve and refine the system.

</details>

<details>

<summary><strong>What should I do if I run into issues?</strong></summary>

Most issues can be resolved easily by yourself. Try two simple steps:

1. Clear your browser cache and try again.
2. Check the [docs for the CLI](https://docs.nexus.xyz/layer-1/network-devnet/cli-node) and try again. If neither of these steps help, we're here to support you on Discord.

</details>

<details>

<summary><strong>Where can I report bugs or issues?</strong></summary>

Submit bug reports on our [GitHub](https://github.com/nexus-xyz/) repositories, or ask a question on Discord. If you rented a node from a third-party service, please reach out to their support channels directly. If you receive a private message through any social media (Telegram, Discord, etc.) claiming to be support, it will be a scam.

</details>

<details>

<summary><strong>Will you send me a friend request, private message, or direct message if I ask for help on your Discord server? / Will I receive a response to my request for help as a "ticket" in direct or private messages?</strong></summary>

NO. If you receive a private message through any social media (Telegram, Discord, etc.) claiming to be support, it will be a scam.

</details>

<details>

<summary><strong>My third-party prover node is not working / I'm having trouble getting my third-party prover node to work with my dashboard-generated node-id.</strong></summary>

Because these are third-party vendors, Nexus will not be able to provide assistance with setup or troubleshooting. You will need to ask your vendor for support. Please make sure you use their official support site/contact; if you receive a private message through any social media (Telegram, Discord, etc.) claiming to be support, it will be a scam.

</details>

### Privacy & Security

<details>

<summary><strong>What personal information do you collect, and how is it used?</strong></summary>

When you first connect, your device is assigned a random identifier to track proving activity. This identifier ensures continuity in tracking your device's contributions. If you prefer unlinked proofs, reset your identifier in the settings. For more details, see our [Terms of Use](https://nexus.xyz/terms-of-use) and [Privacy Policy](https://nexus.xyz/privacy-policy).

</details>

<details>

<summary><strong>Is my computer and data safe while connected to the Nexus network?</strong></summary>

Yes. The Nexus CLI and Nexus zkVM code is open-source and available on [GitHub](https://github.com/nexus-xyz/). The Nexus web app runs in a sandboxed instance of the Nexus zkVM inside your browser.

</details>

### Getting Involved

<details>

<summary><strong>How do I join the Nexus community?</strong></summary>

Nexus community is active on Discord and Telegram. Join us to connect with builders, get support, and stay up to date on Testnet III and beyond. Make sure to read the community guide and explore the channels!

</details>

<details>

<summary><strong>Does the Nexus community have a role or ambassador system? How does it work?</strong></summary>

Yes! Nexus has a community role and contribution system designed to recognize and reward meaningful involvement. Roles are assigned based on your activity and contribution. Ambassadors are trusted community leaders who help grow and support regional and interest-based groups. You can find the full guide in the #roles channel on Discord.

</details>

<details>

<summary><strong>How can I partner with Nexus or contribute to the Nexus ecosystem?</strong></summary>

If you are a project interested in partnership or collaboration opportunities, reach out to the Nexus team at <growth@nexus.xyz>

</details>


# Network Information

### Welcome to the Nexus Layer 1

Nexus Layer 1 is designed to be familiar and accessible to Ethereum developers. If you’ve built on Ethereum before, you’re already equipped to build on Nexus. Our platform is fully EVM-compatible, which means you can use all your existing tools, libraries, and code without any modifications.

### Network Configuration

| Property        | Value                                 |
| --------------- | ------------------------------------- |
| Chain ID        | `3945`                                |
| Native Token    | Nexus (NEX)                           |
| RPC (HTTP)      | `https://testnet.rpc.nexus.xyz`       |
| RPC (WebSocket) | `wss://testnet.rpc.nexus.xyz`         |
| Explorer        | `https://testnet.explorer.nexus.xyz/` |
| Faucet          | `https://faucet.nexus.xyz`            |

***


# Nexus Layer 1 Testnet III

This page covers Nexus Layer 1 Testnet, the current testing environment for the Nexus Network.

### Testnet III Overview

**Testnet III is now live** and represents the current phase of Nexus testing. This testnet focuses on security, decentralization, and orchestration testing.

### How Testnet III Works

In Testnet III, users earn **NEX Testnet III Points** by proving via Nexus OS or CLI and then **claim** them to convert them into **NEX Testnet III Tokens**.

#### Proving via Nexus OS or CLI

When you start to prove via Nexus OS or CLI, you will earn NEX Testnet III Points.

Because Testnet III is a new environment, you will start with 0 Testnet III Points and earn them through proving.

![NEX Testnet III Points](https://content.gitbook.com/content/PUemy5iDAcT0e1cZJm4f/blobs/0zBIBAyPj9hQMFfKTAAA/home%20page%20points.png)

#### Nexus OS wallet

The Nexus OS wallet will show NEX Testnet III Tokens.

![NEX Testnet III Tokens](https://content.gitbook.com/content/PUemy5iDAcT0e1cZJm4f/blobs/G0yu2h4s2fU1QNzxxAx9/dynamic%20wallet%20tokens.png)

### Accessing Historical Data

#### Viewing Historical Points

Users can view their historical data in the rewards page: <https://app.nexus.xyz/rewards>, including previous testnet records.

![Historical rewards data](https://content.gitbook.com/content/PUemy5iDAcT0e1cZJm4f/blobs/POR96dpzK61BZyKxHimK/rewards.png)

### Network Info

| Property        | Value                                  |
| --------------- | -------------------------------------- |
| Chain ID        | `3945`                                 |
| Native Token    | Nexus Token (NEX)                      |
| RPC (HTTP)      | `https://testnet.rpc.nexus.xyz`        |
| RPC (WebSocket) | `wss://testnet.rpc.nexus.xyz`          |
| Explorer        | `https://nexus.testnet.blockscout.com` |
| Faucet          | `https://faucet.nexus.xyz`             |

### Useful Links

* [Testnet III Explorer — Track transactions and network activity on Testnet III](https://testnet3.explorer.nexus.xyz/)
* [Testnet III Faucet — Get test tokens for Testnet III](https://faucets.alchemy.com/faucets/nexus-testnet)


# Contribute via Web App

## Introduction

**Testnet III is now live.** This is the current testing environment for Nexus Layer 1, focusing on security, decentralization, and orchestration testing.

The Nexus App — [app.nexus.xyz](https://app.nexus.xyz/) — provides a browser-based way to contribute compute to the Nexus Network. No installation required.

Under the hood, the Nexus App runs a high-performance Rust-based WebAssembly (WASM) runtime, allowing users to contribute computation securely and efficiently with a single click — directly from their browser. There’s no technical setup or prior knowledge required.

The web app also serves as the primary dashboard for managing all aspects of your participation:

* Start or stop compute contribution with one toggle.
* Track your NEX Points in real time.
* Manage linked CLI nodes and wallets.
* Redeem rewards and monitor leaderboard performance.

![Web nodes connecting to Nexus](https://2905424450-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FPUemy5iDAcT0e1cZJm4f%2Fuploads%2FjchG54Z9aDdYhSgBxVwP%2FWebApp.png?alt=media\&token=c8d9551b-a263-4440-b641-06cfb220eb9f)

## Proving Options

* Link to Nexus Account (Recommended)
* Anonymous Proving

{% stepper %}
{% step %}

### Create an Account

Go to [app.nexus.xyz](https://app.nexus.xyz/) and sign up. You’ll automatically receive a built-in wallet. You can also add MetaMask or other wallets.
{% endstep %}

{% step %}

### Start Contributing

Flip the toggle switch to begin contributing compute and earning points.
{% endstep %}
{% endstepper %}

#### Why link your account?

* Automatically generate a wallet tied to your Nexus identity.
* Earn NEX Points for your contributions.
* Track your performance on the global leaderboard.
* Manage all your browser and CLI nodes from one dashboard.

## Benefits of Web-Based Contribution

* **Zero Setup**\
  Start contributing without downloads or manual configuration.
* **Cross-Platform Access**\
  Participate from any device with a modern browser — desktop, laptop, or tablet.
* **WASM-Powered Performance**\
  Leverages a Rust-compiled WebAssembly runtime to maximize compute efficiency in the browser.
* **Full Dashboard Control**\
  Monitor, manage, and scale your contributions — all from a single interface.

## Need Help?

<details>

<summary>Support and questions</summary>

Have questions or need assistance? Reach out to our team on [Discord](https://discord.com/invite/nexus-xyz).

</details>


# Contribute via CLI

### Introduction

The [Nexus Network CLI](https://github.com/nexus-xyz/nexus-cli) is a command-line tool for contributing compute resources to the network.

![CLI nodes connecting to Nexus](https://content.gitbook.com/content/PUemy5iDAcT0e1cZJm4f/blobs/tuG5hSYQ04XzARtWDIzi/cli%20tui.png)

### Install Script

Quick install (scripted):

```
curl https://cli.nexus.xyz/ | sh
```

After installing, restart or refresh your terminal (e.g. `source ~/.bashrc`, `source ~/.zshrc`, etc.). To start with an existing node ID:

```
nexus-network start --node-id <your-node-id>
```

Alternatively, register your wallet address and create a node ID with the CLI, or at [app.nexus.xyz](https://docs.nexus.xyz/network/proving-on-the-layer-1/broken-reference):

```
nexus-network register-user --wallet-address <your-wallet-address>
nexus-network register-node
nexus-network start
```

The `register-user` and `register-node` commands will save your credentials to `~/.nexus/credentials.json`. To clear credentials, run:

```
nexus-network logout
```

### Setup & Configuration

{% stepper %}
{% step %}

### Initial setup

1. Run the CLI for the first time.
2. Accept the [Terms of Use](https://nexus.xyz/terms-of-use).
3. Choose between anonymous or linked proving (see the next step).
   {% endstep %}

{% step %}

### Choose proving mode

You have two options:

* Link to Nexus Account (Recommended)
  * Create an account at [app.nexus.xyz](https://app.nexus.xyz/).
  * Follow the account linking instructions.
  * Your contributions will earn NEX Points.
  * Track your progress on the leaderboard.
  * Manage all your nodes in one place.

To earn NEX Points, you must link your CLI to your Nexus account. Anonymous proving will not record contributions.
{% endstep %}
{% endstepper %}

### Troubleshooting

<details>

<summary>Known issues &#x26; help</summary>

* If you have previously proved with an older version of the CLI, you must run the install script for the new CLI, as the versions are not backwards compatible. Proofs submitted by the old CLI will not receive rewards in Testnet III.
* Check Documentation:
  * Search existing [GitHub Issues](https://github.com/nexus-xyz/nexus-cli/issues).
* Get Help:
  * Join our [Discord](https://discord.gg/nexus-xyz)
  * [Open a new GitHub issue](https://github.com/nexus-xyz/nexus-cli/issues/new) for technical problems

</details>

***

Related:

* Contribute via Web App: <https://docs.nexus.xyz/layer-1/testnet/web-node>
* FAQ: <https://docs.nexus.xyz/layer-1/testnet/faq>


# Points and Tokens

NEX Testnet Points and NEX Testnet Tokens are Nexus’s native reward system for recognizing user and developer participation during testnet phases. The system is for testing purposes only and is subject to change.

* NEX Testnet Points and NEX Testnet Tokens during Testnet III are distinct from those accumulated in earlier testnets and devnets.
* To view NEX Testnet Points from previous testnets, log in to your Nexus account with the original email that you used to register.
* Users cannot use NEX Testnet Points from previous testnets to claim NEX Testnet Tokens during Testnet III.
* In the future, you may be able to earn points and tokens in a variety of other ways through your on-going participation in the Nexus ecosystem.

<details>

<summary><strong>What are NEX Testnet Points and NEX Testnet Tokens?</strong></summary>

NEX Testnet Points and NEX Testnet Tokens are Nexus’s native reward system for recognizing user and developer participation during testnet phases.

</details>

<details>

<summary><strong>How do I earn NEX Testnet Points and NEX Testnet Tokens?</strong></summary>

Once Testnet III begins, logged in users will begin to earn NEX Testnet Points for contributing compute power, and will be able to claim NEX Testnet Tokens from the NEX Testnet Points they earn. The ratio of NEX Testnet Points to NEX Testnet Tokens may vary during Testnet III.

</details>

<details>

<summary><strong>Why did my points go to 0 on June 24?</strong></summary>

Your NEX Testnet Points are safe and still being tracked. All of your NEX Testnet Points, both claimed and unclaimed, have been converted to NEX Testnet Tokens and transferred to your wallet. As a result, all claimed and unclaimed NEX Testnet Points will show up as 0 in your claim history.

* All points earned before 3:00 PM PT on June 24 have already been converted to NEX Testnet Tokens and sent to your wallet.
* Contributions made after 3:00 PM PT on June 24 are still being tracked and will appear in your account.

This is due to a maintenance update to Testnet III, and no points have been lost. No action is needed on your part.

</details>

<details>

<summary><strong>What are NEX Devnet Points and NEX Devnet Tokens?</strong></summary>

NEX Devnet Points and NEX Devnet Tokens are Nexus’s native reward system for recognizing user and developer participation during a devnet phase. The system is for testing purposes only and is subject to change.

Once Testnet III begins, current NEX Devnet Points and NEX Devnet Tokens will reset so that users can begin earning NEX Testnet Points and NEX Testnet Tokens.

</details>

<details>

<summary><strong>How do I earn NEX Devnet Points and NEX Devnet Tokens?</strong></summary>

You can earn NEX Devnet Points and NEX Devnet Tokens by contributing compute power via the Nexus web app or Nexus CLI during a devnet period. Like other devnet activity, these points and tokens may not be tracked.

</details>

<details>

<summary><strong>What happened to my previous NEX Devnet Points and NEX Testnet Tokens?</strong></summary>

Once Testnet III begins, prior NEX Devnet Points and NEX Testnet Tokens will reset so that users can begin earning NEX Testnet Points and NEX Testnet Tokens.

</details>


# The Nexus zkVM

![](https://3435725530-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FLJ85JA3XlaU4USdPDSkb%2Fuploads%2FSiQoM7hcMaTD6C7qrMpo%2Fnexus-github_network_zkvm.png?alt=media\&token=987b3462-8464-43fa-af1d-08b42b39c23e)

The Nexus zero-knowledge virtual machine is a modular, extensible, prover-optimized, fully-specified zkVM written in Rust, focused on performance and security. [Nexus zkVM v0.3.6](https://github.com/nexus-xyz/nexus-zkvm/releases/tag/v0.3.6) is the current stable release, implementing the [Nexus zkVM 3.0 machine](https://docs.nexus.xyz/zkvm/specifications/the-complete-specification).

## What is the Nexus zkVM?

Nexus zkVM is a [zero-knowledge virtual machine](https://docs.nexus.xyz/zkvm/overview/zkvm-overview) that enables developers to generate succinct proofs for any computation, demonstrating that a program executed every instruction and accessed memory correctly to produce a given output. Built with Rust and focused on performance and security, it provides a robust foundation for building applications.

## Proving Computation

The Nexus zkVM can generate proofs for any computation. For example, given a Rust program that calculates the Fibonacci sequence:

{% code title="fib.rs" %}

```rust
#![cfg_attr(target_arch = "riscv32", no_std, no_main)]

use nexus_rt::println;

fn fib(n: u32) -> u32 {
    match n {
        0 => 0,
        1 => 1,
        _ => fib(n - 1) + fib(n - 2),
    }
}

#[nexus_rt::main]
fn main() {
    let n = 7;
    let result = fib(n);
    assert_eq!(result, 13);
    println!("fib({}) = {}", n, result);
}
```

{% endcode %}

the zkVM can generate a succinct, efficiently verifiable proof of its correct execution. To get started with the Nexus zkVM, check out the [Getting Started](https://docs.nexus.xyz/zkvm/development/getting-started) page.

{% hint style="warning" %}
The Nexus zkVM is in an experimental stage and is not currently recommended for production use.
{% endhint %}

## Key Features

### Security First

* The Nexus zkVM provides fully-specified cryptographic components with careful analysis of security and performance.
* The system includes no code obfuscation, no proprietary components, and no closed-source code.
* Source-available transparency ensures complete auditability for all users.

### Performance Optimized

* The prover-optimized architecture enables efficient proof generation across diverse workloads.
* Sensible defaults are configured to work out of the box without complex setup requirements.

### Developer Friendly

* Developers can write programs with execution proven to be correct.
* A comprehensive SDK and tooling ecosystem supports rapid development and deployment.
* Extensive documentation and examples guide users through implementation details.

### Extensible & Modular

* The system supports new languages, new precompiles, and new provers as the state-of-the-art advances.
* Configurable components prevent vendor lock-in and allow customization for specific use cases.
* Source-available code and consistent development by the Nexus zkVM team ensure long-term reliability.

## The Nexus Ethos: Assurance through Open Science

We believe a zkVM must provide an efficient proving mechanism without compromising on security and correctness. A zkVM cannot provide transparency without being transparent itself. Every component of a zkVM should be powered by fully and publicly specified cryptographic components, with careful analysis of security and performance. The Nexus zkVM features no code obfuscation, no proprietary components, and no closed-source code.

## Modular and Extensible Architecture

Built with a modular architecture at its core, the Nexus zkVM features independently optimized components that integrate smoothly. The system ships with carefully chosen defaults for the prover and memory model, allowing developers to start building immediately while maintaining confidence in both security and performance across diverse applications.

Extensibility is a fundamental design principle of the Nexus zkVM. The codebase and active development by the Nexus team ensures continuous evolution, supporting emerging languages, advanced precompiles, and cutting-edge proving systems as the field progresses—all without locking developers into proprietary solutions.

## Use Cases

The Nexus zkVM enables a wide range of applications:

* **Verifiable Computation**: Prove correct execution of any program
* **Privacy-Preserving Applications**: Compute on sensitive data without revealing it
* **Blockchain Scaling**: Generate proofs for off-chain computation
* **Compliance & Auditing**: Provide cryptographic guarantees for regulatory requirements
* **Trustless Systems**: Build applications that don’t require trusted intermediaries

## Getting Started

{% stepper %}
{% step %}

### Quick Start Guide

Get up and running in minutes: <https://docs.nexus.xyz/zkvm/proving/overview>
{% endstep %}

{% step %}

### SDK Documentation

Comprehensive API reference: <https://docs.nexus.xyz/zkvm/proving/sdk>
{% endstep %}

{% step %}

### Architecture Overview

Understand how it works: <https://docs.nexus.xyz/zkvm/architecture>
{% endstep %}

{% step %}

### Example Walkthroughs

Learn through practical examples: <https://docs.nexus.xyz/zkvm/walkthroughs/galeshapley>
{% endstep %}
{% endstepper %}

***

*Experience the future of verifiable computation with Nexus zkVM - where transparency meets performance.*


# zkVM Overview

Zero-Knowledge Virtual Machines (zkVMs) represent an approach to verifiable computation, enabling developers to generate cryptographic proofs that a computation was executed correctly.

## What is a zkVM?

A zero-knowledge virtual machine is a system that can execute programs and generate succinct, verifiable proofs of their correct execution. These proofs demonstrate that a program executed every line of code and accessed memory correctly, culminating in the expected output. Unlike traditional virtual machines that simply run code, zkVMs produce cryptographic evidence that the computation was performed accurately according to the specified program logic.

This fundamental capability transforms how we approach trust in computing. Instead of relying on individual parties or infrastructure to validate computations, zkVMs enable any computation execution to be independently verified. This opens up entirely new possibilities for preserving privacy and ensuring computational integrity across distributed networks.

## Key Concepts

### Zero-Knowledge Proofs

Succinct proofs of correct execution are cryptographic proofs that allow a prover to convince a verifier that a certain computation was performed correctly — without the verifier having to redo the computation themselves. These proofs are typically non-interactive, publicly verifiable, and much smaller and faster to verify than re-executing the original computation.

A zero-knowledge proof is a special type of such proof that reveals nothing beyond the correctness of the statement itself. That is, it allows the verifier to be convinced that the computation was carried out correctly, without learning anything about the inputs, intermediate steps, or any other private data.

Example: For an example of a zero-knowledge proof, see this description of Schnorr’s: <https://www.zkdocs.com/docs/zkdocs/zero-knowledge-protocols/schnorr/>

### Succinct Verification

zkVM proofs are “succinct,” meaning they can be verified much faster than re-executing the original computation. A proof for a program that takes hours to run can often be verified in milliseconds.

### Universal Computation

Modern zkVMs are designed to handle arbitrary computations, not just specific mathematical operations. This means developers can write programs in familiar languages and generate proofs for complex business logic.

## How zkVMs Work

{% stepper %}
{% step %}

### Program Execution

The zkVM executes a program step-by-step, tracking all operations and state changes and recording the computational trace.
{% endstep %}

{% step %}

### Proof Generation

The trace is converted into a cryptographic proof using advanced techniques like STARKs, SNARKs, or other proof systems.
{% endstep %}

{% step %}

### Verification

Anyone can verify the proof to confirm the correctness of the trace is proven.
{% endstep %}
{% endstepper %}

## Applications of zkVMs

### Privacy-Preserving Computation

Sensitive computations can be proven correct without revealing private inputs, enabling applications in healthcare, finance, and personal data processing. See walkthroughs at Gale-Shapley and Lambda Calculus:

* <https://docs.nexus.xyz/zkvm/walkthroughs/galeshapley>
* <https://docs.nexus.xyz/zkvm/walkthroughs/lambdacalculus>

### Verifiable AI/ML

Machine learning models can generate proofs of their inference results, ensuring AI decisions are transparent and auditable.

### Compliance and Auditing

Organizations can prove compliance with regulations or internal policies without exposing sensitive business data.

### Blockchain Scaling

zkVMs enable Layer 2 scaling solutions by allowing complex computations to be performed off-chain while maintaining on-chain verifiability.

***

*Zero-knowledge virtual machines are transforming how we think about computation, privacy, and trust in digital systems.*

Further reading:

* The Nexus zkVM: <https://docs.nexus.xyz/zkvm/nexus-zkvm>
* Architecture: <https://docs.nexus.xyz/zkvm/architecture>


# Architecture

The ethos of the Nexus project is a commitment to open and transparent science and engineering. For an in-depth look at the science behind the Nexus zkVM, see the [specification](https://docs.nexus.xyz/zkvm/specifications/the-complete-specification).

### Core Components

The Nexus zkVM features a modular and extensible architecture built from highly optimized components:

* **The Nexus Runtime**: A feature-rich runtime environment that streamlines guest program development for the Nexus zkVM, with full support for public and private inputs, public outputs, logging, and performance benchmarking — all in native Rust syntax.
* **The Nexus zkVM Machine Architecture**: A custom designed and from-scratch implemented and purpose-built RISC-V virtual machine in a modified Harvard architecture, designed to optimize prover performance through careful memory management in support of a “only prove what you use” model.
* **The Nexus zkVM**: A fully-specified Algebraic Intermediate Representation (AIR) arithmetization of the machine architecture, featuring comprehensive constraints for the full RISC-V32im instruction set alongside efficient offline memory checking.
* **The Stwo Prover:** An integration with StarkWare’s powerful [Stwo prover](https://github.com/starkware-libs/stwo) (which has since rebranded from Stwo to S-two), a state-of-the-art Circle STARK with excellent performance characteristics.

Every component within the Nexus zkVM has been carefully chosen or designed from scratch by the [Nexus team](https://nexus.xyz/aboutus) to maximize security, performance, modularity, and extensibility.

As a consequence of the architectural foundation, the Nexus zkVM is architected to support new theoretical developments led by our research team, as well as tooling to accelerate deploying the zkVM for a variety of use cases:

* **Proving Schemes**: Beyond the Stwo prover, the Nexus zkVM maintains compatibility with the Nova family of folding schemes and supports integration of emerging proving constructions as cryptographic research advances.
* **Precompiles**: Precompiles are extensions to the instruction set of the machine architecture, supporting common operations (e.g., cryptographic hashing like Keccak, or matrix multiplication) that the zkVM can use to accelerate specific computations. Developers will be able to extend the zkVM with their own custom precompiles, as well as import those published by other developers.
* **Developer Tooling:** The Nexus zkVM comes with a comprehensive SDK that streamlines application development with APIs that enable efficient development workflows regardless of use case complexity.
* **Language Support**: As the Nexus zkVM implements RISC-V ISA, the zkVM can run programs written in most high-level languages (e.g., Rust, C++, etc.) given its common availability as a computation target.

The zkVM aims to offer developers out-of-the-box prover performance and security, designed to power numerous applications.

### Proving Architectures

The Nexus zkVM turns programs into proofs, but the computational work of executing and proving the zkVM must be implemented by a proving architecture. The Nexus zkVM’s flexible design supports diverse proving architectures, ranging from local sequential execution on personal devices to the massively parallel [Nexus Network](https://docs.nexus.xyz/layer-1/vision/network), a globally-distributed proving infrastructure currently in active development.

Related:

* [zkVM Overview](https://docs.nexus.xyz/zkvm/overview/zkvm-overview)
* [Getting Started](https://docs.nexus.xyz/zkvm/development/getting-started)


# Getting Started

The Nexus zkVM provides both a comprehensive runtime for streamlined program development and a powerful SDK for configuring, executing, and generating proofs for your applications.

{% hint style="info" %}
Recommended starting points:

* SDK Quick Start — step-by-step guidance to begin proving with the Nexus zkVM.
* Runtime — guidance for writing guest programs for the zkVM and developing host programs to manage the proving process.
  {% endhint %}

## Key resources

* <a href="sdk-quick-start" class="button primary">SDK Quick Start</a>
* <a href="runtime" class="button primary">Runtime</a>

Additional references:

* SDK Documentation: <https://docs.nexus.xyz/zkvm/proving/sdk-docs>
* Benchmarking your host project: <https://docs.nexus.xyz/zkvm/proving/sdk-benchmarking>
* Integrating Precompiles: <https://docs.nexus.xyz/zkvm/proving/precompiles>

(Links preserved with original query parameters and targets.)


# SDK Quick Start

The Nexus SDK provides simple, misuse-resistant programmatic use of the Nexus zkVM.

{% stepper %}
{% step %}

### Install the Nexus zkVM

First, install Rust: <https://www.rust-lang.org/tools/install>. Next, install the RISC-V target:

{% code title="Install RISC-V target" %}

```bash
$ rustup target add riscv32i-unknown-none-elf
```

{% endcode %}

Then, install the Nexus zkVM:

{% code title="Install cargo-nexus (v0.3.4)" %}

```bash
$ rustup run nightly-2025-05-09 cargo install --git https://github.com/nexus-xyz/nexus-zkvm cargo-nexus --tag 'v0.3.6'
```

{% endcode %}

And verify the installation:

{% code title="Verify installation" %}

```bash
$ rustup run nightly-2025-05-09 cargo nexus --help
```

{% endcode %}

This should print the available CLI commands. At present, the `cargo nexus` CLI is minimal, providing just a `cargo nexus host` command to setup an SDK based project.
{% endstep %}

{% step %}

### Create a new Nexus host project

To use the zkVM programmatically, you need two programs: a guest program that runs on the zkVM, and a host program that operates the zkVM. Create the project with:

{% code title="Generate host project" %}

```bash
$ rustup run nightly-2025-05-09 cargo nexus host nexus-host
```

{% endcode %}

This will create a new Rust project directory with the following structure:

{% code title="Project structure" %}

```
./nexus-host
├── Cargo.lock
├── Cargo.toml
├── rust-toolchain.toml
└── src
    ├── main.rs
    └── guest
        ├── Cargo.toml
        ├── rust-toolchain.toml
        └── src
            └── main.rs
```

{% endcode %}

Here, `./src/main.rs` is the host program, while `./src/guest/src/main.rs` is the guest program.

Replace `./src/guest/src/main.rs` with this guest program (takes two integers, one public and one private, logs values, returns their product):

{% code title="src/guest/src/main.rs" %}

```rust
#![cfg_attr(target_arch = "riscv32", no_std, no_main)]

use nexus_rt::println;

#[nexus_rt::main]
#[nexus_rt::public_input(x)]
fn main(x: u32, y: u32) -> u32 {
    println!("Read public input:  {}", x);
    println!("Read private input: {}", y);

    x * y
}
```

{% endcode %}

Then replace `./src/main.rs` with this host program (compiles guest, invokes it with public input x = 5 and private input y = 3, reads output and logs, and verifies the proof):

{% code title="src/main.rs" %}

```rust
use nexus_sdk::{
    compile::{cargo::CargoPackager, Compile, Compiler},
    stwo::seq::Stwo,
    ByGuestCompilation, Local, Prover, Verifiable, Viewable,
};

const PACKAGE: &str = "guest";

fn main() {
    println!("Compiling guest program...");
    let mut prover_compiler = Compiler::<CargoPackager>::new(PACKAGE);
    let prover: Stwo<Local> =
        Stwo::compile(&mut prover_compiler).expect("failed to compile guest program");

    let elf = prover.elf.clone(); // save elf for use with test verification

    print!("Proving execution of vm... ");
    let (view, proof) = prover
        .prove_with_input::<u32, u32>(&3, &5)
        .expect("failed to prove program"); // x = 5, y = 3

    assert_eq!(view.exit_code().expect("failed to retrieve exit code"), nexus_sdk::KnownExitCodes::EXIT_SUCCESS as u32);

    let output: u32 = view
        .public_output::<u32>()
        .expect("failed to retrieve public output");
    assert_eq!(output, 15); // z = 15

    println!("output is {}!", output);
    println!(
        ">>>>> Logging\n{}<<<<<",
        view.logs().expect("failed to retrieve debug logs").join("")
    );

    print!("Verifying execution...");
    proof
        .verify_expected::<u32, u32>(
            &5,   // x = 5
            nexus_sdk::KnownExitCodes::EXIT_SUCCESS as u32,
            &15,  // z = 15
            &elf, // expected elf (program binary)
            &[],  // no associated data,
        )
        .expect("failed to verify proof");

    println!("  Succeeded!");
}
```

{% endcode %}

This host program compiles the guest, runs the zkVM with supplied inputs, retrieves output and logs, and verifies the proof of correct execution.
{% endstep %}

{% step %}

### Run your program

Run the host program (which executes and proves the guest program) with:

{% code title="Run host" %}

```bash
$ cargo run -r
```

{% endcode %}

You should see output similar to:

{% code title="Expected output" %}

```
Proving execution of vm... output is 15!
>>>>> Logging
Read public input:  5
Read private input: 3
<<<<<
Verifying execution...  Succeeded!
```

{% endcode %}

For more examples using the SDK with more complicated guest programs, see the walkthroughs for Gale-Shapley stable matching and the lambda calculus:

* <https://docs.nexus.xyz/zkvm/walkthroughs/galeshapley>
* <https://docs.nexus.xyz/zkvm/walkthroughs/lambdacalculus>
  {% endstep %}

{% step %}

### Run in legacy mode

In addition to the Stwo-based Nexus zkVM 3.0 prover, the SDK supports a legacy mode that uses the Nova, HyperNova, and (experimental) Jolt-based Nexus zkVM 2.0 machine. This machine uses a different runtime and requires additional host-side configuration due to public parameters and reference strings.

To use legacy mode, activate the appropriate feature for the `nexus-sdk` dependency in the host program: `legacy-nova`, `legacy-hypernova`, or `legacy-jolt`. Examples of using legacy mode to prove legacy guest programs are provided in the examples folder on GitHub:

* Legacy guest examples: <https://github.com/nexus-xyz/nexus-zkvm/tree/main/examples/legacy/src>
* SDK examples: <https://github.com/nexus-xyz/nexus-zkvm/tree/main/sdk/examples>

The legacy-mode code corresponds to the Nexus zkVM v0.2.4 release:

* <https://github.com/nexus-xyz/nexus-zkvm/tree/releases/0.2.4>
  {% endstep %}
  {% endstepper %}


# SDK Documentation

The Nexus zkVM SDK documentation is available at:

* <https://sdk-docs.nexus.xyz/doc/nexus_sdk/index.html>


# Runtime

## What’s a Runtime?

In the vast majority of modern software development, a developer never writes code that directly interacts with the platform it’s running on. Instead, the platforms for which developers write code offer runtimes: easy-to-use (and often standardized) APIs that provide high-level functionality while abstracting away most platform-specific details. Prominent examples include POSIX and `glibc`. Runtimes also provide controlled and abstracted access to platform-specific functionality that developers do need access to, which is especially relevant for the Nexus zkVM.

## The Nexus Runtime

The zkVM runtime environment is most similar to a bare-metal or embedded environment, though it has properties specific to being a zkVM. As is typical for embedded platforms, interaction with the platform (zkVM) is done via raw `ecall`s, custom instructions, and memory-mapped I/O. Uniquely to zkVMs, however, [the memory model changes fundamentally between executions of the same guest program](https://docs.nexus.xyz/zkvm/overview/architecture) (see the aside below). The Nexus runtime is a set of libraries and macros that allows developers to write higher-level programs that can run efficiently and correctly on the Nexus zkVM, agnostic to the subtleties of the zkVM’s varying executions.

{% hint style="info" %}
Aside: the zkVM’s first pass uses a Harvard-like architecture with distinct memory spaces for code, data, inputs, and output. During the first pass, the zkVM collects statistics about exactly how much memory is used in each of these spaces. Before the second pass, the zkVM lays out the program’s memory in a single address space whose size is minimized based on the statistics collected during the first pass. Because proving memory is expensive, this process significantly reduces proof sizes and proving times. The second pass maintains memory protections but uses a single address space for all memory segments.
{% endhint %}

More specifically, the Nexus runtime consists of a few parts:

* Macros that allow developers to work easily with input and output, which are memory-mapped and directly managed by the zkVM.
* A `main` macro that ensures the guest program’s `main` function can be correctly located and run by the zkVM.
* `print!` / `println!` macros that write to an output log, implemented by the zkVM via an `ecall`.
* A `#[panic_handler]`, required by Rust’s `core`, implemented by the zkVM via an `ecall`.
* A `#[global_allocator]` that operates correctly across the zkVM’s memory models.
* An assembly entry point for the program that configures zkVM-specific global state and calls the guest program’s `main` function; this ensures stack, heap, and input/output segments are usable during both passes of execution.
* Well-known locations that correspond to particular memory-mapped values provided or read by the zkVM.

The rest of this section discusses these components in more detail and with examples. For even more detail, see [the VM specification](https://docs.nexus.xyz/zkvm/specifications/the-complete-specification).

### Notable Macros & Functions

#### Main

The `nexus_rt::main` attribute marks the entry point of the guest program. It is a procedural macro that:

* Ensures that the main function can be located and run by the runtime’s entry-point assembly by re-exporting the main function with a non-mangled, well-known name referenced by the runtime’s entry-point assembly.
* Generates code that automatically reads in all inputs and writes to the output. Unless specified otherwise, inputs default to private.
* Re-orders the function’s attributes to ensure that input type specifications are evaluated before the `main` macro generates code that reads them.

Example use:

```rust
#[nexus_rt::main]
fn main(x: u32, y: u32) -> bool {
    x > y
}
```

The `main` macro also handles the program’s public output, which is simply the value returned from `main`. The macro internally uses the `write_public_output` function to serialize the output and write it to the output tape. The public output is written by the Nexus runtime’s `write_public_output`, which is a function that serializes the program’s output in a [COBS](https://en.wikipedia.org/wiki/Consistent_Overhead_Byte_Stuffing) representation [generated by](https://docs.rs/postcard/latest/postcard/fn.to_allocvec_cobs.html) [`postcard`](https://crates.io/crates/postcard).

The serialized bytes are written to the output tape using the Nexus runtime’s `write_output!(byte_index, value)` macro, which writes a byte-addressed word to the output tape by:

{% stepper %}
{% step %}
Read the public output address from well-known location `PUBLIC_OUTPUT_ADDRESS_LOCATION`.
{% endstep %}

{% step %}
Add `byte_index` to that address.
{% endstep %}

{% step %}
Emit a `wou` instruction, whose behavior depends on zkVM execution mode:

* In the zkVM’s first pass (Harvard-like architecture), `wou` writes the word to a unique memory address space that only contains public output.
* In the second pass, the zkVM replaces the binary’s `wou` instructions with ordinary `sw` instructions that write the output values from a location calculated and populated by the zkVM using data collected from the first pass.
  {% endstep %}
  {% endstepper %}

#### Public Input

Public inputs are input values known to the verifier, specified as arguments to `#[nexus_rt::main]` and tagged with `#[nexus_rt::public_input]`.

Example use:

```rust
#[nexus_rt::main]
#[nexus_rt::public_input(x)]
fn main(x: u32, y: u32) -> bool {
    x > y
}
```

In this example, `x` is a public input while `y` is private.

Public inputs are read by the Nexus runtime’s `read_public_input`, which reads the entire public input tape and [deserializes](https://docs.rs/postcard/latest/postcard/fn.from_bytes_cobs.html) it from a [COBS](https://en.wikipedia.org/wiki/Consistent_Overhead_Byte_Stuffing) representation [produced by](https://docs.rs/postcard/latest/postcard/fn.to_allocvec_cobs.html) [`postcard`](https://crates.io/crates/postcard).

The serialized bytes are read using the Nexus runtime’s `read_input!(byte_index)` macro, which reads a byte-addressed word from the serialized public input by:

{% stepper %}
{% step %}
Read the public input address from well-known location `PUBLIC_INPUT_ADDRESS_LOCATION`.
{% endstep %}

{% step %}
Add `byte_index` to that address.
{% endstep %}

{% step %}
Emit a `rin` instruction, whose behavior depends on zkVM execution mode:

* In the zkVM’s first pass (Harvard-like architecture), `rin` reads the word from a unique memory address space which only contains public input.
* In the second pass, the zkVM replaces the binary’s `rin` instructions with ordinary `lw` instructions that read the input values from a location calculated and populated by the zkVM using data collected from the first pass.
  {% endstep %}
  {% endstepper %}

#### Private Input

Private inputs are input values known only to the prover. They are specified as arguments to `#[nexus_rt::main]` and optionally tagged with `#[nexus_rt::private_input]`. Arguments default to being private, but developers can explicitly mark them private for clarity.

Example use:

```rust
#[nexus_rt::main]
#[nexus_rt::private_input(y)]
fn main(x: u32, y: u32) -> bool {
    x > y
}
```

In this example, both `x` and `y` are private inputs.

Private inputs are read by the Nexus runtime’s `read_private_input`, which sequentially reads a single byte from the private input tape via an `ecall`, returning `None` after each byte has been read once. The runtime provides no further special handling for private inputs; guest program developers are expected to handle the interpretation of the private input tape themselves.

#### Host-Native Execution

It is often useful to run and debug guest programs in a native environment (e.g., `cargo run`). The Nexus runtime itself cannot run outside the zkVM, but its macros support native handlers—functions compiled and executed only when the guest program is run natively on the host. These functions generate inputs and handle outputs without the zkVM’s presence.

Example:

```rust
#![cfg_attr(target_arch = "riscv32", no_std, no_main)]

#[cfg(not(target_arch = "riscv32"))]
fn native_input_handler() -> Option<u32> {
    let mut input = String::new();

    std::io::stdin().read_line(&mut input).ok()?;

    Some(input.trim().parse().ok()?)
}

#[cfg(not(target_arch = "riscv32"))]
fn native_output_handler(output: &u32) -> Option<()> {
    println!("Output: {}", output);

    Some(())
}

#[nexus_rt::main]
#[cfg_attr(target_arch = "riscv32", nexus_rt::public_input(x))]
#[cfg_attr(not(target_arch = "riscv32"), nexus_rt::custom_input(x, native_input_handler))]
#[cfg_attr(not(target_arch = "riscv32"), nexus_rt::custom_input(y, native_input_handler))]
#[cfg_attr(not(target_arch = "riscv32"), nexus_rt::custom_output(native_output_handler))]
fn main(x: u32, y: u32) -> u32 {
    x ^ 0xdeadbeef
}
```

This allows running the program natively to ensure correctness without relying on the zkVM’s limited debugging capabilities.

#### Functionality in a `no_std` Environment

The Nexus zkVM has no operating system and cannot implement large portions of the Rust standard library, so guest programs must be `no_std`. To help developers, the Nexus runtime implements particular parts of the Rust runtime:

* A simple global allocator and implementations for `panic` and `abort`, as required by `core`.
* Simple `print!` and `println!` implementations that wrap zkVM-specific system calls for logging.

In the future, the team plans to enable `std` for the Nexus zkVM where appropriate by gating functionality dependent on an operating system or incompatible with provable computation. For example, there are no plans to enable multi-threading or general I/O, but certain `std` functionality useful for the zkVM (e.g., some system calls like `exit`, algorithms, and data structures) may be supported.

### Memory Allocation

The Nexus runtime implements a simple allocator required for any data structures that rely on heap allocations (i.e., those in `alloc`). Currently, it uses a naive bump allocator that allocates bottom-up and never deallocates.

## Assumptions

Despite the conveniences offered by the Nexus runtime, there are still some requirements for guest programs:

* The guest program must depend on `nexus-rt` and provide a `nexus_rt::main`-decorated function as the entry point. Without these, the zkVM can’t properly load the program and behavior is undefined.
* The guest program must be annotated with `no_std` and `no_main` when compiled for the zkVM (i.e., for a `riscv32` target architecture).
* The guest program’s code must be position-independent (compiled with `-fPIC`).

The Nexus `cargo` CLI tool ensures these requirements are met for projects it creates; initializing projects with it is highly recommended.

Further reading:

* [SDK Documentation](https://docs.nexus.xyz/zkvm/development/broken-reference)
* [Precompiles](https://docs.nexus.xyz/zkvm/development/precompiles)


# Precompiles

## Introduction

**Precompiles** are custom extensions to the zkVM’s instruction set that accelerate complex operations most efficiently proved by custom circuits.

As a concrete example, consider [Keccak](https://keccak.team/keccak_specs_summary.html), which implements SHA-3 and is used prominently in some blockchains. The Keccak family of hash functions is optimized for performance on real CPUs—they make extensive use of bitwise operations that conventional CPUs can perform efficiently and in parallel. For current zkVM backends, however, proving a round of a Keccak hash function as a sequence of assembly instructions is quite expensive—that sequence of assembly instructions is long, and bitwise operations are each individually complex to express and expensive to constrain. Using a precompile, we can specifically design a monolithic, optimized circuit for proving a round of a Keccak hash function, potentially saving orders of magnitude in proving time for that operation. As it turns out, many common cryptographic and mathematical operations lend themselves to this kind of optimization.

Actually integrating precompiles into the zkVM is a complex task, however. Guest programs need to be able to use precompiles as if they were standard Rust libraries, and the VM needs to be able to seamlessly provide precompile evaluations to the guest and constraints to the prover. The rest of this documentation is concerned with how the Nexus zkVM actually achieves this.

## Architecture

Above all, the Nexus zkVM is designed to make guest program development as easy as possible. This means that, from the perspective of a developer writing a guest program, using precompiles should be just as easy as using any other Rust library. Using Keccak256 as a concrete example, we want developers to be able to write code like the following:

```rust
use_precompile!(nexus_keccak::Keccak256);

#[nexus_rt::public_input(x)]
#[nexus_rt::main]
fn main(x: &[u8]) -> [u8; 32] {
    Keccak256::hash(x)
}
```

Save for using the `use_precompile!` macro instead of the standard `use` statement, the guest program looks exactly as it would if it were using a standard Rust library. The guest program’s author needs no knowledge whatsoever about how precompiles work to use them correctly and efficiently.

This naturally requires trade-offs. Here, the precompile’s developer takes on the burden of ensuring that their precompile is able to provide a usable interface to the precompile’s functionality. The zkVM tooling provides a set of macros and library functions that make this as easy as possible for precompile developers, but precompile development is a much more advanced task than guest program development.

Consequently, the rest of this document primarily targets precompile developers and advanced users.

### Precompile Instructions

The atom of the Nexus zkVM is the RISC-V `RV32` assembly instruction, each of which the zkVM emulates and proves. A primary characteristic of a modern assembly language like RISC-V is that its instruction set is simple and minimal, making extensions to the instruction set something that needs to be approached carefully.

Fortunately, custom instructions are common, and RISC-V makes provisions for them. Specifically, there are two ways that the RISC-V ISA is designed to be extensible: syscalls (via `ecall`) and custom instructions with reserved opcodes.

We chose to use reserved custom instructions for precompiles. This is primarily because, conceptually, precompiles are *not* syscalls; their purpose is not to interact with the host environment in any particular way. Instead, they are simply a way to extend the functionality of the zkVM, which matches the intended use of reserved custom instructions by the RISC-V specification. These custom instructions make up the `RV32Nexus` extension to the `RV32` ISA, which, in addition to supporting third-party precompiles, will include a set of vetted and optimized first-party precompiles that address common use-cases.

This approach, however, creates some issues. System calls are fundamentally dynamic—one specifies desired behavior by setting register values, and there is only a single `ecall` instruction. As we use them, though, custom instructions, which are static in nature, also need to be dynamic in practice; we cannot simply reserve an instruction for every precompile in our ecosystem. Were we to do that, our ecosystem could only tolerate a small, fixed number of precompiles (1024, here), and developers would need to waste time best spent writing code and circuits fighting for a slot in the instruction set.

Our solution to this problem is multi-fold. At the moment, we have constrained Nexus precompiles to a single opcode (`0x0B`) reserved by the RISC-V specification—technically, this opcode is only reserved by the RISC-V specification for the 32- and 64-bit instruction sets, but, fortunately, Nexus has no plans to ever develop a 128-bit-addressed zkVM. We chose for instructions using this opcode to be R-type. A precompile instruction, then, looks like the following:

```
|--fn7--|-rs2-|-rs1-|fn3|-rd--|0001011|
 31---25       19-15     11--7
         24-20       14        6-----0
                     -12
```

| Our Use                    | `opcode` ( `inst[6:0]`) | `rd`         | `rs1`         | `rs2`         | `imm` | `fn`                                        |
| -------------------------- | ----------------------- | ------------ | ------------- | ------------- | ----- | ------------------------------------------- |
| Dynamic R-type Precompiles | `0001011`               | `inst[11:7]` | `inst[19:15]` | `inst[24:20]` | N/A   | `fn3 = inst[14:12]` and `fn7 = inst[31:25]` |

We generate concrete instructions via a procedural macro, which, for each precompile call, ultimately generates a corresponding custom instruction roughly as follows:

```rust
fn precompile_call<const FN3: u8, const FN7: u8>(rs1: u32, rs2: u32) -> u32 {
    let insn = format!(
        ".insn r 0x{R_TYPE_PRECOMPILE_OPCODE:x}, \
        0x{fn3:x}, 0x{fn7:x}, {{rd}}, {{rs1}}, {{rs2}}"
    );
    let mut rd: u32;
    unsafe {
        ::core::arch::asm!(
            ".insn r 0x0B 0x{FN3} 0x{FN7}, {rd}, {rs1}, {rs2}",
            rd = out(reg) rd,
            rs1 = in(reg) rs1,
            rs2 = in(reg) rs2,
        );
    };

    return rd;
}
```

This doesn’t precisely match our implementation (see [`precompiles/macros/src/generation.rs`](https://github.com/nexus-xyz/nexus-zkvm/blob/main/precompiles/macros/src/generation.rs) for that), but this example code is conceptually the same.

`FN3` and `FN7` are dynamically generated on a per-guest-program-compilation basis. Concretely, guest programs are limited to using no more than 1,024 precompiles, and a procedural macro is responsible for generating an integer index in `[0, 1024)` for each precompile and embedding an (index → precompile) mapping into the compiled program’s code (again, see `generation.rs` for specifics).

When the VM loads a guest program, it first uses the mapping embedded in the binary to discover which precompiles it will need to load in order to offer the guest program its desired functionality. The static reserved opcode and the mapping embedded in the guest program binary together encode all the instruction information needed for the zkVM to dynamically execute and prove the precompiles needed by a guest program.

In order to verify a proof, the verifier also has to be able to discover the precompiles used by the guest program. The verifier does this almost exactly the same as the zkVM does. The only difference is that the verifier ignores the precompile’s implementation, only verifying that the precompile’s constraints are satisfied and the same as the ones proved by the zkVM. The Nexus ecosystem ensures that the verifier is able to seamlessly access the same precompile implementations as the zkVM.

### Executing Precompiles

Precompiles are distributed as shared libraries compiled for the host’s native platform (e.g., Linux or macOS). On startup, the zkVM is configured to search for and load precompiles from a set of directories and files. Each of these is loaded into memory using the platform-appropriate dynamic library loading mechanism (e.g., `dlopen` on Unixes).

Precompile implementations adhere to the precompile interfaces specified in `nexus-precompiles` (see [`precompiles/src/traits.rs`](https://github.com/nexus-xyz/nexus-zkvm/blob/main/precompiles/src/traits.rs)). These traits mirror the traits that define native instructions as closely as possible, the only difference being that precompiles use dynamic dispatch instead of static dispatch via generics. Again, Nexus-provided macros automate exporting these implementations under well-known names which the zkVM can discover.

It's worth noting that while dynamically loaded libraries typically use the C ABI, we chose to use the Rust ABI for the time being. Nexus’ macros and zkVM implementation hide this from precompile developers and users, but there is one user-visible consequence: precompiles must be built with the same Rust version as the zkVM. This is because Rust has no ABI stability guarantees, and after precompiles stabilize, we may switch internally to the completely stable C ABI.

Upon loading a guest binary, the zkVM searches for well-known Nexus precompile symbols in that binary. If it finds any, it will construct a table mapping precompile instructions, discussed above, to the precompile implementations found in the loaded libraries. The zkVM will then use this table to dynamically dispatch precompile calls to the appropriate implementation during emulation.

### Proving Precompiles

Because precompile instructions are conceptually no different from native instructions, the zkVM’s proving process is able to integrate them easily. We need no special treatment for precompiles in the tracing process; they are simply another kind of instruction present in the trace that the emulator generates for the prover.

The prover, however, does need to be aware of precompiles in the same way that the emulator is. The same table constructed during guest binary loading is used by the prover, but instead of fetching instruction implementations, it fetches constraint circuits. The prover then uses these circuits to constrain the trace of the precompile instructions in the same way that it does for native instructions.

## Precompile Development

Because of Nexus’ choice to prioritize the precompile consumer’s experience, developing precompiles is a more advanced task than developing guest programs. This section is intended to help precompile developers understand the steps required to develop a precompile, each either on the host or guest side.

Fortunately, there are still only a few steps in developing a precompile, and Nexus provides tooling to assist with each. To create a precompile, a developer must:

{% stepper %}
{% step %}

### Implement the precompile’s functionality (host)

Write the host-side implementation that performs the operation exposed by the precompile.
{% endstep %}

{% step %}

### Create the precompile’s circuit (host)

Design and provide the constraint circuit that the prover will use to constrain traces for the precompile instruction.
{% endstep %}

{% step %}

### Provide precompile consumers with an idiomatic interface (guest)

Package a small, idiomatic Rust guest-side interface (crate) so guest programs can use the precompile like a normal library.
{% endstep %}
{% endstepper %}

The host functionality and circuit will be packaged in the precompile’s shared library, while the guest interface is packaged in a Rust crate imported by guest programs. The host implementation needs no awareness of the guest interface, and the guest interface needs no awareness of how the precompile is implemented.

### Host-Side Development

The bulk of the work necessary to create a precompile is its host-side implementation and constraint circuit. Concretely, precompile developers must write a `struct` which implements `PrecompileInstruction` (which will be specified in [`precompiles/src/traits.rs`](https://github.com/nexus-xyz/nexus-zkvm/blob/main/precompiles/src/traits.rs) once full precompile support is published). The source code for this trait (and its supertraits) is extensively documented, and for the most up-to-date guide, refer to the rustdoc for `traits.rs` and the example precompiles in `precompiles/examples`.

### Guest-Side Development

The developer work involved with creating a guest-side interface for a precompile is minimal: the developer only needs to write a single function that provides idiomatic access to the precompile’s functionality. This function has to be defined by a macro for code-generation reasons (only upon compilation will the precompile’s opcode be calculated) but is otherwise a simple wrapper around the precompile’s raw instruction.

As a concrete example, consider a simple hash. The host-side implementation and macro might write a function like the following:

```rust
impl MyHashInstruction {
    pub fn emit_instruction(rs1: u32, rs2: u32) -> u32 {
        let mut rd: u32;

        unsafe {
            ::core::arch::asm!(
                "/* inst. details */ {rd}, {rs1}, {rs2}",
                rd = out(reg) rd,
                rs1 = in(reg) rs1,
                rs2 = in(reg) rs2,
            );
        }

        return rd;
    }
}
```

Where `emit_instruction` computes the hash of `rs2` bytes starting at memory address `rs1` and writes it to `rd`. We don’t want guest program developers to have any awareness of how the underlying instruction works, so the precompile developer would write a macro like the following:

```rust
// Package: my-precompile
// File: my_precompile/src/guest.rs

#[cfg(target_arch = "riscv32")]
#[macro_export]
macro_rules! generate_instruction_caller {
    ($path:path) => {
        pub trait HashCaller {
            fn hash(data: &[u8]) -> u32;
        }

        impl HashCaller for $path {
            fn hash(data: &[u8]) -> u32 {
                let data_ptr = data.as_ptr() as u32;
                let data_len = data.len() as u32;

                Self::emit_instruction(data_ptr, data_len)
            }
        }
    };
}
```

Then, when the guest program developer wants to use the precompile, their `use_precompiles!` macro will automatically call the `generate_instruction_caller!` macro, which will generate an ad-hoc `HashCaller` trait implementation for the precompile’s instruction. The guest program developer can then use the precompile like this:

```rust
use_precompiles!(my_precompile::MyHash);

#[nexus_rt::public_input(x)]
#[nexus_rt::main]
fn main(x: &[u8]) -> u32 {
    MyHash::hash(x)
}
```

Which is exactly the kind of experience we set out to provide for guest program developers.


# Benchmarking

```bash
# Arrays for input and output
public_inputs=(0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19)
public_outputs=(1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765)

# Loop through the arrays
for i in "${!public_inputs[@]}"; do
    public_input="${public_inputs[$i]}"
    public_output="${public_outputs[$i]}"

    echo "Running with PUBLIC_INPUT=$public_input and PUBLIC_OUTPUT=$public_output"

    # Run the Rust program with environment variables set
    # Ensure the Rust program is built in release mode
    PUBLIC_INPUT=$public_input PUBLIC_OUTPUT=$public_output cargo run --release

    echo "----------------------------------------"
done
```

Results (units in milliseconds)

| n-th Fibonacci | Compile (ms) | Prove (ms) | Verify (ms) | Total Time (ms) | Proof size (bytes) |
| -------------- | -----------: | ---------: | ----------: | --------------: | -----------------: |
| 0              |          161 |       1592 |          11 |            1764 |              51968 |
| 1              |          149 |       1522 |          11 |            1684 |              51968 |
| 2              |          148 |       1514 |          11 |            1675 |              51968 |
| 3              |          151 |       1538 |          11 |            1701 |              51440 |
| 5              |          151 |       1477 |          12 |            1641 |              51968 |
| 8              |          128 |       1465 |          11 |            1606 |              46008 |
| 13             |          136 |       1454 |          11 |            1602 |              49304 |
| 21             |          138 |       1440 |          12 |            1591 |              49880 |
| 34             |          149 |       1551 |          12 |            1713 |              51968 |
| 55             |          149 |       1422 |          13 |            1584 |              51440 |
| 89             |          151 |       1432 |          12 |            1596 |              51440 |
| 144            |          153 |       1427 |          11 |            1593 |              49460 |
| 233            |          149 |       1434 |          12 |            1596 |              50384 |
| 377            |          138 |       1417 |          11 |            1567 |              50368 |
| 610            |          148 |       1453 |          11 |            1613 |              51968 |
| 987            |          150 |       1510 |          12 |            1673 |              49280 |
| 1597           |          149 |       1443 |          11 |            1604 |              50384 |
| 2584           |          146 |       1460 |          13 |            1620 |              50864 |
| 4181           |          147 |       1449 |          11 |            1610 |              51968 |
| 6765           |          149 |       1440 |          11 |            1602 |              51968 |

Observation: Proving time is roughly constant for the first 20 Fibonacci numbers — likely because zkVM setup overhead dominates while the actual Fibonacci computation is still small.

Larger inputs (around the 200th Fibonacci)

| n-th Fibonacci | Compile (ms) | Prove (ms) | Verify (ms) | Total Time (ms) | Proof size (bytes) |
| -------------- | -----------: | ---------: | ----------: | --------------: | -----------------: |
| 200            |          156 |      17416 |         189 |           17762 |              58544 |
| 201            |          154 |      17179 |         183 |           17518 |              59904 |
| 202            |          152 |      17468 |         183 |           17804 |              59248 |
| 204            |          158 |      17238 |         181 |           17579 |              59248 |
| 205            |          151 |      17242 |         184 |           17579 |              57920 |

Observation: Proving time increases substantially with input size, while verification time remains small compared to proving time.

{% stepper %}
{% step %}

### Optimize Guest Programs

Focus on minimizing RISC-V cycles in guest programs. The benchmark shows the number of RISC-V cycles directly impacts proving time, which is the dominant component of total execution time.
{% endstep %}

{% step %}

### Consider Algorithmic Efficiency

For computationally demanding scenarios, prioritize efficient algorithms and implementations. The Fibonacci example demonstrates how complexity can rapidly increase proving time.
{% endstep %}

{% step %}

### Profile Regularly

Regularly profile Nexus zkVM projects to identify performance bottlenecks and optimization opportunities.
{% endstep %}
{% endstepper %}

{% hint style="info" %}
Note: Verification time remains negligible in these benchmarks compared to proving time; optimizing the proving workload yields the largest gains.
{% endhint %}

Related links:

* <https://docs.nexus.xyz/zkvm/proving/precompiles>
* <https://docs.nexus.xyz/zkvm/walkthroughs/galeshapley>


# Use Case: Stable Matching

Every year in the United States, \~50,000 graduating medical students (doctors, for short) are placed into the residencies where they will begin their careers by the [National Resident Matching Program](https://www.nrmp.org/) (or The Match). To do so, the program finds a stable matching: an assignment of doctors to medical programs (hospitals, for short) such that there is no pair of doctor and hospital that would prefer to be assigned each other over the match(es) they ended up with. Each candidate doctor ranks their preferred hospitals and each hospital ranks their preferences in candidates, and the matching proceeds algorithmically.

One of the original problems in the field of algorithmic mechanism design, the matching program uses the [Roth-Peranson algorithm (1999)](https://www.aeaweb.org/articles?id=10.1257/aer.89.4.748), a modification of the earlier [Gale-Shapley algorithm (1962)](https://www.tandfonline.com/doi/pdf/10.1080/00029890.1962.11989827). These contributions in large part earned Roth & Shapley the 2012 Nobel Prize in Economics.

The Match is a classic example of a computation [whose transparency and accountability can benefit from private verifiable computation](https://scholarship.law.upenn.edu/penn_law_review/vol165/iss3/3/): at present, doctors receive no direct assurance that an algorithmic decision that will shape their careers (and their career earnings) is being executed correctly. However, The Match cannot simply publish a transcript of the matching, as it would harm the privacy of the doctors in particular (“Alice said she wanted to come back home for residency, but she didn’t rank any local hospitals” or “when we interviewed Bob he said fifteen years ago he ranked us highly in The Match, but he only had us seventh”). [Anonymizing the doctors can only accomplish so much](https://heinonline.org/HOL/LandingPage?handle=hein.journals/uclalr57\&div=48\&id=\&page=) as it offers only the illusion of privacy; modern re-identification techniques routinely pierce de-identified data. As a result, anonymization *fails to actually anonymize*. Our goal is to create a system that provides complete transparency about the correctness of the matching algorithm while preserving the privacy of all preference rankings.

Specifically, we want to generate a cryptographic proof that demonstrates the Gale-Shapley algorithm was executed correctly and produced a stable matching, without revealing any individual’s private preferences. The Nexus zkVM enables us to achieve exactly this balance between accountability and privacy.

***

{% stepper %}
{% step %}

### Implementation — initialize host and guest programs

Follow the [SDK Quick Start](https://docs.nexus.xyz/zkvm/development/sdk-quick-start). After installing the zkVM, to initialize the host and guest programs, run:

{% code title="Initialize host and guest" %}

```
$ cargo nexus host matching
```

{% endcode %}
{% endstep %}

{% step %}

### Guest Program

This guest program is the program to be proven; it implements the matching itself using the Gale-Shapley approach.

matching/src/guest/src/main.rs

{% code title="stable\_matching implementation" %}

```rust
#![cfg_attr(target_arch = "riscv32", no_std, no_main)]

extern crate alloc;
use alloc::collections::BTreeSet;
use alloc::{vec, vec::Vec};

fn stable_matching(
    n: usize,
    mut employers: BTreeSet<usize>,
    mut candidates: BTreeSet<usize>,
    employer_prefs: Vec<Vec<usize>>,
    candidate_prefs: Vec<Vec<usize>>,
) -> Vec<Option<usize>> {
    let mut hires: Vec<Option<usize>> = vec![None; n];
    while !employers.is_empty() {
        let next = employers.pop_first().unwrap();
        let prefs = &employer_prefs[next];

        for c in prefs {
            if candidates.contains(c) {
                hires[next] = Some(*c);
                assert!(candidates.remove(c));
                break;
            } else {
                let current = hires
                    .iter()
                    .position(|&x| x.is_some() && *c == x.unwrap())
                    .unwrap();
                if candidate_prefs[*c].iter().position(|&x| next == x)
                    < candidate_prefs[*c].iter().position(|&x| current == x)
                {
                    assert!(employers.insert(current));
                    hires[next] = Some(*c);
                    hires[current] = None;
                    break;
                }
            }
        }
    }

    hires
}
```

{% endcode %}

The function takes:

* a set of candidates (doctors),
* a set of employers (hospitals),
* preference rankings in matrix form (row i of `employer_prefs` encodes the ranking for the i-th employer),
* a parameter `n = employers.len()`.

It returns a vector `hires` of length `n`, where `hires[j] = i` means the j-th hospital hires the i-th doctor.

You also need a `main` to handle zkVM inputs/outputs and declare which inputs are public/private.

matching/src/guest/src/main.rs

{% code title="guest main" %}

```rust
#[nexus_rt::main]
#[nexus_rt::private_input(prefs)]
#[nexus_rt::public_input(lists)]
fn main(
    prefs: (Vec<Vec<usize>>, Vec<Vec<usize>>),
    lists: (BTreeSet<usize>, BTreeSet<usize>),
) -> Vec<Option<usize>> {
    let (mut employer_prefs, mut candidate_prefs) = prefs;
    let (mut employers, mut candidates) = lists;

    let n = employers.len();
    let m = candidates.len();

    nexus_rt::print!("Matching {} employers with {} candidates... ", n, m);

    let hires = stable_matching(n, employers, candidates, employer_prefs, candidate_prefs);

    nexus_rt::println!("completed.");

    hires
}
```

{% endcode %}

Note: inputs default to private unless explicitly declared public. The public inputs/outputs here leak only which hospital each candidate matched with (the `hires` vector), which is acceptable for auditing the algorithm while keeping preferences private.
{% endstep %}

{% step %}

### Host Program

The host program compiles the guest and runs it with the provided preferences (these preferences are private inside the host).

matching/src/main.rs

{% code title="host main" %}

```rust
use nexus_sdk::{
    compile::{cargo::CargoPackager, Compile, Compiler},
    stwo::seq::Stwo,
    ByGuestCompilation, Local, Prover, Viewable,
};
use std::collections::BTreeSet;

type Matches = Vec<Option<usize>>;
type Prefs = (Vec<Vec<usize>>, Vec<Vec<usize>>);
type Lists = (BTreeSet<usize>, BTreeSet<usize>);

const PACKAGE: &str = "guest";

fn main() {
    println!("Compiling guest program...");
    let mut prover_compiler = Compiler::<CargoPackager>::new(PACKAGE);
    let prover: Stwo<Local> =
        Stwo::compile(&mut prover_compiler).expect("failed to compile guest program");

    let n = 10;
    let m = 8;
    assert!(m < n);

    let mut employers = BTreeSet::<usize>::new();
    let mut candidates = BTreeSet::<usize>::new();

    for i in 0..n {
        employers.insert(i);
        if i < m {
            candidates.insert(i);
        }
    }

    let employer_prefs = vec![\
        vec![4, 1, 2, 7, 3, 0, 6, 5],\
        vec![0, 1, 4, 5, 7, 2, 6, 3],\
        vec![3, 7, 4, 6, 2, 0, 5, 1],\
        vec![4, 6, 0, 2, 7, 3, 5, 1],\
        vec![2, 6, 1, 3, 7, 0, 4, 5],\
        vec![1, 4, 5, 3, 7, 0, 6, 2],\
        vec![1, 5, 4, 0, 6, 2, 7, 3],\
        vec![3, 6, 1, 2, 7, 0, 5, 4],\
        vec![7, 5, 3, 4, 1, 6, 2, 0],\
        vec![0, 6, 1, 4, 5, 2, 7, 3],\
    ];

    let candidate_prefs = vec![\
        vec![0, 5, 7, 8, 3, 1, 4, 2, 6, 9],\
        vec![8, 2, 0, 9, 3, 4, 5, 6, 1, 7],\
        vec![3, 6, 4, 0, 5, 9, 7, 8, 2, 1],\
        vec![2, 9, 7, 3, 4, 1, 5, 8, 0, 6],\
        vec![7, 5, 9, 4, 6, 8, 0, 1, 3, 2],\
        vec![4, 1, 7, 6, 2, 9, 8, 0, 5, 3],\
        vec![0, 5, 3, 6, 8, 7, 4, 1, 9, 2],\
        vec![7, 5, 6, 1, 4, 0, 2, 8, 9, 3],\
    ];

    println!("Proving execution of vm...");
    let (view, proof) = prover.prove_with_input::<Prefs, Lists>(
        &(employer_prefs, candidate_prefs),
        &(employers, candidates),
    ).expect("failed to prove program");

    println!(
        ">>>>> Logging\n{}<<<<<",
        view.logs().expect("failed to retrieve debug logs").join("")
    );
    assert_eq!(view.exit_code().expect("failed to retrieve exit code"), nexus_sdk::KnownExitCodes::ExitSuccess as u32);

    let hires = view.public_output::<Matches>().expect("failed to retrieve public output");

    print!("Found matching (employer, candidate): ");
    for i in 0..n {
        if i > 0 {
            print!(", ")
        }
        print!(
            "({}, {})",
            i,
            if hires[i].is_some() {
                hires[i].unwrap().to_string()
            } else {
                "None".to_string()
            }
        );
    }
    println!("\n");

    /// the host program would go on to publish `view` and `proof` publicly.
}
```

{% endcode %}

The ranking matrices shown above are random example data for demonstration.
{% endstep %}

{% step %}

### Verification

Once the program, its public input/output (`view`) and the `proof` are published, any interested party can verify correctness without access to preferences.

{% code title="verifier snippet" %}

```rust
println!("Verifier recompiling guest program...");
let mut verifier_compiler = Compiler::<CargoPackager>::new(PACKAGE);
let path = verifier_compiler.build().expect("failed to (re)compile guest program");

print!("Verifying execution...");
proof.verify_expected_from_program_path::<&str, Lists, Matches>(
  &(employers, candidates),                       // at view.public_input
  nexus_sdk::KnownExitCodes::ExitSuccess as u32,  // at view.exit_code
  &hires,                                         // at view.public_output
  &path,                                          // path to program binary
  &[]                                             // no associated data,
).expect("failed to verify proof");
```

{% endcode %}

If the published matching (`hires`) has been tampered with in a way that violates Gale-Shapley guarantees, verification will fail.

Limitation: a verifier cannot directly confirm that the private preference matrices themselves are the ones originally provided by participants. The zkVM guarantees there exists some private input for which the execution is correct, not that the private input specifically matches an off-chain record. To mitigate this, participants can submit salted hashes of their preferences (with per-participant passphrases) that the guest program includes (hashed) in public output. Each participant can then verify their own preference hash matches what was used in the execution without revealing preferences to others.
{% endstep %}

{% step %}

### Conclusion

This walkthrough demonstrates how the Nexus zkVM can provide verifiable transparency for algorithmic decision-making while preserving privacy. Achievements:

* A publicly auditable guest program implementing stable matching.
* Proof generation that keeps preference rankings private.
* A verification mechanism for any party to confirm correct execution.
* A framework balancing individual privacy with institutional accountability.

The approach transforms the medical residency matching process from a “trust us” system to a “verify for yourself” system and can be applied to other algorithmic decision systems (financial algorithms, ML-based hiring/lending/healthcare) where transparency and privacy must coexist.
{% endstep %}
{% endstepper %}


# Use Case: Program Execution

### Introduction

*As this walkthrough describes a more advanced use case for the zkVM, we recommend reviewing both the* [SDK Quick Start](https://docs.nexus.xyz/zkvm/development/sdk-quick-start) *and the simpler* [Stable Matching](https://docs.nexus.xyz/zkvm/walkthroughs/use-case-stable-matching) *walkthrough first.*

By definition, a zkVM is designed to prove the correctness of a program’s execution. However, a more advanced use case arises when the **program to be proven** is not the code running directly in the zkVM, but is instead provided **as input** to the zkVM.

In this case, the zkVM executes an **interpreter** as its guest program, which then reads, interprets, and runs the input program inside the zkVM. This effectively allows the zkVM to generate a proof for the execution of arbitrary, dynamically supplied programs.

Consider the following guest program in which `program_to_be_proven` is nested inside as input to the zkVM:

```rust
fn digest(program: &ElfFile) -> Vec<u8> { ... }

fn rv32i_interpret(program: &ElfFile) -> Vec<u8> { ... }

#[nexus_rt::main]
#[nexus_rt::private_input(program_to_be_proven)]
#[nexus_rt::public_input(program_digest)]
fn main(program_to_be_proven: ElfFile, program_digest: Vec<u8>) -> Vec<u8> {
    assert_eq!(digest(&program_to_be_proven), &program_digest);

    nexus_rt::print!("Program digest {} validated, executing program... ", program_digest);

    let output = rv32i_interpret(&program_to_be_proven);

    nexus_rt::println!("completed.");

    output
}
```

At first glance, this pattern may seem redundant—why not just run `program_to_be_proven` directly as the guest program? However, this level of **indirection** unlocks powerful capabilities that significantly expand the utility of the zkVM.

#### Enabling Private Program Execution

The first benefit, illustrated by the example above, is the ability to treat the **program to be proven** as a **private input**. This allows the zkVM to prove the execution of programs **without revealing their source**, making it possible to build **private smart contracts** on-chain, among other use cases.

By comparing the program’s digest to a **public input**, verifiers can still check meaningful properties such as:

* Consistency of the private program across multiple invocations.
* Conformance to a known, audited version without exposing implementation details.

This digest check enables **trust minimization** while preserving **privacy**.

#### Generalization Across Programs with a Single zkVM Binary

A second, more technical benefit is that this structure enables the zkVM to handle a wide range of programs through a **single, fixed guest binary** — the interpreter.

With careful planning around memory constraints (e.g. stack, heap, and output size bounds), this pattern allows:

* The proving key and public parameters can be shared and reused across many programs, which simplifies definitions for [non-transparent provers which may require per-program setup](https://blog.nexus.xyz/the-murky-proof-system-waters-part-ii/).
* Deployment pipelines for applications and smart contracts verifying zkVM proofs on-chain can be simplified significantly.
* Systems using non-transparent proving systems can be managed more easily, even though they often require per-program setup (note: the `Stwo` prover used here is transparent).

This approach decouples the proving circuit from individual guest programs, significantly improving **composability** and **maintainability**.

### The Lambda Calculus Model

Instead of working through this design at the full complexity of the RISC-V32i instruction set, this walkthrough uses a simpler computational model: the [lambda calculus](https://en.wikipedia.org/wiki/Lambda_calculus). The example demonstrates the core concept with a minimal interpreter implemented as a guest program inside the zkVM.

***

### Implementation

To start, follow the [SDK Quick Start](https://docs.nexus.xyz/zkvm/development/sdk-quick-start). After installing the zkVM, initialize the host and guest programs:

```bash
$ cargo nexus host lambda_calculus
```

Begin by creating a shared library for the guest and host program, located within the guest program crate.

#### Shared Library

The first part of the library defines terms in the calculus:

lambda\_calculus/src/guest/src/common.rs

```rust
#![cfg_attr(no_std)]

extern crate alloc;

use alloc::boxed::Box;
use core::fmt::{Debug, Display};
use serde::{Serialize, Deserialize};

#[derive(Clone, Copy, Debug, PartialEq, Eq, PartialOrd, Ord, Serialize, Deserialize)]
#[repr(transparent)]
pub struct DeBruijnIndex(usize);

impl From<usize> for DeBruijnIndex {
    fn from(value: usize) -> Self {
        Self(value)
    }
}

impl Display for DeBruijnIndex {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        write!(f, "{}", self.0)
    }
}

#[derive(Clone, Debug, Serialize, Deserialize)]
enum Term<R> {
    Var(DeBruijnIndex),
    Lambda(R),
    Apply(R, R),
}

impl<R: Display> Display for Term<R> {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            Term::Var(v) => write!(f, "{v}"),
            Term::Lambda(t) => {
                write!(f, "(\\")?;
                write!(f, "{t}")?;
                write!(f, ")")
            }
            Term::Apply(t1, t2) => {
                write!(f, "(")?;
                write!(f, "{t1}")?;
                write!(f, " ")?;
                write!(f, "{t2}")?;
                write!(f, ")")
            }
        }
    }
}
```

This defines an enum `Term` for possible term kinds: indexed `Var`, `Lambda`, and `Apply`, and includes trait implementations for construction and debugging. Next, full expressions and evaluation routines:

lambda\_calculus/src/guest/src/common.rs

```rust
#[derive(Clone, Debug, Serialize, Deserialize)]
pub struct Expr(Term<Box<Self>>);

impl Display for Expr {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        write!(f, "{}", self.0)
    }
}

impl PartialEq for Expr {
    fn eq(&self, other: &Self) -> bool {
        self.clone().eval().structural_eq(&other.clone().eval())
    }
}

impl Eq for Expr {}

impl Expr {
    pub fn var<T: Into<DeBruijnIndex>>(binding: T) -> Self {
        Self(Term::Var(binding.into()))
    }

    pub fn lambda<T: Into<Box<Self>>>(inner: T) -> Self {
        Self(Term::Lambda(inner.into()))
    }

    pub fn apply<T1, T2>(left: T1, right: T2) -> Self
    where
        T1: Into<Box<Self>>,
        T2: Into<Box<Self>>,
    {
        Self(Term::Apply(left.into(), right.into()))
    }

    pub fn identity() -> Self {
        Self::lambda(Self::var(0))
    }

    pub fn omega() -> Self {
        let expr = Self::lambda(Self::apply(Self::var(0), Self::var(0)));
        Self::apply(expr.clone(), expr)
    }

    pub fn step(&self) -> Self {
        fn subst(body: Expr, arg: Expr, depth: usize) -> Expr {
            match body.0 {
                Term::Var(i) => {
                    if i.0 == depth {
                        arg
                    } else {
                        Expr::var(i)
                    }
                }
                Term::Lambda(e) => subst(*e, arg, depth + 1),
                Term::Apply(e1, e2) => {
                    Expr::apply(subst(*e1, arg.clone(), depth), subst(*e2, arg, depth))
                }
            }
        }

        // attempt beta reduction
        if let Term::Apply(e1, e2) = &self.0 {
            if let Term::Lambda(e) = &e1.0 {
                return subst(*e.clone(), *e2.clone(), 0);
            }
        }

        self.clone()
    }

    pub fn structural_eq(&self, other: &Self) -> bool {
        match (&self.0, &other.0) {
            (Term::Var(i), Term::Var(j)) => *i == *j,
            (Term::Lambda(e), Term::Lambda(f)) => e.structural_eq(f),
            (Term::Apply(e1, e2), Term::Apply(f1, f2)) => {
                e1.structural_eq(f1) && e2.structural_eq(f2)
            }
            _ => false,
        }
    }

    pub fn eval(self) -> Self {
        let mut curr = self;
        loop {
            let next = curr.step();
            if next.structural_eq(&curr) {
                return curr.clone();
            } else {
                curr = next;
            }
        }
    }
}
```

This provides `step` and `eval` routines to reduce expressions into stable forms.

To make the common library work across both host and guest:

* Update the guest crate to depend on `serde` (used for serialization/deserialization of `Expr`):

lambda\_calculus/src/guest/Cargo.toml

```toml
...

[dependencies]
nexus-rt = { git = "https://github.com/nexus-xyz/nexus-zkvm.git", tag = "0.3.0", version = "0.3.0" }
postcard = { version = "1.1.1", default-features = false, features = ["alloc"] }
serde = { version = "1.0", default-features = false, features = ["derive"] }

...
```

* Export the common code as a Rust library:

lambda\_calculus/src/guest/src/lib.rs

```rust
#![no_std]

pub mod common;
pub use common::*;
```

* Make the library visible to the host program:

lambda\_calculus/Cargo.toml

```toml
...

[dependencies]
nexus-sdk = { git = "https://github.com/nexus-xyz/nexus-zkvm.git", tag = "0.3.0", version = "0.3.0" }
guest = { path = "./src/guest" }

...
```

#### Guest Program

As an `Expr` is a program in the lambda calculus, implement a simple interpreter (here omitting hash-based checking):

lambda\_calculus/src/guest/src/main.rs

```rust
#![cfg_attr(target_arch = "riscv32", no_std, no_main)]

use guest::Expr;

#[nexus_rt::main]
#[nexus_rt::private_input(program_to_be_proven)]
fn main(program_to_be_proven: Expr) -> Expr {
    program_to_be_proven.eval()
}
```

#### Host Program

Create a host program that compiles the guest, provides a private program as input, and produces a proof of its execution:

lambda\_calculus/src/main.rs

```rust
use nexus_sdk::{
    compile::{cargo::CargoPackager, Compile, Compiler},
    stwo::seq::Stwo,
    ByGuestCompilation, Local, Prover, Viewable,
};

use guest::Expr;

const PACKAGE: &str = "guest";

fn main() {
    println!("Compiling guest program...");
    let mut prover_compiler = Compiler::<CargoPackager>::new(PACKAGE);
    let prover: Stwo<Local> =
        Stwo::compile(&mut prover_compiler).expect("failed to compile guest program");

    let program_to_be_proven = Expr::apply(Expr::identity(), Expr::var(42));

    println!("Proving execution of vm...");
    let (view, proof) = prover.prove_with_input::<Expr, ()>(
        &program_to_be_proven,
        (),
    ).expect("failed to prove program");

    assert_eq!(view.exit_code().expect("failed to retrieve exit code"), nexus_sdk::KnownExitCodes::ExitSuccess as u32);

    let output = view.public_output::<Expr>().expect("failed to retrieve public output");

    println!("Reduced expression: {}", output);
}
```

### Verification

Verification does not require access to the private program. A verifier can recompile the guest program and verify the proof against the expected outputs:

```rust
println!("Verifier recompiling guest program...");
let mut verifier_compiler = Compiler::<CargoPackager>::new(PACKAGE);
let path = verifier_compiler.build().expect("failed to (re)compile guest program");

print!("Verifying execution...");
proof.verify_expected_from_program_path::<&str, (), Expr>(
  &(),                                           // at view.public_input
  nexus_sdk::KnownExitCodes::ExitSuccess as u32, // at view.exit_code
  &output,                                       // at view.public_output
  &path,                                         // path to program binary
  &[]                                            // no associated data,
).expect("failed to verify proof");
```

This demonstrates using the zkVM to prove the correctness of executing a private program.

### Conclusion

This walkthrough demonstrates how the Nexus zkVM can be applied to fundamental computational models, illustrating versatility beyond practical applications. The implementation proves correct execution of lambda calculus programs while keeping program logic private.

Key achievements:

1. A shared library architecture enabling code reuse between guest and host programs.
2. A clean abstraction for lambda calculus expressions with evaluation semantics.
3. A zkVM-based interpreter that generates proofs for program execution.
4. A verification system that confirms correctness without exposing the original program.

This example shows that zkVMs can handle abstract computational models, not just concrete algorithms, and that privacy-preserving verification principles generalize across domains. The approach transforms program execution from “trust the interpreter” to “verify the computation,” providing mathematical assurance that programs are evaluated correctly according to their formal semantics.

Links for further reading:

* Use Case: Stable Matching: <https://docs.nexus.xyz/zkvm/walkthroughs/galeshapley>
* The Complete Specification: <https://docs.nexus.xyz/zkvm/specifications/zkvm-overview>


# The Complete Specification

The Nexus zkVM 3.0 Specification provides an overview of the runtime and machine architecture of the zkVM, as well as a full, formal description of the constraints and proving integration.

In this Specifications section, we provide accessible introductions to some of the core concepts from the specification.

<table data-view="cards"><thead><tr><th>Title</th><th data-card-target data-type="content-ref">Target</th></tr></thead><tbody><tr><td>Home</td><td><a href="https://docs.nexus.xyz/home">https://docs.nexus.xyz/home</a></td></tr><tr><td>Nexus Layer 1 — Overview</td><td><a href="https://docs.nexus.xyz/layer-1/vision/overview">https://docs.nexus.xyz/layer-1/vision/overview</a></td></tr><tr><td>Nexus zkVM</td><td><a href="../overview/the-nexus-zkvm">the-nexus-zkvm</a></td></tr><tr><td>Web3 Fundamentals — Overview</td><td><a href="https://docs.nexus.xyz/essentials/web3-fundamentals/overview">https://docs.nexus.xyz/essentials/web3-fundamentals/overview</a></td></tr><tr><td>Use Case: Program Execution</td><td><a href="../walkthroughs/use-case-program-execution">use-case-program-execution</a></td></tr><tr><td>Machine Architecture</td><td><a href="machine-architecture">machine-architecture</a></td></tr><tr><td>Full zkVM Specification: zkVM Overview</td><td><a href="#content-area">#content-area</a></td></tr></tbody></table>


# Machine Architecture

The primary use of the Nexus zkVM machine architecture is to support the verifiable computation of the full zkVM. However, it is a well-defined virtual machine in its own right, and some of its key components are described below.

### Architectural overview

The machine architecture is built around an instruction set, not the same as, but close enough to the RISC-V RV32I instruction set. The primary difference is the lack of a few supported instructions, such as `fence` and `ebreak`. The machine uses a modified Harvard architecture in which the program, data, and input-output memory segments are distinct and permissioned with respect to whether they can be read from, written to, or both.

### Execution Model

The Nexus zkVM is designed around a “only prove what you use” memory architecture, where unused memory does not need to be proven. As a trade-off, the zkVM requires that the amounts of memory used by most of the program segments (all but the heap) must be known before execution — even though the sizes of the stack and output are often execution-dependent.

To avoid this chicken-and-egg problem, the machine architecture operates on a two-pass tracing model: the program is first executed in a (mostly) traditional Harvard architecture, and statistics are kept as to the resultant memory usage. The guest program is then executed again using the same inputs in a modified Harvard architecture with a fixed-memory organization determined from the statistics of the first execution, which is more conducive to proving.

### Execution Environment

Through environment calls the guest program can interact with the execution environment. The machine architecture supports six environment calls. Two of these calls are used for debugging (logging) and optimization (cycle counting), and these are no-ops during the second, proven tracing. The other four are used for setting up stack and heap pointers in the second, fixed memory model, as well as for reading off the private input tape and exiting the guest program, analogous to the exit system calls (like Rust’s `std::process::exit(code: i32) -> !}` provided by most programming languages).

### Memory Layout

The machine architecture uses distinct component memories. Each memory has three attributes: in which address space it exists, with what permission structure (read-write, read-only, write-only, or no access), and whether it is of fixed or variable size.

For the first pass, the organization of the memory is a mostly traditional Harvard architecture, with five distinct address spaces:

* (i) the cpu registers,
* (ii) the public input,
* (iii) the error code and public output,
* (iv) the associated data, and
* (v) the RAM containing both the program and data segments (including the stack and heap).

Other than the joining of the program and data memories this forms a relatively traditional Harvard architecture. In terms of permissions and sizes:

* (i) is read-write and fixed,
* (ii) is read-only and fixed,
* (iii) is write-only and variable,
* (iv) is no-access and fixed, and
* (v) is variable and mixed read-only (for static global variables) and read-write (for the remaining global variables and the entire data memory).

For (v) the guest program itself has no access to its instructions: they can only be accessed by the CPU.

For the second tracing pass, the memories are combined into a fixed-size, linear memory layout with one single, unified address space. As this is the memory layout used in tracing, the zkVM is best understood as a modified Harvard architecture, as the permission structures on the segments are maintained but they no longer exist in distinct memories. Also, a small additional read-only 8-byte segment containing well-known location pointers is introduced to enable the runtime to successfully access the now relocated public input and output segments.

### Registers

The zkVM machine has 32 registers that hold 32-bit word values. When tracing the program the zkVM stores the state of the registers separate from its record of memory operations. However, it also reserves the addresses `0x00-0x7F` so that prover integrations are able to identify the registers with those addresses should the prover need to consider the entire state of the machine to lie within a single address space.

### Well-Known Location Pointers

When tracing, the machine architecture also reserves two words of memory, the first from `0x80-0x83` and the second from `0x84-0x87`, which contain pointers to other memory locations for use by the runtime to manage input and output handling. These pointers existing in a well-known location for the runtime to access enables the zkVM to dynamically situate the input and output memory segments within the unified, linear architecture while still allowing the guest program easy access to their contents.

### Program Memory

The zkVM executes a guest program encoded in an ELF binary. The core of such a binary is the program consisting of a sequence of instructions and supporting read-only data (such as that contained in the `.rodata` segment). Before the zkVM executes the guest, this data must be loaded into a read-only segment of program memory, and after that remains unchanged during execution.

Additionally, the binary may contain read-write segments, such as the `.bss` and `.data` segments commonly used by programming languages to store global variables. Being writable, these segments must also be private over the course of the execution post-initialization. As such, the machine functionally treats these segments as a small part of the RAM that is non-contiguous with it, but with additional constraints to guarantee they are initialized as specified in the binary.

To simplify management of the dual-nature of these segments as both part of the program but also writable, the zkVM keeps the program memory and data memory in the same address space during the first-pass tracing, but with distinct permissions for the writable vs. read-only components. Those permissions are maintained in the unified address space of the linear memory model used in the second pass.

### Public Input

The public input segment contains an input of length `n` bytes prefaced by a four-byte (one 32-bit word) segment `n` so that the guest program can determine the length of the input made available to it. To read from the input the runtime invokes a custom instruction `rin`. During the second tracing pass — which is the one proven — `rin` is treated as a pseudoinstruction equivalent to `lb`, and the offset is loaded from the first word of the well-known segment (addresses `0x80-0x83` in the unified address space of the linear memory model). During both tracing passes, the contents of the segment are read-only — the zkVM will halt if an attempt is made by the guest program to write to those memory segments.

### Associated Data

For many zkVM use cases it can be useful to be able to bind arbitrary contextual information about an execution or the context of the proving into the proof itself. For example, from the perspective of the zkVM the program is just a compiled binary. By incorporating the hash of the program as originally written in a high-level language — such as Rust or Python — the proof can carry a reference to that code for use by the verifier, such as for auditing its functional correctness or the correctness of its compilation. In the particular case where the program forms a standalone software package, such as a Cargo crate or Python wheel, then binding in the hash of that package can even relate the proof to the broader software ecosystem.

To support binding arbitrary external information into the proof, the machine architecture contains an associated data memory segment that the prover can populate with an arbitrary bytestring. This segment is no-access within the Harvard architecture — it can neither be written to nor read from during an execution. But, the verifier otherwise treats it as a public input segment with checked contents that can then be used post-verification for application-focused infrastructure built on top of the proof, such as the aforementioned auditing. The associated data is placed before the public output and exit code, so that the memory regions after it form a contiguous space of writable segments.

### Public Output

The public output and exit code work in much the same way as the public input, except the relevant custom instruction is `wou` — interpreted on the second pass as `sb` — and the offset is loaded from the second word of the well-known segment (addresses `0x84-0x87` in the unified address space of the linear memory model). Otherwise, the most significant difference is that the single-word exit code segment and the public output segment are write-only, rather than read-only.

During the first tracing pass the public output segment can grow arbitrarily (up to addressing limits) to support additional written output. The length of the resultant output is then reserved ahead of time for the memory segment for the second and proven tracing pass.

### Data Memory

The zkVM includes a RAM. Instructions can read from the data memory, write to the data memory, or leave the data memory untouched. The primary use of the data memory is to store the stack and the heap.

During the first tracing pass, its size is variable and the stack and heap grow towards each other, as is standard. During the second tracing pass the stack and heap still grow towards each other, but are given fixed-size segments within which to do so. As a consequence, the size of the data memory is limited to only what is needed, enabling quicker proving and smaller proofs in the zkVM as only memory that is used is “paid for” by needing to prove its contents.


# Proving Instructions

The final component of the Nexus zkVM is the execution component, which is responsible for enforcing the correct execution of the instructions supported by the VM. It is designed with modularity and extensibility in mind.

Currently, this component provides support for the Nexus Virtual Machine (NVM) instruction set described in Section 2 of [the specification](https://docs.nexus.xyz/zkvm/specifications/the-complete-specification). The NVM instruction set is closely related to the RISC-V RV32I unprivileged instruction set found in [the RISC-V specification](https://drive.google.com/file/d/1s0lZxUZaa7eV_O0_WsZzaurFLLww7ou5/view). As a result, existing tooling for RISC-V RV32I can usually be used without modification.

We discuss some of the constraints for this component when we describe our [example](https://docs.nexus.xyz/zkvm/specifications/proving-an-example), but details of all the constraints for this component can be found in Section 8 of [the specification](https://docs.nexus.xyz/zkvm/specifications/the-complete-specification).


# Proving the CPU

The CPU component of the Nexus zkVM’s constraint system is responsible for ensuring that each state transition is correct. In particular, it is responsible for ensuring that the [instruction fetch](https://en.wikipedia.org/wiki/Classic_RISC_pipeline#Instruction_fetch), [instruction decode](https://en.wikipedia.org/wiki/Classic_RISC_pipeline#Instruction_decode), and [write-back](https://en.wikipedia.org/wiki/Classic_RISC_pipeline#Writeback) stages of the classic RISC pipeline are correct. It also facilitates connecting other stages of the pipeline with their respective constraint circuits.

Concretely, the CPU component performs the following tasks for each CPU cycle:

* Interacts with the program memory to fetch the next instruction pointed to by the program counter.
* Decodes that instruction and verifies that it is well-formed.
* Interacts with the register memory component to read the values associated with the instruction’s operands.
* Interacts with the execution component to execute the just-fetched instruction.
* Interacts with the register memory to perform write-back.

We discuss some of the constraints for this component when we describe our [example](https://docs.nexus.xyz/zkvm/specifications/proving-an-example), but details of all the constraints for this component can be found in Section 4 of [the specification](https://docs.nexus.xyz/zkvm/specifications/the-complete-specification).


# Proving Memory

The Nexus zkVM has three different components for handling the behavior of each type of memory used by the zkVM. Those types are:

* Program memory: a byte-addressed read-only memory space that contains the program being executed.
* Register memory: a word-addressed read-write memory space that contains the 32 32-bit registers specified by RISC-V RV32I.
* Data memory: a byte-addressed read-write memory space that accounts for all remaining memory used by the program.

To maintain consistency of accesses to the register and data memories, the Nexus zkVM uses a well-known offline memory checking technique (see [BEG+94](#references)). In this technique, each memory cell is associated with a timestamp which serves as a unique identifier for each memory access. In addition to the timestamps, the memory checking algorithm also maintains read and write sets, whose purpose is to record a trace of the program’s memory access pattern.

The main advantage of offline memory checking techniques is that one does not need to keep track of the actual status of the running memory. Instead, the memory checking algorithm only keeps a trace digest of memory accesses, which is inexpensive and can be updated at a cost that is independent of the size of the memory.

For program memory, a simpler memory checking technique can be used to maintain the consistency of the memory accesses. Instead of keeping a timestamp for each memory cell, it suffices to associate a counter to each memory cell to keep track of the number of times that each cell has been read.

In this version of the Nexus zkVM, the computation of the digest is implemented using logarithmic derivatives (also known as logups). See [EKRN24](#references) and [Hab22](#references).

We discuss some of the constraints for these components when we describe our [example](https://docs.nexus.xyz/zkvm/specifications/proving-an-example). Full details of all the constraints for these components can be found in:

* Section 5 of the specification for register memory: <https://docs.nexus.xyz/zkvm/specifications/zkvm-overview>
* Section 6 of the specification for program memory: <https://docs.nexus.xyz/zkvm/specifications/zkvm-overview>
* Section 7 of the specification for data memory: <https://docs.nexus.xyz/zkvm/specifications/zkvm-overview>

## References

* [BEG+94](https://doi.org/10.1007/BF01185212) Manuel Blum, William S. Evans, Peter Gemmell, Sampath Kannan, and Moni Naor. “Checking the correctness of memories”. Algorithmica, 12(2/3):225–244, 1994.
* [EKRN24](https://eprint.iacr.org/2022/510) Liam Eagen, Sanket Kanjalkar, Tim Ruffing, and Jonas Nick. “Bulletproofs++: Next Generation Confidential Transactions via Reciprocal Set Membership Arguments”. In EUROCRYPT 2024.
* [Hab22](https://eprint.iacr.org/2022/1530) Ulrich Haböck. “Multivariate lookups based on logarithmic derivatives”. In: Cryptology ePrint Archive (2022).

Related pages:

* [Proving the CPU](https://docs.nexus.xyz/zkvm/specifications/proving-the-cpu)
* [Proving Instructions](https://docs.nexus.xyz/zkvm/specifications/proving-instructions)
* [Nexus zkVM overview](https://docs.nexus.xyz/zkvm/specifications/the-complete-specification)
* Example: <https://docs.nexus.xyz/zkvm/specifications/example>


# Proving — An Example

In order to illustrate how these different components work together, let us consider an example in which the program counter pc points to memory location 0x00000004, containing the binary encoding of the instruction `ADDI x10 x8 3`. Moreover, for the sake of this example, let us assume the following about the state of the VM.

* Current clock cycle: 256
* Current trace row: 255
* Total number of rows: 2^16
* R\[x8] = 0x000000FF was last updated with timestamp 323
* R\[x10] = 0x00000005 was last updated with timestamp 77
* Prog\[0x00000004] has been accessed 222 times before the current clock cycle

In the following we describe the relevant trace columns associated with each component, their expected values at row 255 associated with the current clock cycle 256, and the associated constraints that they must satisfy.

### CPU Component Trace Columns and Constraints

In order to verify the correct execution of the `ADDI x10 x8 3` instruction at clock cycle 256, the CPU component will perform the following operations:

* Ensure a correct state transition;
* Fetch the instruction `ADDI x10 x8 3` from the program memory component;
* Decode the contents of the instruction and check the correctness of its format;
* Read contents of register x8 from the register memory component;
* Interact with the execution component to execute the instruction `ADDI x10 x8 3`; and
* Update the contents of register x10 based on the output of the execution component.

Let us now show how each of these operations is performed.

#### Ensuring a Correct State Transition

The CPU component ensures the state transition is performed correctly to guarantee correct ordering of instructions. It performs these checks:

{% stepper %}
{% step %}

### Verify program counter continuity

* Verify that the program counter in the present row matches the value of the next program counter from the preceding row (accounting for limb decomposition).
* Transition constraints (comparing two limbs at a time):
  * (1 - is\_first\[i]) \* (1 - is\_pad\[i]) \* (pc(1)\[i] + pc(2)\[i] \* 2^8 - pc\_next(1)\[i-1] - pc\_next(2)\[i-1] \* 2^8) = 0
  * (1 - is\_first\[i]) \* (1 - is\_pad\[i]) \* (pc(3)\[i] + pc(4)\[i] \* 2^8 - pc\_next(3)\[i-1] - pc\_next(4)\[i-1] \* 2^8) = 0

For our concrete state at row 255:

* i = 255
* pc(1)\[255] = 0x04, pc(2)\[255] = 0x00, pc(3)\[255] = 0x00, pc(4)\[255] = 0x00
* is\_pad\[255] = 0, is\_first\[255] = 0

Therefore pc\_next limbs on row 254 must equal 0x04, 0x00, 0x00, 0x00 respectively.
{% endstep %}

{% step %}

### Check clock update correctness

* Transition constraints for clk\[i] for row i > 0:
  * Use clk\_carry(1), clk\_carry(2) for carries.
  * Adding two limbs at a time:
    * clk(1)\[i] + clk(2)\[i] \* 2^8 + clk\_carry(1)\[i] \* 2^16 = clk(1)\[i-1] + clk(2)\[i-1] \* 2^8 + 1
    * clk(3)\[i] + clk(4)\[i] \* 2^8 + clk\_carry(2)\[i] \* 2^16 = clk(3)\[i-1] + clk(4)\[i-1] \* 2^8 + clk\_carry(1)\[i]
  * Enforce clk\_carry(j) in {0,1} via (clk\_carry(j))\*(1 - clk\_carry(j)) = 0
  * Range-check clk(j) ∈ \[0, 2^8 - 1] for each limb.

For our state, to increment clock from 255 → 256 it must hold that on row 254:

* clk(1)\[254] = 0xFF, clk(2)\[254] = 0x00, clk(3)\[254] = 0x00, clk(4)\[254] = 0x00
* clk\_carry(1)\[255] = 0, clk\_carry(2)\[255] = 0
  {% endstep %}

{% step %}

### Prevent padding rows from being followed by non-padding rows

* Enforce: (1 - is\_first\[i]) \* (1 - is\_pad\[i]) \* (is\_pad\[i-1]) = 0

With is\_pad\[255] = 0 and is\_first\[255] = 0, this implies is\_pad\[254] = 0.
{% endstep %}
{% endstepper %}

#### Fetching the Instruction

The CPU must read the instruction stored at the memory location pointed by pc and ensure pc is memory-aligned (multiple of 4).

Remark: Whenever constraints involve columns restricted to the same row, we omit explicit \[i] index for readability (values below apply to row 255 unless otherwise noted).

* The CPU interaction with program memory is captured by ReadProg interface with parameters (pc, clk) to obtain instr\_val. In the trace, instr\_val and pc are shared between CPU and program memory.

As a result at row 255:

* instr\_val(1) = Prog\[0x00000004] = 0b00010011
* instr\_val(2) = Prog\[0x00000005] = 0b00000101
* instr\_val(3) = Prog\[0x00000006] = 0b00110100
* instr\_val(4) = Prog\[0x00000007] = 0b00000000

Binary encoding breakdown for `ADDI x10 x8 3`:

* Bits 0–6: 0b0010011 (ADDI constant)
* Bits 7–11: 0b01010 → destination register x10 (op\_a)
* Bits 12–14: 0b000 (ADDI constant)
* Bits 15–19: 0b01000 → source register x8 (op\_b)
* Bits 20–31: 0b000000000011 → immediate 3 (op\_c)

Memory alignment constraint for pc:

* pc\_aux(1) \* 4 - pc(1) = 0
* pc\_aux(1) ∈ \[0, 2^6 - 1]

For this example, set pc\_aux(1) = 0x01 to show pc is multiple of 4.

#### Decoding the Instruction

The prover provides auxiliary values (advices) to help verify the binary encoding:

* op\_a = destination register (10)
* op\_b = source register (8)
* op\_c = immediate (3)
* op\_b\_flag = 1 (operand b used)
* imm\_c = 1 (operand c is immediate)
* is\_add = 1 (selector for ADD/ADDI)
* is\_alu\_imm\_no\_shift = 1
* is\_type\_i = 1
* is\_pad = 0, is\_first = 0, is\_last = 0

Operand decomposition advices (bits split across limbs):

* op\_a0 = 0 (bit 0 of op\_a)
* op\_a1\_4 = 5 (bits 1–4 of op\_a)
* op\_b0 = 0 (bit 0 of op\_b)
* op\_b1\_4 = 4 (bits 1–4 of op\_b)
* op\_c0\_3 = 3 (bits 0–3 of op\_c)
* op\_c4\_7 = 0 (bits 4–7 of op\_c)
* op\_c8\_10 = 0 (bits 8–10 of op\_c)
* op\_c11 = 0 (bit 11 of op\_c)

Convert the numbered set of constraints used to validate decoding into steps:

{% stepper %}
{% step %}

### 1) Exactly one instruction or padding flag is set

Enforce sum of instruction flags + is\_pad = 1. Since is\_add = 1, all other flags are 0.
{% endstep %}

{% step %}

### 2) op\_b\_flag correctness

Enforce op\_b\_flag = 1 for all instructions except {LUI, AUIPC, JAL, UNIMP}. This is satisfied by is\_add = 1 and op\_b\_flag = 1.
{% endstep %}

{% step %}

### 3) imm\_c correctness

Enforce imm\_c = 1 for all non-ALU instructions (constraint used to ensure correctness across instruction types). Given imm\_c = 1 in our example, constraints are satisfied.
{% endstep %}

{% step %}

### 4) Match instruction flag with opcode

For ADD/ADDI: (is\_add) \* (opcode - ADD) = 0. With is\_add = 1 and opcode set to ADD constant, satisfied.
{% endstep %}

{% step %}

### 5) ALU flags grouping

Define aggregated flags:

* is\_alu = sum of ALU instruction selectors
* is\_alu\_imm\_shift = imm\_c \* (is\_sll + is\_srl + is\_sra)
* is\_alu\_imm\_no\_shift = imm\_c \* (is\_add + is\_slt + is\_sltu + is\_xor + is\_or + is\_and)
* is\_type\_i\_no\_shift = is\_load + is\_alu\_imm\_no\_shift + is\_jalr
* is\_type\_i = is\_load + is\_alu\_imm\_no\_shift + is\_alu\_imm\_shift + is\_jalr

With is\_add = 1 and imm\_c = 1 we get:

* is\_alu = 1
* is\_alu\_imm\_shift = 0
* is\_alu\_imm\_no\_shift = 1
* is\_type\_i\_no\_shift = 1
* is\_type\_i = 1
  {% endstep %}

{% step %}

### 6) Operand decomposition consistency and range checks

* Ensure op\_a0 + op\_a1\_4 \* 2 - op\_a = 0 (when is\_type\_i\_no\_shift = 1)
* Range-check op\_a0 is binary, op\_a1\_4 ∈ \[0, 2^4 - 1]
* Ensure op\_b0 + op\_b1\_4 \* 2 - op\_b = 0
* Range-check op\_b parts
* Ensure op\_c0\_3 + op\_c4\_7 \* 2^4 + op\_c8\_10 \* 2^8 + op\_c11 \* 2^11 - op\_c = 0
* Range-check op\_c parts

With provided operand parts and is\_type\_i\_no\_shift = 1, these constraints hold for the example.
{% endstep %}

{% step %}

### 7) Sign-extension for operand c

Compute c\_val from op\_c using sign-extension constraints across limbs. Since op\_c11 = 0, higher limbs become 0. Prover sets:

* c\_val(1) = 0x03
* c\_val(2) = 0x00
* c\_val(3) = 0x00
* c\_val(4) = 0x00
  {% endstep %}

{% step %}

### 8) Instruction format checks across limbs

* Limb 1: (is\_alu\_imm\_no\_shift) \* (0b0010011 + op\_a0 \* 2^7 - instr\_val(1)) = 0
* Limb 2: (is\_add) \* (imm\_c) \* (op\_a1\_4 + 0b000 \* 2^4 + op\_b0 \* 2^7 - instr\_val(2)) = 0
* Limb 3: (is\_type\_i\_no\_shift) \* (op\_b1\_4 + op\_c0\_3 \* 2^4 - instr\_val(3)) = 0
* Limb 4: (is\_type\_i\_no\_shift) \* (op\_c4\_7 + op\_c8\_10 \* 2^4 + op\_c11 \* 2^7 - instr\_val(4)) = 0

With the previously set flags and operand parts, these constraints are satisfied for the given instr\_val limbs.
{% endstep %}
{% endstepper %}

#### Reading the Contents of Register x8

The interaction with register memory is captured by ReadReg interface with parameters (op\_b, clk, 1) where 1 indicates this is source register reg1. In the trace, fields are shared between CPU and register memory.

As a result of the interaction:

* reg1\_addr = op\_b
* b\_val limbs are set equal to reg1\_val\_cur limbs

Given the assumption R\[x8] = 0x000000FF before execution, the limbs are:

* b\_val(1) = reg1\_val\_cur(1) = 0xFF
* b\_val(2) = reg1\_val\_cur(2) = 0x00
* b\_val(3) = reg1\_val\_cur(3) = 0x00
* b\_val(4) = reg1\_val\_cur(4) = 0x00

#### Executing the Instruction

The CPU calls the execution component via exec(pc, opcode, a\_val, b\_val, c\_val) to obtain pc\_next. For ADD, execution updates a\_val.

After execution (ADDI x10 x8 3 → x10 := x8 + 3), the limbs are set as:

* a\_val(1) = 0x02
* a\_val(2) = 0x01
* a\_val(3) = 0x00
* a\_val(4) = 0x00

pc is incremented by 4, so:

* pc\_next(1) = 0x08
* pc\_next(2) = 0x00
* pc\_next(3) = 0x00
* pc\_next(4) = 0x00

(These a\_val limbs follow from b\_val = 0x000000FF and c\_val = 0x00000003.)

#### Updating the contents of register x10

To ensure x0 stays zero, CPU computes a\_val\_effective:

* a\_val\_effective = a\_val when op\_a ≠ 0, otherwise 0.
* Use auxiliary a\_val\_effective\_flag and supporting auxiliaries to enforce this (including multiplicative inverse aux variables).
* Enforce a\_val\_effective\_flag ∈ {0,1} and relation a\_val(limb) \* a\_val\_effective\_flag = a\_val\_effective(limb).

For op\_a = x10 (non-zero) the prover sets:

* a\_val\_effective\_flag = 1
* a\_val\_effective\_flag\_aux = 1 (non-zero aux)
* a\_val\_effective\_flag\_aux\_inv = appropriate inverse
* a\_val\_effective(limbs) = a\_val(limbs) = 0x02, 0x01, 0x00, 0x00 respectively

Then CPU interacts with register memory via WriteReg(op\_a, a\_val\_effective, clk, 3) to write to reg3 (destination). As a result reg3\_val\_cur limbs (for reg3\_addr = op\_a = x10) become:

* reg3\_val\_cur(1) = 0x02
* reg3\_val\_cur(2) = 0x01
* reg3\_val\_cur(3) = 0x00
* reg3\_val\_cur(4) = 0x00

### Execution Component Trace Columns and Constraints

To verify the ADD execution, the execution component enforces carry-handling constraints across limbs and that helper carries are binary.

Carry handling for ADD (per limb):

* (is\_add) \* (op\_a\_val(1) + h\_carry(1) \* 2^8 - op\_b\_val(1) - op\_c\_val(1)) = 0
* (is\_add) \* (op\_a\_val(2) + h\_carry(2) \* 2^8 - op\_b\_val(2) - op\_c\_val(2) - h\_carry(1)) = 0
* (is\_add) \* (op\_a\_val(3) + h\_carry(3) \* 2^8 - op\_b\_val(3) - op\_c\_val(3) - h\_carry(2)) = 0
* (is\_add) \* (op\_a\_val(4) + h\_carry(4) \* 2^8 - op\_b\_val(4) - op\_c\_val(4) - h\_carry(3)) = 0

And enforce (is\_add) \* h\_carry(j) \* (1 - h\_carry(j)) = 0 for each helper carry.

Given b\_val = 0x000000FF and c\_val = 0x00000003, to satisfy these constraints:

* a\_val limbs = 0x02, 0x01, 0x00, 0x00
* h\_carry(1) = 1, h\_carry(2) = 0, h\_carry(3) = 0, h\_carry(4) = 0

Next, execution determines whether pc is incremented by 4 (is\_pc\_inc\_std). It enforces:

* (is\_alu + is\_load + is\_type\_s + is\_type\_u + is\_type\_sys \* (1 - is\_sys\_halt) - is\_pc\_inc\_std) = 0

If is\_pc\_inc\_std = 1 then pc\_next must equal pc + 4, handled limb-wise with pc\_carry auxiliaries:

* (is\_pc\_inc\_std) \* (pc\_next(1) + pc\_next(2) \* 2^8 + pc\_carry(1) \* 2^16 - pc(1) - pc(2) \* 2^8 - 4) = 0
* (is\_pc\_inc\_std) \* (pc\_next(3) + pc\_next(4) \* 2^8 + pc\_carry(2) \* 2^16 - pc(3) - pc(4) \* 2^8 - pc\_carry(1)) = 0
* Enforce pc\_carry(j) binary via (is\_pc\_inc\_std) \* pc\_carry(j) \* (1 - pc\_carry(j)) = 0

For pc = 0x00000004, this yields pc\_next = 0x00000008 and pc\_carry(1) = pc\_carry(2) = 0.

### Program Memory Component Trace Columns and Constraints

The program memory component uses offline memory checking (simplified for read-only memory) with a counter per memory cell tracking read counts. Trace elements include:

* pc (word-aligned base address for instruction)
* instr\_val(1..4): instruction word bytes at pc, pc+1, pc+2, pc+3
* prog\_ctr\_prev (4 limbs): previous counter for base address pc
* prog\_ctr\_cur (4 limbs): current counter for base address pc
* prog\_read\_digest: digest of read set (logup)
* prog\_write\_digest: digest of write set (logup)

Actions per read:

* Check counter update correctness
* Verify read/write set digests updated correctly

#### Enforcing correct update of access counters

Enforce prog\_ctr\_cur = prog\_ctr\_prev + 1 using prog\_ctr\_carry auxiliaries across limbs. Carry bits must be binary.

Given Prog\[0x00000004] was accessed 222 times before current clock, set:

* prog\_ctr\_prev = 222 → limbs: prog\_ctr\_prev(1) = 2, prog\_ctr\_prev(2..4) = 0
* prog\_ctr\_cur = 223 → limbs: prog\_ctr\_cur(1) = 3, prog\_ctr\_cur(2..4) = 0
* prog\_ctr\_carry(1..4) = 0

#### Enforcing correct update of read- and write-set digests

Let fp(pc, instr\_val, prog\_ctr) be a fingerprint function (uses verifier-chosen β). Using random α chosen by verifier, enforce transition constraints for i > 0:

* prog\_read\_digest\[i] - prog\_read\_digest\[i-1] = 1 / (fp(pc\[i], instr\_val\[i], prog\_ctr\_prev\[i]) + α)
* prog\_write\_digest\[i] - prog\_write\_digest\[i-1] = 1 / (fp(pc\[i], instr\_val\[i], prog\_ctr\_cur\[i]) + α)

For row 255 with known pc and instr\_val limbs, these constraints must hold with the corresponding prog\_ctr\_prev and prog\_ctr\_cur.

Remark: instr\_val, prog\_ctr\_prev and prog\_ctr\_cur limbs also have range checks in the formal spec; the values above satisfy those ranges.

### Register Memory Component Trace Columns and Constraints

The register memory component uses offline memory checking for read/write memory and associates a timestamp per cell. It also uses logups for read/write set digest consistency. Each access maintains tuples of (reg\_addr, reg\_val\_prev, reg\_val\_cur, reg\_ts\_prev, reg\_ts\_cur). Up to three register addresses can be accessed in one execution cycle; the trace contains three such sets.

Trace elements include:

* clk
* reg1\_addr, reg2\_addr, reg3\_addr
* reg1\_val\_cur, reg2\_val\_cur, reg3\_val\_cur (32-bit values)
* reg1\_ts\_cur, reg2\_ts\_cur, reg3\_ts\_cur (current timestamps)
* reg1\_val\_prev, reg2\_val\_prev, reg3\_val\_prev
* reg1\_ts\_prev, reg2\_ts\_prev, reg3\_ts\_prev
* reg\_read\_digest, reg\_write\_digest
* reg1\_accessed, reg2\_accessed, reg3\_accessed flags (indicate whether each set is used)

Register memory enforces:

1. Current timestamps for reg1/2/3 satisfy:
   * reg1\_ts\_cur = 3 \* clk - 2
   * reg2\_ts\_cur = 3 \* clk - 1
   * reg3\_ts\_cur = 3 \* clk
2. Previous timestamps precede current timestamps:
   * regj\_ts\_prev ∈ {0, …, regj\_ts\_cur - 1}
3. Read/write digest updates via logup contributions (described below).

Remark: reg1\_addr, reg2\_addr, reg3\_addr should be accessed in order and only reg3\_addr can be modified during a clock cycle.

#### Enforcing the Correct Update of Read- and Write-Set Digests (Registers)

Let fp(reg\_addr, reg\_val, reg\_ts) be a fingerprint function (uses verifier-chosen β). For row index i > 0 and random α:

* reg\_read\_digest\[i] - reg\_read\_digest\[i-1] = reg1\_accessed\[i] / (fp(reg1\_addr\[i], reg1\_val\[i], reg1\_ts\_prev\[i]) + α)
  * reg2\_accessed\[i] / (fp(reg2\_addr\[i], reg2\_val\[i], reg2\_ts\_prev\[i]) + α)
  * reg3\_accessed\[i] / (fp(reg3\_addr\[i], reg3\_val\[i], reg3\_ts\_prev\[i]) + α)
* reg\_write\_digest\[i] - reg\_write\_digest\[i-1] = reg1\_accessed\[i] / (fp(reg1\_addr\[i], reg1\_val\[i], reg1\_ts\_cur\[i]) + α)
  * reg2\_accessed\[i] / (fp(reg2\_addr\[i], reg2\_val\[i], reg3\_ts\_cur\[i]) + α)
  * reg3\_accessed\[i] / (fp(reg3\_addr\[i], reg3\_val\[i], reg3\_ts\_cur\[i]) + α)

For this example, the assumptions and derived values for row 255 are:

* R\[x8] = 0x000000FF with last timestamp 323
* R\[x10] = 0x00000005 with last timestamp 77
* clk\[255] = 256
* reg1\_ts\_cur\[255] = 3 \* 256 - 2 = 766
* reg3\_ts\_cur\[255] = 3 \* 256 = 768
* reg1\_accessed\[255] = 1, reg2\_accessed\[255] = 0, reg3\_accessed\[255] = 1
* R\[x10] updated to 0x00000102 at current clock

To satisfy logup constraints at i = 255, the following must be set consistently (limb decompositions shown):

* reg1\_ts\_prev\[255] limbs: (1) = 32, (2..4) = 0
* reg1\_val\_prev\[255] = reg1\_val\_cur\[255] = 0xFF, 0x00, 0x00, 0x00
* reg1\_ts\_cur\[255] limbs: (1) = 254, (2) = 2, (3..4) = 0 (representation of 766)
* reg3\_ts\_prev\[255] limbs: (1) = 7, (2..4) = 0
* reg3\_val\_prev\[255] limbs: 0x05, 0x00, 0x00, 0x00
* reg3\_ts\_cur\[255] limbs: (1) = 0, (2) = 3, (3..4) = 0 (representation of 768)
* reg3\_val\_cur\[255] limbs: 0x02, 0x01, 0x00, 0x00

With these values, the register read/write digest transition constraints hold for the example.

***

References (kept intact):

* Proving Memory: <https://docs.nexus.xyz/zkvm/specifications/memory-checking>
* Proving Instructions: <https://docs.nexus.xyz/zkvm/specifications/instructions>
* Licensing: <https://docs.nexus.xyz/zkvm/license>

(End of cleaned/import-optimized page content.)


# Licensing

## Licensing

The Nexus zkVM is licensed under the source-available Business Source License (BUSL):\
<https://github.com/nexus-xyz/nexus-zkvm/blob/main/LICENSE>

This license will convert to an open-source dual Apache 2.0 and MIT licensing on February 10th, 2029.


