# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StreamDownloadTask.StreamProcessor.md.txt

# StreamDownloadTask.StreamProcessor

# StreamDownloadTask.StreamProcessor


```
public interface StreamDownloadTask.StreamProcessor
```

<br />

*** ** * ** ***

A callback that is used to handle the stream download

## Summary

| ### Public methods |
|---|---|
| `abstract void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StreamDownloadTask.StreamProcessor#doInBackground(com.google.firebase.storage.StreamDownloadTask.TaskSnapshot,java.io.InputStream)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot state, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/io/InputStream.html stream )` doInBackground gets called on a background thread and should process the input stream to load data as desired. |

## Public methods

### doInBackground

```
abstract void doInBackground(
    @NonNull StreamDownloadTask.TaskSnapshot state,
    @NonNull InputStream stream
)
```

doInBackground gets called on a background thread and should process the input stream to load data as desired. The stream should be closed prior to returning or in the handler `https://developers.google.com/android/reference/com/google/android/gms/tasks/OnSuccessListener.html#onSuccess-TResult-`

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot state` | is the current `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot` for this task |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/io/InputStream.html stream` | the `https://developer.android.com/reference/kotlin/java/io/InputStream.html` for the downloaded bytes. |

| Throws |
|---|---|
| `https://developer.android.com/reference/kotlin/java/io/IOException.html java.io.IOException` | may be thrown to cancel the operation. |