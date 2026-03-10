# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ktx/TaskState.InProgress.md.txt

# TaskState.InProgress

# TaskState.InProgress


```
class TaskState.InProgress<T : Any?> : TaskState
```

<br />

|---|---|---|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html) |||
| ↳ | [com.google.firebase.storage.ktx.TaskState](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ktx/TaskState) ||
|   | ↳ | [com.google.firebase.storage.ktx.TaskState.InProgress](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ktx/TaskState.InProgress) |

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Called periodically as data is transferred and can be used to populate an upload/download indicator.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

## Summary

| ### Public constructors |
|---|
| `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ktx/TaskState.InProgress#InProgress(kotlin.Any)(snapshot: T)` |

| ### Public properties |
|---|---|
| `T` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ktx/TaskState.InProgress#snapshot()` |

## Public constructors

### InProgress

```
<T : Any?> InProgress(snapshot: T)
```

## Public properties

### snapshot

```
val snapshot: T
```