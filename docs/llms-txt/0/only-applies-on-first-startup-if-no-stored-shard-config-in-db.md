# Only applies on first startup if no stored shard config in db
shard_position = "0/2"
```

Sharding allows controlling how much data your node stores:
- `"0/2"` or `"1/2"` = 50% of total data (each on specific ranges)
- `"0/4"` to `"3/4"` = 25% of total data each
- Initial setup is deterministic (shard_id maps to specific range)
- Auto-splitting is NOT deterministic (random assignment when capacity exceeded)

**Run Storage Node**:
```bash
cd run
../target/release/zgs_node --config config.toml --miner-key <your_private_key>
```

**Documentation**: [https://docs.0g.ai/run-a-node/storage-node](https://docs.0g.ai/run-a-node/storage-node)

## Developer Tools

### Indexing with Goldsky

**Website**: https://docs.goldsky.com/chains/0g

**Products**:
- **Subgraphs**: GraphQL indexing for smart contracts
- **Mirror**: Real-time data streaming to databases

**Documentation**: [https://docs.0g.ai/developer-hub/building-on-0g/indexing/goldsky](https://docs.0g.ai/developer-hub/building-on-0g/indexing/goldsky)

### Rollup-as-a-Service

**Caldera on 0G DA**: [https://docs.0g.ai/developer-hub/building-on-0g/rollup-as-a-service/caldera-on-0g-da](https://docs.0g.ai/developer-hub/building-on-0g/rollup-as-a-service/caldera-on-0g-da)

### Smart Contract Development

**Deploy with Hardhat**:
```javascript
// hardhat.config.js
module.exports = {
  networks: {
    testnet: {
      url: "https://evmrpc-testnet.0g.ai",
      chainId: 16602,
      accounts: ["YOUR_PRIVATE_KEY"]
    },
    mainnet: {
      url: "https://evmrpc.0g.ai",
      chainId: 16661,
      accounts: ["YOUR_PRIVATE_KEY"]
    }
  }
};
```

**Deploy with Foundry**:
```bash