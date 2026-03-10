# foundry.toml
[profile.default]
evm_version = "cancun"
```

This step will generate the binary and ABI (Application Binary Interface) for your contract.

### Step 3: Deploy the Contract on 0G Chain

Once compiled, you can use your preferred Ethereum-compatible deployment tools, such as `web3.js`, `ethers.js`, or `hardhat`, to deploy the contract on 0G Chain.

**Configure Network Connection**:

```javascript
// For Hardhat
networks: {
  "testnet": {
    url: "https://evmrpc-testnet.0g.ai",
    chainId: 16602,
    accounts: [process.env.PRIVATE_KEY]
  },
  "mainnet": {
    url: "https://evmrpc.0g.ai",
    chainId: 16661,
    accounts: [process.env.PRIVATE_KEY]
  }
}

// For Foundry
[rpc_endpoints]
0g_testnet = "https://evmrpc-testnet.0g.ai"
0g_mainnet = "https://evmrpc.0g.ai"
```

**Deploy Using Your Preferred Tool**:

<details>
<summary>Hardhat Deployment</summary>

```javascript
// scripts/deploy.js
async function main() {
  const MyToken = await ethers.getContractFactory("MyToken");
  const token = await MyToken.deploy(1000000); // 1M initial supply
  await token.deployed();

  console.log("Token deployed to:", token.address);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
```

Run: `npx hardhat run scripts/deploy.js --network 0g-testnet`

</details>

<details>
<summary>Foundry Deployment</summary>

```bash
forge create --rpc-url https://evmrpc-testnet.0g.ai \
  --private-key $PRIVATE_KEY \
  --evm-version cancun \
  src/MyToken.sol:MyToken \
  --constructor-args 1000000
```

</details>

<details>
<summary>Truffle Deployment</summary>

```javascript
// migrations/2_deploy_token.js
module.exports = function (deployer) {
  deployer.deploy(MyToken, 1000000);
};
```

Run: `truffle migrate --network 0g-testnet`

</details>

Follow the same deployment steps as you would on Ethereum, using your 0G Chain node or RPC endpoint.

> For complete working examples using different frameworks, check out the official deployment scripts repository: 🔗 **[0G Deployment Scripts](https://github.com/0gfoundation/0g-deployment-scripts)**

### Step 4: Verify Deployment Results on 0G Chain Scan

After deployment, you can verify your contract on 0G Chain Scan, the block explorer for **[0G Chain](https://chainscan.0g.ai)** or via the provided API below:

<Tabs>
  <TabItem value="verify-hardhat" label="Hardhat" default>
    <!-- Prerequisites -->
    Make sure you have the following plugins installed:
    ```bash
    npm install --save-dev @nomicfoundation/hardhat-verify @nomicfoundation/viem @nomicfoundation/hardhat-toolbox-viem dotenv 
    ```

    To verify your contract using Hardhat, please use the following settings in your `hardhat.config.js`:

    ```javascript
    solidity: {
      ...
      settings: {
        evmVersion: "cancun", // Make sure this matches your compiler setting
        optimizer: {
          enabled: true,
          runs: 200, // Adjust based on your optimization needs
        },
        viaIR: true, // Enable if your contract uses inline assembly
        metadata: {
          bytecodeHash: "none", // Optional: Set to "none" to exclude metadata hash
        },
      },
    }
    ```

    Add the network configuration:

    ```javascript
    networks: {
      "testnet": {
        url: "https://evmrpc-testnet.0g.ai",
        chainId: 16602,
        accounts: [process.env.PRIVATE_KEY]
      },
      "mainnet": {
        url: "https://evmrpc.0g.ai",
        chainId: 16661,
        accounts: [process.env.PRIVATE_KEY]
      }
    }
    ```

    and finally, add the etherscan configuration:

    ```javascript
    etherscan: {
      apiKey: {
        testnet: "YOUR_API_KEY", // Use a placeholder if you don't have one
        mainnet: "YOUR_API_KEY"  // Use a placeholder if you don't have one
      },
      customChains: [
        {
          // Testnet
          network: "testnet",
          chainId: 16602,
          urls: {
            apiURL: "https://chainscan-galileo.0g.ai/open/api",
            browserURL: "https://chainscan-galileo.0g.ai",
          },
        },
        {
          // Mainnet
          network: "mainnet",
          chainId: 16661,
          urls: {
            apiURL: "https://chainscan.0g.ai/open/api",
            browserURL: "https://chainscan.0g.ai",
          },
        },
      ],
    },
    ```

    To verify your contract, run the following command:

    ```bash
    npx hardhat verify DEPLOYED_CONTRACT_ADDRESS --network <Network>
    ```

    You should get a success message like this:

    ```bash
    Successfully submitted source code for contract
    contracts/Contract.sol:ContractName at DEPLOYED_CONTRACT_ADDRESS
    for verification on the block explorer. Waiting for verification result...

    Successfully verified contract TokenDist on the block explorer.
    https://chainscan.0g.ai/address/<DEPLOYED_CONTRACT_ADDRESS>#code
    ```

</TabItem>
<TabItem value="verify-forge" label="Forge">
On Foundry, you can verify your contract using the `forge verify-contract` command. Make sure to set your compiler settings in `foundry.toml` as needed.

| Precompile | Verifier URL                               |
| ---------- | ------------------------------------------ |
| Testnet    | `https://chainscan-galileo.0g.ai/open/api` |
| Mainnet    | `https://chainscan.0g.ai/open/api`         |

    ```bash
    forge verify-contract \
    --chain-id <CHAIN_ID> \
    --num-of-optimizations <NUM_OPTIMIZATIONS> \
    --verifier custom \
    --verifier-api-key "PLACEHOLDER" \
    --compiler-version <COMPILER_VERSION> \
    <CONTRACT_ADDRESS> \
    src/Counter.sol:Counter \
    --verifier-url <VERIFIER_URL> \
    ```

You should get a success message like this:

    ```bash
    Submitted contract for verification:
    Response: OK
    GUID: <GUID>
    URL: https://chainscan-galileo.0g.ai/open/address/<CONTRACT_ADDRESS>
    ```

</TabItem>
</Tabs>

## Using 0G Precompiles

### Available Precompiles

| Precompile                                               | Address     | Purpose                      |
| -------------------------------------------------------- | ----------- | ---------------------------- |
| [DASigners](./precompiles/precompiles-dasigners)         | `0x...1000` | Data availability signatures |
| [Wrapped0GBase](./precompiles/precompiles-wrappedogbase) | `0x...1002` | Wrapped 0G token operations  |

## Troubleshooting

<details>
<summary>Transaction failing with "invalid opcode"?</summary>

If you're using newer experimental opcodes from unreleased Ethereum upgrades and see "invalid opcode" errors, consider:

- Use `--evm-version cancun` in your compiler settings
- Downgrade to an earlier Solidity compiler version (e.g., from 0.8.26 to 0.8.19)
</details>

<details>
<summary>Can't connect to RPC?</summary>

Try alternative endpoints:

- QuikNode: [Get endpoint](https://www.quicknode.com/chains/0g)
- ThirdWeb: [Get endpoint](https://thirdweb.com/0g-galileo-testnet-16601)
</details>

## What's Next?

- **Learn Precompiles**: [Precompiles Overview](./precompiles/precompiles-overview)
- **Storage Integration**: [0G Storage SDK](/developer-hub/building-on-0g/storage/sdk)
- **Compute Integration**: [0G Compute Guide](/developer-hub/building-on-0g/compute-network/overview)

---

Need help? Join our [Discord](https://discord.gg/0glabs) for developer support.

---

## DASigners