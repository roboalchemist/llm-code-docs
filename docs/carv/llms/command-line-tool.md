# Source: https://docs.carv.io/svm-ai-agentic-chain/quick-start/command-line-tool.md

# Command line tool

**Set Up CARV SVM RPC**

Run the following command to set the RPC URL to CARV SVM Testnet:

```bash
solana config set --url https://rpc.testnet.carv.io/rpc
```

You can verify that the Solana CLI is properly configured to use the CARV SVM Testnet by running:

```bash
solana config get
```

You should see an output that includes the following URL:

```bash
Config File: /xxx/xxx/.config/solana/cli/config.yml
RPC URL: https://rpc.testnet.carv.io/rpc 
WebSocket URL: wss:////rpc.testnet.carv.io/rpc (computed)
Keypair Path: ./wallet.json
Commitment: confirmed
```
