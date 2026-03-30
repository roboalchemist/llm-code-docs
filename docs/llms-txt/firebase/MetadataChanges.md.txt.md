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

| ### Enum Values |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MetadataChanges#EXCLUDE` |   |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MetadataChanges#INCLUDE` |   |

| ### Public methods |
|---|---|
| `static https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MetadataChanges` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MetadataChanges#valueOf(java.lang.String)(https://developer.android.com/reference/kotlin/java/lang/String.html name)` Returns the enum constant of this type with the specified name. |
| `static MetadataChanges[]` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MetadataChanges#values()()` Returns an array containing the constants of this enum type, in the order they're declared. |

## Enum Values

### EXCLUDE

```
MetadataChanges MetadataChanges.EXCLUDE
```

### INCLUDE

```
MetadataChanges MetadataChanges.INCLUDE
```

## Public methods

### valueOf

```
public static MetadataChanges valueOf(String name)
```

Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MetadataChanges` | the enum constant with the specified name |

| Throws |
|---|---|
| `https://developer.android.com/reference/kotlin/java/lang/IllegalArgumentException.html java.lang.IllegalArgumentException` | if this enum type has no constant with the specified name |

### values

```
public static MetadataChanges[] values()
```

Returns an array containing the constants of this enum type, in the order they're declared. This method may be used to iterate over the constants.

| Returns |
|---|---|
| `MetadataChanges[]` | an array containing the constants of this enum type, in the order they're declared |