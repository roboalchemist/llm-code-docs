# Deploy Smart Contracts on 0G Chain

Deploy smart contracts on 0G Chain - an EVM-compatible blockchain with built-in AI capabilities.

## Why Deploy on 0G Chain?

### ⚡ Performance Benefits

- **11,000 TPS per Shard**: Higher throughput than Ethereum
- **Low Fees**: Fraction of mainnet costs
- **Sub-second Finality**: Near-instant transaction confirmation

### 🔧 Latest EVM Compatibility

- **Pectra & Cancun-Deneb Support**: Leverage newest Ethereum capabilities
- **Future-Ready**: Architecture designed for quick integration of upcoming EVM upgrades
- **Familiar Tools**: Use Hardhat, Foundry, Remix
- **No Learning Curve**: Deploy like any EVM chain

## Prerequisites

Before deploying contracts on 0G Chain, ensure you have:

- Node.js 16+ installed (for Hardhat/Truffle)
- Rust installed (for Foundry)
- A wallet with testnet 0G tokens ([get from faucet](https://faucet.0g.ai))
- Basic Solidity knowledge

## Steps to Deploy Your Contract

### Step 1: Prepare Your Smart Contract Code

Write your contract code as you would for any Ethereum-compatible blockchain, ensuring that it meets the requirements for your specific use case.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

contract MyToken {
    mapping(address => uint256) public balances;
    uint256 public totalSupply;

    constructor(uint256 _initialSupply) {
        totalSupply = _initialSupply;
        balances[msg.sender] = _initialSupply;
    }

    function transfer(address to, uint256 amount) public returns (bool) {
        require(balances[msg.sender] >= amount, "Insufficient balance");
        balances[msg.sender] -= amount;
        balances[to] += amount;
        return true;
    }
}
```

### Step 2: Compile Your Smart Contract

Use `solc` or another compatible Solidity compiler to compile your smart contract.

**Important**: When compiling, specify `--evm-version cancun` to ensure compatibility with the latest EVM upgrades supported by 0G Chain.

**Using solc directly**:

```bash
solc --evm-version cancun --bin --abi MyToken.sol
```

**Using Hardhat**:

```javascript
// hardhat.config.js
module.exports = {
  solidity: {
    version: "0.8.19",
    settings: {
      evmVersion: "cancun",
      optimizer: {
        enabled: true,
        runs: 200,
      },
    },
  },
};
```

**Using Foundry**:

```toml