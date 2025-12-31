# Source: https://planetscale.com/docs/postgres/cluster-configuration/parameters.md

# Cluster configuration parameters

> You can configure your PlanetScale Postgres cluster settings in the "**Parameters**" tab on the Clusters page for your database.

You can configure your PlanetScale Postgres cluster settings in the "**Parameters**" tab on the Clusters page for your database.

The defaults for each parameter depend on the configuration of your cluster. The defaults have been chosen to optimize performance, resource usage, and connection handling for each cluster size. However, you are able to fine-tune each of these settings as needed.

## Configuring parameter values

You must be a database or organization administrator to modify these settings.

1. From the PlanetScale organization dashboard, select the desired database
2. Navigate to the **Clusters** page from the menu on the left
3. Choose the branch whose parameters you'd like to configure in the "**Branch**" dropdown
4. Select the **Parameters** tab
5. Search for a specific parameter or scroll through the page to see all configurable parameters
6. Update the value for the parameter(s) you wish to adjust
7. Click "**Queue parameter changes**"
8. Once you're ready to apply the changes, click "**Apply changes**"

## Tracking changes to parameters

You can click on the "Changes" tab on the Clusters page to view a log of any changes made to your parameter settings. The log will include the settings affected, the original and updated values, status, user that made the changes, start time, and end time.

<Note>
  When updating a cluster's size, some [parameters](/docs/postgres/cluster-configuration/parameters) will automatically
  be adjusted. Each cluster size is associated with default parameter settings, changing the cluster size will also
  update those defaults. The exception to this is if you manually override a default parameter setting. In that case, a
  cluster size adjustment will not automatically change that setting.
</Note>

## Parameter change types

PostgreSQL parameter changes fall into two categories based on how they are applied:

* **Reloadable changes**: The parameter can be updated without restarting PostgreSQL, resulting in zero downtime
* **Restart-required changes**: PostgreSQL requires a cluster restart for the parameter to take effect

Parameters that require a restart are marked with a ✅ in the "Restart Required" column in the [parameter reference table](#default-parameter-values) below.

### Restart behavior for production clusters

When you apply parameters that require a restart, PlanetScale performs a rolling restart process to minimize downtime:

1. Configuration changes are first applied to replica instances and they are restarted
2. Once replicas are ready, a switchover promotes one replica to become the new primary
3. The configuration is applied to the former primary (now a replica) and it is restarted

<img src="https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/cluster-configuration/config-change-restart.png?fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=45d150b0d1b17b527ce56bf4b675f903" alt="Config change with restart" data-og-width="3501" width="3501" data-og-height="1169" height="1169" data-path="docs/postgres/cluster-configuration/config-change-restart.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/cluster-configuration/config-change-restart.png?w=280&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=830ae7067c370466ca4271deba042608 280w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/cluster-configuration/config-change-restart.png?w=560&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=6af727f44c8af722e3f504bd7efe11f7 560w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/cluster-configuration/config-change-restart.png?w=840&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=dfb37f96d52a91a37d7bf40a73d2ab3c 840w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/cluster-configuration/config-change-restart.png?w=1100&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=db47ef6bbefcd554bdb45e27998c859d 1100w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/cluster-configuration/config-change-restart.png?w=1650&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=579b4012953bc76a77c5cc5e240ab534 1650w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/cluster-configuration/config-change-restart.png?w=2500&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=2bd8a73b10e3ddfe6919524f166e9a04 2500w" />

This rolling restart process minimizes downtime, but there remains a brief several-second window of unavailability during the primary switchover. All direct database connections will be terminated during this process, so your application should implement connection retry logic. With the exception of the `Number of processes` parameter for PgBouncer, PgBouncer connections persist through all parameter changes and do not require reconnection.

Some parameters are [required by PostgreSQL](https://www.postgresql.org/docs/current/hot-standby.html#HOT-STANDBY-ADMIN) to be applied to the primary before replicas, which may result in a slightly longer unavailability period.

## Default parameter values

The following table shows the default values for parameters that are displayed by default to customers. You can find additional parameters in the search field.

| Parameter                             | Restart Required            | Description                                                                                                                 |
| ------------------------------------- | --------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| **PgBouncer**                         |                             |                                                                                                                             |
| Number of processes                   | ✅ (restarts PGBouncer only) | Sets the number of PgBouncer processes that will run on each node in this branch's cluster                                  |
| default\_pool\_size                   |                             | Sets the number of server connections to allow per user/database pair                                                       |
| max\_client\_conn                     |                             | Sets the maximum number of client connections allowed                                                                       |
| max\_db\_client\_connections          |                             | Sets the maximum number of client connections allowed per database (regardless of user). 0 is unlimited                     |
| max\_db\_connections                  |                             | Sets the maximum number of server connections allowed per database (regardless of user). 0 is unlimited                     |
| max\_prepared\_statements             |                             | Sets the maximum number of client-prepared statements available across server connections                                   |
| max\_user\_connections                |                             | Sets the maximum number of server connections allowed per user (regardless of database). 0 is unlimited                     |
| server\_lifetime                      |                             | Sets how long an unused server connection stays open                                                                        |
| server\_idle\_timeout                 |                             | Sets how long an idle server connection stays open                                                                          |
| **Resource usage**                    |                             |                                                                                                                             |
| effective\_io\_concurrency            |                             | Sets the number of simultaneous requests that can be handled efficiently by the disk subsystem                              |
| effective\_cache\_size                |                             | Sets the planner's assumption about the total size of the data caches                                                       |
| huge\_pages                           | ✅                           | Controls whether huge pages are requested for the main shared memory area                                                   |
| maintenance\_io\_concurrency          |                             | Sets the number of simultaneous requests that can be handled efficiently by the disk subsystem for maintenance operations   |
| maintenance\_work\_mem                |                             | Sets the maximum memory to be used for maintenance operations                                                               |
| max\_parallel\_maintenance\_workers   |                             | Sets the maximum number of parallel processes per maintenance operation                                                     |
| max\_parallel\_workers                |                             | Sets the maximum number of parallel workers that can be active at one time                                                  |
| max\_parallel\_workers\_per\_gather   |                             | Sets the maximum number of parallel processes per executor node                                                             |
| max\_worker\_processes                | ✅                           | Sets the maximum number of background processes that the cluster can support                                                |
| shared\_buffers                       | ✅                           | Sets the amount of memory the database server uses for shared memory buffers                                                |
| work\_mem                             |                             | Sets the amount of memory the database will use for internal operations like sorting and hashing                            |
| **Write-ahead log**                   |                             |                                                                                                                             |
| max\_slot\_wal\_keep\_size            |                             | Sets the maximum WAL size that can be reserved by replication slots                                                         |
| max\_wal\_size                        |                             | Sets the WAL size that triggers a checkpoint                                                                                |
| min\_wal\_size                        |                             | Sets the minimum size to shrink the WAL to                                                                                  |
| wal\_buffers                          | ✅                           | Sets the number of disk-page buffers in shared memory for WAL                                                               |
| wal\_level                            | ✅                           | Sets the level of information written to the WAL                                                                            |
| **Query tuning**                      |                             |                                                                                                                             |
| deadlock\_timeout                     |                             | Sets the maximum time to wait on a lock before checking for deadlocks                                                       |
| default\_statistics\_target           |                             | Sets the default statistics target for table columns without a column-specific target set                                   |
| random\_page\_cost                    |                             | Sets the planner's estimate of the cost of a nonsequentially fetched disk page                                              |
| seq\_page\_cost                       |                             | Sets the planner's estimate of the cost of a sequentially fetched disk page                                                 |
| **Connections and authentication**    |                             |                                                                                                                             |
| max\_connections                      | ✅                           | Sets the maximum number of concurrent connections                                                                           |
| **Replication**                       |                             |                                                                                                                             |
| hot\_standby\_feedback                |                             | Sends feedback to the primary about queries being executed on the standby. Required for logical replication failover        |
| max\_logical\_replication\_workers    | ✅                           | Sets the maximum number of logical replication workers                                                                      |
| max\_replication\_slots               | ✅                           | Sets the maximum number of replication slots that the server can support                                                    |
| max\_sync\_workers\_per\_subscription |                             | Sets the maximum number of synchronization workers per subscription                                                         |
| max\_wal\_senders                     | ✅                           | Sets the maximum number of WAL senders                                                                                      |
| sync\_replication\_slots              |                             | Enables standbys to synchronize logical replication streams from the primary. Required for logical replication failover     |
| **Failover**                          |                             |                                                                                                                             |
| failover\_delay                       |                             | Sets the time to wait before triggering a failover to drain inflight transactions                                           |
| **Statistics**                        |                             |                                                                                                                             |
| track\_io\_timing                     |                             | Enables timing of database I/O calls. This may cause significant overhead                                                   |
| **Logging**                           |                             |                                                                                                                             |
| log\_lock\_waits                      |                             | Logs the duration of lock waits that exceed the deadlock\_timeout                                                           |
| log\_min\_duration\_statement         |                             | Sets the minimum execution time above which all statements will be logged                                                   |
| **Client connection defaults**        |                             |                                                                                                                             |
| shared\_preload\_libraries            | ✅                           | Specifies shared libraries to preload into the server at server start                                                       |
| **Autovacuum**                        |                             |                                                                                                                             |
| autovacuum\_vacuum\_scale\_factor     |                             | Specifies a fraction of the table size to add to autovacuum\_vacuum\_threshold when deciding whether to trigger a VACUUM    |
| autovacuum\_analyze\_scale\_factor    |                             | Specifies a fraction of the table size to add to autovacuum\_analyze\_threshold when deciding whether to trigger an ANALYZE |

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt