# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Source.md.txt

# Source

# Source


```
enum Source
```

<br />

*** ** * ** ***

Configures the behavior of `get()` calls on `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference` and `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query`. By providing a `Source` value, these methods can be configured to fetch results only from the server, only from the local cache, or attempt to fetch results from the server and fall back to the cache (which is the default).

## Summary

| ### Enum Values |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Source#CACHE` | Causes Cloud Firestore to immediately return a value from the cache, ignoring the server completely (implying that the returned value may be stale with respect to the value on the server). |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Source#DEFAULT` | Causes Cloud Firestore to try to retrieve an up-to-date (server-retrieved) snapshot, but fall back to returning cached data if the server can't be reached. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Source#SERVER` | Causes Cloud Firestore to avoid the cache, generating an error if the server cannot be reached. |

| ### Public functions |
|---|---|
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Source!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Source#valueOf(java.lang.String)(name: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!)` Returns the enum constant of this type with the specified name. |
| `java-static https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Source!>!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Source#values()()` Returns an array containing the constants of this enum type, in the order they're declared. |

## Enum Values

### CACHE

```
val Source.CACHE: Source
```

Causes Cloud Firestore to immediately return a value from the cache, ignoring the server completely (implying that the returned value may be stale with respect to the value on the server). If there is no data in the cache to satisfy the `get()` call, `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference#get()` will return an error and `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query#get()` will return an empty `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QuerySnapshot` with no documents.

### DEFAULT

```
val Source.DEFAULT: Source
```

Causes Cloud Firestore to try to retrieve an up-to-date (server-retrieved) snapshot, but fall back to returning cached data if the server can't be reached.

### SERVER

```
val Source.SERVER: Source
```

Causes Cloud Firestore to avoid the cache, generating an error if the server cannot be reached. Note that the cache will still be updated if the server request succeeds. Also note that latency-compensation still takes effect, so any pending write operations will be visible in the returned data (merged into the server-provided data).

## Public functions

### valueOf

```
java-static fun valueOf(name: String!): Source!
```

Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Source!` | the enum constant with the specified name |

| Throws |
|---|---|
| `java.lang.IllegalArgumentException: https://developer.android.com/reference/kotlin/java/lang/IllegalArgumentException.html` | if this enum type has no constant with the specified name |

### values

```
java-static fun values(): Array<Source!>!
```

Returns an array containing the constants of this enum type, in the order they're declared. This method may be used to iterate over the constants.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Source!>!` | an array containing the constants of this enum type, in the order they're declared |