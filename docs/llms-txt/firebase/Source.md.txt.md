# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Source.md.txt

# Source

# Source


```
public enum Source
```

<br />

*** ** * ** ***

Configures the behavior of `get()` calls on `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentReference` and `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Query`. By providing a `Source` value, these methods can be configured to fetch results only from the server, only from the local cache, or attempt to fetch results from the server and fall back to the cache (which is the default).

## Summary

| ### Enum Values |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Source#CACHE` | Causes Cloud Firestore to immediately return a value from the cache, ignoring the server completely (implying that the returned value may be stale with respect to the value on the server). |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Source#DEFAULT` | Causes Cloud Firestore to try to retrieve an up-to-date (server-retrieved) snapshot, but fall back to returning cached data if the server can't be reached. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Source#SERVER` | Causes Cloud Firestore to avoid the cache, generating an error if the server cannot be reached. |

| ### Public methods |
|---|---|
| `static https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Source` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Source#valueOf(java.lang.String)(https://developer.android.com/reference/kotlin/java/lang/String.html name)` Returns the enum constant of this type with the specified name. |
| `static Source[]` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Source#values()()` Returns an array containing the constants of this enum type, in the order they're declared. |

## Enum Values

### CACHE

```
Source Source.CACHE
```

Causes Cloud Firestore to immediately return a value from the cache, ignoring the server completely (implying that the returned value may be stale with respect to the value on the server). If there is no data in the cache to satisfy the `get()` call, `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentReference#get()` will return an error and `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Query#get()` will return an empty `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/QuerySnapshot` with no documents.

### DEFAULT

```
Source Source.DEFAULT
```

Causes Cloud Firestore to try to retrieve an up-to-date (server-retrieved) snapshot, but fall back to returning cached data if the server can't be reached.

### SERVER

```
Source Source.SERVER
```

Causes Cloud Firestore to avoid the cache, generating an error if the server cannot be reached. Note that the cache will still be updated if the server request succeeds. Also note that latency-compensation still takes effect, so any pending write operations will be visible in the returned data (merged into the server-provided data).

## Public methods

### valueOf

```
public static Source valueOf(String name)
```

Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Source` | the enum constant with the specified name |

| Throws |
|---|---|
| `https://developer.android.com/reference/kotlin/java/lang/IllegalArgumentException.html java.lang.IllegalArgumentException` | if this enum type has no constant with the specified name |

### values

```
public static Source[] values()
```

Returns an array containing the constants of this enum type, in the order they're declared. This method may be used to iterate over the constants.

| Returns |
|---|---|
| `Source[]` | an array containing the constants of this enum type, in the order they're declared |