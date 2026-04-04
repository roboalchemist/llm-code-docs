# Add to PATH if not already configured
export PATH=~/go/bin:$PATH
```

## Command Overview

The CLI provides a comprehensive set of commands for storage operations:

```
0g-storage-client [command] [flags]

Available Commands:
  upload      Upload file to 0G Storage network
  download    Download file from 0G Storage network
  upload-dir  Upload directory to 0G Storage network
  download-dir Download directory from 0G Storage network
  diff-dir    Diff directory from 0G Storage network
  gen         Generate test files
  kv-write    Write to KV streams
  kv-read     Read KV streams
  gateway     Start gateway service
  indexer     Start indexer service
  deploy      Deploy storage contracts
  completion  Generate shell completion scripts
  help        Get help for any command

Global Flags:
  --gas-limit uint                Custom gas limit to send transaction
  --gas-price uint                Custom gas price to send transaction
  --log-level string              Log level (default "info")
  --log-color-disabled            Force to disable colorful logs
  --rpc-retry-count int           Retry count for rpc request (default 5)
  --rpc-retry-interval duration   Retry interval for rpc request (default 5s)
  --rpc-timeout duration          Timeout for single rpc request (default 30s)
  --web3-log-enabled              Enable Web3 RPC logging
```

## Core Operations

### File Upload

Upload files to the 0G Storage network using the indexer service or explicit nodes:

```bash
0g-storage-client upload \
  --url <blockchain_rpc_endpoint> \
  --key <private_key> \
  --indexer <storage_indexer_endpoint> \
  --file <file_path>
```

**Parameters:**
`--url` is the chain RPC endpoint, `--key` is your private key, and `--file` is the path to the file you want to upload. Use exactly one of `--indexer` or `--node`.

Common flags include `--tags`, `--submitter`, `--expected-replica`, `--skip-tx`, `--finality-required`, `--task-size`, `--fast-mode`, `--fragment-size`, `--routines`, `--fee`, `--nonce`, `--max-gas-price`, `--n-retries`, `--step`, `--method`, `--full-trusted`, `--timeout`, `--flow-address`, and `--market-address`.

Fee notes (turbo):
- `unitPrice = 11 / pricePerToken / 1024 * 256`. If `pricePerToken = 1`, then `unitPrice = 2.75` (tokens), or `2.75e18` a0gi.
- `pricePerSector(256B)/month = lifetimeMonth * unitPrice * 1e18 / 1024 / 1024 / 1024` (no `/12` since $11 is per TB per month).

### File Download

Download files from the network using the indexer or explicit nodes:

```bash
0g-storage-client download \
  --indexer <storage_indexer_endpoint> \
  --root <file_root_hash> \
  --file <output_file_path>
```

**Parameters:**
`--file` is the output path. Use exactly one of `--indexer` or `--node`. Use exactly one of `--root` or `--roots`.

### Download with Verification

Enable proof verification for enhanced security:

```bash
0g-storage-client download \
  --indexer <storage_indexer_endpoint> \
  --root <file_root_hash> \
  --file <output_file_path> \
  --proof
```

The `--proof` flag requests cryptographic proof of data integrity from the storage node.

### Directory Upload

Upload an entire directory using explicit storage nodes:

```bash
0g-storage-client upload-dir \
  --url <blockchain_rpc_endpoint> \
  --key <private_key> \
  --node <storage_node_endpoint> \
  --file <directory_path>
```

### Directory Download

Download a directory by root:

```bash
0g-storage-client download-dir \
  --indexer <storage_indexer_endpoint> \
  --root <directory_root_hash> \
  --file <output_directory>
```

### Directory Diff

Compare a local directory with the on-chain version:

```bash
0g-storage-client diff-dir \
  --indexer <storage_indexer_endpoint> \
  --root <directory_root_hash> \
  --file <local_directory>
```

## Practical Examples

### Upload Example

```bash