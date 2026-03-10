# Source: https://firebase.google.com/docs/ml-kit/android/detect-objects.md.txt

> [!CAUTION]
> This page describes an old version of the Object Detection and Tracking API, which was part
> of ML Kit for Firebase. Development of this API has been moved to the
> standalone ML Kit SDK, which you can use with or without Firebase.
> [Learn more](https://developers.google.com/ml-kit/migration).
>
> See
> [Detect and track objects with ML Kit on Android](https://developers.google.com/ml-kit/vision/object-detection/android)
> for the latest documentation.


You can use ML Kit to detect and track objects across frames of video.

When you pass ML Kit images, ML Kit returns, for each image, a list of
up to five detected objects and their position in the image. When detecting
objects in video streams, every object has an ID that you can use to track the
object across images. You can also optionally enable coarse object
classification, which labels objects with broad category descriptions.

<br />

## Before you begin

1. If you haven't already, [add Firebase to your Android project](https://firebase.google.com/docs/android/setup).
2. Add the dependencies for the ML Kit Android libraries to your module (app-level) Gradle file (usually `app/build.gradle`):

   ```
   apply plugin: 'com.android.application'
   apply plugin: 'com.google.gms.google-services'

   dependencies {
     // ...

     implementation 'com.google.firebase:firebase-ml-vision:24.0.3'
     implementation 'com.google.firebase:firebase-ml-vision-object-detection-model:19.0.6'
   }
   ```

## 1. Configure the object detector

To start detecting and tracking objects, first create an instance of
`FirebaseVisionObjectDetector`, optionally specifying any detector settings you
want to change from the default.

1. Configure the object detector for your use case with a
   `FirebaseVisionObjectDetectorOptions` object. You can change the following
   settings:

   | Object Detector Settings ||
   |---|---|
   | Detection mode | `STREAM_MODE` (default) \| `SINGLE_IMAGE_MODE` In `STREAM_MODE` (default), the object detector runs with low latency, but might produce incomplete results (such as unspecified bounding boxes or category labels) on the first few invocations of the detector. Also, in `STREAM_MODE`, the detector assigns tracking IDs to objects, which you can use to track objects across frames. Use this mode when you want to track objects, or when low latency is important, such as when processing video streams in real time. In `SINGLE_IMAGE_MODE`, the object detector waits until a detected object's bounding box and (if you enabled classification) category label are available before returning a result. As a consequence, detection latency is potentially higher. Also, in `SINGLE_IMAGE_MODE`, tracking IDs are not assigned. Use this mode if latency isn't critical and you don't want to deal with partial results. |
   | Detect and track multiple objects | `false` (default) \| `true` Whether to detect and track up to five objects or only the most prominent object (default). |
   | Classify objects | `false` (default) \| `true` Whether or not to classify detected objects into coarse categories. When enabled, the object detector classifies objects into the following categories: fashion goods, food, home goods, places, plants, and unknown. |

   The object detection and tracking API is optimized for these two core use
   cases:
   - Live detection and tracking of the most prominent object in the camera viewfinder
   - Detection of multiple objects from a static image

   To configure the API for these use cases:

   ### Java

       // Live detection and tracking
       FirebaseVisionObjectDetectorOptions options =
               new FirebaseVisionObjectDetectorOptions.Builder()
                       .setDetectorMode(FirebaseVisionObjectDetectorOptions.STREAM_MODE)
                       .enableClassification()  // Optional
                       .build();

       // Multiple object detection in static images
       FirebaseVisionObjectDetectorOptions options =
               new FirebaseVisionObjectDetectorOptions.Builder()
                       .setDetectorMode(FirebaseVisionObjectDetectorOptions.SINGLE_IMAGE_MODE)
                       .enableMultipleObjects()
                       .enableClassification()  // Optional
                       .build();

   ### Kotlin

       // Live detection and tracking
       val options = FirebaseVisionObjectDetectorOptions.Builder()
               .setDetectorMode(FirebaseVisionObjectDetectorOptions.STREAM_MODE)
               .enableClassification()  // Optional
               .build()

       // Multiple object detection in static images
       val options = FirebaseVisionObjectDetectorOptions.Builder()
               .setDetectorMode(FirebaseVisionObjectDetectorOptions.SINGLE_IMAGE_MODE)
               .enableMultipleObjects()
               .enableClassification()  // Optional
               .build()

2. Get an instance of `FirebaseVisionObjectDetector`:

   ### Java

       FirebaseVisionObjectDetector objectDetector =
               FirebaseVision.getInstance().getOnDeviceObjectDetector();

       // Or, to change the default settings:
       FirebaseVisionObjectDetector objectDetector =
               FirebaseVision.getInstance().getOnDeviceObjectDetector(options);

   ### Kotlin

       val objectDetector = FirebaseVision.getInstance().getOnDeviceObjectDetector()

       // Or, to change the default settings:
       val objectDetector = FirebaseVision.getInstance().getOnDeviceObjectDetector(options)

   > [!NOTE]
   > **Note:** Check the console for errors generated by the constructor.

## 2. Run the object detector

To detect and track objects, pass images to the `FirebaseVisionObjectDetector`
instance's `processImage()` method.

For each frame of video or image in a sequence, do the following:

1. Create a `FirebaseVisionImage` object from your image.

   -
     To create a `FirebaseVisionImage` object from a
     `media.Image` object, such as when capturing an image from a
     device's camera, pass the `media.Image` object and the image's
     rotation to `FirebaseVisionImage.fromMediaImage()`.


     If you use the
     [CameraX](https://developer.android.com/training/camerax) library, the `OnImageCapturedListener` and
     `ImageAnalysis.Analyzer` classes calculate the rotation value
     for you, so you just need to convert the rotation to one of ML Kit's
     `ROTATION_` constants before calling
     `FirebaseVisionImage.fromMediaImage()`:

     ### Java

     ```java
     private class YourAnalyzer implements ImageAnalysis.Analyzer {

         private int degreesToFirebaseRotation(int degrees) {
             switch (degrees) {
                 case 0:
                     return FirebaseVisionImageMetadata.ROTATION_0;
                 case 90:
                     return FirebaseVisionImageMetadata.ROTATION_90;
                 case 180:
                     return FirebaseVisionImageMetadata.ROTATION_180;
                 case 270:
                     return FirebaseVisionImageMetadata.ROTATION_270;
                 default:
                     throw new IllegalArgumentException(
                             "Rotation must be 0, 90, 180, or 270.");
             }
         }

         @Override
         public void analyze(ImageProxy imageProxy, int degrees) {
             if (imageProxy == null || imageProxy.getImage() == null) {
                 return;
             }
             Image mediaImage = imageProxy.getImage();
             int rotation = degreesToFirebaseRotation(degrees);
             FirebaseVisionImage image =
                     FirebaseVisionImage.fromMediaImage(mediaImage, rotation);
             // Pass image to an ML Kit Vision API
             // ...
         }
     }
     ```

     ### Kotlin

     ```kotlin
     private class YourImageAnalyzer : ImageAnalysis.Analyzer {
         private fun degreesToFirebaseRotation(degrees: Int): Int = when(degrees) {
             0 -> FirebaseVisionImageMetadata.ROTATION_0
             90 -> FirebaseVisionImageMetadata.ROTATION_90
             180 -> FirebaseVisionImageMetadata.ROTATION_180
             270 -> FirebaseVisionImageMetadata.ROTATION_270
             else -> throw Exception("Rotation must be 0, 90, 180, or 270.")
         }

         override fun analyze(imageProxy: ImageProxy?, degrees: Int) {
             val mediaImage = imageProxy?.image
             val imageRotation = degreesToFirebaseRotation(degrees)
             if (mediaImage != null) {
                 val image = FirebaseVisionImage.fromMediaImage(mediaImage, imageRotation)
                 // Pass image to an ML Kit Vision API
                 // ...
             }
         }
     }
     ```


     If you don't use a camera library that gives you the image's rotation, you
     can calculate it from the device's rotation and the orientation of camera
     sensor in the device:

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

     Then, pass the `media.Image` object and the
     rotation value to `FirebaseVisionImage.fromMediaImage()`:

     ### Java

     ```java
     FirebaseVisionImage image = FirebaseVisionImage.fromMediaImage(mediaImage, rotation);
     ```

     ### Kotlin

     ```kotlin
     val image = FirebaseVisionImage.fromMediaImage(mediaImage, rotation)
     ```
   - To create a `FirebaseVisionImage` object from a file URI, pass the app context and file URI to `FirebaseVisionImage.fromFilePath()`. This is useful when you use an `ACTION_GET_CONTENT` intent to prompt the user to select an image from their gallery app.

     ### Java

     ```java
     FirebaseVisionImage image;
     try {
         image = FirebaseVisionImage.fromFilePath(context, uri);
     } catch (IOException e) {
         e.printStackTrace();
     }
     ```

     ### Kotlin

     ```kotlin
     val image: FirebaseVisionImage
     try {
         image = FirebaseVisionImage.fromFilePath(context, uri)
     } catch (e: IOException) {
         e.printStackTrace()
     }
     ```
   - To create a `FirebaseVisionImage` object from a `ByteBuffer` or a byte array, first calculate the image rotation as described above for `media.Image` input.

     Then, create a `FirebaseVisionImageMetadata` object
     that contains the image's height, width, color encoding format,
     and rotation:

     ### Java

     ```java
     FirebaseVisionImageMetadata metadata = new FirebaseVisionImageMetadata.Builder()
             .setWidth(480)   // 480x360 is typically sufficient for
             .setHeight(360)  // image recognition
             .setFormat(FirebaseVisionImageMetadata.IMAGE_FORMAT_NV21)
             .setRotation(rotation)
             .build();
     ```

     ### Kotlin

     ```kotlin
     val metadata = FirebaseVisionImageMetadata.Builder()
             .setWidth(480) // 480x360 is typically sufficient for
             .setHeight(360) // image recognition
             .setFormat(FirebaseVisionImageMetadata.IMAGE_FORMAT_NV21)
             .setRotation(rotation)
             .build()
     ```

     Use the buffer or array, and the metadata object, to create a
     `FirebaseVisionImage` object:

     ### Java

     ```java
     FirebaseVisionImage image = FirebaseVisionImage.fromByteBuffer(buffer, metadata);
     // Or: FirebaseVisionImage image = FirebaseVisionImage.fromByteArray(byteArray, metadata);https://github.com/firebase/snippets-android/blob/e69640da6af8999c7650b5f01297d92f88da115a/mlkit/app/src/main/java/com/google/firebase/example/mlkit/VisionImage.java#L65-L65
     ```

     ### Kotlin

     ```kotlin
     val image = FirebaseVisionImage.fromByteBuffer(buffer, metadata)
     // Or: val image = FirebaseVisionImage.fromByteArray(byteArray, metadata)https://github.com/firebase/snippets-android/blob/e69640da6af8999c7650b5f01297d92f88da115a/mlkit/app/src/main/java/com/google/firebase/example/mlkit/kotlin/VisionImage.kt#L59-L59
     ```
   - To create a `FirebaseVisionImage` object from a `Bitmap` object:

     ### Java

     ```java
     FirebaseVisionImage image = FirebaseVisionImage.fromBitmap(bitmap);
     ```

     ### Kotlin

     ```kotlin
     val image = FirebaseVisionImage.fromBitmap(bitmap)
     ```
     The image represented by the `Bitmap` object must be upright, with no additional rotation required.
2. Pass the image to the `processImage()` method:

   ### Java

       objectDetector.processImage(image)
               .addOnSuccessListener(
                       new OnSuccessListener<List<FirebaseVisionObject>>() {
                           @Override
                           public void onSuccess(List<FirebaseVisionObject> detectedObjects) {
                               // Task completed successfully
                               // ...
                           }
                       })
               .addOnFailureListener(
                       new OnFailureListener() {
                           @Override
                           public void onFailure(@NonNull Exception e) {
                               // Task failed with an exception
                               // ...
                           }
                       });

   ### Kotlin

       objectDetector.processImage(image)
               .addOnSuccessListener { detectedObjects ->
                   // Task completed successfully
                   // ...
               }
               .addOnFailureListener { e ->
                   // Task failed with an exception
                   // ...
               }

   > [!NOTE]
   > **Note:** Check the console for errors generated by the detector.

3. If the call to `processImage()` succeeds, a list of `FirebaseVisionObject`s
   is passed to the success listener.

   > [!NOTE]
   > **Note:** In streaming mode, the object detector might need to process 30 or more frames, depending on device performance, before it detects the first object.

   Each `FirebaseVisionObject` contains the following properties:

   |---|---|
   | Bounding box | A `Rect` indicating the position of the object in the image. |
   | Tracking ID | An integer that identifies the object across images. Null in SINGLE_IMAGE_MODE. |
   | Category | The coarse category of the object. If the object detector doesn't have classification enabled, this is always `FirebaseVisionObject.CATEGORY_UNKNOWN`. |
   | Confidence | The confidence value of the object classification. If the object detector doesn't have classification enabled, or the object is classified as unknown, this is `null`. |

   ### Java

       // The list of detected objects contains one item if multiple object detection wasn't enabled.
       for (FirebaseVisionObject obj : detectedObjects) {
           Integer id = obj.getTrackingId();
           Rect bounds = obj.getBoundingBox();

           // If classification was enabled:
           int category = obj.getClassificationCategory();
           Float confidence = obj.getClassificationConfidence();
       }

   ### Kotlin

       // The list of detected objects contains one item if multiple object detection wasn't enabled.
       for (obj in detectedObjects) {
           val id = obj.trackingId       // A number that identifies the object across images
           val bounds = obj.boundingBox  // The object's position in the image

           // If classification was enabled:
           val category = obj.classificationCategory
           val confidence = obj.classificationConfidence
       }

## Improving usability and performance

For the best user experience, follow these guidelines in your app:

- Successful object detection depends on the object's visual complexity. Objects with a small number of visual features might need to take up a larger part of the image to be detected. You should provide users with guidance on capturing input that works well with the kind of objects you want to detect.
- When using classification, if you want to detect objects that don't fall cleanly into the supported categories, implement special handling for unknown objects.

Also, check out the
\[ML Kit Material Design showcase app\]\[showcase-link\]{: .external } and the
Material Design
[Patterns for machine learning-powered features](https://material.io/collections/machine-learning/) collection.

When using streaming mode in a real-time application, follow these guidelines to
achieve the best framerates:

- Don't use multiple object detection in streaming mode, as most devices won't
  be able to produce adequate framerates.

- Disable classification if you don't need it.

- Throttle calls to the detector. If a new video frame becomes available while the detector is running, drop the frame.
- If you are using the output of the detector to overlay graphics on the input image, first get the result from ML Kit, then render the image and overlay in a single step. By doing so, you render to the display surface only once for each input frame.
- If you use the Camera2 API, capture images in
  `ImageFormat.YUV_420_888` format.

  If you use the older Camera API, capture images in
  `ImageFormat.NV21` format.