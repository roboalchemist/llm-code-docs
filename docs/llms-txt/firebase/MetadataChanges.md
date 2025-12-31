# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MetadataChanges.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MetadataChanges.md.txt

# MetadataChanges

# MetadataChanges


```
public enum MetadataChanges
```

<br />

*** ** * ** ***

Indicates whether metadata-only changes (that is, only `DocumentSnapshot.getMetadata()` or `QuerySnapshot.getMetadata()` changed) should trigger snapshot events.

## Summary

|                                                   ### Enum Values                                                   |
|---------------------------------------------------------------------------------------------------------------------|---|
| [EXCLUDE](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MetadataChanges#EXCLUDE) |   |
| [INCLUDE](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MetadataChanges#INCLUDE) |   |

|                                                      ### Public methods                                                      |
|------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `static `[MetadataChanges](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MetadataChanges) | [valueOf](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MetadataChanges#valueOf(java.lang.String))`(`[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` name)` Returns the enum constant of this type with the specified name. |
| `static MetadataChanges[]`                                                                                                   | [values](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MetadataChanges#values())`()` Returns an array containing the constants of this enum type, in the order they're declared.                                                                            |

## Enum Values

### EXCLUDE

```
MetadataChangesÂ MetadataChanges.EXCLUDE
```  

### INCLUDE

```
MetadataChangesÂ MetadataChanges.INCLUDE
```  

## Public methods

### valueOf

```
publicÂ staticÂ MetadataChangesÂ valueOf(StringÂ name)
```

Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)  

|                                                       Returns                                                       |
|---------------------------------------------------------------------------------------------------------------------|-------------------------------------------|
| [MetadataChanges](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MetadataChanges) | the enum constant with the specified name |

|                                                                              Throws                                                                               |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| [java.lang.IllegalArgumentException](https://developer.android.com/reference/kotlin/java/lang/IllegalArgumentException.html)` java.lang.IllegalArgumentException` | if this enum type has no constant with the specified name |

### values

```
publicÂ staticÂ MetadataChanges[]Â values()
```

Returns an array containing the constants of this enum type, in the order they're declared. This method may be used to iterate over the constants.  

|       Returns       |
|---------------------|------------------------------------------------------------------------------------|
| `MetadataChanges[]` | an array containing the constants of this enum type, in the order they're declared |