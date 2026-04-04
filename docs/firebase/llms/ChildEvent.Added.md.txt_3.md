# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent.Added.md.txt

# ChildEvent.Added

# ChildEvent.Added


```
data class ChildEvent.Added : ChildEvent
```

<br />

|---|---|---|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html) |||
| ↳ | [com.google.firebase.database.ChildEvent](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent) ||
|   | ↳ | [com.google.firebase.database.ChildEvent.Added](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent.Added) |

*** ** * ** ***

Emitted when a new child is added to the location.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent.Added#Added(com.google.firebase.database.DataSnapshot,kotlin.String)(snapshot: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DataSnapshot, previousChildName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?)` |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent.Added#previousChildName()` The key name of sibling location ordered before the new child. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DataSnapshot` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent.Added#snapshot()` An immutable snapshot of the data at the new child location |

## Public constructors

### Added

```
Added(snapshot: DataSnapshot, previousChildName: String?)
```

| Parameters |
|---|---|
| `snapshot: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DataSnapshot` | An immutable snapshot of the data at the new child location |
| `previousChildName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | The key name of sibling location ordered before the new child. This ```kotlin will be null for the first child node of a location. ``` |

## Public properties

### previousChildName

```
val previousChildName: String?
```

The key name of sibling location ordered before the new child. This

```kotlin
    will be null for the first child node of a location.
```

### snapshot

```
val snapshot: DataSnapshot
```

An immutable snapshot of the data at the new child location