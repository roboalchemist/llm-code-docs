# Source: https://firebase.google.com/docs/firestore/enterprise/backups.md.txt

This page describes how to use the Cloud Firestore scheduled backups
feature. Use backups to protect your data from application-level data
corruption or from accidental data deletion.

Backups let you configure backup schedules to take daily or weekly
backups of the specified database. You can then use these backups to restore
data to a new database.

## About backups

A backup is a consistent copy of the database at a point in time.
The backup contains all data and index configurations at that point
in time.
A backup does not contain database [time to live policies.](https://firebase.google.com/docs/firestore/enterprise/ttl) A backup resides in the same location as the source database.

<br />

Backups have a configurable retention period and are stored until the retention
period expires or until you delete the backup. Deleting the source database does
not automatically delete related backups.

Cloud Firestore stores metadata related to backups and backup
schedules related to a database. Cloud Firestore retains this metadata
until **all** backups for the database expire or are deleted.

Creating or retaining backups does not affect the performance of reads or
writes in your live database.

## Costs

When you use backups, you're charged for the following:

- The amount of storage used by each backup.
- For a restore operation, you're charged based on the size of the backup.

For more details and exact rates, see the [Pricing](https://cloud.google.com/firestore/enterprise/pricing) page.

## Before you begin

This feature requires the [Blaze pricing plan](https://firebase.google.com/docs/projects/billing/firebase-pricing-plans#blaze-pricing-plan).

### Required roles

To get the permissions that you need to manage backups and backup schedules,
ask your administrator to grant you one or more of the following Identity and Access Management
roles:

- `roles/datastore.owner`: Full access to the Cloud Firestore database
- `roles/datastore.backupsAdmin`: Read and write access to backups
- `roles/datastore.backupsViewer`: Read access to backups
- `roles/datastore.backupSchedulesAdmin`: Read and write access to backup schedules
- `roles/datastore.backupSchedulesViewer`: Read access to backup schedules
- `roles/datastore.restoreAdmin`: Permissions to initiate restore operations

## Create and manage backup schedules

The following examples demonstrate how to set up a backup schedule. For each
database, you can configure up to one daily backup schedule and up to one weekly
backup schedule. You cannot configure multiple weekly backups schedules for
different days of the week.

You cannot configure the exact time of day of the backup. Backups are taken at
different times each day. For weekly backup
schedules, you can configure the day of the week to take a backup.

### Create a backup schedule

Use one of the following tools to create a backup schedule.

#### Create a daily backup schedule

##### Google Cloud console

1. In the Google Cloud console, go to the **Databases** page.

   [Go to Databases](https://console.cloud.google.com/firestore/databases)
2. In the list of databases, find the row for the database. In the **Scheduled backups** column click either **View backups** or **Edit settings**, depending on whether a backup schedule exists.
3. Click **Edit** to edit disaster recovery settings.
4. Select the **Daily** checkbox, set the retention period, and then click **Save**.

##### Firebase CLI

To create a backup schedule for a database, use the `firebase firestore:databases:backups:schedules:create` command. To create a daily backup schedule, set the `--recurrence` flag to `DAILY`:

```sh
firebase firestore:backups:schedules:create \
--database 'DATABASE_ID' \
--recurrence 'DAILY' \
--retention RETENTION_PERIOD
```

Replace the following:

- <var translate="no">DATABASE_ID</var>: The ID of the database to back up. Set to `'(default)'` for the default database.
- <var translate="no">RETENTION_PERIOD</var>: Set this to a value up to 14 weeks (`14w`).

##### Terraform

To create a daily backup schedule, create a `https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/firestore_backup_schedule` resource.

```terraform
resource "google_firestore_backup_schedule" "daily-backup" {
  project  = PROJECT_ID
  database = DATABASE_ID

  retention = RETENTION_PERIOD_SECONDS

  daily_recurrence {}
}
```

Replace the following:

- <var translate="no">PROJECT_ID</var>: The ID of the project.
- <var translate="no">DATABASE_ID</var>: The ID of the database to back up. Set to `'(default)'` for the default database.
You can also use a [resource reference](https://developer.hashicorp.com/terraform/language/expressions/references#resources) to a Terraform resource of type `https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/firestore_database`.
- <var translate="no">RETENTION_PERIOD_SECONDS</var>: Set this to a value in seconds, followed by "s". The maximum value is `8467200s` (14 weeks).

#### Create a weekly backup schedule

##### Google Cloud console

1. In the Google Cloud console, go to the **Databases** page.

   [Go to Databases](https://console.cloud.google.com/firestore/databases)
2. In the list of databases, find the row for the database. In the **Scheduled backups** column click either **View backups** or **Edit settings**, depending on whether a backup schedule exists.
3. Click **Edit** to edit disaster recovery settings.
4. Select the **Weekly** checkbox, select a backup day, set the retention period, and then click **Save**.

##### Firebase CLI

To create a weekly backup schedule, set the `--recurrence` flag to `WEEKLY` and choose the `--day-of-week`:

```sh
firebase firestore:backups:schedules:create \
--database 'DATABASE_ID' \
--recurrence 'WEEKLY' \
--retention RETENTION_PERIOD
--day-of-week DAY
```
Replace the following:

- <var translate="no">DATABASE_ID</var>: The ID of the database to back up. Set to `'(default)'` for the default database.
- <var translate="no">RETENTION_PERIOD</var>: Set this to a value up to 14 weeks (`14w`).
- <var translate="no">DAY</var>: The day of the week to take the backup. Set to one of the following:
  - `SUNDAY` for Sunday
  - `MONDAY` for Monday
  - `TUESDAY` for Tuesday
  - `WEDNESDAY` for Wednesday
  - `THURSDAY` for Thursday
  - `FRIDAY` for Friday
  - `SATURDAY` for Saturday

##### Terraform

To create a weekly backup schedule, create a `https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/firestore_backup_schedule` resource.

```terraform
resource "google_firestore_backup_schedule" "weekly-backup" {
  project  = PROJECT_ID
  database = DATABASE_ID

  retention = RETENTION_PERIOD_SECONDS

  weekly_recurrence {
    day = DAY
  }
}
```

Replace the following:

- <var translate="no">PROJECT_ID</var>: The ID of the project.
- <var translate="no">DATABASE_ID</var>: The ID of the database to back up. Set to `'(default)'` for the default database.
You can also use a [resource reference](https://developer.hashicorp.com/terraform/language/expressions/references#resources) to a Terraform resource of type `https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/firestore_database`.
- <var translate="no">RETENTION_PERIOD_SECONDS</var>: Set this to a value in seconds, followed by "s". The maximum value is `8467200s` (14 weeks).
- <var translate="no">DAY</var>: The day of the week to take the backup. Set to one of the following:
  - `SUNDAY` for Sunday
  - `MONDAY` for Monday
  - `TUESDAY` for Tuesday
  - `WEDNESDAY` for Wednesday
  - `THURSDAY` for Thursday
  - `FRIDAY` for Friday
  - `SATURDAY` for Saturday

### List backup schedules

To list all backup schedules for a database, use one of the following methods:

##### Google Cloud console

1. In the Google Cloud console, go to the **Databases** page.

   [Go to Databases](https://console.cloud.google.com/firestore/databases)
2. In the list of databases, find the row for the database. In the **Scheduled backups** column click either **View backups** or **Edit settings**, depending on whether a backup schedule exists.
3. The **Disaster recovery** page opens. This page describes backup schedules and lists available backups.

##### Firebase CLI

Use the `firebase firestore:backups:schedules:list` command.

```sh
firebase firestore:backups:schedules:list \
--database 'DATABASE_ID'
```
Replace <var translate="no">DATABASE_ID</var> with the ID of the database. Use `'(default)'` for the default database.

### Describe backup schedule

To retrieve information about a backup schedule, use one of the following methods:

##### Google Cloud console

1. In the Google Cloud console, go to the **Databases** page.

   [Go to Databases](https://console.cloud.google.com/firestore/databases)
2. In the list of databases, find the row for the database. In the **Scheduled backups** column click either **View backups** or **Edit settings**, depending on whether a backup schedule exists.
3. The **Disaster recovery** page opens. This page describes backup schedules and lists available backups.

##### gcloud

Use the [`gcloud firestore backups schedules describe`](https://cloud.google.com/sdk/gcloud/reference/alpha/firestore/backups/schedules/describe) command:

```sh
gcloud firestore backups schedules describe \
--database='DATABASE_ID' \
--backup-schedule=BACKUP_SCHEDULE_ID
```
Replace the following:

- <var translate="no">DATABASE_ID</var>: The ID of the database to back up. Set to `'(default)'` for the default database.
- <var translate="no">BACKUP_SCHEDULE_ID</var>: The ID of a backup schedule. You can view the ID of each backup schedule when you [list all backup schedules](https://firebase.google.com/docs/firestore/enterprise/backups#list_backup_schedules).

### Update a backup schedule

To update the retention period of a backup schedule, use one of the following methods:

##### Google Cloud console

1. In the Google Cloud console, go to the **Databases** page.

   [Go to Databases](https://console.cloud.google.com/firestore/databases)
2. In the list of databases, find the row for the database. In the **Scheduled backups** column click either **View backups** or **Edit settings**.
3. Click **Edit** to edit disaster recovery settings.
4. Edit the backup schedule settings and then click **Save**.

##### Firebase CLI

Use the `firebase firestore:backups:schedules:update` command:

```sh
firebase firestore:backups:schedules:update \
BACKUP_SCHEDULE \
--retention RETENTION_PERIOD
```
Replace the following:

- <var translate="no">BACKUP_SCHEDULE</var>: The full resource name of a backup schedule. You can view the name of each backup schedule when you [list all backup schedules](https://firebase.google.com/docs/firestore/enterprise/backups#list_backup_schedules).
- <var translate="no">RETENTION_PERIOD</var>: Set this to a value up to 14 weeks (`14w`).

You can update the retention period of a backup schedule, but you cannot update its recurrence. If you need a backup schedule with a different recurrence, delete the old backup schedule if it is no longer required and create a new backup schedule with the preferred recurrence.

### Delete a backup schedule

To delete a backup schedule, use one of the following methods:

##### Google Cloud console

1. In the Google Cloud console, go to the **Databases** page.

   [Go to Databases](https://console.cloud.google.com/firestore/databases)
2. In the list of databases, find the row for the database. In the **Scheduled backups** column click either **View backups** or **Edit settings**, depending on whether a backup schedule exists.
3. Click **Edit** to edit disaster recovery settings.
4. Edit the backup schedule settings and then click **Save**.

##### Firebase CLI

Use the `firebase firestore:backups:schedules:delete` command:

```sh
firebase firestore:backups:schedules:delete \
BACKUP_SCHEDULE
```
Replace the following:

- <var translate="no">BACKUP_SCHEDULE</var>: The full resource name of a backup schedule. You can view the name of each backup schedule when you [list all backup schedules](https://firebase.google.com/docs/firestore/enterprise/backups#list_backup_schedules).

Note that deleting a backup schedule won't delete backups already created by
this schedule. You can wait for them to expire after their retention period, or
to manually delete a backup, see [delete backup](https://firebase.google.com/docs/firestore/enterprise/backups#delete_backup).

## Manage backups

### List backups

To list available backups, use one of the following methods:

##### Google Cloud console

1. In the Google Cloud console, go to the **Databases** page.

   [Go to Databases](https://console.cloud.google.com/firestore/databases)
2. In the list of databases, find the row for the database. In the **Scheduled backups** column click either **View backups** or **Edit settings**, depending on whether a backup schedule exists.
3. Click **Edit** to edit disaster recovery settings.
4. Edit the backup schedule settings and then click **Save**.

##### Firebase CLI

Use the `firebase firestore:backups:list` command:

```sh
firebase firestore:backups:list
```
To list only the backups from a specific location, use the `--location` flag:

```sh
firebase firestore:backups:list \
--location=LOCATION
```
Replace `LOCATION` with the name of a Cloud Firestore location.

### Describe a backup

To view details about a backup, use one of the following methods:

##### Google Cloud console

1. In the Google Cloud console, go to the **Databases** page.

   [Go to Databases](https://console.cloud.google.com/firestore/databases)
2. In the list of databases, find the row for the database. In the **Scheduled backups** column click either **View backups** or **Edit settings**, depending on whether a backup schedule exists.
3. The **Disaster recovery** page opens. This page describes backup schedules and lists available backups.

##### Firebase CLI

Use the `firebase firestore:backups:get` command:

```sh
firebase firestore:backups:get BACKUP
```
Replace the following:

- <var translate="no">BACKUP</var>: The full resource name of a backup. You can view the name of each backup when you [list all backups](https://firebase.google.com/docs/firestore/enterprise/backups#list_backups).

### Delete backup

To delete a backup, use one of the following methods.

> [!WARNING]
> **Warning:** You cannot recover a deleted backup.

##### Google Cloud console

1. In the Google Cloud console, go to the **Databases** page.

   [Go to Databases](https://console.cloud.google.com/firestore/databases)
2. In the list of databases, find the row for the database. In the **Scheduled backups** column click either **View backups** or **Edit settings** , depending on whether a backup schedule exists. The **Disaster recovery** page opens. This page describes backup schedules and lists available backups.
3. In the **Backups** table, find the row for a backup and in the **Actions** column, click **View more** (). Click **Delete**.
4. Confirm the action using the text field and click **Delete**.

##### Firebase CLI

Use the `firebase firestore:backups:delete` command:

```sh
firebase firestore:backups:delete \
BACKUP
```
Replace the following:

- <var translate="no">BACKUP</var>: The full resource name of a backup. You can view the name of each backup when you [list all backups](https://firebase.google.com/docs/firestore/enterprise/backups#list_backups).

> [!NOTE]
> **Note:** Cloud Firestore stores metadata related to backups and backup schedules related to a database. Cloud Firestore retains this metadata until **all** backups for the database expire or are deleted.

## Restore data from a database backup

A restore operation writes the data from a backup to a new Cloud Firestore
database.

To begin a restore operation, use one of the following methods:

##### Google Cloud console

1. In the Google Cloud console, go to the **Databases** page.

   [Go to Databases](https://console.cloud.google.com/firestore/databases)
2. In the list of databases, find the row for the database. In the **Scheduled backups** column click either **View backups** or **Edit settings** , depending on whether a backup schedule exists. The **Disaster recovery** page opens. This page describes backup schedules and lists available backups.
3. In the **Backups** table, find the row for a backup and in the **Actions** column, click **View more** (). Click **Restore with Cloud Shell**.
4. The Cloud Shell panel opens with a gcloud CLI command
   to restore from the selected backup. Replace <var translate="no">ID_OF_NEW_DATABASE</var> with
   an ID for the database and run the command.


   Running the command returns a response with more information about the
   operation. The database soon appears in your list of databases. The restore
   operation will take some time and must complete before the database is accessible.

##### Firebase CLI

Use the `firebase firestore:databases:restore` command:

```sh
firebase firestore:databases:restore \
--backup 'BACKUP' \
--database 'DATABASE_ID'
```
Replace the following:

- <var translate="no">BACKUP</var>: The full resource name of a backup. You can view the name of each backup when you [list all backups](https://firebase.google.com/docs/firestore/enterprise/backups#list_backups).
- <var translate="no">DATABASE_ID</var>: A database ID for the new database. You cannot use a database ID that is already in use.

### Limitations

A restore operation does not restore [App Engine search data](https://cloud.google.com/appengine/docs/legacy/standard/python/search) or [blob entities](https://cloud.google.com/appengine/docs/legacy/standard/python/blobstore) from a `(default)` database. This data is only valid for the `(default)` database, and it won't be useful if you restore from `(default)` to a database which does not support such data, so it is excluded from backups.

### What to do after restoring

After you finish restoring, you should do the following:

- Verify that appropriate [IAM controls](https://firebase.google.com/docs/firestore/enterprise/security/iam) are applied to your new database.

- If you previously used [TTL](https://firebase.google.com/docs/firestore/enterprise/ttl) policies, reapply them to the new database. TTL policies are not included in backups and are not automatically reapplied to restored databases.