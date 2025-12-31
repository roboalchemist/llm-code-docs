# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentChange.Type.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentChange.Type.md.txt

# DocumentChange.Type

# DocumentChange.Type


```
enum DocumentChange.Type
```

<br />

*** ** * ** ***

An enumeration of snapshot diff types.

## Summary

|                                                     ### Enum Values                                                      |
|--------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| [ADDED](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentChange.Type#ADDED)       | Indicates a new document was added to the set of documents matching the query.                    |
| [MODIFIED](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentChange.Type#MODIFIED) | Indicates a document within the query was modified.                                               |
| [REMOVED](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentChange.Type#REMOVED)   | Indicates a document within the query was removed (either deleted or no longer matches the query. |

|                                                                                                      ### Public functions                                                                                                      |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `java-static `[DocumentChange.Type](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentChange.Type)`!`                                                                                    | [valueOf](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentChange.Type#valueOf(java.lang.String))`(name: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!)` Returns the enum constant of this type with the specified name. |
| `java-static `[Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)`<`[DocumentChange.Type](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentChange.Type)`!>!` | [values](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentChange.Type#values())`()` Returns an array containing the constants of this enum type, in the order they're declared.                                                                                |

## Enum Values

### ADDED

```
valÂ DocumentChange.Type.ADDED:Â DocumentChange.Type
```

Indicates a new document was added to the set of documents matching the query.  

### MODIFIED

```
valÂ DocumentChange.Type.MODIFIED:Â DocumentChange.Type
```

Indicates a document within the query was modified.  

### REMOVED

```
valÂ DocumentChange.Type.REMOVED:Â DocumentChange.Type
```

Indicates a document within the query was removed (either deleted or no longer matches the query.  

## Public functions

### valueOf

```
java-staticÂ funÂ valueOf(name:Â String!):Â DocumentChange.Type!
```

Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)  

|                                                            Returns                                                            |
|-------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------|
| [DocumentChange.Type](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentChange.Type)`!` | the enum constant with the specified name |

|                                                                               Throws                                                                               |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| `java.lang.IllegalArgumentException: `[java.lang.IllegalArgumentException](https://developer.android.com/reference/kotlin/java/lang/IllegalArgumentException.html) | if this enum type has no constant with the specified name |

### values

```
java-staticÂ funÂ values():Â Array<DocumentChange.Type!>!
```

Returns an array containing the constants of this enum type, in the order they're declared. This method may be used to iterate over the constants.  

|                                                                                                     Returns                                                                                                      |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| [Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)`<`[DocumentChange.Type](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentChange.Type)`!>!` | an array containing the constants of this enum type, in the order they're declared |