# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/LoadBundleTaskProgress.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress.md.txt

# LoadBundleTaskProgress

# LoadBundleTaskProgress


```
public final class LoadBundleTaskProgress
```

<br />

*** ** * ** ***

Represents a progress update or a final state from loading bundles.

## Summary

|                                                                                                 ### Nested types                                                                                                  |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `public enum `[LoadBundleTaskProgress.TaskState](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress.TaskState) Represents the state of bundle loading tasks. |

|                                                                                                                      ### Public fields                                                                                                                      |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| `final long`                                                                                                                                                                                                                                                | [bytesLoaded](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress#bytesLoaded())         |
| `final int`                                                                                                                                                                                                                                                 | [documentsLoaded](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress#documentsLoaded()) |
| `final @`[Nullable](https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html)` `[Exception](https://developer.android.com/reference/kotlin/java/lang/Exception.html)                                                                | [exception](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress#exception())             |
| `final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[LoadBundleTaskProgress.TaskState](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress.TaskState) | [taskState](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress#taskState())             |
| `final long`                                                                                                                                                                                                                                                | [totalBytes](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress#totalBytes())           |
| `final int`                                                                                                                                                                                                                                                 | [totalDocuments](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress#totalDocuments())   |

|                                                                                                                  ### Public methods                                                                                                                   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `boolean`                                                                                                                                                                                                                                             | [equals](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress#equals(java.lang.Object))`(`[Object](https://developer.android.com/reference/kotlin/java/lang/Object.html)` o)`                                                                   |
| `long`                                                                                                                                                                                                                                                | [getBytesLoaded](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress#getBytesLoaded())`()` Returns how many bytes have been loaded.                                                                                                            |
| `int`                                                                                                                                                                                                                                                 | [getDocumentsLoaded](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress#getDocumentsLoaded())`()` Returns how many documents have been loaded.                                                                                                |
| `@`[Nullable](https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html)` `[Exception](https://developer.android.com/reference/kotlin/java/lang/Exception.html)                                                                | [getException](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress#getException())`()` If the [LoadBundleTask](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTask) failed, returns the exception. |
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[LoadBundleTaskProgress.TaskState](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress.TaskState) | [getTaskState](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress#getTaskState())`()` Returns the current state of the [LoadBundleTask](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTask).     |
| `long`                                                                                                                                                                                                                                                | [getTotalBytes](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress#getTotalBytes())`()` Returns the total number of bytes in the bundle.                                                                                                      |
| `int`                                                                                                                                                                                                                                                 | [getTotalDocuments](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress#getTotalDocuments())`()` Returns the total number of documents in the bundle.                                                                                          |
| `int`                                                                                                                                                                                                                                                 | [hashCode](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress#hashCode())`()`                                                                                                                                                                 |

## Public fields

### bytesLoaded

```
publicÂ finalÂ longÂ bytesLoaded
```  

### documentsLoaded

```
publicÂ finalÂ intÂ documentsLoaded
```  

### exception

```
publicÂ finalÂ @Nullable ExceptionÂ exception
```  

### taskState

```
publicÂ finalÂ @NonNull LoadBundleTaskProgress.TaskStateÂ taskState
```  

### totalBytes

```
publicÂ finalÂ longÂ totalBytes
```  

### totalDocuments

```
publicÂ finalÂ intÂ totalDocuments
```  

## Public methods

### equals

```
publicÂ booleanÂ equals(ObjectÂ o)
```  

### getBytesLoaded

```
publicÂ longÂ getBytesLoaded()
```

Returns how many bytes have been loaded.  

### getDocumentsLoaded

```
publicÂ intÂ getDocumentsLoaded()
```

Returns how many documents have been loaded.  

### getException

```
publicÂ @Nullable ExceptionÂ getException()
```

If the [LoadBundleTask](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTask) failed, returns the exception. Otherwise, returns `null`.  

### getTaskState

```
publicÂ @NonNull LoadBundleTaskProgress.TaskStateÂ getTaskState()
```

Returns the current state of the [LoadBundleTask](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTask).  

### getTotalBytes

```
publicÂ longÂ getTotalBytes()
```

Returns the total number of bytes in the bundle. Returns 0 if the bundle failed to parse.  

### getTotalDocuments

```
publicÂ intÂ getTotalDocuments()
```

Returns the total number of documents in the bundle. Returns 0 if the bundle failed to parse.  

### hashCode

```
publicÂ intÂ hashCode()
```