# Download the binary (replace with actual URL)
wget https://github.com/0gfoundation/alignment-node-release/releases/download/v1.0.0/alignment-node.tar.gz

tar -xzf alignment-node.tar.gz

cd alignment-node

chmod +x 0g-alignment-node
```

#### Step 2: Configure Environment

1. Copy the example environment file:
```bash
cp .env.example .env
```

2. Edit the `.env` file with your configuration:
```bash
nano .env
```

3. Configure the following parameters:

```bash
export ZG_ALIGNMENT_NODE_LOG_LEVEL=debug
export ZG_ALIGNMENT_NODE_SERVICE_IP="http://127.0.0.1:34567"  # Full URL endpoint
export ZG_ALIGNMENT_NODE_SERVICE_PRIVATEKEY=your_private_key_here
```

:::note
The private key is the private key of the wallet you used to purchase the NFT. If the wallet doesn't have any NFTs, the wallet is not eligible to register as operator.
:::

**Important Configuration Notes:**
- **LOG_LEVEL**: Set to `debug` for troubleshooting, `info` for normal operation
- **SERVICE_IP**: The ip of the service you are running. You need to add the external ip of the node to the `.env` file. The external ip is the ip of the node that is accessible from the internet.
- **PRIVATEKEY**: Your wallet's private key that holds the alignment node license(s)

#### Step 3: Network Configuration

::::warning **Open your service port**
The port specified in your configuration must be accessible externally for consensus communication.

Make sure this port is open in:
- Cloud security groups/firewalls (AWS, Azure, GCP, etc.)
- VPS provider firewalls
- Local server firewall rules

Steps vary by provider; consult your host's docs.
::::

#### Step 4: Start Your Node

1. Load environment variables:
```bash
source .env
```

2. Register the operator:
```bash
./0g-alignment-node registerOperator --key <your_private_key> --token-id <your_token_id> --chain-id <chain_id> --rpc <rpc_url> --contract <contract_address>
```

:::note
The token id is the token id of the NFT you purchased. The private key is the private key of the wallet you used to purchase the NFT. If the wallet doesn't have any NFTs, the wallet is not eligible to register as operator.
:::

**Configuration Details:**
- **Chain ID**: `42161` (Arbitrum Mainnet)
- **RPC URL**: Use a reliable Arbitrum RPC endpoint such as:
  - `https://arb1.arbitrum.io/rpc` (Public endpoint)
  - Or your preferred Arbitrum RPC provider
- **Alignment manager contract address**: `0xdD158B8A76566bC0c342893568e8fd3F08A9dAac` (Arbitrum Mainnet)

3. Start the node:
```bash
./0g-alignment-node start --mainnet
```

4. To run in background (recommended for production):
```bash
nohup ./0g-alignment-node start --mainnet > node.log 2>&1 &
```

### Monitoring Your Node

View logs:
```bash
tail -f node.log
```

### Node command help
```bash
./0g-alignment-node --help

./0g-alignment-node <command> --help
```

::::tip **Healthy node checklist**
- Status reports without errors
- Logs show steady activity, no repeated crashes
::::

### Troubleshooting

**Node not connecting:**
- Verify port is open and accessible externally
- Check your firewall/security group settings
- Ensure private key has associated licenses

**Node crashes:**
- Check logs for errors
- Verify system requirements are met
- Ensure stable internet connection

---

## Best Practices

### For Self-Hosted Nodes
1. **Regular Updates**: Keep node binary updated
2. **Monitoring**: Set up alerts for downtime
3. **Backup**: Keep secure backup of private keys
4. **Security**: Use dedicated wallet for node operation
5. **Network**: Ensure stable internet connection

### For NAAS Delegation
1. **Research Providers**: Check reputation and uptime history
2. **Understand Terms**: Read commission rates and prepaid terms
3. **Monitor Status**: Regularly check delegation status
4. **Payment Tracking**: Set reminders for prepaid renewals
5. **Diversification**: Consider splitting licenses across providers

---

---

## Compliance and Regulatory Requirements

## Regulation S Compliance
The sale follows Regulation S guidelines, restricting U.S. persons from participating. The sale website, promotional content, and user interface clearly indicate these restrictions, and KYC verification is mandatory for claiming rewards to maintain regulatory adherence. Prospective participants are advised to review these conditions and understand that resale of node licenses is not permitted within the first 12 months.
## Information Disclosure
All communications related to the sale are made with transparency but exclude any directed selling to U.S. persons. Information shared in marketing materials, promotional activities, and social media avoids U.S.-targeted content, aligning with compliance requirements to mitigate any regulatory risks.

---

## Incentives & Rewards