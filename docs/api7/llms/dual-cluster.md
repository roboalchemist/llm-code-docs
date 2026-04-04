# Source: https://docs.api7.ai/enterprise/upgrade-guides/dual-cluster.md

# Dual-Cluster Upgrade

You can use the dual-cluster upgrade strategy to upgrade the **API7 Enterprise Cluster**.

The dual-cluster upgrade strategy deploys a completely new, parallel cluster (Cluster Y) alongside your existing production cluster (Cluster X). Each cluster is entirely independent, with its own Control Plane, Data Plane, and Database. During the upgrade process, modifications to your configuration through API or continued CP operations are **prohibited**.

Traffic is gradually shifted from the old cluster to the new one using an external load balancer. This upgrade method provides zero downtime and allows for instant rollback, as shown in the diagram below:

<!-- -->

## Preparation[â](#preparation "Direct link to Preparation")

1. Read the [upgrade guide](https://docs.api7.ai/enterprise/upgrade-guides/upgrade.md) and ensure you understand how the entire upgrade process is executed.

2. Ensure you have sufficient resources to run two complete production clusters in parallel.

3. [Backup](https://docs.api7.ai/enterprise/upgrade-guides/backup-and-restore.md) your current data from Cluster X (Database X).

4. Review the [upgrade considerations](https://docs.api7.ai/enterprise/upgrade-guides/upgrade.md#upgrade-considerations).

5. Check all changes between the current version and the target upgrade version.

   <!-- -->

   * [Complete changelog](https://docs.api7.ai/enterprise/release-notesx)
   * [Breaking changes](https://docs.api7.ai/enterprise/upgrade-guides/breaking-changes.md)

6. Prepare your external load balancer configuration for traffic shifting.

7. Plan the traffic shifting schedule and monitoring strategy.

## Dual-Cluster Upgrade Steps[â](#dual-cluster-upgrade-steps "Direct link to Dual-Cluster Upgrade Steps")

info

The implementation steps below are for reference only. The actual execution may vary depending on your deployment environment.

### Step 1: Freeze Configuration Changes[â](#step-1-freeze-configuration-changes "Direct link to Step 1: Freeze Configuration Changes")

Announce a maintenance window for configuration changes. During the entire upgrade process, **do not make any changes** to your API configurations on the old cluster (Cluster X). This is critical to prevent inconsistencies between the two clusters.

* Stop all configuration modifications through API or Dashboard UI on Cluster X.
* Document the current state of all configurations for reference.

### Step 2: Deploy New Cluster (Cluster Y)[â](#step-2-deploy-new-cluster-cluster-y "Direct link to Step 2: Deploy New Cluster (Cluster Y)")

1. **Provision New Database (Database Y)**:

   * Set up a new database instance for Cluster Y.
   * Ensure it has sufficient capacity and performance characteristics similar to Database X.

2. **Backup and Restore Database**:

   * Perform a full backup of Database X using `pg_dump` or your preferred backup method.
   * Restore the backup to Database Y using `pg_restore` or your preferred restore method.

3. **Deploy New Version of API7 Enterprise**:

   * Based on your API7 Enterprise installation method ([Docker](https://docs.api7.ai/enterprise/deployment/docker.md), [Kubernetes](https://docs.api7.ai/enterprise/deployment/gateway-openshift.md)), deploy a new API7 Enterprise cluster with the target version.

   * Configure the Control Plane (CP B) to connect to Database Y.

   * Deploy the Data Plane (DP B) nodes and configure them to connect to CP B.

   * Update image versions in your configuration files:

     <!-- -->

     * `api7-ee-dashboard` (for CP)
     * `api7-ee-dp-manager` (for CP)
     * `api7-ee-gateway` (for DP)

4. **Start and Verify Cluster Y**:

   * Start Cluster Y and ensure all components are running properly.
   * Access the Dashboard of CP B to verify it is operational.
   * Conduct thorough functional and performance tests in isolation to ensure Cluster Y is working correctly.
   * Verify that all configurations from Database X are correctly loaded in Cluster Y.

### Step 3: Begin Traffic Shifting[â](#step-3-begin-traffic-shifting "Direct link to Step 3: Begin Traffic Shifting")

1. **Configure Load Balancer**:

   * Configure your external load balancer to send a small percentage of production traffic (e.g., 1-10%) to the new Data Plane (DP B).
   * Keep the majority of traffic (90-99%) on the old Data Plane (DP A).

2. **Monitor Cluster Y**:

   * Closely monitor the performance, error rates, and logs of Cluster Y.
   * Compare its behavior against Cluster X.

### Step 4: Gradually Increase Traffic[â](#step-4-gradually-increase-traffic "Direct link to Step 4: Gradually Increase Traffic")

If Cluster Y remains stable and performs as expected, incrementally increase the percentage of traffic it receives:

1. **Increase to 25%**: Shift 25% of traffic to DP B, monitor for a period (e.g., 1-2 hours).
2. **Increase to 50%**: Shift 50% of traffic to DP B, monitor for a period (e.g., 1-2 hours).
3. **Increase to 75%**: Shift 75% of traffic to DP B, monitor for a period (e.g., 2-4 hours).

At each stage:

* Continue to monitor key metrics for a sufficient observation period.
* Compare error rates and logs between Cluster X and Cluster Y.
* Watch for any anomalies or issues.

### Step 5: Complete Traffic Migration[â](#step-5-complete-traffic-migration "Direct link to Step 5: Complete Traffic Migration")

1. **Shift 100% Traffic**:

   * Once you are confident in the stability and performance of Cluster Y, direct 100% of the traffic to it.
   * All API requests should now be handled by DP B.

2. **Keep Cluster X as Hot Standby**:

   * Keep Cluster X running for a designated period (e.g., 24-48 hours) as a hot standby.
   * This allows for immediate rollback if any issues arise.

3. **Extended Observation**:

   * Monitor Cluster Y closely during this period.
   * Verify all functionality is working as expected.

### Step 6: Rollback (If Needed)[â](#step-6-rollback-if-needed "Direct link to Step 6: Rollback (If Needed)")

If you encounter any critical issues during the upgrade process:

1. **Immediate Rollback**:

   * Redirect all traffic back to Cluster X (DP A) through your load balancer.
   * Since Cluster X remains untouched, rollback is instant and requires no data restoration.

2. **Investigate Issues**:

   * Investigate the issues encountered in Cluster Y.
   * Fix any problems before attempting the upgrade again.

### Step 7: Decommission Old Cluster[â](#step-7-decommission-old-cluster "Direct link to Step 7: Decommission Old Cluster")

After the observation period passes without issues:

1. **Final Verification**:

   * Perform a final verification that Cluster Y is operating correctly.
   * Ensure all monitoring and alerting systems are properly configured for Cluster Y.

2. **Decommission Cluster X**:

   * Safely decommission Cluster X and its database (Database X) to release the resources.

## Special Considerations[â](#special-considerations "Direct link to Special Considerations")

### Resource Requirements[â](#resource-requirements "Direct link to Resource Requirements")

This strategy is the most resource-intensive, as it requires running two full production environments in parallel. Ensure you have:

* Sufficient compute resources for both clusters
* Adequate network capacity
* Storage for two separate databases

### Stateful Plugins[â](#stateful-plugins "Direct link to Stateful Plugins")

Runtime metrics and the state of stateful plugins (like rate-limiting) are not synchronized between the two clusters. Stateful plugins such as rate-limiting store their counter data in Redis, not in the database.

**Considerations**:

* If each cluster uses a separate Redis instance, this can lead to temporary inconsistencies during the traffic shifting phase.
* For example, a user might be able to make more requests than the configured limit because their requests are split between two separate rate-limiting counters in different Redis instances.

**Mitigation Strategies**:

* Consider using a shared Redis cluster for both API7 Enterprise clusters to maintain consistent state.
* Alternatively, accept temporary rate limit inaccuracies during the transition period.
* Plan the traffic shifting schedule to minimize the impact of these inconsistencies.

### Configuration Freeze[â](#configuration-freeze "Direct link to Configuration Freeze")

It is critical to enforce a strict configuration freeze during the entire process to prevent inconsistencies between the two clusters. Any configuration changes made during the upgrade process could lead to:

* Data inconsistencies between clusters
* Unexpected behavior during traffic shifting
* Difficulties in rollback scenarios

### Zero Downtime[â](#zero-downtime "Direct link to Zero Downtime")

The dual-cluster upgrade strategy provides true zero downtime. API requests continue to be served throughout the entire upgrade process, with traffic gradually shifting from the old cluster to the new one.
