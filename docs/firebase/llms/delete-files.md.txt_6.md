# Source: https://firebase.google.com/docs/storage/unity/delete-files.md.txt

<br />

After uploading files to Cloud Storage, you can also delete them.

> [!NOTE]
> **Note:** By default, a Cloud Storage for Firebase bucket requires Firebase Authentication to perform any action on the bucket's data or files. You can change your Firebase Security Rules for Cloud Storage to [allow unauthenticated access for specific situations](https://firebase.google.com/docs/storage/security/rules-conditions#public). However, for most situations, we strongly recommend [restricting access and setting up robust security rules](https://firebase.google.com/docs/storage/security/get-started) (especially for production apps). Note that if you use Google App Engine and have a default Cloud Storage bucket with a name format of `*.appspot.com`, you may need to consider [how your security rules impact access to App Engine files](https://firebase.google.com/docs/storage/gcp-integration#security-rules-and-app-engine-files).

## Delete a File

To delete a file, first
[create a reference](https://firebase.google.com/docs/storage/unity/create-reference)
to that file. Then call the `DeleteAsync()` method on that reference.

```c#
// Create a reference to the file to delete.
StorageReference desertRef = storageRef.Child("images/desert.jpg");

// Delete the file
desertRef.DeleteAsync().ContinueWithOnMainThread(task => {
    if (task.IsCompleted) {
        Debug.Log("File deleted successfully.");
    }
    else {
        // Uh-oh, an error occurred!
    }
});
```

> [!NOTE]
> **Note:** Deleted files are typically recoverable for 7 days with [soft delete](https://cloud.google.com/storage/docs/soft-delete), which is enabled by default.

## Handle Errors

There are a number of reasons why errors may occur on file deletes,
including the file not existing, or the user not having permission
to delete the specified file. More information on errors can be found in the
[Handle Errors](https://firebase.google.com/docs/storage/unity/handle-errors)
section of the docs.