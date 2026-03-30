# Source: https://docs.api7.ai/enterprise/upgrade-guides/in-place.md

# Source: https://docs.api7.ai/enterprise/3.8.x/upgrade-guides/in-place.md

# In-Place Upgrade

You can use the in-place upgrade strategy to upgrade the **Control Plane (CP)**.

The in-place upgrade strategy reuses the existing database. During the upgrade process, modifications to your configuration through API or continued CP operations are **prohibited**.

Therefore, this upgrade method will result in some downtime for the CP, as shown in the diagram below:

<!-- -->

## Preparation[â](#preparation "Direct link to Preparation")

1. Read the [upgrade guide](https://docs.api7.ai/enterprise/3.8.x/upgrade-guides/upgrade.md) and ensure you understand how the entire upgrade process is executed.
2. Note the downtime during this upgrade process and confirm an appropriate upgrade timing.
3. [Backup](https://docs.api7.ai/enterprise/3.8.x/upgrade-guides/backup-and-restore.md) your data.

## In-Place Upgrade Steps[â](#in-place-upgrade-steps "Direct link to In-Place Upgrade Steps")

info

The implementation steps below are for reference only. The actual execution may vary depending on your deployment environment.

1. During the upgrade process, modifications to your data through API or other methods are prohibited.

2. Back up your current data, refer to the [backup guide](https://docs.api7.ai/enterprise/3.8.x/upgrade-guides/backup-and-restore.md#database-backup).

3. Read the [upgrade considerations](https://docs.api7.ai/enterprise/3.8.x/upgrade-guides/upgrade.md#upgrade-considerations).

4. Check all changes between the current version and the target upgrade version.

   <!-- -->

   * [Complete changelog](https://docs.api7.ai/enterprise/release-notesx)
   * [Breaking changes](https://docs.api7.ai/enterprise/3.8.x/upgrade-guides/breaking-changes.md)

5. Based on your API7 Enterprise installation method ([Docker](https://docs.api7.ai/enterprise/3.8.x/deployment/docker.md), [Kubernetes](https://docs.api7.ai/enterprise/3.8.x/deployment/openshift.md)), modify the image versions of `api7-ee-dashboard` and `api7-ee-dp-manager` in the corresponding configuration files (`docker-compose`, `helm chart`).

6. Restart the CP using the modified configuration files.

7. Access the Dashboard to check if it is running properly.

8. If you encounter any issues, please refer to [Rollback Upgrade](https://docs.api7.ai/enterprise/3.8.x/upgrade-guides/backup-and-restore.md#data-restore-and-rollback).

9. After observing for a period of time with no additional issues, the CP upgrade is complete.

## Next Steps[â](#next-steps "Direct link to Next Steps")

After completing the CP upgrade, you can begin preparing to [upgrade the DP](https://docs.api7.ai/enterprise/3.8.x/upgrade-guides/rolling-upgrade.md).
