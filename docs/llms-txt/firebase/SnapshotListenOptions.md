# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/SnapshotListenOptions.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SnapshotListenOptions.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SnapshotListenOptions.md.txt

# SnapshotListenOptions

# SnapshotListenOptions


```
public final class SnapshotListenOptions
```

<br />

*** ** * ** ***

An options object that configures the behavior of `addSnapshotListener()` calls. Instances of this class control settings such as whether metadata-only changes trigger events, the preferred data source (server or cache), and the executor for listener callbacks.

## Summary

|                                                                                                                                                          ### Nested types                                                                                                                                                          |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `public class `[SnapshotListenOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SnapshotListenOptions.Builder) Builder for constructing [SnapshotListenOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SnapshotListenOptions) instances. |

|                                                      ### Public fields                                                      |
|-----------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `final `[Activity](https://developer.android.com/reference/kotlin/android/app/Activity.html)                                | [activity](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SnapshotListenOptions#activity()) The activity to scope the listener to.                                                |
| `final `[Executor](https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html)                       | [executor](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SnapshotListenOptions#executor()) The executor to use to call the listener.                                             |
| `final `[MetadataChanges](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MetadataChanges) | [metadataChanges](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SnapshotListenOptions#metadataChanges()) Indicates whether metadata-only changes should trigger snapshot events. |
| `final `[ListenSource](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/ListenSource)       | [source](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SnapshotListenOptions#source()) Specifies the data source for the listener.                                               |

|                                                                                                 ### Public methods                                                                                                  |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `boolean`                                                                                                                                                                                                           | [equals](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SnapshotListenOptions#equals(java.lang.Object))`(`[Object](https://developer.android.com/reference/kotlin/java/lang/Object.html)` o)`             |
| `@`[Nullable](https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html)` `[Activity](https://developer.android.com/reference/kotlin/android/app/Activity.html)                              | [getActivity](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SnapshotListenOptions#getActivity())`()` Returns the optional Activity that scopes this snapshot listener's lifespan.                        |
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Executor](https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html)                       | [getExecutor](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SnapshotListenOptions#getExecutor())`()` Returns the executor that will be used to execute the snapshot listener's callback.                 |
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[MetadataChanges](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MetadataChanges) | [getMetadataChanges](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SnapshotListenOptions#getMetadataChanges())`()` Returns the setting for whether metadata-only changes should trigger snapshot events. |
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[ListenSource](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/ListenSource)       | [getSource](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SnapshotListenOptions#getSource())`()` Returns the preferred source for retrieving data in snapshot listeners.                                 |
| `int`                                                                                                                                                                                                               | [hashCode](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SnapshotListenOptions#hashCode())`()`                                                                                                           |
| [String](https://developer.android.com/reference/kotlin/java/lang/String.html)                                                                                                                                      | [toString](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SnapshotListenOptions#toString())`()`                                                                                                           |

## Public fields

### activity

```
publicÂ finalÂ ActivityÂ activity
```

The activity to scope the listener to.  

### executor

```
publicÂ finalÂ ExecutorÂ executor
```

The executor to use to call the listener.  

### metadataChanges

```
publicÂ finalÂ MetadataChangesÂ metadataChanges
```

Indicates whether metadata-only changes should trigger snapshot events.  

### source

```
publicÂ finalÂ ListenSourceÂ source
```

Specifies the data source for the listener.  

## Public methods

### equals

```
publicÂ booleanÂ equals(ObjectÂ o)
```  

### getActivity

```
publicÂ @Nullable ActivityÂ getActivity()
```

Returns the optional Activity that scopes this snapshot listener's lifespan. If provided, the listener will automatically stop receiving events when the activity is destroyed.  

|                                                                                        Returns                                                                                         |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| `@`[Nullable](https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html)` `[Activity](https://developer.android.com/reference/kotlin/android/app/Activity.html) | The Activity associated with this listener, or null if no activity is set. |

### getExecutor

```
publicÂ @NonNull ExecutorÂ getExecutor()
```

Returns the executor that will be used to execute the snapshot listener's callback.  

|                                                                                            Returns                                                                                            |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Executor](https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html) | The executor for snapshot listener callbacks. |

### getMetadataChanges

```
publicÂ @NonNull MetadataChangesÂ getMetadataChanges()
```

Returns the setting for whether metadata-only changes should trigger snapshot events.  

|                                                                                                       Returns                                                                                                       |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[MetadataChanges](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MetadataChanges) | The setting object for metadata-only changes. |

### getSource

```
publicÂ @NonNull ListenSourceÂ getSource()
```

Returns the preferred source for retrieving data in snapshot listeners.  

|                                                                                                    Returns                                                                                                    |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[ListenSource](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/ListenSource) | The listen source for retrieving data. |

### hashCode

```
publicÂ intÂ hashCode()
```  

### toString

```
publicÂ StringÂ toString()
```