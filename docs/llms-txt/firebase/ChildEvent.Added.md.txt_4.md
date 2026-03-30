# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ktx/ChildEvent.Added.md.txt

# ChildEvent.Added

# ChildEvent.Added


```
data class ChildEvent.Added : ChildEvent
```

<br />

|---|---|---|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html) |||
| ↳ | [com.google.firebase.database.ktx.ChildEvent](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ktx/ChildEvent) ||
|   | ↳ | [com.google.firebase.database.ktx.ChildEvent.Added](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ktx/ChildEvent.Added) |

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Emitted when a new child is added to the location.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ktx/ChildEvent.Added#Added(com.google.firebase.database.DataSnapshot,kotlin.String)(snapshot: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DataSnapshot, previousChildName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?)` |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ktx/ChildEvent.Added#previousChildName()` The key name of sibling location ordered before the new child. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DataSnapshot` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ktx/ChildEvent.Added#snapshot()` An immutable snapshot of the data at the new child location |

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