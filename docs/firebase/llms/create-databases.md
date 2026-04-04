# Source: https://firebase.google.com/docs/firestore/enterprise/create-databases.md.txt

<br />

<br />

|--------------------------------------------------------|
| *Relevant to Cloud Firestore Enterprise edition only.* |

<br />

This page describes how to create, update, and delete Cloud Firestore with MongoDB compatibility databases. You can create multipleCloud Firestoredatabases per project. You can use multiple databases to set up production and testing environments, to isolate customer data, and for data regionalization.

## Free tier usage

Cloud Firestoreoffers[free tier](https://firebase.google.com/docs/firestore/enterprise/quotas)that lets you get started at no cost.

The free tier applies to only oneCloud Firestoredatabase per project. The first database that is created in a project without a free tier database will get the free tier. If the database with the free tier applied is deleted, the next database created will receive the free tier.

## Before you begin

You must complete the following before creating a database:

1. If you haven't already, create a Firebase project: In the[Firebaseconsole](https://console.firebase.google.com/), click**Add project** , then follow the on-screen instructions to create a Firebase project or to add Firebase services to an existingGoogle Cloudproject.

2. Assign appropriate Identity and Access Management roles as described in the next section.

### Required roles

To create and manage databases, you need the`Owner`or`Datastore Owner`Identity and Access Management role. These roles grant the required permissions.

#### Required permissions

To manage databases, you need the following permissions:

- Create a database:`datastore.databases.create`
- Read database configuration:`datastore.databases.getMetadata`
- Configure a database:`datastore.databases.update`
- Delete a database:`datastore.databases.delete`
- Clone a database:`datastore.databases.clone`

## Create a database

To create a Cloud Firestore with MongoDB compatibility database, use one of the following methods:  

##### Firebaseconsole

1. In theFirebaseconsole, go to the**Firestore Database**page.

   [Go to Firestore Database](https://console.firebase.google.com/project/_/firestore/databases/-default-/data/)
2. Click**Create Database**.
3. Select**Enterprise edition** . Click**Next**.
4. Enter a Database ID.
5. Select a location for your database.
6. Configure your database where you select a mode.
7. Click**Create**.

##### Firebase CLI

```scdoc
firebase firestore:databases:create --edition EDITION DATABASE_ID \
--location=LOCATION
```

##### gcloud CLI

Use the[`gcloud firestore databases create`](https://cloud.google.com/sdk/gcloud/reference/firestore/databases/create)command and set`--edition=enterprise`.  

```scdoc
gcloud firestore databases create \
--database=DATABASE_ID \
--location=LOCATION \
--edition=enterprise
```

Replace the following:

- <var translate="no">DATABASE_ID</var>: a[valid database ID](https://firebase.google.com/docs/firestore/enterprise/create-databases#database_id).
- <var translate="no">LOCATION</var>: the name of a[Cloud Firestore with MongoDB compatibility multi-region or region](https://firebase.google.com/docs/firestore/enterprise/locations#types).

To enable deletion protection, add the`--delete-protection`flag. You cannot delete a database with deletion protection enabled until you disable this setting. This setting is disabled by default.  

```scdoc
gcloud firestore databases create \
--database=DATABASE_ID \
--location=LOCATION \
--edition=enterprise \
--delete-protection
```

To add[tags](https://firebase.google.com/firestore/mongodb-compatibility/docs/tags)to the database, use the[`--tags`](https://cloud.google.com/sdk/gcloud/reference/firestore/databases/create#--tags)flag. For example:

- `--tags=123/environment=production,123/costCenter=marketing`
- `--tags=tagKeys/333=tagValues/444`

##### Terraform

Use the[`google_firestore_database`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/firestore_database)resource and set`database_edition`to`ENTERPRISE`  

```terraform
resource "google_firestore_database" "database" {
  name             = "<var translate="no">DATABASE_ID</var>"
  location_id      = "<var translate="no">LOCATION</var>"
  type             = "FIRESTORE_NATIVE"
  database_edition = "ENTERPRISE"

  // Optional
  delete_protection_state = "<var translate="no">DELETE_PROTECTION_STATE</var>"
}
```

Replace the following:

- <var translate="no">DATABASE_ID</var>: a[valid database ID](https://firebase.google.com/docs/firestore/enterprise/create-databases#database_id).
- <var translate="no">LOCATION</var>: the name of a[Cloud Firestore with MongoDB compatibility multi-region or region](https://firebase.google.com/docs/firestore/enterprise/locations#types).
- <var translate="no">DELETE_PROTECTION_ENABLEMENT</var>: Either`DELETE_PROTECTION_ENABLED`or`DELETE_PROTECTION_DISABLED`.

To enable deletion protection, set`delete_protection_state`to`DELETE_PROTECTION_ENABLED`. You cannot delete a database with deletion protection enabled until you disable this setting. This setting is disabled by default.

### Database ID

Valid database IDs include IDs that conform to the following:

- Includes only letters, numbers, and hyphen (`-`) characters.
- Letters must be lowercase.
- The first character must be a letter.
- The last character must be a letter or number.
- Minimum of 4 characters.
- Maximum of 63 characters.
- Must not be a UUID or resemble a UUID. For example, don't use an ID like`f47ac10b-58cc-0372-8567-0e02b2c3d479`.

If you delete a database, you cannot immediately re-use the database ID until after 5 minutes.

### Delete protection

Use delete protection to prevent accidental deletion of a database. Delete protection works in the following way:

- You cannot delete a database with delete protection enabled until you disable delete protection.
- Delete protection is disabled by default.
- You can enable delete protection when you create the database or you can[update a database configuration](https://firebase.google.com/docs/firestore/enterprise/create-databases#update_database_configuration)to enable delete protection.

## List databases

Use one of the following methods to list your databases:  

##### Firebaseconsole

1. In theFirebaseconsole, go to the**Firestore Database**page.

   [Go to Firestore Database](https://console.firebase.google.com/project/_/firestore/databases/-default-/data/)
2. Click**Cloud Firestore**to view all databases for the project.

##### gcloud CLI

Use the[`gcloud firestore databases list`](https://cloud.google.com/sdk/gcloud/reference/firestore/databases/list)command to list all the databases in your project.  

```text
gcloud firestore databases list
```

### View database details

To view details about a single database, use one of the following methods:  

##### Firebaseconsole

1. In theFirebaseconsole, go to the**Firestore Database**page.

   [Go to Firestore Database](https://console.firebase.google.com/project/_/firestore/databases/-default-/data/)
2. Select a database from the list of databases.

##### gcloud CLI

Use the[`gcloud firestore databases describe`](https://cloud.google.com/sdk/gcloud/reference/firestore/databases/describe)command:  

```scdoc
gcloud firestore databases describe --database=DATABASE_ID
```

Replace<var translate="no">DATABASE_ID</var>with a database ID.

## Update database configuration

To update the configuration settings of a database, use the[`gcloud firestore databases update`](https://cloud.google.com/sdk/gcloud/reference/firestore/databases/update)command.

Use this command to change, enable, or disable delete protection.

### Update the delete protection setting

To enable delete protection on a database, use the`gcloud firestore databases update`command with the`--delete-protection`flag. For example:  

##### gcloud CLI

```scdoc
gcloud firestore databases update --database=DATABASE_ID --delete-protection
```

Replace<var translate="no">DATABASE_ID</var>with a database ID.

To disable delete protection on a database, use the`gcloud firestore databases update`command with the`--no-delete-protection`flag. For example:  

##### gcloud CLI

```scdoc
gcloud firestore databases update --database=DATABASE_ID --no-delete-protection
```

Replace<var translate="no">DATABASE_ID</var>with a database ID.

## Delete a database

To delete a database, use the console or command-line tool. Deleting a database does not incur charges for delete operations.

If the database has the delete protection setting enabled, you must first[disable delete protection](https://firebase.google.com/docs/firestore/enterprise/create-databases#update_the_delete_protection_setting).  

##### Firebaseconsole

1. In theFirebaseconsole, go to the**Firestore Database**page.

   [Go to Firestore Database](https://console.firebase.google.com/project/_/firestore/databases/-default-/data/)
2. Select the database you want to delete.
3. Clickmore_vert**View more**.
4. Click**Delete**to delete the database.

##### gcloud CLI

Use the[\`gcloud firestore databases delete\`](https://cloud.google.com/sdk/gcloud/reference/firestore/databases/delete)command.  

```scdoc
gcloud firestore databases delete --database=DATABASE_ID
```

Replace<var translate="no">DATABASE_ID</var>with the ID of the database to delete.

## Clone a database

You can clone an existing database at a selected timestamp into a new database:

- The cloned database is a new database that will be created in the same location as the source database.

  To make a clone,Cloud Firestoreuses[point-in-time recovery (PITR) data](https://firebase.google.com/docs/firestore/enterprise/pitr)of the source database. The cloned database includes all data and indexes.
- By default, the cloned database will be encrypted in the same way as the source database, using either Google's default encryption or[CMEK encryption](https://firebase.google.com/docs/firestore/enterprise/use-cmek). You can specify a different encryption type or use a different key for CMEK encryption.

- The timestamp has a granularity of one minute and specifies a point of time in the past, in the period defined by the[PITR window](https://firebase.google.com/docs/firestore/enterprise/pitr#pitr_window):

  - If PITR is enabled for your database, you select any minute in the last 7 days (or less if PITR was enabled less than 7 days ago).
  - If PITR isn't enabled, you can select any minute in the past hour.
  - You can check the earliest timestamp that you can pick[in your database's description](https://firebase.google.com/docs/firestore/enterprise/use-pitr#get-period).

**Note:** To clone databases, your Google Account must have the[`datastore.databases.clone`IAM permission](https://firebase.google.com/docs/firestore/enterprise/create-databases#permissions).  

### Console

1. In the Google Cloud console, go to the**Databases**page.

   [Go to Databases](https://console.cloud.google.com/firestore/databases)
2. Clickmore_vert**View more** in the table row for the database that you want to clone. Click**Clone** . The**Create a clone**dialog appears.

3. In the**Create a clone**dialog, provide parameters for cloning the database:

   1. In the**Give the clone an ID** field, a[database ID](https://firebase.google.com/docs/firestore/enterprise/create-databases#database_id)for a new cloned database. This database ID must not be associated with an existing database.

   2. In the**Clone from**field, select a point in time to use for cloning. The selected time corresponds to a PITR timestamp, at the minute granularity.

4. Click**Create clone**.

| **Note:** The cloned database will have the**same encryption configuration**as the source database. If you want to specify a different encryption configuration for the cloned database, you can use Google Cloud CLI commands.

### gcloud

Use the[`gcloud firestore databases clone`](https://cloud.google.com/sdk/gcloud/reference/firestore/databases/clone)command to clone a database:  

    gcloud firestore databases clone \
    --source-database='<var translate="no">SOURCE_DATABASE</var>' \
    --snapshot-time='<var translate="no">PITR_TIMESTAMP</var>' \
    --destination-database='<var translate="no">DESTINATION_DATABASE_ID</var>'

Replace the following:

- <var translate="no">SOURCE_DATABASE</var>: the database name of an existing database that you want to clone. The name uses the format`projects/`<var translate="no">PROJECT_ID</var>`/databases/`<var translate="no">SOURCE_DATABASE_ID</var>.

- <var translate="no">PITR_TIMESTAMP</var>: a[PITR timestamp](https://firebase.google.com/docs/firestore/enterprise/use-pitr#get-period)in the[RFC 3339 format](https://tools.ietf.org/html/rfc3339), at minute granularity. For example:`2025-06-01T10:20:00.00Z`or`2025-06-01T10:30:00.00-07:00`.

- <var translate="no">DESTINATION_DATABASE_ID</var>: a[database ID](https://firebase.google.com/docs/firestore/enterprise/create-databases#database_id)for a new cloned database. This database ID must not be associated with an existing database.

Example:  

    gcloud firestore databases clone \
    --source-database='projects/example-project/databases/example-source-db' \
    --snapshot-time='2025-06-01T10:20:00.00Z' \
    --destination-database='example-dest-db'

If you want to bind to some tags while cloning a database, use the previous command with the`--tags`flag, which is an optional list of tags KEY=VALUE pairs to bind.

Example:  

    gcloud firestore databases clone \
    --source-database='projects/example-project/databases/(default)' \
    --snapshot-time='2025-06-01T10:20:00.00Z' \
    --destination-database='example-dest-db' \
    --tags=key1=value1,key2=value2

By default, the cloned database will have the same encryption configuration as the source database. To change the encryption configuration, use the`--encryption-type`argument:

- (Default)`use-source-encryption`: use the same encryption configuration as the source database.
- `google-default-encryption`: use Google's default encryption.
- `customer-managed-encryption`: use CMEK encryption. Specify a[key ID](https://cloud.google.com/kms/docs/getting-resource-ids#getting_the_id_for_a_key_and_version)in the`--kms-key-name`argument.

The following example shows how to configure CMEK encryption for the cloned database:  

    gcloud firestore databases clone \
    --source-database='projects/example-project/databases/example-source-db' \
    --snapshot-time='2025-06-01T10:20:00.00Z' \
    --destination-database='example-dest-db' \
    --encryption-type='customer-managed-encryption' \
    --kms-key-name='projects/example-project/locations/us-central1/keyRings/example-key-ring/cryptoKeys/example-key'

### Firebase CLI

Use the`firebase firestore:databases:clone`command to clone a database:  

    firebase firestore:databases:clone \
    '<var translate="no">SOURCE_DATABASE</var>' \
    '<var translate="no">DESTINATION_DATABASE</var>' \
    --snapshot-time '<var translate="no">PITR_TIMESTAMP</var>' \

Replace the following:

- <var translate="no">SOURCE_DATABASE</var>: the database name of an existing database that you want to clone. The name uses the format`projects/`<var translate="no">PROJECT_ID</var>`/databases/`<var translate="no">SOURCE_DATABASE_ID</var>.

- <var translate="no">DESTINATION_DATABASE</var>: a database name for a new cloned database. The name uses the format`projects/`<var translate="no">PROJECT_ID</var>`/databases/`<var translate="no">DESTINATION_DATABASE_ID</var>. This database name must not be associated with an existing database.

- <var translate="no">PITR_TIMESTAMP</var>: a[PITR timestamp](https://firebase.google.com/docs/firestore/enterprise/use-pitr#get-period)in the[RFC 3339 format](https://tools.ietf.org/html/rfc3339), at minute granularity. For example:`2025-06-01T10:20:00.00Z`or`2025-06-01T10:30:00.00-07:00`. If unspecified, the chosen snapshot will be the current time, rounded down to the minute.

By default, the cloned database will have the same encryption configuration as the source database. To change the encryption configuration, use the`--encryption-type`argument:

- (Default)`USE_SOURCE_ENCRYPTION`: use the same encryption configuration as the source database.
- `GOOGLE_DEFAULT_ENCRYPTION`: use Google's default encryption.
- `CUSTOMER_MANAGED_ENCRYPTION`: use CMEK encryption. Specify a[key ID](https://cloud.google.com/kms/docs/getting-resource-ids#getting_the_id_for_a_key_and_version)in the`--kms-key-name`argument.

## Configure per-database access permissions

You can use[Identity and Access Management Conditions](https://firebase.google.com/iam/docs/conditions-overview)to configure access permissions on a per-database level. The following examples use the Google Cloud CLI to assign conditional access for one or more databases. You can also[define IAM conditions in the Google Cloud console](https://firebase.google.com/iam/docs/managing-conditional-role-bindings).
| **Warning:** The Google Cloud console does not allow nor deny access to databases based on IAM conditions configured at the database level. IAM conditions are enforced when accessing databases outside of the Google Cloud console such as with the REST API or the client libraries.

### View existing IAM policies

    gcloud projects get-iam-policy <var label="project ID" translate="no">PROJECT_ID</var>

Set<var label="project ID" translate="no">PROJECT_ID</var>to your project ID.

### Grant access to a database

    gcloud projects add-iam-policy-binding <var label="project ID" translate="no">PROJECT_ID</var> \
    --member='user:<var label="user email" translate="no">EMAIL</var>' \
    --role='roles/datastore.user' \
    --condition='expression=resource.name=="projects/<var label="project ID" translate="no">PROJECT_ID</var>/databases/<var label="database" translate="no">DATABASE_ID</var>",title=<var label="title" translate="no">TITLE</var>,description=<var label="description" translate="no">DESCRIPTION</var>'

Set the following:

- <var translate="no">PROJECT_ID</var>: your project ID
- <var translate="no">EMAIL</var>: an email address that represents a specific account. For example,`alice@example.com`.
- <var translate="no">DATABASE_ID</var>: a database ID.
- <var translate="no">TITLE</var>: an optional title for the expression.
- <var translate="no">DESCRIPTION</var>: an optional description of the expression.

### Grant access to all except one database

    gcloud projects add-iam-policy-binding <var label="project ID" translate="no">PROJECT_ID</var> \
    --member='user:<var label="user email" translate="no">EMAIL</var>' \
    --role='roles/datastore.user' \
    --condition='expression=resource.name!="projects/<var label="project ID" translate="no">PROJECT_ID</var>/databases/<var label="database" translate="no">DATABASE_ID</var>",title=<var label="title" translate="no">TITLE</var>,description=<var label="description" translate="no">DESCRIPTION</var>'

Set the following:

- <var translate="no">PROJECT_ID</var>: your project ID
- <var translate="no">EMAIL</var>: an email address that represents a specific account. For example,`alice@example.com`.
- <var translate="no">DATABASE_ID</var>: a database ID.
- <var translate="no">TITLE</var>: an optional title for the expression.
- <var translate="no">DESCRIPTION</var>: an optional description of the expression.

### Remove policies for a given member and role

    gcloud projects remove-iam-policy-binding <var label="project ID" translate="no">PROJECT_ID</var> \
    --member='user:<var label="user email" translate="no">EMAIL</var>' \
    --role='roles/datastore.user' --all

Set the following:

- <var translate="no">PROJECT_ID</var>: your project ID
- <var translate="no">EMAIL</var>: an email address that represents a specific account. For example,`alice@example.com`.

## Limitations

You can have a maximum of 100 databases per project. You can[contact support](https://firebase.google.com/support-hub)to request an increase to this limit.

## What's next

- Run the[Quickstart: Create a database and connect to it](https://firebase.google.com/docs/firestore/enterprise/create-and-query-database).
- Learn about[Behavior differences](https://firebase.google.com/docs/firestore/enterprise/behavior-differences).
- Learn about[Cloud Monitoringmetrics for Cloud Firestore with MongoDB compatibility](https://firebase.google.com/docs/firestore/enterprise/use-monitoring-dashboard).