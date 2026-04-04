# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/database/ChildEvent.Changed.md.txt

# ChildEvent.Changed

# ChildEvent.Changed


```
public final data class ChildEvent.Changed extends ChildEvent
```

<br />

|---|---|---|
| [java.lang.Object](https://developer.android.com/reference/kotlin/java/lang/Object.html) |||
| ↳ | [com.google.firebase.database.ChildEvent](https://firebase.google.com/docs/reference/android/com/google/firebase/database/ChildEvent) ||
|   | ↳ | [com.google.firebase.database.ChildEvent.Changed](https://firebase.google.com/docs/reference/android/com/google/firebase/database/ChildEvent.Changed) |

*** ** * ** ***

Emitted when the data at a child location has changed.

## Summary

| ### Public fields |
|---|---|
| `final https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/ChildEvent.Changed#previousChildName()` The key name of sibling location ordered before the child. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DataSnapshot` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/ChildEvent.Changed#snapshot()` An immutable snapshot of the data at the new data at the child location |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/database/ChildEvent.Changed#Changed(com.google.firebase.database.DataSnapshot,kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DataSnapshot snapshot, https://developer.android.com/reference/kotlin/java/lang/String.html previousChildName)` |

## Public fields

### previousChildName

```
public final String previousChildName
```

The key name of sibling location ordered before the child. This will

```
    be null for the first child node of a location.
```

### snapshot

```
public final @NonNull DataSnapshot snapshot
```

An immutable snapshot of the data at the new data at the child location

## Public constructors

### Changed

```
public Changed(@NonNull DataSnapshot snapshot, String previousChildName)
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DataSnapshot snapshot` | An immutable snapshot of the data at the new data at the child location |
| `https://developer.android.com/reference/kotlin/java/lang/String.html previousChildName` | The key name of sibling location ordered before the child. This will ``` be null for the first child node of a location. ``` |