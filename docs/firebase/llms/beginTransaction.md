# Source: https://firebase.google.com/docs/firestore/reference/rest/v1beta1/projects.databases.documents/beginTransaction.md.txt

# Source: https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.documents/beginTransaction.md.txt

# Method: projects.databases.documents.beginTransaction

Starts a new transaction.

### HTTP request

`POST https://firestore.googleapis.com/v1/{database=projects/*/databases/*}/documents:beginTransaction`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

|                                                   Parameters                                                    ||
|------------|-----------------------------------------------------------------------------------------------------|
| `database` | `string` Required. The database name. In the format: `projects/{projectId}/databases/{databaseId}`. |

### Request body

The request body contains data with the following structure:

|                                                 JSON representation                                                 |
|---------------------------------------------------------------------------------------------------------------------|
| ``` { "options": { object (https://firebase.google.com/docs/firestore/reference/rest/v1/TransactionOptions) } } ``` |

|                                                                                                Fields                                                                                                ||
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `options` | `object (`[TransactionOptions](https://firebase.google.com/docs/firestore/reference/rest/v1/TransactionOptions)`)` The options for the transaction. Defaults to a read-write transaction. |

### Response body

The response for [Firestore.BeginTransaction](https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.documents/beginTransaction#google.firestore.v1.Firestore.BeginTransaction).

If successful, the response body contains data with the following structure:

|        JSON representation        |
|-----------------------------------|
| ``` { "transaction": string } ``` |

|                                                                            Fields                                                                             ||
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| `transaction` | `string (`[bytes](https://developers.google.com/discovery/v1/type-format)` format)` The transaction that was started. A base64-encoded string. |

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/datastore`
- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).