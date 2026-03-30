# Source: https://firebase.google.com/docs/functions/1st-gen/gcp-storage-events-1st.md.txt

> [!NOTE]
> **Note:** The 1st-gen functionality described in this page is also supported in Cloud Functions (2nd gen) with improved features and performance. For more information about 2nd gen, see the [version comparison](https://firebase.google.com/docs/functions/version-comparison). To go directly to the 2nd gen guide for this feature, see [Cloud Storage triggers](https://firebase.google.com/docs/functions/gcp-storage-events).

You can trigger a function in response to the uploading, updating, or
deleting of files and folders in Cloud Storage.

Examples in this page are based on a sample function that triggers when image
files are uploaded to Cloud Storage. This sample function demonstrates
how to access event attributes, how to download a file to a Cloud Functions
instance, and other fundamentals of handling Cloud Storage events.

For more examples of use cases, see
[What can I do with Cloud Functions?](https://firebase.google.com/docs/functions/use-cases)

## Trigger a function on Cloud Storage changes

Use [`functions.storage`](https://firebase.google.com/docs/reference/functions/firebase-functions.storage)
to create a function that handles
Cloud Storage events. Depending on whether you want to scope your
function to a specific Cloud Storage bucket or use the default
bucket, use one of the following:

- [`functions.storage.object()`](https://firebase.google.com/docs/reference/functions/firebase-functions.storage#storageobject) to listen for object changes on the default Cloud Storage bucket.
- [`functions.storage.bucket('bucketName').object()`](https://firebase.google.com/docs/reference/functions/firebase-functions.storage#storagebucket) to listen for object changes on a specific bucket.

For example, the thumbnail generator sample is scoped to the default bucket for
the project:

<br />

```
exports.firstGenGenerateThumbnail = functions.storage.object().onFinalize(async (object) => {
  // ...
});
```

<br />

> [!IMPORTANT]
> **Important:** Distance between the location of a Cloud Storage bucket and the location of the function can create significant network latency. To optimize performance, consider specifying the [function location](https://firebase.google.com/docs/functions/locations) where applicable.

Cloud Storage supports these events:

- `onArchive` Only sent when a bucket has enabled [object versioning](https://cloud.google.com/storage/docs/object-versioning). This event indicates that the live version of an object has become an archived version, either because it was archived or because it was overwritten by the upload of an object of the same name.
- `onDelete` Sent when an object has been permanently deleted. This includes objects that are overwritten or are deleted as part of the bucket's [lifecycle configuration](https://cloud.google.com/storage/docs/lifecycle). For buckets with [object versioning](https://cloud.google.com/storage/docs/object-versioning) enabled, this is not sent when an object is archived (see `onArchive`), even if archival occurs via the `storage.objects.delete` method.
- `onFinalize` Sent when a new object (or a new generation of an existing object) is successfully created in the bucket. This includes copying or rewriting an existing object. A failed upload does not trigger this event.
- `onMetadataUpdate` Sent when the metadata of an existing object changes.

Set the event within the `on` event handler as shown above for `onFinalize`.

## Access Cloud Storage object attributes

Cloud Functions exposes a number of Cloud Storage object attributes such
as
[`size`](https://firebase.google.com/docs/reference/functions/firebase-functions.storage#storageobjectmetadatasize)
and
[`contentType`](https://firebase.google.com/docs/reference/functions/firebase-functions.storage.objectmetadata#storageobjectmetadatacontenttype)
for the file updated. The
['metageneration'](https://firebase.google.com/docs/reference/functions/firebase-functions.storage.objectmetadata#storageobjectmetadatametageneration)
attribute is incremented whenever there's a change to the
object's metadata. For new objects, the `metageneration` value is `1`.

<br />

```
const fileBucket = object.bucket; // The Storage bucket that contains the file.
const filePath = object.name; // File path in the bucket.
const contentType = object.contentType; // File content type.
```

<br />

The thumbnail generation sample uses some of these attributes to detect exit
cases in which the function returns:

```
// Exit if this is triggered on a file that is not an image.
if (!contentType.startsWith('image/')) {
  return functions.logger.log('This is not an image.');
}

// Get the file name.
const fileName = path.basename(filePath);
// Exit if the image is already a thumbnail.
if (fileName.startsWith('thumb_')) {
  return functions.logger.log('Already a Thumbnail.');
}
```

## Download, transform, and upload a file

For some cases, it may not be necessary to download files from
Cloud Storage. However, to perform intensive tasks such as generating a
thumbnail image from a file stored in Cloud Storage, you need to download
files to the functions instance---that is, the virtual machine that runs
your code.

To easily download and re-upload objects to Cloud Storage, install the
[Google Cloud Storage
package](https://www.npmjs.com/package/@google-cloud/storage) using
`npm install --save @google-cloud/storage`, and import it. To use JavaScript
promises to handle external processes like the thumbnail processing tasks in the
sample, also import `child-process-promise`:

<br />

```
const functions = require('firebase-functions/v1');
const admin = require('firebase-admin');
admin.initializeApp()
const path = require('path');

//library for resizing images
const sharp = require('sharp');
```

<br />

Use `gcs.bucket.file(filePath).download` to download a file to a temporary
directory on your Cloud Functions instance. In this location, you can
process the file as needed and then upload to Cloud Storage. When
performing asynchronous tasks, make sure you return a JavaScript promise in your
callback.

### Example: image transformation

Using Cloud Functions together with image-processing programs like
[`sharp`](https://sharp.pixelplumbing.com/), you can perform
manipulations on graphical image files. The following is an example of how to
create a thumbnail image for an uploaded image file:

<br />

```
// Download file from bucket.
const bucket = admin.storage().bucket(fileBucket);
const metadata = {
  contentType: contentType,
};
const downloadResponse = await bucket.file(filePath).download();
const imageBuffer = downloadResponse[0];
functions.logger.log("Image downloaded!");

// Generate a thumbnail using sharp.
const thumbnailBuffer = await sharp(imageBuffer).resize({
  width: 200,
  height: 200,
  withoutEnlargement: true,
}).toBuffer();
functions.logger.log("Thumbnail created");

// Upload the thumbnail with a 'thumb_' prefix.
const thumbFileName = `thumb_${fileName}`;
const thumbFilePath = path.join(path.dirname(filePath), thumbFileName);
await bucket.file(thumbFilePath).save(thumbnailBuffer, {
  metadata: metadata,
});
return functions.logger.log("Thumbnail uploaded!");
```

<br />

This code creates a
200x200 thumbnail for the image saved in a temporary directory, then uploads it
back to Cloud Storage.

### Explore more examples

More examples of common media transformation functions including
[transcoding images](https://github.com/firebase/functions-samples/tree/main/Node-1st-gen/convert-images),
[moderating content](https://github.com/firebase/functions-samples/tree/main/Node-1st-gen/moderate-images),
[extracting EXIF metadata](https://github.com/firebase/functions-samples/tree/main/Node-1st-gen/exif-images).
The [full list of examples](https://github.com/firebase/functions-samples) is
available on GitHub.