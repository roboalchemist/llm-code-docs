# Source: https://firebase.google.com/docs/storage/android/handle-errors.md.txt

# Handle errors for Cloud Storage on Android

<br />

> [!CAUTION]
> **If you have an `*.appspot.com` default bucket,** your Firebase project must be upgraded to the [pay-as-you-go Blaze pricing plan](https://firebase.google.com/pricing) by **February 03, 2026** to maintain access to your default bucket. [Learn more.](https://firebase.google.com/docs/storage/faqs-storage-changes-announced-sept-2024)

Sometimes things don't go as planned and an error occurs.

When in doubt, check the error returned and see what the error message says.
The following code shows a custom error handler implementation that inspects
the error code and error message returned by Cloud Storage. Such error
handlers can be added to various objects used in the Cloud Storage API (for
example, `UploadTask` and `FileDownloadTask`).

### Kotlin

```kotlin
internal inner class MyFailureListener : OnFailureListener {
    override fun onFailure(exception: Exception) {
        val errorCode = (exception as StorageException).errorCode
        val errorMessage = exception.message
        // test the errorCode and errorMessage, and handle accordingly
    }
}
```

### Java

```java
class MyFailureListener implements OnFailureListener {
    @Override
    public void onFailure(@NonNull Exception exception) {
        int errorCode = ((StorageException) exception).getErrorCode();
        String errorMessage = exception.getMessage();
        // test the errorCode and errorMessage, and handle accordingly
    }
}
```

If you've checked the error message and have Cloud Storage Security Rules that allow your
action, but are still struggling to fix the error, visit our
[Support page](https://firebase.google.com/support) and let us know how we can help.

## Handle Error Messages

There are a number of reasons why errors may occur, including the file
not existing, the user not having permission to access the desired file, or the
user cancelling the file upload.

To properly diagnose the issue and handle the error, here is a full list of all
the errors our client will raise, and how they can occur. Error codes in this
table are defined in the `StorageException` class as integer constants.

| Code | Reason |
|---|---|
| `ERROR_UNKNOWN` | An unknown error occurred. |
| `ERROR_OBJECT_NOT_FOUND` | No object exists at the specified reference. |
| `ERROR_BUCKET_NOT_FOUND` | No bucket is configured for Cloud Storage |
| `ERROR_PROJECT_NOT_FOUND` | No project is configured for Cloud Storage |
| `ERROR_QUOTA_EXCEEDED` | Quota on your Cloud Storage bucket has been exceeded. If you're on the Spark pricing plan, consider upgrading to the [pay-as-you-go Blaze pricing plan](https://firebase.google.com/pricing). If you're already on the Blaze pricing plan, reach out to Firebase Support. **Important** : Starting February 03, 2026, the [Blaze pricing plan will be *required* to use Cloud Storage](https://firebase.google.com/docs/storage/faqs-storage-changes-announced-sept-2024), even default buckets. |
| `ERROR_NOT_AUTHENTICATED` | User is unauthenticated, please authenticate and try again. |
| `ERROR_NOT_AUTHORIZED` | User is not authorized to perform the requested action, check your rules to ensure they are correct. |
| `ERROR_RETRY_LIMIT_EXCEEDED` | The maximum time limit on an operation (upload, download, delete, etc.) has been excceded. Try again. |
| `ERROR_INVALID_CHECKSUM` | File on the client does not match the checksum of the file received by the server. Try uploading again. |
| `ERROR_CANCELED` | User canceled the operation. |

Additionally, attempting to call `getReferenceFromUrl()` with an invalid URL
will result in an `IllegalArgumentException` from being thrown. The argument to
the above method must be of the form `gs://bucket/object` or
`https://firebasestorage.googleapis.com/v0/b/bucket/o/object?token=<TOKEN>`