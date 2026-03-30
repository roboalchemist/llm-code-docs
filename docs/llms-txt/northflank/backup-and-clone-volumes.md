# Source: https://northflank.com/docs/v1/application/databases-and-persistence/backup-and-clone-volumes.md

# Backup and clone volumes

Volume backups allow you to create point-in-time snapshots of your persistent volumes. You can restore these backups to new volumes or clone existing volumes for testing and development.

## Creating volume backups

Volume backups create snapshots of your volume at a specific point in time.

### Manual backups

To create a manual backup:

1. Navigate to your project

2. Click **Volumes** and select the volume you want to backup

3. Open the **Backups** tab

4. Click **Create backup**

5. (Optional) Provide a description for the backup

6. Click **Create**

The backup will be created and appear in the backups list.

## Cloning volumes

Cloning creates a new volume from an existing volume or backup. This is useful for:

- Creating test environments with production data

- Duplicating volumes across projects

- Recovering from volume corruption

### Clone from an existing volume

To clone a volume:

1. Navigate to **Volumes** in your project

2. Click **Create volume**

3. In the **Configuration** section, select **From source**

4. Configure the source:
  
  
  - **Source type**: Select **Existing volume**
  
  - **Volume to clone**: Select the volume to clone

5. Configure the new volume:
  
  
  - **Access mode**: Choose Single Read/Write or Multi Read/Write
  
  - **Storage type**: Select your preferred storage type
  
  - **Storage**: Must be equal to or larger than source volume
  
  - **Container mount path**: Specify where to mount the volume in containers

6. In the **Resources** section, select the service you want to attach it to

7. Click **Create volume**

The new volume will be created with data from the source volume.

### Restore from backup

To create a volume from a backup:

1. Navigate to **Volumes** in your project

2. Click **Create volume**

3. In the **Configuration** section, select **From source**

4. Configure the source:
  
  
  - **Source type**: Select **From backup**
  
  - **Source backup**: Select the backup to restore from

5. Configure the new volume:
  
  
  - **Access mode**: Choose **Single Read/Write** or **Multi Read/Write**
  
  - **Storage type**: Select **SSD** (or your preferred storage type)
  
  - **Storage**: Set size (must be equal to or larger than backup size)
  
  - **Container mount path**: Specify where to mount the volume (e.g., `/mydata`)

6. Complete any additional configuration (resources, tags, etc.)

7. Click **Create volume**

The new volume will be created with data from the backup.

## Use cases

### Development and testing

Clone production volumes to create staging or development environments with realistic data:

1. Create a backup of the production volume

2. Restore the backup to a new volume in your staging project

3. Attach the cloned volume to your staging services

4. Test with production-like data without affecting production

### Disaster recovery

Regular backups enable quick recovery from data corruption or accidental deletion:

1. Create regular manual backups of critical volumes

2. If data is corrupted, restore from the most recent backup

3. Attach the restored volume to your services

## Best practices

**Backup frequency:**

- Production volumes: Daily or more frequent

- Development volumes: Weekly or on-demand

- Critical data: Create backups before major changes

**Testing restores:**

- Regularly test backup restoration to verify data integrity

- Create test volumes from backups to ensure they're usable

- Document restoration procedures

**Monitoring:**

- Track backup creation success

- Monitor backup size growth

- Document backup schedules and procedures

## Limitations

- Backups are point-in-time snapshots and may not capture in-flight writes

- Restoration time depends on volume size

- Cloned volumes must be equal to or larger than the source

- Backups must be created manually (scheduled backups not currently supported)

## Next steps

- [Deploy a database: Create a database to use with your Northflank deployments.](/v1/application/databases-and-persistence/deploy-a-database)
- [Inject secrets: Set build arguments and inject runtime variables into running deployments.](/v1/application/secure/inject-secrets)
- [Transfer data to and from containers: Download data from, or to, ephemeral or persistent storage in your running containers.](/v1/application/run/transfer-data-to-and-from-containers)
