# Zerog storage nodes to download data from.
zgs_node_urls = "http://127.0.0.1:5678,http://127.0.0.1:5679"

#######################################################################
###                     Misc Config Options                         ###
#######################################################################

log_config_file = "log_config"
```

## Running the Storage KV Node

1. Navigate to the `run` directory:
```bash
cd run
```

2. Run the KV service:
```bash
../target/release/zgs_kv --config config.toml
```

For long-running sessions, consider using `tmux` or `screen` to run the node in the background.

## Monitoring and Maintenance

1. Check logs:
   The node outputs logs based on the `log_config` file specified in your configuration.

2. Updating the node:

 To update to the latest version, pull the latest changes from the repository and rebuild:

 ```bash
   git pull
   cargo build --release
   ```

## Troubleshooting

If you encounter issues:

1. Check the logs for any error messages.
2. Ensure your node meets the hardware requirements.
3. Verify that your `config.toml` file is correctly formatted and contains valid settings.
4. Check your internet connection and firewall settings.
5. Ensure the specified blockchain RPC endpoint and contract addresses are correct and accessible.

## Getting Help

If you need assistance:

1. Check the [GitHub Issues](https://github.com/0gfoundation/0g-storage-kv/issues) for known problems and solutions.
2. Join the 0G community channels (Discord, Telegram, etc.) for community support.
3. For critical issues, consider reaching out to the 0G team directly.

## Conclusion

Running a 0G Storage KV node is an important part of the 0G ecosystem, providing key-value storage capabilities. By following this guide, you should be able to set up and operate your node successfully. Remember to keep your node updated and monitor its performance regularly to ensure optimal operation.
</TabItem>
</Tabs>

---

## Validator Node

---

Running a Validator node means providing validator services for the network, processing transactions and maintaining consensus.

:::info **What You'll Need**
- Linux/macOS system with adequate hardware
- Stable internet connection
- Ethereum RPC endpoint (mainnet for Aristotle, HoleSky testnet for Galileo)
:::

## Hardware Requirements

| Component  | Mainnet (Aristotle) | Testnet (Galileo) |
|------------|---------|----------|
| Memory     | 64 GB   | 64 GB    |
| CPU        | 8 cores | 8 cores  |
| Disk       | 1 TB NVME SSD | 4 TB NVME SSD |
| Bandwidth  | 100 MBps for Download / Upload | 100 MBps for Download / Upload |

## Restaking RPC Configuration

- **Validator Nodes**: When running your consensus client, add the following flags to enable restaking and configure the Symbiotic RPC:

```bash
--chaincfg.restaking.enabled \
--chaincfg.restaking.symbiotic-rpc-dial-url ${ETH_RPC_URL} \
--chaincfg.restaking.symbiotic-get-logs-block-range ${BLOCK_NUM}
```

- **ETH_RPC_URL**: The RPC endpoint for the Symbiotic network.
  - **Mainnet (Aristotle)**: Use an Ethereum Mainnet RPC endpoint (e.g., https://eth-mainnet.g.alchemy.com/v2/YOUR_API_KEY)
  - **Testnet (Galileo)**: Use an Ethereum HoleSky RPC endpoint
- **BLOCK_NUM**: The maximum block number range per call when syncing restaking events. Default is 1. Adjust based on your RPC provider limits.

- **Non-Validator Nodes**: No restaking-related configuration is required; you can keep your current startup parameters unchanged.

This enables staking in Symbiotic contracts on Ethereum (mainnet: Ethereum, testnet: HoleSky) to participate in 0G Chain consensus. Validators must be able to read the Ethereum contract state to generate and verify new blocks. You can run your own node or use a third-party RPC provider such as QuickNode or Infura for `${ETH_RPC_URL}`.

:::tip Non-Validator Nodes
Restaking configuration is NOT required for non-validator nodes. Do not add the `--chaincfg.restaking.*` flags when running non-validator nodes.
:::

---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

<Tabs>
  <TabItem value="mainnet" label="Mainnet (Aristotle)" default>

## Mainnet (Aristotle) Setup Guide

### 1. Download Package

Download the latest Aristotle mainnet package:

```bash
wget -O aristotle.tar.gz https://github.com/0gfoundation/0gchain-Aristotle/releases/download/v1.0.4/Aristotle-v1.0.4.tar.gz
```

:::note Version Information
Latest Aristotle mainnet release: v1.0.4. Check [releases page](https://github.com/0gfoundation/0gchain-Aristotle/releases) for newer versions.
:::

### 2. Extract Package

Extract the Aristotle node package to your home directory:

```bash
tar -xzvf Aristotle-v1.0.4.tar.gz -C ~
```

### 3. Create Data Directory and Copy Configuration

Create your data directory and copy the default configuration:

```bash
cd Aristotle-v1.0.4

cp -r 0g-home {your data path}
sudo chmod 777 ./bin/geth
sudo chmod 777 ./bin/0gchaind
```

### 4. Initialize Geth

Initialize the Geth execution client with the genesis configuration:

```bash
./bin/geth init --datadir {your data path}/0g-home/geth-home ./geth-genesis.json
```

**Expected output:** "Successfully wrote genesis state"

### 5. Initialize 0gchaind for Mainnet

Create a temporary initialization with the mainnet chain specification:

```bash
./bin/0gchaind init {node name} --home {your data path}/tmp --chaincfg.chain-spec mainnet
```

⚠️ **Important:** The `--chaincfg.chain-spec mainnet` flag is REQUIRED for validators

### 6. Copy Node Keys and Validator Keys

Copy all necessary keys to the permanent directory:

```bash
cp {your data path}/tmp/data/priv_validator_state.json {your data path}/0g-home/0gchaind-home/data/
cp {your data path}/tmp/config/node_key.json {your data path}/0g-home/0gchaind-home/config/
cp {your data path}/tmp/config/priv_validator_key.json {your data path}/0g-home/0gchaind-home/config/
```

### 7. Generate JWT Authentication Token

Generate a JWT token with mainnet specification for secure communication:

```bash
./bin/0gchaind jwt generate --home {your data path}/0g-home/0gchaind-home --chaincfg.chain-spec mainnet

cp -f {your data path}/0g-home/0gchaind-home/config/jwt.hex ./
```

### 8. Configure Node Name

Update the node moniker in the configuration file:

```bash
sed -i 's/moniker = "0G-mainnet-aristotle-node"/moniker = "{your node name}"/' {your data path}/0g-home/0gchaind-home/config/config.toml
```

### 9. Verify Configuration Files

Ensure all required configuration files are present:

```bash
ls -la {your data path}/0g-home/0gchaind-home/config/
```

**Should display:**
- `app.toml`
- `client.toml`
- `config.toml`
- `genesis.json`
- `jwt.hex`
- `node_key.json`
- `priv_validator_key.json`

### 10. Set Environment Variables

Configure required environment variables for Symbiotic restaking:

```bash