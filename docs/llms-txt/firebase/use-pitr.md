# Source: https://firebase.google.com/docs/firestore/use-pitr.md.txt

# Source: https://firebase.google.com/docs/firestore/enterprise/use-pitr.md.txt

<br />

<br />

|----------------------------------------------------------------------------------------|
| *Relevant to Cloud Firestore Standard edition and Cloud Firestore Enterprise edition.* |

<br />

This page describes how to use point-in-time recovery (PITR) to retain and recover data in Cloud Firestore with MongoDB compatibility.

To understand PITR concepts, see[Point-in-time recovery](https://firebase.google.com/docs/firestore/enterprise/pitr).

## Permissions

To get the permissions that you need to manage PITR settings, ask your administrator to grant you the following IAM roles on the project where you want to enable PITR:

- Cloud Datastore Owner (`roles/datastore.owner`)

For custom roles, ensure that the following permissions are granted:

- To enable PITR when creating a database:`datastore.databases.create`
- To update PITR settings on existing database:`datastore.databases.update`,`datastore.databases.list`
- To perform reads from PITR data:`datastore.databases.get`,`datastore.entities.get`,`datastore.entities.list`
- To export PITR data:`datastore.databases.export`
- To import PITR data:`datastore.databases.import`
- To clone a database:`datastore.databases.clone`

## Before you begin

Note the following points before you start using PITR:

- You can't start reading from seven days in the past immediately after you enable PITR.
- If you want to enable PITR when you create a database, you must use the`gcloud firestore databases create`command. Enabling PITR while creating a database using the Google Cloud console is not supported.
- Cloud Firestore with MongoDB compatibility starts retaining versions from the point forward after enabling PITR.
- You cannot read PITR data in the PITR window after you disable PITR.
- If you re-enable PITR immediately after disabling it, the past PITR data is no longer available. Any PITR data created before disabling PITR will be deleted after the PITR expiration date.
- If you accidentally deleted data in the last hour and PITR is disabled, you can restore your data by enabling PITR within one hour of deletion.
- Any read performed on expired PITR data fails.

## Enable PITR

Before using PITR,[enable billing for your Google Cloud project](https://cloud.google.com/billing/docs/how-to/modify-project#enable_billing_for_a_project). Only Google Cloud projects with billing enabled can use the PITR functionality.

To enable PITR for your database:  

### Console

1. In the Google Cloud console, go to the**Databases**page.

   [Go to Databases](https://console.cloud.google.com/firestore/databases)
2. Select the required database from the list of databases.

3. In the navigation menu, click**Disaster Recovery**.

4. Click**Edit**to edit the settings.

5. Select the**Enable point-in-time recovery** checkbox, and then click**Save**.

Enabling PITR incurs storage costs. See[Pricing](https://firebase.google.com/docs/firestore/pricing)for more information.

To disable PITR, clear the**Enable point-in-time recovery**checkbox from the Disaster Recovery page in the Google Cloud console.

### gcloud

Enable PITR during database creation with the[`gcloud firestore databases create`](https://cloud.google.com/sdk/gcloud/reference/firestore/databases/create)and the`--enable-ptir`command as follows:  

    gcloud firestore databases create\
      --location=<var translate="no">LOCATION</var>\
      --database=<var translate="no">DATABASE_ID</var>\
      --type=firestore-native\
      --enable-pitr

Replace the values as follows:

- <var translate="no">LOCATION</var>- location where you want to create your database.
- <var translate="no">DATABASE_ID</var>- set to a database ID.

You can disable PITR using the[`gcloud firestore databases update`](https://cloud.google.com/sdk/gcloud/reference/firestore/databases/update)command as follows:  

    gcloud firestore databases update\
      --database=<var translate="no">DATABASE_ID</var>\
      --no-enable-pitr

Replace the values as follows:

- <var translate="no">DATABASE_ID</var>- set to the database ID or (default).

## Get the retention period and earliest version time

### Console

1. In the Google Cloud console, go to the**Databases**page.

   [Go to Databases](https://console.cloud.google.com/firestore/databases)
2. Select the required database from the list of databases.

3. In the navigation menu, click**Disaster Recovery**.

4. In the**Settings** section, note the**Retention period** and**Earliest version time**.

   - **Retention period**: the period in which Cloud Firestore with MongoDB compatibility retains all versions of data for the database. The value is one hour when PITR is disabled and seven days when PITR is enabled.
   - **Earliest version time**: the earliest timestamp at which older versions of the data can be read in the PITR window. This value is continuously updated by Cloud Firestore with MongoDB compatibility and becomes stale the moment it is queried. If you are using this value to recover data, make sure to account for the time from the moment wÌ¦hen the value is queried to the moment when you initiate the recovery.
   - **Point-in-time recovery** : shows`Enabled`, if PITR is enabled. If PITR is disabled, you will see`Disabled`.

### gcloud

Run the[gcloud firestore databases describe](https://cloud.google.com/sdk/gcloud/reference/firestore/databases/describe)command as follows:  

    gcloud firestore databases describe --database=<var translate="no">DATABASE_ID</var>

Replace<var translate="no">DATABASE_ID</var>with the database ID or`'(default)'`.

Here's the output:  

        appEngineIntegrationMode: ENABLED
        concurrencyMode: PESSIMISTIC
        createTime: '2021-03-24T17:02:35.234Z'
        deleteProtectionState: DELETE_PROTECTION_DISABLED
        earliestVersionTime: '2023-06-12T16:17:25.222474Z'
        etag: IIDayqOevv8CMNTvyNK4uv8C
        keyPrefix: s
        locationId: nam5
        name: projects/<var translate="no">PROJECT_ID</var>/databases/<var translate="no">DATABASE_ID</var>
        pointInTimeRecoveryEnablement: POINT_IN_TIME_RECOVERY_DISABLED
        type: FIRESTORE_NATIVE
        uid: 5230c382-dcd2-468f-8cb3-2a1acfde2b32
        updateTime: '2021-11-17T17:48:22.171180Z'
        versionRetentionPeriod: 3600s

where,

- `earliestVersionTime`: timestamp of the earliest PITR data stored.
- `pointInTimeRecoveryEnablement`: shows`POINT_IN_TIME_RECOVERY_ENABLED`, if PITR is enabled. If PITR is disabled, you will either see`POINT_IN_TIME_RECOVERY_DISABLED`or the`pointInTimeRecoveryEnablement`field might not be displayed.
- `versionRetentionPeriod`: time period for which PITR data is retained in milliseconds. The value can be one hour when PITR is disabled or seven days if PITR is enabled.

## Read PITR data

You can read PITR data using the client libraries, REST API methods, or FirestoreIO Apache Beam connector.

<br />

### Client libraries

**Note:** You can read from PITR data in the server client libraries, namely Go, Java, Node.js, and PHP. The mobile and web SDKs, namely, Android, IOS, and Web are not supported.  

### Java

You must use the`ReadOnly`transaction to read PITR data. You cannot directly specify`readTime`in reads. See[Transactions and batched writes](https://firebase.google.com/docs/firestore/enterprise/manage-data/transactions)for more information.  

      Firestore firestore = ...

      TransactionOptions options =
              TransactionOptions.createReadOnlyOptionsBuilder()
                  .setReadTime(
                      com.google.protobuf.Timestamp.newBuilder()
                          .setSeconds(1684098540L)
                          .setNanos(0))
                  .build();

      ApiFuture<Void> futureTransaction = firestore.runTransaction(
                  transaction -> {
                    // Does a snapshot read document lookup
                    final DocumentSnapshot documentResult =
                        transaction.get(documentReference).get();

                    // Executes a snapshot read query
                    final QuerySnapshot queryResult =
                      transaction.get(query).get();
                  },
                  options);

      // Blocks on transaction to complete
      futureTransaction.get();

### Node

You must use a`ReadOnly`transaction to read PITR data. You cannot directly specify`readTime`in reads. See[Transactions and batched writes](https://firebase.google.com/docs/firestore/enterprise/manage-data/transactions)for more information.  

    const documentSnapshot = await firestore.runTransaction(
        updateFunction => updateFunction.get(documentRef),
        {readOnly: true, readTime: new Firestore.Timestamp(1684098540, 0)}
    );

    const querySnapshot = await firestore.runTransaction(
        updateFunction => updateFunction.get(query),
        {readOnly: true, readTime: new Firestore.Timestamp(1684098540, 0)}
    );

### REST API

PITR reads are supported in all Cloud Firestore with MongoDB compatibility read methods, which are[get](https://firebase.google.com/docs/firestore/enterprise/reference/rest/v1/projects.databases.documents/get),[list](https://firebase.google.com/docs/firestore/enterprise/reference/rest/v1/projects.databases.documents/list),[batchGet](https://firebase.google.com/docs/firestore/enterprise/reference/rest/v1/projects.databases.documents/batchGet),[listCollectionIds](https://firebase.google.com/docs/firestore/enterprise/reference/rest/v1/projects.databases.documents/listCollectionIds),[listDocuments](https://firebase.google.com/docs/firestore/enterprise/reference/rest/v1/projects.databases.documents/listDocuments),[runQuery](https://firebase.google.com/docs/firestore/enterprise/reference/rest/v1/projects.databases.documents/runQuery),[runAggregationQuery](https://cloud.google.com/firestore/docs/reference/rest/v1/projects.databases.documents/runAggregationQuery), and[partitionQuery](https://firebase.google.com/docs/firestore/enterprise/reference/rest/v1/projects.databases.documents/partitionQuery).

To perform a read using the REST methods, try one of the following options:

1. In your read method request, pass the`readTime`value as as a supported PITR timestamp in the`readOptions`method. A PITR timestamp can be either microsecond precision timestamp within the past hour or a whole minute timestamp beyond the past hour, but not earlier than the`earliestVersionTime`.

2. Use the`readTime`parameter together with the`BeginTransaction`method as part of a[`ReadOnly`transaction](https://cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore#transactionoptions)for multiple PITR reads.

### Apache Beam

Use the Cloud Firestore with MongoDB compatibilityIO Apache Beam connector to read or write documents in a Cloud Firestore with MongoDB compatibility database at a large scale with Dataflow.

PITR reads are supported in the following read method of the Cloud Firestore with MongoDB compatibilityIO connector. These read methods support the`withReadTime(@Nullable Instant readTime)`method that you use can use for PITR reads:

- [FirestoreV1.BatchGetDocuments](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/gcp/firestore/FirestoreV1.BatchGetDocuments.Builder.html)
- [FirestoreV1.ListCollectionIds](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/gcp/firestore/FirestoreV1.ListCollectionIds.Builder.html)
- [FirestoreV1.ListDocuments](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/gcp/firestore/FirestoreV1.ListDocuments.Builder.html)
- [FirestoreV1.PartitionQuery](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/gcp/firestore/FirestoreV1.PartitionQuery.Builder.html)
- [FirestoreV1.RunQuery](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/gcp/firestore/FirestoreV1.RunQuery.Builder.html)

### Java

The following code can be used with the[example Dataflow pipeline code](https://firebase.google.com/docs/firestore/enterprise/dataflow-connector)for bulk read or write operations. The example uses the`withReadTime(@Nullable Instant readTime)`method for PITR reads.  

      Instant readTime = Instant.ofEpochSecond(1684098540L);

      PCollection<Document> documents =
          pipeline
              .apply(Create.of(collectionId))
              .apply(
                  new FilterDocumentsQuery(
                      firestoreOptions.getProjectId(), firestoreOptions.getDatabaseId()))
              .apply(FirestoreIO.v1().read().runQuery().withReadTime(readTime).withRpcQosOptions(rpcQosOptions).build())
      ...

For a complete list of`readTime`examples in the Dataflow pipeline, see the[GitHub repository](https://github.com/apache/beam/blob/master/sdks/java/io/google-cloud-platform/src/test/java/org/apache/beam/sdk/io/gcp/firestore/it/BaseFirestoreIT.java).

## Clone from a database

You can clone an existing database at a selected timestamp into a new database:

- The cloned database is a new database that will be created in the same location as the source database.

  To make a clone,Cloud Firestoreuses[point-in-time recovery (PITR) data](https://firebase.google.com/docs/firestore/enterprise/pitr)of the source database. The cloned database includes all data and indexes.
- By default, the cloned database will be encrypted in the same way as the source database, using either Google's default encryption or[CMEK encryption](https://firebase.google.com/docs/firestore/enterprise/use-cmek). You can specify a different encryption type or use a different key for CMEK encryption.

- The timestamp has a granularity of one minute and specifies a point of time in the past, in the period defined by the[PITR window](https://firebase.google.com/docs/firestore/enterprise/pitr#pitr_window):

  - If PITR is enabled for your database, you select any minute in the last 7 days (or less if PITR was enabled less than 7 days ago).
  - If PITR isn't enabled, you can select any minute in the past hour.
  - You can check the earliest timestamp that you can pick[in your database's description](https://firebase.google.com/docs/firestore/enterprise/use-pitr#get-period).

**Note:** To clone databases, your Google Account must have the[`datastore.databases.clone`IAM permission](https://firebase.google.com/docs/firestore/enterprise/use-pitr#permissions).  

### Console

Firebaseconsole doesn't support database cloning. You can use instructions forGoogle Cloud CLIto clone databases.
| **Note:** The cloned database will have the**same encryption configuration** as the source database. If you want to specify a different encryption configuration for the cloned database, you can useGoogle Cloud CLIcommands.

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
    --source-database='projects/example-project/databases/(default)' \
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

- <var translate="no">PITR_TIMESTAMP</var>: a[PITR timestamp](https://firebase.google.com/docs/firestore/enterprise/use-pitr#get-period)in the[RFC 3339 format](https://tools.ietf.org/html/rfc3339), at minute granularity. For example:`2025-06-01T10:20:00.00Z`or`2025-06-01T10:30:00.00-07:00`. If unspecified, the chosen snapshot will be the current time, rounded down to the minute.

By default, the cloned database will have the same encryption configuration as the source database. To change the encryption configuration, use the`--encryption-type`argument:

- (Default)`USE_SOURCE_ENCRYPTION`: use the same encryption configuration as the source database.
- `GOOGLE_DEFAULT_ENCRYPTION`: use Google's default encryption.
- `CUSTOMER_MANAGED_ENCRYPTION`: use CMEK encryption. Specify a[key ID](https://cloud.google.com/kms/docs/getting-resource-ids#getting_the_id_for_a_key_and_version)in the`--kms-key-name`argument.

The following example shows how to configure CMEK encryption for the cloned database:  

    firebase firestore:databases:clone \
    'projects/example-project/databases/(default)' \
    'projects/example-project/databases/example-dest-db' \
    --snapshot-time '<var translate="no">PITR_TIMESTAMP</var>' \
    --encryption-type CUSTOMER_MANAGED_ENCRYPTION

### Limitations

A clone operation does not clone[App Enginesearch data](https://cloud.google.com/appengine/docs/legacy/standard/python/search)or[blob entities](https://cloud.google.com/appengine/docs/legacy/standard/python/blobstore)from a`(default)`database. This data is only valid for the`(default)`database, and it won't be useful if you clone from`(default)`to a database which does not support such data, so it is excluded from clones.

## Export and import from PITR data

You can export your database toCloud Storagefrom PITR data using the[`gcloud firestore export`](https://cloud.google.com/sdk/gcloud/reference/firestore/export)command. You can export PITR data where the timestamp is a whole minute timestamp within the past seven days, but not earlier than the`earliestVersionTime`. If data no longer exists at the specified timestamp, the export operation fails.

The PITR export operation supports all filters, including export of all documents and export of specific collections.

1. Export the database, specifying the`snapshot-time`parameter to the chosen recovery timestamp.

   ### gcloud

   Run the following command to export the database to your bucket.  

       gcloud firestore export gs://<var translate="no">BUCKET_NAME_PATH</var> \
           --snapshot-time=<var translate="no">PITR_TIMESTAMP</var> \
           --collection-ids=<var translate="no">COLLECTION_IDS</var> \
           --namespace-ids=<var translate="no">NAMESPACE_IDS</var>

   Where,
   - <var translate="no">BUCKET_NAME_PATH</var>- a validCloud Storagebucket with an optional path prefix where export files are stored.
   - <var translate="no">PITR_TIMESTAMP</var>- a PITR timestamp at the minute granularity, for example,`2023-05-26T10:20:00.00Z`or`2023-10-19T10:30:00.00-07:00`.
   - <var translate="no">COLLECTION_IDS</var>- a list of collection IDs or collection group IDs, for example-`'specific-collection-group1','specific-collection-group2'`.
   - <var translate="no">NAMESPACE_IDS</var>- a list of namespace IDs, for example-`'customer','orders'`.

   Note the following points before exporting PITR data:
   - Specify the timestamp in[RFC 3339 format](https://tools.ietf.org/html/rfc3339). For example,`2023-05-26T10:20:00.00Z`or`2023-10-19T10:30:00.00-07:00`.
   - Make sure that the timestamp you specify is a whole minute timestamp within the past seven days, but not earlier than the`earliestVersionTime`. If data no longer exists at the specified timestamp, an error is generated. The timestamp must be a whole minute, even if the specified time is within the past hour.
   - You are not charged for a failed PITR export.
2. Import to a database.

   Use the steps in[Import all documents](https://firebase.google.com/docs/firestore/enterprise/export-import#import_all_documents_from_an_export)to import your exported database. If any document already exists in your database, it will be overwritten.