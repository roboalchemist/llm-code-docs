# Source: https://docs.api7.ai/enterprise/upgrade-guides/cluster-migration.md

# API Gateway Cluster Migration

Cluster migration is the process of moving an entire API7 Enterprise deployment from one infrastructure environment to another while keeping the software version the same. This guide is designed for platform engineers and architects who need to perform a zero-downtime migration for scenarios like data center relocation, infrastructure upgrades, or transitioning between cloud providers.

Unlike a version upgrade, a cluster migration focuses on moving the existing deployment to a new, parallel environment without changing the version of the Control Plane (CP) or Data Plane (DP). The core of this strategy is to ensure configuration and data integrity by backing up the production database and restoring it in the new cluster. Traffic is then carefully shifted using a load balancer, allowing for a seamless transition with a reliable rollback plan.

This approach mitigates the risks associated with infrastructure changes and prevents common pitfalls, such as mTLS certificate mismatches that can occur if a new Data Plane incorrectly connects to an old Control Plane.

## Migration Workflow[â](#migration-workflow "Direct link to Migration Workflow")

The following diagram illustrates the workflow for a zero-downtime cluster migration:

<!-- -->

The diagram above shows a complete migration workflow. The old cluster (Cluster A) continues to serve production traffic while the new cluster (Cluster B) is being prepared. Once the new cluster is verified and healthy, traffic is gradually shifted from the old cluster to the new one through a load balancer.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

Before you begin the cluster migration, ensure that the following prerequisites are met to ensure a smooth and successful transition.

| Prerequisite                     | Description                                                                                                                                       |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| **New Cluster Infrastructure**   | The infrastructure for the new cluster (Cluster B) must be fully provisioned, including all networking, storage, and computing resources.         |
| **API7 Enterprise Installation** | The same version of API7 Enterprise that is running on the old cluster (Cluster A) must be installed on the new cluster.                          |
| **Database Tools**               | Database backup and restore tools must be configured and tested for both the old and new database environments.                                   |
| **Load Balancer**                | An external load balancer must be in place with the ability to manage and split traffic between the old and new clusters.                         |
| **Permissions**                  | You must have the necessary administrative permissions to perform a database backup from the old cluster and a restore to the new cluster.        |
| **Pre-migration Testing**        | A complete migration rehearsal should be performed in a staging or testing environment to validate the process and identify any potential issues. |

## Migration Steps[â](#migration-steps "Direct link to Migration Steps")

Follow these steps to perform a zero-downtime cluster migration. This process is designed to be sequential and includes verification checks at each stage to ensure a safe transition.

### Step 1: Freeze Configuration Changes on the Old Cluster[â](#step-1-freeze-configuration-changes-on-the-old-cluster "Direct link to Step 1: Freeze Configuration Changes on the Old Cluster")

To prevent data inconsistencies during the migration, you must establish a configuration freeze on the old cluster (Cluster A). Announce a maintenance window to your development teams and halt all configuration changes made through the API7 Dashboard, Admin API, or any other configuration management tools.

This freeze ensures that the database backup you create contains a complete and static snapshot of your production configuration. Any changes made after the backup will not be migrated to the new cluster.

### Step 2: Back Up and Restore the Database[â](#step-2-back-up-and-restore-the-database "Direct link to Step 2: Back Up and Restore the Database")

Once the configuration freeze is in effect, proceed with backing up the database from the old cluster and restoring it in the new one.

1. **Back-Up Database A**: Perform a full backup of the database from Cluster A. Ensure the backup includes all API configurations, routes, plugins, consumer credentials, and SSL certificates. Refer to the [Database Backup and Restoration](https://docs.api7.ai/enterprise/upgrade-guides/backup-and-restore.md#database-backup) guide for detailed instructions.
2. **Transfer and Restore to Database B**: Transfer the backup file to the new cluster environment and restore it to Database B. After the restoration is complete, verify the data integrity by checking the number of APIs, routes, and other critical configuration objects.

### Step 3: Start and Verify the New Cluster[â](#step-3-start-and-verify-the-new-cluster "Direct link to Step 3: Start and Verify the New Cluster")

With the database restored, you can now bring the new cluster (Cluster B) online.

1. **Start Control Plane B**: Start the Control Plane (CP) in the new cluster and ensure it successfully connects to the restored database (Database B).

2. **Verify DP Manager Address**: Before deploying the Data Plane, verify that the DP Manager address in the new cluster is correctly configured to point to the new Control Plane. You can check this in the Control Plane's **Gateway Settings > Deployment** page, or update the configuration in your deployment method:

   <!-- -->

   * For Helm deployments, update the `etcd.host[0]` value in your `values.yaml` file.
   * For Docker/Docker Compose deployments, ensure the `API7_DP_MANAGER_ENDPOINTS` address in your deployment configuration points to the new Control Plane.

3. **Verify Health**: Use the [Gateway Health Probe](https://docs.api7.ai/enterprise/best-practices/gateway-health-probe.md) to confirm that the new DP is running and healthy. You should also check the logs of both the CP and DP to ensure there are no connection errors.

### Step 4: Gradually Shift Traffic[â](#step-4-gradually-shift-traffic "Direct link to Step 4: Gradually Shift Traffic")

Once the new cluster is running and verified, you can begin shifting production traffic to it using your external load balancer.

1. **Initial Traffic Shift**: Configure the load balancer to send a small percentage of traffic (e.g., 5-10%) to the new cluster's Data Plane (DP B).
2. **Monitor and Validate**: Closely monitor the performance of the new cluster, including latency, error rates, and resource utilization. Compare these metrics against the old cluster to ensure the new cluster is performing as expected.
3. **Incremental Increase**: If the new cluster remains stable, gradually increase the traffic percentage in stages (e.g., 25%, 50%, 75%, 100%). At each stage, continue to monitor the system's health and performance.

### Step 5: Complete the Migration[â](#step-5-complete-the-migration "Direct link to Step 5: Complete the Migration")

After 100% of the traffic is directed to the new cluster and it has been running stably for a sufficient period (e.g., 24-48 hours), the migration is considered complete.

At this point, you can decommission the old cluster (Cluster A). It is recommended to keep the old cluster on standby for a few days as a final safety measure before shutting it down permanently.

## Important Considerations[â](#important-considerations "Direct link to Important Considerations")

Migrating a production cluster requires careful planning and attention to detail. Below are some critical considerations to keep in mind throughout the process.

### mTLS Certificate Mismatch[â](#mtls-certificate-mismatch "Direct link to mTLS Certificate Mismatch")

A common failure point in cluster migration is when a new Data Plane (DP) attempts to connect to the old Control Plane (CP). Each API7 Enterprise cluster uses a unique set of mTLS certificates for secure communication between the CP and DP. If a DP from Cluster B tries to connect to the CP from Cluster A, the connection will be rejected due to a certificate mismatch, and the DP will fail to start.

To avoid this, always ensure that the DP's configuration file (config.yaml) points to the correct CP address within its own cluster. If you are using a domain name to access the Control Plane, make sure to update your DNS configuration so that the new Data Plane resolves to the new Control Plane's address.

### Data Consistency[â](#data-consistency "Direct link to Data Consistency")

Enforcing a configuration freeze is essential for maintaining data consistency. If a configuration change is made on the old cluster after the database backup is taken, that change will not be present in the new cluster. If an emergency change is unavoidable, it must be manually applied to both clusters to prevent inconsistencies.

### Stateful Plugins[â](#stateful-plugins "Direct link to Stateful Plugins")

Plugins that rely on an external state store, such as the `rate-limiting` plugin that uses Redis, require special attention. If each cluster uses a separate Redis instance, the state (e.g., rate-limiting counters) will not be synchronized. During the traffic shifting phase, this can lead to temporary inaccuracies, such as a user being able to make more requests than the configured limit.

To mitigate this, you can either use a shared Redis instance for both clusters or accept the temporary inconsistencies during the migration period.

### Rollback Plan[â](#rollback-plan "Direct link to Rollback Plan")

A key advantage of the dual-cluster migration strategy is the ability to roll back instantly. If you encounter any issues with the new cluster during the traffic shifting phase, you can immediately redirect all traffic back to the old cluster through the load balancer. Keep the old cluster running until you are fully confident in the stability and performance of the new cluster.

## Best Practices[â](#best-practices "Direct link to Best Practices")

Following these best practices will help ensure a smooth and successful cluster migration.

**Rehearse in a Non-Production Environment**: Before migrating your production cluster, perform a complete dry run in a staging or testing environment. This rehearsal allows you to validate the migration process, identify potential issues, and refine your procedures without impacting live traffic.

**Schedule During Off-Peak Hours**: Plan the migration during a period of low business activity to minimize the impact on users. Even though the migration is designed to be zero-downtime, performing it during off-peak hours provides an additional safety margin.

**Prepare a Detailed Rollback Plan**: Document a clear and actionable rollback plan that can be executed quickly if issues arise. This plan should include the exact steps to redirect all traffic back to the old cluster and the criteria for triggering a rollback.

**Maintain Communication**: Keep all relevant teams informed throughout the migration process, including development, operations, and business stakeholders. Establish a communication channel for real-time updates and issue escalation.

**Document the Process**: Record all actions taken during the migration, including configuration changes, traffic percentages, and any anomalies observed. This documentation will be valuable for post-migration analysis and for future migrations.

**Monitor Continuously**: Use comprehensive monitoring and alerting tools to track the health and performance of both clusters during the migration. Key metrics to monitor include request latency, error rates, throughput, CPU usage, memory consumption, and database connection status.
