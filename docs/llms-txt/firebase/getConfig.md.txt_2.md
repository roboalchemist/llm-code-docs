# Source: https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps/getConfig.md.txt

# Method: projects.androidApps.getConfig

Gets the configuration artifact associated with the specified `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps#AndroidApp`.

### HTTP request

`GET https://firebase.googleapis.com/v1beta1/{name=projects/*/androidApps/*/config}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `name` | `string` The resource name of the `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps#AndroidApp` configuration to download, in the format: `projects/PROJECT_IDENTIFIER/androidApps/APP_ID/config` <br /> Since an <var translate="no">APP_ID</var> is a unique identifier, the Unique Resource from Sub-Collection access pattern may be used here, in the format: `projects/-/androidApps/APP_ID` <br /> Refer to the `AndroidApp` [`name`](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps#AndroidApp.FIELDS.name) field for details about <var translate="no">PROJECT_IDENTIFIER</var> and <var translate="no">APP_ID</var> values. |

### Request body

The request body must be empty.

### Response body

Configuration metadata of a single Firebase App for Android.

If successful, the response body contains data with the following structure:

| JSON representation |
|---|
| ``` { "configFilename": string, "configFileContents": string } ``` |

| Fields ||
|---|---|
| `configFilename` | `string` The filename that the configuration artifact for the `AndroidApp` is typically saved as. For example: `google-services.json` |
| `configFileContents` | `string (https://developers.google.com/discovery/v1/type-format format)` The contents of the JSON configuration file. A base64-encoded string. |

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/cloud-platform`
- `
  https://www.googleapis.com/auth/cloud-platform.read-only`
- `
  https://www.googleapis.com/auth/firebase`
- `
  https://www.googleapis.com/auth/firebase.readonly`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).