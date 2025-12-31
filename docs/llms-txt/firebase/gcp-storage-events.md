# Source: https://firebase.google.com/docs/functions/gcp-storage-events.md.txt

<br />

You can trigger a function in response to the uploading, updating, or deleting of files and folders inCloud Storage.

Examples in this page are based on a sample function that triggers when image files are uploaded toCloud Storage. This sample function demonstrates how to access event attributes, how to download a file to aCloud Functionsinstance, and other fundamentals of handlingCloud Storageevents.

## Import the required modules

To get started, import the module required for handlingCloud Storageevents:  

### Node.js

     const {onObjectFinalized} = require("firebase-functions/storage");  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Node/quickstarts/thumbnails/functions/index.js#L20-L20

### Python

     from firebase_functions import storage_fn  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Python/thumbnails/functions/main.py#L29-L29

To build out the full sample, also add the dependencies for theFirebaseAdmin SDKand image processing tools:  

### Node.js

     const {initializeApp} = require("firebase-admin/app");
    const {getStorage} = require("firebase-admin/storage");
    const logger = require("firebase-functions/logger");
    const path = require("path");

    // library for image resizing
    const sharp = require("sharp");

    initializeApp();  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Node/quickstarts/thumbnails/functions/index.js#L24-L32

### Python

     import io
    import pathlib

    from PIL import Image

    from firebase_admin import initialize_app

    initialize_app()
    from firebase_admin import storage  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Python/thumbnails/functions/main.py#L17-L25

## Scope aCloud Storagefunction

Use the following pattern to scope your function to a specificCloud Storagebucket and set any desired options:  

### Node.js

    // scope handler to a specific bucket, using storage options parameter
    exports.archivedopts = onObjectArchived({ bucket: "myBucket" }, (event) => {
      //...
    });

### Python

    # Scope handler to a specific bucket using storage options parameter
    @storage_fn.on_object_archived(bucket="myBucket")
    def archived_bucket(event: storage_fn.CloudEvent[storage_fn.StorageObjectData]):
        # ...

By contrast, the example thumbnail generator function is scoped to the default bucket for the project:  

### Node.js

```javascript
exports.generateThumbnail = onObjectFinalized({cpu: 2}, async (event) => {
// ...
});
```

### Python

    @storage_fn.on_object_archived()
    def generatethumbnail(event: storage_fn.CloudEvent[storage_fn.StorageObjectData]):
        # ...

## Set the function location

A mismatch between locations can result in deployment failure. Also, distance between the location of aCloud Storagebucket and the location of the function can create significant network latency. To avoid these situations, specify the[function location](https://firebase.google.com/docs/functions/locations)so that it matches the bucket/trigger location in one of these ways:

- Function location is the same as the trigger location
- Function location is inside the trigger location (when the trigger region is dual/multi region)
- Function may be in any location if the trigger region is set to`us-central1`

## HandleCloud Storageevents

These handlers for responding toCloud Storageevents are available:  

### Node.js

- `onObjectArchived`Only sent when a bucket has enabled[object versioning](https://cloud.google.com/storage/docs/object-versioning). This event indicates that the live version of an object has become an archived version, either because it was archived or because it was overwritten by the upload of an object of the same name.
- `onObjectDeleted`Sent when an object has been permanently deleted. This includes objects that are overwritten or are deleted as part of the bucket's[lifecycle configuration](https://cloud.google.com/storage/docs/lifecycle). For buckets with[object versioning](https://cloud.google.com/storage/docs/object-versioning)enabled, this is not sent when an object is archived (see`onArchive`), even if archival occurs via the`storage.objects.delete`method.
- `onObjectFinalized`Sent when a new object (or a new generation of an existing object) is successfully created in the bucket. This includes copying or rewriting an existing object. A failed upload does not trigger this event.
- `onMetadataUpdated`Sent when the metadata of an existing object changes.

### Python

- `on_object_archived`Only sent when a bucket has enabled[object versioning](https://cloud.google.com/storage/docs/object-versioning). This event indicates that the live version of an object has become an archived version, either because it was archived or because it was overwritten by the upload of an object of the same name.
- `on_object_deleted`Sent when an object has been permanently deleted. This includes objects that are overwritten or are deleted as part of the bucket's[lifecycle configuration](https://cloud.google.com/storage/docs/lifecycle). For buckets with[object versioning](https://cloud.google.com/storage/docs/object-versioning)enabled, this is not sent when an object is archived (see`onArchive`), even if archival occurs via the`storage.objects.delete`method.
- `on_object_finalized`Sent when a new object (or a new generation of an existing object) is successfully created in the bucket. This includes copying or rewriting an existing object. A failed upload does not trigger this event.
- `on_metadata_updated`Sent when the metadata of an existing object changes.

## AccessCloud Storageobject attributes

Cloud Functionsexposes a number ofCloud Storageobject attributes such as the object's size and content type for the file updated. The`metageneration`attribute is incremented whenever there's a change to the object's metadata. For new objects, the`metageneration`value is`1`.  

### Node.js

```javascript
const fileBucket = event.data.bucket; // Storage bucket containing the file.
const filePath = event.data.name; // File path in the bucket.
const contentType = event.data.contentType; // File content type.  
https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Node/quickstarts/thumbnails/functions/index.js#L46-L48
```

### Python

    bucket_name = event.data.bucket
    file_path = pathlib.PurePath(event.data.name)
    content_type = event.data.content_type  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Python/thumbnails/functions/main.py#L43-L45

The thumbnail generation sample uses some of these attributes to detect exit cases in which the function returns:  

### Node.js

```javascript
// Exit if this is triggered on a file that is not an image.
if (!contentType.startsWith("image/")) {
  return logger.log("This is not an image.");
}
// Exit if the image is already a thumbnail.
const fileName = path.basename(filePath);
if (fileName.startsWith("thumb_")) {
  return logger.log("Already a Thumbnail.");
}https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Node/quickstarts/thumbnails/functions/index.js#L52-L60
```

### Python

    # Exit if this is triggered on a file that is not an image.
    if not content_type or not content_type.startswith("image/"):
        print(f"This is not an image. ({content_type})")
        return

    # Exit if the image is already a thumbnail.
    if file_path.name.startswith("thumb_"):
        print("Already a thumbnail.")
        return  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Python/thumbnails/functions/main.py#L49-L57

## Download, transform, and upload a file

For some cases, it may not be necessary to download files fromCloud Storage. However, to perform intensive tasks such as generating a thumbnail image from a file stored inCloud Storage, you need to download files to the functions instance---that is, the virtual machine that runs your code.

UsingCloud Functionstogether with image-processing programs like[`sharp`](https://sharp.pixelplumbing.com/)for Node.js and[Pillow](https://pillow.readthedocs.io/en/stable/)for Python, you can perform manipulations on graphical image files. The following is an example of how to create a thumbnail image for an uploaded image file:  

### Node.js

    /**
     * When an image is uploaded in the Storage bucket,
     * generate a thumbnail automatically using sharp.
     */
    exports.generateThumbnail = onObjectFinalized({cpu: 2}, async (event) => {

      const fileBucket = event.data.bucket; // Storage bucket containing the file.
      const filePath = event.data.name; // File path in the bucket.
      const contentType = event.data.contentType; // File content type.

      // Exit if this is triggered on a file that is not an image.
      if (!contentType.startsWith("image/")) {
        return logger.log("This is not an image.");
      }
      // Exit if the image is already a thumbnail.
      const fileName = path.basename(filePath);
      if (fileName.startsWith("thumb_")) {
        return logger.log("Already a Thumbnail.");
      }

      // Download file into memory from bucket.
      const bucket = getStorage().bucket(fileBucket);
      const downloadResponse = await bucket.file(filePath).download();
      const imageBuffer = downloadResponse[0];
      logger.log("Image downloaded!");

      // Generate a thumbnail using sharp.
      const thumbnailBuffer = await sharp(imageBuffer).resize({
        width: 200,
        height: 200,
        withoutEnlargement: true,
      }).toBuffer();
      logger.log("Thumbnail created");

      // Prefix 'thumb_' to file name.
      const thumbFileName = `thumb_${fileName}`;
      const thumbFilePath = path.join(path.dirname(filePath), thumbFileName);

      // Upload the thumbnail.
      const metadata = {contentType: contentType};
      await bucket.file(thumbFilePath).save(thumbnailBuffer, {
        metadata: metadata,
      });
      return logger.log("Thumbnail uploaded!");
    });  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Node/quickstarts/thumbnails/functions/index.js#L37-L89

Download the file to a temporary directory on yourCloud Functionsinstance. In this location, you can process the file as needed and then upload toCloud Storage. When performing asynchronous tasks, make sure you return a JavaScript promise in your callback.

### Python

    @storage_fn.on_object_finalized()
    def generatethumbnail(event: storage_fn.CloudEvent[storage_fn.StorageObjectData]):
        """When an image is uploaded in the Storage bucket, generate a thumbnail
        automatically using Pillow."""

        bucket_name = event.data.bucket
        file_path = pathlib.PurePath(event.data.name)
        content_type = event.data.content_type

        # Exit if this is triggered on a file that is not an image.
        if not content_type or not content_type.startswith("image/"):
            print(f"This is not an image. ({content_type})")
            return

        # Exit if the image is already a thumbnail.
        if file_path.name.startswith("thumb_"):
            print("Already a thumbnail.")
            return

        bucket = storage.bucket(bucket_name)

        image_blob = bucket.blob(str(file_path))
        image_bytes = image_blob.download_as_bytes()
        image = Image.open(io.BytesIO(image_bytes))

        image.thumbnail((200, 200))
        thumbnail_io = io.BytesIO()
        image.save(thumbnail_io, format="png")
        thumbnail_path = file_path.parent / pathlib.PurePath(f"thumb_{file_path.stem}.png")
        thumbnail_blob = bucket.blob(str(thumbnail_path))
        thumbnail_blob.upload_from_string(thumbnail_io.getvalue(), content_type="image/png")  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Python/thumbnails/functions/main.py#L35-L73

This code creates a 200x200 thumbnail for the image saved in a temporary directory, then uploads it back toCloud Storage.