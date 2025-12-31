# Source: https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.versions/populateFiles.md.txt

# Method: sites.versions.populateFiles

Adds content files to the specified version.

Each file must be under 2 GB.

### HTTP request

`POST https://firebasehosting.googleapis.com/v1beta1/{parent=sites/*/versions/*}:populateFiles`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

|                                                                                Parameters                                                                                ||
|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `parent` | `string` Required. The version to which to add files, in the format: `sites/`<var translate="no">SITE_ID</var>`/versions/`<var translate="no">VERSION_ID</var> |

### Request body

The request body contains data with the following structure:

|             JSON representation              |
|----------------------------------------------|
| ``` { "files": { string: string, ... } } ``` |

|                                                                                                                                                                                                               Fields                                                                                                                                                                                                                ||
|---------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `files` | `map (key: string, value: string)` A set of file paths to the hashes corresponding to assets that should be added to the version. A file path to an empty hash will remove the path from the version. Calculate a hash by Gzipping the file then taking the SHA256 hash of the newly compressed file. An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`. |

### Response body

If successful, the response body contains data with the following structure:

|                         JSON representation                         |
|---------------------------------------------------------------------|
| ``` { "uploadRequiredHashes": [ string ], "uploadUrl": string } ``` |

|                                                                                                                                                                                              Fields                                                                                                                                                                                              ||
|--------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `uploadRequiredHashes[]` | `string` The content hashes of the specified files that need to be uploaded to the specified URL.                                                                                                                                                                                                                                                                      |
| `uploadUrl`              | `string` The URL to which the files should be uploaded, in the format: `"https://upload-firebasehosting.googleapis.com/upload/sites/`<var translate="no">SITE_ID</var>`/versions/`<var translate="no">VERSION_ID</var>`/files"` Perform a multipart `POST` of the Gzipped file contents to the URL using a forward slash and the hash of the file appended to the end. |

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/firebase.hosting`
- `
  https://www.googleapis.com/auth/firebase`
- `
  https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).