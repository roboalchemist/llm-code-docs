# Validate the deposit message
./bin/0gchaind deposit validate-delegation \
    {pubkey} \
    {staking_address} \
    {amount} \
    {signature} \
    $HOMEDIR/config/genesis.json \
    --home $HOMEDIR \
    --chaincfg.chain-spec=mainnet \
    --override-rpc-url \
    --rpc-dial-url https://evmrpc.0g.ai
```

**Example:**
```bash
./bin/0gchaind deposit validate-delegation \
    0x8497312cd37eef3a7a50017cfbebcb00a9bc400c5881ffb1011cba1c3f29e5d005a980880b7b919b558b95565bc1e628 \
    0xea224dBB52F57752044c0C86aD50930091F561B9 \
    500000000000 \
    0xb1dae1164d931c46178785246203eb1c4496b403a7c417bfb33bdfd3c26b552bdbec8e466ed6712ade0b99cc9b0ee8b004cc766687565ba5b0929a1382997a6cc548cf5e390b69f849933c7ac017fbddc612cb3de285fdf89e6fe32e0ccbfc43 \
    $HOMEDIR/config/genesis.json \
    --home $HOMEDIR \
    --chaincfg.chain-spec=mainnet \
    --override-rpc-url \
    --rpc-dial-url https://evmrpc.0g.ai
```

**Output:**
```
✅ Deposit message is valid!
```

### Step 3: Prepare Validator Description and Settings

#### Description Structure

The Description struct contains your validator's public information. All fields have character limits that must be respected:

| Field | Max Length | Description |
|-------|-----------|-------------|
| `moniker` | 70 chars | Your validator's display name |
| `identity` | 100 chars | **Optional:** Keybase identity |
| `website` | 140 chars | Your validator website URL |
| `securityContact` | 140 chars | Security contact email |
| `details` | 200 chars | Additional validator description |

**Example Description Object:**

```jsx
{
  moniker: "Your Validator Name",      // Max 70 chars
  identity: "keybase_id",              // Optional
  website: "https://yoursite.com",     // Max 140 chars
  securityContact: "security@you.com", // Max 140 chars
  details: "Professional validator"     // Max 200 chars
}
```

#### Commission Rate Configuration

The commission rate determines what percentage of staking rewards your validator keeps

| Value | Commission |
|-------|-----------|
| `100` | 0.01% |
| `1000` | 0.1% |
| `10000` | 1% |
| `50000` | 5% |
| `100000` | 10% |

#### Withdrawal Fee Configuration

The withdrawal fee (in Gwei) is charged when delegators undelegate from your validator.

**Recommended value:** `1` (equivalent to 1 Gneuron, ~1 Gwei)

### Step 4: Execute Initialization Transaction

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

<Tabs>
  <TabItem value="chainscan" label="0G Chain Scan (Recommended)" default>

The easiest way to initialize your validator using the web interface:

1. Navigate to https://chainscan.0g.ai/address/0xea224dBB52F57752044c0C86aD50930091F561B9
2. Under **Contracts** Tab, click on the **Write As Proxy** button
3. Find and click on `createAndInitializeValidatorIfNecessary`
4. Fill in all the required parameters:
   - **description** (struct):
     - `moniker`: Your validator name (max 70 chars)
     - `identity`: Keybase ID (optional)
     - `website`: Your website URL
     - `securityContact`: Security contact email
     - `details`: Additional description
   - **commissionRate**: Commission percentage (e.g., 10000 for 1%)
   - **withdrawalFeeInGwei**: Withdrawal fee in Gwei (e.g.,1 Gneuron ~ 1 Gwei)
   - **pubkey**: The public key from Step 1
   - **signature**: The signature from Step 1
5. Set the `payable amount` to **500** OG tokens
6. Connect your wallet and execute the transaction

:::tip **Tip**
Using the Chain Scan interface requires no coding knowledge and is the safest option for most users.
:::

  </TabItem>
  <TabItem value="metamask" label="MetaMask / Web3 Wallet">

For users comfortable with wallet interactions:

1. Ensure your wallet is connected to **0G Chain Mainnet**
2. Go to the contract address: `0xea224dBB52F57752044c0C86aD50930091F561B9`
3. Use a contract interaction tool like:
   - [0G Chain Scan](https://chainscan.0g.ai)
   - Your wallet's built-in contract interaction features
4. Call `createAndInitializeValidatorIfNecessary` with:
   - `description`: Struct with all validator details
   - `commissionRate`: Commission percentage (e.g., 10000 for 1%)
   - `withdrawalFeeInGwei`: Withdrawal fee in Gwei (~1 Gneuron equivalent)
   - `pubkey`: Your validator's public key
   - `signature`: Your validator's signature
5. Set transaction value to **500 OG tokens** (500000000000000000000 wei)
6. Confirm the transaction in your wallet

:::warning **Important**
Ensure your wallet has sufficient funds:
- 500 OG tokens for initialization
- Additional gas fees for the transaction
:::

  </TabItem>
  <TabItem value="ethersjs" label="Ethers.js (Programmatic)">

For developers who want to automate the process:

```javascript
const { ethers } = require("ethers");

// Initialize provider and wallet
const provider = new ethers.JsonRpcProvider("https://evmrpc.0g.ai");
const wallet = new ethers.Wallet(process.env.PRIVATE_KEY, provider);

// Staking contract ABI (minimal)
const stakingABI = [
  {
    "inputs": [
      {
        "components": [
          { "internalType": "string", "name": "moniker", "type": "string" },
          { "internalType": "string", "name": "identity", "type": "string" },
          { "internalType": "string", "name": "website", "type": "string" },
          { "internalType": "string", "name": "securityContact", "type": "string" },
          { "internalType": "string", "name": "details", "type": "string" }
        ],
        "internalType": "struct IStakingContract.Description",
        "name": "description",
        "type": "tuple"
      },
      { "internalType": "uint32", "name": "commissionRate", "type": "uint32" },
      { "internalType": "uint96", "name": "withdrawalFeeInGwei", "type": "uint96" },
      { "internalType": "bytes", "name": "pubkey", "type": "bytes" },
      { "internalType": "bytes", "name": "signature", "type": "bytes" }
    ],
    "name": "createAndInitializeValidatorIfNecessary",
    "outputs": [{ "internalType": "address", "name": "", "type": "address" }],
    "stateMutability": "payable",
    "type": "function"
  }
];

async function initializeValidator() {
  const stakingContract = new ethers.Contract(
    "0xea224dBB52F57752044c0C86aD50930091F561B9",
    stakingABI,
    wallet
  );

  const description = {
    moniker: "Your Validator Name",
    identity: "keybase_id",
    website: "https://yourvalidator.com",
    securityContact: "security@yourvalidator.com",
    details: "Professional 0G Chain validator"
  };

  try {
    const tx = await stakingContract.createAndInitializeValidatorIfNecessary(
      description,
      10000,      // 1% commission
      1000000,    // 1 Gwei withdrawal fee
      "0x...",    // Your pubkey
      "0x...",    // Your signature
      { value: ethers.parseEther("500") }  // 500 OG tokens
    );

    console.log("Transaction hash:", tx.hash);
    const receipt = await tx.wait();
    console.log("Validator initialized successfully!");
    console.log("Transaction receipt:", receipt);
  } catch (error) {
    console.error("Error initializing validator:", error);
  }
}

initializeValidator();
```

:::note **Environment Setup**
Make sure to set `PRIVATE_KEY` in your `.env` file before running the script.
:::

</TabItem>
</Tabs>

### Step 5: Verify Initialization

After successful initialization, you can verify your validator status:

- Check the transaction on **0G Chain Scan**: https://chainscan.0g.ai
- Verify your validator status on **0G Explorer**: https://explorer.0g.ai/mainnet/validators

:::info **Activation Time**
Your validator may initially appear as **inactive** on the explorer. This is normal. Validators typically take **30-60 minutes** to activate on the network after successful initialization.

You can check the transaction status and logs to confirm the initialization was successful while waiting for activation.
:::

### Troubleshooting

<details>
<summary>Error: "Insufficient funds"</summary>

Ensure you have at least 500 OG tokens plus gas fees in your wallet.

```bash