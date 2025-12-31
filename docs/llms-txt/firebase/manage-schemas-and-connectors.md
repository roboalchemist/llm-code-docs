# Source: https://firebase.google.com/docs/data-connect/manage-schemas-and-connectors.md.txt

<br />

AFirebase Data Connectservice has three main components:

- An underlying PostgreSQL**database** with its own**SQL schema**
- aData Connect**application schema** (declared in your`.gql`files)
- a number of**connectors** (declared in your`.gql`files, configured in`connector.yaml`files).

The SQL schema is the source of truth for your data, theData Connectschema is how your connectors can see that data, and the connectors declare the APIs that your clients can use to access that data.

When you deploy yourData Connectservice with the CLI, you will migrate your SQL schema, then update yourData Connectschema, then update each of your connectors.
| **Note:** Deploying and managing client code you develop with generated SDKs is covered in the SDK guides ([Android](https://firebase.google.com/docs/data-connect/android-sdk),[web](https://firebase.google.com/docs/data-connect/web-sdk),[iOS](https://firebase.google.com/docs/data-connect/ios-sdk), and[Flutter](https://firebase.google.com/docs/data-connect/flutter-sdk)).

## Important deployment concepts

To fully understand deployment, it's important to note key concepts about schemas and connectors.

### Schema deployments

Deployment of aData Connectschema affects the SQL schema for your Cloud SQL database.Data Connecthelps you*migrate*your schemas during deployment, whether you're working with a new database or need to non-destructively adapt an existing database.

Data Connectschema migrations have two different schema validation modes:*strict* and*compatible*.

- Strict mode validation requires that the database schema*exactly* match the application schema before the application schema can be updated. Any tables or columns that are not used in yourData Connectschema will be deleted from the database.

- Compatible mode validation requires that the database schema be*compatible*with the application schema before the application schema can be updated; any additional changes that drop schemas, tables or columns are optional.

  Compatible means that schema migrations only affect tables and columns referenced in your application schema. Elements in your database that are not used by your application schema are left unmodified. Therefore, after deployment, your database may contain unused:
  - Schemas
  - Tables
  - Columns

| **Note:** By default, tooling that handles migration will apply compatible mode changes automatically and then prompt you for optional strict mode changes. You can adjust this behavior as discussed in[migrate database schemas](https://firebase.google.com/docs/data-connect/manage-schemas-and-connectors#migrate-schemas-manually).

### Connector deployments

Data Connectqueries and mutations are not submitted by client code and executed on the server. Instead, when deployed, theseData Connectoperations are stored on the server, likeCloud Functions. This means deployment may break existing users.

Data Connectintegrates analysis of breaking changes in your connector updates into theFirebaseCLI.

The CLI analyzes changes to each connector with respect to your schema, and issues a set of assessment messages with respect to connector changes that might*alter client behavior* (messages are warning-level) or**might or will break**(messages are breaking-level) previous versions of client code.

For example:

- Connector changes that might alter client behavior include removing a nullable field from a query without a`@retired`schema annotation.
- Connector changes that might or will break clients include changing a nullable operation variable to non-null without a default value, or changing the data type of a field to something incompatible (e.g.`String`to`Int`).

A more extensive list of warning-level and breaking-level scenarios is given in the[CLI reference guide](https://firebase.google.com/docs/data-connect/cli-reference#update-connectors).

## Follow the deployment workflow

You can work on aData Connectproject both in a local project directory and in theFirebaseconsole.

A recommended deployment flow involves:

1. Listing currently-deployed**schemas and connectors** with`firebase dataconnect:services:list`.
2. Managing any**schema updates** .
   1. Check for SQL schema differences between your Cloud SQL database and local Data Connect schema with`firebase dataconnect:sql:diff`.
   2. If needed, perform SQL schema migration with`dataconnect:sql:migrate`.
3. Performing**schema and connect deployments** by running`firebase deploy`, for either just your schema, just your connectors, or combinations of resources.

## Deploy and manageData Connectresources

It's a good idea to verify production resources before performing deployments.  

    firebase dataconnect:services:list

When working in a local project directory, you'll generally use the`firebase deploy`command to deploy your schema and connectors into production, with interactive feedback.

Using any`deploy`command, the`--only dataconnect`flag lets you to separateData Connectdeployments from other products in your project.

### Normal deployment

    firebase deploy --only dataconnect

In this normal deployment, theFirebaseCLI attempts to deploy your schema and connectors.
| **Note:** Data Connectimposes a 100kB limit on schema source files and connector source files. Avoid including extraneous or unused files in your schema or connector deployments to prevent hitting this limit.

It validates that the new schema does not breaking any existing connectors. Follow[best practices](https://firebase.google.com/docs/data-connect/manage-schemas-and-connectors#best-practices)when making breaking changes.

It also verifies that the SQL schema is already migrated before updating theData Connectschema. If not, it automatically prompts you through any necessary steps to[migrate schemas](https://firebase.google.com/docs/data-connect/manage-schemas-and-connectors#migrate-schemas-manually).

### `--force`flag deployment

    firebase deploy --only dataconnect --force

If neither the connector or SQL schema validations are of concern, you can re-run the command with`--force`to ignore them.

The`--force`deploy still checks if the SQL schema matches theData Connectschema, warns of incompatibility, and prompts.

### Deploy selected resources

To deploy with more granular control, use the`--only`flag with the`serviceId`argument. To deploy only schema changes for a particular service:  

    firebase deploy --only dataconnect:serviceId:schema

You can also deploy all resources for a specified connector and service.  

    firebase deploy --only dataconnect:serviceId:connectorId

Finally, you can deploy the schema and all connectors for a single service.  

    firebase deploy --only dataconnect:serviceId

### Roll back a deployment

To perform a manual rollback, check out a previous version of your code and deploy it. If the original deployment included destructive breaking changes, you may not be able to fully recover any data deleted.

## Migrate database schemas

If you're prototyping rapidly, experimenting with schemas, and know your schema changes are destructive, you can plan on usingData Connecttools to verify the changes and supervise how the updates are carried out.
| **Tip:** Follow our recommended best practices for working with[new databases](https://firebase.google.com/docs/data-connect/manage-schemas-and-connectors#new-databases-recommendations)and[existing databases](https://firebase.google.com/docs/data-connect/manage-schemas-and-connectors#existing-databases-recommendations).

### Diff SQL schema changes

You can verify changes:  

    firebase dataconnect:sql:diff

You can pass a comma-separated list of services.

The command compares local schema for a service with the current schema of the corresponding Cloud SQL database. If there is a difference, it prints out the SQL commands that would be run to fix that difference

### Apply changes

When you're satisfied and ready to deploy changes to the schema Cloud SQL instance, issue the`firebase dataconnect:sql:migrate`command. You'll be prompted to approve changes.  

    firebase dataconnect:sql:migrate [serviceId]

In interactive environments, SQL migration statements and action prompts are displayed.

### Migrate in strict or compatible mode

In a brand new project, the default[schema validation mode](https://firebase.google.com/docs/data-connect/manage-schemas-and-connectors#schema-deployments)applies. The behavior of the`migrate`command is to apply all database schema changes that are required by your application schema, then prompt you to approve optional operations that drop schemas, tables or columns to force your database schema to exactly match your application schema.

You can adjust this behavior by modifying your`dataconnect.yaml`file. Uncomment the`schemaValidation`key, and declare`COMPATIBLE`so that only required changes are applied in migrations.  

    schemaValidation: "COMPATIBLE"

Or set the behavior to`STRICT`so that all schema changes are applied and your database schema is forced to match your application schema.  

    schemaValidation: "STRICT"

See the[Data ConnectCLI reference for more information](https://firebase.google.com/docs/data-connect/cli-reference#manage-cloudsql-schemas).

## Update connectors

When you run`firebase deploy`, the CLI initiates an update of the applicable connectors and issues applicable warning-level (may impact client behavior) and breaking-level (possibly or certainly breaking) assessment messages.

### Manage connector updates with the CLI

The CLI has slightly different behavior in interactive mode and non-interactive mode.

As you might expect, in interactive mode, the CLI prompts you to accept all messages. You can override and force connector deployment with the`--force`flag.  

    # Prompts for acceptance for any warning-level or breaking-level changes prior
    # to deploying connectors.
    firebase deploy --only dataconnect
    # Will deploy connectors without prompting.
    firebase deploy --only dataconnect --force

In non-interactive mode, the CLI will deploy your connector as long as there are no breaking-level assessments. Otherwise, your script will exit with a log of breaking changes. You can override and deploy by setting the`--force`flag.  

    # Will deploy connectors with warning-level changes. If any breaking changes
    # are present, the deploy will fail and output any breaking changes
    firebase deploy --only dataconnect --non-interactive
    # Will deploy the connectors from the previous step, if the same issues are present.
    firebase deploy --only dataconnect --non-interactive --force

For more information, see the[CLI reference guide](https://firebase.google.com/docs/data-connect/cli-reference#update-connectors).

## Best practices for managing schemas and connectors

Firebase recommends some practices to follow in yourData Connectprojects.

### Minimize breaking changes

- Firebase recommends keeping yourData Connectschema and connector files in source control.
- Avoid breaking changes when possible. Some common examples of breaking changes include:
  - Removing a field from your schema
  - Making a nullable field in your schema nonnullable (ie`Int`-\>`Int!`)
  - Renaming a field in your schema.
- If you do need to remove a field from your schema, consider splitting it into a few deployments to minimize impact:
  - First, remove any references to the field in your connectors, and deploy the change.
  - Next, update your apps to use newly generated SDKs.
  - Finally, remove the field in your schema`.gql`file, migrate your SQL schema, and deploy once more.

### Use strict mode when working with new databases

If you are usingData Connectwith a new database and actively developing your application schema, and you want to ensure your database schema stays exactly in line with your application schema, you can specify`schemaValidation: "STRICT"`in your`dataconnect.yaml`.

This will ensure optional changes are applied as well.

### Use compatible mode when you have production data in your database

If you are making changes to a database that contains production data, we recommend you execute your schema migrations in compatible mode, to ensure existing data is not dropped. You can specify`schemaValidation: "COMPATIBLE"`in your`dataconnect.yaml`.

In compatible mode, only required schema migration changes are applied to your database.

- `DROP SCHEMA`,`DROP TABLE`, and`DROP COLUMN`are considered optional statements and will not be generated for your plan, even if your database schema contains schemas, tables, or columns not defined in your application schema.
- If your database table contains a non-null column that is not included in your application schema, the`NOT NULL`constraint will be removed, so that data can still be added to the table with your defined connectors.

## What's next?

- Deploying and managing client code you develop with generated SDKs are covered in the guides for[Android](https://firebase.google.com/docs/data-connect/android-sdk),[iOS](https://firebase.google.com/docs/data-connect/ios-sdk),[web](https://firebase.google.com/docs/data-connect/web-sdk), and[Flutter](https://firebase.google.com/docs/data-connect/flutter-sdk).
- For more information about deployment tooling, review the[Data ConnectCLI reference](https://firebase.google.com/docs/data-connect/cli-reference)and[Data Connectconfiguration file reference](https://firebase.google.com/docs/data-connect/configuration-reference).