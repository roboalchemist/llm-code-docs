# Check geth logs
tail -f {your data path}/0g-home/log/geth.log
```

:::success **Success Indicators**
- 0gchaind should show "Committed state" messages
- No error messages in either log
- Validator is participating in consensus
:::

  </TabItem>
</Tabs>

---

## Validator Operations

### Initialize Your Validator

Once your validator node is running and fully synced (`catching_up: false`), you need to initialize your validator on the blockchain to start validating transactions.

**Next Step:** Follow the **[Validator Initialization Guide](../developer-hub/building-on-0g/contracts-on-0g/staking-interfaces#validator-initialization)** to:
1. Generate validator signature
2. Prepare validator description and settings
3. Execute the initialization transaction
4. Verify your validator activation (typically 30-60 minutes)

---

### Monitor Consensus Participation

```bash