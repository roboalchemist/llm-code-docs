# This only applies if there is no stored shard config in db
shard_position = "0/2"
```

**Format**: `<shard_id>/<shard_number>`
- `shard_id`: Which shard this node stores (0, 1, 2, 3, etc.)
- `shard_number`: Total number of shards (must be a power of 2: 2, 4, 8, 16, etc.)

**Examples**:
- `shard_position = "0/2"` → Store 50% of data (shard 0 of 2 total shards)
- `shard_position = "1/2"` → Store 50% of data (shard 1 of 2 total shards)
- `shard_position = "0/4"` → Store 25% of data (shard 0 of 4 total shards)
- `shard_position = "2/4"` → Store 25% of data (shard 2 of 4 total shards)

Each shard stores a **specific range** of the total data. For example, with `0/2` and `1/2`, both store 50% of data but on different, non-overlapping ranges.

#### How Sharding Works

Consider a scenario with 128 GB total network data and a 100 GB disk:

1. **Initial Setup** (`shard_position = "0/2"`):
   - Your node stores 64 GB (50% of 128 GB)
   - Stores a specific, deterministic data range
   - Fits comfortably on your 100 GB disk

2. **Network Growth** (total data becomes 256 GB):
   - Your node would be responsible for 128 GB (50% of 256 GB)
   - This exceeds your 100 GB disk capacity
   - **Automatic adjustment**: Node automatically splits to `x/4`
   - Now stores 64 GB (25% of 256 GB)
   - `shard_id` changes: `0` → `0 or 2`, `1` → `1 or 3` (randomly assigned by the node, you cannot control which)

#### Automatic Shard Division

When network data exceeds your disk capacity, the node automatically:
- Doubles the shard number (2 → 4 → 8 → 16, etc.)
- Randomly reassigns to a new shard within the split (you cannot control which)
- Maintains storage within disk limits

:::warning Important Notes
- **Initial setup is deterministic**: When you first configure `shard_position`, the shard_id deterministically maps to a specific data range
- This setting only applies on **first startup** if no shard config exists in the database
- **Auto-splitting is NOT deterministic**: When the node automatically splits shards due to capacity limits, you cannot control which new shard_id you get - it's randomly assigned
- Once shard config is stored in the database, the node manages all future shard adjustments automatically
:::

#### Choosing Your Shard Configuration

To determine the right shard configuration:

1. **Estimate network data size**: Check current total data on the network
2. **Consider disk capacity**: Leave headroom for growth (e.g., use 70-80% of disk)
3. **Calculate shard number**: `shard_number = total_data / (disk_capacity * 0.75)`
4. **Round up to nearest power of 2**: 2, 4, 8, 16, 32, etc.

**Example**:
- Network data: 500 GB
- Your disk: 200 GB
- Safe storage: 150 GB (75% of disk)
- Calculation: 500 / 150 ≈ 3.33 → Round up to 4
- Configuration: `shard_position = "0/4"` (stores ~125 GB)

### Running the Node

1. Check configuration options:
```bash
../target/release/zgs_node -h
```

2. Run the mainnet storage service:
```bash
cd run
../target/release/zgs_node --config config.toml --miner-key <your_private_key>
```

**Important Mainnet Notes**:
- Ensure your miner key has sufficient 0G tokens for transaction fees
- Mainnet nodes should have stable internet connectivity and sufficient bandwidth
- Monitor your node's performance and logs regularly

</TabItem>
</Tabs>

## Snapshot
Make sure to only include `flow_db` and delete `data_db` under `db` folder when you use a snapshot from a 3rd party !
> Using others' `data_db` will make the node mine for others!

**Additional Notes**
*   **Security:** Keep your private key (`miner_key`) safe and secure. Anyone with access to it can control your node and potentially claim your mining rewards.

*   **Network Connectivity:** Ensure your node has a stable internet connection and that the necessary ports are open for communication with other nodes.

*   **Monitoring:** Monitor your node's logs and resource usage to ensure it's running smoothly.

*   **Updates:** Stay informed about updates to the 0G storage node software and follow the project's documentation for any changes in the setup process.

**Remember:** Running a storage node is a valuable contribution to the 0G network. You'll be helping to maintain its decentralization and robustness while earning rewards for your efforts.

  </TabItem>
  <TabItem value="docker" label="Storage KV Node">

## Overview
  0G Storage KV is a key-value store built on top of the 0G Storage system. This guide provides detailed steps to deploy and run a 0G Storage KV node.

## Prerequisites

Before setting up your 0G Storage KV node:

- Understand that 0G KV interacts with on-chain contracts and storage nodes to simulate KV data streams.
- For official deployed contract addresses, visit the [testnet information page](../developer-hub/testnet/testnet-overview.md).

## Install Dependencies

Follow the same steps to install dependencies and Rust as in the storage node setup:
<Tabs>
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

#### 1. Download the Source Code

```bash
git clone -b <latest_tag> https://github.com/0gfoundation/0g-storage-kv.git
```

#### 2. Build the Source Code

```bash
cd 0g-storage-kv