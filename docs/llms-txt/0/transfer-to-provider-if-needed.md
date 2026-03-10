# Transfer to provider if needed
0g-compute-cli transfer-fund --provider <ADDRESS> --amount 5
```

</details>

<details>
<summary>Refund Not Available</summary>

Refunds have a 24-hour lock period. After the lock period expires, you need to call the retrieve-fund function again to complete the refund. Check the status:

```bash
0g-compute-cli get-sub-account --provider <PROVIDER_ADDRESS>
```

Look for "Remaining Locked Time" in the output.

</details>

<details>
<summary>Transaction Failed</summary>

Common causes:

1. Network issues - Check your RPC endpoint
2. Gas price too low - Increase gas price
3. Insufficient gas - Ensure wallet has enough for gas fees

```bash