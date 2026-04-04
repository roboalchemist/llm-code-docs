# Source: https://planetscale.com/docs/vitess/imports/gcp-cloudsql-migration-guide.md

# GCP Cloud SQL Migration Guide

## Overview

This document will demonstrate how to migrate a database from Google Cloud Platform (GCP) Cloud SQL MySQL Cluster to PlanetScale using our [Import tool](/docs/vitess/imports/database-imports).

<Note>
  This guide assumes you are using MySQL on GCP. Other database systems available through GCP will not work with the
  PlanetScale import tool.
</Note>

We recommend reading through the [Database import documentation](/docs/vitess/imports/database-imports) to learn how our import tool works before proceeding.

## Prerequisites

Before you can perform a migration, gather the following information from the GCP Console:

* **Public IP address** - Found in the **Overview** tab of your Cloud SQL cluster under the **Connect to this instance** section
* **Database name** - The name of the database you want to import
* **Root username and password** - You'll need these to create the migration user

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/AspOsmxsYasYOxA4/docs/images/assets/docs/imports/gcp-cloudsql-migration-guide/cloudsql-ip-address.png?fit=max&auto=format&n=AspOsmxsYasYOxA4&q=85&s=d998a6198377ed0d0bba597d5b0bedde" alt="The GCP Cloud SQL console with the IP address highlighted." data-og-width="1754" width="1754" data-og-height="1330" height="1330" data-path="docs/images/assets/docs/imports/gcp-cloudsql-migration-guide/cloudsql-ip-address.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/AspOsmxsYasYOxA4/docs/images/assets/docs/imports/gcp-cloudsql-migration-guide/cloudsql-ip-address.png?w=280&fit=max&auto=format&n=AspOsmxsYasYOxA4&q=85&s=d7bbcd497e902ce4e5d6c4e2f06a71ae 280w, https://mintcdn.com/planetscale-cad1a68a/AspOsmxsYasYOxA4/docs/images/assets/docs/imports/gcp-cloudsql-migration-guide/cloudsql-ip-address.png?w=560&fit=max&auto=format&n=AspOsmxsYasYOxA4&q=85&s=8e345b8b6712bbf8f767a46f2b7951e2 560w, https://mintcdn.com/planetscale-cad1a68a/AspOsmxsYasYOxA4/docs/images/assets/docs/imports/gcp-cloudsql-migration-guide/cloudsql-ip-address.png?w=840&fit=max&auto=format&n=AspOsmxsYasYOxA4&q=85&s=ef043d2d0307cd13547991b3793baf8c 840w, https://mintcdn.com/planetscale-cad1a68a/AspOsmxsYasYOxA4/docs/images/assets/docs/imports/gcp-cloudsql-migration-guide/cloudsql-ip-address.png?w=1100&fit=max&auto=format&n=AspOsmxsYasYOxA4&q=85&s=406e6ace4cc2422eb09a46ec7e478180 1100w, https://mintcdn.com/planetscale-cad1a68a/AspOsmxsYasYOxA4/docs/images/assets/docs/imports/gcp-cloudsql-migration-guide/cloudsql-ip-address.png?w=1650&fit=max&auto=format&n=AspOsmxsYasYOxA4&q=85&s=9a75e188035a8e579cd0758d58581e8b 1650w, https://mintcdn.com/planetscale-cad1a68a/AspOsmxsYasYOxA4/docs/images/assets/docs/imports/gcp-cloudsql-migration-guide/cloudsql-ip-address.png?w=2500&fit=max&auto=format&n=AspOsmxsYasYOxA4&q=85&s=346f7c911abf90732276c1ad5db7e1f9 2500w" />
</Frame>

A list of your databases can be found in the **Databases** tab. In this guide, we'll be using the `prod` database.

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/AspOsmxsYasYOxA4/docs/images/assets/docs/imports/gcp-cloudsql-migration-guide/cloudsql-databases.png?fit=max&auto=format&n=AspOsmxsYasYOxA4&q=85&s=d32ce30657df2225b95e0326424dd58d" alt="The Databases list in the GCP console." data-og-width="1982" width="1982" data-og-height="1038" height="1038" data-path="docs/images/assets/docs/imports/gcp-cloudsql-migration-guide/cloudsql-databases.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/AspOsmxsYasYOxA4/docs/images/assets/docs/imports/gcp-cloudsql-migration-guide/cloudsql-databases.png?w=280&fit=max&auto=format&n=AspOsmxsYasYOxA4&q=85&s=376a9be77b70ec19742fa4b12cdf7129 280w, https://mintcdn.com/planetscale-cad1a68a/AspOsmxsYasYOxA4/docs/images/assets/docs/imports/gcp-cloudsql-migration-guide/cloudsql-databases.png?w=560&fit=max&auto=format&n=AspOsmxsYasYOxA4&q=85&s=7bb062a6938817e3abc4d23fbb45aed7 560w, https://mintcdn.com/planetscale-cad1a68a/AspOsmxsYasYOxA4/docs/images/assets/docs/imports/gcp-cloudsql-migration-guide/cloudsql-databases.png?w=840&fit=max&auto=format&n=AspOsmxsYasYOxA4&q=85&s=ebba9a3ea16cc1c570c55b2a2bb65c38 840w, https://mintcdn.com/planetscale-cad1a68a/AspOsmxsYasYOxA4/docs/images/assets/docs/imports/gcp-cloudsql-migration-guide/cloudsql-databases.png?w=1100&fit=max&auto=format&n=AspOsmxsYasYOxA4&q=85&s=99efbf396af676b815daea92d9b98e48 1100w, https://mintcdn.com/planetscale-cad1a68a/AspOsmxsYasYOxA4/docs/images/assets/docs/imports/gcp-cloudsql-migration-guide/cloudsql-databases.png?w=1650&fit=max&auto=format&n=AspOsmxsYasYOxA4&q=85&s=c1a98c2aaac4e1bb63d754690f5f8826 1650w, https://mintcdn.com/planetscale-cad1a68a/AspOsmxsYasYOxA4/docs/images/assets/docs/imports/gcp-cloudsql-migration-guide/cloudsql-databases.png?w=2500&fit=max&auto=format&n=AspOsmxsYasYOxA4&q=85&s=06c11421fd2d5122f310cde0335dfa6d 2500w" />
</Frame>

## Create a migration user

Create a migration user account with limited privileges for the import process. **You must run this as the root user or another user with admin privileges.** Connect to your Cloud SQL instance as root using the MySQL command line:

```bash  theme={null}
mysql -u root -p -h [your-cloud-sql-ip]
```

Then run the following script, making sure to update the placeholders:

* `<SUPER_STRONG_PASSWORD>` - The password for the `migration_user` account
* `<DATABASE_NAME>` - The name of the database you will import into PlanetScale

```sql  theme={null}
CREATE USER 'migration_user'@'%' IDENTIFIED BY '<SUPER_STRONG_PASSWORD>';
GRANT PROCESS, REPLICATION SLAVE, REPLICATION CLIENT, RELOAD ON *.* TO 'migration_user'@'%';
GRANT SELECT, INSERT, UPDATE, DELETE, SHOW VIEW, LOCK TABLES ON `<DATABASE_NAME>`.* TO 'migration_user'@'%';
GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, ALTER ON *.* TO 'migration_user'@'%';
GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, ALTER ON `_vt`.* TO 'migration_user'@'%';
GRANT SELECT ON mysql.db TO 'migration_user'@'%';
GRANT SELECT ON mysql.func TO 'migration_user'@'%';
GRANT SELECT ON mysql.tables_priv TO 'migration_user'@'%';
GRANT SELECT ON mysql.user TO 'migration_user'@'%';
GRANT SELECT ON performance_schema.* TO 'migration_user'@'%';
FLUSH PRIVILEGES;
```

Verify the grants were applied correctly:

```sql  theme={null}
SHOW GRANTS FOR 'migration_user'@'%';
```

You should see all the GRANT statements listed. If you only see one or two lines, the grants didn't apply correctly.

<Note>
  **Important**

  You must create the migration user on the MySQL command line and not in the GCP console. Creating users through the GCP console automatically grants the `cloudsqlsuperuser` role, which will cause the import to fail.
</Note>

## Allow PlanetScale to connect to your Cloud SQL instance

For PlanetScale to connect to your database, you'll need to update the Authorized networks for your cluster. The specific IP addresses to permit are shown during the import workflow on the **Connect to external database** step. The list includes IP addresses specific to your PlanetScale database region.

See the [Import public IP addresses](/docs/vitess/imports/import-tool-migration-addresses) page for more details on where to find these IP addresses in the workflow. To permit traffic from these IP addresses to your database in GCP, select **Connections** from the navigation on the left. Under **Authorized networks**, click “**Add network**”. This will display an inline form for you to add a network. The name of the field is arbitrary, but the **Network** field should contain the IP address that needs access to your database. Click “**Done**” to add the new entry. Perform this step for each IP address for the selected region, then click “**Save**” to apply the settings.

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/AspOsmxsYasYOxA4/docs/images/assets/docs/imports/gcp-cloudsql-migration-guide/cloudsql-networking.png?fit=max&auto=format&n=AspOsmxsYasYOxA4&q=85&s=306bf5676a73e89c2da04bb62a6f053a" alt="The form to add a new authorized network in the GCP console." data-og-width="1448" width="1448" data-og-height="1556" height="1556" data-path="docs/images/assets/docs/imports/gcp-cloudsql-migration-guide/cloudsql-networking.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/AspOsmxsYasYOxA4/docs/images/assets/docs/imports/gcp-cloudsql-migration-guide/cloudsql-networking.png?w=280&fit=max&auto=format&n=AspOsmxsYasYOxA4&q=85&s=93b7f00da2fe783e178ad120d511369e 280w, https://mintcdn.com/planetscale-cad1a68a/AspOsmxsYasYOxA4/docs/images/assets/docs/imports/gcp-cloudsql-migration-guide/cloudsql-networking.png?w=560&fit=max&auto=format&n=AspOsmxsYasYOxA4&q=85&s=3dfb907738a537b395852911523bf521 560w, https://mintcdn.com/planetscale-cad1a68a/AspOsmxsYasYOxA4/docs/images/assets/docs/imports/gcp-cloudsql-migration-guide/cloudsql-networking.png?w=840&fit=max&auto=format&n=AspOsmxsYasYOxA4&q=85&s=925d61023753732ed109a189c112910d 840w, https://mintcdn.com/planetscale-cad1a68a/AspOsmxsYasYOxA4/docs/images/assets/docs/imports/gcp-cloudsql-migration-guide/cloudsql-networking.png?w=1100&fit=max&auto=format&n=AspOsmxsYasYOxA4&q=85&s=177d735a386200dd0ea9128e9fd51ace 1100w, https://mintcdn.com/planetscale-cad1a68a/AspOsmxsYasYOxA4/docs/images/assets/docs/imports/gcp-cloudsql-migration-guide/cloudsql-networking.png?w=1650&fit=max&auto=format&n=AspOsmxsYasYOxA4&q=85&s=1e5f688725d34724d7d643dc0bf58db6 1650w, https://mintcdn.com/planetscale-cad1a68a/AspOsmxsYasYOxA4/docs/images/assets/docs/imports/gcp-cloudsql-migration-guide/cloudsql-networking.png?w=2500&fit=max&auto=format&n=AspOsmxsYasYOxA4&q=85&s=12767ab87731d206cc1faa16f15a8e8e 2500w" />
</Frame>

## Configure MySQL server settings

Certain MySQL server settings may need to be changed before you can begin the import. The initial connection test will fail if these settings are not configured correctly.

* binlog\_expire\_logs\_seconds

To set a flag in your GCP console, go to your database's “**Overview**” page, select the “**Edit**” button, and then scroll down to the “**Flags**” section.

You want to select the “**binlog\_expire\_logs\_seconds**” flag and set it to `172800` seconds.

Make sure to select the “**Done**” button.

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/AspOsmxsYasYOxA4/docs/images/assets/docs/imports/gcp-cloudsql-migration-guide/cloudsql-set-flags.png?fit=max&auto=format&n=AspOsmxsYasYOxA4&q=85&s=3a395537ace05e3139646ece64609af9" alt="The form to set MySQL flags." data-og-width="1490" width="1490" data-og-height="1560" height="1560" data-path="docs/images/assets/docs/imports/gcp-cloudsql-migration-guide/cloudsql-set-flags.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/AspOsmxsYasYOxA4/docs/images/assets/docs/imports/gcp-cloudsql-migration-guide/cloudsql-set-flags.png?w=280&fit=max&auto=format&n=AspOsmxsYasYOxA4&q=85&s=885eb6f3f1b27646f0b3e6965146b9c9 280w, https://mintcdn.com/planetscale-cad1a68a/AspOsmxsYasYOxA4/docs/images/assets/docs/imports/gcp-cloudsql-migration-guide/cloudsql-set-flags.png?w=560&fit=max&auto=format&n=AspOsmxsYasYOxA4&q=85&s=0b234630cc0316a99a07e7312ed8f9e5 560w, https://mintcdn.com/planetscale-cad1a68a/AspOsmxsYasYOxA4/docs/images/assets/docs/imports/gcp-cloudsql-migration-guide/cloudsql-set-flags.png?w=840&fit=max&auto=format&n=AspOsmxsYasYOxA4&q=85&s=c7ea320059bd97e129dbfa38bbaf3a6a 840w, https://mintcdn.com/planetscale-cad1a68a/AspOsmxsYasYOxA4/docs/images/assets/docs/imports/gcp-cloudsql-migration-guide/cloudsql-set-flags.png?w=1100&fit=max&auto=format&n=AspOsmxsYasYOxA4&q=85&s=d1e56bfb9691564e8b485624eb25cf72 1100w, https://mintcdn.com/planetscale-cad1a68a/AspOsmxsYasYOxA4/docs/images/assets/docs/imports/gcp-cloudsql-migration-guide/cloudsql-set-flags.png?w=1650&fit=max&auto=format&n=AspOsmxsYasYOxA4&q=85&s=82f4102c710f8262f663eab4492bba87 1650w, https://mintcdn.com/planetscale-cad1a68a/AspOsmxsYasYOxA4/docs/images/assets/docs/imports/gcp-cloudsql-migration-guide/cloudsql-set-flags.png?w=2500&fit=max&auto=format&n=AspOsmxsYasYOxA4&q=85&s=c0660ba0016f3b040868861c3d17d516 2500w" />
</Frame>

* log\_bin

If `log_bin` is set to OFF you may need to [enable Point in Time Recovery (PITR)](https://cloud.google.com/sql/docs/mysql/backup-recovery/pitr#enablingpitr) from the GCP console to start binary logging.

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/AspOsmxsYasYOxA4/docs/images/assets/docs/imports/gcp-cloudsql-migration-guide/cloudsql-enable-pitr.png?fit=max&auto=format&n=AspOsmxsYasYOxA4&q=85&s=9b8b6493d1058801ce03636d3c05ec9e" alt="The form to set enable point in time recovery." data-og-width="2118" width="2118" data-og-height="1644" height="1644" data-path="docs/images/assets/docs/imports/gcp-cloudsql-migration-guide/cloudsql-enable-pitr.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/AspOsmxsYasYOxA4/docs/images/assets/docs/imports/gcp-cloudsql-migration-guide/cloudsql-enable-pitr.png?w=280&fit=max&auto=format&n=AspOsmxsYasYOxA4&q=85&s=8fe84b1b1f5c65b5ee7df83bdab3dc74 280w, https://mintcdn.com/planetscale-cad1a68a/AspOsmxsYasYOxA4/docs/images/assets/docs/imports/gcp-cloudsql-migration-guide/cloudsql-enable-pitr.png?w=560&fit=max&auto=format&n=AspOsmxsYasYOxA4&q=85&s=1142df9a5e2992ed95c68fa74ed24992 560w, https://mintcdn.com/planetscale-cad1a68a/AspOsmxsYasYOxA4/docs/images/assets/docs/imports/gcp-cloudsql-migration-guide/cloudsql-enable-pitr.png?w=840&fit=max&auto=format&n=AspOsmxsYasYOxA4&q=85&s=a9e64e02310fac0fdfa55f4b2f1d81c0 840w, https://mintcdn.com/planetscale-cad1a68a/AspOsmxsYasYOxA4/docs/images/assets/docs/imports/gcp-cloudsql-migration-guide/cloudsql-enable-pitr.png?w=1100&fit=max&auto=format&n=AspOsmxsYasYOxA4&q=85&s=a936663d41d864e5f65e8ae7dc93302b 1100w, https://mintcdn.com/planetscale-cad1a68a/AspOsmxsYasYOxA4/docs/images/assets/docs/imports/gcp-cloudsql-migration-guide/cloudsql-enable-pitr.png?w=1650&fit=max&auto=format&n=AspOsmxsYasYOxA4&q=85&s=091aae0d6079e5241f99a1279184617a 1650w, https://mintcdn.com/planetscale-cad1a68a/AspOsmxsYasYOxA4/docs/images/assets/docs/imports/gcp-cloudsql-migration-guide/cloudsql-enable-pitr.png?w=2500&fit=max&auto=format&n=AspOsmxsYasYOxA4&q=85&s=3d8be00078be6e4906b54d8767b7c488 2500w" />
</Frame>

## Importing your database

Now that your GCP Cloud SQL database is configured and ready, follow the [Database Imports guide](/docs/vitess/imports/database-imports) to complete your import.

When filling out the connection form in the import workflow, use the following information:

* **Host name** - Your GCP Cloud SQL public IP address (from Prerequisites)
* **Port** - 3306 (default for Cloud SQL)
* **Database name** - The exact database name to import
* **Username** - `migration_user`
* **Password** - The password you set for the migration user
* **SSL verification mode** - Select based on your Cloud SQL SSL configuration

The Database Imports guide will walk you through:

* Creating your PlanetScale database
* Connecting to your Cloud SQL database
* Validating your configuration
* Selecting tables to import
* Monitoring the import progress
* Switching traffic and completing the import

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt