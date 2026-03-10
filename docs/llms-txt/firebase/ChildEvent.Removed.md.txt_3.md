# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent.Removed.md.txt

# ChildEvent.Removed

# ChildEvent.Removed


```
data class ChildEvent.Removed : ChildEvent
```

<br />

|---|---|---|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html) |||
| ↳ | [com.google.firebase.database.ChildEvent](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent) ||
|   | ↳ | [com.google.firebase.database.ChildEvent.Removed](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent.Removed) |

*** ** * ** ***

Emitted when a child is removed from the location.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent.Removed#Removed(com.google.firebase.database.DataSnapshot)(snapshot: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DataSnapshot)` |

| ### Public properties |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DataSnapshot` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent.Removed#snapshot()` An immutable snapshot of the data at the child that was removed. |

## Public constructors

### Removed

```
Removed(snapshot: DataSnapshot)
```

| Parameters |
|---|---|
| `snapshot: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DataSnapshot` | An immutable snapshot of the data at the child that was removed. |

## Public properties

### snapshot

```
val snapshot: DataSnapshot
```

An immutable snapshot of the data at the child that was removed.