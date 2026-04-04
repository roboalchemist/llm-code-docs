# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior.md.txt

# DocumentSnapshot.ServerTimestampBehavior

# DocumentSnapshot.ServerTimestampBehavior


```
enum DocumentSnapshot.ServerTimestampBehavior
```

<br />

*** ** * ** ***

Controls the return value for server timestamps that have not yet been set to their final value.

## Summary

| ### Enum Values |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior#ESTIMATE` | Return local estimates for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldValue#serverTimestamp()` that have not yet been set to their final value. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior#NONE` | Return `null` for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldValue#serverTimestamp()` that have not yet been set to their final value. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior#PREVIOUS` | Return the previous value for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldValue#serverTimestamp()` that have not yet been set to their final value. |

| ### Public functions |
|---|---|
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior#valueOf(java.lang.String)(name: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!)` Returns the enum constant of this type with the specified name. |
| `java-static https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior!>!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior#values()()` Returns an array containing the constants of this enum type, in the order they're declared. |

## Enum Values

### ESTIMATE

```
val DocumentSnapshot.ServerTimestampBehavior.ESTIMATE: DocumentSnapshot.ServerTimestampBehavior
```

Return local estimates for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldValue#serverTimestamp()` that have not yet been set to their final value. This estimate will likely differ from the final value and may cause these pending values to change once the server result becomes available.

### NONE

```
val DocumentSnapshot.ServerTimestampBehavior.NONE: DocumentSnapshot.ServerTimestampBehavior
```

Return `null` for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldValue#serverTimestamp()` that have not yet been set to their final value.

### PREVIOUS

```
val DocumentSnapshot.ServerTimestampBehavior.PREVIOUS: DocumentSnapshot.ServerTimestampBehavior
```

Return the previous value for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldValue#serverTimestamp()` that have not yet been set to their final value.

## Public functions

### valueOf

```
java-static fun valueOf(name: String!): DocumentSnapshot.ServerTimestampBehavior!
```

Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior!` | the enum constant with the specified name |

| Throws |
|---|---|
| `java.lang.IllegalArgumentException: https://developer.android.com/reference/kotlin/java/lang/IllegalArgumentException.html` | if this enum type has no constant with the specified name |

### values

```
java-static fun values(): Array<DocumentSnapshot.ServerTimestampBehavior!>!
```

Returns an array containing the constants of this enum type, in the order they're declared. This method may be used to iterate over the constants.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior!>!` | an array containing the constants of this enum type, in the order they're declared |