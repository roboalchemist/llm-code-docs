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

| ### Public functions |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask.StreamProcessor#doInBackground(com.google.firebase.storage.StreamDownloadTask.TaskSnapshot,java.io.InputStream)( state: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot, stream: https://developer.android.com/reference/kotlin/java/io/InputStream.html )` doInBackground gets called on a background thread and should process the input stream to load data as desired. |

## Public functions

### doInBackground

```
fun doInBackground(
    state: StreamDownloadTask.TaskSnapshot,
    stream: InputStream
): Unit
```

doInBackground gets called on a background thread and should process the input stream to load data as desired. The stream should be closed prior to returning or in the handler `https://developers.google.com/android/reference/com/google/android/gms/tasks/OnSuccessListener.html#onSuccess-TResult-`

| Parameters |
|---|---|
| `state: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot` | is the current `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot` for this task |
| `stream: https://developer.android.com/reference/kotlin/java/io/InputStream.html` | the `https://developer.android.com/reference/kotlin/java/io/InputStream.html` for the downloaded bytes. |

| Throws |
|---|---|
| `java.io.IOException: https://developer.android.com/reference/kotlin/java/io/IOException.html` | may be thrown to cancel the operation. |