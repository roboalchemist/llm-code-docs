# Source: https://firebase.google.com/docs/storage/ios/handle-errors.md.txt

# Handle errors for Cloud Storage on Apple platforms

<br />

> [!CAUTION]
> **If you have an `*.appspot.com` default bucket,** your Firebase project must be upgraded to the [pay-as-you-go Blaze pricing plan](https://firebase.google.com/pricing) by **February 03, 2026** to maintain access to your default bucket. [Learn more.](https://firebase.google.com/docs/storage/faqs-storage-changes-announced-sept-2024)

Sometimes when you're building an app, things don't go as planned and an
error occurs.

When in doubt, check the error returned, and see what the error message says.

> [!NOTE]
> **Note:** By default, a Cloud Storage for Firebase bucket requires Firebase Authentication to perform any action on the bucket's data or files. You can change your Firebase Security Rules for Cloud Storage to [allow unauthenticated access for specific situations](https://firebase.google.com/docs/storage/security/rules-conditions#public). However, for most situations, we strongly recommend [restricting access and setting up robust security rules](https://firebase.google.com/docs/storage/security/get-started) (especially for production apps). Note that if you use Google App Engine and have a default Cloud Storage bucket with a name format of `*.appspot.com`, you may need to consider [how your security rules impact access to App Engine files](https://firebase.google.com/docs/storage/gcp-integration#security-rules-and-app-engine-files).

If you've checked the error message and have Cloud Storage Security Rules that allow your
action, but are still struggling to fix the error, visit our
[Support page](https://firebase.google.com/support) and let us know how we can help.

## Handle Error Messages

There are a number of reasons why errors may occur, including the file
not existing, the user not having permission to access the desired file, or the
user cancelling the file upload.

To properly diagnose the issue and handle the error, here is a full list of
all the errors our client will raise, and how they can occur.

| Name | Reason |
|---|---|
| `FIRStorageErrorCodeUnknown` | An unknown error occurred. |
| `FIRStorageErrorCodeObjectNotFound` | No object exists at the specified reference. |
| `FIRStorageErrorCodeBucketNotFound` | No bucket is configured for Cloud Storage. |
| `FIRStorageErrorCodeProjectNotFound` | No project is configured for Cloud Storage. |
| `FIRStorageErrorCodeQuotaExceeded` | Quota on your Cloud Storage bucket has been exceeded. If you're on the Spark pricing plan, consider upgrading to the [pay-as-you-go Blaze pricing plan](https://firebase.google.com/pricing). If you're already on the Blaze pricing plan, reach out to Firebase Support. **Important** : Starting February 03, 2026, the [Blaze pricing plan will be *required* to use Cloud Storage](https://firebase.google.com/docs/storage/faqs-storage-changes-announced-sept-2024), even default buckets. |
| `FIRStorageErrorCodeUnauthenticated` | User is unauthenticated. Authenticate and try again. |
| `FIRStorageErrorCodeUnauthorized` | User is not authorized to perform the requested action. Check your rules to ensure they are correct. |
| `FIRStorageErrorCodeRetryLimitExceeded` | The maximum time limit on an operation (upload, download, delete, etc.) has been exceeded. Try uploading again. |
| `FIRStorageErrorCodeNonMatchingChecksum` | File on the client does not match the checksum of the file received by the server. Try uploading again. |
| `FIRStorageErrorCodeCanceled` | User canceled the operation. |
| `FIRStorageErrorCodeDownloadSizeExceeded` | Size of the downloaded file exceeds the amount of memory allocated for the download. Increase memory cap and try downloading again. |