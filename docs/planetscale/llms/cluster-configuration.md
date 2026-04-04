# Source: https://planetscale.com/docs/vitess/scaling/cluster-configuration.md

# Source: https://planetscale.com/docs/vitess/cluster-configuration.md

# Source: https://planetscale.com/docs/postgres/cluster-configuration.md

# Cluster configuration

The Clusters page in your PlanetScale dashboard allows you to monitor your cluster utilization and configure cluster settings for each branch in your database. You can:

* Adjust the cluster size and instance type ([Metal](/docs/metal) vs network-attached storage)
* Configure the number of replicas
* Monitor cluster utilization with real-time graphs
* Configure storage settings including:
  * Disk size configuration
  * Autoscaling settings and thresholds
  * Storage limits
  * IOPS configuration
  * Bandwidth settings
* Modify PostgreSQL [parameters](/docs/postgres/cluster-configuration/parameters)
* Manage PostgreSQL [extensions](/docs/postgres/extensions)
* View and track configuration changes

These settings may only be changed by a [database administrator or organization administrator](/docs/security/access-control).

## Adjusting cluster size

To adjust your cluster size:

<Steps>
  <Step>From the PlanetScale organization dashboard, select the desired database</Step>
  <Step>Navigate to the **Clusters** page from the menu on the left</Step>
  <Step>In the Cluster size section, click on the cluster size dropdown</Step>

  <Step>
    Select the new cluster size, (Metal or network-attached storage). If you select Metal, make sure you select the
    correct storage size.
  </Step>

  <Step>Click Queue instance changes > Apply changes to apply the new cluster size</Step>
</Steps>

<Note>
  You cannot change the [CPU architecture](/docs/postgres/cluster-configuration/cpu-architectures) (AMD, Intel, ARM) of an existing cluster. To use a different architecture, you'll need to create a new branch with the desired cluster type.
</Note>

Cluster resizing may take several minutes to complete and you cannot make additional configuration changes until the resize is finished.

Consider the case where you need to upgrade from an `M-160` database cluster to an `M-320`, doubling the compute resources of each node.
After applying the upgrade, three new `M-320` nodes are created.
These are caught up with the primary through a combination of a backup restore and data replication.

<img src="https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/cluster-resize-1.png?fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=ced1ff95e9ce762110b0f652d8886005" alt="Cluster Resize 1" data-og-width="2162" width="2162" data-og-height="1187" height="1187" data-path="docs/postgres/cluster-resize-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/cluster-resize-1.png?w=280&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=81a7bb92955f32a0264c85d2dd743a38 280w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/cluster-resize-1.png?w=560&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=7f0484d209c5923bac082e55cc59b088 560w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/cluster-resize-1.png?w=840&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=3183eac038676fae4d991b7b9aa64b39 840w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/cluster-resize-1.png?w=1100&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=8d538f93b6d47b1db0511809836e4f70 1100w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/cluster-resize-1.png?w=1650&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=1e69ccd44aefa11bc057d2a5734f0da5 1650w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/cluster-resize-1.png?w=2500&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=bbba3fc94e8cf31e0eb9357734636e78 2500w" />

Once these new `M-320` replicas are sufficiently caught up, the operator transitions primaryship to the one of the new `M-320` nodes.

After this, the old `M-160` replicas are decommissioned, using the new ones for all replica traffic.
During each node replacement, the connections to the decommissioned node will be terminated.
Your clients will need to establish new connections with the new nodes.

<img src="https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/cluster-resize-2.png?fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=71a04aee7f55f0d5ff393df7cdd2e598" alt="Cluster Resize 2" data-og-width="2181" width="2181" data-og-height="932" height="932" data-path="docs/postgres/cluster-resize-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/cluster-resize-2.png?w=280&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=a43236270b1ded7a957c5e762b582496 280w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/cluster-resize-2.png?w=560&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=67306337aa11cea1b461d92d972c84b7 560w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/cluster-resize-2.png?w=840&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=5a9b2d4fa925f42cad377f95edeea916 840w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/cluster-resize-2.png?w=1100&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=3ebbb5dca2cfe6d41da78715f624b313 1100w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/cluster-resize-2.png?w=1650&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=063c25fb9baf5210b9a1796957eed852 1650w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/cluster-resize-2.png?w=2500&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=b2c73a85655df524bbcf62a131334032 2500w" />

During the primary cutover all database connections will be terminated.
Normally a primary promotion proceeds in a fast and orderly manner in less than 5 seconds.
In cases where the operator is not able to quickly and cleanly shutdown the primary due to unresponsive user queries or transactions, the the operator will failover to a replica after a timeout of 30 seconds.

For all the steps leading up to the node replacement, your existing M-160 database cluster remains fully functional.
Due to the way this works, it's important for your application to have connection retry logic.

## Managing replicas

[Replicas](/docs/postgres/scaling/replicas) provide read scalability and high availability for your PostgreSQL database. Each production branch (excluding single node) comes with 2 replicas by default.

<Note>
  If you add additional replicas beyond the default 2, you will incur additional charges. Billing for additional replicas begins once the replica change has completed. See [pricing](https://planetscale.com/docs/postgres/pricing) to understand the additional costs.
</Note>

To adjust the number of replicas:

<Steps>
  <Step>From the PlanetScale organization dashboard, select the desired database</Step>
  <Step>Navigate to the **Clusters** page from the menu on the left</Step>
  <Step>In the **Cluster size** section, use the dropdown **Replicas** to select your desired number of replicas</Step>
  <Step>Click **Queue instance changes**</Step>
  <Step>Click **Apply changes** to immediately begin the process to update the number of replicas</Step>
</Steps>

## Monitoring cluster utilization

The cluster utilization graph provides real-time insights into your database's CPU and memory utilization. You can change the graph view to the past hour, 6 hours, 12 hours, day, or week. The graph also displays indicators when cluster settings were changed.

<Note>
  If you are consistently close to 100% CPU, we recommend upsizing your cluster. Likewise, if you are consistently below 50% CPU, you can likely safely downgrade.
</Note>

## Parameters and settings

You can customize your PostgreSQL cluster's behavior in the **Parameters** tab on the Clusters page. This allows you to configure the following settings:

* PgBouncer
* Resource usage
* Write-ahead logs (WAL)
* Query tuning
* Connections and authentication
* Failover

For more information about each setting, refer to the [Parameters documentation](/docs/postgres/cluster-configuration/parameters).

## Configuring storage

You can configure your cluster's storage settings in the "**Storage**" tab on the Clusters page. Storage configuration includes:

* Setting the minimum disk size for your cluster
* Enabling autoscaling to automatically increase storage when approaching limits
* Configuring storage limits to control maximum storage allocation
* Monitoring current storage usage

For detailed information about storage configuration options, refer to the [Storage configuration documentation](/docs/postgres/cluster-configuration/cluster-storage).

## Managing extensions

PostgreSQL [extensions](/docs/postgres/extensions) provide additional functionality for your database. The "**Extensions**" tab on the Clusters page allows you to view and enable/disable available extensions.

### Extension management

* View currently installed extensions
* See available extensions for installation
* Enable or disable extensions
* Configure extension parameters

## Monitoring configuration changes

The Clusters page provides visibility into all changes made to your cluster settings.

* Navigate to the Changes tab for the selected branch on the Clusters page
* View a chronological list of all configuration changes
* See details including:
  * What was changed (cluster size, replicas, parameters)
  * Previous and new values
  * Status of the change
  * Who initiated the change
  * When the change was started and completed

<Note>
  When updating a cluster's size, some [parameters](/docs/postgres/cluster-configuration/parameters) will automatically be adjusted. Each cluster size is associated with default parameter settings, changing the cluster size will also update those defaults. The exception to this is if you manually override a default parameter setting. In that case, a cluster size adjustment will not automatically change that setting.
</Note>

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt