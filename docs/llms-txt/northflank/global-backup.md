# Source: https://northflank.com/docs/v1/application/databases-and-persistence/global-backup.md

# Global backup

Global backups are team-level backup resources that can be accessed and restored across any project in your team. Unlike project-scoped backups which are tied to a specific addon, global backups provide flexibility for cross-project restoration, disaster recovery, and data migration scenarios.

To view or manage global backups, navigate to the `Backups` page from your team menu.

The global backups page displays all backups created in your team, including both native snapshots and database dumps, regardless of which project they originated from.

> [!note] 
> [Click here](http://app.northflank.com/s/account/backups) to view your global backups.

## Global backup types

Global backups support two backup types:

| Type | Description | Best for |
| --- | --- | --- |
| Disk | Block-level snapshots of addon storage | Fast backups with minimal impact on running addons |
| Native | Database dumps using native tools | Portability outside Northflank and cross-platform use |

**Disk backups** create snapshots of your addon's storage. They're fast to create and restore with minimal impact on your addon. Global backups enable cross-region restoration of disk snapshots, which are normally zone or region-scoped.

**Native backups** export database contents using database-native tools (e.g., `pg_dump`, `mongodump`). They take longer and may impact the addon during backup (run against read replicas when possible). The main advantage is portability: native dumps work outside Northflank and across different infrastructure.

Both types support cross-region restoration and migration through global backups.

## Creating global backups

### Manual global backups

Manual global backups can be created on-demand from any addon in your team.

**From an addon:**

1. Navigate to the addon you want to backup

2. Open the **Backups** tab

3. Click **Create backup**

4. Choose backup type:
  
  
  - **Disk**: For fast snapshots
  
  - **Native Dump**: For portable database dumps

5. Configure global backup settings:
  
  
  - For **disk backups**: Enable "Take additional global backups" and choose the destination and retention time
  
  - For **native backups**: Enable "Store backup in custom destination" and select the backup destination

6. Click **Create backup**

The backup will appear in the global backups list and be accessible from any project in your team. Global backups are automatically tagged with the source addon name, project, timestamp, and database information.

### Scheduled global backups

Configure automatic global backups to run on a schedule, ensuring your critical data is backed up regularly without manual intervention.

**Setting up a backup schedule:**

1. Navigate to the addon

2. Click on the **Backup schedule** tab

3. Click **Add schedule**

4. Configure the schedule:
  
  
  - **Hourly**: Every N hours (1-23)
  
  - **Daily**: Specific time each day
  
  - **Weekly**: Specific day and time

5. Enable "Take additional global backups" and choose the destination and retention time

6. Save the schedule

### Multiple destinations

Scheduled global backups can store copies in multiple destinations simultaneously. This provides redundancy and allows you to meet different requirements with a single backup operation.

For example, you could configure:

- Primary: Your S3 bucket in `us-east-1` (co-located with services)

- Secondary: Your S3 bucket in `eu-west-1` (for disaster recovery)

All copies are created from the same backup operation, ensuring consistency.

## Global backup destinations

Backup destinations define where backup data is stored. You can use Northflank's managed storage (on PaaS) or configure custom S3-compatible destinations (on BYOC).

To manage backup destinations, navigate to the [backup destinations page](https://app.northflank.com/s/account/backups/destinations) from your team menu.

### Custom backup destinations

Create custom backup destinations for:

- **Compliance**: Store backups in your own infrastructure

- **Fault tolerance**: Store backups in different regions

- **Data migration**: Move data between clusters

**To create a custom destination:**

1. Navigate to [backup destinations](https://app.northflank.com/s/account/backups/destinations)

2. Click **Create backup destination**

3. Provide S3-compatible storage credentials:
  
  
  - Endpoint URL
  
  - Access key ID
  
  - Secret access key
  
  - Bucket name
  
  - Region

4. Test the connection

5. Save the destination

## Restoring from global backups

Global backups can be restored to create new addons in any project within your team.

**To restore a backup:**

1. Navigate to the [global backups page](https://app.northflank.com/s/account/backups)

2. Find the backup you want to restore

3. Click **Restore** or **Fork**

4. Select the target project

5. Configure the new addon settings (name, region, resources, version)

6. Confirm restoration

The addon will be created from the backup data.

## Forking addons from global backups

Forking creates a new addon from an existing global backup, allowing you to create copies of databases for testing, development, or migration. This can be done across projects, clusters, and regions.

### During addon creation

When creating a new addon, you can select a global backup as the data source:

1. Create a new addon (database)

2. In the **Data** section, choose **From global backup** and select:
  
  
  - **Source project**: Choose any project in your team
  
  - **Source addon**: Choose your preferred source addon
  
  - **Global backup**: Choose from any backup in your team

3. Configure the new addon settings (name, region, resources, version)

4. Click **Create addon**

The new addon will be created with data from the selected backup.
