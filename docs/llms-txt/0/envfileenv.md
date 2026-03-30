# envfile.env
COMBINED_SERVER_CHAIN_RPC=https://evmrpc-testnet.0g.ai
COMBINED_SERVER_PRIVATE_KEY=YOUR_PRIVATE_KEY
ENTRANCE_CONTRACT_ADDR=0x857C0A28A8634614BB2C96039Cf4a20AFF709Aa9

COMBINED_SERVER_RECEIPT_POLLING_ROUNDS=180
COMBINED_SERVER_RECEIPT_POLLING_INTERVAL=1s
COMBINED_SERVER_TX_GAS_LIMIT=2000000
COMBINED_SERVER_USE_MEMORY_DB=true
COMBINED_SERVER_KV_DB_PATH=/runtime/
COMBINED_SERVER_TimeToExpire=2592000
DISPERSER_SERVER_GRPC_PORT=51001
BATCHER_DASIGNERS_CONTRACT_ADDRESS=0x0000000000000000000000000000000000001000
BATCHER_FINALIZER_INTERVAL=20s
BATCHER_CONFIRMER_NUM=3
BATCHER_MAX_NUM_RETRIES_PER_BLOB=3
BATCHER_FINALIZED_BLOCK_COUNT=50
BATCHER_BATCH_SIZE_LIMIT=500
BATCHER_ENCODING_INTERVAL=3s
BATCHER_ENCODING_REQUEST_QUEUE_SIZE=1
BATCHER_PULL_INTERVAL=10s
BATCHER_SIGNING_INTERVAL=3s
BATCHER_SIGNED_PULL_INTERVAL=20s
BATCHER_EXPIRATION_POLL_INTERVAL=3600
BATCHER_ENCODER_ADDRESS=DA_ENCODER_SERVER
BATCHER_ENCODING_TIMEOUT=300s
BATCHER_SIGNING_TIMEOUT=60s
BATCHER_CHAIN_READ_TIMEOUT=12s
BATCHER_CHAIN_WRITE_TIMEOUT=13s
```

**4. Run the Docker Node**

```bash
docker run -d --env-file envfile.env --name 0g-da-client -v ./run:/runtime -p 51001:51001 0g-da-client combined
```

## Configuration

| Field | Description |
|-------|-------------|
| `--chain.rpc` | JSON RPC node endpoint for the blockchain network. |
| `--chain.private-key` | Hex-encoded signer private key. |
| `--chain.receipt-wait-rounds` | Maximum retries to wait for transaction receipt. |
| `--chain.receipt-wait-interval` | Interval between retries when waiting for transaction receipt. |
| `--chain.gas-limit` | Transaction gas limit. |
| `--combined-server.use-memory-db` | Whether to use mem-db for blob storage. |
| `--combined-server.storage.kv-db-path` | Path for level db. |
| `--combined-server.storage.time-to-expire` | Expiration duration for blobs in level db. |
| `--combined-server.log.level-file` | File log level. |
| `--combined-server.log.level-std` | Standard output log level. |
| `--combined-server.log.path` | Log file path. |
| `--disperser-server.grpc-port` | Server listening port. |
| `--disperser-server.retriever-address` | GRPC host for retriever. |
| `--batcher.da-entrance-contract` | Hex-encoded da-entrance contract address. |
| `--batcher.da-signers-contract` | Hex-encoded da-signers contract address. |
| `--batcher.finalizer-interval` | Interval for finalizing operations. |
| `--batcher.finalized-block-count` | Default number of blocks between finalized block and latest block. |
| `--batcher.confirmer-num` | Number of Confirmer threads. |
| `--batcher.max-num-retries-for-sign` | Number of retries before signing fails. |
| `--batcher.batch-size-limit` | Maximum batch size in MiB. |
| `--batcher.encoding-request-queue-size` | Size of the encoding request queue. |
| `--batcher.encoding-interval` | Interval between blob encoding requests. |
| `--batcher.pull-interval` | Interval for pulling from the encoded queue. |
| `--batcher.signing-interval` | Interval between slice signing requests. |
| `--batcher.signed-pull-interval` | Interval for pulling from the signed queue. |
| `--encoder-socket` | GRPC host of the encoder. |
| `--encoding-timeout` | Total time to wait for a response from encoder. |
| `--signing-timeout` | Total time to wait for a response from signer. |

</TabItem>
<TabItem value="source" label="DA Encoder">

## Features

- `parallel`: Uses parallel algorithms for computations, maximizing CPU resource utilization.
- `cuda`: Uses GPU for computations, applicable only on platforms with NVIDIA GPUs.

:::note
GPU support is currently tested with NVIDIA 12.04 drivers on the RTX 4090. Other NVIDIA GPUs may require parameter adjustments and have not been tuned yet.
:::

## Preparation

### Install Rust

Ensure you have curl installed.

Run the following command to install Rust:

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

After installation, add the cargo bin directory to your PATH environment variable:

```bash
source $HOME/.cargo/env
```

Verify the installation:

```bash
rustc --version
```

### Install other dependencies

```bash