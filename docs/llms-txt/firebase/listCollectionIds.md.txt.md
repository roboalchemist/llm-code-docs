# Source: https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.documents/listCollectionIds.md.txt

Lists all the collection IDs underneath a document.

### HTTP request

Choose a location:
<button value="global" default="">global</button> <button value="africa-south1">africa-south1</button> <button value="asia-east1">asia-east1</button> <button value="asia-east2">asia-east2</button> <button value="asia-northeast1">asia-northeast1</button> <button value="asia-northeast2">asia-northeast2</button> <button value="asia-northeast3">asia-northeast3</button> <button value="asia-south1">asia-south1</button> <button value="asia-south2">asia-south2</button> <button value="asia-southeast1">asia-southeast1</button> <button value="asia-southeast2">asia-southeast2</button> <button value="asia-southeast3">asia-southeast3</button> <button value="australia-southeast1">australia-southeast1</button> <button value="australia-southeast2">australia-southeast2</button> <button value="europe-central2">europe-central2</button> <button value="europe-north1">europe-north1</button> <button value="europe-north2">europe-north2</button> <button value="europe-southwest1">europe-southwest1</button> <button value="europe-west1">europe-west1</button> <button value="europe-west10">europe-west10</button> <button value="europe-west12">europe-west12</button> <button value="europe-west15">europe-west15</button> <button value="europe-west2">europe-west2</button> <button value="europe-west3">europe-west3</button> <button value="europe-west4">europe-west4</button> <button value="europe-west6">europe-west6</button> <button value="europe-west8">europe-west8</button> <button value="europe-west9">europe-west9</button> <button value="me-central1">me-central1</button> <button value="me-central2">me-central2</button> <button value="me-west1">me-west1</button> <button value="northamerica-northeast1">northamerica-northeast1</button> <button value="northamerica-northeast2">northamerica-northeast2</button> <button value="northamerica-south1">northamerica-south1</button> <button value="southamerica-east1">southamerica-east1</button> <button value="southamerica-west1">southamerica-west1</button> <button value="us-central1">us-central1</button> <button value="us-east1">us-east1</button> <button value="us-east4">us-east4</button> <button value="us-east5">us-east5</button> <button value="us-south1">us-south1</button> <button value="us-west1">us-west1</button> <button value="us-west2">us-west2</button> <button value="us-west3">us-west3</button> <button value="us-west4">us-west4</button> <button value="eu">eu</button> <button value="us">us</button>   
`POST https://firestore.googleapis.com/v1/{parent=projects/*/databases/*/documents}:listCollectionIds`

<br />

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `parent` | `string` Required. The parent document. In the format: `projects/{projectId}/databases/{databaseId}/documents/{document_path}`. For example: `projects/my-project/databases/my-database/documents/chatrooms/my-chatroom` |

### Request body

The request body contains data with the following structure:

| JSON representation |
|---|
| ``` { "pageSize": integer, "pageToken": string, // Union field `consistency_selector` can be only one of the following: "readTime": string // End of list of possible types for union field `consistency_selector`. } ``` |

| Fields ||
|---|---|
| `pageSize` | `integer` The maximum number of results to return. |
| `pageToken` | `string` A page token. Must be a value from `https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.documents/listCollectionIds#body.ListCollectionIdsResponse`. |
| Union field `consistency_selector`. The consistency mode for this request. If not set, defaults to strong consistency. `consistency_selector` can be only one of the following: ||
| `readTime` | ``string (`https://protobuf.dev/reference/protobuf/google.protobuf#timestamp` format)`` Reads documents as they were at the given time. This must be a microsecond precision timestamp within the past one hour, or if Point-in-Time Recovery is enabled, can additionally be a whole minute timestamp within the past 7 days. Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. |

### Response body

The response from `https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.documents/listCollectionIds#google.firestore.v1.Firestore.ListCollectionIds`.

If successful, the response body contains data with the following structure:

| JSON representation |
|---|
| ``` { "collectionIds": [ string ], "nextPageToken": string } ``` |

| Fields ||
|---|---|
| `collectionIds[]` | `string` The collection ids. |
| `nextPageToken` | `string` A page token that may be used to continue the list. |

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/datastore`
- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).