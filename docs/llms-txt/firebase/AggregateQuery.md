# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/AggregateQuery.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateQuery.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateQuery.md.txt

# AggregateQuery

# AggregateQuery


```
class AggregateQuery
```

<br />

*** ** * ** ***

A query that calculates aggregations over an underlying query.

**Subclassing Note**: Cloud Firestore classes are not meant to be subclassed except for use in test mocks. Subclassing is not supported in production code and new SDK releases may break code that does so.

## Summary

|                                                                                                         ### Public functions                                                                                                          |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)                                                                                                                                                    | [equals](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateQuery#equals(java.lang.Object))`(object: `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`!)` Compares this object with the given object for equality.                           |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[AggregateQuerySnapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateQuerySnapshot)`!>` | [get](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateQuery#get(com.google.firebase.firestore.AggregateSource))`(source: `[AggregateSource](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateSource)`)` Executes this query. |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)                                                                                                                                                            | [hashCode](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateQuery#hashCode())`()` Calculates and returns the hash code for this object.                                                                                                                               |

|                                     ### Public properties                                      |
|------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| [Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query) | [query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateQuery#query()) |

## Public functions

### equals

```
funÂ equals(object:Â Any!):Â Boolean
```

Compares this object with the given object for equality.

This object is considered "equal" to the other object if and only if all of the following conditions are satisfied:

1. `object` is a non-null instance of [AggregateQuery](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateQuery).
2. `object` performs the same aggregations as this [AggregateQuery](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateQuery).
3. The underlying [Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query) of `object` compares equal to that of this object.

|                                       Parameters                                        |
|-----------------------------------------------------------------------------------------|----------------------------------------------------|
| `object: `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`!` | The object to compare to this object for equality. |

|                                      Returns                                       |
|------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `true` if this object is "equal" to the given object, as defined above, or ` false` otherwise. |

### get

```
funÂ get(source:Â AggregateSource):Â Task<AggregateQuerySnapshot!>
```

Executes this query.  

|                                                          Parameters                                                          |
|------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------|
| `source: `[AggregateSource](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateSource) | The source from which to acquire the aggregate results. |

|                                                                                                                Returns                                                                                                                |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[AggregateQuerySnapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateQuerySnapshot)`!>` | A [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html) that will be resolved with the results of the query. |

### hashCode

```
funÂ hashCode():Â Int
```

Calculates and returns the hash code for this object.  

|                                  Returns                                   |
|----------------------------------------------------------------------------|--------------------------------|
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | the hash code for this object. |

## Public properties

### query

```
valÂ query:Â Query
```