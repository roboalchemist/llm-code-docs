# Set block range for syncing (adjust based on your RPC limits)
export BLOCK_NUM=1
```

### 11. Start 0gchaind

Launch the 0gchaind consensus client with validator-specific parameters:

```bash
cd Aristotle-v1.0.4

nohup ./bin/0gchaind start \
    --rpc.laddr tcp://0.0.0.0:26657 \
    --chaincfg.kzg.trusted-setup-path=kzg-trusted-setup.json \
    --chaincfg.engine.jwt-secret-path=jwt.hex \
    --chaincfg.block-store-service.enabled \
    --chaincfg.restaking.enabled \
    --chaincfg.restaking.symbiotic-rpc-dial-url ${ETH_RPC_URL} \
    --chaincfg.restaking.symbiotic-get-logs-block-range ${BLOCK_NUM} \
    --home {your data path}/0g-home/0gchaind-home \
    --p2p.external_address {your node ip}:26656 > {your data path}/0g-home/log/0gchaind.log 2>&1 &
```

**Validator-Specific Parameters:**
- `--chaincfg.restaking.enabled`: Enables restaking functionality
- `--chaincfg.restaking.symbiotic-rpc-dial-url`: Ethereum RPC for Symbiotic protocol
- `--chaincfg.restaking.symbiotic-get-logs-block-range`: Block range per sync call

### 12. Start Geth

Launch the Geth execution client:

```bash
cd Aristotle-v1.0.4

nohup ./bin/geth \
    --config geth-config.toml \
    --nat extip:{your node ip} \
    --datadir {your data path}/0g-home/geth-home \
    --networkid 16661 > {your data path}/0g-home/log/geth.log 2>&1 &
```

### 13. Verify Node Status

Check that both services are running correctly:

```bash