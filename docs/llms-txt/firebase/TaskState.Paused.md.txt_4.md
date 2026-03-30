# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ktx/TaskState.Paused.md.txt

# TaskState.Paused

# TaskState.Paused


```
class TaskState.Paused<T : Any?> : TaskState
```

<br />

|---|---|---|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html) |||
| ↳ | [com.google.firebase.storage.ktx.TaskState](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ktx/TaskState) ||
|   | ↳ | [com.google.firebase.storage.ktx.TaskState.Paused](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ktx/TaskState.Paused) |

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Called any time the upload/download is paused.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

## Summary

| ### Public constructors |
|---|
| `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ktx/TaskState.Paused#Paused(kotlin.Any)(snapshot: T)` |

| ### Public properties |
|---|---|
| `T` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ktx/TaskState.Paused#snapshot()` |

## Public constructors

### Paused

```
<T : Any?> Paused(snapshot: T)
```

## Public properties

### snapshot

```
val snapshot: T
```