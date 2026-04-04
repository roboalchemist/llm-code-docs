# Source: https://docs.aws.amazon.com/elemental-server/latest/migrationguide/llms.txt

# AWS Elemental Server Migration Guide

> Learn how to upgrade the AWS Elemental Server software on an appliance.

- [About this guide](https://docs.aws.amazon.com/elemental-server/latest/migrationguide/migration-guide-about.html)
- [Document history](https://docs.aws.amazon.com/elemental-server/latest/migrationguide/doc-history.html)

## [Migrating to version 2.18](https://docs.aws.amazon.com/elemental-server/latest/migrationguide/migrate-server-218.html)

- [Get ready](https://docs.aws.amazon.com/elemental-server/latest/migrationguide/migrate-server-218-get-ready.html)
- [Prepare the node](https://docs.aws.amazon.com/elemental-server/latest/migrationguide/migrate-server-218-prepare-node.html)
- [Stop running jobs](https://docs.aws.amazon.com/elemental-server/latest/migrationguide/migrate-server-218-stop-jobs.html): Stop, or complete, all the running jobs on the node.
- [Create a backup](https://docs.aws.amazon.com/elemental-server/latest/migrationguide/migrate-server-218-backup.html): You must create a backup of the data on the node.

### [Switch boot mode](https://docs.aws.amazon.com/elemental-server/latest/migrationguide/migrate-server-218-boot-mode-uefi.html)

RHEL 9 requires that the boot mode for the appliance is UEFI.

- [Switch to UEFI on a Dell](https://docs.aws.amazon.com/elemental-server/latest/migrationguide/migrate-server-218-boot-mode-uefi-dell.html): There are three ways to switch the boot mode from Legacy mode to UEFI.
- [Switch to UEFI on a SuperMicro](https://docs.aws.amazon.com/elemental-server/latest/migrationguide/migrate-server-218-boot-mode-uefi-smc.html): To switch the boot mode from BIOS (Legacy mode) to UEFI, you can use the IPMI interface, or you can work when directly connected to the server.

### [Install RHEL 9](https://docs.aws.amazon.com/elemental-server/latest/migrationguide/migrate-server-218-rhel9.html)

Topics

- [Install on a Dell](https://docs.aws.amazon.com/elemental-server/latest/migrationguide/migrate-server-218-rhel9-dell.html): You can install RHEL 9 on a Dell chassis either from the iDRAC interface or using a USB stick.
- [Install on an SMC](https://docs.aws.amazon.com/elemental-server/latest/migrationguide/migrate-server-218-rhel9-smc.html): You install RHEL 9 on an SMC chassis from the IPMI interface.
- [Install the worker software](https://docs.aws.amazon.com/elemental-server/latest/migrationguide/migrate-server-218-install-software.html): This install procedure isn't the same as the install procedure on a newly obtained appliance (as described in AWS Elemental Server Installation Guide).
- [Restore the database](https://docs.aws.amazon.com/elemental-server/latest/migrationguide/migrate-server-218-install-restore.html): You restore data using the same lifeboat script that you used to create the backup.
