# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/storage/TaskState.InProgress.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ktx/TaskState.InProgress.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/TaskState.InProgress.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/storage/ktx/TaskState.InProgress.md.txt

# TaskState.InProgress

# TaskState.InProgress


```
public final class TaskState.InProgress<TÂ extendsÂ Object> extends TaskState
```

<br />

|---|---|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [java.lang.Object](https://developer.android.com/reference/kotlin/java/lang/Object.html)                                                                              |||
| â³ | [com.google.firebase.storage.ktx.TaskState](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/ktx/TaskState)                          ||
|   | â³ | [com.google.firebase.storage.ktx.TaskState.InProgress](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/ktx/TaskState.InProgress) |

*** ** * ** ***

| **This class is deprecated.**   
| Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Called periodically as data is transferred and can be used to populate an upload/download indicator.

**Important:** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

## Summary

|                                            ### Public fields                                            |
|---------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| `final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` T` | [snapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/ktx/TaskState.InProgress#snapshot()) |

|                                                                                                                                                                 ### Public constructors                                                                                                                                                                 |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `<T extends `[Object](https://developer.android.com/reference/kotlin/java/lang/Object.html)`> `[InProgress](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/ktx/TaskState.InProgress#InProgress(kotlin.Any))`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` T snapshot)` |

## Public fields

### snapshot

```
publicÂ finalÂ @NonNull TÂ snapshot
```  

## Public constructors

### InProgress

```
publicÂ <TÂ extendsÂ Object> InProgress(@NonNull TÂ snapshot)
```