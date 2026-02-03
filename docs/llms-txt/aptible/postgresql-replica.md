# Source: https://www.aptible.com/docs/how-to-guides/troubleshooting/common-errors-issues/postgresql-replica.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# PostgreSQL Replica max_connections

A PostgreSQL replica's `max_connections` setting must be greater than or equal to the primary's setting; if the value is increased on the primary before being changed on the replica it will result in the replica becoming inaccessible with the following error:

```
FATAL:  hot standby is not possible because max_connections = 1000 is a
lower setting than on the master server (its value was 2000)
```

Our SRE Team is alerted when a replica fails for this reason and will take action to correct the situation (generally by increasing `max_connections` on the replica and notifying the user).

To avoid this issue, you need to update `max_connections` on the replica Database to the higher value *before* updating the value on the primary.
