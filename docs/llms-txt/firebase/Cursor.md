# Source: https://firebase.google.com/docs/firestore/reference/rest/v1/Cursor.md.txt

# Source: https://firebase.google.com/docs/firestore/reference/rest/v1beta1/Cursor.md.txt

# Cursor

A position in a query result set.

|                        JSON representation                        |
|-------------------------------------------------------------------|
| ``` { "values": [ { object (`Value`) } ], "before": boolean } ``` |

|                                                                                               Fields                                                                                               ||
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `values[]` | `object (``Value``)` The values that represent a position, in the order they appear in the order by clause of a query. Can contain fewer values than specified in the order by clause. |
| `before`   | `boolean` If the position is just before or just after the given values, relative to the sort order defined by the query.                                                              |