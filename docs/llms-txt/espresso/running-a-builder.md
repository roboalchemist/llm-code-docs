# Source: https://docs.espressosys.com/network/guides/node-operators/running-a-builder.md

# Running a Builder

### **Overview**

Participants creating blocks for the Espresso Network must run a builder, a piece of software which tracks the state of [HotShot consensus](https://github.com/EspressoSystems/gitbook/blob/main/guides/learn/the-espresso-network/README.md) so that it is able to and propose blocks at the correct time. The builder functions to create a block filled with transactions, drawing from transactions accessible in Espresso's public mempool as well as its own private mempool.

Espresso provides a simple builder implementation, which participants can run out-of-the-box or build their own software on top of. This document describes how to run the basic builder software.

For comprehensive guidance on the design of an Espresso builder, it is recommended to refer to the [`hotshot-builder-core`](https://github.com/EspressoSystems/hotshot-builder-core) repository. Furthermore, to gain insight into the process of enabling builder services for a sequencer, pertinent information can be found at [`espresso-sequencer-builder`](https://github.com/EspressoSystems/espresso-sequencer/tree/main/builder). For access to the most recent builder Docker images, please visit [here](https://github.com/EspressoSystems/espresso-sequencer/pkgs/container/espresso-sequencer%2Fbuilder).

### Usage

```bash
# Clone the espresso-sequencer repository
git clone https://github.com/EspressoSystems/espresso-sequencer

# Build the executable in release mode
cargo build --release

# Run a builder natively
target/release/permissionless-builder [options]

# To understand more about the available builder options
target/release/permissionless-builder -h

# Run a node with the builder docker image
docker run -it \
  [-e ENV=VALUE...] \
  ghcr.io/espressosystems/espresso-sequencer/builder:main
```

For a quick start, we recommend referring to the `espresso-sequencer` [docker-compose](https://github.com/EspressoSystems/espresso-sequencer/blob/main/docker-compose.yaml) file, and looking particularly at [`permissionless-builder`](https://github.com/EspressoSystems/espresso-sequencer/blob/270393c5bc5d1c974652d46edb5034251fa16bd7/docker-compose.yaml#L415C1-L435C35).

### Parameters & options

<table><thead><tr><th>Environment variable</th><th width="157">CLI flag</th><th>Description</th></tr></thead><tbody><tr><td>ESPRESSO_SEQUENCER_HOTSHOT_EVENT_STREAMING_API_URL</td><td>--hotshot-event-streaming-url</td><td>URL of hotshot events API running on Espresso Sequencer DA committee node. A builder will subscribe to this server to receive hotshot events. (e.g. http://localhost:8081)</td></tr><tr><td>ESPRESSO_BUILDER_ETH_MNEMONIC</td><td>--eth-mnemonic</td><td>Mnemonic phrase for builder account (e.g. "test test test test test test test test test test test junk")</td></tr><tr><td>ESPRESSO_BUILDER_ETH_ACCOUNT_INDEX</td><td>--eth-account-index</td><td>Index of a funded account. <strong>Note</strong>: This account must be funded in <em>Espresso</em>, meaning ETH must be bridged from the L1</td></tr><tr><td>ESPRESSO_BUILDER_L1_PROVIDER</td><td>--l1-provider-url</td><td>A Url builder will use for RPC communication with L1 (e.g. http://demo-l1-network:8545)</td></tr><tr><td>ESPRESSO_SEQUENCER_STATE_PEERS</td><td>--state-peers</td><td>Peer nodes use to fetch missing state</td></tr><tr><td>ESPRESSO_SEQUENCER_CHAIN_ID</td><td>--chain-id</td><td>Unique identifier for an instance of the sequencer network</td></tr><tr><td>ESPRESSO_SEQUENCER_MAX_BLOCK_SIZE</td><td>--max-block-size</td><td>Maximum allowed size (in bytes) for a block</td></tr><tr><td>ESPRESSO_SEQUENCER_BASE_FEE</td><td>--base-fee</td><td>Minimum fee in WEI per byte of payload</td></tr><tr><td>ESPRESSO_BUILDER_SERVER_PORT</td><td>--port</td><td>Port to run builder server on through which sequencer node can query builder provided APIs (e.g 41003)</td></tr><tr><td>ESPRESSO_BUILDER_BOOTSTRAPPED_VIEW</td><td>--view-number</td><td>Bootstrapping View number (e.g. 0)</td></tr><tr><td>ESPRESSO_BUILDER_CHANNEL_CAPACITY</td><td>--channel-capacity</td><td>The most outstanding hotshot events a builder wants at a point in time (e.g. 1024)</td></tr><tr><td>ESPRESSO_BUILDER_WEBSERVER_RESPONSE_TIMEOUT_DURATION</td><td>--max-api-timeout-duratio</td><td>The amount of time a builder can wait before timing out a request to the API (e.g 1s)</td></tr><tr><td>ESPRESSO_BUILDER_BUFFER_VIEW_NUM_COUNT</td><td>--buffer-view-num-count</td><td>The number of views to buffer before a builder garbage collects its state (e.g. 15)</td></tr></tbody></table>

## Hardware requirements

Hardware requirements are subject to change as new features are added, but for now we recommend the following:

* **Memory**: 4-8 GB
* **CPU:** 2-4 Cores
