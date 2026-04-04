# Source: https://docs.api7.ai/enterprise/upgrade-guides/rolling-upgrade.md

# Source: https://docs.api7.ai/enterprise/3.8.x/upgrade-guides/rolling-upgrade.md

# Rolling Upgrade

The nodes in the **Data Plane (DP)** will be upgraded using the rolling upgrade method.

Rolling upgrade means continuously adding new version DP nodes while shutting down old version DP nodes, allowing uninterrupted processing of API requests during the process.

<!-- -->

## Preparation[â](#preparation "Direct link to Preparation")

1. Read the [upgrade guide](https://docs.api7.ai/enterprise/3.8.x/upgrade-guides/upgrade.md) and ensure you understand how the entire upgrade process is executed.
2. [Control Plane (CP) upgrade](https://docs.api7.ai/enterprise/3.8.x/upgrade-guides/in-place.md) is completed.

## Rolling Upgrade Steps[â](#rolling-upgrade-steps "Direct link to Rolling Upgrade Steps")

info

The steps below are for reference only. The actual steps may vary depending on your deployment environment.

1. During the upgrade process, modifications to your data through API or other methods are prohibited.

2. Back up your current data, refer to the [backup guide](https://docs.api7.ai/enterprise/3.8.x/upgrade-guides/backup-and-restore.md#database-backup).

3. Read the [upgrade considerations](https://docs.api7.ai/enterprise/3.8.x/upgrade-guides/upgrade.md#upgrade-considerations).

4. Check all changes between the current version and the target upgrade version.

   <!-- -->

   * [Complete changelog](https://docs.api7.ai/enterprise/release-notesx)
   * [Breaking changes](https://docs.api7.ai/enterprise/3.8.x/upgrade-guides/breaking-changes.md)

5. Based on your gateway instance installation method ([Docker](https://docs.api7.ai/enterprise/3.8.x/getting-started/add-gateway-instance.md), [Kubernetes](https://docs.api7.ai/enterprise/3.8.x/getting-started/add-gateway-instance.md)), modify the image versions of `api7-ee-3-gateway` in the corresponding configuration files (`docker-compose`, `helm chart`).
   <!-- -->
   * If the version update record includes changes to other configurations, please check the changelog description to confirm if other configurations need to be updated accordingly.

6. Restart the gateway instances using the modified configuration files.

   <!-- -->

   * After updating the instances in one gateway group, you can perform some tests on this gateway group to ensure normal operation. If the results are not as expected, please review the [changelog](https://docs.api7.ai/enterprise/release-notesx) again to confirm if anything was missed.
   * Continue updating and replacing the gateway instances in your other gateway groups.

7. Actively monitor all proxy metrics and send some test requests to verify normal operation after the upgrade.

8. If you encounter any issues, please refer to [Rollback Upgrade](https://docs.api7.ai/enterprise/3.8.x/upgrade-guides/backup-and-restore.md#restore-from-database).

9. After observing for a period of time with no additional issues, DP upgrade is complete.

You can now continue using API, Dashboard, and ADC to update and modify your configurations.
