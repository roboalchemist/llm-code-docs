# Source: https://docs.espressosys.com/network/releases/testnets/doppio-testnet-release/benchmarks.md

# Source: https://docs.espressosys.com/network/releases/testnets/cappuccino-testnet-release/benchmarks.md

# Source: https://docs.espressosys.com/network/references/benchmarks.md

# Espresso Network Benchmarks

Providing faster finality is Espresso's core priority. The engineering team has worked on reducing block finality from 10s to 2s, and thus has performed some benchmarking tests on an internal network, which emulates Espresso's Decaf netwok.

## Summary

**- Finality latency:** 2 seconds to finalize a block (5 MB blocks).

**- Throughput:** Increased from 1 MB/s → 5 MB/s.

**- Benchmark network:** 100 globally distributed nodes + 21 DA nodes.

## Why This Matters

One of Espresso’s core goals is to enable chains to communicate quickly and securely, helping solve the problem of liquidity fragmentation across the blockchain ecosystem.

The faster crosschain applications can securely react to on-chain events, the more usable and unified liquidity becomes, thus bringing us closer to a truly interconnected ecosystem.

These latest benchmark results represent a major step forward. And Espresso is far from finished: **the team is already working toward sub-second block finality in the coming year.**

## What Enabled the Performance Gains

### 1. High-bandwidth TCP tuning

Default operating system TCP settings severely limit global throughput (≈30 Mbps). By optimizing TCP parameters for high-latency, high-bandwidth networking, nodes now utilize virtually the full 1 Gbps capacity available on AWS machines.

### 2. Regional Builders

Requesting blocks from a remote [Builder](https://docs.espressosys.com/network/guides/node-operators/running-a-builder) introduced large global round-trip delays. Espresso now runs a Builder in every region, each sharing the same mempool. Validators fetch blocks locally, cutting block preparation time in half.

### 3. Earlier block preparation in the pipeline

Leaders nodes now begin block assembly as soon as they receive the proposal, instead of waiting for the previous view to be finished, saving roughly 200 ms per view.

## Future Improvements

### 1. Faster block retrieval

The Builder block exchange currently takes \~500 ms per view. Moving to a single round-trip request could significantly reduce the time.

### 2. Smarter networking

Today, all messages route through a central CDN, adding an extra hop. Seding smaller messages over a dedicated p2p network could further improve latency.

### 3. Removing the DA committee bottleneck

Removing the Data Availability Commitee could reduce time in around 800ms.

## Benchmarking Set-up

* 100 nodes and 21 DA nodes geographically distributed across `ap-southeast-1`, `eu-central-1`, `us-east-1`, `ap-southeast-2` and `sa-east-1` regions.
* 1 CDN (located in `us-east-2`, run on `c8gn.large`).
* A Builder located in each region and run on `c8g.xlarge`.
