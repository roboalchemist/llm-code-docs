# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior.md.txt

# DocumentSnapshot.ServerTimestampBehavior

# DocumentSnapshot.ServerTimestampBehavior


```
public enum DocumentSnapshot.ServerTimestampBehavior
```

<br />

*** ** * ** ***

Controls the return value for server timestamps that have not yet been set to their final value.

## Summary

|                                                                ### Enum Values                                                                 |
|------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ESTIMATE](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior#ESTIMATE) | Return local estimates for [ServerTimestamps](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldValue#serverTimestamp()) that have not yet been set to their final value.    |
| [NONE](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior#NONE)         | Return `null` for [ServerTimestamps](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldValue#serverTimestamp()) that have not yet been set to their final value.             |
| [PREVIOUS](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior#PREVIOUS) | Return the previous value for [ServerTimestamps](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldValue#serverTimestamp()) that have not yet been set to their final value. |

|                                                                               ### Public methods                                                                               |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `static `[DocumentSnapshot.ServerTimestampBehavior](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior) | [valueOf](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior#valueOf(java.lang.String))`(`[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` name)` Returns the enum constant of this type with the specified name. |
| `static DocumentSnapshot.ServerTimestampBehavior[]`                                                                                                                            | [values](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior#values())`()` Returns an array containing the constants of this enum type, in the order they're declared.                                                                            |

## Enum Values

### ESTIMATE

```
DocumentSnapshot.ServerTimestampBehaviorÂ DocumentSnapshot.ServerTimestampBehavior.ESTIMATE
```

Return local estimates for [ServerTimestamps](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldValue#serverTimestamp()) that have not yet been set to their final value. This estimate will likely differ from the final value and may cause these pending values to change once the server result becomes available.  

### NONE

```
DocumentSnapshot.ServerTimestampBehaviorÂ DocumentSnapshot.ServerTimestampBehavior.NONE
```

Return `null` for [ServerTimestamps](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldValue#serverTimestamp()) that have not yet been set to their final value.  

### PREVIOUS

```
DocumentSnapshot.ServerTimestampBehaviorÂ DocumentSnapshot.ServerTimestampBehavior.PREVIOUS
```

Return the previous value for [ServerTimestamps](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldValue#serverTimestamp()) that have not yet been set to their final value.  

## Public methods

### valueOf

```
publicÂ staticÂ DocumentSnapshot.ServerTimestampBehaviorÂ valueOf(StringÂ name)
```

Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)  

|                                                                                Returns                                                                                |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------|
| [DocumentSnapshot.ServerTimestampBehavior](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior) | the enum constant with the specified name |

|                                                                              Throws                                                                               |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| [java.lang.IllegalArgumentException](https://developer.android.com/reference/kotlin/java/lang/IllegalArgumentException.html)` java.lang.IllegalArgumentException` | if this enum type has no constant with the specified name |

### values

```
publicÂ staticÂ DocumentSnapshot.ServerTimestampBehavior[]Â values()
```

Returns an array containing the constants of this enum type, in the order they're declared. This method may be used to iterate over the constants.  

|                   Returns                    |
|----------------------------------------------|------------------------------------------------------------------------------------|
| `DocumentSnapshot.ServerTimestampBehavior[]` | an array containing the constants of this enum type, in the order they're declared |