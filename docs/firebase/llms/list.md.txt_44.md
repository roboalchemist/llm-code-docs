# Source: https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.versions.files/list.md.txt

# Method: sites.versions.files.list

Lists the remaining files to be uploaded for the specified version.

### HTTP request

`GET https://firebasehosting.googleapis.com/v1beta1/{parent=sites/*/versions/*}/files`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `parent` | `string` Required. The version for which to list files, in the format: `sites/SITE_ID/versions/VERSION_ID` |

### Query parameters

| Parameters ||
|---|---|
| `status` | ``enum (`https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.versions.files/list#Status`)`` The type of files that should be listed for the specified version. |
| `pageSize` | `integer` The maximum number of version files to return. The service may return a lower number if fewer version files exist than this maximum number. If unspecified, defaults to 1000. |
| `pageToken` | `string` A token from a previous call to `files.list` that tells the server where to resume listing. |

### Request body

The request body must be empty.

### Response body

If successful, the response body contains data with the following structure:

| JSON representation |
|---|
| ``` { "files": [ { object (`https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.versions.files/list#VersionFile`) } ], "nextPageToken": string } ``` |

| Fields ||
|---|---|
| `files[]` | ``object (`https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.versions.files/list#VersionFile`)`` The list of paths to the hashes of the files in the specified version. |
| `nextPageToken` | `string` The pagination token, if more results exist beyond the ones in this response. Include this token in your next call to `files.list`. Page tokens are short-lived and should not be stored. |

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/firebase.hosting.readonly`
- `
  https://www.googleapis.com/auth/firebase.hosting`
- `
  https://www.googleapis.com/auth/firebase.readonly`
- `
  https://www.googleapis.com/auth/firebase`
- `
  https://www.googleapis.com/auth/cloud-platform.read-only`
- `
  https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

## Status

The current status of the files being added to a version.

| Enums ||
|---|---|
| `STATUS_UNSPECIFIED` | The default status; should not be intentionally used. |
| `EXPECTED` | The file has been included in the version and is expected to be uploaded in the near future. |
| `ACTIVE` | The file has already been uploaded to Firebase Hosting. |

## VersionFile

A static content file that is part of a version.

| JSON representation |
|---|
| ``` { "path": string, "hash": string, "status": enum (`https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.versions.files/list#Status`) } ``` |

| Fields ||
|---|---|
| `path` | `string` The URI at which the file's content should display. |
| `hash` | `string` The SHA256 content hash of the file. |
| `status` | ``enum (`https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.versions.files/list#Status`)`` Output only. The current status of a particular file in the specified version. The value will be either `pending upload` or `uploaded`. |