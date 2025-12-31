# Source: https://firebase.google.com/docs/firestore/manage-databases.md.txt

<br />

This page describes how to create, update, and deleteCloud Firestoredatabases. You can create multipleCloud Firestoredatabases per project. You can use multiple databases to set up production and testing environments, to isolate customer data, and for data regionalization.

## The`(default)`database

If you don't specify a database, theCloud Firestoreclient libraries and the Google Cloud CLI connect to the`(default)`database by default.

## Required roles

To create and manage databases, you need the`Owner`or`Datastore Owner`Identity and Access Management role. These roles grant the required permissions.

### Required permissions

To manage databases, you require the following permissions:

- Create a database:`datastore.databases.create`
- Read database configuration:`datastore.databases.getMetadata`
- Configure a database:`datastore.databases.update`
- Delete a database:`datastore.databases.delete`
- Clone a database:`datastore.databases.clone`

## Create a database

To create a database, use one of the following methods:  

##### Console

1. In theFirebaseconsole, go to the**Firestore Database**page.

   [Go to Firestore Database](https://console.firebase.google.com/project/_/firestore/databases/-default-/data/)
2. If this is your first named database, click**Add database**.
3. Otherwise, click**(default)** , then**Add database**.
4. Configure your database. Enter a Database ID. Select a location. Click**Create Database**.

##### gcloud

Use the[`gcloud firestore databases create`](https://cloud.google.com/sdk/gcloud/reference/firestore/databases/create)command.  

```carbon
gcloud firestore databases create \
--database=DATABASE_ID \
--location=LOCATION \
--type=DATABASE_TYPE \
[--delete-protection]
```

Replace the following:

- <var translate="no">DATABASE_ID</var>: a[valid database ID](https://firebase.google.com/docs/firestore/manage-databases#database_id).
- <var translate="no">LOCATION</var>: the name of a[Cloud Firestoremulti-region or region](https://firebase.google.com/docs/firestore/locations#types).
- <var translate="no">DATABASE_TYPE</var>: either`firestore-native`for Native mode or`datastore-mode`for Datastore mode.

`--delete-protection`is an optional flag to enable deletion protection. You cannot delete a database with deletion protection enabled until you disable this setting. This setting is disabled by default.

To add[tags](https://cloud.google.com/firestore/docs/tags)to the database, use the[`--tags`](https://cloud.google.com/sdk/gcloud/reference/firestore/databases/create#--tags)flag. For example:

- `--tags=123/environment=production,123/costCenter=marketing`
- `--tags=tagKeys/333=tagValues/444`

##### Firebase CLI

```scdoc
firebase firestore:databases:create DATABASE_ID \
--location=LOCATION \
[--delete-protection DELETE_PROTECTION_ENABLEMENT]
```

Replace the following:

- <var translate="no">DATABASE_ID</var>: a[valid database ID](https://firebase.google.com/docs/firestore/manage-databases#database_id).
- <var translate="no">LOCATION</var>: the name of a[Cloud Firestoremulti-region or region](https://firebase.google.com/docs/firestore/locations#types).
- <var translate="no">DELETE_PROTECTION_ENABLEMENT</var>: Either`ENABLED`or`DISABLED`.
The database created is always in Firestore Native mode.

`--delete-protection `is an optional argument to enable deletion protection. You cannot delete a database with deletion protection enabled until you disable this setting. This setting is disabled by default.

##### Terraform

```terraform
resource "google_firestore_database" "database" {
  project     = "project-id"
  name        = DATABASE_ID
  location_id = LOCATION
  type        = DATABASE_TYPE

  // Optional
  delete_protection_state = DELETE_PROTECTION_STATE
}
```

Replace the following:

- <var translate="no">DATABASE_ID</var>: a[valid database ID](https://firebase.google.com/docs/firestore/manage-databases#database_id).
- <var translate="no">LOCATION</var>: the name of a[Cloud Firestoremulti-region or region](https://firebase.google.com/docs/firestore/locations#types).
- <var translate="no">DATABASE_TYPE</var>: either`FIRESTORE_NATIVE`for Native mode or`DATASTORE_MODE`for Datastore mode.
- <var translate="no">DELETE_PROTECTION_ENABLEMENT</var>: Either`DELETE_PROTECTION_ENABLED`or`DELETE_PROTECTION_DISABLED`.

`delete_protection_state`is an optional argument to enable deletion protection. You cannot delete a database with deletion protection enabled until you disable this setting. This setting is disabled by default.

### Database ID

Valid database IDs include`(default)`and IDs that conform to the following:

- Includes only letters, numbers, and hyphen (`-`) characters.
- Letters must be lowercase.
- The first character must be a letter.
- The last character must be a letter or number.
- Minimum of 4 characters.
- Maximum of 63 characters.
- Must not be a UUID or resemble a UUID. For example, don't use an ID like`f47ac10b-58cc-0372-8567-0e02b2c3d479`.

If you delete a database, you cannot immediately re-use the database ID until after 5 minutes.

### Delete protection

Use delete protection to prevent accidental deletion of a database. You cannot delete a database with delete protection enabled until you disable delete protection. Delete protection is disabled by default. You can enable delete protection when you create the database or you can[update a database configuration](https://firebase.google.com/docs/firestore/manage-databases#update_database_configuration)to enable delete protection.

## Set upCloud FirestoreSecurity Rulesfor your databases

Use theFirebaseCLI to deployCloud FirestoreSecurity Rulesto each of your databases. Refer to the[guide for managing and deployingCloud FirestoreSecurity Rules](https://firebase.google.com/docs/rules/manage-deploy).

## Access a named database with a client library

A named database includes any database not named`(default)`. By default, the Firebase SDKs and Google API Client Libraries connect to the`(default)`Cloud Firestoredatabase in a project. To create a client connected to a named database, set the database ID when you instantiate a client.
| **Note:** To work with multiple databases, be sure to update to the latest[Firebase Client SDKs](https://firebase.google.com/docs/firestore/client/libraries#mobile_and_web_sdks)and[Google API Client Libraries](https://firebase.google.com/docs/firestore/client/libraries#google_cloud_client_libraries).

## List databases

Use one of the following methods to list your databases:  

##### Console

In the Google Cloud console, go to the**Databases**page.

[Go to Databases](https://console.cloud.google.com/firestore/databases)
| **Note:** You can view and list your databases in the Google Cloud console. You can create the`(default)`database using the Google Cloud console, but you must use the[Google Cloud CLI or another method](https://firebase.google.com/docs/firestore/manage-databases#create_a_database)to create a named database. To delete a database[use the Google Cloud CLI](https://firebase.google.com/docs/firestore/manage-databases#delete-database).

##### gcloud

Use the[`gcloud firestore databases list`](https://cloud.google.com/sdk/gcloud/reference/firestore/databases/list)command to list all the databases in your project.  

```text
gcloud firestore databases list
```

##### Firebase CLI

Use the`firebase firestore:databases:list`command to list all the databases in your project.  

```text
firebase firestore:databases:list
```

### View database details

To view details about a single database, use one of the following methods:  

##### gcloud

Use the[`gcloud firestore databases describe`](https://cloud.google.com/sdk/gcloud/reference/firestore/databases/describe)command:  

```scdoc
gcloud firestore databases describe --database=DATABASE_ID
```

##### Firebase CLI

Use the`firebase firestore:databases:get`command:  

```scdoc
firebase firestore:databases:get DATABASE_ID
```

Replace<var translate="no">DATABASE_ID</var>with a database ID.

## Update database configuration

To update the configurations settings of a database, use the[`gcloud firestore databases update`](https://cloud.google.com/sdk/gcloud/reference/firestore/databases/update)command. Use this command to change to enable or disable delete protection.

### Update the delete protection setting

To enable delete protection on a database, use the`gcloud firestore databases update`command with the`--delete-protection`flag. For example:  

##### gcloud

```scdoc
gcloud firestore databases update --database=DATABASE_ID --delete-protection
```

Replace<var translate="no">DATABASE_ID</var>with a database ID.

To disable delete protection on a database, use the`gcloud firestore databases update`command with the`--no-delete-protection`flag. For example:  

##### gcloud

```scdoc
gcloud firestore databases update --database=DATABASE_ID --no-delete-protection
```

Replace<var translate="no">DATABASE_ID</var>with a database ID.

## Delete a database

To delete a database, use the console or command-line tool.

If the database has the delete protection setting enabled, you must first[disable delete protection](https://firebase.google.com/docs/firestore/manage-databases#update_the_delete_protection_setting).

If the database contains[App Enginesearch data](https://cloud.google.com/appengine/docs/legacy/standard/python/search)or[blob entities](https://cloud.google.com/appengine/docs/legacy/standard/python/blobstore), you must delete that data first.

Deleting a database does not automatically delete any[Eventarctriggers](https://firebase.google.com/docs/firestore/eventarc)for that database. The trigger stops delivering events but continues to exist until you[delete the trigger](https://cloud.google.com/eventarc/docs/managing-triggers#trigger-delete).

Deleting a database does not incur charges for delete operations.  

##### Console

1. In theFirebaseconsole, go to the**Firestore Database**page.

   [Go to Firestore Database](https://console.firebase.google.com/project/_/firestore/databases/-default-/data/)
2. On the Data tab, above the data table view for the database, clickmore_vert, then select**Delete database**.
3. Follow the instructions to delete the database.

##### gcloud

Use the[\`gcloud firestore databases delete\`](https://cloud.google.com/sdk/gcloud/reference/firestore/databases/delete)command.  

```scdoc
gcloud firestore databases delete --database=DATABASE_ID
```

Replace<var translate="no">DATABASE_ID</var>with the ID of the database to delete. To delete the default database use the ID`'(default)'`

## Clone a database

You can clone an existing database at a selected timestamp into a new database:

- The cloned database is a new database that will be created in the same location as the source database.

  To make a clone,Cloud Firestoreuses[point-in-time recovery (PITR) data](https://firebase.google.com/docs/firestore/pitr)of the source database. The cloned database includes all data and indexes.
- By default, the cloned database will be encrypted in the same way as the source database, using either Google's default encryption or[CMEK encryption](https://firebase.google.com/docs/firestore/use-cmek). You can specify a different encryption type or use a different key for CMEK encryption.

- The timestamp has a granularity of one minute and specifies a point of time in the past, in the period defined by the[PITR window](https://firebase.google.com/docs/firestore/pitr#pitr_window):

  - If PITR is enabled for your database, you select any minute in the last 7 days (or less if PITR was enabled less than 7 days ago).
  - If PITR isn't enabled, you can select any minute in the past hour.
  - You can check the earliest timestamp that you can pick[in your database's description](https://firebase.google.com/docs/firestore/use-pitr#get-period).

**Note:** To clone databases, your Google Account must have the[`datastore.databases.clone`IAM permission](https://firebase.google.com/docs/firestore/manage-databases#permissions).  

### Console

Firebaseconsole doesn't support database cloning. You can use instructions for Google Cloud CLI to clone databases.

### gcloud

Use the[`gcloud firestore databases clone`](https://cloud.google.com/sdk/gcloud/reference/firestore/databases/clone)command to clone a database:  

    gcloud firestore databases clone \
    --source-database='<var translate="no">SOURCE_DATABASE</var>' \
    --snapshot-time='<var translate="no">PITR_TIMESTAMP</var>' \
    --destination-database='<var translate="no">DESTINATION_DATABASE_ID</var>'

Replace the following:

- <var translate="no">SOURCE_DATABASE</var>: the database name of an existing database that you want to clone. The name uses the format`projects/`<var translate="no">PROJECT_ID</var>`/databases/`<var translate="no">SOURCE_DATABASE_ID</var>.

- <var translate="no">PITR_TIMESTAMP</var>: a[PITR timestamp](https://firebase.google.com/docs/firestore/use-pitr#get-period)in the[RFC 3339 format](https://tools.ietf.org/html/rfc3339), at minute granularity. For example:`2025-06-01T10:20:00.00Z`or`2025-06-01T10:30:00.00-07:00`.

- <var translate="no">DESTINATION_DATABASE_ID</var>: a[database ID](https://firebase.google.com/docs/firestore/manage-databases#database_id)for a new cloned database. This database ID must not be associated with an existing database.

Example:  

    gcloud firestore databases clone \
    --source-database='projects/example-project/databases/(default)' \
    --snapshot-time='2025-06-01T10:20:00.00Z' \
    --destination-database='example-dest-db'

If you want to bind to some tags while cloning a database, use the previous command with the`--tags`flag, which is an optional list of tags KEY=VALUE pairs to bind.

Example:  

    gcloud firestore databases clone \
    --source-database='projects/example-project/databases/(default)' \
    --snapshot-time='2025-06-01T10:20:00.00Z' \
    --destination-database='example-dest-db'

By default, the cloned database will have the same encryption configuration as the source database. To change the encryption configuration, use the`--encryption-type`argument:

- (Default)`use-source-encryption`: use the same encryption configuration as the source database.
- `google-default-encryption`: use Google's default encryption.
- `customer-managed-encryption`: use CMEK encryption. Specify a[key ID](https://cloud.google.com/kms/docs/getting-resource-ids#getting_the_id_for_a_key_and_version)in the`--kms-key-name`argument.

The following example shows how to configure CMEK encryption for the cloned database:  

    gcloud firestore databases clone \
    --source-database='projects/example-project/databases/(default)' \
    --snapshot-time='2025-06-01T10:20:00.00Z' \
    --destination-database='example-dest-db' \
    --encryption-type='customer-managed-encryption' \
    --kms-key-name='projects/example-project/locations/us-central1/keyRings/example-key-ring/cryptoKeys/example-key'

### Firebase CLI

Use the`firebase firestore:databases:clone`command to clone a database:  

    firebase firestore:databases:clone \
    '<var translate="no">SOURCE_DATABASE</var>' \
    '<var translate="no">DESTINATION_DATABASE</var>' \
    --snapshot-time '<var translate="no">PITR_TIMESTAMP</var>'

Replace the following:

- <var translate="no">SOURCE_DATABASE</var>: the database name of an existing database that you want to clone. The name uses the format`projects/`<var translate="no">PROJECT_ID</var>`/databases/`<var translate="no">SOURCE_DATABASE_ID</var>.

- <var translate="no">DESTINATION_DATABASE</var>: a database name for a new cloned database. The name uses the format`projects/`<var translate="no">PROJECT_ID</var>`/databases/`<var translate="no">DESTINATION_DATABASE_ID</var>. This database name must not be associated with an existing database.

- <var translate="no">PITR_TIMESTAMP</var>: a[PITR timestamp](https://firebase.google.com/docs/firestore/use-pitr#get-period)in the[RFC 3339 format](https://tools.ietf.org/html/rfc3339), at minute granularity. For example:`2025-06-01T10:20:00.00Z`or`2025-06-01T10:30:00.00-07:00`. If unspecified, the chosen snapshot will be the current time, rounded down to the minute.

By default, the cloned database will have the same encryption configuration as the source database. To change the encryption configuration, use the`--encryption-type`argument:

- (Default)`USE_SOURCE_ENCRYPTION`: use the same encryption configuration as the source database.
- `GOOGLE_DEFAULT_ENCRYPTION`: use Google's default encryption.
- `CUSTOMER_MANAGED_ENCRYPTION`: use CMEK encryption. Specify a[key ID](https://cloud.google.com/kms/docs/getting-resource-ids#getting_the_id_for_a_key_and_version)in the`--kms-key-name`argument.

## Configure per-database access permissions

You can use[Identity and Access Management Conditions](https://cloud.google.com/iam/docs/conditions-overview)to configure access permissions on a per-database level. The following examples use the Google Cloud CLI to assign conditional access for one or more databases. You can also[define IAM conditions in the Google Cloud console](https://cloud.google.com/iam/docs/managing-conditional-role-bindings).
| **Warning:** The Google Cloud console does not allow/deny access to databases based on IAM conditions configured at the database level. This only applies to accessing databases with the Google Cloud console. IAM conditions are enforced when accessing databases outside of the Google Cloud console such as with the REST API or the client libraries.

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
- <var translate="no">EMAIL</var>: an email address that represents a specific Google Account. For example,`alice@example.com`.
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
- <var translate="no">EMAIL</var>: an email address that represents a specific Google Account. For example,`alice@example.com`.
- <var translate="no">DATABASE_ID</var>: a database ID.
- <var translate="no">TITLE</var>: an optional title for the expression.
- <var translate="no">DESCRIPTION</var>: an optional description of the expression.

### Remove policies for a given member and role

    gcloud projects remove-iam-policy-binding <var label="project ID" translate="no">PROJECT_ID</var> \
    --member='user:<var label="user email" translate="no">EMAIL</var>' \
    --role='roles/datastore.user' --all

Set the following:

- <var translate="no">PROJECT_ID</var>: your project ID
- <var translate="no">EMAIL</var>: an email address that represents a specific Google Account. For example,`alice@example.com`.

## Cloud Monitoring

Cloud Firestoremetrics are reported under two monitored resources.

- [firestore.googleapis.com/Database](https://cloud.google.com/monitoring/api/resources#tag_firestore.googleapis.com/Database)
- [firestore_instance](https://cloud.google.com/monitoring/api/resources#tag_firestore_instance)(Legacy)

You can inspect aggregate metrics at the database level by looking at`firestore.googleapis.com/Database`. The metrics reported under`firestore_instance`are aggregated at the project level.

## Limitations

- You can have a maximum of 100 databases per project. You can[contact support](https://firebase.google.com/support)to request an increase to this limit.
- You cannot delete your`(default)`database if it contains any[GAE search data](https://cloud.google.com/appengine/docs/legacy/standard/python/search). Use the[index delete api](https://cloud.google.com/appengine/docs/legacy/standard/python/search#deleting_an_index)to delete GAE search data. If you recently deleted GAE Search data, there may be a waiting period before you are able to delete the database.
- You cannot delete your`(default)`database if it contains any[blob entities](https://cloud.google.com/appengine/docs/legacy/standard/python/blobstore). Use the[Blobstore delete api](https://cloud.google.com/appengine/docs/legacy/standard/python/refdocs/google.appengine.ext.blobstore.blobstore#google.appengine.ext.blobstore.blobstore.delete)to delete Blobstore data. You can check if your`(default)`database has Blobstore data by running the following GQL query in the Google Cloud console:`SELECT * FROM __BlobInfo__`.
- You cannot reuse a database ID until 5 minutes after the delete happens.
- Cloud Function v1 does not support Firestore Named databases. Use[Cloud Firestore Triggers (2nd Gen)](https://cloud.google.com/functions/docs/calling/cloud-firestore)to configure events for named databases.
- [Firestore function triggers v1](https://cloud.google.com/firestore/docs/extend-with-functions)and[Firestore event triggers](https://cloud.google.com/firestore/docs/eventarc)may stop working after the database is deleted, even if a new database is created with the same name.

## What's next

- [Add data](https://firebase.google.com/docs/firestore/manage-data/add-data)
- [Get data](https://firebase.google.com/docs/firestore/query-data/get-data)
- [Delete data](https://firebase.google.com/docs/firestore/manage-data/delete-data)