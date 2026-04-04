# Source: https://firebase.google.com/docs/firestore/reference/rest/v1beta2/projects.databases.collectionGroups.fields/patch.md.txt

Updates a field configuration. Currently, field updates apply only to single field index configuration. However, calls to `https://firebase.google.com/docs/firestore/reference/rest/v1beta2/projects.databases.collectionGroups.fields/patch#google.firestore.admin.v1beta2.FirestoreAdmin.UpdateField` should provide a field mask to avoid changing any configuration that the caller isn't aware of. The field mask should be specified as: `{ paths: "indexConfig" }`.

This call returns a `https://firebase.google.com/docs/firestore/reference/rest/Shared.Types/Operation` which may be used to track the status of the field update. The metadata for the operation will be the type `FieldOperationMetadata`.

To configure the default field settings for the database, use the special `Field` with resource name: `projects/{projectId}/databases/{databaseId}/collectionGroups/__default__/fields/*`.

### HTTP request

Choose a location:
<button value="global" default="">global</button> <button value="africa-south1">africa-south1</button> <button value="asia-east1">asia-east1</button> <button value="asia-east2">asia-east2</button> <button value="asia-northeast1">asia-northeast1</button> <button value="asia-northeast2">asia-northeast2</button> <button value="asia-northeast3">asia-northeast3</button> <button value="asia-south1">asia-south1</button> <button value="asia-south2">asia-south2</button> <button value="asia-southeast1">asia-southeast1</button> <button value="asia-southeast2">asia-southeast2</button> <button value="asia-southeast3">asia-southeast3</button> <button value="australia-southeast1">australia-southeast1</button> <button value="australia-southeast2">australia-southeast2</button> <button value="europe-central2">europe-central2</button> <button value="europe-north1">europe-north1</button> <button value="europe-north2">europe-north2</button> <button value="europe-southwest1">europe-southwest1</button> <button value="europe-west1">europe-west1</button> <button value="europe-west10">europe-west10</button> <button value="europe-west12">europe-west12</button> <button value="europe-west15">europe-west15</button> <button value="europe-west2">europe-west2</button> <button value="europe-west3">europe-west3</button> <button value="europe-west4">europe-west4</button> <button value="europe-west6">europe-west6</button> <button value="europe-west8">europe-west8</button> <button value="europe-west9">europe-west9</button> <button value="me-central1">me-central1</button> <button value="me-central2">me-central2</button> <button value="me-west1">me-west1</button> <button value="northamerica-northeast1">northamerica-northeast1</button> <button value="northamerica-northeast2">northamerica-northeast2</button> <button value="northamerica-south1">northamerica-south1</button> <button value="southamerica-east1">southamerica-east1</button> <button value="southamerica-west1">southamerica-west1</button> <button value="us-central1">us-central1</button> <button value="us-east1">us-east1</button> <button value="us-east4">us-east4</button> <button value="us-east5">us-east5</button> <button value="us-south1">us-south1</button> <button value="us-west1">us-west1</button> <button value="us-west2">us-west2</button> <button value="us-west3">us-west3</button> <button value="us-west4">us-west4</button> <button value="eu">eu</button> <button value="us">us</button>   
`PATCH https://firestore.googleapis.com/v1beta2/{field.name=projects/*/databases/*/collectionGroups/*/fields/*}`

<br />

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `field.name` | `string` A field name of the form `projects/{projectId}/databases/{databaseId}/collectionGroups/{collectionId}/fields/{fieldPath}` A field path may be a simple field name, e.g. `address` or a path to fields within mapValue , e.g. `address.city`, or a special field path. The only valid special field is `*`, which represents any field. Field paths may be quoted using `(backtick). The only character that needs to be escaped within a quoted field path is the backtick character itself, escaped using a backslash. Special characters in field paths that must be quoted include:`\*`,`.````, ``` (backtick),````\[`,`\]\`, as well as any ascii symbolic characters. Examples: (Note: Comments here are written in markdown syntax, so there is an additional layer of backticks to represent a code block) `\`address.city\``represents a field named`address.city`, not the map key `city`in the field`address`. `\`\*\``represents a field named`\*\`, not any field. A special `Field` contains the default indexing settings for all fields. This field's resource name is: `projects/{projectId}/databases/{databaseId}/collectionGroups/__default__/fields/*` Indexes defined on this `Field` will be applied to all fields which do not have their own `Field` index configuration. |

### Query parameters

| Parameters ||
|---|---|
| `updateMask` | ``string (`https://protobuf.dev/reference/protobuf/google.protobuf#field-mask` format)`` A mask, relative to the field. If specified, only configuration specified by this field_mask will be updated in the field. This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`. |

### Request body

The request body contains an instance of `https://firebase.google.com/docs/firestore/reference/rest/v1beta2/projects.databases.collectionGroups.fields#Field`.

### Response body

If successful, the response body contains an instance of `https://firebase.google.com/docs/firestore/reference/rest/Shared.Types/Operation`.

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/datastore`
- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).