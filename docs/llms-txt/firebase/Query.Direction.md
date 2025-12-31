# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query.Direction.md.txt

# Query.Direction

# Query.Direction


```
enum Query.Direction
```

<br />

*** ** * ** ***

An enum for the direction of a sort.

## Summary

|                                                     ### Enum Values                                                      |
|--------------------------------------------------------------------------------------------------------------------------|---|
| [ASCENDING](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query.Direction#ASCENDING)   |   |
| [DESCENDING](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query.Direction#DESCENDING) |   |

|                                                                                                  ### Public functions                                                                                                  |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `java-static `[Query.Direction](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query.Direction)`!`                                                                                    | [valueOf](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query.Direction#valueOf(java.lang.String))`(name: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!)` Returns the enum constant of this type with the specified name. |
| `java-static `[Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)`<`[Query.Direction](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query.Direction)`!>!` | [values](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query.Direction#values())`()` Returns an array containing the constants of this enum type, in the order they're declared.                                                                                |

## Enum Values

### ASCENDING

```
valÂ Query.Direction.ASCENDING:Â Query.Direction
```  

### DESCENDING

```
valÂ Query.Direction.DESCENDING:Â Query.Direction
```  

## Public functions

### valueOf

```
java-staticÂ funÂ valueOf(name:Â String!):Â Query.Direction!
```

Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)  

|                                                        Returns                                                        |
|-----------------------------------------------------------------------------------------------------------------------|-------------------------------------------|
| [Query.Direction](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query.Direction)`!` | the enum constant with the specified name |

|                                                                               Throws                                                                               |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| `java.lang.IllegalArgumentException: `[java.lang.IllegalArgumentException](https://developer.android.com/reference/kotlin/java/lang/IllegalArgumentException.html) | if this enum type has no constant with the specified name |

### values

```
java-staticÂ funÂ values():Â Array<Query.Direction!>!
```

Returns an array containing the constants of this enum type, in the order they're declared. This method may be used to iterate over the constants.  

|                                                                                                 Returns                                                                                                  |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| [Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)`<`[Query.Direction](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query.Direction)`!>!` | an array containing the constants of this enum type, in the order they're declared |