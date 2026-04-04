# Monitor progress
0g-compute-cli fine-tuning get-task --task-id <TASK_ID>
```

**Documentation Links**:
- Overview: [https://docs.0g.ai/developer-hub/building-on-0g/compute-network/overview](https://docs.0g.ai/developer-hub/building-on-0g/compute-network/overview)
- Inference: [https://docs.0g.ai/developer-hub/building-on-0g/compute-network/inference](https://docs.0g.ai/developer-hub/building-on-0g/compute-network/inference)
- Fine-tuning: [https://docs.0g.ai/developer-hub/building-on-0g/compute-network/fine-tuning](https://docs.0g.ai/developer-hub/building-on-0g/compute-network/fine-tuning)
- Account Management: [https://docs.0g.ai/developer-hub/building-on-0g/compute-network/account-management](https://docs.0g.ai/developer-hub/building-on-0g/compute-network/account-management)
- Provider Setup: [https://docs.0g.ai/developer-hub/building-on-0g/compute-network/inference-provider](https://docs.0g.ai/developer-hub/building-on-0g/compute-network/inference-provider)

### 0G DA (Data Availability)
**Documentation**: [https://docs.0g.ai/concepts/da](https://docs.0g.ai/concepts/da)

Scalable data availability layer for rollups with 50 Gbps throughput.

**Key Features**:
- 50 Gbps demonstrated throughput
- VRF-based node selection
- Inherits Ethereum security

**For Rollup Developers**:
- OP Stack Integration: [https://docs.0g.ai/developer-hub/building-on-0g/rollups-and-appchains/op-stack-on-0g-da](https://docs.0g.ai/developer-hub/building-on-0g/rollups-and-appchains/op-stack-on-0g-da)
  - Repo: https://github.com/0gfoundation/0g-da-op-plasma
- Arbitrum Nitro: [https://docs.0g.ai/developer-hub/building-on-0g/rollups-and-appchains/arbitrum-nitro-on-0g-da](https://docs.0g.ai/developer-hub/building-on-0g/rollups-and-appchains/arbitrum-nitro-on-0g-da)
  - Repo: https://github.com/0gfoundation/nitro
- Integration Guide: [https://docs.0g.ai/developer-hub/building-on-0g/da-integration](https://docs.0g.ai/developer-hub/building-on-0g/da-integration)

### INFT (Intelligent NFTs)
**Documentation**: [https://docs.0g.ai/concepts/inft](https://docs.0g.ai/concepts/inft)

NFT standard (ERC-7857) for tokenizing AI agents with complete intelligence.

**Key Features**:
- Extends ERC-721 standard
- Encrypted metadata storage via 0G Storage
- Secure re-encryption for ownership transfer
- Oracle verification
- True AI ownership transfer

**Use Cases**:
- AI Trading Bots
- Personal Assistants
- Game Characters
- Content Creation AI
- Research Tools

**Documentation Links**:
- INFT Overview: [https://docs.0g.ai/developer-hub/building-on-0g/inft/inft-overview](https://docs.0g.ai/developer-hub/building-on-0g/inft/inft-overview)
- ERC-7857 Standard: [https://docs.0g.ai/developer-hub/building-on-0g/inft/erc7857](https://docs.0g.ai/developer-hub/building-on-0g/inft/erc7857)
- Integration Guide: [https://docs.0g.ai/developer-hub/building-on-0g/inft/integration](https://docs.0g.ai/developer-hub/building-on-0g/inft/integration)

## Running Nodes

### Hardware Requirements

| Node Type | Memory | CPU | Disk | Bandwidth | Purpose |
|-----------|--------|-----|------|-----------|---------|
| **Validator (Mainnet)** | 64 GB | 8 cores | 1 TB NVMe | 100 Mbps | Transaction validation |
| **Validator (Testnet)** | 64 GB | 8 cores | 4 TB NVMe | 100 Mbps | Transaction validation |
| **Storage Node** | 32 GB | 8 cores | 500GB-1TB SSD | 100 Mbps | Data storage |
| **Storage KV** | 32 GB | 8 cores | Flexible | - | Key-value storage |
| **DA Node** | 16 GB | 8 cores | 1 TB NVMe | 100 Mbps | Blob verification |
| **Archival Node** | 64 GB | 8 cores | Large NVMe | 100 Mbps | Historical data |

### Validator Node Setup

**Mainnet (Aristotle)**:
```bash