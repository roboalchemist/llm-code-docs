# Should show "catching_up": false when fully synced
curl http://localhost:26657/status | jq '.result.sync_info'
```

### Key Management

⚠️ **Critical Security Notice:**

- **Backup your validator keys immediately**: `priv_validator_key.json` and `node_key.json`
- **Never share your private validator key** with anyone
- Store backups in multiple secure locations
- Test recovery process in a non-production environment first

<details>
<summary>Backup & Recovery</summary>

These files are essential for validator recovery and must be backed up securely:

```bash