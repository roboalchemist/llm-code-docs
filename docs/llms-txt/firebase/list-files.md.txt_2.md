# Source: https://firebase.google.com/docs/storage/web/list-files.md.txt

# List files with Cloud Storage on Web

<br />

Cloud Storage for Firebase allows you to list the contents of your
Cloud Storage bucket. The SDKs return both the items and the prefixes of
objects under the current Cloud Storage reference.

Projects that use the List API require Cloud Storage for Firebase
Rules Version 2. If you have an existing Firebase project, follow the steps in
the [Security Rules Guide](https://firebase.google.com/docs/storage/security/).

> [!NOTE]
> **Note:** The List API is only allowed for Rules version 2. In Rules version 2, `allow read` is the shorthand for `allow get, list`.

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

You can use `listAll` to fetch all results for a directory.
This is best used for small directories as all results are buffered in memory.
The operation also may not return a consistent snapshot if objects are added or
removed during the process.

For a large list, use the paginated `list()` method as `listAll()` buffers all
results in memory.

The following example demonstrates `listAll`.

### Web

```javascript
import { getStorage, ref, listAll } from "firebase/storage";

const storage = getStorage();

// Create a reference under which you want to list
const listRef = ref(storage, 'files/uid');

// Find all the prefixes and items.
listAll(listRef)
  .then((res) => {
    res.prefixes.forEach((folderRef) => {
      // All the prefixes under listRef.
      // You may call listAll() recursively on them.
    });
    res.items.forEach((itemRef) => {
      // All the items under listRef.
    });
  }).catch((error) => {
    // Uh-oh, an error occurred!
  });
```

### Web

```javascript
// Create a reference under which you want to list
var listRef = storageRef.child('files/uid');

// Find all the prefixes and items.
listRef.listAll()
  .then((res) => {
    res.prefixes.forEach((folderRef) => {
      // All the prefixes under listRef.
      // You may call listAll() recursively on them.
    });
    res.items.forEach((itemRef) => {
      // All the items under listRef.
    });
  }).catch((error) => {
    // Uh-oh, an error occurred!
  });
```

## Paginate list results

The `list()` API places a limit on the number of results it returns. `list()`
provides a consistent pageview and exposes a pageToken that allows control over
when to fetch additional results.

The pageToken encodes the path and version of the last item returned in the
previous result. In a subsequent request using the pageToken, items that come
after the pageToken are shown.

The following example demonstrates paginating a result using `async/await`.

### Web

```javascript
import { getStorage, ref, list } from "firebase/storage";

async function pageTokenExample(){
  // Create a reference under which you want to list
  const storage = getStorage();
  const listRef = ref(storage, 'files/uid');

  // Fetch the first page of 100.
  const firstPage = await list(listRef, { maxResults: 100 });

  // Use the result.
  // processItems(firstPage.items)
  // processPrefixes(firstPage.prefixes)

  // Fetch the second page if there are more elements.
  if (firstPage.nextPageToken) {
    const secondPage = await list(listRef, {
      maxResults: 100,
      pageToken: firstPage.nextPageToken,
    });
    // processItems(secondPage.items)
    // processPrefixes(secondPage.prefixes)
  }
}
```

### Web

```javascript
async function pageTokenExample(){
  // Create a reference under which you want to list
  var listRef = storageRef.child('files/uid');

  // Fetch the first page of 100.
  var firstPage = await listRef.list({ maxResults: 100});

  // Use the result.
  // processItems(firstPage.items)
  // processPrefixes(firstPage.prefixes)

  // Fetch the second page if there are more elements.
  if (firstPage.nextPageToken) {
    var secondPage = await listRef.list({
      maxResults: 100,
      pageToken: firstPage.nextPageToken,
    });
    // processItems(secondPage.items)
    // processPrefixes(secondPage.prefixes)
  }
}
```

## Handle errors

`list()` and `listAll()` return a rejected Promise if you haven't upgraded
the Security Rules to version 2. Upgrade your Security Rules if you see this
error:

    Listing objects in a bucket is disallowed for rules_version = "1".
    Please update storage security rules to rules_version = "2" to use list.

Other possible errors may indicate the user does not have the right permission.
More information on errors can be found in the
[Handle Errors](https://firebase.google.com/docs/storage/web/handle-errors).