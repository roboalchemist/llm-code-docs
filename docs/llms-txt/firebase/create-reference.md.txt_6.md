# Source: https://firebase.google.com/docs/storage/unity/create-reference.md.txt

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

References are created from the `Firebase.Storage.FirebaseStorage` service on
your Firebase app by calling the `GetReferenceFromUrl()` method and passing in a
URL of the form `gs://<your-cloud-storage-bucket>`. You can find this URL in
the *Storage section* of the [Firebase console](https://console.firebase.google.com/).

```c#
// Get a reference to the storage service, using the default Firebase App
FirebaseStorage storage = FirebaseStorage.DefaultInstance;

// Create a storage reference from our storage service
StorageReference storageRef =
    storage.GetReferenceFromUrl("gs://<your-cloud-storage-bucket>");
```

You can create a reference to a location lower in the tree, for example
`'images/space.jpg'`, by using the `child` method on an existing reference.

```c#
// Create a child reference
// imagesRef now points to "images"
StorageReference imagesRef = storageRef.Child("images");

// Child references can also take paths delimited by '/' such as:
// "images/space.jpg".
StorageReference spaceRef = imagesRef.Child("space.jpg");
// spaceRef now points to "images/space.jpg"
// imagesRef still points to "images"

// This is equivalent to creating the full referenced
StorageReference spaceRefFull = storage.GetReferenceFromUrl(
    "gs://<your-cloud-storage-bucket>/images/space.jpg");
```

## Navigate with References

You can also use the `Parent` and `Root` methods to navigate up in our file
hierarchy. `Parent` navigates up one level, while `Root` navigates all the way
to the top.

```c#
// Parent allows us to move to the parent of a reference
// imagesRef now points to 'images'
StorageReference imagesRef = spaceRef.Parent;

// Root allows us to move all the way back to the top of our bucket
// rootRef now points to the root
StorageReference rootRef = spaceRef.Root;
```

`Child`, `Parent`, and `Root` can be chained together multiple times, as
each returns a reference. The exception is the `Parent` of `Root`, which
is an invalid `StorageReference`.

```c#
// References can be chained together multiple times
// earthRef points to "images/earth.jpg"
StorageReference earthRef =
    spaceRef.Parent.Child("earth.jpg");

// nullRef is null since the parent of root is an invalid StorageReference
StorageReference nullRef = spaceRef.Root.Parent;
```

## Reference Methods

You can inspect references to better understand the files they point to using
the `Path`, `Name`, and `Bucket` properties. These properties get the file's
full path, name, and bucket.

```c#
// Reference's path is: "images/space.jpg"
// This is analogous to a file path on disk
string path = spaceRef.Path;

// Reference's name is the last segment of the full path: "space.jpg"
// This is analogous to the file name
string name = spaceRef.Name;

// Reference's bucket is the name of the storage bucket where files are stored
string bucket = spaceRef.Bucket;
```

## Limitations on References

Reference paths and names can contain any sequence of valid Unicode characters,
but certain restrictions are imposed including:

1. Total length of `reference.Path` must be between 1 and 1024 bytes when UTF-8 encoded.
2. No Carriage Return or Line Feed characters.
3. Avoid using `#`, `[`, `]`, `*`, or `?`, as these do not work well with other tools such as the [Firebase Realtime Database](https://firebase.google.com/docs/database) or [gsutil](https://cloud.google.com/storage/docs/gsutil).

## Full Example

```c#
FirebaseStorage storage = FirebaseStorage.DefaultInstance;

// Points to the root reference
StorageReference storageRef =
    storage.GetReferenceFromUrl("gs://<your-bucket-name>");

// Points to "images"
StorageReference imagesRef = storageRef.Child("images");

// Points to "images/space.jpg"
// Note that you can use variables to create child values
string filename = "space.jpg";
StorageReference spaceRef = imagesRef.Child(filename);

// File path is "images/space.jpg"
string path = spaceRef.Path;

// File name is "space.jpg"
string name = spaceRef.Name;

// Points to "images"
StorageReference imagesRef = spaceRef.Parent;
```

## Next Steps

Next, let's learn how to
[upload files](https://firebase.google.com/docs/storage/unity/upload-files) to
Cloud Storage.