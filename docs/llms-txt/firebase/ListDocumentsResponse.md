# Source: https://firebase.google.com/docs/firestore/reference/rest/v1beta1/ListDocumentsResponse.md.txt

# Source: https://firebase.google.com/docs/firestore/reference/rest/v1/ListDocumentsResponse.md.txt

# ListDocumentsResponse

The response for [Firestore.ListDocuments](https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.documents/list#google.firestore.v1.Firestore.ListDocuments).

|                                                                          JSON representation                                                                          |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ``` { "documents": [ { object (https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.documents#Document) } ], "nextPageToken": string } ``` |

|                                                                              Fields                                                                               ||
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| `documents[]`   | `object (`[Document](https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.documents#Document)`)` The Documents found. |
| `nextPageToken` | `string` A token to retrieve the next page of documents. If this field is omitted, there are no subsequent pages.                                |