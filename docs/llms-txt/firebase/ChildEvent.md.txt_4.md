# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ktx/ChildEvent.md.txt

# ChildEvent

# ChildEvent


```
sealed class ChildEvent
```

<br />

Known direct subclasses [ChildEvent.Added](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ktx/ChildEvent.Added), [ChildEvent.Changed](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ktx/ChildEvent.Changed), [ChildEvent.Moved](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ktx/ChildEvent.Moved), [ChildEvent.Removed](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ktx/ChildEvent.Removed)

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ktx/ChildEvent.Added` | **This class is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ktx/ChildEvent.Changed` | **This class is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ktx/ChildEvent.Moved` | **This class is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ktx/ChildEvent.Removed` | **This class is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Used to emit events about changes in the child locations of a given Query when using the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ktx/package-summary#(com.google.firebase.database.Query).childEvents()` Flow.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

## Summary

| ### Nested types |
|---|
| `data class https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ktx/ChildEvent.Added : https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ktx/ChildEvent` **This class is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |
| `data class https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ktx/ChildEvent.Changed : https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ktx/ChildEvent` **This class is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |
| `data class https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ktx/ChildEvent.Moved : https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ktx/ChildEvent` **This class is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |
| `data class https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ktx/ChildEvent.Removed : https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ktx/ChildEvent` **This class is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |

| ### Protected constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ktx/ChildEvent#ChildEvent()()` |

## Protected constructors

### ChildEvent

```
protected ChildEvent()
```