# Source: https://firebase.google.com/docs/data-connect/cli-reference.md.txt

<br />

TheFirebaseCLI is a tool that lets you to manage and configure Firebase products and services from the command line.

The CLI provides commands that can be used to perform a variety ofData Connecttasks, like creating a newData Connectproject, initializing a corresponding local working directory, setting up theData Connectemulator, listingData Connectresources, generating client SDKs and more.

## Setup commands

### AddData Connectto a Firebase project

#### firebase init

Use`firebase init`to set up a new local project configuration. This workflow creates or updates[Firebase configuration files](https://firebase.google.com/docs/data-connect/configuration-reference)in your directory.  

    firebase init

The`firebase init`flow guides you through setting up a service and database, and optionally installing theData Connectemulator and configuring generated SDKs.

#### Service and database setup

If you select`dataconnect`for product setup, the CLI prompts you for a new service name and location, and whether to link an existing Cloud SQL for PostgreSQL instance or create a new instance.

If an existing instance is linked, the CLI checks for compatible settings, such as IAM authentication and public IP addresses.
| **Note:** Provisioning a new Cloud SQL instance during the flow can take up to 15 minutes.
| **Note:** If you would like to use customer-managed encryption keys (CMEK) make sure you link an existing Cloud SQL database with CMEK.

#### Local Emulator Suitesetup

The CLI flow offers to set up emulators, including theData Connectemulator.

## Data Connectemulator commands

### Start theData Connectemulator

#### emulators:start/exec

    firebase emulators:start/exec

Use theLocal Emulator Suiteversion of theData Connectemulator in interactive mode with`start`or script-driven, non-interactive mode with`exec`.

### Export and import local PostgreSQL data

To support local prototyping and testing, and continuous integration, you can export the data stored in a local database instance and import it between development iterations and test runs.

Exports are stored as snapshots of your local PostgreSQL database.

Data Connectoffers three approaches to export/import:

- Automatic export/import configured in your`firebase.json`to provide snapshot backups on emulator shutdown and startup
- Manual export/import using the CLI
- Manual export/import using the VS Code extension interface

#### Automatic export and import configured in your`firebase.json`

To backup data between development sessions, specify an automatic backup location during the`firebase init`sequence. This location is stored in your`firebase.json`in the`emulators.dataconnect.dataDir`field. Any data changes you make will automatically be saved here between emulator runs, so it is useful during local testing and exploration.

#### Manual export:`emulators:export`and`emulators:start/exec --import`

While theData Connectemulator is running, in a separate terminal, run the`firebase emulators:export`command to save a snapshot of your data. Then, you can start the emulator from that snapshot by using the`--import`flag.  

    # Export data from local emulator from a separate terminal
    firebase emulators:export --only dataconnect \<export_directory\>

    # Import data from local directory, here using emulators:exec
    firebase emulators:exec ./<your-test-script>.sh --only dataconnect --import \<import_directory\>

| **Note:** An import directory you specify during manual import with the CLI`emulators:start --import`flag takes precedence over the default backup directory configured in`firebase.json`.
| **Note:** Manual import and export is a good way to seed tests with data in CI/CD.

#### Manual export/import: VS Code extension

In the VS Code extension UI, while the emulator is running, use the**Export emulator data** button to export data to export the current database contents. The default export location is the`exportedData`directory at the root of your project directory.
| **Note:** To modify this export location, before you start the emulator using the extension, click the**Configure emulator**link.

You can import this data using the CLI, as described in the previous section. You can also import this data before starting the emulator through VS Code by clicking the**Configure emulator** link and setting**Import Path**.

## Schema and connector management commands

This section contains CLI reference information for commands you use to manage schemas and connectors.
| **Note:** You can limit access to PostgreSQL databases by granting more or less elevated roles to individual users. Behavior of the following commands may vary depending on the role the current user has. See[Cloud SQL management commands](https://firebase.google.com/docs/data-connect/cli-reference#cloudsql-management-commands).

For how-to use cases and recommended practices related to these commands, see the[schema and connector management guide](https://firebase.google.com/docs/data-connect/manage-schemas-and-connectors).

### Deploy schemas and connectors

#### deploy

    firebase deploy

This command deploys resources for Data Connect services indexed in[firebase.json](https://firebase.google.com/docs/data-connect/configuration-reference). A[schema migration](https://firebase.google.com/docs/data-connect/cli-reference#manage-cloudsql-schemas)and[connector update](https://firebase.google.com/docs/data-connect/cli-reference#update-connectors)are performed if necessary.

|   **Command**   |                                                                               **Description**                                                                               ||
|-----------------|-------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| firebase deploy | **Flag**                                  | **Description**                                                                                                                  |
| firebase deploy | ---only dataconnect                       | Deploy schemas and connectors for all Data Connect services for this project, but don't deploy other Firebase product resources. |
| firebase deploy | ---only dataconnect:serviceId             | Deploy schema and connectors for specified Data Connect service.                                                                 |
| firebase deploy | ---only dataconnect:serviceId:connectorId | Deploy a single connector for specified Data Connect service.                                                                    |
| firebase deploy | ---only dataconnect:serviceId:schema      | Deploy the schema for the specified Data Connect service.                                                                        |

With the`---only`flags, you can pass comma-separated values to deploy any subset of resources you want.  

    firebase deploy --only dataconnect:service1:schema,dataconnect:service2

### List Data Connect services, schemas and connectors

#### dataconnect:services:list

    firebase dataconnect:services:list

This command prints out basic info about the services, schemas, and connectors deployed on a project.

### Compare and migrate SQL schemas

When you run[`firebase deploy`](https://firebase.google.com/docs/data-connect/cli-reference#deploy-schema), the CLI performs a SQL schema comparison before deploying updates. You can also perform the comparison and update directly with a set of`dataconnect:sql`commands.

#### dataconnect:sql:diff

    firebase dataconnect:sql:diff

This command compares local schema for a service with the current schema of the corresponding Cloud SQL database. It prints out the commands that would be run to migrate the database to your new schema.

|          **Command**          |                                            **Description**                                             ||
|-------------------------------|--------------------|------------------------------------------------------------------------------------|
| firebase dataconnect:sql:diff | **Flag/Parameter** | **Description**                                                                    |
| firebase dataconnect:sql:diff | serviceId          | Specify the service. If omitted, print the diff for all services in firebase.json. |
| firebase dataconnect:sql:diff |

#### dataconnect:sql:migrate

    firebase dataconnect:sql:migrate

This command applies local schema changes to a service's Cloud SQL database.

When you set up a new localData Connectproject, with the default`dataconnect.yaml`file, the behavior of the`dataconnect:sql:migrate`command is to prompt you for any required changes, and then prompt for any optional changes, before executing the changes. You can modify this behavior to always include or ignore optional changes by updating your`dataconnect.yaml`configuration, as discussed in[migrate a schema in strict or compatible mode](https://firebase.google.com/docs/data-connect/cli-reference#migrate-compat-strict-modes)

In interactive environments, the CLI displays each migration SQL statement (and whether it is destructive) and prompts for the changes you want to apply. Passing the`--force`flag is equivalent to accepting all prompts.

In noninteractive environments:

- Without`--force`, only non-destructive changes are made. If there are destructive changes, the CLI aborts with no changes made.
- With`--force`, all changes are made. If this includes any destructive changes, they are printed and you are prompted whether you want to continue, unless the`--force`flag is provided.

|           **Command**            |                                                      **Description**                                                       ||
|----------------------------------|-----------|-----------------------------------------------------------------------------------------------------------------|
| firebase dataconnect:sql:migrate | **Flag**  | **Description**                                                                                                 |
| firebase dataconnect:sql:migrate | serviceId | Migrate the database for the specified service. The serviceId is inferred if your project has only one service. |
| firebase dataconnect:sql:migrate | ---force  | Automatically accept prompts.                                                                                   |

As with other`--only`flags, you can provide multiple services separated by commas.

#### Migrate a schema in strict or compatible mode

Data Connectschema migrations have two different schema validation modes:*strict* and*compatible* . Strict mode validation requires that the database schema exactly match the application schema before the application schema can be deployed. Compatible mode validation requires that the database schema be*compatible*with the application schema, meaning elements in your database that are not used by your application schema are left unmodified.

These schema validation modes and best practices for schema migration are covered in the[schema and connector management guide](https://firebase.google.com/docs/data-connect/manage-schemas-and-connectors)

The validation mode is defined using the`schemaValidation`key in your`dataconnect.yaml`file. If`schemaValidation`is unspecified, the CLI applies compatible changes and prompts you before executing any strict changes. See the[configuration reference](https://firebase.google.com/docs/data-connect/configuration-reference).

### Manage changes to connectors

When you run[`firebase deploy`](https://firebase.google.com/docs/data-connect/cli-reference#deploy-schema), the CLI initiates an update of the applicable connectors. The CLI analyzes changes to each connector and issues a set of assessment messages with respect to connector changes that may cause unexpected behavior (messages are warning-level) or breakages (messages are breaking-level) in previous versions of client code.
| **Note:** The following lists are not exhaustive. Refer to the CLI output messages for warnings and errors applicable to your connector.

|                    Impact assessment                     |                                                                                                                                                                              Scenario                                                                                                                                                                               |
|----------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Warning-level (wire compatible, may change behavior)     | - Removing a nullable field from a query without a`@retired`annotation.                                                                                                                                                                                                                                                                                             |
| Breaking-level (wire incompatible, may break clients)    | - Changing a nullable variable to non-null without a default value. - Changing the data type of a field to be something JSON-compatible (e.g.`Int`to`Float`). - Changing a non-null column to nullable. - Removing a nullable variable without a`@retired`annotation. - Removing a non-null variable with a default value without a`@retired`annotation.            |
| Breaking-level (wire incompatible,**will**break clients) | - Removing an operation without a`@retired`annotation. - Removing a non-null field from a query without a`@retired`annotation. - Adding a non-null variable without a default value. - Changing the data type of a field to something incompatible (e.g.`String`to`Int`). - Removing a non-null variable without a default value and without a`@retired`annotation. |

In interactive environments, the CLI displays each connector assessment and prompts for the changes you want to apply. Passing the`--force`flag is equivalent to accepting all assessments.

In non-interactive environments:

- if only warning-level assessments (possible behavior changes) occur, all connectors will be deployed and warnings will be logged to terminal.
- if any breaking-level assessments occur, no connectors will be deployed and warnings will be logged to terminal. You can override with the`--force`flag.

### Audit authorization code

Data Connecthelps you audit your authorization strategy by analyzing your connector code when you deploy to the server using`firebase deploy`from theFirebaseCLI. You can use this audit to help you review your codebase.

When you deploy your connectors, the CLI will output assessments for existing, modified and new operation code in your connector.

For modified and new operations, the CLI issues warnings and prompts you for confirmation when you use certain access levels in your new operations, or when you modify existing operations to use those access levels.
| **Note:** Insecure operation warnings are suppressed if you annotate the`@auth`directive in the operation with the[`insecureReason`argument](https://firebase.google.com/docs/data-connect/authorization-and-security#insecureReasons).

Warnings and prompts always occur for:

- `PUBLIC`

And, warnings and prompts occur on the following access levels when you*don't augment them* with filters using`auth.uid`:

- `USER`
- `USER_ANON`
- `USER_EMAIL_VERIFIED`

For more information about authorization, refer to the[authorization and attestation guide](https://firebase.google.com/docs/data-connect/authorization-and-security).

## SDK commands

### Generate SDKs

#### dataconnect:sdk:generate

    firebase dataconnect:sdk:generate

This command generates the typed SDKs declared in[connector.yaml](https://firebase.google.com/docs/data-connect/configuration-reference#connector.yaml-configuration).

Also see the guides for working with[the web SDKs](https://firebase.google.com/docs/data-connect/web-sdk),[the Android SDKs](https://firebase.google.com/docs/data-connect/android-sdk)and[the iOS SDKs](https://firebase.google.com/docs/data-connect/ios-sdk).

|            **Command**            |                                                                                                                                   **Description**                                                                                                                                   ||
|-----------------------------------|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| firebase dataconnect:sdk:generate | **Flag**                     | **Description**                                                                                                                                                                                                                                       |
| firebase dataconnect:sdk:generate | ---watch                     | Keeps the process running and generates new SDKs whenever you save changes to your schema and connector GQL files. If generation fails, errors will be printed to stdout, the generated code won't be changed, and the command will continue running. |
| firebase dataconnect:sdk:generate | ---only connectorId:platform | Only generate SDKs for a single platform and single connector.                                                                                                                                                                                        |
| firebase dataconnect:sdk:generate |

<br />

With the`--only`flags, you can pass comma-separated values.  

    firebase dataconnect:sdk:generate ---only connector1, connector1:kotlin

## Cloud SQL management commands

### Grant SQL roles for Cloud SQL

Data Connectoperates on top of your own PostgreSQL instance hosted on Cloud SQL. SQL role commands help you manage permissions on your database tables.

#### dataconnect:sql:setup

    firebase dataconnect:sql:setup

This command configures initial, global permissions to tables in your database.

The default database provisioning and management flow assumes your project uses a new (greenfield) database, and when you invoke`firebase deploy`,Data Connectwill display database schema changes to be made and performs any migrations after you approve. If this is your preferred flow,`dataconnect:sql:setup`prompts you to grant permissions including`superuser`schema ownerships.

For existing (brownfield) databases, you may have your own workflow for migrating schemas and want to maintain schema ownership yourself. If this is your preferred flow, make sure to**decline** at the`dataconnect:sql:setup`prompt for whetherData Connectshould handle SQL migrations for you. As a result of declining,Data Connectwill only take`read`and`write`access to your database tables, but schema ownerships and migrations will remain your responsibility.

For more discussion and use cases, see[Manage services and databases](https://firebase.google.com/docs/data-connect/manage-services-and-databases#integrate-existing-databases).

#### dataconnect:sql:grant

    firebase dataconnect:sql:grant

In some cases, you might want to access your database directly to query or update the data generated by yourData Connectapps. To do this, you will need to grant one of the roles defined in this section to the needed user or service account.

For details on the granted roles, see[PostgreSQL user roles](https://www.postgresql.org/docs/current/user-manag.html).
| **Note:** In addition to setting PostgreSQL roles with theFirebaseCLI, you will need to assign the IAM role`roles/cloudsql.client`. See the[guide for managing services and databases](https://firebase.google.com/docs/data-connect/manage-services-and-databases#sql-roles-cloudsql-iam).

|   Role    |                 SQL Role                 |                                                                                                                          Permissions                                                                                                                           |                                                                                                                                                                  Usage                                                                                                                                                                   |                                        Grantable                                         |
|-----------|------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| reader    | `firebasereader_<db_name>_<schema_name>` | Read-only access to the database. Can perform`SELECT`operations on all tables within the specified schema.                                                                                                                                                     | Ideal for users or services requiring data retrieval but not modification.                                                                                                                                                                                                                                                               | Yes                                                                                      |
| writer    | `firebasewriter_<db_name>_<schema_name>` | Read and write access to the database. Can perform`SELECT`,`INSERT`,`UPDATE`,`DELETE`, and`TRUNCATE`operations on all tables within the schema.                                                                                                                | Suitable for users or services that need to modify data within the database.                                                                                                                                                                                                                                                             | Yes                                                                                      |
| owner     | `firebaseowner_<db_name>_<schema_name>`  | Schema owner. Has all privileges on all tables and sequences in the schema.                                                                                                                                                                                    | This role, in combination of the IAM`roles/cloudsql.client`role, grants permission to performing migration on the database. For example, when calling`firebase dataconnect:sql:migrate`.                                                                                                                                                 | Yes                                                                                      |
| superuser | `cloudsqlsuperuser`                      | Built-in superuser role with full privileges on the database. In addition to owner permissions, it can create schemas, drop schemas, install extensions, and perform any other administrative tasks. Accessed in the CLI by logging in as "firebasesuperuser". | Required for installing extensions, creating the initial schema, and granting any of the grantable SQL roles to other users. If a non-admin user needs superuser privileges, the migration will fail and prompt the user to ask the database administrator (i.e., a user with`roles/cloudsql.admin`) to run the privileged SQL commands. | Granted to users with`roles/cloudsql.admin`and can't be directly granted fromFirebaseCLI |

| **Note:** These SQL roles are distinct from Cloud SQL IAM roles. IAM roles control who can access a database. SQL roles control which operations you can perform with such access, and which tables you can modify.

|          **Command**           |                                   **Description**                                    ||
|--------------------------------|---------------------------|-----------------------------------------------------------|
| firebase dataconnect:sql:grant | **Flag/Parameter**        | **Description**                                           |
| firebase dataconnect:sql:grant | -R, --role role           | The SQL role to grant, one of: owner, writer, or reader.  |
| firebase dataconnect:sql:grant | -E, --email email_address | Email for a user or service account to grant the role to. |

## Global options

The following global options apply to all commands:

- `--json`switches CLI output to JSON for parsing by other tools.
- `--noninteractive`and`--interactive`override, as needed, automatic detection of non-TTY environments.