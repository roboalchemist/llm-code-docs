# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ktx/ChildEvent.Moved.md.txt

# ChildEvent.Moved

# ChildEvent.Moved


```
data class ChildEvent.Moved : ChildEvent
```

<br />

|---|---|---|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html) |||
| ↳ | [com.google.firebase.database.ktx.ChildEvent](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ktx/ChildEvent) ||
|   | ↳ | [com.google.firebase.database.ktx.ChildEvent.Moved](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ktx/ChildEvent.Moved) |

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Emitted when a child location's priority changes.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ktx/ChildEvent.Moved#Moved(com.google.firebase.database.DataSnapshot,kotlin.String)(snapshot: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DataSnapshot, previousChildName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?)` |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ktx/ChildEvent.Moved#previousChildName()` The key name of the sibling location ordered before the child |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DataSnapshot` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ktx/ChildEvent.Moved#snapshot()` An immutable snapshot of the data at the location that moved. |

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