# Source: https://firebase.google.com/docs/storage/ios/list-files.md.txt

# List files with Cloud Storage on Apple platforms

<br />

Cloud Storage for Firebase allows you to list the contents of your
Cloud Storage bucket. The SDKs return both the items and the prefixes
of objects under the current Cloud Storage reference.

Projects that use the list API require Cloud Storage for Firebase
Rules version 2. If you have an existing Firebase project, follow the steps in
the [Security Rules Guide](https://firebase.google.com/docs/storage/security/core-syntax).

> [!NOTE]
> **Note:** The list API is only allowed for Rules version 2. In Rules version 2, `allow read` is the shorthand for `allow get, list`.

`list()` uses the
[Google Cloud Storage List API](https://cloud.google.com/storage/docs/json_api/v1/objects/list).
In Cloud Storage for Firebase, we use `/` as a delimiter, which allows us to
emulate file system semantics. To allow for efficient traversal of large,
hierarchical Cloud Storage buckets, the List API returns prefixes and items
separately. For example, if you upload one file `/images/uid/file1`,

- `root.child('images').listAll()` will return `/images/uid` as a prefix.
- `root.child('images/uid').listAll()` will return the file as an item.

The Cloud Storage for Firebase SDK does not return object paths that contain two
consecutive `/`s or end with a `/.`. For example, consider a bucket that has the
following objects:

- `correctPrefix/happyItem`
- `wrongPrefix//sadItem`
- `lonelyItem/`

The list operations on items in this bucket will give the following results:

- The list operation at the root returns the references to `correctPrefix`, `wrongPrefix` and `lonelyItem` as `prefixes`.
- The list operation at the `correctPrefix/` returns the references to `correctPrefix/happyItem` as `items`.
- The list operation at the `wrongPrefix/` doesn't return any references because `wrongPrefix//sadItem` contains two consecutive `/`s.
- The list operation at the `lonelyItem/` doesn't return any references because the object `lonelyItem/` ends with `/`.

## List all files

You can use `listAll(completion:)` to fetch all results for a directory.
This is best used for small directories as all results are buffered in memory.
The operation also may not return a consistent snapshot if objects are added or
removed during the process.

For a large list, use the paginated `list(withMaxResults:completion:)` method as
`listAll(completion:)` buffers all results in memory.

The following example demonstrates `listAll(completion:)`.

### Swift

```swift
let storageReference = storage.reference().child("files/uid")
do {
  let result = try await storageReference.listAll()
  for prefix in result.prefixes {
    // The prefixes under storageReference.
    // You may call listAll(completion:) recursively on them.
  }
  for item in result.items {
    // The items under storageReference.
  }
} catch {
  // ...
}
```

### Objective-C

```objective-c
FIRStorageReference *storageReference = [storage reference];
[storageReference listAllWithCompletion:^(FIRStorageListResult *result, NSError *error) {
  if (error != nil) {
    // ...
  }

  for (FIRStorageReference *prefix in result.prefixes) {
    // All the prefixes under storageReference.
    // You may call listAllWithCompletion: recursively on them.
  }
  for (FIRStorageReference *item in result.items) {
    // All items under storageReference.
  }
}];
```

## Paginate list results

The `list(withMaxResults:completion:)` API places a limit on the number of
results it returns. `list(withMaxResults:completion)` provides a consistent
pageview and exposes a pageToken that allows control over when to fetch
additional results.

The pageToken encodes the path and version of the last item returned in the
previous result. In a subsequent request using the pageToken, items that come
after the pageToken are shown.

The following example demonstrates paginating a result:

### Swift

```swift
func listAllPaginated(pageToken: String? = nil) async throws {
  let storage = Storage.storage()
  let storageReference = storage.reference().child("files/uid")

  let listResult: StorageListResult
  if let pageToken = pageToken {
    listResult = try await storageReference.list(maxResults: 100, pageToken: pageToken)
  } else {
    listResult = try await storageReference.list(maxResults: 100)
  }
  let prefixes = listResult.prefixes
  let items = listResult.items
  // Handle list result
  // ...

  // Process next page
  if let token = listResult.pageToken {
    try await listAllPaginated(pageToken: token)
  }
}
```

### Objective-C

```objective-c
- (void)paginateFilesAtReference:(FIRStorageReference *)reference
                       pageToken:(nullable NSString *)pageToken {
  void (^pageHandler)(FIRStorageListResult *_Nonnull, NSError *_Nullable) =
      ^(FIRStorageListResult *result, NSError *error) {
        if (error != nil) {
          // ...
        }
        NSArray *prefixes = result.prefixes;
        NSArray *items = result.items;

        // ...

        // Process next page
        if (result.pageToken != nil) {
          [self paginateFilesAtReference:reference pageToken:result.pageToken];
        }
  };

  if (pageToken != nil) {
    [reference listWithMaxResults:100 pageToken:pageToken completion:pageHandler];
  } else {
    [reference listWithMaxResults:100 completion:pageHandler];
  }
}
```

## Handle errors

Methods in the list API will fail if you haven't upgraded your Security Rules to
version 2. Upgrade your Security Rules if you see this error:

    Listing objects in a bucket is disallowed for rules_version = "1".
    Please update storage security rules to rules_version = "2" to use list.

Other possible errors may indicate the user does not have the right permissions.
More information on errors can be found in
[Handle Errors](https://firebase.google.com/docs/storage/ios/handle-errors).