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

2. Run the testnet storage service:
```bash
cd run
../target/release/zgs_node --config config.toml --miner-key <your_private_key>
```

  </TabItem>
  <TabItem value="mainnet" label="Mainnet">

### Configuration

1. Copy the mainnet configuration:

```bash
cd run
cp config-mainnet-turbo.toml config.toml
```

2. Update the following fields in `config.toml`:

```toml