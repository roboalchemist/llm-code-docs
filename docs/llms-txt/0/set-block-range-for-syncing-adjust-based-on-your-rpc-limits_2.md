# Set block range for syncing (adjust based on your RPC limits)
export BLOCK_NUM=1
```

### 9. Start 0gchaind

Launch the 0gchaind consensus client with testnet parameters:

```bash
cd ~/Galileo-v3.0.4

nohup ./bin/0gchaind start \
    --rpc.laddr tcp://0.0.0.0:26657 \
    --chaincfg.chain-spec testnet \
    --chaincfg.kzg.trusted-setup-path=kzg-trusted-setup.json \
    --chaincfg.engine.jwt-secret-path=jwt.hex \
    --chaincfg.block-store-service.enabled \
    --chaincfg.restaking.enabled \
    --chaincfg.restaking.symbiotic-rpc-dial-url ${ETH_RPC_URL} \
    --chaincfg.restaking.symbiotic-get-logs-block-range ${BLOCK_NUM} \
    --home {your data path}/0g-home/0gchaind-home \
    --p2p.external_address {your node ip}:26656 > {your data path}/0g-home/log/0gchaind.log 2>&1 &
```

### 10. Start Geth

Launch the Geth execution client:

```bash
cd ~/Galileo-v3.0.4

nohup ./bin/geth \
    --config geth-config.toml \
    --nat extip:{your node ip} \
    --datadir {your data path}/0g-home/geth-home \
    --networkid 16602 > {your data path}/0g-home/log/geth.log 2>&1 &
```

### 11. Verify Setup

Check the logs to confirm your node is running properly:

```bash