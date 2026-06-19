# Download
client.download_file(root_hash, "/path/to/output")
```

### Chain/Smart Contract Starter Kit
**Hardhat Project**:
```bash
npm install --save-dev hardhat @nomicfoundation/hardhat-toolbox
npx hardhat init
```
```javascript
// hardhat.config.js
require("@nomicfoundation/hardhat-toolbox");

module.exports = {
  solidity: "0.8.20",
  networks: {
    testnet: {
      url: "https://evmrpc-testnet.0g.ai",
      chainId: 16602,
      accounts: [process.env.PRIVATE_KEY]
    }
  }
};
```
```bash
npx hardhat compile
npx hardhat run scripts/deploy.js --network testnet
```

**Foundry Project**:
```bash
forge init my-project
cd my-project
```
```bash