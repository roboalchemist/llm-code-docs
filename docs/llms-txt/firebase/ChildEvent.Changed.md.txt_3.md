# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent.Changed.md.txt

# ChildEvent.Changed

# ChildEvent.Changed


```
data class ChildEvent.Changed : ChildEvent
```

<br />

|---|---|---|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html) |||
| ↳ | [com.google.firebase.database.ChildEvent](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent) ||
|   | ↳ | [com.google.firebase.database.ChildEvent.Changed](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent.Changed) |

*** ** * ** ***

Emitted when the data at a child location has changed.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent.Changed#Changed(com.google.firebase.database.DataSnapshot,kotlin.String)(snapshot: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DataSnapshot, previousChildName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?)` |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent.Changed#previousChildName()` The key name of sibling location ordered before the child. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DataSnapshot` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEvent.Changed#snapshot()` An immutable snapshot of the data at the new data at the child location |

## Public constructors

### Changed

```
Changed(snapshot: DataSnapshot, previousChildName: String?)
```

| Parameters |
|---|---|
| `snapshot: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DataSnapshot` | An immutable snapshot of the data at the new data at the child location |
| `previousChildName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | The key name of sibling location ordered before the child. This will ```kotlin be null for the first child node of a location. ``` |

## Public properties

### previousChildName

```
val previousChildName: String?
```

The key name of sibling location ordered before the child. This will

```kotlin
    be null for the first child node of a location.
```

### snapshot

```
val snapshot: DataSnapshot
```

An immutable snapshot of the data at the new data at the child location