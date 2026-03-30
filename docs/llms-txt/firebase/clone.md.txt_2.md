# Source: https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.versions/clone.md.txt

# Method: sites.versions.clone

Creates a new version on the specified target site using the content of the specified version.

### HTTP request

`POST https://firebasehosting.googleapis.com/v1beta1/{parent=sites/*}/versions:clone`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `parent` | `string` Required. The target site for the cloned version, in the format: `sites/SITE_ID` |

### Request body

The request body contains data with the following structure:

| JSON representation |
|---|
| ``` { "sourceVersion": string, "finalize": boolean, // Union field `filter` can be only one of the following: "include": { object (`https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.versions/clone#PathFilter`) }, "exclude": { object (`https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.versions/clone#PathFilter`) } // End of list of possible types for union field `filter`. } ``` |

| Fields ||
|---|---|
| `sourceVersion` | `string` Required. The unique identifier for the version to be cloned, in the format: `sites/SITE_ID/versions/VERSION_ID` |
| `finalize` | `boolean` If true, the call to `versions.clone` immediately finalizes the version after cloning is complete. If false, the cloned version will have a status of `CREATED`. Use [`versions.patch`](https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.versions/patch) to set the status of the version to `FINALIZED`. |
| Union field `filter`. `filter` can be only one of the following: ||
| `include` | ``object (`https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.versions/clone#PathFilter`)`` If provided, only paths that match one or more RegEx values in this list will be included in the new version. |
| `exclude` | ``object (`https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.versions/clone#PathFilter`)`` If provided, only paths that do not match any of the RegEx values in this list will be included in the new version. |

### Response body

If successful, the response body contains an instance of `https://firebase.google.com/docs/reference/hosting/rest/v1beta1/projects.operations#Operation`.

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/firebase.hosting`
- `
  https://www.googleapis.com/auth/firebase`
- `
  https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

## PathFilter

A representation of filter path.

| JSON representation |
|---|
| ``` { "regexes": [ string ] } ``` |

| Fields ||
|---|---|
| `regexes[]` | `string` An array of RegEx values by which to filter. |