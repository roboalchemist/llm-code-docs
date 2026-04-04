# Source: https://firebase.google.com/docs/storage/web/create-reference.md.txt

# Source: https://firebase.google.com/docs/storage/android/create-reference.md.txt

# Source: https://firebase.google.com/docs/storage/unity/create-reference.md.txt

# Source: https://firebase.google.com/docs/storage/ios/create-reference.md.txt

# Source: https://firebase.google.com/docs/storage/flutter/create-reference.md.txt

# Source: https://firebase.google.com/docs/storage/cpp/create-reference.md.txt

# Source: https://firebase.google.com/docs/storage/unity/create-reference.md.txt

# Source: https://firebase.google.com/docs/storage/ios/create-reference.md.txt

# Source: https://firebase.google.com/docs/storage/flutter/create-reference.md.txt

# Source: https://firebase.google.com/docs/storage/cpp/create-reference.md.txt

<br />

Your files are stored in a[Cloud Storage](https://cloud.google.com/storage)bucket. The files in this bucket are presented in a hierarchical structure, just like the file system on your local hard disk, or the data in theFirebase Realtime Database. By creating a reference to a file, your app gains access to it. These references can then be used to upload or download data, get or update metadata or delete the file. A reference can either point to a specific file or to a higher level node in the hierarchy.

If you've used the[Firebase Realtime Database](https://firebase.google.com/docs/database), these paths should seem very familiar to you. However, your file data is stored inCloud Storage,**not** in theRealtime Database.

## Create a Reference

Create a reference to upload, download, or delete a file, or to get or update its metadata. A reference can be thought of as a pointer to a file in the cloud. References are lightweight, so you can create as many as you need. They are also reusable for multiple operations.

References are created from the`storage`service on your Firebase app by calling the`GetReferenceFromUrl()`method and passing in a URL of the form`gs://<your-cloud-storage-bucket>`. You can find this URL in the*Storage* section of the[Firebaseconsole](https://console.firebase.google.com/).  

```c++
// Get a reference to the storage service, using the default Firebase App
Storage* storage = Storage::GetInstance(app);

// Create a Cloud Storage reference from our storage service
StorageReference storage_ref = storage->GetReferenceFromUrl("gs://<your-cloud-storage-bucket>");
```

You can create a reference to a location lower in the tree, say`'images/space.jpg'`, by using the`child`method on an existing reference.  

```c++
// Create a child reference
// images_ref now points to "images"
StorageReference images_ref = storage_ref.Child("images");

// Child references can also take paths delimited by '/'
// space_ref now points to "images/space.jpg"
// images_ref still points to "images"
StorageReference space_ref = storage_ref.Child("images/space.jpg");

// This is equivalent to creating the full reference
StorageReference space_ref = storage.GetReferenceFromUrl("gs://<your-cloud-storage-bucket>/images/space.jpg");
```

## Navigate with References

You can also use the`Parent`and`Root`methods to navigate up in our file hierarchy.`Parent`navigates up one level, while`Root`navigates all the way to the top.  

```c++
// Parent allows us to move to the parent of a reference
// images_ref now points to 'images'
StorageReference images_ref = space_ref.Parent();

// Root allows us to move all the way back to the top of our bucket
// root_ref now points to the root
StorageReference root_ref = space_ref.Root();
```

`Child`,`Parent`, and`Root`can be chained together multiple times, as each returns a reference. The exception is the`Parent`of`Root`, which is an invalid`StorageReference`.  

```c++
// References can be chained together multiple times
// earth_ref points to "images/earth.jpg"
StorageReference earth_ref = space_ref.Parent().Child("earth.jpg");

// null_ref is null, since the parent of root is an invalid StorageReference
StorageReference null_ref = space_ref.Root().Parent();
```

## Reference Methods

You can inspect references to better understand the files they point to using the`full_path`,`name`, and`bucket`methods. These methods get the file's full path, name, and bucket.  

```c++
// Reference's path is: "images/space.jpg"
// This is analogous to a file path on disk
space_ref.full_path();

// Reference's name is the last segment of the full path: "space.jpg"
// This is analogous to the file name
space_ref.name();

// Reference's bucket is the name of the Cloud Storage bucket where files are stored
space_ref.bucket();
```

## Limitations on References

Reference paths and names can contain any sequence of valid Unicode characters, but certain restrictions are imposed including:

1. Total length of reference.fullPath must be between 1 and 1024 bytes when UTF-8 encoded.
2. No Carriage Return or Line Feed characters.
3. Avoid using`#`,`[`,`]`,`*`, or`?`, as these do not work well with other tools such as the[Firebase Realtime Database](https://firebase.google.com/docs/database)or[gsutil](https://cloud.google.com/storage/docs/gsutil).

## Full Example

```c++
Storage* storage = Storage::GetInstance(app);

// Points to the root reference
StorageReference storage_ref = storage->GetReferenceFromUrl("gs://<your-bucket-name>");

// Points to "images"
StorageReference images_ref = storage_ref.Child("images");

// Points to "images/space.jpg"
// Note that you can use variables to create child values
std::string filename = "space.jpg";
StorageReference space_ref = images_ref.Child(filename);

// File path is "images/space.jpg"
std::string path = space_ref.full_path()

// File name is "space.jpg"
std::string name = space_ref.name()

// Points to "images"
StorageReference images_ref = space_ref.Parent();
```

## Next Steps

Next, let's learn how to[upload files](https://firebase.google.com/docs/storage/cpp/upload-files)toCloud Storage.