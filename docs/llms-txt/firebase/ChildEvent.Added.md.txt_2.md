# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/database/ChildEvent.Added.md.txt

# ChildEvent.Added

# ChildEvent.Added


```
public final data class ChildEvent.Added extends ChildEvent
```

<br />

|---|---|---|
| [java.lang.Object](https://developer.android.com/reference/kotlin/java/lang/Object.html) |||
| ↳ | [com.google.firebase.database.ChildEvent](https://firebase.google.com/docs/reference/android/com/google/firebase/database/ChildEvent) ||
|   | ↳ | [com.google.firebase.database.ChildEvent.Added](https://firebase.google.com/docs/reference/android/com/google/firebase/database/ChildEvent.Added) |

*** ** * ** ***

Emitted when a new child is added to the location.

## Summary

| ### Public fields |
|---|---|
| `final https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/ChildEvent.Added#previousChildName()` The key name of sibling location ordered before the new child. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DataSnapshot` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/ChildEvent.Added#snapshot()` An immutable snapshot of the data at the new child location |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/database/ChildEvent.Added#Added(com.google.firebase.database.DataSnapshot,kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DataSnapshot snapshot, https://developer.android.com/reference/kotlin/java/lang/String.html previousChildName)` |

## Public fields

### previousChildName

```
public final String previousChildName
```

The key name of sibling location ordered before the new child. This

```
    will be null for the first child node of a location.
```

### snapshot

```
public final @NonNull DataSnapshot snapshot
```

An immutable snapshot of the data at the new child location

## Public constructors

### Added

```
public Added(@NonNull DataSnapshot snapshot, String previousChildName)
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DataSnapshot snapshot` | An immutable snapshot of the data at the new child location |
| `https://developer.android.com/reference/kotlin/java/lang/String.html previousChildName` | The key name of sibling location ordered before the new child. This ``` will be null for the first child node of a location. ``` |