# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/database/ChildEvent.Removed.md.txt

# ChildEvent.Removed

# ChildEvent.Removed


```
public final data class ChildEvent.Removed extends ChildEvent
```

<br />

|---|---|---|
| [java.lang.Object](https://developer.android.com/reference/kotlin/java/lang/Object.html) |||
| ↳ | [com.google.firebase.database.ChildEvent](https://firebase.google.com/docs/reference/android/com/google/firebase/database/ChildEvent) ||
|   | ↳ | [com.google.firebase.database.ChildEvent.Removed](https://firebase.google.com/docs/reference/android/com/google/firebase/database/ChildEvent.Removed) |

*** ** * ** ***

Emitted when a child is removed from the location.

## Summary

| ### Public fields |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DataSnapshot` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/ChildEvent.Removed#snapshot()` An immutable snapshot of the data at the child that was removed. |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/database/ChildEvent.Removed#Removed(com.google.firebase.database.DataSnapshot)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DataSnapshot snapshot)` |

## Public fields

### snapshot

```
public final @NonNull DataSnapshot snapshot
```

An immutable snapshot of the data at the child that was removed.

## Public constructors

### Removed

```
public Removed(@NonNull DataSnapshot snapshot)
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DataSnapshot snapshot` | An immutable snapshot of the data at the child that was removed. |