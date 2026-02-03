# Source: https://www.aptible.com/docs/reference/aptible-cli/cli-commands/cli-backup-restore.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# aptible backup:restore

This command is used to [restore from a Database Backup](/core-concepts/managed-databases/managing-databases/database-backups#restoring-from-a-backup). This command creates a new database: it **does not overwrite your existing database.** In fact, it doesn't interact with your existing database at all. By default, all newly restored Databases are created as a 1GB [General Purpose Container Profile](/core-concepts/scaling/container-profiles#default-container-profile), however you can specify both container size and profile using the options.

You'll need the ID of an existing [Backup](/core-concepts/managed-databases/managing-databases/database-backups) to use this command. You can find those IDs using the [`aptible backup:list`](/reference/aptible-cli/cli-commands/cli-backup-list) command or through the Dashboard.

<Warning> Warning: If you are restoring a Backup of a GP3 volume, the new Database will be provisioned with the base [performance characteristics](/core-concepts/scaling/database-scaling#throughput-performance): 3,000 IOPs and 125MB/s throughput. If the original Database's performance was scaled up, you may need to modify the restored Database if you wish to retain the performance of the source Database. </Warning>

# Synopsis

```
Usage:
  aptible backup:restore BACKUP_ID [--environment ENVIRONMENT_HANDLE] [--handle HANDLE] [--container-size SIZE_MB] [--disk-size SIZE_GB] [--container-profile PROFILE] [--iops IOPS] [--key-arn KEY_ARN]

Options:
  [--handle=HANDLE]            # a name to use for the new database
  --env, [--environment=ENVIRONMENT]  # a different environment to restore to
  [--container-size=N]
  [--size=N]
  [--disk-size=N]
  [--key-arn=KEY_ARN]
  [--container-profile=PROFILE]
  [--iops=IOPS]
```

# Examples

## Restore a Backup

```shell  theme={null}
aptible backup:restore "$BACKUP_ID"
```

## Customize the new Database

You can also customize the new [Database](/core-concepts/managed-databases/overview) that will be created from the Backup:

```shell  theme={null}
aptible backup:restore "$BACKUP_ID" \
        --handle "$NEW_DATABASE_HANDLE" \
        --container-size "$CONTAINER_SIZE_MB" \
        --disk-size "$DISK_SIZE_GB"
```

If no handle is provided, it will default to `$DB_HANDLE-at-$BACKUP_DATE` where `$DB_HANDLE` is the handle of the Database the backup was taken from. Database handles must:

* Only contain lowercase alphanumeric characters,`.`, `_`, or `-`
* Be between 1 to 64 characters in length
* Be unique within their [Environment](/core-concepts/architecture/environments)

Therefore, there are two situations where the default handle can be invalid:

* The handle is longer than 64 characters. The default handle will be 23 characters longer than the original Database's handle.
* The default handle is not unique within the Environment. Most likely, this would be caused by restoring the same backup to the same Environment multiple times.

## Restore to a different Environment

You can restore Backups across [Environments](/core-concepts/architecture/environments) as long as they are hosted on the same type of [Stack](/core-concepts/architecture/stacks). You can only restore Backups from a [Dedicated Stack](/core-concepts/architecture/stacks#dedicated-stacks) in another Dedicated Stack and backups from a Shared Stack in another Shared Stack. Since Environments are globally unique, you do not need to specify the Stack in your command:

```shell  theme={null}
aptible backup:restore "$BACKUP_ID" \
        --environment "$ENVIRONMENT_HANDLE"
```

## Disk Resizing Note

When specifying a disk size, note that the restored database can only be resized up (i.e., you cannot shrink your Database Disk). If you need to scale a Database Disk down, you can either dump and restore to a smaller Database or create a replica and failover. Refer to our [Supported Databases](/core-concepts/managed-databases/supported-databases/overview) documentation to see if replication and failover is supported for your Database type.

#### Container Sizes (MB)

**General Purpose(M)**: 512, 1024, 2048, 4096, 7168, 15360, 30720, 61440, 153600, 245760
