# Run an OP Stack Rollup on 0G DA

Optimism is a lightning-fast Ethereum L2 blockchain, built with the OP Stack. 0G DA is a high-performance data availability layer that can be used with Optimism to provide a cost-effective and secure solution for storing transaction data.

## Overview

To implement this server specification, 0G DA provides a `da-server` that runs as a sidecar process alongside the OP Stack rollup node. This server connects to a 0G DA client to securely communicate with the 0G DA network.

### Required Components

- [0G DA client node](/developer-hub/building-on-0g/da-integration)
- [0G DA encoder node](/developer-hub/building-on-0g/da-integration)
- 0G DA Server (deployment guide below)
- OP Stack components with configuration adjustments

### GitHub Repository

Find the repository for this integration at: https://github.com/0gfoundation/0g-da-op-plasma

The Optimism codebase has been extended to integrate with the 0G DA `da-server`. This server utilizes the 0G DA Open API to efficiently store and retrieve rollup data.

## Deployment Steps

### 1. Deploy DA Server

<Tabs>
<TabItem value="docker" label="Run with Docker" default>

**Build the Docker image:**

```bash
docker build -t 0g-da-op-plasma .
```

**Run the Docker container:**

Adjust commands and parameters as required for your setup:

```bash
docker run -p 3100:3100 0g-da-op-plasma:latest da-server \
  --addr 0.0.0.0 \
  --port 3100 \
  --zg.server rpc_to_a_da_client  # default: 127.0.0.1:51001
```

</TabItem>
<TabItem value="source" label="Build from Source">

**Build DA Server:**

```bash
git clone https://github.com/0gfoundation/0g-da-op-plasma.git
cd 0g-da-op-plasma
make da-server
```

**Run DA Server:**

```bash
./bin/da-server \
  --addr 127.0.0.1 \
  --port 3100 \
  --zg.server rpc_to_a_da_client  # default: 127.0.0.1:51001
```

</TabItem>
</Tabs>

**DA Server Configuration Flags:**

| Flag | Description | Default |
|------|-------------|---------|
| `--zg.server` | 0G DA client server endpoint | `localhost:51001` |
| `--addr` | Server listening address | - |
| `--port` | Server listening port | - |

### 2. Deploy DA Client and DA Encoder

For guidance on setting up a 0G DA client and DA Encoder, refer to the [DA integration documentation](../da-integration.md).

### 3. Deploy OP Stack

## Prerequisites

Ensure you have installed the following software:

| Software | Version |
|----------|---------|
| Git | OS default |
| Go | 1.21.6 |
| Node | ^20 |
| just | 1.34.0 |
| Make | OS default |
| jq | OS default |
| direnv | Latest |

**Required releases:**
- op-node/v1.9.1
- op-proposer/v1.9.1
- op-batcher/v1.9.1
- op-geth v1.101408.0

## Build the Optimism Monorepo

**1. Clone and navigate to the Optimism Monorepo:**

```bash
git clone https://github.com/ethereum-optimism/optimism.git
cd optimism
git fetch --tag --all
git checkout v1.9.1
git submodule update --init --recursive
```

**2. Check your dependencies:**

```bash
./packages/contracts-bedrock/scripts/getting-started/versions.sh
```

**3. Compile the necessary packages:**

```bash
make op-node op-batcher op-proposer
make build
```

## Build the Optimism Geth Source

**1. Clone and navigate to op-geth:**

```bash
git clone https://github.com/ethereum-optimism/op-geth.git
cd op-geth
git fetch --tag --all
git checkout v1.101408.0
```

**2. Compile op-geth:**

```bash
make geth
```

## Get Access to a Sepolia Node

For deploying to Sepolia, access an L1 node using a provider like [Alchemy](https://www.alchemy.com/) (easier) or run your own Sepolia node (harder).

## Configure Environment Variables

**1. Enter the Optimism Monorepo:**

```bash
cd ~/optimism
```

**2. Duplicate the sample environment variable file:**

```bash
cp .envrc.example .envrc
```

**3. Fill out the environment variables:**

| Variable Name | Description |
|---------------|-------------|
| `L1_RPC_URL` | URL for your L1 node (a Sepolia node in this case) |
| `L1_RPC_KIND` | Kind of L1 RPC you're connecting to (`alchemy`, `quicknode`, `infura`, `parity`, `nethermind`, `debug_geth`, `erigon`, `basic`, `any`) |

## Generate Addresses

You'll need four addresses and their private keys:

- **Admin**: Has the ability to upgrade contracts
- **Batcher**: Publishes Sequencer transaction data to L1
- **Proposer**: Publishes L2 transaction results (state roots) to L1
- **Sequencer**: Signs blocks on the p2p network

**1. Navigate to the contracts-bedrock package:**

```bash
cd ~/optimism/packages/contracts-bedrock
```

**2. Generate accounts:**

```bash
./scripts/getting-started/wallets.sh
```

you will get the following output:
```bash
Copy the following into your .envrc file: