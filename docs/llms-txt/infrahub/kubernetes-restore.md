# Source: https://docs.infrahub.app/backup/guides/kubernetes-restore.md

# How to restore Infrahub on Kubernetes

This guide walks you through restoring your Infrahub instance on Kubernetes from a backup stored in S3-compatible storage. The restore process uses the same `infrahub-backup` Helm chart and runs as a Kubernetes Job.

warning

Restoring a backup will overwrite your current Infrahub data. Create a safety backup before proceeding if you need to preserve any recent changes.

## High availability (CloudNativePG)[​](#high-availability-cloudnativepg "Direct link to High availability (CloudNativePG)")

If your deployment uses a CloudNativePG HA PostgreSQL cluster, the restore process automatically detects and targets the primary pod. No special configuration is needed. See the [Kubernetes backup guide](/backup/guides/kubernetes-backup.md#high-availability-cloudnativepg) for details on supported HA operators.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

Before restoring:

* A backup file stored in S3-compatible storage
* The backup was created from the same Infrahub edition (Community or Enterprise)
* Access to modify Helm values for your Infrahub deployment
* S3 credentials with read access to the backup bucket

## Step 1: Identify the backup to restore[​](#step-1-identify-the-backup-to-restore "Direct link to Step 1: Identify the backup to restore")

List available backups in your S3 bucket:

```
# AWS S3
aws s3 ls s3://my-infrahub-backups/

# MinIO
mc ls myminio/my-infrahub-backups/
```

Note the exact filename of the backup you want to restore, for example: `infrahub_backup_20250120_020000.tar.gz`

### Verify backup metadata[​](#verify-backup-metadata "Direct link to Verify backup metadata")

Before restoring, verify the backup is compatible:

```
# Download and inspect metadata
aws s3 cp s3://my-infrahub-backups/infrahub_backup_20250120_020000.tar.gz ./
tar -xzOf infrahub_backup_20250120_020000.tar.gz backup_information.json | jq '.'
```

Check that:

* `neo4j_edition` matches your current deployment
* `infrahub_version` is compatible with your target version
* `components` includes the data you need to restore

## Step 2: Configure S3 source[​](#step-2-configure-s3-source "Direct link to Step 2: Configure S3 source")

Create or verify the S3 credentials secret exists:

```
kubectl create secret generic backup-s3-credentials \
  --namespace infrahub \
  --from-literal=AWS_ACCESS_KEY_ID=your-access-key \
  --from-literal=AWS_SECRET_ACCESS_KEY=your-secret-key
```

## Step 3: Configure the restore Job[​](#step-3-configure-the-restore-job "Direct link to Step 3: Configure the restore Job")

* Via Infrahub Helm Chart (Recommended)
* Standalone Chart

Add the restore configuration to your Infrahub Helm values:

```
# values.yaml for Infrahub Helm chart
infrahub-backup:
  enabled: true

  # Disable backup during restore
  backup:
    enabled: false

  # Enable restore
  restore:
    enabled: true
    s3:
      bucket: "my-infrahub-backups"
      key: "infrahub_backup_20250120_020000.tar.gz"
      endpoint: "https://s3.amazonaws.com"
      region: "us-east-1"
      secretName: "backup-s3-credentials"
```

Create a values file for the restore operation:

```
# restore-values.yaml
backup:
  enabled: false

restore:
  enabled: true
  s3:
    bucket: "my-infrahub-backups"
    key: "infrahub_backup_20250120_020000.tar.gz"
    endpoint: "https://s3.amazonaws.com"
    region: "us-east-1"
    secretName: "backup-s3-credentials"
```

## Step 4: Deploy the restore Job[​](#step-4-deploy-the-restore-job "Direct link to Step 4: Deploy the restore Job")

warning

The restore process will stop Infrahub services temporarily. Plan for downtime during the restore operation.

* Via Infrahub Helm Chart
* Standalone Chart

Update your Infrahub Helm release:

```
helm upgrade infrahub oci://registry.opsmill.io/opsmill/chart/infrahub \
  --namespace infrahub \
  --values values.yaml
```

Install or upgrade the chart with restore enabled:

```
helm upgrade --install infrahub-backup oci://registry.opsmill.io/opsmill/chart/infrahub-backup \
  --namespace infrahub \
  --values restore-values.yaml
```

## Step 5: Monitor restore progress[​](#step-5-monitor-restore-progress "Direct link to Step 5: Monitor restore progress")

### Watch the restore Job[​](#watch-the-restore-job "Direct link to Watch the restore Job")

```
# Check Job status
kubectl get job -n infrahub -l app.kubernetes.io/name=infrahub-backup

# Watch pod status
kubectl get pods -n infrahub -l app.kubernetes.io/name=infrahub-backup -w
```

### View restore logs[​](#view-restore-logs "Direct link to View restore logs")

```
# Stream logs from the restore pod
kubectl logs -n infrahub -l app.kubernetes.io/name=infrahub-backup -f
```

Expected output for a successful restore:

```
INFO[0000] Starting restore process...
INFO[0001] Downloading backup from S3: s3://my-infrahub-backups/infrahub_backup_20250120_020000.tar.gz
INFO[0010] Download completed (1.5GB)
INFO[0010] Extracting backup archive...
INFO[0012] Validating backup metadata...
INFO[0012] Backup ID: 20250120_020000
INFO[0012] Infrahub version: 0.15.0
INFO[0012] Components: database, task-manager-db
INFO[0013] Validating checksums...
INFO[0015] All checksums valid
INFO[0015] Stopping Infrahub services...
INFO[0020] Wiping transient data (cache, message-queue)...
INFO[0022] Restoring PostgreSQL database...
INFO[0030] PostgreSQL restore completed
INFO[0030] Restarting support services...
INFO[0035] Restoring Neo4j database...
INFO[0060] Neo4j restore completed
INFO[0060] Starting Infrahub services...
INFO[0070] All services started
INFO[0070] Restore completed successfully
```

## Step 6: Verify restored instance[​](#step-6-verify-restored-instance "Direct link to Step 6: Verify restored instance")

### Check service health[​](#check-service-health "Direct link to Check service health")

```
# Verify all pods are running
kubectl get pods -n infrahub

# Check Infrahub server logs
kubectl logs -n infrahub -l app.kubernetes.io/component=infrahub-server --tail=50
```

### Validate data integrity[​](#validate-data-integrity "Direct link to Validate data integrity")

1. **Access the Infrahub UI** - Log in and verify your data is present
2. **Check the GraphQL API** - Query a known object to confirm data restoration
3. **Review task manager** - Verify historical task runs are visible

### Test a sample query[​](#test-a-sample-query "Direct link to Test a sample query")

```
# Port-forward to the Infrahub server
kubectl port-forward -n infrahub svc/infrahub-server 8000:8000

# Query the API
curl -X POST http://localhost:8000/graphql \
  -H "Content-Type: application/json" \
  -d '{"query": "{ InfrahubStatus { summary { schema_hash } } }"}'
```

## Step 7: Disable restore and re-enable backups[​](#step-7-disable-restore-and-re-enable-backups "Direct link to Step 7: Disable restore and re-enable backups")

After a successful restore, update your values to disable the restore Job and re-enable scheduled backups:

```
infrahub-backup:
  enabled: true

  backup:
    enabled: true
    mode: "cronjob"
    schedule: "0 2 * * *"
    storage:
      type: "s3"
      s3:
        bucket: "my-infrahub-backups"
        endpoint: "https://s3.amazonaws.com"
        region: "us-east-1"
        secretName: "backup-s3-credentials"

  restore:
    enabled: false  # Disable restore
```

Apply the updated configuration:

```
helm upgrade infrahub oci://registry.opsmill.io/opsmill/chart/infrahub \
  --namespace infrahub \
  --values values.yaml
```

## Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

### Restore Job fails to start[​](#restore-job-fails-to-start "Direct link to Restore Job fails to start")

Check if the S3 credentials secret exists:

```
kubectl get secret backup-s3-credentials -n infrahub
```

Verify the secret contains the expected keys:

```
kubectl get secret backup-s3-credentials -n infrahub -o jsonpath='{.data}' | jq 'keys'
```

### Download fails[​](#download-fails "Direct link to Download fails")

Check network connectivity and S3 endpoint configuration:

```
# View detailed error in logs
kubectl logs -n infrahub -l app.kubernetes.io/name=infrahub-backup

# Common issues:
# - Incorrect bucket name
# - Wrong S3 endpoint URL
# - Invalid credentials
# - Network policy blocking egress
```

### Checksum validation fails[​](#checksum-validation-fails "Direct link to Checksum validation fails")

The backup file may be corrupted. Try downloading a fresh copy:

```
# Verify the backup locally
aws s3 cp s3://my-infrahub-backups/infrahub_backup_20250120_020000.tar.gz ./
tar -tzf infrahub_backup_20250120_020000.tar.gz > /dev/null
```

### Services fail to restart[​](#services-fail-to-restart "Direct link to Services fail to restart")

Check for resource constraints or scheduling issues:

```
# Check pod events
kubectl describe pods -n infrahub -l app.kubernetes.io/name=infrahub

# Check node resources
kubectl top nodes
```

## Validation[​](#validation "Direct link to Validation")

Confirm your restore completed successfully:

* <!-- -->
  Restore Job completed without errors
* <!-- -->
  All Infrahub pods are running
* <!-- -->
  Infrahub UI is accessible
* <!-- -->
  Data is present and correct
* <!-- -->
  Task manager shows historical runs
* <!-- -->
  Scheduled backups are re-enabled
* <!-- -->
  Restore Job is disabled to prevent accidental re-runs

## Related resources[​](#related-resources "Direct link to Related resources")

* [How to backup Infrahub on Kubernetes](/backup/guides/kubernetes-backup.md)
* [How to restore from backup (CLI)](/backup/guides/restore-backup.md)
