# Source: https://planetscale.com/docs/vitess/imports/postgres-planetscale-migration-guide.md

# Postgres to PlanetScale for Vitess migration guide

<Warning>
  **PlanetScale now supports Postgres**. This guide is for migrating from Postgres to PlanetScale's Vitess product. You can still use these scripts if you would like to utilize [Vitess](/docs/vitess). If you prefer to stay on Postgres, refer to the [Postgres import guides](/docs/postgres/imports/postgres-imports).
</Warning>

This guide covers how to do an import directly between a Postgres source database and a PlanetScale for Vitess target.
For this, we will be using the [postgres-planetscale scripts](https://github.com/planetscale/migration-scripts).
This method of importing can be slow.
If you have a large database, you might consider trying [an alternative, faster approach](/docs/vitess/imports/postgres-mysql-planetscale-migration-guide).
You are encouraged to modify these scripts to suit your needs if need be.

## Methodology

The scripts in this guide leverage [AWS Database Migration Service](https://aws.amazon.com/dms/) to handle conversions between Postgres and MySQL types.
Even if you are migrating from a non-AWS Postgres provider, such as Neon or Supabase, you will still need an AWS account to perform the migration.

DMS acts as a middle-man between your Postgres source database and PlanetScale.
All of your data will pass through the DMS server which will handle type conversions before passing the data on to your PlanetScale database.
After the initial data copy, DMS will continue to replicate changes from your source to the target until you stop it.
It is up to you to determine how to handle the cut over between the two in your application.

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/postgres-planetscale-darkmode.png?fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=b25cdd0826775f1940fc1d157a6bee40" alt="Import data flow" data-og-width="2424" width="2424" data-og-height="812" height="812" data-path="docs/images/postgres-planetscale-darkmode.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/postgres-planetscale-darkmode.png?w=280&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=26c1636f243437e310fd800284ba7088 280w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/postgres-planetscale-darkmode.png?w=560&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=a18802bdeff9cf36d8a7f987dc8b3474 560w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/postgres-planetscale-darkmode.png?w=840&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=eeea225deca228b171f93baf9b38aedf 840w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/postgres-planetscale-darkmode.png?w=1100&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=cf047a3be7bc9ae7a442f5d66001ad03 1100w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/postgres-planetscale-darkmode.png?w=1650&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=cdfdadeabd55d6eb4d90e17eadbee5c2 1650w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/postgres-planetscale-darkmode.png?w=2500&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=5cc77a4e3e69cd2555465392fd1ceb36 2500w" />
</Frame>

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

### 2. Install the AWS CLI

The migration scripts we provide rely on [AWS Database Migration Service](https://aws.amazon.com/dms/).
To use the scripts, you need to download and install the [AWS CLI](https://aws.amazon.com/docs/cli/).
You will also need to authenticate into the AWS account that you would like to run the migration from.
This step is necessary, even if you are importing from a non-AWS Postgres provider.

Go ahead and download and install the AWS CLI.
On **MacOS**, you can run:

```
curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg"
sudo installer -pkg AWSCLIV2.pkg -target /
```

On **Linux**, you run:

```
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```

Full instructions can be found on the [AWS documentation](https://docs.aws.amazon.com/docs/cli/latest/userguide/getting-started-install.html).

### 3. Authenticate into AWS

After installing the CLI, you must authenticate into the AWS account that you intend to run the import scripts in.
There are several ways to authenticate.
You can find instructions in the [AWS documentation](https://docs.aws.amazon.com/docs/cli/v1/userguide/cli-chap-authentication.html).
We recommend you authenticate with [short-term credentials](https://docs.aws.amazon.com/docs/cli/v1/userguide/cli-authentication-short-term.html).
The authenticated account will need permissions to both create and modify DMS resources, security groups, and parameter groups.

### 4. Customizing import of large tables

If you have large tables that are in need of a [parallel import](https://aws.amazon.com/blogs/database/speed-up-database-migration-by-using-aws-dms-with-parallel-load-and-filter-options/), you should specify custom rules for these to give to DMS.

For example, perhaps we have a large table named `items` that contains 1 million rows.
We would like DMS to import this in parallel with multiple threads.
To configure this, create a json file named `custom-table-mappings.json` and place this in there:

```json expandable theme={null}
{
  "rules": [
    {
      "object-locator": {
        "schema-name": "public",
        "table-name": "items"
      },
      "parallel-load": {
        "boundaries": [
          ["250000"],
          ["500000"],
          ["750000"]
        ],
        "columns": ["item_id"],
        "type": "ranges"
      },
      "rule-id": "3",
      "rule-name": "parallel-load-settings",
      "rule-type": "table-settings"
    }
  ]
}
```

These rules will be used to tell DMS that it can load the table in 4 parallel threads.
It can load rows with `item_id` ranges 0-250k, 250k-500k, 500k-750k, and 750k+ in separate threads.

You can add multiple rules here if there are multiple large tables.
You do not need to specify custom rules for small tables.

If you use custom rules, ensure you pass this file to the `import.sh` script in the next step via `--table-mappings custom-table-mappings.json`.

Learn more about the options available to you here in the [AWS table mappings documentation](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TableMapping.html).

### 5. Begin the import

Check out the [migration-scripts](https://github.com/planetscale/migration-scripts) repository, and navigate to the `postgres-planetscale` directory.

```bash  theme={null}
git clone https://github.com/planetscale/migration-scripts
cd migration-scripts/docs/postgres-planetscale
```

Since these scripts will be running in your AWS account, it is important that you understand what the scripts are doing before executing them.
Before running, look through the scripts and confirm what they will be doing in your AWS account is acceptable to you and your organization.
At a high level, the `import.sh` script does the following:

<Steps>
  <Step>
    Creates a new DMS source and target using the credentials you provide
  </Step>

  <Step>
    Creates a DMS import instance (a server to handle the migration)
  </Step>

  <Step>
    Creates / modifies the subnets so the databases can communicate with DMS
  </Step>

  <Step>
    Sets up rules for how to handle the migration and how to map tables between the source and target
  </Step>

  <Step>
    Begins the DMS migration task to copy data between the two instances
  </Step>

  <Step>
    After initial data copy is complete, continues to replicate the data between the instances until you are ready to stop the task
  </Step>
</Steps>

If there are any concerns, you should modify the scripts to suit your needs.

If you are comfortable proceeding, the next step is to execute the `import.sh` script.
You will need to provide this with a unique identifier for this import, as well as the connection credentials for both the source Postgres database and the target PlanetScale database.

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
 sh import.sh --identifier "PGtoPSImport01" \
   --source "${PG_USER}:${PG_PASSWORD}@${PG_HOST}/${PG_DB}/${PG_SCHEMA}" \
   --target "${PS_USER}:${PS_PASSWORD}@${PS_HOST}/${PS_DB}"
```

You can choose whatever identifier you want in place of `PGtoPSImport01`.
The variables prefixed with `PG_` are for the Postgres source, and the ones prefixed with `PS_` are for the PlanetScale target.

Running the script like this will give you occasional log messages indicating which phase of the import process it is at.
If you want full debug mode, including each command the script executes, add the `--debug` flag:

```
 sh import.sh --identifier "PGtoPSImport01" \
   --source "${PG_USER}:${PG_PASSWORD}@${PG_HOST}/${PG_DB}/${PG_SCHEMA}" \
   --target "${PS_USER}:${PS_PASSWORD}@${PS_HOST}/${PS_DB}" \
   --debug
```

If you are running the script for the first time, we recommend using `--debug` in case you encounter any issues needing debugging.

### 6. Completing the import

The `import.sh` script can take upwards of 20 minutes to prepare all of the resources before even beginning the import.
After this, the time for the import itself varies widely depending on the size and load of your database.
You should monitor the progress of the migration by comparing row counts in PlanetScale to ones from the source.

Once the migration is complete, it is up to you to determine when you want to cut over your application to use PlanetScale as your primary database instead of the old Postgres source.
Before doing this, you should ensure all of your queries are updated to work properly with PlanetScale and do some performance testing.
If you encounter performance issues, you likely need to add indexes. Use [PlanetScale Query Insights](/docs/vitess/monitoring/query-insights) to discover and improve poor performing queries.

### 7. Cleaning up the import

When you have fully switched all traffic over to PlanetScale and are comfortable stopping the replication between Postgres and PlanetScale, you can use the `cleanup.sh` script to delete the DMS resources that `import.sh` created.
All you have to provide is the `--identifier` that you used when starting the import.

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