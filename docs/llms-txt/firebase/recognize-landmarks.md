# Source: https://firebase.google.com/docs/ml/recognize-landmarks.md.txt

# Source: https://firebase.google.com/docs/ml/android/recognize-landmarks.md.txt

# Source: https://firebase.google.com/docs/ml-kit/recognize-landmarks.md.txt

# Source: https://firebase.google.com/docs/ml/ios/recognize-landmarks.md.txt

# Source: https://firebase.google.com/docs/ml-kit/ios/recognize-landmarks.md.txt

# Source: https://firebase.google.com/docs/ml-kit/android/recognize-landmarks.md.txt

| This page is about an old version of the Landmark Recognition API, which was part of ML Kit for Firebase. For the latest docs, see[the latest version](https://firebase.google.com/docs/ml/android/recognize-landmarks)in theFirebase MLsection.

<br />

You can use ML Kit to recognize well-known landmarks in an image.
| Use of ML Kit to access Cloud ML functionality is subject to the[Google Cloud Platform License Agreement](https://cloud.google.com/terms/)and[Service Specific Terms](https://cloud.google.com/terms/service-terms), and billed accordingly. For billing information, see the Firebase[Pricing](https://firebase.google.com/pricing)page.

<br />

## Before you begin

1. If you haven't already,[add Firebase to your Android project](https://firebase.google.com/docs/android/setup).
2. Add the dependencies for the ML Kit Android libraries to your module (app-level) Gradle file (usually`app/build.gradle`):  

   ```carbon
   apply plugin: 'com.android.application'
   apply plugin: 'com.google.gms.google-services'

   dependencies {
     // ...

     implementation 'com.google.firebase:firebase-ml-vision:24.0.3'
   }
   ```
3. If you have not already enabled Cloud-based APIs for your project, do so now:

   1. Open the[ML Kit APIs page](https://console.firebase.google.com/project/_/ml/apis)of theFirebaseconsole.
   2. If you have not already upgraded your project to a Blaze pricing plan, click**Upgrade**to do so. (You will be prompted to upgrade only if your project isn't on the Blaze plan.)

      Only Blaze-level projects can use Cloud-based APIs.
   3. If Cloud-based APIs aren't already enabled, click**Enable Cloud-based APIs**.

   | Before you deploy to production an app that uses a Cloud API, you should take some additional steps to[prevent and mitigate the effect of unauthorized API access](https://firebase.google.com/docs/ml-kit/android/secure-api-key).

## Configure the landmark detector

By default, the Cloud detector uses the`STABLE`version of the model and returns up to 10 results. If you want to change either of these settings, specify them with a[`FirebaseVisionCloudDetectorOptions`](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/FirebaseVisionCloudDetectorOptions.Builder)object.

For example, to change both of the default settings, build a`FirebaseVisionCloudDetectorOptions`object as in the following example:  

### Java

```java
FirebaseVisionCloudDetectorOptions options =
        new FirebaseVisionCloudDetectorOptions.Builder()
                .setModelType(FirebaseVisionCloudDetectorOptions.LATEST_MODEL)
                .setMaxResults(15)
                .build();https://github.com/firebase/snippets-android/blob/e69640da6af8999c7650b5f01297d92f88da115a/mlkit/app/src/main/java/com/google/firebase/example/mlkit/MainActivity.java#L17-L21
```

### Kotlin

```kotlin
val options = FirebaseVisionCloudDetectorOptions.Builder()
        .setModelType(FirebaseVisionCloudDetectorOptions.LATEST_MODEL)
        .setMaxResults(15)
        .build()https://github.com/firebase/snippets-android/blob/e69640da6af8999c7650b5f01297d92f88da115a/mlkit/app/src/main/java/com/google/firebase/example/mlkit/kotlin/MainActivity.kt#L15-L18
```

To use the default settings, you can use`FirebaseVisionCloudDetectorOptions.DEFAULT`in the next step.

## Run the landmark detector

To recognize landmarks in an image, create a`FirebaseVisionImage`object from either a`Bitmap`,`media.Image`,`ByteBuffer`, byte array, or a file on the device. Then, pass the`FirebaseVisionImage`object to the`FirebaseVisionCloudLandmarkDetector`'s`detectInImage`method.

<br />

1. Create a[`FirebaseVisionImage`](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage)object from your image.

   - To create a`FirebaseVisionImage`object from a`media.Image`object, such as when capturing an image from a device's camera, pass the`media.Image`object and the image's rotation to`FirebaseVisionImage.fromMediaImage()`.

     If you use the[CameraX](https://developer.android.com/training/camerax)library, the`OnImageCapturedListener`and`ImageAnalysis.Analyzer`classes calculate the rotation value for you, so you just need to convert the rotation to one of ML Kit's`ROTATION_`constants before calling`FirebaseVisionImage.fromMediaImage()`:  

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

     If you don't use a camera library that gives you the image's rotation, you can calculate it from the device's rotation and the orientation of camera sensor in the device:  

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
     }https://github.com/firebase/snippets-android/blob/e69640da6af8999c7650b5f01297d92f88da115a/mlkit/app/src/main/java/com/google/firebase/example/mlkit/VisionImage.java#L81-L131
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
     }https://github.com/firebase/snippets-android/blob/e69640da6af8999c7650b5f01297d92f88da115a/mlkit/app/src/main/java/com/google/firebase/example/mlkit/kotlin/VisionImage.kt#L75-L110
     ```

     Then, pass the`media.Image`object and the rotation value to`FirebaseVisionImage.fromMediaImage()`:  

     ### Java

     ```java
     FirebaseVisionImage image = FirebaseVisionImage.fromMediaImage(mediaImage, rotation);https://github.com/firebase/snippets-android/blob/e69640da6af8999c7650b5f01297d92f88da115a/mlkit/app/src/main/java/com/google/firebase/example/mlkit/VisionImage.java#L39-L39
     ```

     ### Kotlin

     ```kotlin
     val image = FirebaseVisionImage.fromMediaImage(mediaImage, rotation)https://github.com/firebase/snippets-android/blob/e69640da6af8999c7650b5f01297d92f88da115a/mlkit/app/src/main/java/com/google/firebase/example/mlkit/kotlin/VisionImage.kt#L33-L33
     ```
   - To create a`FirebaseVisionImage`object from a file URI, pass the app context and file URI to`FirebaseVisionImage.fromFilePath()`. This is useful when you use an`ACTION_GET_CONTENT`intent to prompt the user to select an image from their gallery app.  

     ### Java

     ```java
     FirebaseVisionImage image;
     try {
         image = FirebaseVisionImage.fromFilePath(context, uri);
     } catch (IOException e) {
         e.printStackTrace();
     }https://github.com/firebase/snippets-android/blob/e69640da6af8999c7650b5f01297d92f88da115a/mlkit/app/src/main/java/com/google/firebase/example/mlkit/VisionImage.java#L71-L76
     ```

     ### Kotlin

     ```kotlin
     val image: FirebaseVisionImage
     try {
         image = FirebaseVisionImage.fromFilePath(context, uri)
     } catch (e: IOException) {
         e.printStackTrace()
     }https://github.com/firebase/snippets-android/blob/e69640da6af8999c7650b5f01297d92f88da115a/mlkit/app/src/main/java/com/google/firebase/example/mlkit/kotlin/VisionImage.kt#L65-L70
     ```
   - To create a`FirebaseVisionImage`object from a`ByteBuffer`or a byte array, first calculate the image rotation as described above for`media.Image`input.

     Then, create a`FirebaseVisionImageMetadata`object that contains the image's height, width, color encoding format, and rotation:  

     ### Java

     ```java
     FirebaseVisionImageMetadata metadata = new FirebaseVisionImageMetadata.Builder()
             .setWidth(480)   // 480x360 is typically sufficient for
             .setHeight(360)  // image recognition
             .setFormat(FirebaseVisionImageMetadata.IMAGE_FORMAT_NV21)
             .setRotation(rotation)
             .build();https://github.com/firebase/snippets-android/blob/e69640da6af8999c7650b5f01297d92f88da115a/mlkit/app/src/main/java/com/google/firebase/example/mlkit/VisionImage.java#L45-L50
     ```

     ### Kotlin

     ```kotlin
     val metadata = FirebaseVisionImageMetadata.Builder()
             .setWidth(480) // 480x360 is typically sufficient for
             .setHeight(360) // image recognition
             .setFormat(FirebaseVisionImageMetadata.IMAGE_FORMAT_NV21)
             .setRotation(rotation)
             .build()https://github.com/firebase/snippets-android/blob/e69640da6af8999c7650b5f01297d92f88da115a/mlkit/app/src/main/java/com/google/firebase/example/mlkit/kotlin/VisionImage.kt#L39-L44
     ```

     Use the buffer or array, and the metadata object, to create a`FirebaseVisionImage`object:  

     ### Java

     ```java
     FirebaseVisionImage image = FirebaseVisionImage.fromByteBuffer(buffer, metadata);
     // Or: FirebaseVisionImage image = FirebaseVisionImage.fromByteArray(byteArray, metadata);  
     https://github.com/firebase/snippets-android/blob/e69640da6af8999c7650b5f01297d92f88da115a/mlkit/app/src/main/java/com/google/firebase/example/mlkit/VisionImage.java#L65-L65
     ```

     ### Kotlin

     ```kotlin
     val image = FirebaseVisionImage.fromByteBuffer(buffer, metadata)
     // Or: val image = FirebaseVisionImage.fromByteArray(byteArray, metadata)  
     https://github.com/firebase/snippets-android/blob/e69640da6af8999c7650b5f01297d92f88da115a/mlkit/app/src/main/java/com/google/firebase/example/mlkit/kotlin/VisionImage.kt#L59-L59
     ```
   - To create a`FirebaseVisionImage`object from a`Bitmap`object:  

     ### Java

     ```java
     FirebaseVisionImage image = FirebaseVisionImage.fromBitmap(bitmap);https://github.com/firebase/snippets-android/blob/e69640da6af8999c7650b5f01297d92f88da115a/mlkit/app/src/main/java/com/google/firebase/example/mlkit/VisionImage.java#L32-L32
     ```

     ### Kotlin

     ```kotlin
     val image = FirebaseVisionImage.fromBitmap(bitmap)https://github.com/firebase/snippets-android/blob/e69640da6af8999c7650b5f01297d92f88da115a/mlkit/app/src/main/java/com/google/firebase/example/mlkit/kotlin/VisionImage.kt#L26-L26
     ```
     The image represented by the`Bitmap`object must be upright, with no additional rotation required.

   <br />

2. Get an instance of[`FirebaseVisionCloudLandmarkDetector`](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/landmark/FirebaseVisionCloudLandmarkDetector):

   ### Java

   ```java
   FirebaseVisionCloudLandmarkDetector detector = FirebaseVision.getInstance()
           .getVisionCloudLandmarkDetector();
   // Or, to change the default settings:
   // FirebaseVisionCloudLandmarkDetector detector = FirebaseVision.getInstance()
   //         .getVisionCloudLandmarkDetector(options);
   ```

   ### Kotlin

   ```kotlin
   val detector = FirebaseVision.getInstance()
           .visionCloudLandmarkDetector
   // Or, to change the default settings:
   // val detector = FirebaseVision.getInstance()
   //         .getVisionCloudLandmarkDetector(options)
   ```
3. Finally, pass the image to the`detectInImage`method:

   ### Java

   ```java
   Task<List<FirebaseVisionCloudLandmark>> result = detector.detectInImage(image)
           .addOnSuccessListener(new OnSuccessListener<List<FirebaseVisionCloudLandmark>>() {
               @Override
               public void onSuccess(List<FirebaseVisionCloudLandmark> firebaseVisionCloudLandmarks) {
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
   ```

   ### Kotlin

   ```kotlin
   val result = detector.detectInImage(image)
           .addOnSuccessListener { firebaseVisionCloudLandmarks ->
               // Task completed successfully
               // ...
           }
           .addOnFailureListener { e ->
               // Task failed with an exception
               // ...
           }
   ```

## Get information about the recognized landmarks

If the landmark recognition operation succeeds, a list of[`FirebaseVisionCloudLandmark`](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/landmark/FirebaseVisionCloudLandmark)objects will be passed to the success listener. Each`FirebaseVisionCloudLandmark`object represents a landmark that was recognized in the image. For each landmark, you can get its bounding coordinates in the input image, the landmark's name, its latitude and longitude, its[Knowledge Graph entity ID](https://developers.google.com/knowledge-graph/)(if available), and the confidence score of the match. For example:

<br />

### Java

```java
for (FirebaseVisionCloudLandmark landmark: firebaseVisionCloudLandmarks) {

    Rect bounds = landmark.getBoundingBox();
    String landmarkName = landmark.getLandmark();
    String entityId = landmark.getEntityId();
    float confidence = landmark.getConfidence();

    // Multiple locations are possible, e.g., the location of the depicted
    // landmark and the location the picture was taken.
    for (FirebaseVisionLatLng loc: landmark.getLocations()) {
        double latitude = loc.getLatitude();
        double longitude = loc.getLongitude();
    }
}
```

### Kotlin

```kotlin
for (landmark in firebaseVisionCloudLandmarks) {

    val bounds = landmark.boundingBox
    val landmarkName = landmark.landmark
    val entityId = landmark.entityId
    val confidence = landmark.confidence

    // Multiple locations are possible, e.g., the location of the depicted
    // landmark and the location the picture was taken.
    for (loc in landmark.locations) {
        val latitude = loc.latitude
        val longitude = loc.longitude
    }
}
```

## Next steps

- Before you deploy to production an app that uses a Cloud API, you should take some additional steps to[prevent and mitigate the effect of unauthorized API access](https://firebase.google.com/docs/ml-kit/android/secure-api-key).