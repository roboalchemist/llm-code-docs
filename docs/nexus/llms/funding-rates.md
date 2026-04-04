# Source: https://docs.nexus.xyz/trading/perpetuals/funding-rates.md

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
