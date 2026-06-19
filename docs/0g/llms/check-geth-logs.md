# Check geth logs
tail -f {your data path}/0g-home/log/geth.log
```

  </TabItem>
  <TabItem value="testnet" label="Testnet (Galileo)">

## Testnet (Galileo) Setup Guide

### 1. Download Package

Download the latest Galileo testnet package:

```bash
wget -O galileo.tar.gz https://github.com/0gfoundation/0gchain-NG/releases/download/v3.0.4/Galileo-v3.0.4.tar.gz
```

:::note Version Information
Latest Galileo testnet release: v3.0.4. Check [releases page](https://github.com/0gfoundation/0gchain-NG/releases) for newer versions.
:::

### 2. Extract Package

Extract the package to your home directory:

```bash
tar -xzvf Galileo-v3.0.4.tar.gz -C ~
```

### 3. Create Data Directory and Copy Configuration

Copy the configuration files and set proper permissions:

```bash
cd Galileo-v3.0.4

cp -r 0g-home {your data path}
sudo chmod 777 ./bin/geth
sudo chmod 777 ./bin/0gchaind
```

### 4. Initialize Geth

Initialize the Geth execution client with the genesis file:

```bash
./bin/geth init --datadir {your data path}/0g-home/geth-home ./geth-genesis.json
```

**Expected output:** "Successfully wrote genesis state"

### 5. Initialize 0gchaind for Testnet

Create a temporary directory for initial configuration with testnet chain specification:

```bash
./bin/0gchaind init {node name} --home {your data path}/tmp --chaincfg.chain-spec testnet
```

⚠️ **Important:** The `--chaincfg.chain-spec testnet` flag is REQUIRED for testnet validators

### 6. Generate JWT Authentication Token

Generate a JWT token with testnet specification for secure communication:

```bash
./bin/0gchaind jwt generate --home {your data path}/0g-home/0gchaind-home --chaincfg.chain-spec testnet

cp -f {your data path}/0g-home/0gchaind-home/config/jwt.hex ./
```

### 7. Copy Node Files

Move the generated keys to the proper location:

```bash
cp {your data path}/tmp/data/priv_validator_state.json {your data path}/0g-home/0gchaind-home/data/
cp {your data path}/tmp/config/node_key.json {your data path}/0g-home/0gchaind-home/config/
cp {your data path}/tmp/config/priv_validator_key.json {your data path}/0g-home/0gchaind-home/config/
```

> Note: The temporary directory can be deleted after this step.

### 8. Set Environment Variables

Configure required environment variables for Symbiotic restaking:

```bash