# Fish
0g-storage-client completion fish > ~/.config/fish/completions/0g-storage-client.fish
```

## Indexer Service

The indexer service provides two types of storage node discovery:

### Trusted Nodes
Well-maintained nodes that provide stable and reliable service.

### Discovered Nodes
Nodes discovered automatically through the P2P network.

The indexer intelligently routes data to appropriate storage nodes based on their shard configurations, eliminating the need to manually specify storage nodes or contract addresses.

## Important Considerations

### Network Configuration

:::info Required Information
**RPC endpoints** and **indexer endpoints** are published in the network overview docs. Use the current values for your network. Keep private keys secure and never share them.
:::

### File Management

- **Root Hash Storage**: Save file root hashes after upload - they're required for downloads
- **Transaction Monitoring**: Track upload transactions on the blockchain explorer
- **Indexer Benefits**: The indexer automatically selects optimal storage nodes for better reliability

## Running Services

### Indexer Service

The indexer helps users find suitable storage nodes:

```bash
0g-storage-client indexer \
  --endpoint :12345 \
  --node <storage_node_endpoint>
```

Or start with a trusted node list:

```bash
0g-storage-client indexer \
  --endpoint :12345 \
  --trusted <node1,node2>
```

### Gateway Service

Run a gateway to provide HTTP access to storage:

```bash
0g-storage-client gateway \
  --nodes <storage_node_endpoint>
```

Optionally specify a local file repo:

```bash
0g-storage-client gateway \
  --nodes <storage_node_endpoint> \
  --repo <local_path>
```

## Automation Examples

### Backup Script

Create automated backup scripts:

```bash
#!/bin/bash