# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/storage/ktx/TaskState.InProgress.md.txt

# TaskState.InProgress

# TaskState.InProgress


```
public final class TaskState.InProgress<T extends Object> extends TaskState
```

<br />

|---|---|---|
| [java.lang.Object](https://developer.android.com/reference/kotlin/java/lang/Object.html) |||
| ↳ | [com.google.firebase.storage.ktx.TaskState](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/ktx/TaskState) ||
|   | ↳ | [com.google.firebase.storage.ktx.TaskState.InProgress](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/ktx/TaskState.InProgress) |

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Called periodically as data is transferred and can be used to populate an upload/download indicator.

**Important:** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

## Summary

| ### Public fields |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/ktx/TaskState.InProgress#snapshot()` |

| ### Public constructors |
|---|
| `<T extends https://developer.android.com/reference/kotlin/java/lang/Object.html> https://firebase.google.com/docs/reference/android/com/google/firebase/storage/ktx/TaskState.InProgress#InProgress(kotlin.Any)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T snapshot)` |

## Public fields

### snapshot

```
public final @NonNull T snapshot
```

## Public constructors

### InProgress

```
public <T extends Object> InProgress(@NonNull T snapshot)
```