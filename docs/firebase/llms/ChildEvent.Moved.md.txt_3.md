# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent.Moved.md.txt

# ChildEvent.Moved

# ChildEvent.Moved


```
data class ChildEvent.Moved : ChildEvent
```

<br />

|---|---|---|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html) |||
| ↳ | [com.google.firebase.database.ChildEvent](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent) ||
|   | ↳ | [com.google.firebase.database.ChildEvent.Moved](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent.Moved) |

*** ** * ** ***

Emitted when a child location's priority changes.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent.Moved#Moved(com.google.firebase.database.DataSnapshot,kotlin.String)(snapshot: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DataSnapshot, previousChildName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?)` |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent.Moved#previousChildName()` The key name of the sibling location ordered before the child |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DataSnapshot` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent.Moved#snapshot()` An immutable snapshot of the data at the location that moved. |

## Public constructors

### Moved

```
Moved(snapshot: DataSnapshot, previousChildName: String?)
```

| Parameters |
|---|---|
| `snapshot: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DataSnapshot` | An immutable snapshot of the data at the location that moved. |
| `previousChildName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | The key name of the sibling location ordered before the child ```kotlin location. This will be null if this location is ordered first. ``` |

## Public properties

### previousChildName

```
val previousChildName: String?
```

The key name of the sibling location ordered before the child

```kotlin
    location. This will be null if this location is ordered first.
```

### snapshot

```
val snapshot: DataSnapshot
```

An immutable snapshot of the data at the location that moved.