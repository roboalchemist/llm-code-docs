# Source: https://firebase.google.com/docs/storage/android/create-reference.md.txt

# Create a Cloud Storage reference on Android

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

Create a reference using the `FirebaseStorage` singleton instance and
calling its `getReference()` method.

### Kotlin

```kotlin
// Create a storage reference from our app
var storageRef = storage.referencehttps://github.com/firebase/snippets-android/blob/a413b0658ff2fc7a72c4b0c59e84a889ff7fac45/storage/app/src/main/java/com/google/firebase/referencecode/storage/kotlin/StorageActivity.kt#L49-L50
```

### Java

```java
// Create a storage reference from our app
StorageReference storageRef = storage.getReference();
```

Next, you can create a reference to a location lower in the tree,
say `"images/space.jpg"` by using the `child()` method on an existing reference.

### Kotlin

```kotlin
// Create a child reference
// imagesRef now points to "images"
var imagesRef: StorageReference? = storageRef.child("images")

// Child references can also take paths
// spaceRef now points to "images/space.jpg
// imagesRef still points to "images"
var spaceRef = storageRef.child("images/space.jpg")
```

### Java

```java
// Create a child reference
// imagesRef now points to "images"
StorageReference imagesRef = storageRef.child("images");

// Child references can also take paths
// spaceRef now points to "images/space.jpg
// imagesRef still points to "images"
StorageReference spaceRef = storageRef.child("images/space.jpg");
```

## Navigate with References

You can also use the `getParent()` and `getRoot()` methods to navigate up in our
file hierarchy. `getParent()` navigates up one level,
while `getRoot()` navigates all the way to the top.

### Kotlin

```kotlin
// parent allows us to move our reference to a parent node
// imagesRef now points to 'images'
imagesRef = spaceRef.parent

// root allows us to move all the way back to the top of our bucket
// rootRef now points to the root
val rootRef = spaceRef.roothttps://github.com/firebase/snippets-android/blob/a413b0658ff2fc7a72c4b0c59e84a889ff7fac45/storage/app/src/main/java/com/google/firebase/referencecode/storage/kotlin/StorageActivity.kt#L67-L73
```

### Java

```java
// getParent allows us to move our reference to a parent node
// imagesRef now points to 'images'
imagesRef = spaceRef.getParent();

// getRoot allows us to move all the way back to the top of our bucket
// rootRef now points to the root
StorageReference rootRef = spaceRef.getRoot();
```

`child()`, `getParent()`, and `getRoot()` can be chained together multiple
times, as each returns a reference. But calling `getRoot().getParent()` returns `null`.

### Kotlin

```kotlin
// References can be chained together multiple times
// earthRef points to 'images/earth.jpg'
val earthRef = spaceRef.parent?.child("earth.jpg")

// nullRef is null, since the parent of root is null
val nullRef = spaceRef.root.parenthttps://github.com/firebase/snippets-android/blob/a413b0658ff2fc7a72c4b0c59e84a889ff7fac45/storage/app/src/main/java/com/google/firebase/referencecode/storage/kotlin/StorageActivity.kt#L77-L82
```

### Java

```java
// References can be chained together multiple times
// earthRef points to 'images/earth.jpg'
StorageReference earthRef = spaceRef.getParent().child("earth.jpg");

// nullRef is null, since the parent of root is null
StorageReference nullRef = spaceRef.getRoot().getParent();
```

## Reference Properties

You can inspect references to better understand the files they point to
using the `getPath()`, `getName()`, and `getBucket()` methods. These methods
get the file's full path, name and bucket.

### Kotlin

```kotlin
// Reference's path is: "images/space.jpg"
// This is analogous to a file path on disk
spaceRef.path

// Reference's name is the last segment of the full path: "space.jpg"
// This is analogous to the file name
spaceRef.name

// Reference's bucket is the name of the storage bucket that the files are stored in
spaceRef.buckethttps://github.com/firebase/snippets-android/blob/a413b0658ff2fc7a72c4b0c59e84a889ff7fac45/storage/app/src/main/java/com/google/firebase/referencecode/storage/kotlin/StorageActivity.kt#L88-L97
```

### Java

```java
// Reference's path is: "images/space.jpg"
// This is analogous to a file path on disk
spaceRef.getPath();

// Reference's name is the last segment of the full path: "space.jpg"
// This is analogous to the file name
spaceRef.getName();

// Reference's bucket is the name of the storage bucket that the files are stored in
spaceRef.getBucket();
```

## Limitations on References

Reference paths and names can contain any sequence of valid Unicode characters,
but certain restrictions are imposed including:

1. Total length of reference.fullPath must be between 1 and 1024 bytes when UTF-8 encoded.
2. No Carriage Return or Line Feed characters.
3. Avoid using `#`, `[`, `]`, `*`, or `?`, as these do not work well with other tools such as the [Firebase Realtime Database](https://firebase.google.com/docs/database) or [gsutil](https://cloud.google.com/storage/docs/gsutil).

## Full Example

### Kotlin

```kotlin
// Points to the root reference
storageRef = storage.reference

// Points to "images"
imagesRef = storageRef.child("images")

// Points to "images/space.jpg"
// Note that you can use variables to create child values
val fileName = "space.jpg"
spaceRef = imagesRef.child(fileName)

// File path is "images/space.jpg"
val path = spaceRef.path

// File name is "space.jpg"
val name = spaceRef.name

// Points to "images"
imagesRef = spaceRef.parenthttps://github.com/firebase/snippets-android/blob/a413b0658ff2fc7a72c4b0c59e84a889ff7fac45/storage/app/src/main/java/com/google/firebase/referencecode/storage/kotlin/StorageActivity.kt#L103-L121
```

### Java

```java
// Points to the root reference
storageRef = storage.getReference();

// Points to "images"
imagesRef = storageRef.child("images");

// Points to "images/space.jpg"
// Note that you can use variables to create child values
String fileName = "space.jpg";
spaceRef = imagesRef.child(fileName);

// File path is "images/space.jpg"
String path = spaceRef.getPath();

// File name is "space.jpg"
String name = spaceRef.getName();

// Points to "images"
imagesRef = spaceRef.getParent();
```

Next, let's learn how to
[upload files](https://firebase.google.com/docs/storage/android/upload-files) to
Cloud Storage.