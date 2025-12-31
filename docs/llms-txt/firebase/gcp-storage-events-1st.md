# Source: https://firebase.google.com/docs/functions/1st-gen/gcp-storage-events-1st.md.txt

<br />

| **Note:** The 1st-gen functionality described in this page is also supported inCloud Functions(2nd gen) with improved features and performance. For more information about 2nd gen, see the[version comparison](https://firebase.google.com/docs/functions/version-comparison). To go directly to the 2nd gen guide for this feature, see[Cloud Storage triggers](https://firebase.google.com/docs/functions/gcp-storage-events).

You can trigger a function in response to the uploading, updating, or deleting of files and folders inCloud Storage.

Examples in this page are based on a sample function that triggers when image files are uploaded toCloud Storage. This sample function demonstrates how to access event attributes, how to download a file to aCloud Functionsinstance, and other fundamentals of handlingCloud Storageevents.

For more examples of use cases, see[What can I do withCloud Functions?](https://firebase.google.com/docs/functions/use-cases)

## Trigger a function onCloud Storagechanges

Use[`functions.storage`](https://firebase.google.com/docs/reference/functions/firebase-functions.storage)to create a function that handlesCloud Storageevents. Depending on whether you want to scope your function to a specificCloud Storagebucket or use the default bucket, use one of the following:

- [`functions.storage.object()`](https://firebase.google.com/docs/reference/functions/firebase-functions.storage#storageobject)to listen for object changes on the defaultCloud Storagebucket.
- [`functions.storage.bucket('bucketName').object()`](https://firebase.google.com/docs/reference/functions/firebase-functions.storage#storagebucket)to listen for object changes on a specific bucket.

For example, the thumbnail generator sample is scoped to the default bucket for the project:

<br />

```gdscript
exports.firstGenGenerateThumbnail = functions.storage.object().onFinalize(async (object) => {
  // ...
});
```

<br />

| **Important:** Distance between the location of aCloud Storagebucket and the location of the function can create significant network latency. To optimize performance, consider specifying the[function location](https://firebase.google.com/docs/functions/locations)where applicable.

Cloud Storagesupports these events:

- `onArchive`Only sent when a bucket has enabled[object versioning](https://cloud.google.com/storage/docs/object-versioning). This event indicates that the live version of an object has become an archived version, either because it was archived or because it was overwritten by the upload of an object of the same name.
- `onDelete`Sent when an object has been permanently deleted. This includes objects that are overwritten or are deleted as part of the bucket's[lifecycle configuration](https://cloud.google.com/storage/docs/lifecycle). For buckets with[object versioning](https://cloud.google.com/storage/docs/object-versioning)enabled, this is not sent when an object is archived (see`onArchive`), even if archival occurs via the`storage.objects.delete`method.
- `onFinalize`Sent when a new object (or a new generation of an existing object) is successfully created in the bucket. This includes copying or rewriting an existing object. A failed upload does not trigger this event.
- `onMetadataUpdate`Sent when the metadata of an existing object changes.

Set the event within the`on`event handler as shown above for`onFinalize`.

## AccessCloud Storageobject attributes

Cloud Functionsexposes a number ofCloud Storageobject attributes such as[`size`](https://firebase.google.com/docs/reference/functions/firebase-functions.storage#storageobjectmetadatasize)and[`contentType`](https://firebase.google.com/docs/reference/functions/firebase-functions.storage.objectmetadata#storageobjectmetadatacontenttype)for the file updated. The['metageneration'](https://firebase.google.com/docs/reference/functions/firebase-functions.storage.objectmetadata#storageobjectmetadatametageneration)attribute is incremented whenever there's a change to the object's metadata. For new objects, the`metageneration`value is`1`.

<br />

```gdscript
const fileBucket = object.bucket; // The Storage bucket that contains the file.
const filePath = object.name; // File path in the bucket.
const contentType = object.contentType; // File content type.https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Node-1st-gen/quickstarts/thumbnails/functions/index.js#L37-L39
```

<br />

The thumbnail generation sample uses some of these attributes to detect exit cases in which the function returns:  

```gdscript
// Exit if this is triggered on a file that is not an image.
if (!contentType.startsWith('image/')) {
  return functions.logger.log('This is not an image.');
}

// Get the file name.
const fileName = path.basename(filePath);
// Exit if the image is already a thumbnail.
if (fileName.startsWith('thumb_')) {
  return functions.logger.log('Already a Thumbnail.');
}https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Node-1st-gen/quickstarts/thumbnails/functions/index.js#L43-L53
```

## Download, transform, and upload a file

For some cases, it may not be necessary to download files fromCloud Storage. However, to perform intensive tasks such as generating a thumbnail image from a file stored inCloud Storage, you need to download files to the functions instance---that is, the virtual machine that runs your code.

To easily download and re-upload objects toCloud Storage, install the[Google Cloud Storagepackage](https://www.npmjs.com/package/@google-cloud/storage)using`npm install --save @google-cloud/storage`, and import it. To use JavaScript promises to handle external processes like the thumbnail processing tasks in the sample, also import`child-process-promise`:

<br />

```gdscript
const functions = require('firebase-functions/v1');
const admin = require('firebase-admin');
admin.initializeApp()
const path = require('path');

//library for resizing images
const sharp = require('sharp');https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Node-1st-gen/quickstarts/thumbnails/functions/index.js#L19-L25
```

<br />

Use`gcs.bucket.file(filePath).download`to download a file to a temporary directory on yourCloud Functionsinstance. In this location, you can process the file as needed and then upload toCloud Storage. When performing asynchronous tasks, make sure you return a JavaScript promise in your callback.

### Example: image transformation

UsingCloud Functionstogether with image-processing programs like[`sharp`](https://sharp.pixelplumbing.com/), you can perform manipulations on graphical image files. The following is an example of how to create a thumbnail image for an uploaded image file:

<br />

```gdscript
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
return functions.logger.log("Thumbnail uploaded!");https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Node-1st-gen/quickstarts/thumbnails/functions/index.js#L57-L80
```

<br />

This code creates a 200x200 thumbnail for the image saved in a temporary directory, then uploads it back toCloud Storage.

### Explore more examples

More examples of common media transformation functions including[transcoding images](https://github.com/firebase/functions-samples/tree/main/Node-1st-gen/convert-images),[moderating content](https://github.com/firebase/functions-samples/tree/main/Node-1st-gen/moderate-images),[extracting EXIF metadata](https://github.com/firebase/functions-samples/tree/main/Node-1st-gen/exif-images). The[full list of examples](https://github.com/firebase/functions-samples)is available on GitHub.