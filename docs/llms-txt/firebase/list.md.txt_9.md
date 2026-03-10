# Source: https://firebase.google.com/docs/firestore/reference/rest/v1beta1/projects.databases.documents/list.md.txt

Lists documents.

### HTTP request

Choose a location:
<button value="global" default="">global</button> <button value="africa-south1">africa-south1</button> <button value="asia-east1">asia-east1</button> <button value="asia-east2">asia-east2</button> <button value="asia-northeast1">asia-northeast1</button> <button value="asia-northeast2">asia-northeast2</button> <button value="asia-northeast3">asia-northeast3</button> <button value="asia-south1">asia-south1</button> <button value="asia-south2">asia-south2</button> <button value="asia-southeast1">asia-southeast1</button> <button value="asia-southeast2">asia-southeast2</button> <button value="asia-southeast3">asia-southeast3</button> <button value="australia-southeast1">australia-southeast1</button> <button value="australia-southeast2">australia-southeast2</button> <button value="europe-central2">europe-central2</button> <button value="europe-north1">europe-north1</button> <button value="europe-north2">europe-north2</button> <button value="europe-southwest1">europe-southwest1</button> <button value="europe-west1">europe-west1</button> <button value="europe-west10">europe-west10</button> <button value="europe-west12">europe-west12</button> <button value="europe-west15">europe-west15</button> <button value="europe-west2">europe-west2</button> <button value="europe-west3">europe-west3</button> <button value="europe-west4">europe-west4</button> <button value="europe-west6">europe-west6</button> <button value="europe-west8">europe-west8</button> <button value="europe-west9">europe-west9</button> <button value="me-central1">me-central1</button> <button value="me-central2">me-central2</button> <button value="me-west1">me-west1</button> <button value="northamerica-northeast1">northamerica-northeast1</button> <button value="northamerica-northeast2">northamerica-northeast2</button> <button value="northamerica-south1">northamerica-south1</button> <button value="southamerica-east1">southamerica-east1</button> <button value="southamerica-west1">southamerica-west1</button> <button value="us-central1">us-central1</button> <button value="us-east1">us-east1</button> <button value="us-east4">us-east4</button> <button value="us-east5">us-east5</button> <button value="us-south1">us-south1</button> <button value="us-west1">us-west1</button> <button value="us-west2">us-west2</button> <button value="us-west3">us-west3</button> <button value="us-west4">us-west4</button> <button value="eu">eu</button> <button value="us">us</button>   
`GET https://firestore.googleapis.com/v1beta1/{parent=projects/*/databases/*/documents/*/**}/{collectionId}`

<br />

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `parent` | `string` Required. The parent resource name. In the format: `projects/{projectId}/databases/{databaseId}/documents` or `projects/{projectId}/databases/{databaseId}/documents/{document_path}`. For example: `projects/my-project/databases/my-database/documents` or `projects/my-project/databases/my-database/documents/chatrooms/my-chatroom` |
| `collectionId` | `string` Optional. The collection ID, relative to `parent`, to list. For example: `chatrooms` or `messages`. This is optional, and when not provided, Firestore will list documents from all collections under the provided `parent`. |

### Query parameters

| Parameters ||
|---|---|
| `pageSize` | `integer` Optional. The maximum number of documents to return in a single response. Firestore may return fewer than this value. |
| `pageToken` | `string` Optional. A page token, received from a previous `documents.list` response. Provide this to retrieve the subsequent page. When paginating, all other parameters (with the exception of `pageSize`) must match the values set in the request that generated the page token. |
| `orderBy` | `string` Optional. The optional ordering of the documents to return. For example: `priority desc, __name__ desc`. This mirrors the `https://firebase.google.com/docs/firestore/reference/rest/v1beta1/StructuredQuery#FIELDS.order_by` used in Firestore queries but in a string representation. When absent, documents are ordered based on `__name__ ASC`. |
| `mask` | ``object (`https://firebase.google.com/docs/firestore/reference/rest/v1beta1/DocumentMask`)`` Optional. The fields to return. If not set, returns all fields. If a document has a field that is not present in this mask, that field will not be returned in the response. |
| `showMissing` | `boolean` If the list should show missing documents. A document is missing if it does not exist, but there are sub-documents nested underneath it. When true, such missing documents will be returned with a key but will not have fields, `https://firebase.google.com/docs/firestore/reference/rest/v1beta1/projects.databases.documents#Document.FIELDS.create_time`, or `https://firebase.google.com/docs/firestore/reference/rest/v1beta1/projects.databases.documents#Document.FIELDS.update_time` set. Requests with `showMissing` may not specify `where` or `orderBy`. |
| Union parameter `consistency_selector`. The consistency mode for this transaction. If not set, defaults to strong consistency. `consistency_selector` can be only one of the following: ||
| `transaction` | `string (https://developers.google.com/discovery/v1/type-format format)` Perform the read as part of an already active transaction. A base64-encoded string. |
| `readTime` | ``string (`https://protobuf.dev/reference/protobuf/google.protobuf#timestamp` format)`` Perform the read at the provided time. This must be a microsecond precision timestamp within the past one hour, or if Point-in-Time Recovery is enabled, can additionally be a whole minute timestamp within the past 7 days. Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. |

### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `https://firebase.google.com/docs/firestore/reference/rest/v1beta1/ListDocumentsResponse`.

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/datastore`
- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).