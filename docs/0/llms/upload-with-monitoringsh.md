# upload-with-monitoring.sh
0g-storage-client upload \
  --file $1 \
  --log-level info \
  # ... other parameters \
  2>&1 | tee -a /var/log/0g-uploads.log
```

## Troubleshooting

<details>
<summary>**Upload fails with "insufficient funds" error**</summary>

Ensure your wallet has enough tokens for:
- Gas fees on 0G Chain
- Storage fees for the file size

Check balance: Use a blockchain explorer or wallet to verify funds.
</details>

<details>
<summary>**"Indexer not found" error during upload/download**</summary>

This can happen if:
- The indexer service is offline
- The indexer endpoint URL is incorrect
- Network connectivity issues

Verify the indexer endpoint and try again.
</details>

<details>
<summary>**RPC timeout errors**</summary>

If you experience RPC timeouts, try adjusting the timeout settings:
```bash
--rpc-timeout 60s --rpc-retry-count 10 --rpc-retry-interval 3s
```
</details>

## Best Practices

1. **Security First**: Store private keys in environment variables, not command line
2. **Backup Root Hashes**: Always save file root hashes after uploads
3. **Use Verification**: Enable `--proof` for important downloads
4. **Monitor Transactions**: Track uploads on the blockchain explorer
5. **Test with Gen**: Use the `gen` command to create test files for development
6. **HTTP Access**: Leverage the RESTful API for web applications and integrations
7. **Batch KV Operations**: Use comma-separated lists for efficient key-value operations

---

*Need more control? Consider running your own [storage node](/run-a-node/storage-node) to participate in the network and earn rewards.*

---

## Getting Started