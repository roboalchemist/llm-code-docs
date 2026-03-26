# Source: https://docs.api7.ai/enterprise/upgrade-guides/backup-and-restore.md

# Source: https://docs.api7.ai/enterprise/3.8.x/upgrade-guides/backup-and-restore.md

# Backup and Restoration

Before starting any upgrade, **please back up your database data first**.

You can use the following two methods to back up your database data used in API7 Enterprise.

1. Use the native tools provided by the database to back up data. This allows you to quickly import the backed-up data into a new database for immediate recovery.
2. Use the [ADC tool](https://docs.api7.ai/enterprise/3.8.x/reference/adc.md) to back up your Gateway configurations (services, routes, plugins, consumers, etc.) in the form of declarative configuration files.

It is recommended to use both methods simultaneously, as this provides greater flexibility when restoring data in case of the following issues.

danger

If data is corrupted, **please try database-level restoration first**, otherwise use a new database and update your previous configurations using the stored declarative configuration files.

## Database Backup[â](#database-backup "Direct link to Database Backup")

### Database-Native Backup[â](#database-native-backup "Direct link to Database-Native Backup")

API7 Enterprise uses `PostgreSQL` database by default. Using PostgreSQL's native commands, you can use the `pg_dump` command to back up data in plain text, directory, and other formats. For example, the command to back up in directory format:

```
pg_dump -U api7ee -d api7ee -F d -f api7ee_backup_20250523
```

* `pg_dump`: PostgreSQL's logical backup tool for exporting database contents.
* `-U api7ee`: Specifies the database connection username as `api7ee`.
* `-d api7ee`: Specifies the database name to back up as `api7ee`.
* `-F d`: Specifies the backup format as directory format, which is suitable for large databases and parallel restoration.
* `-f api7ee_backup_20250523`: Specifies the output directory name for the backup as `api7ee_backup_20250523`. The backup results will be stored in this directory.

### Declarative File Backup[â](#declarative-file-backup "Direct link to Declarative File Backup")

Use the [ADC tool](https://docs.api7.ai/enterprise/3.8.x/reference/adc.md) to back up your API7 Gateway configurations (services, routes, plugins, consumers, etc.) in the form of declarative configuration files.

1. Use ADC to perform service verification, ensuring it can connect to API7 Enterprise normally:

   ```
   adc ping --backend api7ee --server "https://{DASHBOARD_ADDR}"
   ```

2. Use ADC `dump` command to store each gateway group's data locally:

   ```
   adc dump -o api7ee-dump.yaml --backend api7ee --server "https://{DASHBOARD_ADDR}"
   ```

There is the [sample configuration file](https://docs.api7.ai/enterprise/3.8.x/reference/configuration-adc.md#sample-configuration-file). For more ADC commands, please see [ADC Command Reference](https://docs.api7.ai/enterprise/3.8.x/reference/adc.md).

## Data Restoration and Rollback[â](#data-restoration-and-rollback "Direct link to Data Restoration and Rollback")

### Restore from Database[â](#restore-from-database "Direct link to Restore from Database")

To restore API7 Enterprise data from database backup, you need to prepare a new database first, using PostgreSQL as an example.

<!-- -->

1. Modify the database connection address to the new database in the CP (Dashboard and DP-Manager) configuration file:

   ```
   database:
     dsn: "postgres://api7ee:changeme@192.168.31.10:5432/api7ee"
   ```

   Restart the CP.

2. Restore the previously backed-up data:

   ```
   pg_restore -U api7ee -C -d api7ee api7ee_backup_20250523/
   ```

   * `-U`: Specifies the database connection username. This user needs sufficient permissions to create and restore the database.
   * `-C`: Create the target database first, then connect to the database for restoration.
   * `-d`: Specifies the target database name.

3. Use the previously stored local deployment scripts or configuration files for Gateway Instance to redeploy the nodes in the DP.

### Restore from Declarative Configuration[â](#restore-from-declarative-configuration "Direct link to Restore from Declarative Configuration")

danger

If you encounter issues and need to roll back, **please try database restoration first**. Only use declarative configuration restoration as a last resort if your data is corrupted.

First, restore your deployed API7 Enterprise (CP & DP) to the original version's configuration and image tag, and connect it to your newly prepared database. Then, use the [ADC tool](https://docs.api7.ai/enterprise/3.8.x/reference/adc.md) to restore your previous configurations.

1. Use ADC to verify service connectivity and confirm that it can connect to API7 Enterprise:

   ```
   adc ping --backend api7ee --server "https://{DASHBOARD_ADDR}"
   ```

2. Use ADC to sync each gateway group's data:

   ```
   adc sync -f api7ee-dump.yaml --backend api7ee --server "https://{DASHBOARD_ADDR}"
   ```

## Other Files[â](#other-files "Direct link to Other Files")

In addition to the resource configurations you created in API7 Enterprise, there are some important files that need to be backed up manually:

1. The `conf.yaml` file created for Gateway Instance.
2. Source code of custom plugins.
3. Deployment scripts and other files used when deploying [API7 Gateway Instance](https://docs.api7.ai/enterprise/3.8.x/getting-started/add-gateway-instance.md).

These files are tied to your business and deployment environment. The absence of these files could impact data restoration in case of issues.

It is recommended to store these files on the platform where you deploy API7 Enterprise for centralized management.
