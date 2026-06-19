# Data Availability Node
---
While there are various approaches to running a DA (Data Availability) node, this guide outlines our recommended method and the necessary hardware specifications. DA Nodes perform the core functions of verifying, signing, and storing encoded blob data. 

To operate effectively, your DA signer needs to run a DA node to verify encoded blob data, sign it, and store it for future farming and rewards. Currently, to run a DA Node on Testnet, users must stake 10 OG tokens. These can be obtained through our [faucet](https://faucet.0g.ai/) or via rewards from running Storage Nodes or Validator Nodes. You can also reach out to our technical moderators on [Discord](https://discord.com/invite/0glabs).

## Hardware Requirements

| Node Type | Memory | CPU | Disk | Bandwidth | Additional Notes |
|-----------|--------|-----|------|-----------|------------------|
| DA Node | 16 GB | 8 cores | 1 TB NVMe SSD | 100 MBps | For Download/Upload |

## Standing up a DA Node and DA Signer
<Tabs>

  <TabItem value="Da-node-docker" label="Run with Docker" default>

**1. Clone the DA Node Repo:** 

   ```
   git clone https://github.com/0gfoundation/0g-da-node.git
   cd 0g-da-node
   ```

**2. Generate BLS Private Key (if needed):**

If you don't have a BLS private key, generate one:

```
cargo run --bin key-gen
```

Keep the generated BLS private key secure.

**3. Set up config.toml:**

1. Create a configuration file named `config.toml` in the project root directory.
2. Add the following content to the file, adjusting values as needed:

   ```toml
   log_level = "info"

   data_path = "/data"

   # path to downloaded params folder
   encoder_params_dir = "/params"

   # grpc server listen address
   grpc_listen_address = "0.0.0.0:34000"
   # chain eth rpc endpoint
   eth_rpc_endpoint = "https://evmrpc-testnet.0g.ai"
   # public grpc service socket address to register in DA contract
   # ip:34000 (keep same port as the grpc listen address)
   # or if you have dns, fill your dns
   socket_address = "<public_ip/dns>:34000"

   # data availability contract to interact with
   da_entrance_address = "0x857C0A28A8634614BB2C96039Cf4a20AFF709Aa9" # testnet config
   # deployed block number of da entrance contract
   start_block_number = 940000 # testnet config

   # signer BLS private key
   signer_bls_private_key = ""
   # signer eth account private key
   signer_eth_private_key = ""
   # miner eth account private key, (could be the same as `signer_eth_private_key`, but not recommended)
   miner_eth_private_key = ""

   # whether to enable data availability sampling
   enable_das = "true"
   ```

   Make sure to fill in the `signer_bls_private_key`, `signer_eth_private_key`, and `miner_eth_private_key` fields with your actual private keys.

**4. Build and Start the Docker Container:**

   ```
   docker build -t 0g-da-node .
   docker run -d --name 0g-da-node 0g-da-node
   ```
**5. Verify the Node is Running**

On the first run, the DA node will register the signer information in the DA contract. You can monitor the console output to ensure the node is running correctly and has successfully registered.

### Node Operations

As a DA node operator, your node will perform the following tasks:
- Encoded blob data verification
- Signing of verified data
- Storing blob data for further farming
- Receiving rewards for these operations

### Troubleshooting

- If you encounter any issues, check the console output for error messages.
- Ensure that the ports specified in your `config.toml` file are not being used by other applications.
- Verify that you have the latest stable version of Rust installed.
- Make sure your system meets the minimum hardware requirements.

### Conclusion

You have now successfully set up and run a 0g DA node as a DA Signer. For more advanced configuration options and usage instructions, please refer to the [Official GitHub repository](https://github.com/0gfoundation/0g-da-node).

Remember to keep your private keys secure and regularly update your node software to ensure optimal performance and security.

  </TabItem>

<TabItem value="Da-node" label="Build from Source" default>

## Step 1: Clone and Build the Repository

1. Install dependencies:

   ```
   sudo apt-get update && sudo apt-get install clang cmake build-essential pkg-config libssl-dev protobuf-compiler llvm llvm-dev
   ```

2. Clone the repository and checkout the specific version:

   ```
   git clone https://github.com/0gfoundation/0g-da-node.git
   cd 0g-da-node
   ```

3. Build the project:

   ```
   cargo build --release
   ```

4. Download necessary parameters:

   ```
   ./dev_support/download_params.sh
   ```

## Step 2: Generate BLS Private Key (if needed)

If you don't have a BLS private key, generate one:

```
cargo run --bin key-gen
```

**Keep the generated BLS private key secure.**

## Step 3: Configure the Node

1. Create a configuration file named `config.toml` in the project root directory.
2. Add the following content to the file, adjusting values as needed:

   ```toml
   log_level = "info"

   data_path = "./db/"

   # path to downloaded params folder
   encoder_params_dir = "params/" 

   # grpc server listen address
   grpc_listen_address = "0.0.0.0:34000"
   # chain eth rpc endpoint
   eth_rpc_endpoint = "https://evmrpc-testnet.0g.ai"
   # public grpc service socket address to register in DA contract
   # ip:34000 (keep same port as the grpc listen address)
   # or if you have dns, fill your dns
   socket_address = "<public_ip/dns>:34000"

   # data availability contract to interact with
   da_entrance_address = "0x857C0A28A8634614BB2C96039Cf4a20AFF709Aa9" # testnet config and see testnet page for the latest info

   # deployed block number of da entrance contract
   start_block_number = 940000 # testnet config

   # signer BLS private key
   signer_bls_private_key = ""
   # signer eth account private key
   signer_eth_private_key = ""
   # miner eth account private key, (could be the same as `signer_eth_private_key`, but not recommended)
   miner_eth_private_key = ""

   # whether to enable data availability sampling
   enable_das = "true"
   ```

   Make sure to fill in the `signer_bls_private_key`, `signer_eth_private_key`, and `miner_eth_private_key` fields with your actual private keys.

## Step 4: Run the Node

Start the 0g DA node using the following command:

```
./target/release/server --config config.toml
```

This will start the node using the configuration file you created.

## Step 5: Verify the Node is Running

On the first run, the DA node will register the signer information in the DA contract. You can monitor the console output to ensure the node is running correctly and has successfully registered.

## Node Operations

As a DA node operator, your node will perform the following tasks:
- Encoded blob data verification
- Signing of verified data
- Storing blob data for further farming
- Receiving rewards for these operations

## Troubleshooting

- If you encounter any issues, check the console output for error messages.
- Ensure that the ports specified in your `config.toml` file are not being used by other applications.
- Verify that you have the latest stable version of Rust installed.
- Make sure your system meets the minimum hardware requirements.

## Conclusion

You have now successfully set up and run a 0g DA node as a DA Signer. For more advanced configuration options and usage instructions, please refer to the [Official GitHub repository](https://github.com/0gfoundation/0g-da-node).

Remember to keep your private keys secure and regularly update your node software to ensure optimal performance and security.
  </TabItem>

<TabItem value="signer" label="Become a Signer">

## Overview

The DASigners contract is an interface through which Solidity contracts can interact with the 0G chain module DASigners. It is registered as a precompiled contract, similar to other precompiled EVM extensions.

## Becoming a DA Signer

To become a DA signer, you must meet the following requirements:

1. Delegation Requirement: To become a signer, an address must receive enough delegations, equivalent to at least the TokensPerVote amount of OG tokens (30 tokens per vote in the testnet), registered in the DASigners module.

2. Node Operation: Each signer needs to run a DA (Data Availability) node that verifies blob encoding and generates BLS signatures for signed blobs.

3. Registration: Signers must register their information using the registerSigner function. This includes providing their address, node socket address, BLS public key, and a signature signed by their BLS private key.

4. Epoch Participation: Signers must submit a registration message (using the registerNextEpoch function) with a signature for each epoch they wish to participate in. This is necessary for joining quorums in the next epoch.

5. Voting Power: Each signer’s voting power is determined by the number of tokens delegated to them. Signers can have up to 1024 votes, and the votes are distributed randomly into quorums.

6. Quorum Responsibilities: Each signer in a quorum is responsible for validating, signing, and storing a specific row of encoded blob data during an epoch.

## Prerequisites

Ensure you have the following installed on your system:

- Git
- Rust (latest stable version)
- Cargo (comes with Rust)

## Contract Details

**Address**: `0x0000000000000000000000000000000000001000`

### Contract Params (Testnet)

```
TokensPerVote = 30
MaxVotesPerSigner = 1024
MaxQuorums = 10
EpochBlocks = 5760
EncodedSlices = 3072
```

## Terminology

### Signer

A Signer is an address with sufficient delegations (at least `TokensPerVote` OG) registered in the DASigners module. Each signer should run a DA node to verify DA blob encoding and generate BLS signatures for signed blobs. The BLS curve used is BN254, and the public keys of signers are registered in the contract.

**Note**: For accounts with delegations to more than 10 validators, only 10 of these delegations are counted and accumulated.

### Epoch

The consecutive blocks in the 0g chain are divided into groups of `EpochBlocks`, and each group is an epoch.

### Quorum

In an epoch, there can be up to `MaxQuorums` quorums. Each quorum is a list of signer addresses with size `EncodedSlices`. The i-th signer in the quorum is responsible for validating, signing, and storing the i-th row of the encoded blob data assigned to this quorum.

### Vote

Signers can submit their signatures on a registration message to request joining the quorums in the next epoch. At the start of each epoch, the DASigners module calculates the voting power for registered signers based on their delegated token amounts. Each delegated `TokensPerVote` OG counts as one vote, and each signer can have up to `MaxVotesPerSigner` votes. All votes are then randomly ordered and distributed into quorums.

## Interface

Find the Solidity interface in the [0g-da-contract repo](https://github.com/0gfoundation/0g-da-contract).

## ABI

Find the ABI in the [0g-chain repo](https://github.com/0gfoundation/0g-chain).

## Transactions

### registerSigner

Register signer's information, including signer address, DA node service socket address, signer BLS public key on G1 and G2 group, and a signature signed by the BLS private key of the following message:

```
Keccak256(signerAddress, chainID, "0G_BN254_Pubkey_Registration")
```

Here `chainID` is left-padded to 32 bytes by zeros.

```solidity
function registerSigner(
    SignerDetail memory _signer, 
    BN254.G1Point memory _signature
) external;
```

### updateSocket

Update signer's socket address.

```solidity
function updateSocket(string memory _socket) external;
```

### registerNextEpoch

Register to join the quorums in the next epoch. The signer needs to submit a signature signed by their BLS private key:

```
Keccak256(signerAddress, epoch, chainID)
```

Here `chainID` is left-padded to 32 bytes by zeros and `epoch` is an unsigned 64-bit number in big-endian format.

```solidity
function registerNextEpoch(BN254.G1Point memory _signature) external;
```

## Queries

### epochNumber

Get the current epoch number.

```solidity
function epochNumber() external view returns (uint);
```

### quorumCount

Get the number of quorums for a given epoch.

```solidity
function quorumCount(uint _epoch) external view returns (uint);
```

### isSigner

Check if a given address is a registered signer.

```solidity
function isSigner(address _account) external view returns (bool);
```

### getSigner

Get the information of given signers.

```solidity
function getSigner(address[] memory _account) external view returns (SignerDetail[] memory);
```

### getQuorum

Get the signer list of a given epoch and quorum id.

```solidity
function getQuorum(uint _epoch, uint _quorumId) external view returns (address[] memory);
```

### getQuorumRow

Get the signer of a specific row in a given epoch and quorum id.

```solidity
function getQuorumRow(uint _epoch, uint _quorumId, uint32 _rowIndex) external view returns (address);
```

### registeredEpoch

Check if a given address is registered to join the given epoch.

```solidity
function registeredEpoch(address _account, uint _epoch) external view returns (bool);
```

### getAggPkG1

Get the aggregated G1 public key for a given signers set. The signers set is specified by the epoch, quorum id, and a bitmap. The bitmap has `EncodedSlices` bits, and each bit denotes whether the row is chosen or not.

```solidity
function getAggPkG1(
    uint _epoch,
    uint _quorumId,
    bytes memory _quorumBitmap
) external view returns (BN254.G1Point memory aggPkG1, uint total, uint hit);
```
  </TabItem>
</Tabs>

---

## Overview(Run-a-node)

---
Want to become an active participant in the 0G network and earn rewards while you're at it? 👇

Each node type plays a crucial role in maintaining the 0G network's functionality, from transaction validation and data storage to ensuring data availability and retrieval. Here, we'll introduce you to the various types of nodes you can run, each contributing to the network's health and security.

### What Nodes Can I Run?

##### **Validator Nodes**
The guardians of the network, validator nodes are responsible for verifying transactions, ensuring consensus, and maintaining the blockchain. They're essential for keeping the 0G blockchain secure and running smoothly.

##### **Storage Nodes**
Unlike Validator Nodes that focus on securing the blockchain itself, Storage Nodes focus on managing and serving data. They are the backbone of the network's data storage capabilities, ensuring persistence and availability for long-term data storage (e.g., training datasets, large AI models). By running a storage node, you'll contribute to the decentralized storage of 0G data, making it accessible and resilient.

##### **Data Availability Services**
DA Nodes are similar to Storage Nodes but focus on immediacy and short-term accessibility to support real-time operations. This data is typically used by Layer 2 and rollup solutions for data availability and is not typically stored long-term. Think of these nodes as the network's librarians, ensuring that data can be quickly retrieved when needed.

##### **Archival Nodes**
Archival Nodes maintain complete historical blockchain data and state, providing comprehensive access to the network's entire history. These nodes are essential for applications requiring historical data analysis, compliance, and serving as reliable backups for the network's complete transaction history.

### Why Run a Node?

Running a node isn't just about supporting the network; it's also a way to earn rewards for your contribution. By actively participating in the 0G ecosystem, you'll be eligible to receive rewards that incentivize your efforts.

#### Ready to Dive In?

We've made it easy to get started. The table below outlines the hardware requirements for each type of node, so you can choose the one that best suits your setup. Once you're ready, head over to the 0G documentation for detailed instructions on how to set up and run your chosen node.

| Node Type | Description | Memory | CPU | Disk | Bandwidth |
|-----------|-------------|--------|-----|------|-----------|
| Validator Node | Validates transactions and maintains network consensus | 64 GB | 8 cores | 1 TB NVME SSD (4 TB on Testnet) | 100 MBps |
| Storage Node | Stores data within the 0g network | 16 GB | 4 cores | 500GB / 1T NVME SSD | 500 MBps |
| Storage KV | Handles key-value storage operations | 4 GB | 2 cores | Matches KV streams size | - |
| DA Node | Performs blob data verification, signing, and storage | 16 GB | 8 cores | 1 TB NVME SSD | 100 MBps |
| DA Retriever | Retrieves data availability information | 8 GB | 2 cores | - | 100 MBps |
| DA Encoder* | Encodes data for availability purposes | - | - | - | - |
| DA Client | Interacts with the Data Availability layer | 8 GB | 2 cores | - | 100 MBps |

*Note: For DA Encoder, GPU support is currently tested with NVIDIA 12.04 drivers on the RTX 4090. Other NVIDIA GPUs may require parameter adjustments and have not been tuned yet.*

#### Next Steps
Ready to set up your node? Check out our detailed guides:

- [Validator Node Setup Guide](validator-node.md)
- [Storage Node Setup Guide](storage-node.md)
- [Data Availability Service Setup Guide](da-node.md)
- [Archival Node Setup Guide](archival-node.md)

---

## Storage Node

---
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

In the 0G network, storage nodes play a vital role in maintaining the system's decentralized storage layer. They are responsible for storing and serving data, ensuring data availability and reliability across the network. By running a storage node, you actively contribute to the network and earn rewards for your participation.
This guide details the process of running a storage node, including hardware specifications and interaction with on-chain contracts.

### Hardware Requirements

| Component | Storage Node | Storage KV |
|-----------|--------------|------------|
| Memory    | 32 GB RAM    | 32 GB RAM  |
| CPU       | 8 cores      | 8 cores    |
| Disk      | 500GB / 1TB SSD | Size matches the KV streams it maintains |
| Bandwidth | 100 Mbps (Download / Upload) | - |

:::note
- For Storage Node: The SSD ensures fast read/write operations, critical for efficient blob storage and retrieval.
- For Storage KV: The disk size requirement is flexible and should be adjusted based on the volume of KV streams you intend to maintain.
:::
### Next Steps
For detailed instructions on setting up and operating your Storage Node or Storage KV, please refer to our comprehensive setup guides below:

<Tabs>
  <TabItem value="binary" label="Storage Node" default>

## Prerequisites

Before setting up your storage node:

- Understand that 0G Storage interacts with on-chain contracts for blob root confirmation and PoRA mining.
- Choose your network: [Testnet](../developer-hub/testnet/testnet-overview.md) or [Mainnet](../developer-hub/mainnet/mainnet-overview.md)
- Check the respective network overview pages for deployed contract addresses and RPC endpoints.
- **For mainnet deployment**: Ensure you have real 0G tokens for transaction fees and mining rewards.

## Install Dependencies
Start by installing all the essential tools and libraries required to build the 0G storage node software.

<Tabs
  defaultValue="linux"
  values={[
    {label: 'Linux', value: 'linux'},
    {label: 'Mac', value: 'mac'},
    ]}>
  <TabItem value="linux">

        ```bash
        sudo apt-get update
        sudo apt-get install clang cmake build-essential pkg-config libssl-dev protobuf-compiler
        ```
</TabItem>
  <TabItem value="mac">
        ```bash
        brew install llvm cmake
        ```
</TabItem>
</Tabs>
**Install `rustup`**: rustup is the Rust toolchain installer, necessary as the 0G node software is written in Rust.

    ```bash
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
    ```

 **Download the Source Code**:

    ```bash
    git clone -b <latest_tag> https://github.com/0gfoundation/0g-storage-node.git
    ```

**Build the Source Code**

    ```bash
    cd 0g-storage-node

    # Build in release mode
    cargo build --release
    ```

This compiles the Rust code into an executable binary. The `--release` flag optimizes the build for performance.

## Setup and Configuration

Navigate to the run directory and configure your storage node for either testnet or mainnet.

:::info Config File References
The official configuration files are in the `run/` directory. Currently only `turbo` is available:
```
run/config-testnet-turbo.toml
run/config-mainnet-turbo.toml
```

Always use the latest versions from the repository as they contain the most up-to-date network parameters.
:::

**Turbo vs Standard**
Both `turbo` and `standard` configs are identical in structure and fields. The only difference is pricing; choose the file that matches the pricing tier you want to run.

**Where The Full Config Is Explained**
The most detailed, up-to-date comments for every field live in `run/config-testnet-turbo.toml` (and the corresponding `run/config-testnet-standard.toml`). Use those files as the authoritative field-by-field explanation.

**Key Fields (Same Wording As `run/config-testnet-turbo.toml`)**
`network_boot_nodes`
Note: List of nodes to bootstrap UDP discovery. Note, `network_enr_address` should be configured as well to enable UDP discovery.

`log_contract_address`
Note: Flow contract address to sync event logs.

`mine_contract_address`
Note: Mine contract address for incentive.

`reward_contract_address`
Note: Reward contract address.

`db_max_num_sectors`
Note: The max number of chunk entries to store in db. Each entry is 256B, so the db size is roughly limited to `256 * db_max_num_sectors` Bytes. If this limit is reached, the node will update its `shard_position` and store only half data.

`chunk_pool_write_window_size`
Note: Maximum number of threads to upload segments of a single file simultaneously.

`chunk_pool_max_writings`
Note: Maximum number of threads to upload segments for all files simultaneously.

`auto_sync_enabled`
Note: Enable file sync among peers automatically. When enabled, each node will store all files, and sufficient disk space is required.

`neighbors_only`
Note: Indicates whether to sync file from neighbor nodes only. This is to avoid flooding file announcements in the whole network, which leads to high latency or even timeout to sync files.

**CLI Options**
CLI flags override values in `config.toml`.
- `-c`, `--config <FILE>`: Sets a custom config file.
- `--log-config-file [FILE]`: Sets log configuration file (Default: `log_config`).
- `--miner-key [KEY]`: Sets miner private key (Default: None).
- `--blockchain-rpc-endpoint [URL]`: Sets blockchain RPC endpoint (Default: `http://127.0.0.1:8545`).
- `--db-max-num-chunks [NUM]`: Sets the max number of chunks to store in DB (Default: None).
- `--network-enr-address [URL]`: Sets the network ENR address (Default: None).

**Configuration Reference**
Full configuration keys are defined in `node/src/config/mod.rs` and log sync behavior is implemented in `node/log_entry_sync/src/sync_manager/config.rs`.

**Network**
- `network_dir`: Directory for node keyfile and network data (Default: `network`).
- `network_listen_address`: IP address to listen on (Default: `0.0.0.0`).
- `network_enr_address`: Public address advertised in ENR (Default: None).
- `network_enr_tcp_port`: TCP port advertised in ENR (Default: `1234`).
- `network_enr_udp_port`: UDP port advertised in ENR (Default: `1234`).
- `network_libp2p_port`: Libp2p TCP port (Default: `1234`).
- `network_discovery_port`: Discovery UDP port (Default: `1234`).
- `network_target_peers`: Target number of connected peers (Default: `50`).
- `network_boot_nodes`: ENR boot nodes list for discovery (Default: empty list).
- `network_libp2p_nodes`: Initial libp2p peers to connect to (Default: empty list).
- `network_private`: Enable private mode (Default: `false`).
- `network_disable_discovery`: Disable discovery protocol (Default: `false`).
- `network_find_chunks_enabled`: Enable find-chunks behavior (Default: `false`).

**Discv5**
- `discv5_request_timeout_secs`: Timeout per UDP request (Default: `5`).
- `discv5_query_peer_timeout_secs`: Timeout to mark a query peer unresponsive (Default: `2`).
- `discv5_request_retries`: Retry count for UDP requests (Default: `1`).
- `discv5_query_parallelism`: Parallelism per query (Default: `5`).
- `discv5_report_discovered_peers`: Emit discovered ENRs during traversal (Default: `false`).
- `discv5_disable_packet_filter`: Disable incoming packet filter (Default: `false`).
- `discv5_disable_ip_limit`: Disable /24 subnet limit in kbuckets (Default: `false`).
- `discv5_disable_enr_network_id`: Disable ENR network ID checks (Default: `false`).

**Log Sync**
- `blockchain_rpc_endpoint`: RPC endpoint to sync EVM logs (Default: `http://127.0.0.1:8545`).
- `log_contract_address`: Flow contract address to sync logs from (Default: empty).
- `log_sync_start_block_number`: Block number to start syncing logs (Default: `0`).
- `force_log_sync_from_start_block_number`: Force sync from start block even if progress exists (Default: `false`).
- `confirmation_block_count`: Blocks required for confirmation to handle reorgs (Default: `3`).
- `log_page_size`: Max number of logs per poll (Default: `999`).
- `max_cache_data_size`: Max cached data size in bytes (Default: `104857600`).
- `cache_tx_seq_ttl`: Cache TTL for tx sequence entries (Default: `500`).
- `rate_limit_retries`: Retries after RPC timeouts (Default: `100`).
- `timeout_retries`: Retries for rate-limited responses (Default: `100`).
- `initial_backoff`: Initial backoff in ms before retry (Default: `500`).
- `recover_query_delay`: Delay in ms between paginated getLogs calls (Default: `50`).
- `default_finalized_block_count`: Finality lag assumed behind latest block (Default: `100`).
- `remove_finalized_block_interval_minutes`: Interval in minutes to prune finalized blocks (Default: `30`).
- `watch_loop_wait_time_ms`: Watch loop delay in ms (Default: `500`).
- `blockchain_rpc_timeout_secs`: RPC connect/read timeout in seconds (Default: `120`).

**Chunk Pool**
- `chunk_pool_write_window_size`: Max threads per file upload (Default: `4`).
- `chunk_pool_max_cached_chunks_all`: Max cached chunk bytes across all files (Default: `4194304`).
- `chunk_pool_max_writings`: Max concurrent file uploads (Default: `16`).
- `chunk_pool_expiration_time_secs`: Cached chunk expiration in seconds (Default: `300`).

**Database**
- `db_dir`: Directory to store data (Default: `db`).
- `db_max_num_sectors`: Max number of chunk entries to store (Default: None).
- `prune_check_time_s`: Interval to check prune conditions in seconds (Default: `60`).
- `prune_batch_size`: Number of entries per prune batch (Default: `16384`).
- `prune_batch_wait_time_ms`: Wait between prune batches in ms (Default: `1000`).
- `merkle_node_cache_capacity`: Merkle node cache capacity in bytes (Default: `33554432`).

**Misc**
- `log_config_file`: Log configuration file name (Default: `log_config`).
- `log_directory`: Directory for log output (Default: `log`).

**Mining**
- `mine_contract_address`: Mine contract address (Default: empty).
- `miner_id`: Optional miner ID (Default: None).
- `miner_key`: Miner private key (Default: None).
- `miner_cpu_percentage`: CPU usage percentage for mining (Default: `100`).
- `mine_iter_batch_size`: Mining iteration batch size (Default: `100`).
- `reward_contract_address`: Reward contract address (Default: empty).
- `shard_position`: Shard selector in `<shard_id>/<shard_number>` format (Default: None).
- `mine_context_query_seconds`: Interval to query mine context in seconds (Default: `5`).

<Tabs>
  <TabItem value="testnet" label="Testnet">

### Configuration

1. Copy the testnet configuration:

```bash
cd run
cp config-testnet-turbo.toml config.toml
```

2. Update the following fields in `config.toml`:

```toml