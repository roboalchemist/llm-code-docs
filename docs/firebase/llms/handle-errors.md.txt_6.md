# Source: https://firebase.google.com/docs/storage/web/handle-errors.md.txt

# Handle errors for Cloud Storage on Web

<br />

> [!CAUTION]
> **If you have an `*.appspot.com` default bucket,** your Firebase project must be upgraded to the [pay-as-you-go Blaze pricing plan](https://firebase.google.com/pricing) by **February 03, 2026** to maintain access to your default bucket. [Learn more.](https://firebase.google.com/docs/storage/faqs-storage-changes-announced-sept-2024)

Sometimes when you're building an app, things don't go as planned and an
error occurs!

When in doubt, check the error handler (or `catch()` function for Promises),
and see what the error message has to say.

> [!NOTE]
> **Note:** By default, a Cloud Storage for Firebase bucket requires Firebase Authentication to perform any action on the bucket's data or files. You can change your Firebase Security Rules for Cloud Storage to [allow unauthenticated access for specific situations](https://firebase.google.com/docs/storage/security/rules-conditions#public). However, for most situations, we strongly recommend [restricting access and setting up robust security rules](https://firebase.google.com/docs/storage/security/get-started) (especially for production apps). Note that if you use Google App Engine and have a default Cloud Storage bucket with a name format of `*.appspot.com`, you may need to consider [how your security rules impact access to App Engine files](https://firebase.google.com/docs/storage/gcp-integration#security-rules-and-app-engine-files).

If you've checked the error message and have Cloud Storage Security Rules that allow your
action, but are still struggling to solve the error, visit our
[Support page](https://firebase.google.com/support) and let us know how we can help.

## Handle Error Messages

There are a number of reasons why errors may occur, including the file
not existing, the user not having permission to access the desired file, or the
user cancelling the file upload.

To properly diagnose the issue and handle the error, here is a full list of
all the errors our client will raise, and how they occurred.

| Code | Reason |
|---|---|
| `storage/unknown` | An unknown error occurred. |
| `storage/object-not-found` | No object exists at the specified reference. |
| `storage/bucket-not-found` | No bucket is configured for Cloud Storage |
| `storage/project-not-found` | No project is configured for Cloud Storage |
| `storage/quota-exceeded` | Quota on your Cloud Storage bucket has been exceeded. If you're on the Spark pricing plan, consider upgrading to the [pay-as-you-go Blaze pricing plan](https://firebase.google.com/pricing). If you're already on the Blaze pricing plan, reach out to Firebase Support. **Important** : Starting February 03, 2026, the [Blaze pricing plan will be *required* to use Cloud Storage](https://firebase.google.com/docs/storage/faqs-storage-changes-announced-sept-2024), even default buckets. |
| `storage/unauthenticated` | User is unauthenticated, please authenticate and try again. |
| `storage/unauthorized` | User is not authorized to perform the requested action, check your security rules to ensure they are correct. |
| `storage/retry-limit-exceeded` | The maximum time limit on an operation (upload, download, delete, etc.) has been exceeded. Try uploading again. |
| `storage/invalid-checksum` | File on the client does not match the checksum of the file received by the server. Try uploading again. |
| `storage/canceled` | User canceled the operation. |
| `storage/invalid-event-name` | Invalid event name provided. Must be one of \[`` `running` ``, `` `progress` ``, `` `pause` ``\] |
| `storage/invalid-url` | Invalid URL provided to `refFromURL()`. Must be of the form: gs://bucket/object or https://firebasestorage.googleapis.com/v0/b/bucket/o/object?token=\&ltTOKEN\> |
| `storage/invalid-argument` | The argument passed to `put()` must be \`File\`, \`Blob\`, or \`UInt8\` Array. The argument passed to `putString()` must be a raw, \`Base64\`, or \`Base64URL\` string. |
| `storage/no-default-bucket` | No bucket has been set in your Firebase config's `storageBucket` property. |
| `storage/cannot-slice-blob` | Commonly occurs when the local file has changed (deleted, saved again, etc.). Try uploading again after verifying that the file hasn't changed. |
| `storage/server-file-wrong-size` | File on the client does not match the size of the file received by the server. Try uploading again. |