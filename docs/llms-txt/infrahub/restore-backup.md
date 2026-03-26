# Source: https://docs.infrahub.app/backup/guides/restore-backup.md

# How to restore from backup

This guide shows you how to restore your Infrahub instance from a backup file. If you need to recover from data loss, roll back changes, or migrate to new infrastructure, follow these steps to safely restore your system.

## Community edition compatibility[​](#community-edition-compatibility "Direct link to Community edition compatibility")

Restores are supported for Infrahub Community Edition when the backup was created from the same edition. Enterprise backups include components that are not available in Community Edition and cannot be restored.

danger

Restoring an Enterprise backup to a Community Edition deployment is not supported. Always use backups that were captured from the same edition you plan to restore.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

Before restoring from backup:

* Have a valid backup file created by infrahub-backup
* Ensure sufficient disk space for extraction (3x backup size)
* Stop all write operations to the current instance
* Verify you have necessary permissions
* **Create a current backup** before overwriting existing data

danger

Restoration replaces all existing data. Always verify you have a current backup before proceeding with a restore operation.

## Docker high availability deployments[​](#docker-high-availability-deployments "Direct link to Docker high availability deployments")

If your Docker Compose deployment runs multiple task manager replicas (HA setup), you must stop the `task-manager` and `task-manager-background-svc` containers before running a restore. This prevents those services from accessing the database while data is being replaced.

```
# Stop task manager services before restore
docker compose stop task-manager task-manager-background-svc
```

After the restore completes, restart the stopped services:

```
# Restart task manager services after restore
docker compose start task-manager task-manager-background-svc
```

## Step 1: Prepare for restoration[​](#step-1-prepare-for-restoration "Direct link to Step 1: Prepare for restoration")

### Create safety backup[​](#create-safety-backup "Direct link to Create safety backup")

Before overwriting current data, create a safety backup:

```
# Backup current state
infrahub-backup create --backup-dir=/tmp/safety-backup

# Note the filename for potential recovery
SAFETY_BACKUP=$(ls -t /tmp/safety-backup/*.tar.gz | head -1)
echo "Safety backup: $SAFETY_BACKUP"
```

## Step 2: Execute the restore[​](#step-2-execute-the-restore "Direct link to Step 2: Execute the restore")

### Basic restore[​](#basic-restore "Direct link to Basic restore")

Restore from a backup file:

```
infrahub-backup restore infrahub_backups/infrahub_backup_20250929_143022.tar.gz
```

The restore process will:

1. Validate backup compatibility
2. Stop all Infrahub containers
3. Clear existing data
4. Restore Neo4j database
5. Restore PostgreSQL task manager
6. Restart all services

### Restore from S3[​](#restore-from-s3 "Direct link to Restore from S3")

Restore directly from S3 or S3-compatible storage using an `s3://` URI:

* AWS S3
* MinIO
* Environment Variables

```
# Restore from S3
infrahub-backup restore s3://my-backups/infrahub/prod/infrahub_backup_20250929_143022.tar.gz
```

```
# Restore from MinIO or S3-compatible storage
infrahub-backup restore \
  --s3-endpoint http://minio.local:9000 \
  s3://my-backups/infrahub_backup_20250929_143022.tar.gz
```

```
# Configure S3 via environment variables
export AWS_ACCESS_KEY_ID=your-access-key
export AWS_SECRET_ACCESS_KEY=your-secret-key

infrahub-backup restore s3://my-backups/infrahub/prod/infrahub_backup_20250929_143022.tar.gz
```

info

The backup is downloaded to the local backup directory before restoration. The downloaded file is automatically cleaned up after the restore completes.

### Restore to specific project[​](#restore-to-specific-project "Direct link to Restore to specific project")

If you have multiple Infrahub projects:

```
# Restore to a specific Docker Compose project
infrahub-backup restore infrahub_backups/infrahub_backup_20250929_143022.tar.gz --project=infrahub-staging
```

## Step 3: Monitor restoration progress[​](#step-3-monitor-restoration-progress "Direct link to Step 3: Monitor restoration progress")

Watch the detailed restoration output:

```
INFO[0000] Starting restore process...
INFO[0000] Reading backup metadata...
INFO[0001] Backup created: 2025-09-29T14:30:22Z
INFO[0001] Backup version: 1.0.0
INFO[0001] Validating backup compatibility...
INFO[0002] Validation successful
INFO[0002] Stopping all Infrahub containers...
INFO[0008] All containers stopped
INFO[0008] Extracting backup archive...
INFO[0012] Archive extracted successfully
INFO[0012] Restoring Neo4j database...
INFO[0025] Neo4j database restored
INFO[0025] Restoring PostgreSQL database...
INFO[0030] PostgreSQL database restored
INFO[0032] Starting Infrahub containers...
INFO[0040] All containers started
INFO[0040] Restore completed successfully
```

## Step 4: verify restoration[​](#step-4-verify-restoration "Direct link to Step 4: verify restoration")

### Check service health[​](#check-service-health "Direct link to Check service health")

Verify all services are running:

```
# Check container status
docker compose ps

# All containers should show "Up" status
# Example output:
# NAME                    IMAGE                      STATUS
# infrahub-server         opsmill/infrahub:stable    Up 2 minutes
# database                neo4j:5.13                 Up 2 minutes
# task-manager-db         postgres:15                Up 2 minutes
```

### Test application access[​](#test-application-access "Direct link to Test application access")

Confirm Infrahub is accessible:

```
# Test HTTP endpoint
curl -I http://localhost:8000

# Check GraphQL endpoint
curl -X POST http://localhost:8000/graphql \
  -H "Content-Type: application/json" \
  -d '{"query": "{ InfrahubInfo { version } }"}'
```

### Validate data integrity[​](#validate-data-integrity "Direct link to Validate data integrity")

Verify your data was restored correctly:

1. Log into the Infrahub web interface
2. Check that your schemas are present
3. Verify critical data objects exist
4. Test a few key queries or operations
5. Review recent task history

## Step 5: post-restoration tasks[​](#step-5-post-restoration-tasks "Direct link to Step 5: post-restoration tasks")

### Verify integrations[​](#verify-integrations "Direct link to Verify integrations")

Check external integrations are working:

* Git repositories sync correctly
* External authentication (LDAP/SSO) functions
* Webhook endpoints are accessible
* API integrations reconnect properly

## Validation[​](#validation "Direct link to Validation")

Confirm restoration was successful:

* ✓ All services are running
* ✓ Web interface is accessible
* ✓ Data appears complete and correct
* ✓ Authentication works
* ✓ Background tasks are processing
* ✓ Integrations are functional

## Related resources[​](#related-resources "Direct link to Related resources")

* [How to backup your Infrahub instance](/backup/guides/backup-instance.md)
* [CLI command reference](/backup/reference/commands.md)
