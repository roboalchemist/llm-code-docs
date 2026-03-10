# Source: https://firebase.google.com/docs/ml/android/label-images-with-automl.md.txt

After you [train your own model using AutoML Vision Edge](https://firebase.google.com/docs/ml/train-image-labeler),
you can use it in your app to label images.

> [!WARNING]
> Firebase ML's AutoML Vision Edge features are deprecated. Consider using [Vertex AI](https://cloud.google.com/vertex-ai/docs/beginner/beginners-guide) to automatically train ML models, which you can either [export as TensorFlow
> Lite models](https://cloud.google.com/vertex-ai/docs/export/export-edge-model) for on-device use or [deploy for cloud-based
> inference](https://cloud.google.com/vertex-ai/docs/predictions/overview).

There are two ways to integrate models trained from AutoML Vision Edge: You can
bundle the model by putting it inside your app's asset folder, or you can
dynamically download it from Firebase.

| Model bundling options ||
|---|---|
| Bundled in your app | - The model is part of your app's APK - The model is available immediately, even when the Android device is offline - No need for a Firebase project |
| Hosted with Firebase | - Host the model by uploading it to [Firebase Machine Learning](https://firebase.google.com/docs/ml) - Reduces APK size - The model is downloaded on demand - Push model updates without republishing your app - Easy A/B testing with [Firebase Remote Config](https://firebase.google.com/docs/remote-config) - Requires a Firebase project |

## Before you begin

1. Add the dependencies for the ML Kit Android libraries to your module's
   app-level gradle file, which is usually `app/build.gradle`:

   For bundling a model with your app:

       dependencies {
         // ...
         // Image labeling feature with bundled automl model
         implementation 'com.google.mlkit:image-labeling-custom:16.3.1'
       }

   For dynamically downloading a model from Firebase, add the `linkFirebase`
   dependency:

       dependencies {
         // ...
         // Image labeling feature with automl model downloaded
         // from firebase
         implementation 'com.google.mlkit:image-labeling-custom:16.3.1'
         implementation 'com.google.mlkit:linkfirebase:16.1.0'
       }

2. **If you want to download a model** , make sure you
   [add Firebase to your Android project](https://firebase.google.com/docs/android/setup),
   if you have not already done so. This is not required when you bundle the model.

## 1. Load the model

### Configure a local model source

To bundle the model with your app:

1. Extract the model and its metadata from the zip archive you downloaded
   from Firebase console. We recommend you use the files as you downloaded
   them, without modification (including the file names).

2. Include your model and its metadata files in your app package:

   1. If you don't have an assets folder in your project, create one by right-clicking the `app/` folder, then clicking **New \> Folder \> Assets Folder**.
   2. Create a sub-folder under the assets folder to contain the model files.
   3. Copy the files `model.tflite`, `dict.txt`, and `manifest.json` to the sub-folder (all three files must be in the same folder).
3. Add the following to your app's `build.gradle` file to ensure
   Gradle doesn't compress the model file when building the app:

       android {
           // ...
           aaptOptions {
               noCompress "tflite"
           }
       }

   The model file will be included in the app package and available to ML Kit
   as a raw asset.

   > [!NOTE]
   > **Note:** starting from version 4.1 of the Android Gradle plugin, .tflite will be added to the noCompress list by default and the above is not needed anymore.

4. Create `LocalModel` object, specifying the path to the model manifest
   file:

   ### Java

       AutoMLImageLabelerLocalModel localModel =
           new AutoMLImageLabelerLocalModel.Builder()
               .setAssetFilePath("manifest.json")
               // or .setAbsoluteFilePath(absolute file path to manifest file)
               .build();

   ### Kotlin

       val localModel = LocalModel.Builder()
           .setAssetManifestFilePath("manifest.json")
           // or .setAbsoluteManifestFilePath(absolute file path to manifest file)
           .build()

### Configure a Firebase-hosted model source

To use the remotely-hosted model, create a `CustomRemoteModel` object,
specifying the name you assigned the model when you published it:

### Java

    // Specify the name you assigned in the Firebase console.
    FirebaseModelSource firebaseModelSource =
        new FirebaseModelSource.Builder("your_model_name").build();
    CustomRemoteModel remoteModel =
        new CustomRemoteModel.Builder(firebaseModelSource).build();

### Kotlin

    // Specify the name you assigned in the Firebase console.
    val firebaseModelSource = FirebaseModelSource.Builder("your_model_name")
        .build()
    val remoteModel = CustomRemoteModel.Builder(firebaseModelSource).build()

Then, start the model download task, specifying the conditions under which
you want to allow downloading. If the model isn't on the device, or if a newer
version of the model is available, the task will asynchronously download the
model from Firebase:

### Java

    DownloadConditions downloadConditions = new DownloadConditions.Builder()
            .requireWifi()
            .build();
    RemoteModelManager.getInstance().download(remoteModel, downloadConditions)
            .addOnSuccessListener(new OnSuccessListener<Void>() {
                @Override
                public void onSuccess(@NonNull Task<Void> task) {
                    // Success.
                }
            });

### Kotlin

    val downloadConditions = DownloadConditions.Builder()
        .requireWifi()
        .build()
    RemoteModelManager.getInstance().download(remoteModel, downloadConditions)
        .addOnSuccessListener {
            // Success.
        }

Many apps start the download task in their initialization code, but you
can do so at any point before you need to use the model.

### Create an image labeler from your model

After you configure your model sources, create a `ImageLabeler` object from one
of them.

If you only have a locally-bundled model, just create a labeler from your
`CustomImageLabelerOptions` object and configure the confidence score
threshold you want to require (see [Evaluate your model](https://firebase.google.com/docs/ml/train-image-labeler#evaluate_the_model)):

### Java

    CustomImageLabelerOptions customImageLabelerOptions = new CustomImageLabelerOptions.Builder(localModel)
        .setConfidenceThreshold(0.0f)  // Evaluate your model in the Cloud console
                                       // to determine an appropriate value.
        .build();
    ImageLabeler labeler = ImageLabeling.getClient(customImageLabelerOptions);

### Kotlin

    val customImageLabelerOptions = CustomImageLabelerOptions.Builder(localModel)
        .setConfidenceThreshold(0.0f)  // Evaluate your model in the Cloud console
                                       // to determine an appropriate value.
        .build()
    val labeler = ImageLabeling.getClient(customImageLabelerOptions)

If you have a remotely-hosted model, you will have to check that it has been
downloaded before you run it. You can check the status of the model download
task using the model manager's `isModelDownloaded()` method.

Although you only have to confirm this before running the labeler, if you
have both a remotely-hosted model and a locally-bundled model, it might make
sense to perform this check when instantiating the image labeler: create a
labeler from the remote model if it's been downloaded, and from the local
model otherwise.

### Java

    RemoteModelManager.getInstance().isModelDownloaded(remoteModel)
            .addOnSuccessListener(new OnSuccessListener<Boolean>() {
                @Override
                public void onSuccess(Boolean isDownloaded) {
                    CustomImageLabelerOptions.Builder optionsBuilder;
                    if (isDownloaded) {
                        optionsBuilder = new CustomImageLabelerOptions.Builder(remoteModel);
                    } else {
                        optionsBuilder = new CustomImageLabelerOptions.Builder(localModel);
                    }
                    CustomImageLabelerOptions options = optionsBuilder
                            .setConfidenceThreshold(0.0f)  // Evaluate your model in the Cloud console
                                                           // to determine an appropriate threshold.
                            .build();

                    ImageLabeler labeler = ImageLabeling.getClient(options);
                }
            });

### Kotlin

    RemoteModelManager.getInstance().isModelDownloaded(remoteModel)
        .addOnSuccessListener { isDownloaded ->
            val optionsBuilder =
                if (isDownloaded) {
                    CustomImageLabelerOptions.Builder(remoteModel)
                } else {
                    CustomImageLabelerOptions.Builder(localModel)
                }
            // Evaluate your model in the Cloud console to determine an appropriate threshold.
            val options = optionsBuilder.setConfidenceThreshold(0.0f).build()
            val labeler = ImageLabeling.getClient(options)
    }

If you only have a remotely-hosted model, you should disable model-related
functionality---for example, grey-out or hide part of your UI---until
you confirm the model has been downloaded. You can do so by attaching a listener
to the model manager's `download()` method:

### Java

    RemoteModelManager.getInstance().download(remoteModel, conditions)
            .addOnSuccessListener(new OnSuccessListener<Void>() {
                @Override
                public void onSuccess(Void v) {
                  // Download complete. Depending on your app, you could enable
                  // the ML feature, or switch from the local model to the remote
                  // model, etc.
                }
            });

### Kotlin

    RemoteModelManager.getInstance().download(remoteModel, conditions)
        .addOnSuccessListener {
            // Download complete. Depending on your app, you could enable the ML
            // feature, or switch from the local model to the remote model, etc.
        }

## 2. Prepare the input image

Then, for each image you want to label, create an [`InputImage`](https://developers.google.com/android/reference/com/google/mlkit/vision/common/InputImage)
object from your image. The image labeler runs fastest when you use a `Bitmap`
or, if you use the camera2 API, a YUV_420_888 `media.Image`, which are
recommended when possible.


You can create an `InputImage` from different sources, each is explained below.

### Using a `media.Image`


To create an `InputImage` object from a
`media.Image` object, such as when you capture an image from a
device's camera, pass the `media.Image` object and the image's
rotation to `InputImage.fromMediaImage()`.


If you use the
[CameraX](https://developer.android.com/training/camerax) library, the `OnImageCapturedListener` and
`ImageAnalysis.Analyzer` classes calculate the rotation value
for you.

### Kotlin

```kotlin
private class YourImageAnalyzer : ImageAnalysis.Analyzer {
    override fun analyze(imageProxy: ImageProxy?) {
        val mediaImage = imageProxy?.image
        if (mediaImage != null) {
            val image = InputImage.fromMediaImage(mediaImage, imageProxy.imageInfo.rotationDegrees)
            // Pass image to an ML Kit Vision API
            // ...
        }
    }
}
```

### Java

```java
private class YourAnalyzer implements ImageAnalysis.Analyzer {

    @Override
    public void analyze(ImageProxy imageProxy) {
        if (imageProxy == null || imageProxy.getImage() == null) {
            return;
        }
        Image mediaImage = imageProxy.getImage();
        InputImage image =
                InputImage.fromMediaImage(mediaImage, imageProxy.imageInfo.rotationDegrees);
        // Pass image to an ML Kit Vision API
        // ...
    }
}
```


If you don't use a camera library that gives you the image's rotation degree, you
can calculate it from the device's rotation degree and the orientation of camera
sensor in the device:

### Kotlin

```kotlin
private val ORIENTATIONS = SparseIntArray()

init {
    ORIENTATIONS.append(Surface.ROTATION_0, 90)
    ORIENTATIONS.append(Surface.ROTATION_90, 0)
    ORIENTATIONS.append(Surface.ROTATION_180, 270)
    ORIENTATIONS.append(Surface.ROTATION_270, 180)
}
/**
 * Get the angle by which an image must be rotated given the device's current
 * orientation.
 */
@RequiresApi(api = Build.VERSION_CODES.LOLLIPOP)
@Throws(CameraAccessException::class)
private fun getRotationCompensation(cameraId: String, activity: Activity, context: Context): Int {
    // Get the device's current rotation relative to its "native" orientation.
    // Then, from the ORIENTATIONS table, look up the angle the image must be
    // rotated to compensate for the device's rotation.
    val deviceRotation = activity.windowManager.defaultDisplay.rotation
    var rotationCompensation = ORIENTATIONS.get(deviceRotation)

    // On most devices, the sensor orientation is 90 degrees, but for some
    // devices it is 270 degrees. For devices with a sensor orientation of
    // 270, rotate the image an additional 180 ((270 + 270) % 360) degrees.
    val cameraManager = context.getSystemService(CAMERA_SERVICE) as CameraManager
    val sensorOrientation = cameraManager
        .getCameraCharacteristics(cameraId)
        .get(CameraCharacteristics.SENSOR_ORIENTATION)!!
    rotationCompensation = (rotationCompensation + sensorOrientation + 270) % 360

    // Return the corresponding FirebaseVisionImageMetadata rotation value.
    val result: Int
    when (rotationCompensation) {
        0 -> result = FirebaseVisionImageMetadata.ROTATION_0
        90 -> result = FirebaseVisionImageMetadata.ROTATION_90
        180 -> result = FirebaseVisionImageMetadata.ROTATION_180
        270 -> result = FirebaseVisionImageMetadata.ROTATION_270
        else -> {
            result = FirebaseVisionImageMetadata.ROTATION_0
            Log.e(TAG, "Bad rotation value: $rotationCompensation")
        }
    }
    return result
}
```

### Java

```java
private static final SparseIntArray ORIENTATIONS = new SparseIntArray();
static {
    ORIENTATIONS.append(Surface.ROTATION_0, 90);
    ORIENTATIONS.append(Surface.ROTATION_90, 0);
    ORIENTATIONS.append(Surface.ROTATION_180, 270);
    ORIENTATIONS.append(Surface.ROTATION_270, 180);
}

/**
 * Get the angle by which an image must be rotated given the device's current
 * orientation.
 */
@RequiresApi(api = Build.VERSION_CODES.LOLLIPOP)
private int getRotationCompensation(String cameraId, Activity activity, Context context)
        throws CameraAccessException {
    // Get the device's current rotation relative to its "native" orientation.
    // Then, from the ORIENTATIONS table, look up the angle the image must be
    // rotated to compensate for the device's rotation.
    int deviceRotation = activity.getWindowManager().getDefaultDisplay().getRotation();
    int rotationCompensation = ORIENTATIONS.get(deviceRotation);

    // On most devices, the sensor orientation is 90 degrees, but for some
    // devices it is 270 degrees. For devices with a sensor orientation of
    // 270, rotate the image an additional 180 ((270 + 270) % 360) degrees.
    CameraManager cameraManager = (CameraManager) context.getSystemService(CAMERA_SERVICE);
    int sensorOrientation = cameraManager
            .getCameraCharacteristics(cameraId)
            .get(CameraCharacteristics.SENSOR_ORIENTATION);
    rotationCompensation = (rotationCompensation + sensorOrientation + 270) % 360;

    // Return the corresponding FirebaseVisionImageMetadata rotation value.
    int result;
    switch (rotationCompensation) {
        case 0:
            result = FirebaseVisionImageMetadata.ROTATION_0;
            break;
        case 90:
            result = FirebaseVisionImageMetadata.ROTATION_90;
            break;
        case 180:
            result = FirebaseVisionImageMetadata.ROTATION_180;
            break;
        case 270:
            result = FirebaseVisionImageMetadata.ROTATION_270;
            break;
        default:
            result = FirebaseVisionImageMetadata.ROTATION_0;
            Log.e(TAG, "Bad rotation value: " + rotationCompensation);
    }
    return result;
}
```

Then, pass the `media.Image` object and the
rotation degree value to `InputImage.fromMediaImage()`:

### Kotlin

```kotlin
val image = InputImage.fromMediaImage(mediaImage, rotation)
```

### Java

```java
InputImage image = InputImage.fromMediaImage(mediaImage, rotation);
```

### Using a file URI

To create an `InputImage` object from a file URI, pass
the app context and file URI to
`InputImage.fromFilePath()`. This is useful when you
use an `ACTION_GET_CONTENT` intent to prompt the user to select
an image from their gallery app.

### Kotlin

```kotlin
val image: InputImage
try {
    image = InputImage.fromFilePath(context, uri)
} catch (e: IOException) {
    e.printStackTrace()
}
```

### Java

```java
InputImage image;
try {
    image = InputImage.fromFilePath(context, uri);
} catch (IOException e) {
    e.printStackTrace();
}
```

### Using a `ByteBuffer` or `ByteArray`

To create an `InputImage` object from a
`ByteBuffer` or a `ByteArray`, first calculate the image
rotation degree as previously described for `media.Image` input.
Then, create the `InputImage` object with the buffer or array, together with image's
height, width, color encoding format, and rotation degree:

### Kotlin

```kotlin
val image = InputImage.fromByteBuffer(
        byteBuffer,
        /* image width */ 480,
        /* image height */ 360,
        rotationDegrees,
        InputImage.IMAGE_FORMAT_NV21 // or IMAGE_FORMAT_YV12
)
```

### Java

```java
InputImage image = InputImage.fromByteBuffer(byteBuffer,
        /* image width */ 480,
        /* image height */ 360,
        rotationDegrees,
        InputImage.IMAGE_FORMAT_NV21 // or IMAGE_FORMAT_YV12
);
```

### Using a `Bitmap`

To create an `InputImage` object from a
`Bitmap` object, make the following declaration:

### Kotlin

```kotlin
val image = InputImage.fromBitmap(bitmap, 0)
```

### Java

```java
InputImage image = InputImage.fromBitmap(bitmap, rotationDegree);
```

The image is represented by a `Bitmap` object together with rotation degrees.

## 3. Run the image labeler

To label objects in an image, pass the `image` object to the `ImageLabeler`'s
`process()` method.

### Java

    labeler.process(image)
            .addOnSuccessListener(new OnSuccessListener<List<ImageLabel>>() {
                @Override
                public void onSuccess(List<ImageLabel> labels) {
                    // Task completed successfully
                    // ...
                }
            })
            .addOnFailureListener(new OnFailureListener() {
                @Override
                public void onFailure(@NonNull Exception e) {
                    // Task failed with an exception
                    // ...
                }
            });

### Kotlin

    labeler.process(image)
            .addOnSuccessListener { labels ->
                // Task completed successfully
                // ...
            }
            .addOnFailureListener { e ->
                // Task failed with an exception
                // ...
            }

## 4. Get information about labeled objects

If the image labeling operation succeeds, a list of [`ImageLabel`](https://developers.google.com/android/reference/com/google/mlkit/vision/label/ImageLabel)
objects is passed to the success listener. Each `ImageLabel` object represents
something that was labeled in the image. You can get each label's text
description, the confidence score of the match and the index of the match.
For example:

### Java

    for (ImageLabel label : labels) {
        String text = label.getText();
        float confidence = label.getConfidence();
        int index = label.getIndex();
    }

### Kotlin

    for (label in labels) {
        val text = label.text
        val confidence = label.confidence
        val index = label.index
    }

## Tips to improve real-time performance

If you want to label images in a real-time application, follow these
guidelines to achieve the best framerates:

- Throttle calls to the image labeler. If a new video frame becomes available while the image labeler is running, drop the frame. See the [`VisionProcessorBase`](https://github.com/firebase/quickstart-android/blob/master/mlkit/app/src/main/java/com/google/firebase/samples/apps/mlkit/java/VisionProcessorBase.java) class in the quickstart sample app for an example.
- If you are using the output of the image labeler to overlay graphics on the input image, first get the result, then render the image and overlay in a single step. By doing so, you render to the display surface only once for each input frame. See the [`CameraSourcePreview`](https://github.com/firebase/quickstart-android/blob/master/mlkit/app/src/main/java/com/google/firebase/samples/apps/mlkit/common/CameraSourcePreview.java) and [`GraphicOverlay`](https://github.com/firebase/quickstart-android/blob/master/mlkit/app/src/main/java/com/google/firebase/samples/apps/mlkit/common/GraphicOverlay.java) classes in the quickstart sample app for an example.
- If you use the Camera2 API, capture images in
  `ImageFormat.YUV_420_888` format.

  If you use the older Camera API, capture images in
  `ImageFormat.NV21` format.

<br />