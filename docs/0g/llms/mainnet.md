# Mainnet
forge create --rpc-url https://evmrpc.0g.ai \
  --private-key YOUR_PRIVATE_KEY \
  src/MyContract.sol:MyContract
```

Using Remix:
1. Open Remix IDE
2. Compile your contract
3. Go to Deploy & Run Transactions
4. Select "Injected Provider - MetaMask"
5. Ensure MetaMask is connected to 0G network
6. Deploy!

**Precompiled Contracts**:

DASigners (0x0000000000000000000000000000000000001000):
```solidity
// Query DA signers and epochs
function getEpochNumber(uint256 blockNumber) external view returns (uint256);
function getQuorum(uint256 epochNumber, uint256 quorumId) external view returns (Signer[] memory);
function isSigner(uint256 epochNumber, address account) external view returns (bool);
```

WrappedOGBase (0x0000000000000000000000000000000000001001):
```solidity
// Wrapped native token (like WETH)
function deposit() external payable;
function withdraw(uint256 amount) external;
function balanceOf(address account) external view returns (uint256);
```

**Verification & Indexing**:
- **Goldsky**: GraphQL indexing and real-time data streaming
  - Docs: https://docs.goldsky.com/chains/0g
  - Guide: [https://docs.0g.ai/developer-hub/building-on-0g/indexing/goldsky](https://docs.0g.ai/developer-hub/building-on-0g/indexing/goldsky)

**Documentation Links**:
- Deploy Contracts: [https://docs.0g.ai/developer-hub/building-on-0g/contracts-on-0g/deploy-contracts](https://docs.0g.ai/developer-hub/building-on-0g/contracts-on-0g/deploy-contracts)
- Precompiles: [https://docs.0g.ai/developer-hub/building-on-0g/contracts-on-0g/precompiles/overview](https://docs.0g.ai/developer-hub/building-on-0g/contracts-on-0g/precompiles/overview)
- Staking: [https://docs.0g.ai/developer-hub/building-on-0g/contracts-on-0g/staking-interfaces](https://docs.0g.ai/developer-hub/building-on-0g/contracts-on-0g/staking-interfaces)
- Validator Contracts: [https://docs.0g.ai/developer-hub/building-on-0g/contracts-on-0g/validator-contract-functions](https://docs.0g.ai/developer-hub/building-on-0g/contracts-on-0g/validator-contract-functions)

### 0G Storage
**Documentation**: [https://docs.0g.ai/concepts/storage](https://docs.0g.ai/concepts/storage)

Decentralized storage offering 95% lower costs than AWS with instant retrieval.

**Key Features**:
- 95% cheaper than centralized alternatives
- 200 MBPS retrieval speed
- Proven TB-scale operations
- Two storage layers: Log (immutable) + KV (mutable)
- Proof of Random Access (PoRA) consensus

**SDK Installation**:

TypeScript/JavaScript:
```bash
npm install @0glabs/0g-ts-sdk ethers
```

Python:
```bash
pip install 0g-storage-client
```

Go:
```bash
go get github.com/0gfoundation/0g-storage-client
```

**Quick Start Examples**:

TypeScript - Upload File:
```typescript
import { ZgFile, Indexer } from "@0glabs/0g-ts-sdk";
import { ethers } from "ethers";

const provider = new ethers.JsonRpcProvider("https://evmrpc-testnet.0g.ai");
const signer = new ethers.Wallet("YOUR_PRIVATE_KEY", provider);
const indexer = new Indexer("https://indexer-storage-testnet-turbo.0g.ai");

const file = await ZgFile.fromFilePath("/path/to/file");
const [tree, treeErr] = await file.merkleTree();
console.log("Root Hash:", tree?.rootHash());

const [tx, uploadErr] = await indexer.upload(file, "https://evmrpc-testnet.0g.ai", signer);
await file.close();
```

Python - Upload File:
```python
from storage_client import ZgStorageClient

client = ZgStorageClient(
    rpc_endpoint="https://evmrpc-testnet.0g.ai",
    contract_address="0x22E03a6A89B950F1c82ec5e74F8eCa321a105296",
    private_key="YOUR_PRIVATE_KEY"
)

root_hash = client.upload_file("/path/to/file")
```

**CLI Tool**:
```bash