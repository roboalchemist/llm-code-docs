# Source: https://planetscale.com/docs/postgres/troubleshooting/read-only-mode.md

# Read-only mode

> PlanetScale may automatically enable read-only mode on a cluster to maintain stability and availability when certain conditions are detected.

Read-only mode preserves cluster functionality while preventing operations that could lead to instability, allowing you to remediate issues before they become critical.

When read-only mode is enabled, attempts to write to the cluster will see the following error:

```sql  theme={null}
invalid statement because cluster is read-only
```

We will also *pause* all logical replication subscriptions writing data into the cluster.
Once your cluster is out of read-only mode you can unpause the subscribers by running

```
ALTER SUBSCRIPTION sub_name ENABLE;
```

on each subscription.

There's no way for a PlanetScale customer to enter or exit read-only mode, except by remediating the conditions that caused the cluster to enter that mode.

Here are the reasons we'll put the cluster into read-only mode:

## Insufficient space

To protect your cluster from crashing, if a cluster has very little space left (typically 5% or less), we will automatically move it into read-only mode. The specific scenarios are:

| Storage Type                 | Scenario                                                                                                                                                                                                                                                                                                                                 | Remediation                                                                                                                                                                                                                       |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Network-attached storage** | Clusters with [Autoscaling](/docs/postgres/cluster-configuration/cluster-storage#enable-autoscaling) disabled or where your current [disk size](/docs/postgres/cluster-configuration/cluster-storage#disk-size) is approaching your configured [Autoscaling maximum](/docs/postgres/cluster-configuration/cluster-storage#storage-limit) | Increase the [cluster disk size](/docs/postgres/cluster-configuration/cluster-storage#disk-size) manually or increase the [storage limit on disk autoscaling](/docs/postgres/cluster-configuration/cluster-storage#storage-limit) |
| **PlanetScale Metal**        | When your data is approaching the storage size of your cluster                                                                                                                                                                                                                                                                           | Increase the [cluster size](/docs/metal)                                                                                                                                                                                          |

Once you have remediated the issue, your cluster will automatically exit read-only mode.

<Note>
  PlanetScale will send notifications via email and webhook (if enabled) when your storage exceeds 60, 75, 85, 90, and 95 percent, respectively. You can also track disk utilization via [Metrics](/docs/postgres/monitoring/metrics). Emails are sent to all Organization and Database administrators. It is critical that these email addresses are monitored regularly.
</Note>

If the issue was temporary, say due to errant data being written by mistake, you could remove the data, perform a [vacuum](/docs/postgres/cluster-configuration/cluster-storage#example-when-and-how-to-run-vacuum), and then reverse the remediation action. See [Managing Storage](/docs/postgres/cluster-configuration/cluster-storage#managing-your-storage) for more on reducing storage usage.

## Single Node Archiver lag

Single node Postgres clusters offer decreased durability compared to HA offerings. In HA, we use Postgres synchronous replication to guarantee every committed transaction reaches the primary and at least one replica.
As part of our usual (we do this on HA too) durability posture, we archive postgres Write-Ahead Logs (WAL) to durable object storage (S3, GCP Cloud Storage). For single-node, we will enter read-only mode if this archiving process falls too far behind writes on your cluster.

If you see this happening frequently, we recommend sizing your cluster up, or moving to an HA cluster.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt