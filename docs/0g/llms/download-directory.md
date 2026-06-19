# Download directory
0g-storage-client download-dir \
  --indexer https://indexer-storage-testnet-turbo.0g.ai \
  --root <DIRECTORY_ROOT_HASH> \
  --file /path/to/output
```

**Documentation Links**:
- SDK Guide: [https://docs.0g.ai/developer-hub/building-on-0g/storage/sdk](https://docs.0g.ai/developer-hub/building-on-0g/storage/sdk)
- CLI Guide: [https://docs.0g.ai/developer-hub/building-on-0g/storage/storage-cli](https://docs.0g.ai/developer-hub/building-on-0g/storage/storage-cli)

**GitHub Repositories**:
- Storage Node: https://github.com/0gfoundation/0g-storage-node
- Storage KV: https://github.com/0gfoundation/0g-storage-kv
- Storage Client/CLI: https://github.com/0gfoundation/0g-storage-client
- TypeScript SDK: https://github.com/0gfoundation/0g-ts-sdk
- Python SDK: https://github.com/0gfoundation/0g-storage-client
- Go SDK: https://github.com/0gfoundation/0g-storage-client

### 0G Compute
**Documentation**: [https://docs.0g.ai/concepts/compute](https://docs.0g.ai/concepts/compute)

Decentralized GPU marketplace offering 90% cheaper AI workloads with OpenAI SDK compatibility.

**Key Features**:
- 90% cost reduction vs traditional cloud (e.g., $0.003 vs $0.03 per 1K tokens)
- Pay-per-use pricing (no subscriptions or monthly minimums)
- OpenAI SDK compatible - drop-in replacement
- Smart contract escrow for trustless payments
- TEE (Trusted Execution Environment) for secure processing
- 50-100ms inference latency
- Supports: Chatbot (LLM), Text-to-Image, Speech-to-Text

**DePIN Partners**:
- **io.net**: 300,000+ GPUs across 139 countries
- **Aethir**: 43,000+ enterprise-grade GPUs, 3,000+ H100s/H200s

**Quick Start (5 minutes)**:

Install CLI:
```bash
pnpm add @0glabs/0g-serving-broker -g
```

Option 1 - Web UI (Easiest):
```bash