# Source: https://docs.infrahub.app/backup/guides/backup-instance.md

# How to backup your Infrahub instance

This guide walks you through creating a comprehensive backup of your Infrahub instance. If you need to protect your data, prepare for upgrades, or establish disaster recovery procedures, follow these steps to create reliable backups.

## Community edition support[​](#community-edition-support "Direct link to Community edition support")

Infrahub Community Edition deployments are fully supported by `infrahub-backup`, but there are a few operational differences to plan for compared to Enterprise environments.

warning

Backing up Community Edition stops the Infrahub application container while the snapshot is taken. Schedule the command during a maintenance window to avoid user-facing downtime.

Restoring a backup that was taken from an Enterprise cluster to a Community Edition instance is not supported. Create and maintain backups from the same edition you intend to restore to.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

Before creating a backup:

* Ensure infrahub-backup is installed and configured
* Verify you have sufficient disk space (at least 2x your database size)
* Have write permissions to the backup directory
* Confirm your Infrahub instance is accessible

## Step 1: Check for running tasks[​](#step-1-check-for-running-tasks "Direct link to Step 1: Check for running tasks")

Before initiating a backup, check if there are active tasks that might be interrupted by checking the Infrahub web interface or waiting for natural completion.

If tasks are running, you have two options:

* Wait for Completion
* Force Backup

Wait for tasks to complete naturally by monitoring the Infrahub UI, then proceed with backup:

```
infrahub-backup create
```

Force backup despite running tasks:

```
# Force backup (running tasks will be ignored)
infrahub-backup create --force
```

## Step 2: Create the backup[​](#step-2-create-the-backup "Direct link to Step 2: Create the backup")

Execute the backup command with your desired options:

### Basic backup[​](#basic-backup "Direct link to Basic backup")

For a standard backup with all components:

```
infrahub-backup create
```

### Selective metadata backup[​](#selective-metadata-backup "Direct link to Selective metadata backup")

Control which Neo4j metadata to include:

```
# Backup without metadata (smallest size)
infrahub-backup create --neo4jmetadata=none

# Backup with only user accounts
infrahub-backup create --neo4jmetadata=users

# Backup with only roles
infrahub-backup create --neo4jmetadata=roles

# Backup with everything (default)
infrahub-backup create --neo4jmetadata=all
```

### Custom backup location[​](#custom-backup-location "Direct link to Custom backup location")

Specify an alternative backup directory:

```
infrahub-backup create --backup-dir=/mnt/backups/infrahub
```

### Target specific project[​](#target-specific-project "Direct link to Target specific project")

If running multiple Infrahub instances:

```
infrahub-backup create --project=infrahub-production
```

## Step 3: Monitor backup progress[​](#step-3-monitor-backup-progress "Direct link to Step 3: Monitor backup progress")

The backup process provides detailed progress information:

```
INFO[0000] Starting backup process...
INFO[0000] Checking for running tasks...
INFO[0001] No running tasks found
INFO[0001] Creating backup ID: 20250929_143022
INFO[0002] Stopping Infrahub application containers...
INFO[0005] Application containers stopped
INFO[0005] Backing up Neo4j database...
INFO[0015] Neo4j backup completed (1.2GB)
INFO[0015] Backing up PostgreSQL database...
INFO[0018] PostgreSQL backup completed (256MB)
INFO[0020] Creating compressed archive...
INFO[0025] Archive created: infrahub_backup_20250929_143022.tar.gz
INFO[0025] Starting application containers...
INFO[0030] All containers started successfully
INFO[0030] Backup completed successfully
```

## Step 4: Verify backup integrity[​](#step-4-verify-backup-integrity "Direct link to Step 4: Verify backup integrity")

After backup completion, verify the backup file:

### Check backup file[​](#check-backup-file "Direct link to Check backup file")

```
# List backup files with sizes
ls -lh infrahub_backups/

# Verify archive integrity
tar -tzf infrahub_backups/infrahub_backup_20250929_143022.tar.gz > /dev/null && echo "Archive is valid"

# View backup metadata
tar -xzOf infrahub_backups/infrahub_backup_20250929_143022.tar.gz backup_information.json | jq '.'
```

### Validate backup contents[​](#validate-backup-contents "Direct link to Validate backup contents")

The backup should contain:

* `backup_information.json` - Backup information and checksums
* `database/` - Neo4j database files
* `prefect.dump` - PostgreSQL dump

Example metadata structure:

```
{
  "metadata_version": 2025092500,
  "backup_id": "20250929_143022",
  "created_at": "2025-09-29T14:30:22Z",
  "tool_version": "1.0.0",
  "infrahub_version": "0.15.0",
  "components": ["database", "task-manager-db"],
  "checksums": {
    "database": "sha256:abc123...",
    "prefect.dump": "sha256:def456..."
  },
  "redacted": false
}
```

## Step 5: Backup artifact storage[​](#step-5-backup-artifact-storage "Direct link to Step 5: Backup artifact storage")

Capture any artifact storage (object stores, shared volumes, artifact registries) that Infrahub references during task execution. Align the snapshot timing with the database backup so the two stay consistent.

* Identify the storage location configured for your task manager (bucket, container, or filesystem path).
* Copy or synchronize the artifacts into a dated folder or snapshot using the native tooling for your storage provider.
* Record the snapshot path or version ID alongside your database backup metadata so operators can retrieve the artifacts during a restore.

If your storage tier already offers automatic versioning or replication, confirm the retention window meets your recovery objectives and document how to retrieve the relevant versions during a disaster scenario.

## Step 6: Test restore capability[​](#step-6-test-restore-capability "Direct link to Step 6: Test restore capability")

Periodically test restoration to ensure backups are valid:

```
# Review what would be restored
infrahub-backup restore infrahub_backups/infrahub_backup_20250929_143022.tar.gz
```

## Advanced usage[​](#advanced-usage "Direct link to Advanced usage")

### Automated backups with cron[​](#automated-backups-with-cron "Direct link to Automated backups with cron")

You can either use a [systemd timer](/backup/guides/install.md#system-service-installation) or regular cron.

Create a cron job for regular backups:

```
# Edit crontab
crontab -e

# Add daily backup at 2 AM
0 2 * * * /usr/local/bin/infrahub-backup create >> /var/log/infrahub-backup.log 2>&1

# With retention management (keep 7 days)
0 2 * * * /usr/local/bin/infrahub-backup create && find /path/to/backups -name "*.tar.gz" -mtime +7 -delete
```

### Backup with notification[​](#backup-with-notification "Direct link to Backup with notification")

Create a wrapper script for notifications:

```
#!/bin/bash
BACKUP_RESULT=$(infrahub-backup create 2>&1)
if [ $? -eq 0 ]; then
    echo "Backup successful" | mail -s "Infrahub Backup Success" ops@example.com
else
    echo "$BACKUP_RESULT" | mail -s "Infrahub Backup Failed" ops@example.com
    exit 1
fi
```

### S3 backup storage[​](#s3-backup-storage "Direct link to S3 backup storage")

Upload backups directly to S3 or S3-compatible storage (like MinIO):

* AWS S3
* MinIO
* Environment Variables

```
# Upload to S3 (deletes local file by default)
infrahub-backup create --s3-upload --s3-bucket my-backups --s3-prefix infrahub/prod

# Upload to S3 but keep local copy
infrahub-backup create --s3-upload --s3-bucket my-backups --s3-keep-local
```

```
# Upload to MinIO or S3-compatible storage
infrahub-backup create --s3-upload \
  --s3-bucket my-backups \
  --s3-endpoint http://minio.local:9000 \
  --s3-region us-east-1
```

```
# Configure S3 via environment variables
export INFRAHUB_S3_BUCKET=my-backups
export INFRAHUB_S3_PREFIX=infrahub/prod
export AWS_ACCESS_KEY_ID=your-access-key
export AWS_SECRET_ACCESS_KEY=your-secret-key

infrahub-backup create --s3-upload
```

info

AWS credentials are loaded from the standard AWS credential chain: environment variables (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`), shared credentials file (`~/.aws/credentials`), or IAM roles when running on AWS infrastructure.

### Redacted backups[​](#redacted-backups "Direct link to Redacted backups")

If you need to share a backup for debugging or testing purposes without exposing sensitive data, use the `--redact` flag. This replaces all attribute values in the Neo4j database with random UUIDs before the backup is created.

danger

The `--redact` flag is a **destructive operation** that irreversibly modifies the live database. All attribute values will be replaced with random UUIDs. Only use this on a disposable copy of your instance, never on a production database you intend to keep using.

Because this operation is destructive, `--force` is required as confirmation:

```
infrahub-backup create --redact --force
```

The resulting backup archive is marked as redacted in its metadata (`"redacted": true`), so consumers can identify that the data has been anonymized.

A typical workflow for creating a redacted backup safely:

1. Create a normal backup of your production instance
2. Restore that backup to a temporary or staging instance
3. Run the redacted backup on the temporary instance
4. Share the redacted backup archive
5. Tear down the temporary instance

### Manual remote backup storage[​](#manual-remote-backup-storage "Direct link to Manual remote backup storage")

If you prefer manual transfers, you can copy backups after creation:

```
# Backup locally first
infrahub-backup create

# Transfer to remote storage
LATEST_BACKUP=$(ls -t infrahub_backups/*.tar.gz | head -1)

# S3 example (manual)
aws s3 cp "$LATEST_BACKUP" s3://my-bucket/infrahub-backups/

# SCP example
scp "$LATEST_BACKUP" backup-server:/backups/infrahub/

# Rsync example
rsync -avz "$LATEST_BACKUP" backup-server:/backups/infrahub/
```

## Validation[​](#validation "Direct link to Validation")

Confirm your backup strategy works:

* ✓ Backup completes without errors
* ✓ Archive passes integrity check
* ✓ Metadata contains expected components
* ✓ File size is reasonable for your data volume
* ✓ Test restore succeeds in non-production environment

## Related resources[​](#related-resources "Direct link to Related resources")

* [How to restore from backup](/backup/guides/restore-backup.md)
* [CLI command reference](/backup/reference/commands.md)
