# Source: https://planetscale.com/docs/vitess/imports/postgres-mysql-planetscale-migration-guide.md

# Postgres to MySQL to PlanetScale migration guide

<Warning>
  **PlanetScale now supports Postgres**. This guide is for migrating from Postgres to PlanetScale's Vitess product. You can still use these scripts if you would like to utilize [Vitess](/docs/vitess). If you prefer to stay on Postgres, refer to the [Postgres import guides](/docs/postgres/imports/postgres-imports).
</Warning>

This guide covers how to import a Postgres database to PlanetScale for Vitess using an intermediate Aurora MySQL database.
For this, we will be using the [postgres-mysql-planetscale scripts](https://github.com/planetscale/migration-scripts/tree/main/docs/postgres-mysql-planetscale).
This technique is good for larger databases that need a fast import, but requires an intermediate MySQL instance.
If you have a smaller database or don't mind a slower import, consider [an alternate approach](/docs/vitess/imports/postgres-planetscale-migration-guide).
You are encouraged to modify these scripts to suit your needs if need be.

## Methodology

The scripts in this guide leverage [AWS Database Migration Service](https://aws.amazon.com/dms/) to handle conversions between Postgres and MySQL types.
It also creates a new Aurora MySQL database to use as a go-between for Postgres and PlanetScale.
Even if you are migrating from a non-AWS Postgres provider, such as Neon or Supabase, you will still need an AWS account to perform the migration.

When using this script, your data will take the following path:

* Data flows from your Postgres source into DMS
* DMS does necessary type conversions and copies the data into the Aurora MySQL database
* Using the PlanetScale import tool, your data will flow from Aurora MySQL into your destination PlanetScale database
* After the initial copy, changes will continue to flow form Postgres, to Aurora MySQL, to PlanetScale so that your data stays in sync, even if the migration takes several hours or days.

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/postgres-mysql-planetscale-darkmode.png?fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=71ccc0d17313bf965ab3310e1ebb9bfd" alt="Import data flow" data-og-width="3202" width="3202" data-og-height="812" height="812" data-path="docs/images/postgres-mysql-planetscale-darkmode.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/postgres-mysql-planetscale-darkmode.png?w=280&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=5cf87871f42ed88da517e046924076fd 280w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/postgres-mysql-planetscale-darkmode.png?w=560&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=9edd29457a5c3f4b8b236e09f7b6cb5e 560w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/postgres-mysql-planetscale-darkmode.png?w=840&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=286980bf36c1e5d597c6509c30feca2d 840w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/postgres-mysql-planetscale-darkmode.png?w=1100&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=cef7752d2771c5b74c295a292a82c909 1100w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/postgres-mysql-planetscale-darkmode.png?w=1650&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=c2012d7f89d1d38f13b2292fe908e35a 1650w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/postgres-mysql-planetscale-darkmode.png?w=2500&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=f6d63c0f8d48c05a908288bb0c597b15 2500w" />
</Frame>

It is up to you to determine how to handle the cut over between the two in your application.

### Prerequisites

* An AWS account
* An empty PlanetScale database as the target
* The [AWS CLI](https://aws.amazon.com/docs/cli/)

<Warning>
  These import scripts create and modify resources in your AWS account.
  Before executing, you should read through the scripts to ensure you are comfortable with the actions they will take.
  You will also be billed in AWS for the resources it creates, which include:

  * 1 DMS replication task
  * 1 DMS replication instance
  * 1 DMS replication subnet group
  * 2 DMS endpoints
  * 1 Aurora MySQL database
</Warning>

## Importing a database

### 1. Prepare Postgres for migration

Before beginning a migration to PlanetScale, you should ensure the following flags are set on your Postgres database.

| flag name                  | flag value |
| -------------------------- | ---------- |
| logical\_replication       | 1          |
| shared\_preload\_libraries | pglogical  |

Given the variety of Postgres options and versions, there may be additional flags that you will need to adjust to make the import work.
If you encounter errors when using the script below, it may be caused by other Postgres options not shown here.
You can either update your Postgres configuration based on the error you see, or [contact support](https://planetscale.com/contact?initial=support) for additional assistance.

<Warning>
  You should not make any schema changes to the source database during an import.
</Warning>

### 2. Create an EC2 instance

These scripts are designed to be run from an EC2 instance on the same account that you will authenticate into.
Create one, and then log in to the instance.
Ensure that both Postgres and MySQL are installed:

```
sudo apt update
sudo apt install postgresql
sudo apt install mysql-server
```

### 3. Install the AWS CLI

The migration scripts we provide rely on [AWS Database Migration Service](https://aws.amazon.com/dms/).
To use the scripts, you will need to download and install the [AWS CLI](https://aws.amazon.com/docs/cli/).
You will also need to authenticate into the AWS account that you would like to run the migration from.
This step is necessary, even if you are importing from a non-AWS Postgres provider.

Go ahead and download and install the AWS CLI on the EC2 instance you created in the last step.

For example, on **Ubuntu**, you would run:

```
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```

Full instructions can be found on the [AWS documentation](https://docs.aws.amazon.com/docs/cli/latest/userguide/getting-started-install.html).

### 4. Authenticate into AWS

After installing the CLI, you must authenticate into the AWS account that you intend to run the import scripts in.
There are several ways to authenticate.
You can find instructions in the [AWS documentation](https://docs.aws.amazon.com/docs/cli/v1/userguide/cli-chap-authentication.html).
We recommend you authenticate with [short-term credentials](https://docs.aws.amazon.com/docs/cli/v1/userguide/cli-authentication-short-term.html).

The authenticated account will need permissions to both create and modify DMS resources, RDS / Aurora databases, security groups, and parameter groups

### 5. Prepare the import

Check out the [migration-scripts](https://github.com/planetscale/migration-scripts) repository, and navigate to the `postgres-mysql-planetscale` directory.

```
git clone https://github.com/planetscale/migration-scripts
cd migration-scripts/docs/postgres-mysql-planetscale
```

Since these scripts will be running in your AWS account, it is important that you understand what the scripts are doing before executing them.
Before running, look through the scripts and confirm what they will be doing in your AWS account is acceptable to you and your organization.
At a high level, this script does the following:

1. Creates a DMS source using the Postgres credentials you provide
2. Creates a new Aurora MySQL database and sets it as the target for the DMS import
3. Creates a DMS import instance (a server to handle the migration)
4. Sets up rules for how to handle the migration

If there are any concerns, you should modify the scripts to suit your needs.

<Warning>
  This script prepares for a migration between your postgres source and a new MySQL database. The MySQL database will be accessible from all IPs.

  If you want a tighter security configuration, modify the script to make the database only accessible from the [required PlanetScale IPs](/docs/vitess/imports/import-tool-migration-addresses).
</Warning>

If you are comfortable proceeding, the next step is to execute the `prepare.sh` script.
You will need to provide this with a unique identifier for this import, as well as the connection credentials for the source Postgres database.

<Note>
  If you are importing from **Supabase**, the scripts will not work with a transaction pooler or session pooler connection.
  You must use a direct connection over ipv4.
  In order to use this, you must be on the pro plan or greater, and pay for the ipv4 connection upgrade.
  After doing so, use the direct connection credentials and host when using `import.sh`.

  If you are importing from **Neon**, You must use `--tls` mode when importing from Neon.
  This sets `SSL_MODE="require"` on the connection, a necessity for Neon.
</Note>

Here's an example of executing this:

```
 sh prepare.sh --identifier "PGtoPSImport01" \
   --source "${PG_USER}:${PG_PASSWORD}@${PG_HOST}/${PG_DB}/${PG_SCHEMA}" \
   --ips "us-east-1"
```

You can choose whatever identifier you want in place of `PGtoPSImport01`.
The variables prefixed with `PG_` are for the Postgres source.

Running the script like this will give you occasional log messages indicating which phase of the import process it is at.
If you want full debug mode, including each command the script executes, add the `--debug` flag:

```
 sh prepare.sh --identifier "PGtoPSImport01" \
   --source "${PG_USER}:${PG_PASSWORD}@${PG_HOST}/${PG_DB}/${PG_SCHEMA}" \
   --ips "us-east-1" \
   --debug
```

This script can take upwards of 15 minutes, particularly because of the step to set up the DMS import server.

When this script completes, it will provide the connection information for the MySQL instance and instructions for next steps.
For example:

```
======================================================================================
SETUP COMPLETED SUCCESSFULLY
======================================================================================

MySQL RDS instance information:
Hostname: TARGET_HOSTNAME
Database: TARGET_DATABASE

Admin user:
Username: TARGET_USERNAME
Password: TARGET_PASSWORD

Migration user (for PlanetScale):
Username: migration_user
Password: MIGRATION_PASSWORD

======================================================================================
NEXT STEPS:
======================================================================================
1. Log into your new MySQL instance using the credentials above
2. Set up your schema manually
3. Once your schema is ready, run the start.sh script with the same identifier:
   sh start.sh --identifier \"$IDENTIFIER\"
```

Notably, this step does not actually begin the migration, but sets up the necessary AWS and DMS resources.

<Note>
  If your database is on a PlanetScale cloud or managed plan, you will need to manually provide your IP addresses.
  For this, use `--ips "manual"` and then give the script a comma-separated list of IPs as instructed by the script.
</Note>

### 6. Copy your schema

We have configured these scripts so that they do not automatically copy the schema from Postgres to MySQL.
This is intentional, as DMS sometimes does not make good choices for how to convert Postgres types to MySQL.
Therefore, we leave it up to you to copy the schema before we begin the migration via `import.sh`.

There are several ways you can do this, but one option is to use `pg_dump` to get your schema, convert to MySQL types / syntax, the apply it to the MySQL target.
First, you'd run a `pg_dump` command:

```
PGPASSWORD=${PG_PASSWORD} pg_dump -h ${PG_HOST} -U ${PG_USERNAME} ${PG_DATABASE} --schema-only --format=p > schema.sql
```

Next, modify `schema.sql`.
Remove all excessive lines from the dump, and update all column types to use ones supported by MySQL.

Finally, apply this schema to a new database in the MySQL target created by the `prepare.sh` script:

```
echo "CREATE DATABASE ${MYSQL_DATABASE}" | mysql -u ${MYSQL_USER} -p${MYSQL_PASSWORD} -h${MYSQL_HOST}
cat schema.sql | mysql -u ${MYSQL_USER} -p${MYSQL_PASSWORD} -h${MYSQL_HOST} ${MYSQL_DATABASE}
```

Then, log in to the MySQL instance to confirm the schema was applied correctly.

### 7. Migration from Postgres to Aurora MySQL

Next, we need to run `start.sh`.
This initiates the migration between the Postgres source and the Aurora MySQL target.
To start, just run:

```
start.sh --identifier "PGtoPSImport01"
```

You can monitor the progress of the migration by comparing row counts between the source and target database.
The initial data copy may range from several minutes to several hours depending on the size of your database.
After the initial copy, data changes to your Postgres database will replicate to Aurora MySQL.
You do not need to connect to the Aurora MySQL database form your application.
We are only using it as a temporary holding-place while moving into PlanetScale.

### 8. The PlanetScale import tool

To get your data into PlanetScale, we will use the import tool to migrate the data from the Aurora MySQL instance created in the previous steps into PlanetScale.
Log into PlanetScale, select your organization, click "New database", and then "Import database."

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/WcazQYbZzMHxCEvC/docs/vitess/imports/planetscale-new-import.png?fit=max&auto=format&n=WcazQYbZzMHxCEvC&q=85&s=fe88a5f1091b7c879fb4d77b32e07896" alt="PlanetScale new database via import" data-og-width="3024" width="3024" data-og-height="1122" height="1122" data-path="docs/vitess/imports/planetscale-new-import.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/WcazQYbZzMHxCEvC/docs/vitess/imports/planetscale-new-import.png?w=280&fit=max&auto=format&n=WcazQYbZzMHxCEvC&q=85&s=9454f709043320c12ee7c47de0fe35e0 280w, https://mintcdn.com/planetscale-cad1a68a/WcazQYbZzMHxCEvC/docs/vitess/imports/planetscale-new-import.png?w=560&fit=max&auto=format&n=WcazQYbZzMHxCEvC&q=85&s=93930359cfe642324ab2028bc66aa2bf 560w, https://mintcdn.com/planetscale-cad1a68a/WcazQYbZzMHxCEvC/docs/vitess/imports/planetscale-new-import.png?w=840&fit=max&auto=format&n=WcazQYbZzMHxCEvC&q=85&s=970c3f819892fa890474c805b8c4845e 840w, https://mintcdn.com/planetscale-cad1a68a/WcazQYbZzMHxCEvC/docs/vitess/imports/planetscale-new-import.png?w=1100&fit=max&auto=format&n=WcazQYbZzMHxCEvC&q=85&s=9bc27a2d4a0480657a371f0fe3256946 1100w, https://mintcdn.com/planetscale-cad1a68a/WcazQYbZzMHxCEvC/docs/vitess/imports/planetscale-new-import.png?w=1650&fit=max&auto=format&n=WcazQYbZzMHxCEvC&q=85&s=ee730466e894993347d2244dfd24b6db 1650w, https://mintcdn.com/planetscale-cad1a68a/WcazQYbZzMHxCEvC/docs/vitess/imports/planetscale-new-import.png?w=2500&fit=max&auto=format&n=WcazQYbZzMHxCEvC&q=85&s=6b5e4ef8555c7fbe8b55fa77711f7624 2500w" />
</Frame>

Enter the name of your database and choose the type and size of database you want to import to.
For large imports, we recommend using Metal for improved import speed.

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/WcazQYbZzMHxCEvC/docs/vitess/imports/planetscale-database-name-type.png?fit=max&auto=format&n=WcazQYbZzMHxCEvC&q=85&s=ddefc55b4d0a83e3ae17ec6ecfd6db80" alt="PlanetScale set database name and type for import" data-og-width="3024" width="3024" data-og-height="1420" height="1420" data-path="docs/vitess/imports/planetscale-database-name-type.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/WcazQYbZzMHxCEvC/docs/vitess/imports/planetscale-database-name-type.png?w=280&fit=max&auto=format&n=WcazQYbZzMHxCEvC&q=85&s=75aafab8dd0de6c1ab2f2f1dc50b62d4 280w, https://mintcdn.com/planetscale-cad1a68a/WcazQYbZzMHxCEvC/docs/vitess/imports/planetscale-database-name-type.png?w=560&fit=max&auto=format&n=WcazQYbZzMHxCEvC&q=85&s=166d7836aee7b6bf2fb69c259c6cf46b 560w, https://mintcdn.com/planetscale-cad1a68a/WcazQYbZzMHxCEvC/docs/vitess/imports/planetscale-database-name-type.png?w=840&fit=max&auto=format&n=WcazQYbZzMHxCEvC&q=85&s=28da7624c7708827c8ac51d259ad9939 840w, https://mintcdn.com/planetscale-cad1a68a/WcazQYbZzMHxCEvC/docs/vitess/imports/planetscale-database-name-type.png?w=1100&fit=max&auto=format&n=WcazQYbZzMHxCEvC&q=85&s=074e106fb9b5190ef4a90f00c863ba5f 1100w, https://mintcdn.com/planetscale-cad1a68a/WcazQYbZzMHxCEvC/docs/vitess/imports/planetscale-database-name-type.png?w=1650&fit=max&auto=format&n=WcazQYbZzMHxCEvC&q=85&s=48617a29b8c6fb0ca265439664f9aae0 1650w, https://mintcdn.com/planetscale-cad1a68a/WcazQYbZzMHxCEvC/docs/vitess/imports/planetscale-database-name-type.png?w=2500&fit=max&auto=format&n=WcazQYbZzMHxCEvC&q=85&s=f6c04c1364af971f698318893e610d72 2500w" />
</Frame>

Scroll down and you will see a section to add the connection information for the database to import.
Enter all of the credentials that the script printed out, and use the username and password for the `migration_user`.

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/WcazQYbZzMHxCEvC/docs/vitess/imports/planetscale-import-connection-info.png?fit=max&auto=format&n=WcazQYbZzMHxCEvC&q=85&s=2527223b990f6afbe197d8d9009d1f39" alt="PlanetScale import connection info" data-og-width="2060" width="2060" data-og-height="1774" height="1774" data-path="docs/vitess/imports/planetscale-import-connection-info.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/WcazQYbZzMHxCEvC/docs/vitess/imports/planetscale-import-connection-info.png?w=280&fit=max&auto=format&n=WcazQYbZzMHxCEvC&q=85&s=c5c97e0a08ad16cffc6a87bcdc1a15e7 280w, https://mintcdn.com/planetscale-cad1a68a/WcazQYbZzMHxCEvC/docs/vitess/imports/planetscale-import-connection-info.png?w=560&fit=max&auto=format&n=WcazQYbZzMHxCEvC&q=85&s=7738ecfb50a3c40713416a7817dc3fec 560w, https://mintcdn.com/planetscale-cad1a68a/WcazQYbZzMHxCEvC/docs/vitess/imports/planetscale-import-connection-info.png?w=840&fit=max&auto=format&n=WcazQYbZzMHxCEvC&q=85&s=c4006d7433de6480cf200916ddb86d09 840w, https://mintcdn.com/planetscale-cad1a68a/WcazQYbZzMHxCEvC/docs/vitess/imports/planetscale-import-connection-info.png?w=1100&fit=max&auto=format&n=WcazQYbZzMHxCEvC&q=85&s=8f9dab2f67ddada6b78610eac6c03e03 1100w, https://mintcdn.com/planetscale-cad1a68a/WcazQYbZzMHxCEvC/docs/vitess/imports/planetscale-import-connection-info.png?w=1650&fit=max&auto=format&n=WcazQYbZzMHxCEvC&q=85&s=84d0a0210f0e1c3009f7cd2415e488c0 1650w, https://mintcdn.com/planetscale-cad1a68a/WcazQYbZzMHxCEvC/docs/vitess/imports/planetscale-import-connection-info.png?w=2500&fit=max&auto=format&n=WcazQYbZzMHxCEvC&q=85&s=b47519543b34689ac98cee61ace94ee5 2500w" />
</Frame>

Click "Connect to Database."
If you encounter any errors at this step, look carefully at the error message and address any connection or schema issues as needed.
When the import is ready, click "Begin import."

### 9. Complete the import

This full import flow not only copies data, but does continuous replication of traffic from Postgres, to DMS, to Aurora MySQL, and finally to PlanetScale.
Replication between these continues until you stop the DMS task using `cleanup.sh` and complete the PlanetScale import flow.

It is up to you to determine how you want to cut over your application to use PlanetScale as your primary database instead of the old Postgres source.
Before doing this, you should ensure all of your queries and/or your ORM are updated to work properly with PlanetScale.
We also recommend doing some performance testing, and adding indexes if you encounter slow queries.

### 10. Clean up import

After you have switched all of your traffic over to PlanetScale and are comfortable wrapping up the import, you can clean up the resources that the script created.
This includes the DMS migration instance, the Aurora database, and the DMS source / targets.

<Warning>
  Do not run this until you are absolutely sure you no longer need the migration set up.
</Warning>

To clean up the resources, you can run:

```
sh cleanup.sh --identifier "PGtoPSImport01"
```

We recommend double checking that all of the resources were properly cleaned up in your AWS console after running this.

## Resolving errors

We have designed these scripts to run as generally as possible and have tested them on a variety of platforms.
Even so, you may encounter errors for a variety of reasons.

In some cases, the `aws` command that fails will produce a useful error message in the script output, which you can take action on as needed.

If the script is able to set up all of the resources without error but the import is not working, we recommend you take a look at the migration task logs.
You can view and search through these in the AWS web console.

Log in to the web console, and go to the AWS DMS service page.
In the sidebar, click on "Database migration tasks."

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/WcazQYbZzMHxCEvC/docs/vitess/imports/aws-dms.png?fit=max&auto=format&n=WcazQYbZzMHxCEvC&q=85&s=043d6ed57996bee3e7dea3d8ddbc9742" alt="AWS DMS landing page" data-og-width="3010" width="3010" data-og-height="1720" height="1720" data-path="docs/vitess/imports/aws-dms.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/WcazQYbZzMHxCEvC/docs/vitess/imports/aws-dms.png?w=280&fit=max&auto=format&n=WcazQYbZzMHxCEvC&q=85&s=95afa3e1bd99ef86e4b73c1442169c8c 280w, https://mintcdn.com/planetscale-cad1a68a/WcazQYbZzMHxCEvC/docs/vitess/imports/aws-dms.png?w=560&fit=max&auto=format&n=WcazQYbZzMHxCEvC&q=85&s=f671f6018c7d8063d0d5b4550c8db3ce 560w, https://mintcdn.com/planetscale-cad1a68a/WcazQYbZzMHxCEvC/docs/vitess/imports/aws-dms.png?w=840&fit=max&auto=format&n=WcazQYbZzMHxCEvC&q=85&s=ea9137d816fdcb1a09f536e47f872380 840w, https://mintcdn.com/planetscale-cad1a68a/WcazQYbZzMHxCEvC/docs/vitess/imports/aws-dms.png?w=1100&fit=max&auto=format&n=WcazQYbZzMHxCEvC&q=85&s=6fd3fd5b3f498ce3d5a9836f3dc20b2d 1100w, https://mintcdn.com/planetscale-cad1a68a/WcazQYbZzMHxCEvC/docs/vitess/imports/aws-dms.png?w=1650&fit=max&auto=format&n=WcazQYbZzMHxCEvC&q=85&s=a741b789aa76433d82e188c939359f0d 1650w, https://mintcdn.com/planetscale-cad1a68a/WcazQYbZzMHxCEvC/docs/vitess/imports/aws-dms.png?w=2500&fit=max&auto=format&n=WcazQYbZzMHxCEvC&q=85&s=7bd3276128a63bab08844441c8894786 2500w" />
</Frame>

You should see a migration task in the list with a name that corresponds to the identifier you chose.

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/WcazQYbZzMHxCEvC/docs/vitess/imports/aws-dms-migration-tasks.png?fit=max&auto=format&n=WcazQYbZzMHxCEvC&q=85&s=6cb6b624de6db0acc2477e58394d287f" alt="AWS DMS migration tasks" data-og-width="3012" width="3012" data-og-height="1722" height="1722" data-path="docs/vitess/imports/aws-dms-migration-tasks.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/WcazQYbZzMHxCEvC/docs/vitess/imports/aws-dms-migration-tasks.png?w=280&fit=max&auto=format&n=WcazQYbZzMHxCEvC&q=85&s=0bbd50cd5f87541036c2e2a746ed70cc 280w, https://mintcdn.com/planetscale-cad1a68a/WcazQYbZzMHxCEvC/docs/vitess/imports/aws-dms-migration-tasks.png?w=560&fit=max&auto=format&n=WcazQYbZzMHxCEvC&q=85&s=de1724f34c7f6e8b957e1c565732f12c 560w, https://mintcdn.com/planetscale-cad1a68a/WcazQYbZzMHxCEvC/docs/vitess/imports/aws-dms-migration-tasks.png?w=840&fit=max&auto=format&n=WcazQYbZzMHxCEvC&q=85&s=faa4d773b55caf3852874b0f637e3a46 840w, https://mintcdn.com/planetscale-cad1a68a/WcazQYbZzMHxCEvC/docs/vitess/imports/aws-dms-migration-tasks.png?w=1100&fit=max&auto=format&n=WcazQYbZzMHxCEvC&q=85&s=b9562e40782af7958bb9ef005f1bac64 1100w, https://mintcdn.com/planetscale-cad1a68a/WcazQYbZzMHxCEvC/docs/vitess/imports/aws-dms-migration-tasks.png?w=1650&fit=max&auto=format&n=WcazQYbZzMHxCEvC&q=85&s=414626fcf29d15ef77c1ec79d2a9a1d3 1650w, https://mintcdn.com/planetscale-cad1a68a/WcazQYbZzMHxCEvC/docs/vitess/imports/aws-dms-migration-tasks.png?w=2500&fit=max&auto=format&n=WcazQYbZzMHxCEvC&q=85&s=30a316341d98c6a3d29cd44e4da2f78b 2500w" />
</Frame>

Click on the migration task, and then click "View logs" in the top right corner.

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/WcazQYbZzMHxCEvC/docs/vitess/imports/aws-dms-migration-task-choice.png?fit=max&auto=format&n=WcazQYbZzMHxCEvC&q=85&s=94c5ea0c4959a1ff036648e4c6ad11b3" alt="AWS DMS migration task choice" data-og-width="3012" width="3012" data-og-height="1722" height="1722" data-path="docs/vitess/imports/aws-dms-migration-task-choice.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/WcazQYbZzMHxCEvC/docs/vitess/imports/aws-dms-migration-task-choice.png?w=280&fit=max&auto=format&n=WcazQYbZzMHxCEvC&q=85&s=701b8f700944ec49040a3f9d5e8e4152 280w, https://mintcdn.com/planetscale-cad1a68a/WcazQYbZzMHxCEvC/docs/vitess/imports/aws-dms-migration-task-choice.png?w=560&fit=max&auto=format&n=WcazQYbZzMHxCEvC&q=85&s=9cc94346aeb525cef62bb320d479cffb 560w, https://mintcdn.com/planetscale-cad1a68a/WcazQYbZzMHxCEvC/docs/vitess/imports/aws-dms-migration-task-choice.png?w=840&fit=max&auto=format&n=WcazQYbZzMHxCEvC&q=85&s=1554029b5d2b36a39af3669ee20fd25d 840w, https://mintcdn.com/planetscale-cad1a68a/WcazQYbZzMHxCEvC/docs/vitess/imports/aws-dms-migration-task-choice.png?w=1100&fit=max&auto=format&n=WcazQYbZzMHxCEvC&q=85&s=778b453f5b222c43e07bfc9676a676da 1100w, https://mintcdn.com/planetscale-cad1a68a/WcazQYbZzMHxCEvC/docs/vitess/imports/aws-dms-migration-task-choice.png?w=1650&fit=max&auto=format&n=WcazQYbZzMHxCEvC&q=85&s=28d11f55c053f78fb5c6c1f79df96535 1650w, https://mintcdn.com/planetscale-cad1a68a/WcazQYbZzMHxCEvC/docs/vitess/imports/aws-dms-migration-task-choice.png?w=2500&fit=max&auto=format&n=WcazQYbZzMHxCEvC&q=85&s=08d87c32dbebaea640a9166863238018 2500w" />
</Frame>

This will bring you to your CloudWatch logs for this replication task, and you can search through it for error and warning messages to help you pinpoint the issue.

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/WcazQYbZzMHxCEvC/docs/vitess/imports/aws-dms-migration-task-logs.png?fit=max&auto=format&n=WcazQYbZzMHxCEvC&q=85&s=41502e80d17eba6b2952ebdfebc96163" alt="AWS DMS migration task logs" data-og-width="2334" width="2334" data-og-height="1722" height="1722" data-path="docs/vitess/imports/aws-dms-migration-task-logs.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/WcazQYbZzMHxCEvC/docs/vitess/imports/aws-dms-migration-task-logs.png?w=280&fit=max&auto=format&n=WcazQYbZzMHxCEvC&q=85&s=1f1b5b436c39ca2e400e7656fb460e80 280w, https://mintcdn.com/planetscale-cad1a68a/WcazQYbZzMHxCEvC/docs/vitess/imports/aws-dms-migration-task-logs.png?w=560&fit=max&auto=format&n=WcazQYbZzMHxCEvC&q=85&s=2fc493aa0b2c4e384b94fa760d19885d 560w, https://mintcdn.com/planetscale-cad1a68a/WcazQYbZzMHxCEvC/docs/vitess/imports/aws-dms-migration-task-logs.png?w=840&fit=max&auto=format&n=WcazQYbZzMHxCEvC&q=85&s=e8dba2bb51359b4830a7619a8f6809fd 840w, https://mintcdn.com/planetscale-cad1a68a/WcazQYbZzMHxCEvC/docs/vitess/imports/aws-dms-migration-task-logs.png?w=1100&fit=max&auto=format&n=WcazQYbZzMHxCEvC&q=85&s=75c6a5949c6f71b936029e9ff976f77c 1100w, https://mintcdn.com/planetscale-cad1a68a/WcazQYbZzMHxCEvC/docs/vitess/imports/aws-dms-migration-task-logs.png?w=1650&fit=max&auto=format&n=WcazQYbZzMHxCEvC&q=85&s=77d458d7cd04a304df982c048e462c6f 1650w, https://mintcdn.com/planetscale-cad1a68a/WcazQYbZzMHxCEvC/docs/vitess/imports/aws-dms-migration-task-logs.png?w=2500&fit=max&auto=format&n=WcazQYbZzMHxCEvC&q=85&s=cea6b9ce7879057d21803d05e926f18e 2500w" />
</Frame>

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt