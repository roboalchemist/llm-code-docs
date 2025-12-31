# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StreamDownloadTask.StreamProcessor.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask.StreamProcessor.md.txt

# StreamDownloadTask.StreamProcessor

# StreamDownloadTask.StreamProcessor


```
interface StreamDownloadTask.StreamProcessor
```

<br />

*** ** * ** ***

A callback that is used to handle the stream download

## Summary

|                             ### Public functions                             |
|------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | [doInBackground](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask.StreamProcessor#doInBackground(com.google.firebase.storage.StreamDownloadTask.TaskSnapshot,java.io.InputStream))`(` ` state: `[StreamDownloadTask.TaskSnapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot)`,` ` stream: `[InputStream](https://developer.android.com/reference/kotlin/java/io/InputStream.html) `)` doInBackground gets called on a background thread and should process the input stream to load data as desired. |

## Public functions

### doInBackground

```
funÂ doInBackground(
Â Â Â Â state:Â StreamDownloadTask.TaskSnapshot,
Â Â Â Â stream:Â InputStream
):Â Unit
```

doInBackground gets called on a background thread and should process the input stream to load data as desired. The stream should be closed prior to returning or in the handler [onSuccess](https://developers.google.com/android/reference/com/google/android/gms/tasks/OnSuccessListener.html#onSuccess-TResult-)  

|                                                                        Parameters                                                                         |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `state: `[StreamDownloadTask.TaskSnapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot) | is the current [TaskSnapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot) for this task |
| `stream: `[InputStream](https://developer.android.com/reference/kotlin/java/io/InputStream.html)                                                          | the [InputStream](https://developer.android.com/reference/kotlin/java/io/InputStream.html) for the downloaded bytes.                                       |

|                                                        Throws                                                         |
|-----------------------------------------------------------------------------------------------------------------------|----------------------------------------|
| `java.io.IOException: `[java.io.IOException](https://developer.android.com/reference/kotlin/java/io/IOException.html) | may be thrown to cancel the operation. |