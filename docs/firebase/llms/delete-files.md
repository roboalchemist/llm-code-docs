# Source: https://firebase.google.com/docs/storage/web/delete-files.md.txt

# Source: https://firebase.google.com/docs/storage/ios/delete-files.md.txt

# Source: https://firebase.google.com/docs/storage/flutter/delete-files.md.txt

# Source: https://firebase.google.com/docs/storage/cpp/delete-files.md.txt

# Source: https://firebase.google.com/docs/storage/unity/delete-files.md.txt

# Source: https://firebase.google.com/docs/storage/android/delete-files.md.txt

# Source: https://firebase.google.com/docs/storage/unity/delete-files.md.txt

# Source: https://firebase.google.com/docs/storage/android/delete-files.md.txt

<br />

After uploading files toCloud Storage, you can also delete them.
| **Note:** By default, aCloud Storage for Firebasebucket requiresFirebase Authenticationto perform any action on the bucket's data or files. You can change yourFirebase Security RulesforCloud Storageto[allow unauthenticated access for specific situations](https://firebase.google.com/docs/storage/security/rules-conditions#public). However, for most situations, we strongly recommend[restricting access and setting up robust security rules](https://firebase.google.com/docs/storage/security/get-started)(especially for production apps). Note that if you useGoogleApp Engineand have a defaultCloud Storagebucket with a name format of`*.appspot.com`, you may need to consider[how your security rules impact access toApp Enginefiles](https://firebase.google.com/docs/storage/gcp-integration#security-rules-and-app-engine-files).

## Delete a File

To delete a file, first[create a reference](https://firebase.google.com/docs/storage/android/create-reference)to that file. Then call the`delete()`method on that reference.  

### Kotlin

```kotlin
// Create a storage reference from our app
val storageRef = storage.reference

// Create a reference to the file to delete
val desertRef = storageRef.child("images/desert.jpg")

// Delete the file
desertRef.delete().addOnSuccessListener {
    // File deleted successfully
}.addOnFailureListener {
    // Uh-oh, an error occurred!
}https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/storage/app/src/main/java/com/google/firebase/referencecode/storage/kotlin/StorageActivity.kt#L401-L412
```

### Java

```java
// Create a storage reference from our app
StorageReference storageRef = storage.getReference();

// Create a reference to the file to delete
StorageReference desertRef = storageRef.child("images/desert.jpg");

// Delete the file
desertRef.delete().addOnSuccessListener(new OnSuccessListener<Void>() {
    @Override
    public void onSuccess(Void aVoid) {
        // File deleted successfully
    }
}).addOnFailureListener(new OnFailureListener() {
    @Override
    public void onFailure(@NonNull Exception exception) {
        // Uh-oh, an error occurred!
    }
});https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/storage/app/src/main/java/com/google/firebase/referencecode/storage/StorageActivity.java#L515-L532
```
| **Note:** Deleted files are typically recoverable for 7 days with[soft delete](https://cloud.google.com/storage/docs/soft-delete), which is enabled by default.

## Handle Errors

There are a number of reasons why errors may occur on file deletes, including the file not existing, or the user not having permission to delete the specified file. More information on errors can be found in the[Handle Errors](https://firebase.google.com/docs/storage/android/handle-errors)section of the docs.