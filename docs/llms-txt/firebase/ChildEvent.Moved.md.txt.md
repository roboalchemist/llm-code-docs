# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/database/ChildEvent.Moved.md.txt

# ChildEvent.Moved

# ChildEvent.Moved


```
public final data class ChildEvent.Moved extends ChildEvent
```

<br />

|---|---|---|
| [java.lang.Object](https://developer.android.com/reference/kotlin/java/lang/Object.html) |||
| ↳ | [com.google.firebase.database.ChildEvent](https://firebase.google.com/docs/reference/android/com/google/firebase/database/ChildEvent) ||
|   | ↳ | [com.google.firebase.database.ChildEvent.Moved](https://firebase.google.com/docs/reference/android/com/google/firebase/database/ChildEvent.Moved) |

*** ** * ** ***

Emitted when a child location's priority changes.

## Summary

| ### Public fields |
|---|---|
| `final https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/ChildEvent.Moved#previousChildName()` The key name of the sibling location ordered before the child |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DataSnapshot` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/ChildEvent.Moved#snapshot()` An immutable snapshot of the data at the location that moved. |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/database/ChildEvent.Moved#Moved(com.google.firebase.database.DataSnapshot,kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DataSnapshot snapshot, https://developer.android.com/reference/kotlin/java/lang/String.html previousChildName)` |

## Public fields

### previousChildName

```
public final String previousChildName
```

The key name of the sibling location ordered before the child

```
    location. This will be null if this location is ordered first.
```

### snapshot

```
public final @NonNull DataSnapshot snapshot
```

An immutable snapshot of the data at the location that moved.

## Public constructors

### Moved

```
public Moved(@NonNull DataSnapshot snapshot, String previousChildName)
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DataSnapshot snapshot` | An immutable snapshot of the data at the location that moved. |
| `https://developer.android.com/reference/kotlin/java/lang/String.html previousChildName` | The key name of the sibling location ordered before the child ``` location. This will be null if this location is ordered first. ``` |