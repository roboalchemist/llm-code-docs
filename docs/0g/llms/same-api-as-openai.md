# Same API as OpenAI
response = client.chat.completions.create(
    model="<model_name>",
    messages=[{"role": "user", "content": "Hello!"}]
)
```

### Storage Starter Kit
**TypeScript Example**:
```bash
npm install @0glabs/0g-ts-sdk ethers
```
```typescript
import { ZgFile, Indexer } from "@0glabs/0g-ts-sdk";
import { ethers } from "ethers";

const provider = new ethers.JsonRpcProvider("https://evmrpc-testnet.0g.ai");
const signer = new ethers.Wallet("YOUR_PRIVATE_KEY", provider);
const indexer = new Indexer("https://indexer-storage-testnet-turbo.0g.ai");

// Upload file
const file = await ZgFile.fromFilePath("/path/to/file");
const [tree, treeErr] = await file.merkleTree();
console.log("Root Hash:", tree?.rootHash());
const [tx, uploadErr] = await indexer.upload(file, "https://evmrpc-testnet.0g.ai", signer);
await file.close();

// Download file
const err = await indexer.download(rootHash, "/path/to/output", true);
```

**Python Example**:
```bash
pip install 0g-storage-client
```
```python
from storage_client import ZgStorageClient

client = ZgStorageClient(
    rpc_endpoint="https://evmrpc-testnet.0g.ai",
    contract_address="0x22E03a6A89B950F1c82ec5e74F8eCa321a105296",
    private_key="YOUR_PRIVATE_KEY"
)