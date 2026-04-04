# Source: https://firebase.google.com/docs/firestore/reference/rest.md.txt

Accesses the NoSQL document database built for automatic scaling, high performance, and ease of application development.

## Service: firestore.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery documents:

- <https://firestore.googleapis.com/$discovery/rest?version=v1>
- <https://firestore.googleapis.com/$discovery/rest?version=v1beta2>
- <https://firestore.googleapis.com/$discovery/rest?version=v1beta1>

### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

- `https://firestore.googleapis.com`

### Regional service endpoint

A regional service endpoint is a base URL that specifies the network address of an API service in a single region. A service that is available in multiple regions might have multiple regional endpoints. Select a location to see its regional service endpoint for this service.
<button value="global" default="">global</button> <button value="africa-south1">africa-south1</button> <button value="asia-east1">asia-east1</button> <button value="asia-east2">asia-east2</button> <button value="asia-northeast1">asia-northeast1</button> <button value="asia-northeast2">asia-northeast2</button> <button value="asia-northeast3">asia-northeast3</button> <button value="asia-south1">asia-south1</button> <button value="asia-south2">asia-south2</button> <button value="asia-southeast1">asia-southeast1</button> <button value="asia-southeast2">asia-southeast2</button> <button value="asia-southeast3">asia-southeast3</button> <button value="australia-southeast1">australia-southeast1</button> <button value="australia-southeast2">australia-southeast2</button> <button value="europe-central2">europe-central2</button> <button value="europe-north1">europe-north1</button> <button value="europe-north2">europe-north2</button> <button value="europe-southwest1">europe-southwest1</button> <button value="europe-west1">europe-west1</button> <button value="europe-west10">europe-west10</button> <button value="europe-west12">europe-west12</button> <button value="europe-west15">europe-west15</button> <button value="europe-west2">europe-west2</button> <button value="europe-west3">europe-west3</button> <button value="europe-west4">europe-west4</button> <button value="europe-west6">europe-west6</button> <button value="europe-west8">europe-west8</button> <button value="europe-west9">europe-west9</button> <button value="me-central1">me-central1</button> <button value="me-central2">me-central2</button> <button value="me-west1">me-west1</button> <button value="northamerica-northeast1">northamerica-northeast1</button> <button value="northamerica-northeast2">northamerica-northeast2</button> <button value="northamerica-south1">northamerica-south1</button> <button value="southamerica-east1">southamerica-east1</button> <button value="southamerica-west1">southamerica-west1</button> <button value="us-central1">us-central1</button> <button value="us-east1">us-east1</button> <button value="us-east4">us-east4</button> <button value="us-east5">us-east5</button> <button value="us-south1">us-south1</button> <button value="us-west1">us-west1</button> <button value="us-west2">us-west2</button> <button value="us-west3">us-west3</button> <button value="us-west4">us-west4</button> <button value="eu">eu</button> <button value="us">us</button>   
- `https://firestore.googleapis.com`

<br />

## REST Resource: [v1beta2.projects.databases](https://firebase.google.com/docs/firestore/reference/rest/v1beta2/projects.databases)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/firestore/reference/rest/v1beta2/projects.databases/exportDocuments` | `POST /v1beta2/{name=projects/*/databases/*}:exportDocuments` Exports a copy of all or a subset of documents from Google Cloud Firestore to another storage system, such as Google Cloud Storage. |
| `https://firebase.google.com/docs/firestore/reference/rest/v1beta2/projects.databases/importDocuments` | `POST /v1beta2/{name=projects/*/databases/*}:importDocuments` Imports documents into Google Cloud Firestore. |

## REST Resource: [v1beta2.projects.databases.collectionGroups.fields](https://firebase.google.com/docs/firestore/reference/rest/v1beta2/projects.databases.collectionGroups.fields)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/firestore/reference/rest/v1beta2/projects.databases.collectionGroups.fields/get` | `GET /v1beta2/{name=projects/*/databases/*/collectionGroups/*/fields/*}` Gets the metadata and configuration for a Field. |
| `https://firebase.google.com/docs/firestore/reference/rest/v1beta2/projects.databases.collectionGroups.fields/list` | `GET /v1beta2/{parent=projects/*/databases/*/collectionGroups/*}/fields` Lists the field configuration and metadata for this database. |
| `https://firebase.google.com/docs/firestore/reference/rest/v1beta2/projects.databases.collectionGroups.fields/patch` | `PATCH /v1beta2/{field.name=projects/*/databases/*/collectionGroups/*/fields/*}` Updates a field configuration. |

## REST Resource: [v1beta2.projects.databases.collectionGroups.indexes](https://firebase.google.com/docs/firestore/reference/rest/v1beta2/projects.databases.collectionGroups.indexes)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/firestore/reference/rest/v1beta2/projects.databases.collectionGroups.indexes/create` | `POST /v1beta2/{parent=projects/*/databases/*/collectionGroups/*}/indexes` Creates a composite index. |
| `https://firebase.google.com/docs/firestore/reference/rest/v1beta2/projects.databases.collectionGroups.indexes/delete` | `DELETE /v1beta2/{name=projects/*/databases/*/collectionGroups/*/indexes/*}` Deletes a composite index. |
| `https://firebase.google.com/docs/firestore/reference/rest/v1beta2/projects.databases.collectionGroups.indexes/get` | `GET /v1beta2/{name=projects/*/databases/*/collectionGroups/*/indexes/*}` Gets a composite index. |
| `https://firebase.google.com/docs/firestore/reference/rest/v1beta2/projects.databases.collectionGroups.indexes/list` | `GET /v1beta2/{parent=projects/*/databases/*/collectionGroups/*}/indexes` Lists composite indexes. |

## REST Resource: [v1beta1.projects.databases](https://firebase.google.com/docs/firestore/reference/rest/v1beta1/projects.databases)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/firestore/reference/rest/v1beta1/projects.databases/exportDocuments` | `POST /v1beta1/{name=projects/*/databases/*}:exportDocuments` Exports a copy of all or a subset of documents from Google Cloud Firestore to another storage system, such as Google Cloud Storage. |
| `https://firebase.google.com/docs/firestore/reference/rest/v1beta1/projects.databases/importDocuments` | `POST /v1beta1/{name=projects/*/databases/*}:importDocuments` Imports documents into Google Cloud Firestore. |

## REST Resource: [v1beta1.projects.databases.documents](https://firebase.google.com/docs/firestore/reference/rest/v1beta1/projects.databases.documents)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/firestore/reference/rest/v1beta1/projects.databases.documents/batchGet` | `POST /v1beta1/{database=projects/*/databases/*}/documents:batchGet` Gets multiple documents. |
| `https://firebase.google.com/docs/firestore/reference/rest/v1beta1/projects.databases.documents/batchWrite` | `POST /v1beta1/{database=projects/*/databases/*}/documents:batchWrite` Applies a batch of write operations. |
| `https://firebase.google.com/docs/firestore/reference/rest/v1beta1/projects.databases.documents/beginTransaction` | `POST /v1beta1/{database=projects/*/databases/*}/documents:beginTransaction` Starts a new transaction. |
| `https://firebase.google.com/docs/firestore/reference/rest/v1beta1/projects.databases.documents/commit` | `POST /v1beta1/{database=projects/*/databases/*}/documents:commit` Commits a transaction, while optionally updating documents. |
| `https://firebase.google.com/docs/firestore/reference/rest/v1beta1/projects.databases.documents/createDocument` | `POST /v1beta1/{parent=projects/*/databases/*/documents/**}/{collectionId}` Creates a new document. |
| `https://firebase.google.com/docs/firestore/reference/rest/v1beta1/projects.databases.documents/delete` | `DELETE /v1beta1/{name=projects/*/databases/*/documents/*/**}` Deletes a document. |
| `https://firebase.google.com/docs/firestore/reference/rest/v1beta1/projects.databases.documents/executePipeline` | `POST /v1beta1/{database=projects/*/databases/*}/documents:executePipeline` Executes a pipeline query. |
| `https://firebase.google.com/docs/firestore/reference/rest/v1beta1/projects.databases.documents/get` | `GET /v1beta1/{name=projects/*/databases/*/documents/*/**}` Gets a single document. |
| `https://firebase.google.com/docs/firestore/reference/rest/v1beta1/projects.databases.documents/list` | `GET /v1beta1/{parent=projects/*/databases/*/documents/*/**}/{collectionId}` Lists documents. |
| `https://firebase.google.com/docs/firestore/reference/rest/v1beta1/projects.databases.documents/listCollectionIds` | `POST /v1beta1/{parent=projects/*/databases/*/documents}:listCollectionIds` Lists all the collection IDs underneath a document. |
| `https://firebase.google.com/docs/firestore/reference/rest/v1beta1/projects.databases.documents/listDocuments` | `GET /v1beta1/{parent=projects/*/databases/*/documents}/{collectionId}` Lists documents. |
| `https://firebase.google.com/docs/firestore/reference/rest/v1beta1/projects.databases.documents/listen` | `POST /v1beta1/{database=projects/*/databases/*}/documents:listen` Listens to changes. |
| `https://firebase.google.com/docs/firestore/reference/rest/v1beta1/projects.databases.documents/partitionQuery` | `POST /v1beta1/{parent=projects/*/databases/*/documents}:partitionQuery` Partitions a query by returning partition cursors that can be used to run the query in parallel. |
| `https://firebase.google.com/docs/firestore/reference/rest/v1beta1/projects.databases.documents/patch` | `PATCH /v1beta1/{document.name=projects/*/databases/*/documents/*/**}` Updates or inserts a document. |
| `https://firebase.google.com/docs/firestore/reference/rest/v1beta1/projects.databases.documents/rollback` | `POST /v1beta1/{database=projects/*/databases/*}/documents:rollback` Rolls back a transaction. |
| `https://firebase.google.com/docs/firestore/reference/rest/v1beta1/projects.databases.documents/runAggregationQuery` | `POST /v1beta1/{parent=projects/*/databases/*/documents}:runAggregationQuery` Runs an aggregation query. |
| `https://firebase.google.com/docs/firestore/reference/rest/v1beta1/projects.databases.documents/runQuery` | `POST /v1beta1/{parent=projects/*/databases/*/documents}:runQuery` Runs a query. |
| `https://firebase.google.com/docs/firestore/reference/rest/v1beta1/projects.databases.documents/write` | `POST /v1beta1/{database=projects/*/databases/*}/documents:write` Streams batches of document updates and deletes, in order. |

## REST Resource: [v1beta1.projects.databases.indexes](https://firebase.google.com/docs/firestore/reference/rest/v1beta1/projects.databases.indexes)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/firestore/reference/rest/v1beta1/projects.databases.indexes/create` | `POST /v1beta1/{parent=projects/*/databases/*}/indexes` Creates the specified index. |
| `https://firebase.google.com/docs/firestore/reference/rest/v1beta1/projects.databases.indexes/delete` | `DELETE /v1beta1/{name=projects/*/databases/*/indexes/*}` Deletes an index. |
| `https://firebase.google.com/docs/firestore/reference/rest/v1beta1/projects.databases.indexes/get` | `GET /v1beta1/{name=projects/*/databases/*/indexes/*}` Gets an index. |
| `https://firebase.google.com/docs/firestore/reference/rest/v1beta1/projects.databases.indexes/list` | `GET /v1beta1/{parent=projects/*/databases/*}/indexes` Lists the indexes that match the specified filters. |

## REST Resource: [v1.projects.databases](https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases/bulkDeleteDocuments` | `POST /v1/{name=projects/*/databases/*}:bulkDeleteDocuments` Bulk deletes a subset of documents from Google Cloud Firestore. |
| `https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases/clone` | `POST /v1/{parent=projects/*}/databases:clone` Creates a new database by cloning an existing one. |
| `https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases/create` | `POST /v1/{parent=projects/*}/databases` Create a database. |
| `https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases/delete` | `DELETE /v1/{name=projects/*/databases/*}` Deletes a database. |
| `https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases/exportDocuments` | `POST /v1/{name=projects/*/databases/*}:exportDocuments` Exports a copy of all or a subset of documents from Google Cloud Firestore to another storage system, such as Google Cloud Storage. |
| `https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases/get` | `GET /v1/{name=projects/*/databases/*}` Gets information about a database. |
| `https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases/importDocuments` | `POST /v1/{name=projects/*/databases/*}:importDocuments` Imports documents into Google Cloud Firestore. |
| `https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases/list` | `GET /v1/{parent=projects/*}/databases` List all the databases in the project. |
| `https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases/patch` | `PATCH /v1/{database.name=projects/*/databases/*}` Updates a database. |
| `https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases/restore` | `POST /v1/{parent=projects/*}/databases:restore` Creates a new database by restoring from an existing backup. |

## REST Resource: [v1.projects.databases.backupSchedules](https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.backupSchedules)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.backupSchedules/create` | `POST /v1/{parent=projects/*/databases/*}/backupSchedules` Creates a backup schedule on a database. |
| `https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.backupSchedules/delete` | `DELETE /v1/{name=projects/*/databases/*/backupSchedules/*}` Deletes a backup schedule. |
| `https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.backupSchedules/get` | `GET /v1/{name=projects/*/databases/*/backupSchedules/*}` Gets information about a backup schedule. |
| `https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.backupSchedules/list` | `GET /v1/{parent=projects/*/databases/*}/backupSchedules` List backup schedules. |
| `https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.backupSchedules/patch` | `PATCH /v1/{backupSchedule.name=projects/*/databases/*/backupSchedules/*}` Updates a backup schedule. |

## REST Resource: [v1.projects.databases.collectionGroups.fields](https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.collectionGroups.fields)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.collectionGroups.fields/get` | `GET /v1/{name=projects/*/databases/*/collectionGroups/*/fields/*}` Gets the metadata and configuration for a Field. |
| `https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.collectionGroups.fields/list` | `GET /v1/{parent=projects/*/databases/*/collectionGroups/*}/fields` Lists the field configuration and metadata for this database. |
| `https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.collectionGroups.fields/patch` | `PATCH /v1/{field.name=projects/*/databases/*/collectionGroups/*/fields/*}` Updates a field configuration. |

## REST Resource: [v1.projects.databases.collectionGroups.indexes](https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.collectionGroups.indexes)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.collectionGroups.indexes/create` | `POST /v1/{parent=projects/*/databases/*/collectionGroups/*}/indexes` Creates a composite index. |
| `https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.collectionGroups.indexes/delete` | `DELETE /v1/{name=projects/*/databases/*/collectionGroups/*/indexes/*}` Deletes a composite index. |
| `https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.collectionGroups.indexes/get` | `GET /v1/{name=projects/*/databases/*/collectionGroups/*/indexes/*}` Gets a composite index. |
| `https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.collectionGroups.indexes/list` | `GET /v1/{parent=projects/*/databases/*/collectionGroups/*}/indexes` Lists composite indexes. |

## REST Resource: [v1.projects.databases.documents](https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.documents)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.documents/batchGet` | `POST /v1/{database=projects/*/databases/*}/documents:batchGet` Gets multiple documents. |
| `https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.documents/batchWrite` | `POST /v1/{database=projects/*/databases/*}/documents:batchWrite` Applies a batch of write operations. |
| `https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.documents/beginTransaction` | `POST /v1/{database=projects/*/databases/*}/documents:beginTransaction` Starts a new transaction. |
| `https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.documents/commit` | `POST /v1/{database=projects/*/databases/*}/documents:commit` Commits a transaction, while optionally updating documents. |
| `https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.documents/createDocument` | `POST /v1/{parent=projects/*/databases/*/documents/**}/{collectionId}` Creates a new document. |
| `https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.documents/delete` | `DELETE /v1/{name=projects/*/databases/*/documents/*/**}` Deletes a document. |
| `https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.documents/executePipeline` | `POST /v1/{database=projects/*/databases/*}/documents:executePipeline` Executes a pipeline query. |
| `https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.documents/get` | `GET /v1/{name=projects/*/databases/*/documents/*/**}` Gets a single document. |
| `https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.documents/list` | `GET /v1/{parent=projects/*/databases/*/documents/*/**}/{collectionId}` Lists documents. |
| `https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.documents/listCollectionIds` | `POST /v1/{parent=projects/*/databases/*/documents}:listCollectionIds` Lists all the collection IDs underneath a document. |
| `https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.documents/listDocuments` | `GET /v1/{parent=projects/*/databases/*/documents}/{collectionId}` Lists documents. |
| `https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.documents/listen` | `POST /v1/{database=projects/*/databases/*}/documents:listen` Listens to changes. |
| `https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.documents/partitionQuery` | `POST /v1/{parent=projects/*/databases/*/documents}:partitionQuery` Partitions a query by returning partition cursors that can be used to run the query in parallel. |
| `https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.documents/patch` | `PATCH /v1/{document.name=projects/*/databases/*/documents/*/**}` Updates or inserts a document. |
| `https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.documents/rollback` | `POST /v1/{database=projects/*/databases/*}/documents:rollback` Rolls back a transaction. |
| `https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.documents/runAggregationQuery` | `POST /v1/{parent=projects/*/databases/*/documents}:runAggregationQuery` Runs an aggregation query. |
| `https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.documents/runQuery` | `POST /v1/{parent=projects/*/databases/*/documents}:runQuery` Runs a query. |
| `https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.documents/write` | `POST /v1/{database=projects/*/databases/*}/documents:write` Streams batches of document updates and deletes, in order. |

## REST Resource: [v1.projects.databases.operations](https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.operations)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.operations/cancel` | `POST /v1/{name=projects/*/databases/*/operations/*}:cancel` Starts asynchronous cancellation on a long-running operation. |
| `https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.operations/delete` | `DELETE /v1/{name=projects/*/databases/*/operations/*}` Deletes a long-running operation. |
| `https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.operations/get` | `GET /v1/{name=projects/*/databases/*/operations/*}` Gets the latest state of a long-running operation. |
| `https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.operations/list` | `GET /v1/{name=projects/*/databases/*}/operations` Lists operations that match the specified filter in the request. |

## REST Resource: [v1.projects.databases.userCreds](https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.userCreds)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.userCreds/create` | `POST /v1/{parent=projects/*/databases/*}/userCreds` Create a user creds. |
| `https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.userCreds/delete` | `DELETE /v1/{name=projects/*/databases/*/userCreds/*}` Deletes a user creds. |
| `https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.userCreds/disable` | `POST /v1/{name=projects/*/databases/*/userCreds/*}:disable` Disables a user creds. |
| `https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.userCreds/enable` | `POST /v1/{name=projects/*/databases/*/userCreds/*}:enable` Enables a user creds. |
| `https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.userCreds/get` | `GET /v1/{name=projects/*/databases/*/userCreds/*}` Gets a user creds resource. |
| `https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.userCreds/list` | `GET /v1/{parent=projects/*/databases/*}/userCreds` List all user creds in the database. |
| `https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.userCreds/resetPassword` | `POST /v1/{name=projects/*/databases/*/userCreds/*}:resetPassword` Resets the password of a user creds. |

## REST Resource: [v1.projects.locations](https://firebase.google.com/docs/firestore/reference/rest/v1/projects.locations)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/firestore/reference/rest/v1/projects.locations/get` | `GET /v1/{name=projects/*/locations/*}` Gets information about a location. |
| `https://firebase.google.com/docs/firestore/reference/rest/v1/projects.locations/list` | `GET /v1/{name=projects/*}/locations` Lists information about the supported locations for this service. |

## REST Resource: [v1.projects.locations.backups](https://firebase.google.com/docs/firestore/reference/rest/v1/projects.locations.backups)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/firestore/reference/rest/v1/projects.locations.backups/delete` | `DELETE /v1/{name=projects/*/locations/*/backups/*}` Deletes a backup. |
| `https://firebase.google.com/docs/firestore/reference/rest/v1/projects.locations.backups/get` | `GET /v1/{name=projects/*/locations/*/backups/*}` Gets information about a backup. |
| `https://firebase.google.com/docs/firestore/reference/rest/v1/projects.locations.backups/list` | `GET /v1/{parent=projects/*/locations/*}/backups` Lists all the backups. |