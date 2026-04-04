# Source: https://docs.snowflake.com/en/release-notes/2025/other/2025-08-28-hybrid-tables-periodic-rekeying.md

# Aug 28, 2025: Hybrid table support for periodic rekeying (*General availability*)

Hybrid tables now support [periodic rekeying](../../../user-guide/security-encryption-manage.md).

Accounts that contain hybrid tables can enable and use periodic rekeying without any
additional configuration. The command to enable periodic rekeying is the same as for
standard tables:

```sqlexample
ALTER ACCOUNT SET PERIODIC_DATA_REKEYING = true;
```
