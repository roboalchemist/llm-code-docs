# Source: https://firebase.google.com/docs/firestore/reference/rest/v1beta1/projects.databases.documents/commit.md.txt

# Source: https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.documents/commit.md.txt

# Method: projects.databases.documents.commit

Commits a transaction, while optionally updating documents.

### HTTP request

`POST https://firestore.googleapis.com/v1/{database=projects/*/databases/*}/documents:commit`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

|                                                   Parameters                                                    ||
|------------|-----------------------------------------------------------------------------------------------------|
| `database` | `string` Required. The database name. In the format: `projects/{projectId}/databases/{databaseId}`. |

### Request body

The request body contains data with the following structure:

|                                                       JSON representation                                                        |
|----------------------------------------------------------------------------------------------------------------------------------|
| ``` { "writes": [ { object (https://firebase.google.com/docs/firestore/reference/rest/v1/Write) } ], "transaction": string } ``` |

|                                                                                           Fields                                                                                            ||
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `writes[]`    | `object (`[Write](https://firebase.google.com/docs/firestore/reference/rest/v1/Write)`)` The writes to apply. Always executed atomically and in order.                       |
| `transaction` | `string (`[bytes](https://developers.google.com/discovery/v1/type-format)` format)` If set, applies all writes in this transaction, and commits it. A base64-encoded string. |

### Response body

The response for [Firestore.Commit](https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.documents/commit#google.firestore.v1.Firestore.Commit).

If successful, the response body contains data with the following structure:

|                                                             JSON representation                                                             |
|---------------------------------------------------------------------------------------------------------------------------------------------|
| ``` { "writeResults": [ { object (https://firebase.google.com/docs/firestore/reference/rest/v1/WriteResult) } ], "commitTime": string } ``` |

|                                                                                                                                                                                                                                                         Fields                                                                                                                                                                                                                                                         ||
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `writeResults[]` | `object (`[WriteResult](https://firebase.google.com/docs/firestore/reference/rest/v1/WriteResult)`)` The result of applying the writes. This i-th write result corresponds to the i-th write in the request.                                                                                                                                                                                                                                                                                         |
| `commitTime`     | `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time at which the commit occurred. Any read with an equal or greater `readTime` is guaranteed to see the effects of the commit. Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. |

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/datastore`
- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).