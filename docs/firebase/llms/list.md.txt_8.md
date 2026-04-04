# Source: https://firebase.google.com/docs/firestore/reference/rest/v1/projects.locations/list.md.txt

Lists information about the supported locations for this service. This method can be called in two ways:

- **List all public locations:** Use the path `GET /v1/locations`.
- **List project-visible locations:** Use the path `GET /v1/projects/{projectId}/locations`. This may include public locations as well as private or other locations specifically visible to the project.

### HTTP request

Choose a location:
<button value="global" default="">global</button> <button value="africa-south1">africa-south1</button> <button value="asia-east1">asia-east1</button> <button value="asia-east2">asia-east2</button> <button value="asia-northeast1">asia-northeast1</button> <button value="asia-northeast2">asia-northeast2</button> <button value="asia-northeast3">asia-northeast3</button> <button value="asia-south1">asia-south1</button> <button value="asia-south2">asia-south2</button> <button value="asia-southeast1">asia-southeast1</button> <button value="asia-southeast2">asia-southeast2</button> <button value="asia-southeast3">asia-southeast3</button> <button value="australia-southeast1">australia-southeast1</button> <button value="australia-southeast2">australia-southeast2</button> <button value="europe-central2">europe-central2</button> <button value="europe-north1">europe-north1</button> <button value="europe-north2">europe-north2</button> <button value="europe-southwest1">europe-southwest1</button> <button value="europe-west1">europe-west1</button> <button value="europe-west10">europe-west10</button> <button value="europe-west12">europe-west12</button> <button value="europe-west15">europe-west15</button> <button value="europe-west2">europe-west2</button> <button value="europe-west3">europe-west3</button> <button value="europe-west4">europe-west4</button> <button value="europe-west6">europe-west6</button> <button value="europe-west8">europe-west8</button> <button value="europe-west9">europe-west9</button> <button value="me-central1">me-central1</button> <button value="me-central2">me-central2</button> <button value="me-west1">me-west1</button> <button value="northamerica-northeast1">northamerica-northeast1</button> <button value="northamerica-northeast2">northamerica-northeast2</button> <button value="northamerica-south1">northamerica-south1</button> <button value="southamerica-east1">southamerica-east1</button> <button value="southamerica-west1">southamerica-west1</button> <button value="us-central1">us-central1</button> <button value="us-east1">us-east1</button> <button value="us-east4">us-east4</button> <button value="us-east5">us-east5</button> <button value="us-south1">us-south1</button> <button value="us-west1">us-west1</button> <button value="us-west2">us-west2</button> <button value="us-west3">us-west3</button> <button value="us-west4">us-west4</button> <button value="eu">eu</button> <button value="us">us</button>   
`GET https://firestore.googleapis.com/v1/{name=projects/*}/locations`

<br />

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `name` | `string` The resource that owns the locations collection, if applicable. |

### Query parameters

| Parameters ||
|---|---|
| `filter` | `string` A filter to narrow down results to a preferred subset. The filtering language accepts strings like `"displayName=tokyo"`, and is documented in more detail in [AIP-160](https://google.aip.dev/160). |
| `pageSize` | `integer` The maximum number of results to return. If not set, the service selects a default. |
| `pageToken` | `string` A page token received from the `nextPageToken` field in the response. Send that page token to receive the subsequent page. |
| `extraLocationTypes[]` | `string` Optional. Do not use this field. It is unsupported and is ignored unless explicitly documented otherwise. This is primarily for internal usage. |

### Request body

The request body must be empty.

### Response body

The response message for `https://firebase.google.com/docs/firestore/reference/rest/v1/projects.locations/list#google.cloud.location.Locations.ListLocations`.

If successful, the response body contains data with the following structure:

| JSON representation |
|---|
| ``` { "locations": [ { object (`https://firebase.google.com/docs/firestore/reference/rest/v1/projects.locations#Location`) } ], "nextPageToken": string } ``` |

| Fields ||
|---|---|
| `locations[]` | ``object (`https://firebase.google.com/docs/firestore/reference/rest/v1/projects.locations#Location`)`` A list of locations that matches the specified filter in the request. |
| `nextPageToken` | `string` The standard List next-page token. |

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/datastore`
- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).