# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/storage/ktx/TaskState.Paused.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/TaskState.Paused.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/storage/TaskState.Paused.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ktx/TaskState.Paused.md.txt

# TaskState.Paused

# TaskState.Paused


```
class TaskState.Paused<TÂ :Â Any?> : TaskState
```

<br />

|---|---|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)                                                                            |||
| â³ | [com.google.firebase.storage.ktx.TaskState](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ktx/TaskState)                  ||
|   | â³ | [com.google.firebase.storage.ktx.TaskState.Paused](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ktx/TaskState.Paused) |

*** ** * ** ***

| **This class is deprecated.**   
| Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Called any time the upload/download is paused.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

## Summary

|                                                                                                       ### Public constructors                                                                                                        |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `<T : `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`?> `[Paused](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ktx/TaskState.Paused#Paused(kotlin.Any))`(snapshot: T)` |

| ### Public properties |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------|
| `T`                   | [snapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ktx/TaskState.Paused#snapshot()) |

## Public constructors

### Paused

```
<TÂ :Â Any?> Paused(snapshot:Â T)
```  

## Public properties

### snapshot

```
valÂ snapshot:Â T
```