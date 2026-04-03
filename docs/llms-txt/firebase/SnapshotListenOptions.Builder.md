# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SnapshotListenOptions.Builder.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SnapshotListenOptions.Builder.md.txt

# SnapshotListenOptions.Builder

# SnapshotListenOptions.Builder


```
class SnapshotListenOptions.Builder
```

<br />

*** ** * ** ***

Builder for constructing [SnapshotListenOptions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SnapshotListenOptions) instances.

## Summary

|                                                        ### Public constructors                                                         |
|----------------------------------------------------------------------------------------------------------------------------------------|
| [Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SnapshotListenOptions.Builder#Builder())`()` |

|                                                              ### Public functions                                                              |
|------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [SnapshotListenOptions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SnapshotListenOptions)                 | [build](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SnapshotListenOptions.Builder#build())`()` Constructs a [SnapshotListenOptions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SnapshotListenOptions) instance using the current settings in this Builder.                                                                               |
| [SnapshotListenOptions.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SnapshotListenOptions.Builder) | [setActivity](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SnapshotListenOptions.Builder#setActivity(android.app.Activity))`(activity: `[Activity](https://developer.android.com/reference/kotlin/android/app/Activity.html)`)` Associates an Activity with this snapshot listener's lifecycle.                                                                                |
| [SnapshotListenOptions.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SnapshotListenOptions.Builder) | [setExecutor](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SnapshotListenOptions.Builder#setExecutor(java.util.concurrent.Executor))`(executor: `[Executor](https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html)`)` Sets the executor to be used for snapshot listener callbacks.                                                                |
| [SnapshotListenOptions.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SnapshotListenOptions.Builder) | [setMetadataChanges](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SnapshotListenOptions.Builder#setMetadataChanges(com.google.firebase.firestore.MetadataChanges))`(metadataChanges: `[MetadataChanges](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MetadataChanges)`)` Sets whether metadata-only changes should trigger snapshot events. |
| [SnapshotListenOptions.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SnapshotListenOptions.Builder) | [setSource](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SnapshotListenOptions.Builder#setSource(com.google.firebase.firestore.ListenSource))`(source: `[ListenSource](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ListenSource)`)` Sets the preferred source for retrieving data in snapshot listeners.                                   |

## Public constructors

### Builder

```
Builder()
```  

## Public functions

### build

```
funÂ build():Â SnapshotListenOptions
```

Constructs a [SnapshotListenOptions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SnapshotListenOptions) instance using the current settings in this Builder.  

|                                                            Returns                                                             |
|--------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------|
| [SnapshotListenOptions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SnapshotListenOptions) | The constructed SnapshotListenOptions instance. |

### setActivity

```
funÂ setActivity(activity:Â Activity):Â SnapshotListenOptions.Builder
```

Associates an Activity with this snapshot listener's lifecycle. If set, the listener will automatically stop when the Activity is destroyed.  

|                                            Parameters                                            |
|--------------------------------------------------------------------------------------------------|----------------------------------------------|
| `activity: `[Activity](https://developer.android.com/reference/kotlin/android/app/Activity.html) | The Activity to associate with the listener. |

|                                                                    Returns                                                                     |
|------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| [SnapshotListenOptions.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SnapshotListenOptions.Builder) | This Builder instance to allow chaining of method calls. |

### setExecutor

```
funÂ setExecutor(executor:Â Executor):Â SnapshotListenOptions.Builder
```

Sets the executor to be used for snapshot listener callbacks.  

|                                                Parameters                                                 |
|-----------------------------------------------------------------------------------------------------------|--------------------------|
| `executor: `[Executor](https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html) | The executor to be used. |

|                                                                    Returns                                                                     |
|------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| [SnapshotListenOptions.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SnapshotListenOptions.Builder) | This Builder instance to allow chaining of method calls. |

### setMetadataChanges

```
funÂ setMetadataChanges(metadataChanges:Â MetadataChanges):Â SnapshotListenOptions.Builder
```

Sets whether metadata-only changes should trigger snapshot events.  

|                                                              Parameters                                                               |
|---------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|
| `metadataChanges: `[MetadataChanges](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MetadataChanges) | The setting for metadata-only changes. |

|                                                                    Returns                                                                     |
|------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| [SnapshotListenOptions.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SnapshotListenOptions.Builder) | This Builder instance to allow chaining of method calls. |

### setSource

```
funÂ setSource(source:Â ListenSource):Â SnapshotListenOptions.Builder
```

Sets the preferred source for retrieving data in snapshot listeners.  

|                                                       Parameters                                                       |
|------------------------------------------------------------------------------------------------------------------------|------------------------------------------|
| `source: `[ListenSource](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ListenSource) | The preferred source for data retrieval. |

|                                                                    Returns                                                                     |
|------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| [SnapshotListenOptions.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SnapshotListenOptions.Builder) | This Builder instance to allow chaining of method calls. |