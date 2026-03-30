# Backup consensus layer data (0gchaind-home)
cp -r {your_0gchaind_home} $BACKUP_DIR/0gchaind-backup
```

### Step 4: Start Node 

If you get error while starting node due to missing `priv_validator_state.json`, create an empty `priv_validator_state.json` file in that directory with `{}`.

For testnet (Galileo), use `--chaincfg.chain-spec testnet`:

```bash
nohup ./bin/0gchaind start \
    --rpc.laddr tcp://0.0.0.0:26657 \
    --chaincfg.chain-spec testnet \
    --chaincfg.restaking.enabled \
    --chaincfg.restaking.symbiotic-rpc-dial-url ${ETH_RPC_URL} \
    --chaincfg.restaking.symbiotic-get-logs-block-range ${BLOCK_NUM} \
    --chaincfg.kzg.trusted-setup-path=kzg-trusted-setup.json \
    --chaincfg.engine.jwt-secret-path=jwt.hex \
    --chaincfg.block-store-service.enabled \
    --home {your_cl_home} \
    --p2p.external_address {your_node_ip}:26656 > {your_log_path}/0gchaind.log 2>&1 &
```

For mainnet (Aristotle), use `--chaincfg.chain-spec mainnet`:

```bash
nohup ./bin/0gchaind start \
    --rpc.laddr tcp://0.0.0.0:26657 \
    --chaincfg.chain-spec mainnet \
    --chaincfg.restaking.enabled \
    --chaincfg.restaking.symbiotic-rpc-dial-url ${ETH_RPC_URL} \
    --chaincfg.restaking.symbiotic-get-logs-block-range ${BLOCK_NUM} \
    --chaincfg.kzg.trusted-setup-path=kzg-trusted-setup.json \
    --chaincfg.engine.jwt-secret-path=jwt.hex \
    --chaincfg.block-store-service.enabled \
    --home {your_cl_home} \
    --p2p.external_address {your_node_ip}:26656 > {your_log_path}/0gchaind.log 2>&1 &
```

Then start Geth:

```bash
nohup ./bin/geth --config geth-config.toml \
     --nat extip:{your_node_ip} \
     --datadir {your_geth_datadir} \
     --networkid {network_id} > {your_log_path}/geth.log 2>&1 &
```

### Step 5: Verify Upgrade Success

```bash