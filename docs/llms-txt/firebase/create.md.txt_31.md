# Source: https://firebase.google.com/docs/reference/rest/storage/rest/v1alpha/projects.defaultBucket/create.md.txt

# Method: projects.defaultBucket.create

Creates the default Cloud Storage bucket and links it to the specified Firebase project.

If the default bucket already exists, this method will re-link it to the Firebase project.

Starting October 30, 2024, using this method requires that the Firebase project is on the [pay-as-you-go Blaze pricing plan](https://firebase.google.com/pricing), and the resulting default bucket name will be in the format `{PROJECT_ID}.firebasestorage.app`.

### HTTP request

`POST https://firebasestorage.googleapis.com/v1alpha/{parent=projects/*}/defaultBucket`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `parent` | `string` Required. The parent resource where the default bucket will be created, `projects/{project_id_or_number}`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`: - `firebasestorage.defaultBucket.create` |

### Request body

The request body contains an instance of `https://firebase.google.com/docs/reference/rest/storage/rest/v1alpha/projects.defaultBucket#DefaultBucket`.

### Response body

If successful, the response body contains a newly created instance of `https://firebase.google.com/docs/reference/rest/storage/rest/v1alpha/projects.defaultBucket#DefaultBucket`.

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/cloud-platform`
- `https://www.googleapis.com/auth/firebase`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

- `firebasestorage.defaultBucket.create`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).