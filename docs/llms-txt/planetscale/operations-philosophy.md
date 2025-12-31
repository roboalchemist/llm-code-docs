# Source: https://planetscale.com/docs/postgres/operations-philosophy.md

# PlanetScale Postgres operations philosophy

> PlanetScale has a high standard for uptime and availability of Postgres databases.

The foundation of achieving this goal in the cloud is our operator: the software that manages new database creation, version upgrades, resizes, failovers, and other operations in an inherently failure-prone environment.

This document presents our architecture and philosophy on operating PlanetScale Postgres databases.
All customers should read it, as it also covers what can be expected during failovers, querying replicas vs the primary, and the tradeoffs of using direct vs pooled connections.

## Database cluster architecture

The cloud is an inherently failure-prone environment.
Servers can experience degraded performance or become unavailable at any time and for unknown reasons.
Because of this, we must treat all cloud server nodes as ephemeral.

We can embrace failure and build database clusters that are resilient in the cloud environment by understanding our constraints and leveraging the cloud's elasticity within known and practical limits.

Every production database cluster in PlanetScale has a primary and two replicas.
This allows us to embrace server failures through failovers.
Some consider failovers as a problem, but we see that as a fundamental building block for operating reliable databases.
Tolerating the brief disruptions produced by failovers has huge upside: PlanetScale can rapidly deliver changes which continuously increase the quality, reliability, and performance of customer databases.

<img src="https://mintcdn.com/planetscale-cad1a68a/WcazQYbZzMHxCEvC/docs/postgres/primary-replicas.png?fit=max&auto=format&n=WcazQYbZzMHxCEvC&q=85&s=88ba5e541613740f1be44bb3477517bc" alt="Primary and Replicas" data-og-width="1864" width="1864" data-og-height="1162" height="1162" data-path="docs/postgres/primary-replicas.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/WcazQYbZzMHxCEvC/docs/postgres/primary-replicas.png?w=280&fit=max&auto=format&n=WcazQYbZzMHxCEvC&q=85&s=ba4dfb2200cbd2ce199d4c9a42b01469 280w, https://mintcdn.com/planetscale-cad1a68a/WcazQYbZzMHxCEvC/docs/postgres/primary-replicas.png?w=560&fit=max&auto=format&n=WcazQYbZzMHxCEvC&q=85&s=876a930801319614daca988b4241c692 560w, https://mintcdn.com/planetscale-cad1a68a/WcazQYbZzMHxCEvC/docs/postgres/primary-replicas.png?w=840&fit=max&auto=format&n=WcazQYbZzMHxCEvC&q=85&s=93864ee2cf924ac0ad01f7f5a8ba7e04 840w, https://mintcdn.com/planetscale-cad1a68a/WcazQYbZzMHxCEvC/docs/postgres/primary-replicas.png?w=1100&fit=max&auto=format&n=WcazQYbZzMHxCEvC&q=85&s=7aaea9d479e76334dbd98db08988987c 1100w, https://mintcdn.com/planetscale-cad1a68a/WcazQYbZzMHxCEvC/docs/postgres/primary-replicas.png?w=1650&fit=max&auto=format&n=WcazQYbZzMHxCEvC&q=85&s=322ec551e56bc87317c1b842aeb9343c 1650w, https://mintcdn.com/planetscale-cad1a68a/WcazQYbZzMHxCEvC/docs/postgres/primary-replicas.png?w=2500&fit=max&auto=format&n=WcazQYbZzMHxCEvC&q=85&s=1404514c04ecb501ca34ca04d23ff156 2500w" />

This is the most proven architecture for highly-available database clusters for several reasons:

1. Replicating data to multiple servers is crucial for data durability, especially in a cloud environment.
   All data is replicated 3 ways at minimum.
2. Each instance is in a distinct availability zone.
   This means we can be resilient to zone-wide incidents.
3. Replicas can receive read queries that can tolerate replication lag.
   This allows offloading work from the primary, reserving it for writes and critical reads.
4. In the event of an incident in the primary's availability zone, we can failover to a healthy replica in a different availability zone.
   Likewise, when performing a planned upgrade on the primary instance, we first promote a healthy replica to become primary before upgrading the old primary (now demoted to a replica)
   Failovers take on the order of seconds, not minutes or hours, getting you back online quickly.

Having a three-node configuration as the starting point for all clusters allows PlanetScale to operate these databases in ways many other providers cannot.
Failovers are used to replace primaries when they go down unexpectedly.
The same, proven cluster failover techniques are used for other changes like upgrading instances, version patches, and reconfiguration.
This means customers benefit from tried-and-true database management techniques to increase availability, and minimize (though not eliminate) downtime during these operations.

## Continual improvement

Most Postgres database platforms shy away from version updates and other incremental improvements due to their disruptive nature.
Many services require minutes or even hours of downtime to handle this.

The PlanetScale philosophy is different.
To give our customers the best possible Postgres experience, we believe that regular version bumps, bugfixes, and quality-of-life improvements are necessary.
We aim to do image upgrades no more than once per week, though we may do so more frequently for urgent updates like security patches.

Because this requires node failovers, these upgrades lead to a short period of database unavailability (seconds) about once per week.

## The ideal Postgres experience

PlanetScale provides a well-rounded, out-of-the-box Postgres experience while also giving users what they need to tune it to their liking.
This shows up in several aspects of the product:

* Each database is given custom default tunings depending on CPU, RAM, and disk characteristics.
  Users can adjust and carefully monitor the effects of their own changes via the Clusters and Insights pages.
* In addition, we tune `effective_io_concurrency` based on the IOPS values specific to your database.
  For example, each Metal node type has unique and very large IOPS capacity, so we customize it on a per-instance-type basis.
  But we also let you experiment with your own tunings.
* Users have lots of freedom to customize their Postgres roles via our UI, giving them fine-grained control over permissions.
* Both direct-to-Postgres and PgBouncer connections are available by default.
  Each has tradeoffs, and we let you choose what makes the most sense for your applications.

The aim is to set you up with a strong foundation, and give users the tools they need to tune for their use-cases.

## Minimizing the impact of configuration changes

PlanetScale takes the database unavailability produced by upgrades extremely seriously.
We monitor this downtime across the fleet, and make continual efforts to reduce its impact.
We apply context-appropriate, rather than a one-size fits all, upgrade strategies to ensure that a given upgrade takes no more time than absolutely necessary.

PlanetScale allows manual configuration of a number of parameters via the [clusters](/docs/postgres/cluster-configuration) page.
Each configuration change falls into one of two categories:

* Reloadable changes: The change can be applied with no need to restart Postgres.
  When applying these, there is zero downtime.
* Restart-required: Postgres requires the server be restarted for the change to take effect.
  When applying these, you can expect a brief period of server unavailability due to the restart.

In the latter case, what we do is more sophisticated than a simple server restart.
Because we have a primary and two replicas, we typically start these configuration changes by applying them to and restarting the replicas.
Once these are ready, we do a switchover from the old primary to one of the replicas with the upgraded configuration.
The config is then applied and the final instance restarted, now demoted to a replica.

<img src="https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/config-change-restart.png?fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=edd337e6e4a88f52579e060b8195b1b0" alt="Config change with restart" data-og-width="3501" width="3501" data-og-height="1169" height="1169" data-path="docs/postgres/config-change-restart.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/config-change-restart.png?w=280&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=f68dddb35c0572fbd51b72e1ecbdf432 280w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/config-change-restart.png?w=560&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=a3ee8da7b70c1c4f7c0da325eb38ff7f 560w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/config-change-restart.png?w=840&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=1ec42d1196f152519ddc57aeb1e9ffcd 840w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/config-change-restart.png?w=1100&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=09b2c760904df1ef73c587456d7ab4aa 1100w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/config-change-restart.png?w=1650&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=7717ba5533d121f99755464865cdc1ad 1650w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/config-change-restart.png?w=2500&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=7cd3410dd7ffd5c840e625fa59e30654 2500w" />

This process allows us to minimize end-user downtime.
There remains an unavoidable several-second window of unavailability.
In addition, all direct connections will be terminated, so your application should have retry logic to accommodate for this.
There are a few configuration options that are [required by Postgres](https://www.postgresql.org/docs/current/hot-standby.html#HOT-STANDBY-ADMIN) to be applied to the primary before replicas.
For these, you will notice a slightly longer unavailability period.

Normally a primary shutdown proceeds in a fast and orderly manner within a second or two, allowing the operator to promote a replica to primary.
In cases where the operator is not able to quickly and cleanly shutdown the primary due to unresponsive user queries or transactions, the operator will failover to a replica after a timeout of 30 seconds.

PgBouncer connections will persist through all config changes.

## Database cluster sizing

PlanetScale does not support autoscaling of CPU and RAM.
Instead, users are put in the driver's seat to choose the hardware the database runs on, and are given tools to closely monitor performance and adjust resources when needed.
There are two main ways to increase the compute capacity of a cluster: Adding replicas and resizing all nodes.

### Adding Replicas

Each production PlanetScale database (excluding single node) has 1 primary and 2 [replicas](/docs/postgres/scaling/replicas).
In this standard configuration, read traffic can be [routed to a replica](/docs/postgres/scaling/replicas#how-to-query-postgres-replicas) rather than relying on the primary for everything.
It's important not to over-stress your replicas, however.
If all three nodes in the cluster experience too much strain, failovers will be more disruptive, since the cluster will temporarily go from 3 nodes down to 2.
Reads from replicas must also be able to tolerate replication lag.

If you only need to increase the read capacity of the cluster, a good option can be to add 1 or several additional replicas.
This is done through the [Clusters](/docs/postgres/cluster-configuration) menu, and has no negative impact on the other nodes when being added.

### Resizing a cluster

Resizing a cluster leads to database connections being terminated.
Therefore, it's important for your application to have connection retry logic.

Consider the case where you need to upgrade from an `M-160` database cluster to an `M-320`, doubling the compute resources of each node.
After applying the upgrade, three new `M-320` nodes are created.
These are caught up with the primary through a combination of a backup restore and data replication.

<img src="https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/cluster-resize-1.png?fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=ced1ff95e9ce762110b0f652d8886005" alt="Cluster Resize 1" data-og-width="2162" width="2162" data-og-height="1187" height="1187" data-path="docs/postgres/cluster-resize-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/cluster-resize-1.png?w=280&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=81a7bb92955f32a0264c85d2dd743a38 280w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/cluster-resize-1.png?w=560&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=7f0484d209c5923bac082e55cc59b088 560w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/cluster-resize-1.png?w=840&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=3183eac038676fae4d991b7b9aa64b39 840w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/cluster-resize-1.png?w=1100&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=8d538f93b6d47b1db0511809836e4f70 1100w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/cluster-resize-1.png?w=1650&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=1e69ccd44aefa11bc057d2a5734f0da5 1650w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/cluster-resize-1.png?w=2500&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=bbba3fc94e8cf31e0eb9357734636e78 2500w" />

Once these new `M-320` replicas are sufficiently caught up, the operator transitions primaryship to one of the new `M-320` nodes.
After this, the old `M-160` replicas are decommissioned, using the new ones for all replica traffic.
During each node replacement, connections to the decommissioned node will be destroyed.
New connections will need to be made to re-establish with one of the new nodes.

<img src="https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/cluster-resize-2.png?fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=71a04aee7f55f0d5ff393df7cdd2e598" alt="Cluster Resize 2" data-og-width="2181" width="2181" data-og-height="932" height="932" data-path="docs/postgres/cluster-resize-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/cluster-resize-2.png?w=280&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=a43236270b1ded7a957c5e762b582496 280w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/cluster-resize-2.png?w=560&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=67306337aa11cea1b461d92d972c84b7 560w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/cluster-resize-2.png?w=840&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=5a9b2d4fa925f42cad377f95edeea916 840w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/cluster-resize-2.png?w=1100&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=3ebbb5dca2cfe6d41da78715f624b313 1100w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/cluster-resize-2.png?w=1650&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=063c25fb9baf5210b9a1796957eed852 1650w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/cluster-resize-2.png?w=2500&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=b2c73a85655df524bbcf62a131334032 2500w" />

During the upgrade process, all database connections will be terminated.
Normally a primary promotion proceeds in a fast and orderly manner in less than 5 seconds.
In cases where the operator is not able to quickly and cleanly shutdown the primary due to unresponsive user queries or transactions, the operator will failover to a replica after a timeout of 30 seconds.

For all the steps leading up to the node replacement, we keep your existing `M-160` database cluster fully functional.
Only brief periods of unavailability are required to ensure we can smoothly replace each node.

Many ORMs have built-in connection retry logic to help with these scenarios.
It's likely your application already has such capabilities if you are using libraries like Rails ActiveRecord, Laravel Eloquent, and Drizzle.

## Unplanned failures

In a cloud-native environment, server failure is to be expected.
This is unavoidable, so we embrace the behavior and have proven failover systems in place to address issues as quickly as possible.
PlanetScale has executed millions of failovers across our Postgres and Vitess database clusters.
They are a well-exercised path and are proven to be an invaluable mechanism for database operations and handling node failures.

### Replicas

Replica health is important to keep your PlanetScale database cluster operating smoothly.
Replica failures are automatically detected and automatically replaced.
There will be a period of time where your cluster has only the primary and a single replica while the replacement replica is created and data restored to it.
This time varies from minutes to hours depending on database size and your instance type.

<img src="https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/failed-replica.png?fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=7b4f0a09b7f9c3551b90d7ec86c252de" alt="Failed replica" data-og-width="1784" width="1784" data-og-height="1008" height="1008" data-path="docs/postgres/failed-replica.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/failed-replica.png?w=280&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=acd60adbeddba6777c2b25d8105d58aa 280w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/failed-replica.png?w=560&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=794ec9f4310d6c82e77981afa34c0817 560w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/failed-replica.png?w=840&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=8c4183b129e2884ef0a19444a4d8392b 840w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/failed-replica.png?w=1100&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=5502c33bddec53ab40abd116fcb8e3a5 1100w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/failed-replica.png?w=1650&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=42d47c863e1f7e86912ba1e29003c205 1650w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/failed-replica.png?w=2500&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=aae598f33d24b7d4313e2618319a6811 2500w" />

Any connections routed to the failed replica will be terminated and need to be re-established.
When re-established, we will route the connections to the other available replica.

### Primaries

The PlanetScale operator will detect a primary failure within seconds and immediately begin the process of replacing the node.
The new primary is chosen based on which one is the most caught-up from the state of the primary.
All Postgres databases are run with semi-sync replication, meaning that at least one replica should have received all the writes that the primary had seen.
Once chosen, this replica is promoted to primary and a new node is brought up to replace it.

<img src="https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/failed-primary.png?fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=ec708d261905e8739112cfb6697a7bb1" alt="Failed primary" data-og-width="2717" width="2717" data-og-height="1047" height="1047" data-path="docs/postgres/failed-primary.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/failed-primary.png?w=280&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=4c0087c4a95ac714ca3bd719adbd6362 280w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/failed-primary.png?w=560&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=3657137816e7fac527726d9a37af3f9e 560w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/failed-primary.png?w=840&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=0371c466074bed3edc67f144d9bb060e 840w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/failed-primary.png?w=1100&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=407bd93ca1a913ba50e9128f684c6ea1 1100w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/failed-primary.png?w=1650&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=58de5f612a49577735a4bb2b49c05476 1650w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/failed-primary.png?w=2500&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=24e70614efa25aba62a9762edf78d59d 2500w" />

The primary failure, detection, and election process typically takes 10 seconds or less when all other components of the cluster are healthy.
During this time your primary database will be inaccessible and no connections can be made.
The time it takes for the new replica to catch-up to the primary varies from minutes to hours depending on database size and your instance type.

## Image upgrades

We have fast iteration cycles at PlanetScale, always aiming to improve the features and capabilities of our customer's Postgres databases.
Postgres minor version updates, PgBouncer updates, and adding support for new extensions all require us to update the container images for your database.
When this happens, the Kubernetes pods that power your primary and replicas are rolled.

<img src="https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/image-upgrade.png?fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=53dbb79032d5891d28a732b17416dfdf" alt="Image upgrade" data-og-width="3153" width="3153" data-og-height="1113" height="1113" data-path="docs/postgres/image-upgrade.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/image-upgrade.png?w=280&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=b3f69621d9cc47bce50688c14347c217 280w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/image-upgrade.png?w=560&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=20088e65fb77a67112b64690056c39ed 560w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/image-upgrade.png?w=840&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=77453aa38637e36ef458947dd2f94cd8 840w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/image-upgrade.png?w=1100&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=a5b64133fff86540ab80689e6ca60ae2 1100w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/image-upgrade.png?w=1650&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=bf8de5daf72589f48a92ce3558b9e302 1650w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/image-upgrade.png?w=2500&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=4e938ed3f4c2ee10aa2943f1919bbb19 2500w" />

As with other operations described earlier, this leads to terminated connections and a brief period of database inaccessibility.
We aim to do image upgrades no more than once per week, though we may do so more frequently for urgent updates like security patches.

## Disk availability, scaling, and cost

For databases using network-attached storage, autoscaling is enabled by default.
This is to protect availability of your database.
Reaching 100% full on a storage volume leads to database downtime.

<img src="https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/disk-autoscaling.png?fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=b0fbcce0ee3969841689fc92a7f0b401" alt="Disk autoscaling" data-og-width="2000" width="2000" data-og-height="1378" height="1378" data-path="docs/postgres/disk-autoscaling.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/disk-autoscaling.png?w=280&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=c92afb8a1438967ec7cdb9d260d63d68 280w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/disk-autoscaling.png?w=560&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=abe110ab6754b20494f488ff3bbc644d 560w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/disk-autoscaling.png?w=840&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=727bc70510773c6de8537f23258fb8f7 840w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/disk-autoscaling.png?w=1100&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=dab4a8cf29f49d912431921cb2c6d93f 1100w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/disk-autoscaling.png?w=1650&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=48ecff856ede40a3b20eaab22784f883 1650w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/disk-autoscaling.png?w=2500&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=889374187d7577a38ee755b34f946d29 2500w" />

Cloud providers like AWS and GCP limit how frequently network-attached disks can be resized.
In both cases, there is a multi-hour cooldown period between resizing operations.
Also, these volumes typically do not support shrinking.

When our disk auto-scaler is able to spread out disk scale-up sufficiently, no downtime is needed to scale the disks.
This is true in the vast majority of cases.

When data growth is rapid, the auto-scaler may need to complete a **surge resize** to support the writes.
In this case, PlanetScale creates brand new database nodes with larger network-attached storage volumes.
Once ready, the nodes in your cluster get replaced with these new ones to increase capacity.
If the surge autoscaler is able to complete the resize before your disk fills, downtime will be minimal for growing the disk (seconds).
If your disk fills before the new disks are ready, you will experience a longer period of downtime.

We make every effort to keep your network-attached storage disk from filling, but it's important for the database administrators to pay close attention to storage and take manual intervention when necessary.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt