# Essential validator keys
/{your data path}/0g-home/0gchaind-home/config/
```

#### Recovery Process

To restore your validator from backup:

1. **Stop running services**:
   ```bash
   pkill 0gchaind
   pkill geth
   ```

2. **Restore key files**:
   ```bash
   cp ~/validator-backup/node_key.json /{your data path}/0g-home/0gchaind-home/config/
   cp ~/validator-backup/priv_validator_key.json /{your data path}/0g-home/0gchaind-home/config/
   ```

3. **Restart services** following the appropriate setup guide steps.

</details>

<details>
<summary>Upgrade Validator</summary>

### Step 1: Extract New Release

```bash