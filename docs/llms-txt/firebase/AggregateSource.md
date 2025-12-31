# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateSource.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/AggregateSource.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateSource.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/AggregateSource.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateSource.md.txt

# AggregateSource

# AggregateSource


```
enum AggregateSource
```

<br />

*** ** * ** ***

The sources from which an [AggregateQuery](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateQuery) can retrieve its results.  

|                                                                         See also                                                                         |
|----------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| [get](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateQuery#get(com.google.firebase.firestore.AggregateSource)) |   |

## Summary

|                                                 ### Enum Values                                                  |
|------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|
| [SERVER](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateSource#SERVER) | Perform the aggregation on the server and download the result. |

|                                                                                                  ### Public functions                                                                                                  |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `java-static `[AggregateSource](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateSource)`!`                                                                                    | [valueOf](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateSource#valueOf(java.lang.String))`(name: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!)` Returns the enum constant of this type with the specified name. |
| `java-static `[Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)`<`[AggregateSource](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateSource)`!>!` | [values](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateSource#values())`()` Returns an array containing the constants of this enum type, in the order they're declared.                                                                                |

## Enum Values

### SERVER

```
valÂ AggregateSource.SERVER:Â AggregateSource
```

Perform the aggregation on the server and download the result.

The result received from the server is presented, unaltered, without considering any local state. That is, documents in the local cache are not taken into consideration, neither are local modifications not yet synchronized with the server. Previously-downloaded results, if any, are not used. Every request using this source necessarily involves a round trip to the server.

The [AggregateQuery](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateQuery) will fail if the server cannot be reached, such as if the client is offline.  

## Public functions

### valueOf

```
java-staticÂ funÂ valueOf(name:Â String!):Â AggregateSource!
```

Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)  

|                                                        Returns                                                        |
|-----------------------------------------------------------------------------------------------------------------------|-------------------------------------------|
| [AggregateSource](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateSource)`!` | the enum constant with the specified name |

|                                                                               Throws                                                                               |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| `java.lang.IllegalArgumentException: `[java.lang.IllegalArgumentException](https://developer.android.com/reference/kotlin/java/lang/IllegalArgumentException.html) | if this enum type has no constant with the specified name |

### values

```
java-staticÂ funÂ values():Â Array<AggregateSource!>!
```

Returns an array containing the constants of this enum type, in the order they're declared. This method may be used to iterate over the constants.  

|                                                                                                 Returns                                                                                                  |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| [Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)`<`[AggregateSource](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateSource)`!>!` | an array containing the constants of this enum type, in the order they're declared |