# Source: https://docs.velodb.io/cloud/4.x/management-guide/backup

Version: 4.x

On this page

# Backup and Restore

VeloDB Cloud supports backing up databases to object storage either
periodically or as a one-time operation, and allows users to quickly restore
data based on specified backup sets, comprehensively ensuring high
availability of data.

## Backup​

### Create a Backup Plan​

Click **Backup** in the left navigation bar, and click **Create Backup Plan**
on the Backup page. You can choose between periodic or one-time backups as
needed. Periodic and one-time backups have a mutual exclusion relationship.
Updating the backup plan will overwrite the original backup plan.

If periodic backup is selected, you need to choose whether to enable it, the
backup execution cycle, start time, backup objects, retention days, and the
cluster used for backup, and save the selected settings for them to take
effect.

![backup-periodic](/assets/images/backup-
periodic-8f7b6b62f6d4df40f129b3e8cc2efcea.png)

If you choose one-time backup, you need to select the start time, backup
objects, retention days, and the cluster used for backup. Similarly, you need
to save the selected settings for them to take effect.

![backup-one-time](/assets/images/backup-one-
time-24d271d69de3ec5713279a4c0861636b.png)

Parameter| Description| Backup Every| Multiple selections are allowed from
Monday to Sunday, with at least one day and at most seven days.| Start Time|
The startup time of the backup task.| Backup Objects| Internal Catalog:
Database; External Catalog: Only backs up DDL, not data.| Backup Retention
Days| Set the retention days for backup sets, and backup sets exceeding the
retention days will be cleared.| Backup Cluster| The backup process consumes
computing resources. In the case of multiple clusters, it is necessary to
specify the cluster to be used for backup operations.  
---|---  
  
### View Backup Tasks​

VeloDB Cloud will automatically execute backup tasks according to the plan you
set. View all backup tasks in the **Backup Tasks** list, including backup
status, retention days, data size, and backup start and completion times.

![backup-list](/assets/images/backup-list-
bfc1b861f701aea82ace15bce4f5e154.png)

Click the **View Details** in the operation column to obtain detailed
information about backup task execution.

![backup-detail](/assets/images/backup-
detail-f6e8d9392855dcb23fe4c9843ed36961.png)

## Restore​

You can select the row where the target backup set is located in the list of
backup tasks, click **Restore** in the operation column, specify the target
warehouse and cluster for the restore task, and then restore the backup.

![backup-restore](/assets/images/backup-
restore-10cb20e55017073d000fcb77c506b5ad.png)

Restore tasks will be displayed in the **Restore Tasks** list, where you can
view detailed information such as task status, data size, start and completion
time, etc.

![restore-list](/assets/images/restore-list-
bb7cfccacba2dcb121071b3ffcd69f85.png)

Click the **View Details** in the operation column to obtain detailed
information about restore task execution.

![restore-detail](/assets/images/restore-
detail-96e6a7d2eb901ef4c7915b70dbccb7b1.png)

On This Page

  * Backup
    * Create a Backup Plan
    * View Backup Tasks
  * Restore

