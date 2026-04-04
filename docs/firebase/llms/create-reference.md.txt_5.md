# Source: https://firebase.google.com/docs/storage/ios/create-reference.md.txt

# Create a Cloud Storage reference on Apple platforms

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

Create a reference to upload, download, or delete a file,
or to get or update its metadata. A reference
can be thought of as a pointer to a file in the cloud. References are
lightweight, so you can create as many as you need. They are also reusable for
multiple operations.

References are created using the `FirebaseStorage` service and calling its
`reference` method.

### Swift

```swift
// Get a reference to the storage service using the default Firebase App
let storage = Storage.storage()

// Create a storage reference from our storage service
let storageRef = storage.reference()
    
```

### Objective-C

```objective-c
// Get a reference to the storage service using the default Firebase App
FIRStorage *storage = [FIRStorage storage];

// Create a storage reference from our storage service
FIRStorageReference *storageRef = [storage reference];
    
```

You can create a reference to a location lower in the tree,
say `'images/space.jpg'`, by using the `child` method on an existing reference.

### Swift

```swift
// Create a child reference
// imagesRef now points to "images"
let imagesRef = storageRef.child("images")

// Child references can also take paths delimited by '/'
// spaceRef now points to "images/space.jpg"
// imagesRef still points to "images"
var spaceRef = storageRef.child("images/space.jpg")

// This is equivalent to creating the full reference
let storagePath = "\(your_firebase_storage_bucket)/images/space.jpg"
spaceRef = storage.reference(forURL: storagePath)
    
```

### Objective-C

```objective-c
// Create a child reference
// imagesRef now points to "images"
FIRStorageReference *imagesRef = [storageRef child:@"images"];

// Child references can also take paths delimited by '/'
// spaceRef now points to "images/space.jpg"
// imagesRef still points to "images"
FIRStorageReference *spaceRef = [storageRef child:@"images/space.jpg"];

// This is equivalent to creating the full reference
spaceRef = [storage referenceForURL:@"gs://<your-firebase-storage-bucket>/images/space.jpg"];
     
```

## Navigate with References

You can also use the `parent` and `root` methods to navigate up in our
file hierarchy. `parent` navigates up one level,
while `root` navigates all the way to the top.

### Swift

```swift
// Parent allows us to move to the parent of a reference
// imagesRef now points to 'images'
let imagesRef = spaceRef.parent()

// Root allows us to move all the way back to the top of our bucket
// rootRef now points to the root
let rootRef = spaceRef.root()
    
```

### Objective-C

```objective-c
// Parent allows us to move to the parent of a reference
// imagesRef now points to 'images'
imagesRef = [spaceRef parent];

// Root allows us to move all the way back to the top of our bucket
// rootRef now points to the root
FIRStorageReference *rootRef = [spaceRef root];
    
```

`child`, `parent`, and `root` can be chained together multiple times, as
each returns a reference. The exception is the `parent` of `root`, which
is `nil`.

### Swift

```swift
// References can be chained together multiple times
// earthRef points to "images/earth.jpg"
let earthRef = spaceRef.parent()?.child("earth.jpg")

// nilRef is nil, since the parent of root is nil
let nilRef = spaceRef.root().parent()
    
```

### Objective-C

```objective-c
// References can be chained together multiple times
// earthRef points to "images/earth.jpg"
FIRStorageReference *earthRef = [[spaceRef parent] child:@"earth.jpg"];

// nilRef is nil, since the parent of root is nil
FIRStorageReference *nilRef = [[spaceRef root] parent];
    
```

## Reference Properties

You can inspect references to better understand the files they point to
using the `fullPath`, `name`, and `bucket` properties. These properties
get the file's full path, name, and bucket.

### Swift

```swift
// Reference's path is: "images/space.jpg"
// This is analogous to a file path on disk
spaceRef.fullPath

// Reference's name is the last segment of the full path: "space.jpg"
// This is analogous to the file name
spaceRef.name

// Reference's bucket is the name of the storage bucket where files are stored
spaceRef.bucket
    
```

### Objective-C

```objective-c
// Reference's path is: "images/space.jpg"
// This is analogous to a file path on disk
spaceRef.fullPath;

// Reference's name is the last segment of the full path: "space.jpg"
// This is analogous to the file name
spaceRef.name;

// Reference's bucket is the name of the storage bucket where files are stored
spaceRef.bucket;
    
```

## Limitations on References

Reference paths and names can contain any sequence of valid Unicode characters,
but certain restrictions are imposed including:

1. Total length of reference.fullPath must be between 1 and 1024 bytes when UTF-8 encoded.
2. No Carriage Return or Line Feed characters.
3. Avoid using `#`, `[`, `]`, `*`, or `?`, as these do not work well with other tools such as the [Firebase Realtime Database](https://firebase.google.com/docs/database) or [gsutil](https://cloud.google.com/storage/docs/gsutil).

## Full Example

### Swift

```swift
// Points to the root reference
let storageRef = Storage.storage().reference()

// Points to "images"
let imagesRef = storageRef.child("images")

// Points to "images/space.jpg"
// Note that you can use variables to create child values
let fileName = "space.jpg"
let spaceRef = imagesRef.child(fileName)

// File path is "images/space.jpg"
let path = spaceRef.fullPath

// File name is "space.jpg"
let name = spaceRef.name

// Points to "images"
let images = spaceRef.parent()
    
```

### Objective-C

```objective-c
// Points to the root reference
FIRStorageReference *storageRef = [[FIRStorage storage] reference];

// Points to "images"
FIRStorageReference *imagesRef = [storageRef child:@"images"];

// Points to "images/space.jpg"
// Note that you can use variables to create child values
NSString *fileName = @"space.jpg";
FIRStorageReference *spaceRef = [imagesRef child:fileName];

// File path is "images/space.jpg"
NSString *path = spaceRef.fullPath;

// File name is "space.jpg"
NSString *name = spaceRef.name;

// Points to "images"
imagesRef = [spaceRef parent];
    
```

Next, let's learn how to
[upload files](https://firebase.google.com/docs/storage/ios/upload-files) to
Cloud Storage.