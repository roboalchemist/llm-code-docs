# With verification
0g-storage-client download \
  --indexer <storage_indexer_endpoint> \
  --root 0xc5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470 \
  --file ./downloads/report.pdf \
  --proof
```

## Key-Value Operations

### Write to KV Store (Batch Operations)

Write multiple key-value pairs in a single operation:

```bash
0g-storage-client kv-write \
  --url <blockchain_rpc_endpoint> \
  --key <private_key> \
  --indexer <storage_indexer_endpoint> \
  --stream-id <stream_id> \
  --stream-keys <comma_separated_keys> \
  --stream-values <comma_separated_values>
```

**Important:** `--stream-keys` and `--stream-values` are comma-separated string lists and their length must be equal.

You can use `--indexer` for node selection or pass storage nodes directly with `--node`. If `--indexer` is omitted, `--node` is required.

**Example:**
```bash
0g-storage-client kv-write \
  --url <blockchain_rpc_endpoint> \
  --key YOUR_PRIVATE_KEY \
  --indexer <storage_indexer_endpoint> \
  --stream-id 1 \
  --stream-keys "key1,key2,key3" \
  --stream-values "value1,value2,value3"
```

### Read from KV Store

```bash
0g-storage-client kv-read \
  --node <kv_node_rpc_endpoint> \
  --stream-id <stream_id> \
  --stream-keys <comma_separated_keys>
```

:::info KV Read Endpoint
Note that for KV read operations, you need to specify `--node` as the URL of a KV node, not the indexer endpoint.
:::

## RESTful API Gateway

The indexer service provides a RESTful API gateway for easy HTTP-based file access:

### File Downloads via HTTP

**By Transaction Sequence Number:**
```
GET /file?txSeq=7
```

**By File Merkle Root:**
```
GET /file?root=0x0376e0d95e483b62d5100968ed17fe1b1d84f0bc5d9bda8000cdfd3f39a59927
```

**With Custom Filename:**
```
GET /file?txSeq=7&name=foo.log
```

### Folder Support

Download specific files from within structured folders:

**By Transaction Sequence:**
```
GET /file/{txSeq}/path/to/file
```

**By Merkle Root:**
```
GET /file/{merkleRoot}/path/to/file
```

## Advanced Features

### Custom Gas Settings

Control transaction costs with custom gas parameters:

```bash
0g-storage-client upload \
  --gas-limit 3000000 \
  --gas-price 10000000000 \
  # ... other parameters
```

### RPC Configuration

Configure RPC retry behavior and timeouts:

```bash
0g-storage-client upload \
  --rpc-retry-count 10 \
  --rpc-retry-interval 3s \
  --rpc-timeout 60s \
  # ... other parameters
```

### Logging Configuration

Adjust logging for debugging:

```bash