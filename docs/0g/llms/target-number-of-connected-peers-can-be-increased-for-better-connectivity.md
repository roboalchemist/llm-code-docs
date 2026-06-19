# Target number of connected peers (can be increased for better connectivity)
network_target_peers = 50
```

### Sharding Configuration

Sharding allows you to control how much data your storage node stores. This is particularly useful when disk space is limited.

#### Understanding Shard Position

The `shard_position` parameter determines which portion of the total network data your node stores:

```toml