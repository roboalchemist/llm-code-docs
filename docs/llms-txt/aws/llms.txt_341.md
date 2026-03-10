# Source: https://docs.aws.amazon.com/elemental-cf2/latest/migrationguide/llms.txt

# AWS Elemental Conductor File Migration Guide

> Learn how to upgrade the AWS Elemental Conductor File software on an appliance.

- [About this guide](https://docs.aws.amazon.com/elemental-cf2/latest/migrationguide/migration-guide-about.html)
- [Document history](https://docs.aws.amazon.com/elemental-cf2/latest/migrationguide/doc-history.html)

## [Standard cluster migration](https://docs.aws.amazon.com/elemental-cf2/latest/migrationguide/migrate-cf-std.html)

- [Plan maintenance windows](https://docs.aws.amazon.com/elemental-cf2/latest/migrationguide/migrate-std-plan-maintenance.html): You should plan to perform the cluster migration in several phases:
- [Step A: Get ready](https://docs.aws.amazon.com/elemental-cf2/latest/migrationguide/migrate-std-get-ready.html)
- [Step B: Prepare each node](https://docs.aws.amazon.com/elemental-cf2/latest/migrationguide/migrate-std-prepare-node.html): Prepare the nodes during one or more maintenance windows.
- [Step C: Tear down an AWS Elemental Conductor File cluster](https://docs.aws.amazon.com/elemental-cf2/latest/migrationguide/migrate-std-decluster.html): Before you can install RHEL 9 and the new software version, you must remove all the nodes from the cluster.
- [Step D: Create backups](https://docs.aws.amazon.com/elemental-cf2/latest/migrationguide/migrate-std-backup.html): Create a backup of the data on every node â the primary Conductor node, the secondary Conductor node, and all the workers.
- [Step E: Upgrade nodes](https://docs.aws.amazon.com/elemental-cf2/latest/migrationguide/migrate-server-218-install-software-cf.html): Perform these steps on each node in the cluster, after you've removed all the nodes from the cluster.
- [Step F: Rebuild the cluster](https://docs.aws.amazon.com/elemental-cf2/latest/migrationguide/migrate-std-rebuild-cluster.html)


## [Tasks](https://docs.aws.amazon.com/elemental-cf2/latest/migrationguide/migration-topics.html)

### [Boot mode â UEFI](https://docs.aws.amazon.com/elemental-cf2/latest/migrationguide/migrate-topic-uefi.html)

RHEL 9 requires that the boot mode for the appliance is UEFI.

- [Switching to UEFI on a Dell](https://docs.aws.amazon.com/elemental-cf2/latest/migrationguide/migrate-topic-uefi-dell.html): There are three ways to switch the boot mode from Legacy mode to UEFI.
- [Switching to UEFI on a SuperMicro](https://docs.aws.amazon.com/elemental-cf2/latest/migrationguide/migrate-topic-uefi-supermicro.html): To switch the boot mode from BIOS (Legacy mode) to UEFI, you can use the IPMI interface, or you can work when directly connected to the server.

### [Boot mode â Legacy](https://docs.aws.amazon.com/elemental-cf2/latest/migrationguide/migrate-topic-bios.html)

RHEL 7 and CentOS 7 require that the boot mode for the appliance is BIOS.

- [Switching to Legacy on a Dell](https://docs.aws.amazon.com/elemental-cf2/latest/migrationguide/migrate-topic-bios-dell.html): There are three ways to switch the boot mode from UEFI back to BIOS (Legacy mode).
- [Switching to Legacy on a SuperMicro](https://docs.aws.amazon.com/elemental-cf2/latest/migrationguide/migrate-topic-bios-supermicro.html): To switch the boot mode from UEFI back to BIOS (Legacy mode), you can use the IPMI interface, or you can work when directly connected to the server.
- [Boot USB drive â create](https://docs.aws.amazon.com/elemental-cf2/latest/migrationguide/migrate-topic-create-boot.html)
- [Cluster â enable HA or disable HA](https://docs.aws.amazon.com/elemental-cf2/latest/migrationguide/migrate-topic-disable-ha.html): Disable high availability prior to performing any changes on the Conductor nodes.
- [Database â back up](https://docs.aws.amazon.com/elemental-cf2/latest/migrationguide/migrate-topic-lifeboat.html): You back up data using the special lifeboat script.
- [Database â restore](https://docs.aws.amazon.com/elemental-cf2/latest/migrationguide/migrate-topic-restore-database.html): You restore data using the same lifeboat script that you used to create the backup.
- [Conductor File â install](https://docs.aws.amazon.com/elemental-cf2/latest/migrationguide/migrate-topic-install-cl3.html)
- [AWS Elemental Server â install](https://docs.aws.amazon.com/elemental-cf2/latest/migrationguide/migrate-topic-install-worker.html): This install procedure isn't the same as the install procedure on a newly obtained appliance.
- [Firmware â update](https://docs.aws.amazon.com/elemental-cf2/latest/migrationguide/migrate-topic-firmware.html)

### [RHEL 9 â install](https://docs.aws.amazon.com/elemental-cf2/latest/migrationguide/migrate-topic-install-rhel.html)

This section provides instructions to install RHEL 9 on a Dell chassis and on an SuperMicro chassis.

- [Installing on a Dell](https://docs.aws.amazon.com/elemental-cf2/latest/migrationguide/migrate-topic-install-rhel-dell.html): You can install RHEL 9 on a Dell chassis either from the iDRAC interface or using a USB stick.
- [Installing on an SuperMicro](https://docs.aws.amazon.com/elemental-cf2/latest/migrationguide/migrate-topic-install-rhel-smc.html): You install RHEL 9 on a SuperMicro chassis from the IPMI interface.
- [RPM repository](https://docs.aws.amazon.com/elemental-cf2/latest/migrationguide/migrate-topic-rpm-repository.html): AWS Elemental maintains an RPM repository for use with RHEL 9.
