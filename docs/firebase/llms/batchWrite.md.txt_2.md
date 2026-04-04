# Source: https://firebase.google.com/docs/firestore/reference/rest/v1beta1/projects.databases.documents/batchWrite.md.txt

Applies a batch of write operations.

The documents.batchWrite method does not apply the write operations atomically and can apply them out of order. Method does not allow more than one write per document. Each write succeeds or fails independently. See the `https://firebase.google.com/docs/firestore/reference/rest/v1beta1/projects.databases.documents/batchWrite#body.BatchWriteResponse` for the success status of each write.

If you require an atomically applied set of writes, use `https://firebase.google.com/docs/firestore/reference/rest/v1beta1/projects.databases.documents/commit#google.firestore.v1beta1.Firestore.Commit` instead.

### HTTP request

Choose a location:
<button value="global" default="">global</button> <button value="africa-south1">africa-south1</button> <button value="asia-east1">asia-east1</button> <button value="asia-east2">asia-east2</button> <button value="asia-northeast1">asia-northeast1</button> <button value="asia-northeast2">asia-northeast2</button> <button value="asia-northeast3">asia-northeast3</button> <button value="asia-south1">asia-south1</button> <button value="asia-south2">asia-south2</button> <button value="asia-southeast1">asia-southeast1</button> <button value="asia-southeast2">asia-southeast2</button> <button value="asia-southeast3">asia-southeast3</button> <button value="australia-southeast1">australia-southeast1</button> <button value="australia-southeast2">australia-southeast2</button> <button value="europe-central2">europe-central2</button> <button value="europe-north1">europe-north1</button> <button value="europe-north2">europe-north2</button> <button value="europe-southwest1">europe-southwest1</button> <button value="europe-west1">europe-west1</button> <button value="europe-west10">europe-west10</button> <button value="europe-west12">europe-west12</button> <button value="europe-west15">europe-west15</button> <button value="europe-west2">europe-west2</button> <button value="europe-west3">europe-west3</button> <button value="europe-west4">europe-west4</button> <button value="europe-west6">europe-west6</button> <button value="europe-west8">europe-west8</button> <button value="europe-west9">europe-west9</button> <button value="me-central1">me-central1</button> <button value="me-central2">me-central2</button> <button value="me-west1">me-west1</button> <button value="northamerica-northeast1">northamerica-northeast1</button> <button value="northamerica-northeast2">northamerica-northeast2</button> <button value="northamerica-south1">northamerica-south1</button> <button value="southamerica-east1">southamerica-east1</button> <button value="southamerica-west1">southamerica-west1</button> <button value="us-central1">us-central1</button> <button value="us-east1">us-east1</button> <button value="us-east4">us-east4</button> <button value="us-east5">us-east5</button> <button value="us-south1">us-south1</button> <button value="us-west1">us-west1</button> <button value="us-west2">us-west2</button> <button value="us-west3">us-west3</button> <button value="us-west4">us-west4</button> <button value="eu">eu</button> <button value="us">us</button>   
`POST https://firestore.googleapis.com/v1beta1/{database=projects/*/databases/*}/documents:batchWrite`

<br />

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `database` | `string` Required. The database name. In the format: `projects/{projectId}/databases/{databaseId}`. |

### Request body

The request body contains data with the following structure:

| JSON representation |
|---|
| ``` { "writes": [ { object (`https://firebase.google.com/docs/firestore/reference/rest/v1beta1/Write`) } ], "labels": { string: string, ... } } ``` |

| Fields ||
|---|---|
| `writes[]` | ``object (`https://firebase.google.com/docs/firestore/reference/rest/v1beta1/Write`)`` The writes to apply. Method does not apply writes atomically and does not guarantee ordering. Each write succeeds or fails independently. You cannot write to the same document more than once per request. |
| `labels` | `map (key: string, value: string)` Labels associated with this batch write. An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`. |

### Response body

The response from `https://firebase.google.com/docs/firestore/reference/rest/v1beta1/projects.databases.documents/batchWrite#google.firestore.v1beta1.Firestore.BatchWrite`.

If successful, the response body contains data with the following structure:

| JSON representation |
|---|
| ``` { "writeResults": [ { object (`https://firebase.google.com/docs/firestore/reference/rest/v1beta1/WriteResult`) } ], "status": [ { object (`https://firebase.google.com/docs/firestore/reference/rest/Shared.Types/Operation#Status`) } ] } ``` |

| Fields ||
|---|---|
| `writeResults[]` | ``object (`https://firebase.google.com/docs/firestore/reference/rest/v1beta1/WriteResult`)`` The result of applying the writes. This i-th write result corresponds to the i-th write in the request. |
| `status[]` | ``object (`https://firebase.google.com/docs/firestore/reference/rest/Shared.Types/Operation#Status`)`` The status of applying the writes. This i-th write status corresponds to the i-th write in the request. |

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/datastore`
- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).