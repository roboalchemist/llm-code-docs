# Source: https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.operations/list.md.txt

Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`.

### HTTP request

Choose a location:
<button value="global" default="">global</button> <button value="africa-south1">africa-south1</button> <button value="asia-east1">asia-east1</button> <button value="asia-east2">asia-east2</button> <button value="asia-northeast1">asia-northeast1</button> <button value="asia-northeast2">asia-northeast2</button> <button value="asia-northeast3">asia-northeast3</button> <button value="asia-south1">asia-south1</button> <button value="asia-south2">asia-south2</button> <button value="asia-southeast1">asia-southeast1</button> <button value="asia-southeast2">asia-southeast2</button> <button value="asia-southeast3">asia-southeast3</button> <button value="australia-southeast1">australia-southeast1</button> <button value="australia-southeast2">australia-southeast2</button> <button value="europe-central2">europe-central2</button> <button value="europe-north1">europe-north1</button> <button value="europe-north2">europe-north2</button> <button value="europe-southwest1">europe-southwest1</button> <button value="europe-west1">europe-west1</button> <button value="europe-west10">europe-west10</button> <button value="europe-west12">europe-west12</button> <button value="europe-west15">europe-west15</button> <button value="europe-west2">europe-west2</button> <button value="europe-west3">europe-west3</button> <button value="europe-west4">europe-west4</button> <button value="europe-west6">europe-west6</button> <button value="europe-west8">europe-west8</button> <button value="europe-west9">europe-west9</button> <button value="me-central1">me-central1</button> <button value="me-central2">me-central2</button> <button value="me-west1">me-west1</button> <button value="northamerica-northeast1">northamerica-northeast1</button> <button value="northamerica-northeast2">northamerica-northeast2</button> <button value="northamerica-south1">northamerica-south1</button> <button value="southamerica-east1">southamerica-east1</button> <button value="southamerica-west1">southamerica-west1</button> <button value="us-central1">us-central1</button> <button value="us-east1">us-east1</button> <button value="us-east4">us-east4</button> <button value="us-east5">us-east5</button> <button value="us-south1">us-south1</button> <button value="us-west1">us-west1</button> <button value="us-west2">us-west2</button> <button value="us-west3">us-west3</button> <button value="us-west4">us-west4</button> <button value="eu">eu</button> <button value="us">us</button>   
`GET https://firestore.googleapis.com/v1/{name=projects/*/databases/*}/operations`

<br />

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `name` | `string` The name of the operation's parent resource. |

### Query parameters

| Parameters ||
|---|---|
| `filter` | `string` The standard list filter. |
| `pageSize` | `integer` The standard list page size. |
| `pageToken` | `string` The standard list page token. |
| `returnPartialSuccess` | `boolean` When set to `true`, operations that are reachable are returned as normal, and those that are unreachable are returned in the `https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.operations/list#body.ListOperationsResponse.FIELDS.unreachable` field. This can only be `true` when reading across collections. For example, when `parent` is set to `"projects/example/locations/-"`. This field is not supported by default and will result in an `UNIMPLEMENTED` error if set unless explicitly documented otherwise in service or product specific documentation. |

### Request body

The request body must be empty.

### Response body

The response message for `https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.operations/list#google.longrunning.Operations.ListOperations`.

If successful, the response body contains data with the following structure:

| JSON representation |
|---|
| ``` { "operations": [ { object (`https://firebase.google.com/docs/firestore/reference/rest/Shared.Types/Operation`) } ], "nextPageToken": string, "unreachable": [ string ] } ``` |

| Fields ||
|---|---|
| `operations[]` | ``object (`https://firebase.google.com/docs/firestore/reference/rest/Shared.Types/Operation`)`` A list of operations that matches the specified filter in the request. |
| `nextPageToken` | `string` The standard List next-page token. |
| `unreachable[]` | `string` Unordered list. Unreachable resources. Populated when the request sets `ListOperationsRequest.return_partial_success` and reads across collections. For example, when attempting to list all resources across all supported locations. |

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/datastore`
- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).