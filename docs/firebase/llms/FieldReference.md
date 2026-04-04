# Source: https://firebase.google.com/docs/firestore/reference/rest/v1beta1/FieldReference.md.txt

# Source: https://firebase.google.com/docs/firestore/reference/rest/v1/FieldReference.md.txt

# FieldReference

A reference to a field in a document, ex: `stats.operations`.

|       JSON representation       |
|---------------------------------|
| ``` { "fieldPath": string } ``` |

|                                                                                                                                                    Fields                                                                                                                                                     ||
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `fieldPath` | `string` A reference to a field in a document. Requires: - MUST be a dot-delimited (`.`) string of segments, where each segment conforms to [document field name](https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.documents#Document.FIELDS.fields) limitations. |