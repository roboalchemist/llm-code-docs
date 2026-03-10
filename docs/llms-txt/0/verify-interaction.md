# Verify interaction
cast call <CONTRACT_ADDRESS> "number()" --rpc-url https://evmrpc-testnet.0g.ai
```

### SDK Examples
- TypeScript SDK: https://github.com/0gfoundation/0g-ts-sdk/tree/main/examples
- Go SDK: https://github.com/0gfoundation/0g-storage-client/tree/main/examples

### Community Projects
**Awesome 0G Repository**: https://github.com/0gfoundation/awesome-0g

Curated list of community projects, tools, and resources built on 0G.

## Quick Reference

### Add Network to MetaMask

**Testnet**:
```javascript
await window.ethereum.request({
  method: 'wallet_addEthereumChain',
  params: [{
    chainId: '0x40EA',
    chainName: '0G-Galileo-Testnet',
    nativeCurrency: { name: '0G', symbol: '0G', decimals: 18 },
    rpcUrls: ['https://evmrpc-testnet.0g.ai'],
    blockExplorerUrls: ['https://chainscan-galileo.0g.ai']
  }]
});
```

**Mainnet**:
```javascript
await window.ethereum.request({
  method: 'wallet_addEthereumChain',
  params: [{
    chainId: '0x4125',
    chainName: '0G Mainnet',
    nativeCurrency: { name: '0G', symbol: '0G', decimals: 18 },
    rpcUrls: ['https://evmrpc.0g.ai'],
    blockExplorerUrls: ['https://chainscan.0g.ai']
  }]
});
```

### Common Commands

**Storage Upload (CLI)**:
```bash
0g-storage-client upload \
  --url https://evmrpc-testnet.0g.ai \
  --key YOUR_PRIVATE_KEY \
  --indexer https://indexer-storage-testnet-turbo.0g.ai \
  --file /path/to/file
```

**Storage Download (CLI)**:
```bash
0g-storage-client download \
  --indexer https://indexer-storage-testnet-turbo.0g.ai \
  --root ROOT_HASH \
  --file output.dat
```

**Check Node Status**:
```bash