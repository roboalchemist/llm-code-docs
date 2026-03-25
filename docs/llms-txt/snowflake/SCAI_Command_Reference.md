# Source: https://docs.snowflake.com/en/migrations/snowconvert-docs/general/user-guide/snowconvert/command-line-interface/SCAI_Command_Reference.md

# SnowConvert AI (scai) Command Reference

This is the full command reference for the SnowConvert CLI.

## Table of Contents

* Quick Start
* Global Options
* Commands

  * scai init
  * scai project
  * scai connection
  * scai code
  * scai data
  * scai ai-convert
  * scai git
  * scai state
  * scai license
  * scai object-selector

## Quick Start

Basic workflow to get started

1. Create a project (use -c to set default Snowflake connection):

```bash
scai init -n <name> -l <language> -c <connection>
```

1. Add source code (E2E languages: SqlServer, Redshift):

```bash
scai code extract
```

1. Add source code (other languages):

```bash
scai code add -i <path>
```

1. Convert to Snowflake SQL:

```bash
scai code convert
```

## Global Options

| Option | Description |
| --- | --- |
| `-h, --help` | Show help message |
| `-v, --version` | Display version information |

## Commands

### scai init

Create a new migration project

#### `scai init`

Create a new migration project in the specified directory (or current directory if PATH is omitted).

**Usage:**

```bash
scai init [PATH] -l <LANGUAGE> [-n <NAME>] [-i <INPUT_PATH>] [-c <CONNECTION>]
```

**Prerequisites:**

* Target directory must not contain an existing project
* Valid source language must be specified

**Options:**

| Option | Description | Required | Default |
| --- | --- | --- | --- |
| `[PATH]` | Optional directory to create the project in. If omitted, uses the current directory. | No | - |
| `-n, --name <NAME>` | Project name. If omitted, defaults to the target folder name. | No | - |
| `-l, --source-language <LANGUAGE>` | Source language for the project | Yes | - |
| `-i, --input-code-path <PATH>` | Optional path to source code files to copy into the project’s Source folder during initialization | No | - |
| `--git-flow` | Enable git workflow automation for iterative conversions | No | `False` |
| `--baseline-branch <NAME>` | Name of the baseline branch for conversion results (requires –git-flow) | No | `baseline` |
| `-s, --state-management` | Enables state management for the project | No | `False` |
| `-c, --connection <NAME>` | Snowflake connection name to save as project default. Precedence: -c option > project connection > default TOML connection. | No | - |

**Examples:**

*Create a project in a new folder (recommended):*

```bash
scai init my-project -l Teradata
```

*Create a project in the current directory:*

```bash
scai init -l Teradata
```

*Create project with source code:*

```bash
scai init my-project -l Oracle -i /path/to/code
```

*Create project with a specific connection:*

```bash
scai init my-project -l Oracle -c my-snowflake-conn
```

### scai ai-convert

AI-powered code improvement and test generation

#### `scai ai-convert cancel`

Cancel a running AI code conversion job.

**Usage:**

```bash
scai ai-convert cancel [JOB_ID] [OPTIONS]
```

**Prerequisites:**

* A running job started with ‘scai ai-convert start’
* Snowflake connection (uses job’s connection if –connection not specified)

**Options:**

| Option | Description | Required | Default |
| --- | --- | --- | --- |
| `[JOB_ID]` | The job ID to cancel. If omitted, cancels the last started job. | No | - |
| `-c, --connection <NAME>` | Override the Snowflake connection. By default, uses the connection saved when the job was started. | No | - |

**Examples:**

*Cancel last job:*

```bash
scai ai-convert cancel
```

*Cancel specific job:*

```bash
scai ai-convert cancel JOB_20260112041123_XYZ
```

*Use different connection:*

```bash
scai ai-convert cancel -c other-snowflake
```

#### `scai ai-convert list`

List AI code conversion jobs for the current project.

**Usage:**

```bash
scai ai-convert list [OPTIONS]
```

**Prerequisites:**

* A migration project initialized with ‘scai init’
* Snowflake connection for refreshing job status

**Options:**

| Option | Description | Required | Default |
| --- | --- | --- | --- |
| `-l, --limit <N>` | Maximum number of jobs to display | No | `10` |
| `-a, --all` | Show all jobs (ignores limit) | No | - |
| `-c, --connection <NAME>` | Override the Snowflake connection for refreshing job status. By default, uses the connection saved when the job was started. | No | - |

**Examples:**

*List recent jobs:*

```bash
scai ai-convert list
```

*Show all jobs:*

```bash
scai ai-convert list --all
```

*Refresh with different connection:*

```bash
scai ai-convert list -c other-snowflake
```

#### `scai ai-convert start`

Start AI-powered code conversion on converted code.

**Usage:**

```bash
scai ai-convert start [OPTIONS]
```

**Prerequisites:**

* Code converted with ‘scai code convert’ (generates TopLevelCodeUnits report)
* Snowflake connection configured with ‘snow connection add’
* CREATE MIGRATION privilege granted on the Snowflake account
* A warehouse configured in the Snowflake connection
* Must accept AI disclaimers (interactive prompt or -y flag)

**Options:**

| Option | Description | Required | Default |
| --- | --- | --- | --- |
| `-c, --connection <NAME>` | Name of the Snowflake connection to use for AI code conversion | No | - |
| `-o, --objects <OBJECTS>` | Comma-separated list of object names to convert, or ‘all’ for all objects | No | `all` |
| `-i, --instructions <PATH>` | Path to instructions file with custom AI code conversion configuration | No | - |
| `-w, --watch` | Display job progress until completion (may take several minutes to hours depending on code size) | No | `False` |
| `-y, --accept-disclaimers` | Accept all AI code conversion disclaimers without prompting (required for non-interactive use) | No | `False` |

**Examples:**

*Start AI code conversion:*

```bash
scai ai-convert start
```

*Start and wait for completion:*

```bash
scai ai-convert start -w
```

*Convert specific objects:*

```bash
scai ai-convert start -o PROC1,PROC2
```

*Non-interactive (CI/CD):*

```bash
scai ai-convert start -y -w
```

*Source system verification:*

```bash
scai ai-convert start -i config/instructions.yml
```

#### `scai ai-convert status`

Check the status of an AI code conversion job.

**Usage:**

```bash
scai ai-convert status [JOB_ID] [OPTIONS]
```

**Prerequisites:**

* A job started with ‘scai ai-convert start’
* Snowflake connection (uses job’s connection if –connection not specified)

**Options:**

| Option | Description | Required | Default |
| --- | --- | --- | --- |
| `[JOB_ID]` | The job ID to check status for. If omitted, checks the last started job. | No | - |
| `-c, --connection <NAME>` | Override the Snowflake connection. By default, uses the connection saved when the job was started. | No | - |
| `-w, --watch` | Monitor job progress until completion. For finished jobs, forces a server-side refresh and downloads detailed results. | No | `False` |

**Examples:**

*Check last job status:*

```bash
scai ai-convert status
```

*Check specific job:*

```bash
scai ai-convert status JOB_20260112041123_XYZ
```

*Wait and download results:*

```bash
scai ai-convert status -w
```

*Use different connection:*

```bash
scai ai-convert status -c other-snowflake
```

### scai code

Code operations: extract, convert, add, deploy

#### `scai code add`

Add source code from an input path to the project’s Source folder.

**Usage:**

```bash
scai code add -i <INPUT_PATH>
```

**Prerequisites:**

* A migration project initialized with ‘scai init’
* source/ folder must be empty
* Input path must contain valid SQL source files

**Options:**

| Option | Description | Required | Default |
| --- | --- | --- | --- |
| `-i, --input-path <PATH>` | Path to the source code files to add to the project | Yes | - |

**Examples:**

*Add source code to project:*

```bash
scai code add -i /path/to/source/code
```

*Add code using full option name:*

```bash
scai code add --input-path ./my-sql-scripts
```

#### `scai code convert`

Transform source database code to Snowflake SQL.

**Usage:**

```bash
scai code convert [OPTIONS]
```

**Prerequisites:**

* A migration project initialized with ‘scai init’
* Source code in the ‘source/’ folder (from ‘scai code extract’, ‘scai code add’, or manual copy)

**Options:**

| Option | Description | Required | Default |
| --- | --- | --- | --- |
| `-h, --help` | Display all the conversion settings available for the specified source language | No | - |
| `-e, --etl-replatform-sources-path <PATH>` | Path to ETL replatform source files for cross-project code analysis. Must be provided for each conversion run. | No | - |
| `-p, --powerbi-repointing <PATH>` | Path to Power BI files for input repointing. Must be provided for each conversion run. | No | - |
| `-x, --show-ewis` | Show detailed EWI (Early Warning Issues) table instead of summary | No | - |
| `--context-path <PATH>` | Path to read migration context from. Defaults to .scai/conversion-context. Generated context is always written to .scai/conversion-context. | No | - |

**Examples:**

*Convert using project defaults:*

```bash
scai code convert
```

*Convert with custom context path:*

```bash
scai code convert --context-path /path/to/context
```

*Show all conversion settings for the project’s dialect:*

```bash
scai code convert --help
```

*Convert with custom schema:*

```bash
scai code convert --customschema MY_SCHEMA
```

*Convert with comment on missing dependencies:*

```bash
scai code convert --comments
```

*Convert with object renaming file:*

```bash
scai code convert --renamingfile /path/to/renaming.json
```

#### `scai code deploy`

Deploy converted SQL code to Snowflake.

**Usage:**

```bash
scai code deploy [OPTIONS]
```

**Prerequisites:**

* Converted code in ‘converted/Output/’ (from ‘scai code convert’)
* Snowflake connection configured (set with ‘scai init -c’ or project settings)
* Appropriate Snowflake privileges (CREATE TABLE, CREATE VIEW, etc.)

**Options:**

| Option | Description | Required | Default |
| --- | --- | --- | --- |
| `-c, --connection <NAME>` | The name of the Snowflake connection to use. Uses default if not specified. | No | - |
| `-d, --database <NAME>` | Target database name for deployment. Uses converted database name if not specified. | No | - |
| `-a, --all` | Deploy all successfully converted objects without selection prompt. | No | `False` |
| `-r, --retry <N>` | Number of retry attempts for failed object deployments. | No | `1` |
| `--continue-on-error` | Continue deploying remaining objects even if some fail. | No | `True` |

**Examples:**

*Deploy using default connection:*

```bash
scai code deploy
```

*Deploy all objects:*

```bash
scai code deploy --all
```

*Deploy with specific connection:*

```bash
scai code deploy --connection my-snowflake
```

#### `scai code extract`

Extract code from the source database.

**Usage:**

```bash
scai code extract [OPTIONS]
```

**Prerequisites:**

* A migration project initialized with ‘scai init’
* Source database connection configured (use ‘scai connection add-redshift’ or ‘scai connection add-sql-server’)
* Network access to the source database

**Options:**

| Option | Description | Required | Default |
| --- | --- | --- | --- |
| `-c, --connection <NAME>` | Name of the source connection to extract code from | No | - |
| `-s, --schema <SCHEMA>` | Schema name to extract code from | No | - |
| `-t, --object-type <TYPES>` | Object types to extract (comma-separated). E.g., TABLE,VIEW,PROCEDURE | No | - |

**Examples:**

*Extract tables from a schema:*

```bash
scai code extract --schema public --object-type TABLE
```

*Extract tables and views:*

```bash
scai code extract --object-type TABLE,VIEW
```

*Extract from all schemas:*

```bash
scai code extract
```

### scai connection

Manage source database connections (Redshift, SQL Server)

#### `scai connection add-redshift`

Add a new Redshift source database connection.

**Usage:**

```bash
scai connection add-redshift [OPTIONS]
```

**Prerequisites:**

* Network access to the Redshift cluster/serverless endpoint
* For IAM auth: AWS credentials configured (AWS CLI or environment variables)
* For standard auth: Username and password

**Options:**

| Option | Description | Required | Default |
| --- | --- | --- | --- |
| `-c, --connection <NAME>` | Name for this connection | No | - |
| `--auth <AUTH>` | Authentication method (iam-serverless, iam-provisioned-cluster, standard) | No | - |
| `--user <USER>` | Username | No | - |
| `--database <DATABASE>` | Database name | No | - |
| `--connection-timeout <SECONDS>` | Connection timeout in seconds | No | - |
| `--workgroup <NAME>` | Redshift Serverless workgroup name | No | - |
| `--cluster-id <ID>` | Redshift Provisioned Cluster ID | No | - |
| `--region <REGION>` | AWS region | No | - |
| `--access-key-id <KEY>` | AWS Access Key ID | No | - |
| `--secret-access-key <KEY>` | AWS Secret Access Key | No | - |
| `--host <HOST>` | Redshift host | No | - |
| `--port <PORT>` | Port number | No | - |
| `--password <PASSWORD>` | Password | No | - |

**Examples:**

*Add connection interactively (recommended):*

```bash
scai connection add-redshift
```

*IAM Serverless (inline):*

```bash
scai connection add-redshift --connection my-redshift --auth iam-serverless --workgroup my-workgroup --database mydb --region us-east-1
```

#### `scai connection add-sql-server`

Add a new SQL Server source database connection.

**Usage:**

```bash
scai connection add-sql-server [OPTIONS]
```

**Prerequisites:**

* Network access to the SQL Server instance
* For Windows auth: Valid domain credentials
* For standard auth: SQL Server username and password

**Options:**

| Option | Description | Required | Default |
| --- | --- | --- | --- |
| `-c, --connection <NAME>` | Name for this connection | No | - |
| `--auth <AUTH>` | Authentication method (windows, standard) | No | - |
| `--user <USER>` | Username | No | - |
| `--database <DATABASE>` | Database name | No | - |
| `--connection-timeout <SECONDS>` | Connection timeout in seconds | No | - |
| `--server-url <URL>` | SQL Server URL | No | - |
| `--port <PORT>` | Port number | No | - |
| `--password <PASSWORD>` | Password | No | - |
| `--trust-server-certificate` | Trust server certificate | No | - |
| `--encrypt` | Encrypt connection | No | - |

**Examples:**

*Add connection interactively (recommended):*

```bash
scai connection add-sql-server
```

*Windows Authentication:*

```bash
scai connection add-sql-server --connection my-sqlserver --auth windows --server-url localhost --database mydb
```

*Standard Authentication:*

```bash
scai connection add-sql-server --connection my-sqlserver --auth standard --server-url localhost --database mydb --username sa
```

#### `scai connection list`

List connections for a given source database.

**Usage:**

```bash
scai connection list [-l <LANGUAGE>]
```

**Options:**

| Option | Description | Required | Default |
| --- | --- | --- | --- |
| `-l, --source-language <LANGUAGE>` | Source language of the connection. If omitted, shows a summary of all connections. | No | - |

**Examples:**

*List all connections summary:*

```bash
scai connection list
```

*List Redshift connections:*

```bash
scai connection list -l redshift
```

*List SQL Server connections:*

```bash
scai connection list -l sqlserver
```

#### `scai connection set-default`

Set the default source connection for a database type.

**Usage:**

```bash
scai connection set-default -l <LANGUAGE> -c <CONNECTION>
```

**Prerequisites:**

* Connection already added with ‘scai connection add-redshift’ or ‘scai connection add-sql-server’

**Options:**

| Option | Description | Required | Default |
| --- | --- | --- | --- |
| `-l, --source-language <LANGUAGE>` | Database type of the connection | Yes | - |
| `-c, --connection <NAME>` | Name of the source connection to set as default | Yes | - |

**Examples:**

*Set default Redshift connection:*

```bash
scai connection set-default -l redshift --connection prod
```

*Set default SQL Server connection:*

```bash
scai connection set-default -l sqlserver --connection dev
```

#### `scai connection test`

Test a source database connection.

**Usage:**

```bash
scai connection test -l <LANGUAGE> [-c <CONNECTION>]
```

**Prerequisites:**

* Connection already configured
* Network access to the database

**Options:**

| Option | Description | Required | Default |
| --- | --- | --- | --- |
| `-l, --source-language <LANGUAGE>` | Source language of the connection. Supported languages: SqlServer and Redshift. | Yes | - |
| `-c, --connection <NAME>` | Name of the connection to test | No | - |

**Examples:**

*Test SQL Server connection:*

```bash
scai connection test -l sqlserver -c my-sqlserver
```

*Test Redshift connection:*

```bash
scai connection test -l redshift -c my-redshift
```

### scai data

Data operations: migrate, validate

#### `scai data migrate`

Migrate data from the source system into a Snowflake account.

**Usage:**

```bash
scai data migrate [OPTIONS]
```

**Prerequisites:**

* Code converted with ‘scai code convert’ (generates TopLevelCodeUnits report)
* Code deployed with ‘scai code deploy’ (creates target tables in Snowflake)
* Source database connection configured
* Snowflake connection configured with INSERT privileges
* If using –selector: A selector file (create with ‘scai object-selector create’)
* For Redshift: S3 Bucket, Snowflake Storage Integration, and External Stage configured

**Options:**

| Option | Description | Required | Default |
| --- | --- | --- | --- |
| `-c, --source-connection <NAME>` | Name of the source connection to extract data from. If not provided, the default connection will be used. | No | - |
| `-t, --target-connection <NAME>` | Name of the target connection to migrate data to. If not provided, the default connection will be used. | No | - |
| `-o, --selector <PATH>` | Name of the selector file to use for migration. If not provided, all tables from the TopLevelCodeUnits report will be migrated. | No | - |
| `-b, --bucket-uri <URI>` | (Redshift only) The S3 bucket URI where data will be staged (e.g., s3://my-bucket/path). | No | - |
| `--stage <STAGE_NAME>` | (Redshift only) The fully qualified name of the Snowflake stage used to load parquet files from the S3 bucket. (e.g., database.schema.stage_name). | No | - |
| `-i, --iam-role-arn <ARN>` | (Redshift only) The IAM role ARN to unload parquet files to the S3 bucket. | No | - |

**Examples:**

*Migrate all tables:*

```bash
scai data migrate --source-connection my-redshift --target-connection my-snowflake
```

*Migrate selected tables:*

```bash
scai data migrate --source-connection my-redshift --target-connection my-snowflake --selector my-selector.yml
```

**Important: Redshift Data Migration Considerations**

When migrating data from Amazon Redshift, you must ensure that the Snowflake stage properly connects to the AWS S3 bucket that you are using to unload the data. The stage must be configured with the correct Storage Integration and have the appropriate permissions to access the S3 bucket.

For detailed instructions on setting up the S3 bucket, configuring the stage, and specifying the data unloading IAM role ARN, see the [Migrate Amazon Redshift data](../../data-migration.md) section in the data migration guide.

#### `scai data validate`

Compare data between source and Snowflake to verify data integrity.

**Usage:**

```bash
scai data validate [OPTIONS]
```

**Prerequisites:**

* Source database connection configured
* Snowflake connection configured
* Tables must exist in both source and target databases

**Options:**

| Option | Description | Required | Default |
| --- | --- | --- | --- |
| `--source-connection <NAME>` | Name of the source connection to use (from the configured source connections). Uses default if not specified. | No | - |
| `--target-connection <NAME>` | Name of the Snowflake connection to use (from connections.toml). Uses default if not specified. | No | - |
| `-d, --target-database <NAME>` | Target Snowflake database for validation. Uses database from connection if not specified. | No | - |
| `-o, --selector <PATH>` | Name of the selector file to use for validation. If not provided, all tables from the TopLevelCodeUnits report will be validated. | No | - |
| `-m, --db-mapping <MAPPING>` | Database name mapping in format ‘source:target’. Can be specified multiple times for multiple mappings. | No | - |
| `-e, --schema-mapping <MAPPING>` | Schema name mapping in format ‘source:target’. Can be specified multiple times for multiple mappings. | No | - |

**Examples:**

*Validate all tables from report:*

```bash
scai data validate
```

*Validate with selector file:*

```bash
scai data validate --selector my-tables.yml
```

*With target database:*

```bash
scai data validate --target-database PROD_DB
```

*With name mappings:*

```bash
scai data validate --db-mapping "sourcedb:TARGETDB" --schema-mapping "dbo:PUBLIC"
```

*With explicit connections:*

```bash
scai data validate --source-connection my-sqlserver --target-connection my-snowflake
```

### scai git

Git workflow for iterative conversions

#### `scai git enable`

Enable Git workflow for iterative conversions.

**Usage:**

```bash
scai git enable [OPTIONS]
```

**Prerequisites:**

* A migration project initialized with ‘scai init’
* Git installed on the system

**Options:**

| Option | Description | Required | Default |
| --- | --- | --- | --- |
| `-b, --baseline-branch <NAME>` | Name of the baseline branch for conversion results | No | `baseline` |

**Examples:**

*Enable git workflow:*

```bash
scai git enable
```

*Enable with custom baseline branch:*

```bash
scai git enable --baseline-branch vendor
```

### scai license

Install offline license for air-gapped environments

#### `scai license install`

Install an offline license for running conversions without online activation.

**Usage:**

```bash
scai license install -p <LICENSE_PATH>
```

**Prerequisites:**

* A valid offline license file (.lic) from Snowflake

**Options:**

| Option | Description | Required | Default |
| --- | --- | --- | --- |
| `-p, --path <LICENSE_PATH>` | Path to the license file to install | Yes | - |

**Examples:**

*Install license:*

```bash
scai license install --path /path/to/license.lic
```

### scai object-selector

Create selector files for filtering objects

#### `scai object-selector create`

Create a selector file to filter objects for data migration.

**Usage:**

```bash
scai object-selector create [OPTIONS]
```

**Prerequisites:**

* Code converted with ‘scai code convert’ (generates TopLevelCodeUnits report)

**Options:**

| Option | Description | Required | Default |
| --- | --- | --- | --- |
| `-d, --database <NAME>` | Filter objects by source database name. | No | - |
| `-s, --schema <NAME>` | Filter objects by source schema name. | No | - |
| `-t, --type <TYPES>` | Filter objects by type (comma-separated, e.g., table,view,procedure). | No | - |
| `-n, --name <NAME>` | Label for the selector file (becomes ..yml), if not provided, it will be called object-selector..yml. | No | - |

**Examples:**

*Create selector file:*

```bash
scai object-selector create
```

*Create with custom output path:*

```bash
scai object-selector create -o custom-selector.yml
```

### scai project

View and manage project configuration

#### `scai project info`

Display project details including name, source language, and status.

**Usage:**

```bash
scai project info
```

**Prerequisites:**

* Must be run from within a migration project directory

**Examples:**

*Show current project details:*

```bash
scai project info
```

#### `scai project set-default-connection`

Set the default Snowflake connection for the current project.

**Usage:**

```bash
scai project set-default-connection -c <CONNECTION>
```

**Prerequisites:**

* A migration project initialized with ‘scai init’
* Snowflake connection available in connections.toml or config.toml

**Options:**

| Option | Description | Required | Default |
| --- | --- | --- | --- |
| `-c, --connection <NAME>` | Name of the Snowflake connection to set as the project default. | Yes | - |

**Examples:**

*Set project default connection:*

```bash
scai project set-default-connection -c my-snowflake
```

*Change to production connection:*

```bash
scai project set-default-connection -c prod-snowflake
```

### scai state

Track code unit state through migration stages

#### `scai state disable`

Disable state management for the project.

**Usage:**

```bash
scai state disable
```

**Prerequisites:**

* A migration project with state management enabled

**Examples:**

*Disable state management:*

```bash
scai state disable
```

#### `scai state enable`

Enable state management for the project.

**Usage:**

```bash
scai state enable
```

**Prerequisites:**

* A migration project initialized with ‘scai init’

**Examples:**

*Enable state management:*

```bash
scai state enable
```

#### `scai state status`

Show the current state of code units in the project.

**Usage:**

```bash
scai state status
```

**Prerequisites:**

* A migration project with state management enabled

**Examples:**

*Show current state:*

```bash
scai state status
```

---

*Generated: 2026-01-30 11:17:01*
