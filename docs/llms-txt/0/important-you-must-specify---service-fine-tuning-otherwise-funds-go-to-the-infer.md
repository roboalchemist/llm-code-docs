# IMPORTANT: You must specify --service fine-tuning, otherwise funds go to the inference sub-account
0g-compute-cli transfer-fund --provider <PROVIDER_ADDRESS> --amount 2 --service fine-tuning
```

:::tip
If you see `MinimumDepositRequired` when creating a task, it means you haven't transferred funds to the provider's **fine-tuning** sub-account. Make sure to include `--service fine-tuning` in the `transfer-fund` command.
:::

### List Providers
```bash
0g-compute-cli fine-tuning list-providers
```
The output will be like:
```bash
┌──────────────────────────────────────────────────┬──────────────────────────────────────────────────┐
│ Provider 1                                       │ 0x940b4a101CaBa9be04b16A7363cafa29C1660B0d       │
├──────────────────────────────────────────────────┼──────────────────────────────────────────────────┤
│ Available                                        │ ✓                                                │
└──────────────────────────────────────────────────┴──────────────────────────────────────────────────┘
```

- **Provider x:** The address of the provider.
- **Available:** Indicates if the provider is available. If `✓`, the provider is available. If `✗`, the provider is occupied.

### List Models

```bash