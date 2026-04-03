# Source: https://firebase.google.com/docs/firestore/reference/rest/v1beta1/projects.databases.documents/batchWrite.md.txt

# Source: https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.documents/batchWrite.md.txt

# Method: projects.databases.documents.batchWrite

Applies a batch of write operations.

The documents.batchWrite method does not apply the write operations atomically and can apply them out of order. Method does not allow more than one write per document. Each write succeeds or fails independently. See the [BatchWriteResponse](https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.documents/batchWrite#body.BatchWriteResponse) for the success status of each write.

If you require an atomically applied set of writes, use [documents.commit](https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.documents/commit#google.firestore.v1.Firestore.Commit) instead.

### HTTP request

`POST https://firestore.googleapis.com/v1/{database=projects/*/databases/*}/documents:batchWrite`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

|                                                   Parameters                                                    ||
|------------|-----------------------------------------------------------------------------------------------------|
| `database` | `string` Required. The database name. In the format: `projects/{projectId}/databases/{databaseId}`. |

### Request body

The request body contains data with the following structure:

|                                                             JSON representation                                                              |
|----------------------------------------------------------------------------------------------------------------------------------------------|
| ``` { "writes": [ { object (https://firebase.google.com/docs/firestore/reference/rest/v1/Write) } ], "labels": { string: string, ... } } ``` |

|                                                                                                                                                      Fields                                                                                                                                                      ||
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `writes[]` | `object (`[Write](https://firebase.google.com/docs/firestore/reference/rest/v1/Write)`)` The writes to apply. Method does not apply writes atomically and does not guarantee ordering. Each write succeeds or fails independently. You cannot write to the same document more than once per request. |
| `labels`   | `map (key: string, value: string)` Labels associated with this batch write. An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.                                                                                                     |

### Response body

The response from [Firestore.BatchWrite](https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.documents/batchWrite#google.firestore.v1.Firestore.BatchWrite).

If successful, the response body contains data with the following structure:

|                                                                                                            JSON representation                                                                                                            |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ``` { "writeResults": [ { object (https://firebase.google.com/docs/firestore/reference/rest/v1/WriteResult) } ], "status": [ { object (https://firebase.google.com/docs/firestore/reference/rest/Shared.Types/Operation#Status) } ] } ``` |

|                                                                                                                  Fields                                                                                                                  ||
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `writeResults[]` | `object (`[WriteResult](https://firebase.google.com/docs/firestore/reference/rest/v1/WriteResult)`)` The result of applying the writes. This i-th write result corresponds to the i-th write in the request.           |
| `status[]`       | `object (`[Status](https://firebase.google.com/docs/firestore/reference/rest/Shared.Types/Operation#Status)`)` The status of applying the writes. This i-th write status corresponds to the i-th write in the request. |

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/datastore`
- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).