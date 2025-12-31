# Source: https://firebase.google.com/docs/reference/app-distribution/rest/v1/upload.v1.projects.apps.releases/upload.md.txt

# Method: upload.v1.projects.apps.releases.upload

- [HTTP request](https://firebase.google.com/docs/reference/app-distribution/rest/v1/upload.v1.projects.apps.releases/upload#body.HTTP_TEMPLATE)
- [Path parameters](https://firebase.google.com/docs/reference/app-distribution/rest/v1/upload.v1.projects.apps.releases/upload#body.PATH_PARAMETERS)
- [Request body](https://firebase.google.com/docs/reference/app-distribution/rest/v1/upload.v1.projects.apps.releases/upload#body.request_body)
- [Response body](https://firebase.google.com/docs/reference/app-distribution/rest/v1/upload.v1.projects.apps.releases/upload#body.response_body)
- [Authorization scopes](https://firebase.google.com/docs/reference/app-distribution/rest/v1/upload.v1.projects.apps.releases/upload#body.aspect)

Uploads a binary. Uploading a binary can result in a new release being created, an update to an existing release, or a no-op if a release with the same binary already exists.

### HTTP request

`POST https://firebaseappdistribution.googleapis.com/upload/v1/{app=projects/*/apps/*}/releases:upload`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.
The following HTTP headers are required:

- `X-Goog-Upload-Protocol`: `raw`
- `X-Goog-Upload-File-Name`: <var translate="no">FILENAME</var>  
  Where <var translate="no">FILENAME</var> is the name of the binary file being uploaded. Example: "**release.apk**".

<br />

### Path parameters

|                                                                                                                                                     Parameters                                                                                                                                                     ||
|-------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `app` | `string` The name of the app resource. Format: `projects/{projectNumber}/apps/{appId}` Authorization requires the following [IAM](https://firebase.google.com/docs/projects/iam/overview/) permission on the Firebase project that owns the specified resource `app`: - `firebaseappdistro.releases.update` |

### Request body

The request body contains the raw binary.

### Response body

If successful, the response body contains an instance of [Operation](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases.operations#Operation).

### Authorization scopes

Requires the following OAuth scope:

- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).