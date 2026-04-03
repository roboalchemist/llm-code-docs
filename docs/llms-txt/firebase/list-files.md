# Source: https://firebase.google.com/docs/storage/web/list-files.md.txt

# Source: https://firebase.google.com/docs/storage/flutter/list-files.md.txt

# Source: https://firebase.google.com/docs/storage/ios/list-files.md.txt

# Source: https://firebase.google.com/docs/storage/android/list-files.md.txt

# Source: https://firebase.google.com/docs/storage/ios/list-files.md.txt

# Source: https://firebase.google.com/docs/storage/android/list-files.md.txt

<br />

Cloud Storage for Firebaseallows you to list the contents of yourCloud Storagebucket. The SDKs return both the items and the prefixes of objects under the currentCloud Storagereference.

Projects that use the List API requireCloud Storage for FirebaseRules version 2. If you have an existing Firebase project, follow the steps in the[Security Rules Guide](https://firebase.google.com/docs/storage/security/core-syntax).
| **Note:** The List API is only allowed for Rules version 2. In Rules version 2,`allow read`is the shorthand for`allow get, list`.

`list()`uses the[Google Cloud StorageList API](https://cloud.google.com/storage/docs/json_api/v1/objects/list). InCloud Storage for Firebase, we use`/`as a delimiter, which allows us to emulate file system semantics. To allow for efficient traversal of large, hierarchicalCloud Storagebuckets, the List API returns prefixes and items separately. For example, if you upload one file`/images/uid/file1`,

- `root.child('images').listAll()`will return`/images/uid`as a prefix.
- `root.child('images/uid').listAll()`will return the file as an item.

TheCloud Storage for FirebaseSDK does not return object paths that contain two consecutive`/`s or end with a`/`. For example, consider a bucket that has the following objects:

- `correctPrefix/happyItem`
- `wrongPrefix//sadItem`
- `lonelyItem/`

The list operations on items in this bucket will give the following results:

- The list operation at the root returns the references to`correctPrefix`,`wrongPrefix`and`lonelyItem`as`prefixes`.
- The list operation at the`correctPrefix/`returns the references to`correctPrefix/happyItem`as`items`.
- The list operation at the`wrongPrefix/`doesn't return any references because`wrongPrefix//sadItem`contains two consecutive`/`s.
- The list operation at the`lonelyItem/`doesn't return any references because the object`lonelyItem/`ends with`/`.

## List all files

You can use`listAll`to fetch all results for a directory. This is best used for small directories as all results are buffered in memory. The operation also may not return a consistent snapshot if objects are added or removed during the process.

For a large list, use the paginated`list()`method as`listAll()`buffers all results in memory.

The following example demonstrates`listAll`.  

### Kotlin

```kotlin
val storage = Firebase.storage
val listRef = storage.reference.child("files/uid")

// You'll need to import com.google.firebase.storage.component1 and
// com.google.firebase.storage.component2
listRef.listAll()
    .addOnSuccessListener { (items, prefixes) ->
        for (prefix in prefixes) {
            // All the prefixes under listRef.
            // You may call listAll() recursively on them.
        }

        for (item in items) {
            // All the items under listRef.
        }
    }
    .addOnFailureListener {
        // Uh-oh, an error occurred!
    }https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/storage/app/src/main/java/com/google/firebase/referencecode/storage/kotlin/StorageActivity.kt#L437-L455
```

### Java

```java
StorageReference listRef = storage.getReference().child("files/uid");

listRef.listAll()
        .addOnSuccessListener(new OnSuccessListener<ListResult>() {
            @Override
            public void onSuccess(ListResult listResult) {
                for (StorageReference prefix : listResult.getPrefixes()) {
                    // All the prefixes under listRef.
                    // You may call listAll() recursively on them.
                }

                for (StorageReference item : listResult.getItems()) {
                    // All the items under listRef.
                }
            }
        })
        .addOnFailureListener(new OnFailureListener() {
            @Override
            public void onFailure(@NonNull Exception e) {
                // Uh-oh, an error occurred!
            }
        });https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/storage/app/src/main/java/com/google/firebase/referencecode/storage/StorageActivity.java#L558-L579
```

## Paginate list results

The`list()`API places a limit on the number of results it returns.`list()`provides a consistent pageview and exposes a pageToken that allows control over when to fetch additional results.

The pageToken encodes the path and version of the last item returned in the previous result. In a subsequent request using the pageToken, items that come after the pageToken are shown.

The following example demonstrates paginating a result:  

### Kotlin

```kotlin
fun listAllPaginated(pageToken: String?) {
    val storage = Firebase.storage
    val listRef = storage.reference.child("files/uid")

    // Fetch the next page of results, using the pageToken if we have one.
    val listPageTask = if (pageToken != null) {
        listRef.list(100, pageToken)
    } else {
        listRef.list(100)
    }

    // You'll need to import com.google.firebase.storage.component1 and
    // com.google.firebase.storage.component2
    listPageTask
        .addOnSuccessListener { (items, prefixes, pageToken) ->
            // Process page of results
            processResults(items, prefixes)

            // Recurse onto next page
            pageToken?.let {
                listAllPaginated(it)
            }
        }.addOnFailureListener {
            // Uh-oh, an error occurred.
        }
}https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/storage/app/src/main/java/com/google/firebase/referencecode/storage/kotlin/StorageActivity.kt#L463-L488
```

### Java

```java
public void listAllPaginated(@Nullable String pageToken) {
    FirebaseStorage storage = FirebaseStorage.getInstance();
    StorageReference listRef = storage.getReference().child("files/uid");

    // Fetch the next page of results, using the pageToken if we have one.
    Task<ListResult> listPageTask = pageToken != null
            ? listRef.list(100, pageToken)
            : listRef.list(100);

    listPageTask
            .addOnSuccessListener(new OnSuccessListener<ListResult>() {
                @Override
                public void onSuccess(ListResult listResult) {
                    List<StorageReference> prefixes = listResult.getPrefixes();
                    List<StorageReference> items = listResult.getItems();

                    // Process page of results
                    // ...

                    // Recurse onto next page
                    if (listResult.getPageToken() != null) {
                        listAllPaginated(listResult.getPageToken());
                    }
                }
            }).addOnFailureListener(new OnFailureListener() {
                @Override
                public void onFailure(@NonNull Exception e) {
                    // Uh-oh, an error occurred.
                }
            });
}https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/storage/app/src/main/java/com/google/firebase/referencecode/storage/StorageActivity.java#L584-L614
```

## Handle errors

`list()`and`listAll()`fail if you haven't upgraded the Security Rules to version 2. Upgrade your Security Rules if you see this error:  

    Listing objects in a bucket is disallowed for rules_version = "1".
    Please update storage security rules to rules_version = "2" to use list.

Other possible errors may indicate the user does not have the right permission. More information on errors can be found in the[Handle Errors](https://firebase.google.com/docs/storage/android/handle-errors).