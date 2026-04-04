# 0G AI Context for Coding Assistants

This page provides comprehensive context about 0G infrastructure to help AI coding assistants help developers build on 0G. All information is extracted from the official documentation at https://docs.0g.ai.

## Network Configurations

### Testnet (Galileo)
**Explorer**: [https://explorer.0g.ai/testnet/home](https://explorer.0g.ai/testnet/home)

| Parameter | Value |
|-----------|-------|
| **Network Name** | 0G-Galileo-Testnet |
| **Chain ID** | 16602 |
| **Token Symbol** | 0G |
| **RPC Endpoint** | https://evmrpc-testnet.0g.ai |
| **Block Explorer** | https://chainscan-galileo.0g.ai |
| **Storage Explorer** | https://storagescan-galileo.0g.ai |
| **Validator Dashboard** | https://testnet.0g.explorers.guru |
| **Faucet** | https://faucet.0g.ai (0.1 0G/day) |
| **Storage Start Block** | 1 |
| **DA Start Block** | 940000 |

**Documentation**: [https://docs.0g.ai/developer-hub/testnet/testnet-overview](https://docs.0g.ai/developer-hub/testnet/testnet-overview)

**Third-Party RPCs (Recommended for Production)**:
- QuickNode: https://www.quicknode.com/chains/0g
- ThirdWeb: https://thirdweb.com/0g-galileo-testnet-16601
- Ankr: https://www.ankr.com/rpc/0g/
- dRPC NodeCloud: https://drpc.org/chainlist/0g-galileo-testnet-rpc

### Mainnet (Aristotle)
**Explorer**: [https://explorer.0g.ai/mainnet/home](https://explorer.0g.ai/mainnet/home)

| Parameter | Value |
|-----------|-------|
| **Network Name** | 0G Mainnet |
| **Chain ID** | 16661 |
| **Token Symbol** | 0G |
| **RPC Endpoint** | https://evmrpc.0g.ai |
| **Storage Indexer** | https://indexer-storage-turbo.0g.ai |
| **Block Explorer** | https://chainscan.0g.ai |
| **Storage Start Block** | 2387557 |

**Documentation**: [https://docs.0g.ai/developer-hub/mainnet/mainnet-overview](https://docs.0g.ai/developer-hub/mainnet/mainnet-overview)

**Third-Party RPCs (Recommended for Production)**:
- QuickNode: https://www.quicknode.com/chains/0g
- ThirdWeb: https://thirdweb.com/0g-aristotle
- Ankr: https://www.ankr.com/rpc/0g/

## Smart Contract Addresses

### Testnet Contracts

| Contract | Address | Purpose |
|----------|---------|---------|
| **Flow** | `0x22E03a6A89B950F1c82ec5e74F8eCa321a105296` | Storage data flow management |
| **Mine** | `0x00A9E9604b0538e06b268Fb297Df333337f9593b` | Storage mining rewards |
| **Reward** | `0xA97B57b4BdFEA2D0a25e535bd849ad4e6C440A69` | Reward distribution |
| **DAEntrance** | `0xE75A073dA5bb7b0eC622170Fd268f35E675a957B` | DA blob submission |
| **DASigners** | `0x0000000000000000000000000000000000001000` | DA signer management (precompile) |
| **WrappedOGBase** | `0x0000000000000000000000000000000000001001` | Wrapped native token (precompile) |
| **Compute Ledger** | `0xE70830508dAc0A97e6c087c75f402f9Be669E406` | Compute network payment ledger |
| **Compute Inference** | `0xa79F4c8311FF93C06b8CfB403690cc987c93F91E` | Compute inference service |
| **Compute FineTuning** | `0xaC66eBd174435c04F1449BBa08157a707B6fa7b1` | Compute fine-tuning service |

### Mainnet Contracts

| Contract | Address | Purpose |
|----------|---------|---------|
| **Flow** | `0x62D4144dB0F0a6fBBaeb6296c785C71B3D57C526` | Storage data flow management |
| **Mine** | `0xCd01c5Cd953971CE4C2c9bFb95610236a7F414fe` | Storage mining rewards |
| **Reward** | `0x457aC76B58ffcDc118AABD6DbC63ff9072880870` | Reward distribution |
| **DASigners** | `0x0000000000000000000000000000000000001000` | DA signer management (precompile) |
| **WrappedOGBase** | `0x0000000000000000000000000000000000001001` | Wrapped native token (precompile) |
| **Compute Ledger** | `0x2dE54c845Cd948B72D2e32e39586fe89607074E3` | Compute network payment ledger |
| **Compute Inference** | `0x47340d900bdFec2BD393c626E12ea0656F938d84` | Compute inference service |
| **Compute FineTuning** | `0x4e3474095518883744ddf135b7E0A23301c7F9c0` | Compute fine-tuning service |

## 0G Services Overview

### 0G Chain
**Documentation**: [https://docs.0g.ai/concepts/chain](https://docs.0g.ai/concepts/chain)

Fastest modular AI chain with 11,000 TPS per Shard, sub-second finality, and full EVM compatibility.

**Key Features**:
- **Full EVM compatibility** - Use existing Ethereum tools (Hardhat, Foundry, Remix)
- **11,000 TPS per Shard** with sub-second finality
- **Same as Ethereum development** - just different RPC endpoint
- Optimized CometBFT consensus
- Native precompiled contracts for DA and wrapped tokens

**Deploy Smart Contracts**:

Using Hardhat:
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
  },
  solidity: "0.8.20"
};
```

Using Foundry:
```bash