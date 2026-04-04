# Source: https://planetscale.com/docs/postgres/cluster-configuration/cluster-storage.md

# Cluster storage configuration

> You can configure storage settings for network-attached storage PlanetScale Postgres clusters in the "**Storage**" tab on the Clusters page for your database.

<Note>
  For PlanetScale Postgres clusters launched on PlanetScale Metal instances, storage is scaled by directly scaling the cluster instance size. Storage autoscaling is not available for Metal clusters. To learn more see the documentation for [PlanetScale Metal](/docs/metal)
</Note>

## Configuring storage settings

You must be a database or organization administrator to modify these settings. Adjusting these settings may incur additional charges. To learn more about pricing for storage, see [pricing](/docs/postgres/pricing).

<Steps>
  <Step>From the PlanetScale organization dashboard, select the desired database</Step>
  <Step>Navigate to the **Clusters** page from the menu on the left</Step>
  <Step>Choose the branch whose storage settings you'd like to configure in the "**Branch**" dropdown</Step>
  <Step>Select the **Storage** tab</Step>
  <Step>Configure your disk size and autoscaling settings</Step>
  <Step>Set your storage limit as needed</Step>
  <Step>Click "**Queue storage changes**"</Step>
  <Step>Once you're ready to apply the changes, click "**Apply changes**"</Step>
</Steps>

## Minimum disk size configuration

Configure the minimum disk size for your database cluster. This setting determines the initial storage capacity allocated to your database. The disk size is specified in GB and serves as the baseline storage allocation for your cluster.

<Note>
  The maximum disk size for network-attached storage is 16384 GB (16 TiB).
</Note>

## Enable autoscaling

<Note>
  PlanetScale storage autoscaling is only for network-attached storage database clusters. For [PlanetScale Metal](/docs/metal) based clusters you will need to increase the cluster instance size.
</Note>

Disk autoscaling is enabled by default upon database creation. Disk autoscaling automatically increases storage when your database approaches a disk size utilization threshold, preventing storage-related outages without manual intervention. You can also enable automatic disk shriking.

Both of these options can be configured by going to "Clusters" > "Storage" > and clicking the "Enable autoscaling" checkbox.

For more information, see the [Disk autoscaling documentation](/docs/postgres/cluster-configuration/disk-autoscaling).

## Storage limit

The storage limit sets the maximum amount of storage that can be allocated to your database cluster through autoscaling. This acts as a ceiling to prevent unlimited storage growth and helps control costs.

When autoscaling is enabled, your storage can grow from the minimum disk size up to the storage limit you specify. The storage limit should be set higher than your initial disk size to allow for growth while providing a reasonable upper bound for your storage costs.

<Note>
  The maximum disk size for network-attached storage is 16384 GB (16 TiB).
</Note>

## IOPS

Configure the maximum input/output operations per second for your database. This will be limited by your database cluster size and disk size.

### Storage volume type and IOPS

| Storage type | Default IOPS | Maximum IOPS                         |
| ------------ | ------------ | ------------------------------------ |
| AWS gp3      | 3000         | 16,000 (at 32GB or larger disk size) |

## Bandwidth

The maximum amount of data that can be read or written to your database in a single second. This will be limited by your database cluster size and configured IOPS.

### Storage volume type and bandwidth

| Storage type | Default bandwidth | Maximum bandwidth                     |
| ------------ | ----------------- | ------------------------------------- |
| AWS gp3      | 125 MiB/s         | 1,000 MiB/s (at 4,000 IOPS or higher) |

### Storage throughput limits

For databases created on AWS-based clusters the **maximum configurable throughput** your cluster can support is based on CPU architecture and cluster size.

| CPU Architecture  | Cluster Size                                                                 | Maximum Throughput (in MiB/s) |
| ----------------- | ---------------------------------------------------------------------------- | ----------------------------- |
| AWS x86-64        | PS-DEV, PS-10, PS-20, PS-40, PS-80, PS-160, PS-320, PS-640, PS-1280, PS-2560 | 1000                          |
| AWS aarch64/ARM64 | PS-DEV, PS-10, PS-20, PS-40, PS-80, PS-160, PS-320, PS-640, PS-1280          | 593                           |
| AWS aarch64/ARM64 | PS-2560                                                                      | 1000                          |

## Monthly storage cost

Displays the estimated monthly cost for your current storage configuration. If you adjust your storage configuration the number shown represents the new monthly estimate for the configured values. Billing for storage changes begins once the storage change has completed.

## Tracking changes to storage settings

You can click on the "Changes" tab on the Clusters page to view a log of any changes made to your storage settings. The log will include the settings affected, the original and updated values, status, user that made the changes, start time, and end time.

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt