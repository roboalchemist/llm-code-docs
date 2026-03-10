# Source: https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases/restore.md.txt

Creates a new database by restoring from an existing backup.

The new database must be in the same cloud region or multi-region location as the existing backup. This behaves similar to `https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases/create#google.firestore.admin.v1.FirestoreAdmin.CreateDatabase` except instead of creating a new empty database, a new database is created with the database type, index configuration, and documents from an existing backup.

The `https://firebase.google.com/docs/firestore/reference/rest/Shared.Types/Operation` can be used to track the progress of the restore, with the Operation's `https://firebase.google.com/docs/firestore/reference/rest/Shared.Types/Operation#FIELDS.metadata` field type being the `https://firebase.google.com/docs/firestore/reference/rest/Shared.Types/RestoreDatabaseMetadata`. The `https://firebase.google.com/docs/firestore/reference/rest/Shared.Types/Operation#FIELDS.response` type is the `https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases#Database` if the restore was successful. The new database is not readable or writeable until the LRO has completed.

### HTTP request

Choose a location:
<button value="global" default="">global</button> <button value="africa-south1">africa-south1</button> <button value="asia-east1">asia-east1</button> <button value="asia-east2">asia-east2</button> <button value="asia-northeast1">asia-northeast1</button> <button value="asia-northeast2">asia-northeast2</button> <button value="asia-northeast3">asia-northeast3</button> <button value="asia-south1">asia-south1</button> <button value="asia-south2">asia-south2</button> <button value="asia-southeast1">asia-southeast1</button> <button value="asia-southeast2">asia-southeast2</button> <button value="asia-southeast3">asia-southeast3</button> <button value="australia-southeast1">australia-southeast1</button> <button value="australia-southeast2">australia-southeast2</button> <button value="europe-central2">europe-central2</button> <button value="europe-north1">europe-north1</button> <button value="europe-north2">europe-north2</button> <button value="europe-southwest1">europe-southwest1</button> <button value="europe-west1">europe-west1</button> <button value="europe-west10">europe-west10</button> <button value="europe-west12">europe-west12</button> <button value="europe-west15">europe-west15</button> <button value="europe-west2">europe-west2</button> <button value="europe-west3">europe-west3</button> <button value="europe-west4">europe-west4</button> <button value="europe-west6">europe-west6</button> <button value="europe-west8">europe-west8</button> <button value="europe-west9">europe-west9</button> <button value="me-central1">me-central1</button> <button value="me-central2">me-central2</button> <button value="me-west1">me-west1</button> <button value="northamerica-northeast1">northamerica-northeast1</button> <button value="northamerica-northeast2">northamerica-northeast2</button> <button value="northamerica-south1">northamerica-south1</button> <button value="southamerica-east1">southamerica-east1</button> <button value="southamerica-west1">southamerica-west1</button> <button value="us-central1">us-central1</button> <button value="us-east1">us-east1</button> <button value="us-east4">us-east4</button> <button value="us-east5">us-east5</button> <button value="us-south1">us-south1</button> <button value="us-west1">us-west1</button> <button value="us-west2">us-west2</button> <button value="us-west3">us-west3</button> <button value="us-west4">us-west4</button> <button value="eu">eu</button> <button value="us">us</button>   
`POST https://firestore.googleapis.com/v1/{parent=projects/*}/databases:restore`

<br />

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `parent` | `string` Required. The project to restore the database in. Format is `projects/{projectId}`. |

### Request body

The request body contains data with the following structure:

| JSON representation |
|---|
| ``` { "databaseId": string, "backup": string, "encryptionConfig": { object (`https://firebase.google.com/docs/firestore/reference/rest/v1/EncryptionConfig`) }, "tags": { string: string, ... } } ``` |

| Fields ||
|---|---|
| `databaseId` | `string` Required. The ID to use for the database, which will become the final component of the database's resource name. This database ID must not be associated with an existing database. This value should be 4-63 characters. Valid characters are /\[a-z\]\[0-9\]-/ with first character a letter and the last a letter or a number. Must not be UUID-like /\[0-9a-f\]{8}(-\[0-9a-f\]{4}){3}-\[0-9a-f\]{12}/. "(default)" database ID is also valid if the database is Standard edition. |
| `backup` | `string` Required. Backup to restore from. Must be from the same project as the parent. The restored database will be created in the same location as the source backup. Format is: `projects/{projectId}/locations/{location}/backups/{backup}` |
| `encryptionConfig` | ``object (`https://firebase.google.com/docs/firestore/reference/rest/v1/EncryptionConfig`)`` Optional. Encryption configuration for the restored database. If this field is not specified, the restored database will use the same encryption configuration as the backup, namely `https://firebase.google.com/docs/firestore/reference/rest/v1/EncryptionConfig#FIELDS.use_source_encryption`. |
| `tags` | `map (key: string, value: string)` Optional. Immutable. Tags to be bound to the restored database. The tags should be provided in the format of `tagKeys/{tag_key_id} -> tagValues/{tag_value_id}`. An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`. |

### Response body

If successful, the response body contains an instance of `https://firebase.google.com/docs/firestore/reference/rest/Shared.Types/Operation`.

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/datastore`
- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).