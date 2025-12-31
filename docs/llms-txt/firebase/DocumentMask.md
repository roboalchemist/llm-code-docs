# Source: https://firebase.google.com/docs/firestore/reference/rest/v1beta1/DocumentMask.md.txt

# Source: https://firebase.google.com/docs/firestore/reference/rest/v1/DocumentMask.md.txt

# DocumentMask

A set of field paths on a document. Used to restrict a get or update operation on a document to a subset of its fields. This is different from standard field masks, as this is always scoped to a [Document](https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.documents#Document), and takes in account the dynamic nature of [Value](https://firebase.google.com/docs/firestore/reference/rest/Shared.Types/ArrayValue#Value).

|         JSON representation          |
|--------------------------------------|
| ``` { "fieldPaths": [ string ] } ``` |

|                                                                                                                  Fields                                                                                                                  ||
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `fieldPaths[]` | `string` The list of field paths in the mask. See [Document.fields](https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.documents#Document.FIELDS.fields) for a field path syntax reference. |