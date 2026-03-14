# Source: https://docs.snowflake.com/en/developer-guide/external-network-access/external-network-access-billing.md

# Costs of external network access

Using external network access incurs normal costs associated with:

* [Snowflake warehouse usage.](../../user-guide/cost-understanding-compute.md)
* [Data transfer.](../../user-guide/cost-understanding-data-transfer.md)

Data transfer charges will appear as a TRANSFER_TYPE of EXTERNAL_ACCESS in the [DATA_TRANSFER_HISTORY view](../../sql-reference/account-usage/data_transfer_history.md).
Any data egress traffic associated with a “bring-your-own-IP” (BYOIP) destination will be charged at cross-cloud or Internet traffic rates.

Calling to an external network location from a handler will result in payload egress. As data egress, this call results in data
transfer cost.

In addition, you might need to pay indirect or third-party charges, including charges by the provider of the remote service. Charges can
vary from vendor to vendor.
