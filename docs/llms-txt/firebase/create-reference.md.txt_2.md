# Source: https://firebase.google.com/docs/storage/web/create-reference.md.txt

# Create a Cloud Storage reference on Web

<br />

Your files are stored in a
[Cloud Storage](https://cloud.google.com/storage) bucket. The
files in this bucket are presented in a hierarchical structure, just like the
file system on your local hard disk, or the data in the Firebase Realtime Database.
By creating a reference to a file, your app gains access to it. These references
can then be used to upload or download data, get or update metadata or delete
the file. A reference can either point to a specific file or to a higher level
node in the hierarchy.

If you've used the [Firebase Realtime Database](https://firebase.google.com/docs/database), these paths should
seem very familiar to you. However, your file data is stored in
Cloud Storage, **not** in the Realtime Database.

## Create a Reference

In order to upload or download files, delete files, or get or update metadata,
you must create a reference to the file you want to operate on. A reference
can be thought of as a pointer to a file in the cloud. References are
lightweight, so you can create as many as you need, and they are also reusable for
multiple operations.

To create a reference, get an instance of the Storage service using
`getStorage()` then call `ref()` with the service as an argument.
This reference points to the root of your Cloud Storage bucket.

### Web

```javascript
import { getStorage, ref } from "firebase/storage";

// Get a reference to the storage service, which is used to create references in your storage bucket
const storage = getStorage();

// Create a storage reference from our storage service
const storageRef = ref(storage);
```

### Web

```javascript
// Get a reference to the storage service, which is used to create references in your storage bucket
var storage = firebase.storage();

// Create a storage reference from our storage service
var storageRef = storage.ref();
```

You can create a reference to a location lower in the tree,
say `'images/space.jpg'` by passing in this path as a second argument when
calling `ref()`.

### Web

```javascript
import { getStorage, ref } from "firebase/storage";

const storage = getStorage();

// Create a child reference
const imagesRef = ref(storage, 'images');
// imagesRef now points to 'images'

// Child references can also take paths delimited by '/'
const spaceRef = ref(storage, 'images/space.jpg');
// spaceRef now points to "images/space.jpg"
// imagesRef still points to "images"https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/storage-next/create-reference/storage_create_ref_child.js#L8-L19
```

### Web

```javascript
// Create a child reference
var imagesRef = storageRef.child('images');
// imagesRef now points to 'images'

// Child references can also take paths delimited by '/'
var spaceRef = storageRef.child('images/space.jpg');
// spaceRef now points to "images/space.jpg"
// imagesRef still points to "images"https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/storage/create-reference.js#L18-L25
```

## Navigate with References

You can also use the `parent` and `root` properties to navigate up the
file hierarchy. `parent` navigates up one level,
while `root` navigates all the way to the top.

### Web

```javascript
import { getStorage, ref } from "firebase/storage";

const storage = getStorage();
const spaceRef = ref(storage, 'images/space.jpg');

// Parent allows us to move to the parent of a reference
const imagesRef = spaceRef.parent;
// imagesRef now points to 'images'

// Root allows us to move all the way back to the top of our bucket
const rootRef = spaceRef.root;
// rootRef now points to the roothttps://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/storage-next/create-reference/storage_navigate_ref.js#L8-L19
```

### Web

```javascript
// Parent allows us to move to the parent of a reference
var imagesRef = spaceRef.parent;
// imagesRef now points to 'images'

// Root allows us to move all the way back to the top of our bucket
var rootRef = spaceRef.root;
// rootRef now points to the roothttps://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/storage/create-reference.js#L33-L39
```

`child()`, `parent`, and `root` can be chained together multiple times, as
each returns a reference. The exception is the `parent` of `root`, which
is `null`.

### Web

```javascript
import { getStorage, ref } from "firebase/storage";

const storage = getStorage();
const spaceRef = ref(storage, 'images/space.jpg');

// References can be chained together multiple times
const earthRef = ref(spaceRef.parent, 'earth.jpg');
// earthRef points to 'images/earth.jpg'

// nullRef is null, since the parent of root is null
const nullRef = spaceRef.root.parent;
```

### Web

```javascript
// References can be chained together multiple times
var earthRef = spaceRef.parent.child('earth.jpg');
// earthRef points to 'images/earth.jpg'

// nullRef is null, since the parent of root is null
var nullRef = spaceRef.root.parent;
```

## Reference Properties

You can inspect references to better understand the files they point to
using the `fullPath`, `name`, and `bucket` properties. These properties
get the full path of the file, the name of the file,
and the bucket the file is stored in.

### Web

```javascript
import { getStorage, ref } from "firebase/storage";

const storage = getStorage();
const spaceRef = ref(storage, 'images/space.jpg');

// Reference's path is: 'images/space.jpg'
// This is analogous to a file path on disk
spaceRef.fullPath;

// Reference's name is the last segment of the full path: 'space.jpg'
// This is analogous to the file name
spaceRef.name;

// Reference's bucket is the name of the storage bucket where files are stored
spaceRef.bucket;
```

### Web

```javascript
// Reference's path is: 'images/space.jpg'
// This is analogous to a file path on disk
spaceRef.fullPath;

// Reference's name is the last segment of the full path: 'space.jpg'
// This is analogous to the file name
spaceRef.name;

// Reference's bucket is the name of the storage bucket where files are stored
spaceRef.bucket;
```

## Limitations on References

Reference paths and names can contain any sequence of valid Unicode characters,
but certain restrictions are imposed including:

1. Total length of `reference.fullPath` must be between 1 and 1024 bytes when UTF-8 encoded.
2. No Carriage Return or Line Feed characters.
3. Avoid using `#`, `[`, `]`, `*`, or `?`, as these do not work well with other tools such as the [Firebase Realtime Database](https://firebase.google.com/docs/database) or [gsutil](https://cloud.google.com/storage/docs/gsutil).

## Full Example

### Web

```javascript
import { getStorage, ref } from "firebase/storage";

const storage = getStorage();

// Points to the root reference
const storageRef = ref(storage);

// Points to 'images'
const imagesRef = ref(storageRef, 'images');

// Points to 'images/space.jpg'
// Note that you can use variables to create child values
const fileName = 'space.jpg';
const spaceRef = ref(imagesRef, fileName);

// File path is 'images/space.jpg'
const path = spaceRef.fullPath;

// File name is 'space.jpg'
const name = spaceRef.name;

// Points to 'images'
const imagesRefAgain = spaceRef.parent;
```

### Web

```javascript
// Points to the root reference
var storageRef = firebase.storage().ref();

// Points to 'images'
var imagesRef = storageRef.child('images');

// Points to 'images/space.jpg'
// Note that you can use variables to create child values
var fileName = 'space.jpg';
var spaceRef = imagesRef.child(fileName);

// File path is 'images/space.jpg'
var path = spaceRef.fullPath;

// File name is 'space.jpg'
var name = spaceRef.name;

// Points to 'images'
var imagesRef = spaceRef.parent;
```

Next, let's learn how to
[upload files](https://firebase.google.com/docs/storage/web/upload-files) to
Cloud Storage.