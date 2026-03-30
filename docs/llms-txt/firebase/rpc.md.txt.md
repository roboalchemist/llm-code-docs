# Source: https://firebase.google.com/docs/firestore/reference/rpc.md.txt

# Cloud Firestore API

Accesses the NoSQL document database built for automatic scaling, high performance, and ease of application development.

## Service: firestore.googleapis.com

The Service name `firestore.googleapis.com` is needed to create RPC client stubs.

## `https://firebase.google.com/docs/firestore/reference/rpc/google.cloud.location#google.cloud.location.Locations`

| Methods ||
|---|---|
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.cloud.location#google.cloud.location.Locations.GetLocation` `` | Gets information about a location. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.cloud.location#google.cloud.location.Locations.ListLocations` `` | Lists information about the supported locations for this service. |

## `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.admin.v1#google.firestore.admin.v1.FirestoreAdmin`

| Methods ||
|---|---|
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.admin.v1#google.firestore.admin.v1.FirestoreAdmin.BulkDeleteDocuments` `` | Bulk deletes a subset of documents from Google Cloud Firestore. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.admin.v1#google.firestore.admin.v1.FirestoreAdmin.CloneDatabase` `` | Creates a new database by cloning an existing one. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.admin.v1#google.firestore.admin.v1.FirestoreAdmin.CreateBackupSchedule` `` | Creates a backup schedule on a database. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.admin.v1#google.firestore.admin.v1.FirestoreAdmin.CreateDatabase` `` | Create a database. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.admin.v1#google.firestore.admin.v1.FirestoreAdmin.CreateIndex` `` | Creates a composite index. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.admin.v1#google.firestore.admin.v1.FirestoreAdmin.CreateUserCreds` `` | Create a user creds. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.admin.v1#google.firestore.admin.v1.FirestoreAdmin.DeleteBackup` `` | Deletes a backup. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.admin.v1#google.firestore.admin.v1.FirestoreAdmin.DeleteBackupSchedule` `` | Deletes a backup schedule. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.admin.v1#google.firestore.admin.v1.FirestoreAdmin.DeleteDatabase` `` | Deletes a database. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.admin.v1#google.firestore.admin.v1.FirestoreAdmin.DeleteIndex` `` | Deletes a composite index. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.admin.v1#google.firestore.admin.v1.FirestoreAdmin.DeleteUserCreds` `` | Deletes a user creds. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.admin.v1#google.firestore.admin.v1.FirestoreAdmin.DisableUserCreds` `` | Disables a user creds. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.admin.v1#google.firestore.admin.v1.FirestoreAdmin.EnableUserCreds` `` | Enables a user creds. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.admin.v1#google.firestore.admin.v1.FirestoreAdmin.ExportDocuments` `` | Exports a copy of all or a subset of documents from Google Cloud Firestore to another storage system, such as Google Cloud Storage. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.admin.v1#google.firestore.admin.v1.FirestoreAdmin.GetBackup` `` | Gets information about a backup. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.admin.v1#google.firestore.admin.v1.FirestoreAdmin.GetBackupSchedule` `` | Gets information about a backup schedule. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.admin.v1#google.firestore.admin.v1.FirestoreAdmin.GetDatabase` `` | Gets information about a database. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.admin.v1#google.firestore.admin.v1.FirestoreAdmin.GetField` `` | Gets the metadata and configuration for a Field. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.admin.v1#google.firestore.admin.v1.FirestoreAdmin.GetIndex` `` | Gets a composite index. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.admin.v1#google.firestore.admin.v1.FirestoreAdmin.GetUserCreds` `` | Gets a user creds resource. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.admin.v1#google.firestore.admin.v1.FirestoreAdmin.ImportDocuments` `` | Imports documents into Google Cloud Firestore. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.admin.v1#google.firestore.admin.v1.FirestoreAdmin.ListBackupSchedules` `` | List backup schedules. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.admin.v1#google.firestore.admin.v1.FirestoreAdmin.ListBackups` `` | Lists all the backups. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.admin.v1#google.firestore.admin.v1.FirestoreAdmin.ListDatabases` `` | List all the databases in the project. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.admin.v1#google.firestore.admin.v1.FirestoreAdmin.ListFields` `` | Lists the field configuration and metadata for this database. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.admin.v1#google.firestore.admin.v1.FirestoreAdmin.ListIndexes` `` | Lists composite indexes. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.admin.v1#google.firestore.admin.v1.FirestoreAdmin.ListUserCreds` `` | List all user creds in the database. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.admin.v1#google.firestore.admin.v1.FirestoreAdmin.ResetUserPassword` `` | Resets the password of a user creds. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.admin.v1#google.firestore.admin.v1.FirestoreAdmin.RestoreDatabase` `` | Creates a new database by restoring from an existing backup. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.admin.v1#google.firestore.admin.v1.FirestoreAdmin.UpdateBackupSchedule` `` | Updates a backup schedule. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.admin.v1#google.firestore.admin.v1.FirestoreAdmin.UpdateDatabase` `` | Updates a database. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.admin.v1#google.firestore.admin.v1.FirestoreAdmin.UpdateField` `` | Updates a field configuration. |

## `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.admin.v1beta1#google.firestore.admin.v1beta1.FirestoreAdmin`

| Methods ||
|---|---|
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.admin.v1beta1#google.firestore.admin.v1beta1.FirestoreAdmin.CreateIndex` `` | Creates the specified index. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.admin.v1beta1#google.firestore.admin.v1beta1.FirestoreAdmin.DeleteIndex` `` | Deletes an index. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.admin.v1beta1#google.firestore.admin.v1beta1.FirestoreAdmin.ExportDocuments` `` | Exports a copy of all or a subset of documents from Google Cloud Firestore to another storage system, such as Google Cloud Storage. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.admin.v1beta1#google.firestore.admin.v1beta1.FirestoreAdmin.GetIndex` `` | Gets an index. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.admin.v1beta1#google.firestore.admin.v1beta1.FirestoreAdmin.ImportDocuments` `` | Imports documents into Google Cloud Firestore. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.admin.v1beta1#google.firestore.admin.v1beta1.FirestoreAdmin.ListIndexes` `` | Lists the indexes that match the specified filters. |

## `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.admin.v1beta2#google.firestore.admin.v1beta2.FirestoreAdmin`

| Methods ||
|---|---|
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.admin.v1beta2#google.firestore.admin.v1beta2.FirestoreAdmin.CreateIndex` `` | Creates a composite index. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.admin.v1beta2#google.firestore.admin.v1beta2.FirestoreAdmin.DeleteIndex` `` | Deletes a composite index. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.admin.v1beta2#google.firestore.admin.v1beta2.FirestoreAdmin.ExportDocuments` `` | Exports a copy of all or a subset of documents from Google Cloud Firestore to another storage system, such as Google Cloud Storage. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.admin.v1beta2#google.firestore.admin.v1beta2.FirestoreAdmin.GetField` `` | Gets the metadata and configuration for a Field. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.admin.v1beta2#google.firestore.admin.v1beta2.FirestoreAdmin.GetIndex` `` | Gets a composite index. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.admin.v1beta2#google.firestore.admin.v1beta2.FirestoreAdmin.ImportDocuments` `` | Imports documents into Google Cloud Firestore. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.admin.v1beta2#google.firestore.admin.v1beta2.FirestoreAdmin.ListFields` `` | Lists the field configuration and metadata for this database. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.admin.v1beta2#google.firestore.admin.v1beta2.FirestoreAdmin.ListIndexes` `` | Lists composite indexes. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.admin.v1beta2#google.firestore.admin.v1beta2.FirestoreAdmin.UpdateField` `` | Updates a field configuration. |

## `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.v1#google.firestore.v1.Firestore`

| Methods ||
|---|---|
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.v1#google.firestore.v1.Firestore.BatchGetDocuments` `` | Gets multiple documents. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.v1#google.firestore.v1.Firestore.BatchWrite` `` | Applies a batch of write operations. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.v1#google.firestore.v1.Firestore.BeginTransaction` `` | Starts a new transaction. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.v1#google.firestore.v1.Firestore.Commit` `` | Commits a transaction, while optionally updating documents. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.v1#google.firestore.v1.Firestore.CreateDocument` `` | Creates a new document. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.v1#google.firestore.v1.Firestore.DeleteDocument` `` | Deletes a document. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.v1#google.firestore.v1.Firestore.ExecutePipeline` `` | Executes a pipeline query. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.v1#google.firestore.v1.Firestore.GetDocument` `` | Gets a single document. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.v1#google.firestore.v1.Firestore.ListCollectionIds` `` | Lists all the collection IDs underneath a document. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.v1#google.firestore.v1.Firestore.ListDocuments` `` | Lists documents. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.v1#google.firestore.v1.Firestore.Listen` `` | Listens to changes. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.v1#google.firestore.v1.Firestore.PartitionQuery` `` | Partitions a query by returning partition cursors that can be used to run the query in parallel. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.v1#google.firestore.v1.Firestore.Rollback` `` | Rolls back a transaction. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.v1#google.firestore.v1.Firestore.RunAggregationQuery` `` | Runs an aggregation query. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.v1#google.firestore.v1.Firestore.RunQuery` `` | Runs a query. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.v1#google.firestore.v1.Firestore.UpdateDocument` `` | Updates or inserts a document. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.v1#google.firestore.v1.Firestore.Write` `` | Streams batches of document updates and deletes, in order. |

## `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.v1beta1#google.firestore.v1beta1.Firestore`

| Methods ||
|---|---|
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.v1beta1#google.firestore.v1beta1.Firestore.BatchGetDocuments` `` | Gets multiple documents. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.v1beta1#google.firestore.v1beta1.Firestore.BatchWrite` `` | Applies a batch of write operations. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.v1beta1#google.firestore.v1beta1.Firestore.BeginTransaction` `` | Starts a new transaction. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.v1beta1#google.firestore.v1beta1.Firestore.Commit` `` | Commits a transaction, while optionally updating documents. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.v1beta1#google.firestore.v1beta1.Firestore.CreateDocument` `` | Creates a new document. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.v1beta1#google.firestore.v1beta1.Firestore.DeleteDocument` `` | Deletes a document. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.v1beta1#google.firestore.v1beta1.Firestore.ExecutePipeline` `` | Executes a pipeline query. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.v1beta1#google.firestore.v1beta1.Firestore.GetDocument` `` | Gets a single document. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.v1beta1#google.firestore.v1beta1.Firestore.ListCollectionIds` `` | Lists all the collection IDs underneath a document. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.v1beta1#google.firestore.v1beta1.Firestore.ListDocuments` `` | Lists documents. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.v1beta1#google.firestore.v1beta1.Firestore.Listen` `` | Listens to changes. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.v1beta1#google.firestore.v1beta1.Firestore.PartitionQuery` `` | Partitions a query by returning partition cursors that can be used to run the query in parallel. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.v1beta1#google.firestore.v1beta1.Firestore.Rollback` `` | Rolls back a transaction. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.v1beta1#google.firestore.v1beta1.Firestore.RunAggregationQuery` `` | Runs an aggregation query. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.v1beta1#google.firestore.v1beta1.Firestore.RunQuery` `` | Runs a query. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.v1beta1#google.firestore.v1beta1.Firestore.UpdateDocument` `` | Updates or inserts a document. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.v1beta1#google.firestore.v1beta1.Firestore.Write` `` | Streams batches of document updates and deletes, in order. |

## `https://firebase.google.com/docs/firestore/reference/rpc/google.longrunning#google.longrunning.Operations`

| Methods ||
|---|---|
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.longrunning#google.longrunning.Operations.CancelOperation` `` | Starts asynchronous cancellation on a long-running operation. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.longrunning#google.longrunning.Operations.DeleteOperation` `` | Deletes a long-running operation. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.longrunning#google.longrunning.Operations.GetOperation` `` | Gets the latest state of a long-running operation. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.longrunning#google.longrunning.Operations.ListOperations` `` | Lists operations that match the specified filter in the request. |
| `` `https://firebase.google.com/docs/firestore/reference/rpc/google.longrunning#google.longrunning.Operations.WaitOperation` `` | Waits until the specified long-running operation is done or reaches at most a specified timeout, returning the latest state. |