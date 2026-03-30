# Your private key for mining (64 chars, no '0x' prefix)
miner_key = "YOUR_PRIVATE_KEY"
```

3. The mainnet configuration includes predefined boot nodes for network connectivity:

```toml
network_boot_nodes = ["/ip4/34.66.131.173/udp/1234/p2p/16Uiu2HAmG81UgZ1JJLx9T2HqELgJNP36ChHzYkCdA9HdxvAbb5jQ","/ip4/34.60.163.4/udp/1234/p2p/16Uiu2HAmL3DoA7e7mbxs7CkeCPtNrAcfJFFtLpJDr2HWuR6QwJ8k","/ip4/34.169.236.186/udp/1234/p2p/16Uiu2HAm489RdhEgZUFmNTR4jdLEE4HjrvwaPCkEpSYSgvqi1CbR","/ip4/34.71.110.60/udp/1234/p2p/16Uiu2HAmBfGfbLNRegcqihiuXhgSXWNpgiGm6EwW2SYexfPUNUHQ"]
```

### Sharding Configuration

Sharding allows you to control how much data your storage node stores. This is particularly useful when disk space is limited.

#### Understanding Shard Position

The `shard_position` parameter determines which portion of the total network data your node stores:

```toml