# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/storage/package-summary.md.txt

# com.google.firebase.storage

# com.google.firebase.storage

## Annotations

|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageException.ErrorCode` | An `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageException.ErrorCode` indicates the source of a failed StorageTask or operation. |

## Interfaces

|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/OnPausedListener` | A listener that is called if the Task is paused via `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/ControllableTask#pause()`. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/OnProgressListener` | A listener that is called periodically during execution of the `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/ControllableTask`. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask.ProvideError` | An object that returns an exception. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StreamDownloadTask.StreamProcessor` | A callback that is used to handle the stream download |

## Classes

|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/CancellableTask` | Represents an asynchronous operation that can be canceled. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/ControllableTask` | Represents an asynchronous operation that can be paused, resumed and canceled. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FileDownloadTask` | A task that downloads bytes of a GCS blob to a specified File. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FileDownloadTask.TaskSnapshot` | Encapsulates state about the running `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FileDownloadTask` |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage` | FirebaseStorage is a service that supports uploading and downloading large objects to Google Cloud Storage. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/ListResult` | Contains the prefixes and items returned by a `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference#list(int)` call. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageKt` |   |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata` | Metadata for a `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference`. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata.Builder` | Creates a StorageMetadata object. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference` | Represents a reference to a Google Cloud Storage object. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask` | A controllable Task that has a synchronized state machine. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask.SnapshotBase` | Base class for state. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StreamDownloadTask` | A task that downloads bytes of a GCS blob. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot` | Encapsulates state about the running `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StreamDownloadTask` |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/TaskState` | Used to emit events about the progress of storage tasks. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/TaskState.InProgress` | Called periodically as data is transferred and can be used to populate an upload/download indicator. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/TaskState.Paused` | Called any time the upload/download is paused. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask` | An controllable task that uploads and fires events for success, progress and failure. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot` | Encapsulates state about the running `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask` |

## Exceptions

|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageException` | Represents an Exception resulting from an operation on a `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference`. |