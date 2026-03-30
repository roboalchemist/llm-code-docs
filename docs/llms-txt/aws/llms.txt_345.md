# Source: https://docs.aws.amazon.com/elemental-cl3/latest/migrationguide/llms.txt

# AWS Elemental Conductor Live Migration Guide

> Learn how to upgrade the AWS Elemental Conductor Live software on an appliance.

- [About this guide](https://docs.aws.amazon.com/elemental-cl3/latest/migrationguide/migration-guide-about.html)
- [Important notes](https://docs.aws.amazon.com/elemental-cl3/latest/migrationguide/migration-notes.html)
- [Document history](https://docs.aws.amazon.com/elemental-cl3/latest/migrationguide/doc-history.html)

## [Standard cluster migration](https://docs.aws.amazon.com/elemental-cl3/latest/migrationguide/migrate-cl-std.html)

- [Plan maintenance windows](https://docs.aws.amazon.com/elemental-cl3/latest/migrationguide/migrate-std-plan-maintenance.html): You should plan to perform the cluster migration in several phases:
- [Step A: Get ready](https://docs.aws.amazon.com/elemental-cl3/latest/migrationguide/migrate-std-get-ready.html)
- [Step B: Prepare each node](https://docs.aws.amazon.com/elemental-cl3/latest/migrationguide/migrate-std-prepare-node.html): Prepare the nodes during one or more maintenance windows.
- [Step C: Tear down the cluster](https://docs.aws.amazon.com/elemental-cl3/latest/migrationguide/migrate-std-decluster.html): Before you can install RHEL 9 and the new software version, you must remove all the nodes from the cluster.
- [Step D: Create backups](https://docs.aws.amazon.com/elemental-cl3/latest/migrationguide/migrate-std-backup.html): Create a backup of the data on every node â the primary Conductor node, the secondary Conductor node, and all the workers.
- [Step E: Upgrade nodes](https://docs.aws.amazon.com/elemental-cl3/latest/migrationguide/migrate-std-upgrade-nodes.html)
- [Step F: Rebuild the cluster](https://docs.aws.amazon.com/elemental-cl3/latest/migrationguide/migrate-std-rebuild-cluster.html)


## [Split cluster migration](https://docs.aws.amazon.com/elemental-cl3/latest/migrationguide/migrate-cl-split-cluster.html)

- [Plan maintenance windows](https://docs.aws.amazon.com/elemental-cl3/latest/migrationguide/migrate-split-c-plan-maintenance.html): You should plan to perform the cluster migration in several phases.
- [Step A: Get ready](https://docs.aws.amazon.com/elemental-cl3/latest/migrationguide/migrate-split-c-get-ready.html)
- [Step B: Prepare each node](https://docs.aws.amazon.com/elemental-cl3/latest/migrationguide/migrate-split-c-prepare-node.html): Prepare the nodes during one or more maintenance windows.
- [Step C: Split the cluster](https://docs.aws.amazon.com/elemental-cl3/latest/migrationguide/migrate-split-c-split.html)
- [Step D: Upgrade node X](https://docs.aws.amazon.com/elemental-cl3/latest/migrationguide/migrate-split-c-upgrade-primary.html): Now that node X is not controlling the cluster, you can upgrade it.
- [Step E: Upgrade the worker nodes](https://docs.aws.amazon.com/elemental-cl3/latest/migrationguide/migrate-split-c-upgrade-w-nodes.html): You must now remove each worker from the original cluster (that is controlled by node Y), upgrade it, and add it to the new cluster (that is controlled by node X).
- [Step F: Upgrade node Y](https://docs.aws.amazon.com/elemental-cl3/latest/migrationguide/migrate-split-c-upgrade-secondary.html): After you remove the last worker node, the original cluster no longer exists.
- [Step G: Add node Y to cluster](https://docs.aws.amazon.com/elemental-cl3/latest/migrationguide/migrate-split-c-add-secondary.html)


## [Tasks](https://docs.aws.amazon.com/elemental-cl3/latest/migrationguide/migration-topics.html)

### [Boot mode â UEFI](https://docs.aws.amazon.com/elemental-cl3/latest/migrationguide/migrate-topic-uefi.html)

RHEL 9 requires that the boot mode for the appliance is UEFI.

- [Switching to UEFI on a Dell](https://docs.aws.amazon.com/elemental-cl3/latest/migrationguide/migrate-topic-uefi-dell.html): There are three ways to switch the boot mode from Legacy mode to UEFI.
- [Switching to UEFI on a SuperMicro](https://docs.aws.amazon.com/elemental-cl3/latest/migrationguide/migrate-topic-uefi-supermicro.html): To switch the boot mode from BIOS (Legacy mode) to UEFI, you can use the IPMI interface, or you can work when directly connected to the server.

### [Boot mode â Legacy](https://docs.aws.amazon.com/elemental-cl3/latest/migrationguide/migrate-topic-bios.html)

RHEL 7 and CentOS 7 require that the boot mode for the appliance is BIOS.

- [Switching to Legacy on a Dell](https://docs.aws.amazon.com/elemental-cl3/latest/migrationguide/migrate-topic-bios-dell.html): There are three ways to switch the boot mode from UEFI back to BIOS (Legacy mode).
- [Switching to Legacy on a SuperMicro](https://docs.aws.amazon.com/elemental-cl3/latest/migrationguide/migrate-topic-bios-supermicro.html): To switch the boot mode from UEFI back to BIOS (Legacy mode), you can use the IPMI interface, or you can work when directly connected to the server.
- [Boot USB drive â create](https://docs.aws.amazon.com/elemental-cl3/latest/migrationguide/migrate-topic-create-boot.html): Only Dell servers support the ability to install RHEL 9 from a boot USB drive.
- [Cluster â add Conductor](https://docs.aws.amazon.com/elemental-cl3/latest/migrationguide/migrate-topic-add-conductor.html): Add the secondary node back to the cluster, and then to the redundancy group.
- [Cluster â add worker node](https://docs.aws.amazon.com/elemental-cl3/latest/migrationguide/migrate-topic-add-w.html)
- [Cluster â enable HA or disable HA](https://docs.aws.amazon.com/elemental-cl3/latest/migrationguide/migrate-topic-disable-ha.html): To enable or disable HA in a cluster, follow these steps.
- [Cluster â enable user authentication](https://docs.aws.amazon.com/elemental-cl3/latest/migrationguide/migrate-topic-user-auth.html): This section applies only if you had previously enabled user authentication on the cluster.
- [Cluster â remove Conductor node](https://docs.aws.amazon.com/elemental-cl3/latest/migrationguide/migrate-topic-remove-c-node.html): You can remove a Conductor node that is not acting as the primary Conductor node â that isn't controlling the cluster.
- [Cluster â remove worker node](https://docs.aws.amazon.com/elemental-cl3/latest/migrationguide/migrate-topic-remove-worker.html): To remove a worker node from the cluster, first you remove channel assignments from the node.
- [Cluster â restart channels](https://docs.aws.amazon.com/elemental-cl3/latest/migrationguide/migrate-topic-channel-start.html): To restart one channel
- [Database â back up](https://docs.aws.amazon.com/elemental-cl3/latest/migrationguide/migrate-topic-lifeboat.html): You back up data using the special lifeboat script.
- [Database â restore](https://docs.aws.amazon.com/elemental-cl3/latest/migrationguide/migrate-topic-restore-database.html): You restore data using the same lifeboat script that you used to create the backup.
- [Conductor Live â install](https://docs.aws.amazon.com/elemental-cl3/latest/migrationguide/migrate-topic-install-cl3.html)
- [Elemental Live â install](https://docs.aws.amazon.com/elemental-cl3/latest/migrationguide/migrate-topic-install-worker.html): This install procedure isn't the same as the install procedure on a newly obtained appliance (as described in AWS Elemental Live Installation Guide).
- [Firmware â update](https://docs.aws.amazon.com/elemental-cl3/latest/migrationguide/migrate-topic-firmware.html)

### [RHEL 9 â install](https://docs.aws.amazon.com/elemental-cl3/latest/migrationguide/migrate-topic-install-rhel.html)

This section provides instructions to install RHEL 9 on a Dell chassis and on an SuperMicro chassis.

- [Installing on a Dell](https://docs.aws.amazon.com/elemental-cl3/latest/migrationguide/migrate-topic-install-rhel-dell.html): You can install RHEL 9 on a Dell chassis either from the iDRAC interface or using a USB stick.
- [Installing on a SuperMicro](https://docs.aws.amazon.com/elemental-cl3/latest/migrationguide/migrate-topic-install-rhel-smc.html): You install RHEL 9 on a SuperMicro chassis from the IPMI interface.
- [RPM repository](https://docs.aws.amazon.com/elemental-cl3/latest/migrationguide/migrate-topic-rpm-repository.html): AWS Elemental maintains an RPM repository for use with RHEL 9.
