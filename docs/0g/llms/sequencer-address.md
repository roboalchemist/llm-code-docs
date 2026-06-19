# Sequencer address
export GS_SEQUENCER_ADDRESS=0xC06566E8Ec6cF81B4B26376880dB620d83d50Dfb
export GS_SEQUENCER_PRIVATE_KEY=0x2a0290473f3838dbd083a5e17783e3cc33c905539c0121f9c76614dda8a38dca

```

**3. Save the addresses:**

Copy the output from the above command and paste it into your `.envrc` file. Fund the addresses with Sepolia ETH:
- Admin: 0.5 ETH
- Proposer: 0.2 ETH
- Batcher: 0.1 ETH

:::warning Production Note
Use secure hardware for key management in production environments. cast wallet is not designed for production deployments.
:::

## Load Environment Variables

**1. Enter the Optimism Monorepo:**

```bash
cd ~/optimism
```

**2. Load the variables with direnv:**

```bash
direnv allow
```

## Deploy Core Contracts

**1. Update the deployment configuration:**

```bash
cd packages/contracts-bedrock
./scripts/getting-started/config.sh
```

**2. Add 0G DA configuration:**

Add the following at the bottom of `getting_started.json`:

```json
{
  "useAltDA": true,
  "daCommitmentType": "GenericCommitment",
  "daChallengeWindow": 160,
  "daResolveWindow": 160,
  "daBondSize": 1000000,
  "daResolverRefundPercentage": 0
}
```

**3. Deploy contracts (this can take up to 15 minutes):**

```bash
DEPLOYMENT_OUTFILE=deployments/artifact.json \
DEPLOY_CONFIG_PATH=deploy-config/getting-started.json \
forge script scripts/deploy/Deploy.s.sol:Deploy \
  --broadcast --private-key $GS_ADMIN_PRIVATE_KEY \
  --rpc-url $L1_RPC_URL --slow
```

**4. Generate L2 allocations:**

```bash
CONTRACT_ADDRESSES_PATH=deployments/artifact.json \
DEPLOY_CONFIG_PATH=deploy-config/getting-started.json \
STATE_DUMP_PATH=deploy-config/statedump.json \
forge script scripts/L2Genesis.s.sol:L2Genesis \
  --sig 'runWithStateDump()' --chain <YOUR_L2_CHAINID>
```

## Set Up L2 Configuration

**1. Navigate to the op-node directory:**

```bash
cd ~/optimism/op-node
```

**2. Generate genesis and rollup configuration:**

```bash
go run cmd/main.go genesis l2 \
  --deploy-config ../packages/contracts-bedrock/deploy-config/getting-started.json \
  --l1-deployments ../packages/contracts-bedrock/deployments/artifact.json \
  --outfile.l2 genesis.json \
  --outfile.rollup rollup.json \
  --l1-rpc $L1_RPC_URL \
  --l2-allocs ../packages/contracts-bedrock/deploy-config/statedump.json
```

**3. Add alt_da configuration to rollup.json:**

```json
{
  "alt_da": {
    "da_challenge_contract_address": "0x0000000000000000000000000000000000000000",
    "da_commitment_type": "GenericCommitment",
    "da_challenge_window": 160,
    "da_resolve_window": 160
  }
}
```

**4. Generate JWT secret:**

```bash
openssl rand -hex 32 > jwt.txt
```

**5. Copy files to op-geth directory:**

```bash
cp genesis.json ~/op-geth
cp jwt.txt ~/op-geth
```

## Initialize and Run Components

### Initialize op-geth

```bash
cd ~/op-geth
mkdir datadir
build/bin/geth init --datadir=datadir genesis.json
```

### Run op-geth

```bash
cd ~/op-geth
./build/bin/geth \
  --datadir ./datadir \
  --http \
  --http.corsdomain="*" \
  --http.vhosts="*" \
  --http.addr=0.0.0.0 \
  --http.port=9545 \
  --http.api=web3,debug,eth,txpool,net,engine \
  --ws \
  --ws.addr=0.0.0.0 \
  --ws.port=9546 \
  --ws.origins="*" \
  --ws.api=debug,eth,txpool,net,engine \
  --syncmode=full \
  --nodiscover \
  --maxpeers=0 \
  --networkid=42069 \
  --authrpc.vhosts="*" \
  --authrpc.addr=0.0.0.0 \
  --authrpc.port=9551 \
  --authrpc.jwtsecret=./jwt.txt \
  --rollup.disabletxpoolgossip=true \
  --state.scheme=hash
```

### Run op-node

```bash
cd ~/optimism/op-node
./bin/op-node \
  --l2=http://localhost:9551 \
  --l2.jwt-secret=./jwt.txt \
  --sequencer.enabled \
  --sequencer.l1-confs=5 \
  --verifier.l1-confs=4 \
  --rollup.config=./rollup.json \
  --rpc.addr=0.0.0.0 \
  --rpc.port=8547 \
  --p2p.disable \
  --rpc.enable-admin \
  --p2p.sequencer.key=$GS_SEQUENCER_PRIVATE_KEY \
  --l1=$L1_RPC_URL \
  --l1.rpckind=$L1_RPC_KIND \
  --altda.enabled=true \
  --altda.da-server=<DA_SERVER_HTTP_URL> \
  --altda.da-service=true \
  --l1.beacon.ignore=true
```

### Run op-batcher

```bash
cd ~/optimism/op-batcher
./bin/op-batcher \
  --l2-eth-rpc=http://localhost:9545 \
  --rollup-rpc=http://localhost:8547 \
  --poll-interval=1s \
  --sub-safety-margin=6 \
  --num-confirmations=1 \
  --safe-abort-nonce-too-low-count=3 \
  --resubmission-timeout=30s \
  --rpc.addr=0.0.0.0 \
  --rpc.port=8548 \
  --rpc.enable-admin \
  --max-channel-duration=1 \
  --l1-eth-rpc=$L1_RPC_URL \
  --private-key=$GS_BATCHER_PRIVATE_KEY \
  --altda.enabled=true \
  --altda.da-service=true \
  --altda.da-server=<DA_SERVER_HTTP_URL>
```

:::tip Controlling Batcher Costs
The `--max-channel-duration=n` setting controls how often data is written to L1. Lower values mean faster synchronization but higher costs. Set to 0 to disable or increase for lower costs.
:::

### Run op-proposer

```bash
cd ~/optimism/op-proposer
./bin/op-proposer \
  --poll-interval=12s \
  --rpc.port=9560 \
  --rollup-rpc=http://localhost:8547 \
  --l2oo-address=$L2OO_ADDR \
  --private-key=$GS_PROPOSER_PRIVATE_KEY \
  --l1-eth-rpc=$L1_RPC_URL
```

## Acquire Sepolia ETH for Layer 2

**1. Navigate to contracts-bedrock:**

```bash
cd ~/optimism/packages/contracts-bedrock
```

**2. Find the L1 standard bridge contract address:**

```bash
cat deployments/artifact.json | jq -r .L1StandardBridgeProxy
```

**3. Send Sepolia ETH to the bridge contract address**

## Test Your Rollup

You now have a fully operational 0G DA-powered Optimism-based EVM Rollup. Experiment with it as you would with any other test blockchain.

:::important Notes
- This is a beta integration with active development ongoing
- Ensure all necessary ports are open in your firewall configuration
- Refer to the [Optimism documentation](https://docs.optimism.io/) for additional configuration options and troubleshooting
:::

---

*Congratulations on setting up your OP Stack rollup with 0G DA!*

---

## Storage SDK

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';