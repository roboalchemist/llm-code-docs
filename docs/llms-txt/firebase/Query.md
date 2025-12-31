# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Query.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Query.md.txt

# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Query.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query.md.txt

# Query

# Query


```
class Query
```

<br />

Known direct subclasses  
[DatabaseReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference)  

|-----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| [DatabaseReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference) | A Firebase reference represents a particular location in your Database and can be used for reading or writing data to that Database location. |

*** ** * ** ***

The Query class (and its subclass, [DatabaseReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference)) are used for reading data. Listeners are attached, and they will be triggered when the corresponding data changes. Instances of Query are obtained by calling startAt(), endAt(), or limit() on a DatabaseReference.

## Summary

|                                                                                               ### Public functions                                                                                               |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ChildEventListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEventListener)                                                                                          | [addChildEventListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#addChildEventListener(com.google.firebase.database.ChildEventListener))`(listener: `[ChildEventListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEventListener)`)` Add a listener for child events occurring at this location.                                                                                                                                                                                                           |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)                                                                                                                                     | [addListenerForSingleValueEvent](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#addListenerForSingleValueEvent(com.google.firebase.database.ValueEventListener))`(listener: `[ValueEventListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ValueEventListener)`)` Add a listener for a single change in the data at this location.                                                                                                                                                                                    |
| [ValueEventListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ValueEventListener)                                                                                          | [addValueEventListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#addValueEventListener(com.google.firebase.database.ValueEventListener))`(listener: `[ValueEventListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ValueEventListener)`)` Add a listener for changes in the data at this location.                                                                                                                                                                                                              |
| [Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query)                                                                                                                    | [endAt](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#endAt(java.lang.String))`(value: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?)` Creates a query constrained to only return child nodes with a value less than or equal to the given value, using the given `orderBy` directive or priority as default.                                                                                                                                                                                                        |
| [Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query)                                                                                                                    | [endAt](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#endAt(double))`(value: `[Double](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html)`)` Creates a query constrained to only return child nodes with a value less than or equal to the given value, using the given `orderBy` directive or priority as default.                                                                                                                                                                                                                   |
| [Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query)                                                                                                                    | [endAt](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#endAt(boolean))`(value: `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)`)` Creates a query constrained to only return child nodes with a value less than or equal to the given value, using the given `orderBy` directive or priority as default.                                                                                                                                                                                                                |
| [Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query)                                                                                                                    | [endAt](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#endAt(java.lang.String,java.lang.String))`(value: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?, key: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?)` Creates a query constrained to only return child nodes with a value less than or equal to the given value, using the given `orderBy` directive or priority as default, and additionally only child nodes with a key less than or equal to the given key.           |
| [Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query)                                                                                                                    | [endAt](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#endAt(double,java.lang.String))`(value: `[Double](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html)`, key: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?)` Creates a query constrained to only return child nodes with a value less than or equal to the given value, using the given `orderBy` directive or priority as default, and additionally only child nodes with a key less than or equal to the given key.                      |
| [Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query)                                                                                                                    | [endAt](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#endAt(boolean,java.lang.String))`(value: `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)`, key: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?)` Creates a query constrained to only return child nodes with a value less than or equal to the given value, using the given `orderBy` directive or priority as default, and additionally only child nodes with a key less than or equal to the given key.                   |
| [Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query)                                                                                                                    | [endBefore](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#endBefore(java.lang.String))`(value: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?)` Creates a query constrained to only return child nodes with a value less than the given value, using the given `orderBy` directive or priority as default.                                                                                                                                                                                                            |
| [Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query)                                                                                                                    | [endBefore](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#endBefore(double))`(value: `[Double](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html)`)` Creates a query constrained to only return child nodes with a value less than the given value, using the given `orderBy` directive or priority as default.                                                                                                                                                                                                                       |
| [Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query)                                                                                                                    | [endBefore](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#endBefore(boolean))`(value: `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)`)` Creates a query constrained to only return child nodes with a value less than the given value, using the given `orderBy` directive or priority as default.                                                                                                                                                                                                                    |
| [Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query)                                                                                                                    | [endBefore](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#endBefore(java.lang.String,java.lang.String))`(value: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?, key: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?)` Creates a query constrained to only return child nodes with a value less than or equal to the given value, using the given `orderBy` directive or priority as default, and additionally only child nodes with a key less than the given key.               |
| [Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query)                                                                                                                    | [endBefore](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#endBefore(double,java.lang.String))`(value: `[Double](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html)`, key: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?)` Creates a query constrained to only return child nodes with a value less than or equal to the given value, using the given `orderBy` directive or priority as default, and additionally only child nodes with a key less than the given key.                          |
| [Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query)                                                                                                                    | [endBefore](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#endBefore(boolean,java.lang.String))`(value: `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)`, key: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?)` Creates a query constrained to only return child nodes with a value less than or equal to the given value, using the given `orderBy` directive or priority as default, and additionally only child nodes with a key less than the given key.                       |
| [Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query)                                                                                                                    | [equalTo](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#equalTo(java.lang.String))`(value: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?)` Creates a query constrained to only return child nodes with the given value.                                                                                                                                                                                                                                                                                              |
| [Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query)                                                                                                                    | [equalTo](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#equalTo(double))`(value: `[Double](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html)`)` Creates a query constrained to only return child nodes with the given value.                                                                                                                                                                                                                                                                                                         |
| [Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query)                                                                                                                    | [equalTo](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#equalTo(boolean))`(value: `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)`)` Creates a query constrained to only return child nodes with the given value.                                                                                                                                                                                                                                                                                                      |
| [Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query)                                                                                                                    | [equalTo](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#equalTo(java.lang.String,java.lang.String))`(value: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?, key: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?)` Creates a query constrained to only return the child node with the given key and value.                                                                                                                                                                        |
| [Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query)                                                                                                                    | [equalTo](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#equalTo(double,java.lang.String))`(value: `[Double](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html)`, key: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?)` Creates a query constrained to only return the child node with the given key and value.                                                                                                                                                                                   |
| [Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query)                                                                                                                    | [equalTo](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#equalTo(boolean,java.lang.String))`(value: `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)`, key: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?)` Creates a query constrained to only return the child node with the given key and value.                                                                                                                                                                                |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[DataSnapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DataSnapshot)`!>` | [get](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#get())`()` Gets the server values for this query.                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [DatabaseReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference)                                                                                            | [getRef](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#getRef())`()`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)                                                                                                                                     | [keepSynced](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#keepSynced(boolean))`(keepSynced: `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)`)` By calling \`keepSynced(true)\` on a location, the data for that location will automatically be downloaded and kept in sync, even when no listeners are attached for that location.                                                                                                                                                                                    |
| [Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query)                                                                                                                    | [limitToFirst](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#limitToFirst(int))`(limit: `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)`)` Creates a query with limit and anchor it to the start of the window.                                                                                                                                                                                                                                                                                                                |
| [Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query)                                                                                                                    | [limitToLast](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#limitToLast(int))`(limit: `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)`)` Creates a query with limit and anchor it to the end of the window.                                                                                                                                                                                                                                                                                                                    |
| [Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query)                                                                                                                    | [orderByChild](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#orderByChild(java.lang.String))`(path: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`)` Creates a query in which child nodes are ordered by the values of the specified path.                                                                                                                                                                                                                                                                             |
| [Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query)                                                                                                                    | [orderByKey](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#orderByKey())`()` Creates a query in which child nodes are ordered by their keys.                                                                                                                                                                                                                                                                                                                                                                                                               |
| [Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query)                                                                                                                    | [orderByPriority](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#orderByPriority())`()` Creates a query in which child nodes are ordered by their priorities.                                                                                                                                                                                                                                                                                                                                                                                               |
| [Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query)                                                                                                                    | [orderByValue](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#orderByValue())`()` Creates a query in which nodes are ordered by their value                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)                                                                                                                                     | [removeEventListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#removeEventListener(com.google.firebase.database.ChildEventListener))`(listener: `[ChildEventListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEventListener)`)` Remove the specified listener from this location.                                                                                                                                                                                                                         |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)                                                                                                                                     | [removeEventListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#removeEventListener(com.google.firebase.database.ValueEventListener))`(listener: `[ValueEventListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ValueEventListener)`)` Remove the specified listener from this location.                                                                                                                                                                                                                         |
| [Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query)                                                                                                                    | [startAfter](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#startAfter(java.lang.String))`(value: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?)` Creates a query constrained to only return child nodes with a value greater than the given value, using the given `orderBy` directive or priority as default.                                                                                                                                                                                                       |
| [Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query)                                                                                                                    | [startAfter](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#startAfter(double))`(value: `[Double](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html)`)` Creates a query constrained to only return child nodes with a value greater than the given value, using the given `orderBy` directive or priority as default.                                                                                                                                                                                                                  |
| [Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query)                                                                                                                    | [startAfter](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#startAfter(boolean))`(value: `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)`)` Creates a query constrained to only return child nodes with a value greater than the given value, using the given `orderBy` directive or priority as default.                                                                                                                                                                                                               |
| [Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query)                                                                                                                    | [startAfter](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#startAfter(java.lang.String,java.lang.String))`(value: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?, key: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?)` Creates a query constrained to only return child nodes with a value greater or equal to the given value, using the given `orderBy` directive or priority as default, and additionally only child nodes with a key greater than the given key.            |
| [Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query)                                                                                                                    | [startAfter](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#startAfter(double,java.lang.String))`(value: `[Double](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html)`, key: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?)` Creates a query constrained to only return child nodes with a value greater than or equal to the given value, using the given `orderBy` directive or priority as default, and additionally only child nodes with a key greater than the given key.                  |
| [Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query)                                                                                                                    | [startAfter](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#startAfter(boolean,java.lang.String))`(value: `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)`, key: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?)` Creates a query constrained to only return child nodes with a value greater than or equal to the given value, using the given `orderBy` directive or priority as default, and additionally only child nodes with a key greater than the given key.               |
| [Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query)                                                                                                                    | [startAt](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#startAt(java.lang.String))`(value: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?)` Creates a query constrained to only return child nodes with a value greater than or equal to the given value, using the given `orderBy` directive or priority as default.                                                                                                                                                                                                 |
| [Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query)                                                                                                                    | [startAt](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#startAt(double))`(value: `[Double](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html)`)` Creates a query constrained to only return child nodes with a value greater than or equal to the given value, using the given `orderBy` directive or priority as default.                                                                                                                                                                                                            |
| [Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query)                                                                                                                    | [startAt](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#startAt(boolean))`(value: `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)`)` Creates a query constrained to only return child nodes with a value greater than or equal to the given value, using the given `orderBy` directive or priority as default.                                                                                                                                                                                                         |
| [Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query)                                                                                                                    | [startAt](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#startAt(java.lang.String,java.lang.String))`(value: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?, key: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?)` Creates a query constrained to only return child nodes with a value greater than or equal to the given value, using the given `orderBy` directive or priority as default, and additionally only child nodes with a key greater than or equal to the given key. |
| [Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query)                                                                                                                    | [startAt](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#startAt(double,java.lang.String))`(value: `[Double](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html)`, key: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?)` Creates a query constrained to only return child nodes with a value greater than or equal to the given value, using the given `orderBy` directive or priority as default, and additionally only child nodes with a key greater than or equal to the given key.            |
| [Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query)                                                                                                                    | [startAt](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#startAt(boolean,java.lang.String))`(value: `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)`, key: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?)` Creates a query constrained to only return child nodes with a value greater than or equal to the given value, using the given `orderBy` directive or priority as default, and additionally only child nodes with a key greater than or equal to the given key.         |

|                                                        ### Extension functions                                                        |
|---------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `inline `[Flow](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html)`<T?>` | `<T : `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`> `[Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query)`.`[values](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#(com.google.firebase.database.Query).values())`()` Starts listening to this query and emits its values converted to a POJO via a [Flow](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html). |

|                                                                                                        ### Extension properties                                                                                                         |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Flow](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html)`<`[ChildEvent](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent)`>`     | [Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query)`.`[childEvents](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#(com.google.firebase.database.Query).childEvents()) Starts listening to this query's child events and emits its values via a [Flow](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html). |
| [Flow](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html)`<`[DataSnapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DataSnapshot)`>` | [Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query)`.`[snapshots](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#(com.google.firebase.database.Query).snapshots()) Starts listening to this query and emits its values via a [Flow](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html).                    |

## Public functions

### addChildEventListener

```
funÂ addChildEventListener(listener:Â ChildEventListener):Â ChildEventListener
```

Add a listener for child events occurring at this location. When child locations are added, removed, changed, or moved, the listener will be triggered for the appropriate event  

|                                                             Parameters                                                              |
|-------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|
| `listener: `[ChildEventListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEventListener) | The listener to be called with changes |

|                                                         Returns                                                         |
|-------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| [ChildEventListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEventListener) | A reference to the listener provided. Save this to remove the listener later. |

### addListenerForSingleValueEvent

```
funÂ addListenerForSingleValueEvent(listener:Â ValueEventListener):Â Unit
```

Add a listener for a single change in the data at this location. This listener will be triggered once with the value of the data at the location.  

|                                                             Parameters                                                              |
|-------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------|
| `listener: `[ValueEventListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ValueEventListener) | The listener to be called with the data |

### addValueEventListener

```
funÂ addValueEventListener(listener:Â ValueEventListener):Â ValueEventListener
```

Add a listener for changes in the data at this location. Each time the data changes, your listener will be called with an immutable snapshot of the data.  

|                                                             Parameters                                                              |
|-------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|
| `listener: `[ValueEventListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ValueEventListener) | The listener to be called with changes |

|                                                         Returns                                                         |
|-------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| [ValueEventListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ValueEventListener) | A reference to the listener provided. Save this to remove the listener later. |

### endAt

```
funÂ endAt(value:Â String?):Â Query
```

Creates a query constrained to only return child nodes with a value less than or equal to the given value, using the given `orderBy` directive or priority as default.  

|                                          Parameters                                          |
|----------------------------------------------------------------------------------------------|--------------------------------|
| `value: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?` | The value to end at, inclusive |

|                                            Returns                                            |
|-----------------------------------------------------------------------------------------------|---------------------------------|
| [Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query) | A query with the new constraint |

### endAt

```
funÂ endAt(value:Â Double):Â Query
```

Creates a query constrained to only return child nodes with a value less than or equal to the given value, using the given `orderBy` directive or priority as default.  

|                                        Parameters                                         |
|-------------------------------------------------------------------------------------------|--------------------------------|
| `value: `[Double](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html) | The value to end at, inclusive |

|                                            Returns                                            |
|-----------------------------------------------------------------------------------------------|---------------------------------|
| [Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query) | A query with the new constraint |

### endAt

```
funÂ endAt(value:Â Boolean):Â Query
```

Creates a query constrained to only return child nodes with a value less than or equal to the given value, using the given `orderBy` directive or priority as default.

2.0  

|                                         Parameters                                          |
|---------------------------------------------------------------------------------------------|--------------------------------|
| `value: `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | The value to end at, inclusive |

|                                            Returns                                            |
|-----------------------------------------------------------------------------------------------|---------------------------------|
| [Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query) | A query with the new constraint |

### endAt

```
funÂ endAt(value:Â String?,Â key:Â String?):Â Query
```

Creates a query constrained to only return child nodes with a value less than or equal to the given value, using the given `orderBy` directive or priority as default, and additionally only child nodes with a key less than or equal to the given key.  

|                                          Parameters                                          |
|----------------------------------------------------------------------------------------------|--------------------------------|
| `value: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?` | The value to end at, inclusive |
| `key: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?`   | The key to end at, inclusive   |

|                                            Returns                                            |
|-----------------------------------------------------------------------------------------------|---------------------------------|
| [Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query) | A query with the new constraint |

### endAt

```
funÂ endAt(value:Â Double,Â key:Â String?):Â Query
```

Creates a query constrained to only return child nodes with a value less than or equal to the given value, using the given `orderBy` directive or priority as default, and additionally only child nodes with a key less than or equal to the given key.  

|                                         Parameters                                         |
|--------------------------------------------------------------------------------------------|--------------------------------|
| `value: `[Double](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html)  | The value to end at, inclusive |
| `key: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?` | The key to end at, inclusive   |

|                                            Returns                                            |
|-----------------------------------------------------------------------------------------------|---------------------------------|
| [Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query) | A query with the new constraint |

### endAt

```
funÂ endAt(value:Â Boolean,Â key:Â String?):Â Query
```

Creates a query constrained to only return child nodes with a value less than or equal to the given value, using the given `orderBy` directive or priority as default, and additionally only child nodes with a key less than or equal to the given key.

2.0  

|                                         Parameters                                          |
|---------------------------------------------------------------------------------------------|--------------------------------|
| `value: `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | The value to end at, inclusive |
| `key: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?`  | The key to end at, inclusive   |

|                                            Returns                                            |
|-----------------------------------------------------------------------------------------------|---------------------------------|
| [Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query) | A query with the new constraint |

### endBefore

```
funÂ endBefore(value:Â String?):Â Query
```

Creates a query constrained to only return child nodes with a value less than the given value, using the given `orderBy` directive or priority as default.

19.6  

|                                          Parameters                                          |
|----------------------------------------------------------------------------------------------|--------------------------------|
| `value: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?` | The value to end at, exclusive |

|                                            Returns                                            |
|-----------------------------------------------------------------------------------------------|---------------------------------|
| [Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query) | A query with the new constraint |

### endBefore

```
funÂ endBefore(value:Â Double):Â Query
```

Creates a query constrained to only return child nodes with a value less than the given value, using the given `orderBy` directive or priority as default.

19.6  

|                                        Parameters                                         |
|-------------------------------------------------------------------------------------------|--------------------------------|
| `value: `[Double](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html) | The value to end at, exclusive |

|                                            Returns                                            |
|-----------------------------------------------------------------------------------------------|---------------------------------|
| [Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query) | A query with the new constraint |

### endBefore

```
funÂ endBefore(value:Â Boolean):Â Query
```

Creates a query constrained to only return child nodes with a value less than the given value, using the given `orderBy` directive or priority as default.

19.6  

|                                         Parameters                                          |
|---------------------------------------------------------------------------------------------|--------------------------------|
| `value: `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | The value to end at, exclusive |

|                                            Returns                                            |
|-----------------------------------------------------------------------------------------------|---------------------------------|
| [Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query) | A query with the new constraint |

### endBefore

```
funÂ endBefore(value:Â String?,Â key:Â String?):Â Query
```

Creates a query constrained to only return child nodes with a value less than or equal to the given value, using the given `orderBy` directive or priority as default, and additionally only child nodes with a key less than the given key.

19.6  

|                                          Parameters                                          |
|----------------------------------------------------------------------------------------------|------------------------------|
| `value: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?` | The value to end at          |
| `key: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?`   | The key to end at, exclusive |

|                                            Returns                                            |
|-----------------------------------------------------------------------------------------------|---------------------------------|
| [Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query) | A query with the new constraint |

### endBefore

```
funÂ endBefore(value:Â Double,Â key:Â String?):Â Query
```

Creates a query constrained to only return child nodes with a value less than or equal to the given value, using the given `orderBy` directive or priority as default, and additionally only child nodes with a key less than the given key.

19.6  

|                                         Parameters                                         |
|--------------------------------------------------------------------------------------------|------------------------------|
| `value: `[Double](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html)  | The value to end at          |
| `key: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?` | The key to end at, exclusive |

|                                            Returns                                            |
|-----------------------------------------------------------------------------------------------|---------------------------------|
| [Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query) | A query with the new constraint |

### endBefore

```
funÂ endBefore(value:Â Boolean,Â key:Â String?):Â Query
```

Creates a query constrained to only return child nodes with a value less than or equal to the given value, using the given `orderBy` directive or priority as default, and additionally only child nodes with a key less than the given key.

19.6  

|                                         Parameters                                          |
|---------------------------------------------------------------------------------------------|------------------------------|
| `value: `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | The value to end at          |
| `key: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?`  | The key to end at, exclusive |

|                                            Returns                                            |
|-----------------------------------------------------------------------------------------------|---------------------------------|
| [Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query) | A query with the new constraint |

### equalTo

```
funÂ equalTo(value:Â String?):Â Query
```

Creates a query constrained to only return child nodes with the given value.  

|                                          Parameters                                          |
|----------------------------------------------------------------------------------------------|------------------------|
| `value: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?` | The value to query for |

|                                            Returns                                            |
|-----------------------------------------------------------------------------------------------|---------------------------------|
| [Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query) | A query with the new constraint |

### equalTo

```
funÂ equalTo(value:Â Double):Â Query
```

Creates a query constrained to only return child nodes with the given value.  

|                                        Parameters                                         |
|-------------------------------------------------------------------------------------------|------------------------|
| `value: `[Double](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html) | The value to query for |

|                                            Returns                                            |
|-----------------------------------------------------------------------------------------------|---------------------------------|
| [Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query) | A query with the new constraint |

### equalTo

```
funÂ equalTo(value:Â Boolean):Â Query
```

Creates a query constrained to only return child nodes with the given value.

2.0  

|                                         Parameters                                          |
|---------------------------------------------------------------------------------------------|------------------------|
| `value: `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | The value to query for |

|                                            Returns                                            |
|-----------------------------------------------------------------------------------------------|---------------------------------|
| [Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query) | A query with the new constraint |

### equalTo

```
funÂ equalTo(value:Â String?,Â key:Â String?):Â Query
```

Creates a query constrained to only return the child node with the given key and value. Note that there is at most one such child as names are unique.  

|                                          Parameters                                          |
|----------------------------------------------------------------------------------------------|------------------------|
| `value: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?` | The value to query for |
| `key: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?`   | The key of the child   |

|                                            Returns                                            |
|-----------------------------------------------------------------------------------------------|---------------------------------|
| [Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query) | A query with the new constraint |

### equalTo

```
funÂ equalTo(value:Â Double,Â key:Â String?):Â Query
```

Creates a query constrained to only return the child node with the given key and value. Note that there is at most one such child as keys are unique.  

|                                         Parameters                                         |
|--------------------------------------------------------------------------------------------|------------------------|
| `value: `[Double](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html)  | The value to query for |
| `key: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?` | The key of the child   |

|                                            Returns                                            |
|-----------------------------------------------------------------------------------------------|---------------------------------|
| [Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query) | A query with the new constraint |

### equalTo

```
funÂ equalTo(value:Â Boolean,Â key:Â String?):Â Query
```

Creates a query constrained to only return the child node with the given key and value. Note that there is at most one such child as keys are unique.  

|                                         Parameters                                          |
|---------------------------------------------------------------------------------------------|------------------------|
| `value: `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | The value to query for |
| `key: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?`  | The name of the child  |

|                                            Returns                                            |
|-----------------------------------------------------------------------------------------------|---------------------------------|
| [Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query) | A query with the new constraint |

### get

```
funÂ get():Â Task<DataSnapshot!>
```

Gets the server values for this query. Updates the cache and raises events if successful. If not connected, falls back to a locally-cached value.  

### getRef

```
funÂ getRef():Â DatabaseReference
```  

|                                                        Returns                                                        |
|-----------------------------------------------------------------------------------------------------------------------|--------------------------------------|
| [DatabaseReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference) | A DatabaseReference to this location |

### keepSynced

```
funÂ keepSynced(keepSynced:Â Boolean):Â Unit
```

By calling \`keepSynced(true)\` on a location, the data for that location will automatically be downloaded and kept in sync, even when no listeners are attached for that location. Additionally, while a location is kept synced, it will not be evicted from the persistent disk cache.

2.3  

|                                            Parameters                                            |
|--------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| `keepSynced: `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | Pass \`true\` to keep this location synchronized, pass \`false\` to stop synchronization. |

### limitToFirst

```
funÂ limitToFirst(limit:Â Int):Â Query
```

Creates a query with limit and anchor it to the start of the window.

2.0  

|                                     Parameters                                      |
|-------------------------------------------------------------------------------------|---------------------------------------------|
| `limit: `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | The maximum number of child nodes to return |

|                                            Returns                                            |
|-----------------------------------------------------------------------------------------------|---------------------------------|
| [Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query) | A query with the new constraint |

### limitToLast

```
funÂ limitToLast(limit:Â Int):Â Query
```

Creates a query with limit and anchor it to the end of the window.

2.0  

|                                     Parameters                                      |
|-------------------------------------------------------------------------------------|---------------------------------------------|
| `limit: `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | The maximum number of child nodes to return |

|                                            Returns                                            |
|-----------------------------------------------------------------------------------------------|---------------------------------|
| [Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query) | A query with the new constraint |

### orderByChild

```
funÂ orderByChild(path:Â String):Â Query
```

Creates a query in which child nodes are ordered by the values of the specified path.

2.0  

|                                        Parameters                                        |
|------------------------------------------------------------------------------------------|-----------------------------------------------|
| `path: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | The path to the child node to use for sorting |

|                                            Returns                                            |
|-----------------------------------------------------------------------------------------------|---------------------------------|
| [Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query) | A query with the new constraint |

### orderByKey

```
funÂ orderByKey():Â Query
```

Creates a query in which child nodes are ordered by their keys.

2.0  

|                                            Returns                                            |
|-----------------------------------------------------------------------------------------------|---------------------------------|
| [Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query) | A query with the new constraint |

### orderByPriority

```
funÂ orderByPriority():Â Query
```

Creates a query in which child nodes are ordered by their priorities.

2.0  

|                                            Returns                                            |
|-----------------------------------------------------------------------------------------------|---------------------------------|
| [Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query) | A query with the new constraint |

### orderByValue

```
funÂ orderByValue():Â Query
```

Creates a query in which nodes are ordered by their value

2.2  

|                                            Returns                                            |
|-----------------------------------------------------------------------------------------------|---------------------------------|
| [Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query) | A query with the new constraint |

### removeEventListener

```
funÂ removeEventListener(listener:Â ChildEventListener):Â Unit
```

Remove the specified listener from this location.  

|                                                             Parameters                                                              |
|-------------------------------------------------------------------------------------------------------------------------------------|------------------------|
| `listener: `[ChildEventListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEventListener) | The listener to remove |

### removeEventListener

```
funÂ removeEventListener(listener:Â ValueEventListener):Â Unit
```

Remove the specified listener from this location.  

|                                                             Parameters                                                              |
|-------------------------------------------------------------------------------------------------------------------------------------|------------------------|
| `listener: `[ValueEventListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ValueEventListener) | The listener to remove |

### startAfter

```
funÂ startAfter(value:Â String?):Â Query
```

Creates a query constrained to only return child nodes with a value greater than the given value, using the given `orderBy` directive or priority as default.

19.6  

|                                          Parameters                                          |
|----------------------------------------------------------------------------------------------|----------------------------------|
| `value: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?` | The value to start at, exclusive |

|                                            Returns                                            |
|-----------------------------------------------------------------------------------------------|---------------------------------|
| [Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query) | A query with the new constraint |

### startAfter

```
funÂ startAfter(value:Â Double):Â Query
```

Creates a query constrained to only return child nodes with a value greater than the given value, using the given `orderBy` directive or priority as default.

19.6  

|                                        Parameters                                         |
|-------------------------------------------------------------------------------------------|----------------------------------|
| `value: `[Double](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html) | The value to start at, exclusive |

|                                            Returns                                            |
|-----------------------------------------------------------------------------------------------|---------------------------------|
| [Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query) | A query with the new constraint |

### startAfter

```
funÂ startAfter(value:Â Boolean):Â Query
```

Creates a query constrained to only return child nodes with a value greater than the given value, using the given `orderBy` directive or priority as default.

19.6  

|                                         Parameters                                          |
|---------------------------------------------------------------------------------------------|----------------------------------|
| `value: `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | The value to start at, exclusive |

|                                            Returns                                            |
|-----------------------------------------------------------------------------------------------|---------------------------------|
| [Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query) | A query with the new constraint |

### startAfter

```
funÂ startAfter(value:Â String?,Â key:Â String?):Â Query
```

Creates a query constrained to only return child nodes with a value greater or equal to the given value, using the given `orderBy` directive or priority as default, and additionally only child nodes with a key greater than the given key.

19.6  

|                                          Parameters                                          |
|----------------------------------------------------------------------------------------------|--------------------------------|
| `value: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?` | The value to start at          |
| `key: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?`   | The key to start at, exclusive |

|                                            Returns                                            |
|-----------------------------------------------------------------------------------------------|---------------------------------|
| [Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query) | A query with the new constraint |

### startAfter

```
funÂ startAfter(value:Â Double,Â key:Â String?):Â Query
```

Creates a query constrained to only return child nodes with a value greater than or equal to the given value, using the given `orderBy` directive or priority as default, and additionally only child nodes with a key greater than the given key.

19.6  

|                                         Parameters                                         |
|--------------------------------------------------------------------------------------------|-------------------------------------|
| `value: `[Double](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html)  | The value to start at               |
| `key: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?` | The key name to start at, exclusive |

|                                            Returns                                            |
|-----------------------------------------------------------------------------------------------|---------------------------------|
| [Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query) | A query with the new constraint |

### startAfter

```
funÂ startAfter(value:Â Boolean,Â key:Â String?):Â Query
```

Creates a query constrained to only return child nodes with a value greater than or equal to the given value, using the given `orderBy` directive or priority as default, and additionally only child nodes with a key greater than the given key.

19.6  

|                                         Parameters                                          |
|---------------------------------------------------------------------------------------------|--------------------------------|
| `value: `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | The value to start at          |
| `key: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?`  | The key to start at, exclusive |

|                                            Returns                                            |
|-----------------------------------------------------------------------------------------------|---------------------------------|
| [Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query) | A query with the new constraint |

### startAt

```
funÂ startAt(value:Â String?):Â Query
```

Creates a query constrained to only return child nodes with a value greater than or equal to the given value, using the given `orderBy` directive or priority as default.  

|                                          Parameters                                          |
|----------------------------------------------------------------------------------------------|----------------------------------|
| `value: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?` | The value to start at, inclusive |

|                                            Returns                                            |
|-----------------------------------------------------------------------------------------------|---------------------------------|
| [Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query) | A query with the new constraint |

### startAt

```
funÂ startAt(value:Â Double):Â Query
```

Creates a query constrained to only return child nodes with a value greater than or equal to the given value, using the given `orderBy` directive or priority as default.  

|                                        Parameters                                         |
|-------------------------------------------------------------------------------------------|----------------------------------|
| `value: `[Double](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html) | The value to start at, inclusive |

|                                            Returns                                            |
|-----------------------------------------------------------------------------------------------|---------------------------------|
| [Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query) | A query with the new constraint |

### startAt

```
funÂ startAt(value:Â Boolean):Â Query
```

Creates a query constrained to only return child nodes with a value greater than or equal to the given value, using the given `orderBy` directive or priority as default.

2.0  

|                                         Parameters                                          |
|---------------------------------------------------------------------------------------------|----------------------------------|
| `value: `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | The value to start at, inclusive |

|                                            Returns                                            |
|-----------------------------------------------------------------------------------------------|---------------------------------|
| [Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query) | A query with the new constraint |

### startAt

```
funÂ startAt(value:Â String?,Â key:Â String?):Â Query
```

Creates a query constrained to only return child nodes with a value greater than or equal to the given value, using the given `orderBy` directive or priority as default, and additionally only child nodes with a key greater than or equal to the given key.  

|                                          Parameters                                          |
|----------------------------------------------------------------------------------------------|-------------------------------------|
| `value: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?` | The priority to start at, inclusive |
| `key: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?`   | The key to start at, inclusive      |

|                                            Returns                                            |
|-----------------------------------------------------------------------------------------------|---------------------------------|
| [Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query) | A query with the new constraint |

### startAt

```
funÂ startAt(value:Â Double,Â key:Â String?):Â Query
```

Creates a query constrained to only return child nodes with a value greater than or equal to the given value, using the given `orderBy` directive or priority as default, and additionally only child nodes with a key greater than or equal to the given key.  

|                                         Parameters                                         |
|--------------------------------------------------------------------------------------------|-------------------------------------|
| `value: `[Double](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html)  | The priority to start at, inclusive |
| `key: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?` | The key name to start at, inclusive |

|                                            Returns                                            |
|-----------------------------------------------------------------------------------------------|---------------------------------|
| [Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query) | A query with the new constraint |

### startAt

```
funÂ startAt(value:Â Boolean,Â key:Â String?):Â Query
```

Creates a query constrained to only return child nodes with a value greater than or equal to the given value, using the given `orderBy` directive or priority as default, and additionally only child nodes with a key greater than or equal to the given key.

2.0  

|                                         Parameters                                          |
|---------------------------------------------------------------------------------------------|-------------------------------------|
| `value: `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | The priority to start at, inclusive |
| `key: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?`  | The key to start at, inclusive      |

|                                            Returns                                            |
|-----------------------------------------------------------------------------------------------|---------------------------------|
| [Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query) | A query with the new constraint |

## Extension functions

### values

```
inlineÂ funÂ <TÂ :Â Any> Query.values():Â Flow<T?>
```

Starts listening to this query and emits its values converted to a POJO via a [Flow](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html).

- When the returned flow starts being collected, a [ValueEventListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ValueEventListener) will be attached.

- When the flow completes, the listener will be removed.

## Extension properties

### childEvents

```
valÂ Query.childEvents:Â Flow<ChildEvent>
```

Starts listening to this query's child events and emits its values via a [Flow](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html).

- When the returned flow starts being collected, a [ChildEventListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEventListener) will be attached.

- When the flow completes, the listener will be removed.

### snapshots

```
valÂ Query.snapshots:Â Flow<DataSnapshot>
```

Starts listening to this query and emits its values via a [Flow](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html).

- When the returned flow starts being collected, a [ValueEventListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ValueEventListener) will be attached.

- When the flow completes, the listener will be removed.