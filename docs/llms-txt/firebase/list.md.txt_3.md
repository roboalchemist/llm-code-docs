# Source: https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.collectionGroups.indexes/list.md.txt

Lists composite indexes.

### HTTP request

Choose a location:
<button value="global" default="">global</button> <button value="africa-south1">africa-south1</button> <button value="asia-east1">asia-east1</button> <button value="asia-east2">asia-east2</button> <button value="asia-northeast1">asia-northeast1</button> <button value="asia-northeast2">asia-northeast2</button> <button value="asia-northeast3">asia-northeast3</button> <button value="asia-south1">asia-south1</button> <button value="asia-south2">asia-south2</button> <button value="asia-southeast1">asia-southeast1</button> <button value="asia-southeast2">asia-southeast2</button> <button value="asia-southeast3">asia-southeast3</button> <button value="australia-southeast1">australia-southeast1</button> <button value="australia-southeast2">australia-southeast2</button> <button value="europe-central2">europe-central2</button> <button value="europe-north1">europe-north1</button> <button value="europe-north2">europe-north2</button> <button value="europe-southwest1">europe-southwest1</button> <button value="europe-west1">europe-west1</button> <button value="europe-west10">europe-west10</button> <button value="europe-west12">europe-west12</button> <button value="europe-west15">europe-west15</button> <button value="europe-west2">europe-west2</button> <button value="europe-west3">europe-west3</button> <button value="europe-west4">europe-west4</button> <button value="europe-west6">europe-west6</button> <button value="europe-west8">europe-west8</button> <button value="europe-west9">europe-west9</button> <button value="me-central1">me-central1</button> <button value="me-central2">me-central2</button> <button value="me-west1">me-west1</button> <button value="northamerica-northeast1">northamerica-northeast1</button> <button value="northamerica-northeast2">northamerica-northeast2</button> <button value="northamerica-south1">northamerica-south1</button> <button value="southamerica-east1">southamerica-east1</button> <button value="southamerica-west1">southamerica-west1</button> <button value="us-central1">us-central1</button> <button value="us-east1">us-east1</button> <button value="us-east4">us-east4</button> <button value="us-east5">us-east5</button> <button value="us-south1">us-south1</button> <button value="us-west1">us-west1</button> <button value="us-west2">us-west2</button> <button value="us-west3">us-west3</button> <button value="us-west4">us-west4</button> <button value="eu">eu</button> <button value="us">us</button>   
`GET https://firestore.googleapis.com/v1/{parent=projects/*/databases/*/collectionGroups/*}/indexes`

<br />

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `parent` | `string` Required. A parent name of the form `projects/{projectId}/databases/{databaseId}/collectionGroups/{collectionId}` |

### Query parameters

| Parameters ||
|---|---|
| `filter` | `string` The filter to apply to list results. |
| `pageSize` | `integer` The number of results to return. |
| `pageToken` | `string` A page token, returned from a previous call to `https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.collectionGroups.indexes/list#google.firestore.admin.v1.FirestoreAdmin.ListIndexes`, that may be used to get the next page of results. |

### Request body

The request body must be empty.

### Response body

The response for `https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.collectionGroups.indexes/list#google.firestore.admin.v1.FirestoreAdmin.ListIndexes`.

If successful, the response body contains data with the following structure:

| JSON representation |
|---|
| ``` { "indexes": [ { object (`https://firebase.google.com/docs/firestore/reference/rest/Shared.Types/FieldOperationMetadata#Index`) } ], "nextPageToken": string } ``` |

| Fields ||
|---|---|
| `indexes[]` | ``object (`https://firebase.google.com/docs/firestore/reference/rest/Shared.Types/FieldOperationMetadata#Index`)`` The requested indexes. |
| `nextPageToken` | `string` A page token that may be used to request another page of results. If blank, this is the last page. |

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/datastore`
- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).