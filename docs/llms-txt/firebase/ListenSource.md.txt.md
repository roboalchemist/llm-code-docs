# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/ListenSource.md.txt

# ListenSource

# ListenSource


```
public enum ListenSource
```

<br />

*** ** * ** ***

Configures the source option of `addSnapshotListener()` calls on `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentReference` and `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Query`. This controls how a listener retrieves data updates.

## Summary

| ### Enum Values |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/ListenSource#CACHE` | The listener retrieves data and listens to updates from the local Firestore cache only. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/ListenSource#DEFAULT` | The default behavior. |

| ### Public methods |
|---|---|
| `static https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/ListenSource` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/ListenSource#valueOf(java.lang.String)(https://developer.android.com/reference/kotlin/java/lang/String.html name)` Returns the enum constant of this type with the specified name. |
| `static ListenSource[]` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/ListenSource#values()()` Returns an array containing the constants of this enum type, in the order they're declared. |

## Enum Values

### CACHE

```
ListenSource ListenSource.CACHE
```

The listener retrieves data and listens to updates from the local Firestore cache only. If the cache is empty, an empty snapshot will be returned. Snapshot events will be triggered on cache updates, like local mutations or load bundles.

Note that the data might be stale if the cache hasn't synchronized with recent server-side changes.

### DEFAULT

```
ListenSource ListenSource.DEFAULT
```

The default behavior. The listener attempts to return initial snapshot from cache and retrieve up-to-date snapshots from the Firestore server. Snapshot events will be triggered on local mutations and server side updates.

## Public methods

### valueOf

```
public static ListenSource valueOf(String name)
```

Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/ListenSource` | the enum constant with the specified name |

| Throws |
|---|---|
| `https://developer.android.com/reference/kotlin/java/lang/IllegalArgumentException.html java.lang.IllegalArgumentException` | if this enum type has no constant with the specified name |

### values

```
public static ListenSource[] values()
```

Returns an array containing the constants of this enum type, in the order they're declared. This method may be used to iterate over the constants.

| Returns |
|---|---|
| `ListenSource[]` | an array containing the constants of this enum type, in the order they're declared |