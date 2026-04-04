# Source: https://firebase.google.com/docs/ml-kit/android/detect-faces.md.txt

> [!CAUTION]
> This page describes an old version of the Face Detection API, which was part
> of ML Kit for Firebase. Development of this API has been moved to the
> standalone ML Kit SDK, which you can use with or without Firebase.
> [Learn more](https://developers.google.com/ml-kit/migration).
>
> See
> [Detect faces with ML Kit on Android](https://developers.google.com/ml-kit/vision/face-detection/android)
> for the latest documentation.


You can use ML Kit to detect faces in images and video.

## Before you begin

1. If you haven't already, [add Firebase to your Android project](https://firebase.google.com/docs/android/setup).
2. Add the dependencies for the ML Kit Android libraries to your module (app-level) Gradle file (usually `app/build.gradle`):

   ```
   apply plugin: 'com.android.application'
   apply plugin: 'com.google.gms.google-services'

   dependencies {
     // ...

     implementation 'com.google.firebase:firebase-ml-vision:24.0.3'
     // If you want to detect face contours (landmark detection and classification
     // don't require this additional model):
     implementation 'com.google.firebase:firebase-ml-vision-face-model:20.0.1'
   }
   ```
3. **Optional but recommended** : Configure your app to automatically download the ML model to the device after your app is installed from the Play Store.

   To do so, add the following declaration to your app's
   `AndroidManifest.xml` file:

   ```
   <application ...>
     ...
     <meta-data
         android:name="com.google.firebase.ml.vision.DEPENDENCIES"
         android:value="face" />
     <!-- To use multiple models: android:value="face,model2,model3" -->
   </application>
   ```
   If you do not enable install-time model downloads, the model will be downloaded the first time you run the detector. Requests you make before the download has completed will produce no results.

## Input image guidelines

For ML Kit to accurately detect faces, input images must contain faces
that are represented by sufficient pixel data. In general, each face you want
to detect in an image should be at least 100x100 pixels. If you want to detect
the contours of faces, ML Kit requires higher resolution input: each face
should be at least 200x200 pixels.

If you are detecting faces in a real-time application, you might also want
to consider the overall dimensions of the input images. Smaller images can be
processed faster, so to reduce latency, capture images at lower resolutions
(keeping in mind the above accuracy requirements) and ensure that the
subject's face occupies as much of the image as possible. Also see
[Tips to improve real-time performance](https://firebase.google.com/docs/ml-kit/android/detect-faces#performance_tips).

Poor image focus can hurt accuracy. If you aren't getting acceptable results,
try asking the user to recapture the image.

The orientation of a face relative to the camera can also affect what facial
features ML Kit detects. See
[Face Detection
Concepts](https://firebase.google.com/docs/ml-kit/face-detection-concepts#landmarks).

## 1. Configure the face detector

Before you apply face detection to an image, if you want to change any of the face detector's default settings, specify those settings with a [`FirebaseVisionFaceDetectorOptions`](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetectorOptions.Builder) object. You can change the following settings:

<br />

| Settings ||
|---|---|
| Performance mode | `FAST` (default) \| `ACCURATE` Favor speed or accuracy when detecting faces. |
| Detect landmarks | `NO_LANDMARKS` (default) \| `ALL_LANDMARKS` Whether to attempt to identify facial "landmarks": eyes, ears, nose, cheeks, mouth, and so on. |
| Detect contours | `NO_CONTOURS` (default) \| `ALL_CONTOURS` Whether to detect the contours of facial features. Contours are detected for only the most prominent face in an image. |
| Classify faces | `NO_CLASSIFICATIONS` (default) \| `ALL_CLASSIFICATIONS` Whether or not to classify faces into categories such as "smiling", and "eyes open". |
| Minimum face size | `float` (default: `0.1f`) The minimum size, relative to the image, of faces to detect. |
| Enable face tracking | `false` (default) \| `true` Whether or not to assign faces an ID, which can be used to track faces across images. Note that when contour detection is enabled, only one face is detected, so face tracking doesn't produce useful results. For this reason, and to improve detection speed, don't enable both contour detection and face tracking. |

For example:

### Java

```java
// High-accuracy landmark detection and face classification
FirebaseVisionFaceDetectorOptions highAccuracyOpts =
        new FirebaseVisionFaceDetectorOptions.Builder()
                .setPerformanceMode(FirebaseVisionFaceDetectorOptions.ACCURATE)
                .setLandmarkMode(FirebaseVisionFaceDetectorOptions.ALL_LANDMARKS)
                .setClassificationMode(FirebaseVisionFaceDetectorOptions.ALL_CLASSIFICATIONS)
                .build();

// Real-time contour detection of multiple faces
FirebaseVisionFaceDetectorOptions realTimeOpts =
        new FirebaseVisionFaceDetectorOptions.Builder()
                .setContourMode(FirebaseVisionFaceDetectorOptions.ALL_CONTOURS)
                .build();
```

### Kotlin

```kotlin
// High-accuracy landmark detection and face classification
val highAccuracyOpts = FirebaseVisionFaceDetectorOptions.Builder()
        .setPerformanceMode(FirebaseVisionFaceDetectorOptions.ACCURATE)
        .setLandmarkMode(FirebaseVisionFaceDetectorOptions.ALL_LANDMARKS)
        .setClassificationMode(FirebaseVisionFaceDetectorOptions.ALL_CLASSIFICATIONS)
        .build()

// Real-time contour detection of multiple faces
val realTimeOpts = FirebaseVisionFaceDetectorOptions.Builder()
        .setContourMode(FirebaseVisionFaceDetectorOptions.ALL_CONTOURS)
        .build()
```

## 2. Run the face detector

To detect faces in an image, create a `FirebaseVisionImage` object from either a `Bitmap`, `media.Image`, `ByteBuffer`, byte array, or a file on the device. Then, pass the `FirebaseVisionImage` object to the `FirebaseVisionFaceDetector`'s `detectInImage` method.

<br />

For face recognition, you should use an image with dimensions of at least
**480x360** pixels. If you are recognizing faces in real time, capturing frames
at this minimum resolution can help reduce latency.

1. Create a [`FirebaseVisionImage`](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage) object from your
   image.

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
2. Get an instance of [`FirebaseVisionFaceDetector`](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetector):

   ### Java

   ```java
   FirebaseVisionFaceDetector detector = FirebaseVision.getInstance()
           .getVisionFaceDetector(options);
   ```

   ### Kotlin

   ```kotlin
   val detector = FirebaseVision.getInstance()
           .getVisionFaceDetector(options)
   ```

   > [!NOTE]
   > **Note:** Check the console for errors generated by the constructor.

3. Finally, pass the image to the `detectInImage` method:

   ### Java

   ```java
   Task<List<FirebaseVisionFace>> result =
           detector.detectInImage(image)
                   .addOnSuccessListener(
                           new OnSuccessListener<List<FirebaseVisionFace>>() {
                               @Override
                               public void onSuccess(List<FirebaseVisionFace> faces) {
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
   ```

   ### Kotlin

   ```kotlin
   val result = detector.detectInImage(image)
           .addOnSuccessListener { faces ->
               // Task completed successfully
               // ...
           }
           .addOnFailureListener { e ->
               // Task failed with an exception
               // ...
           }
   ```

   > [!NOTE]
   > **Note:** Check the console for errors generated by the detector.

## 3. Get information about detected faces

If the face recognition operation succeeds, a list of [`FirebaseVisionFace`](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFace) objects will be passed to the success listener. Each `FirebaseVisionFace` object represents a face that was detected in the image. For each face, you can get its bounding coordinates in the input image, as well as any other information you configured the face detector to find. For example:

<br />

### Java

```java
for (FirebaseVisionFace face : faces) {
    Rect bounds = face.getBoundingBox();
    float rotY = face.getHeadEulerAngleY();  // Head is rotated to the right rotY degrees
    float rotZ = face.getHeadEulerAngleZ();  // Head is tilted sideways rotZ degrees

    // If landmark detection was enabled (mouth, ears, eyes, cheeks, and
    // nose available):
    FirebaseVisionFaceLandmark leftEar = face.getLandmark(FirebaseVisionFaceLandmark.LEFT_EAR);
    if (leftEar != null) {
        FirebaseVisionPoint leftEarPos = leftEar.getPosition();
    }

    // If contour detection was enabled:
    List<FirebaseVisionPoint> leftEyeContour =
            face.getContour(FirebaseVisionFaceContour.LEFT_EYE).getPoints();
    List<FirebaseVisionPoint> upperLipBottomContour =
            face.getContour(FirebaseVisionFaceContour.UPPER_LIP_BOTTOM).getPoints();

    // If classification was enabled:
    if (face.getSmilingProbability() != FirebaseVisionFace.UNCOMPUTED_PROBABILITY) {
        float smileProb = face.getSmilingProbability();
    }
    if (face.getRightEyeOpenProbability() != FirebaseVisionFace.UNCOMPUTED_PROBABILITY) {
        float rightEyeOpenProb = face.getRightEyeOpenProbability();
    }

    // If face tracking was enabled:
    if (face.getTrackingId() != FirebaseVisionFace.INVALID_ID) {
        int id = face.getTrackingId();
    }
}
```

### Kotlin

```kotlin
for (face in faces) {
    val bounds = face.boundingBox
    val rotY = face.headEulerAngleY // Head is rotated to the right rotY degrees
    val rotZ = face.headEulerAngleZ // Head is tilted sideways rotZ degrees

    // If landmark detection was enabled (mouth, ears, eyes, cheeks, and
    // nose available):
    val leftEar = face.getLandmark(FirebaseVisionFaceLandmark.LEFT_EAR)
    leftEar?.let {
        val leftEarPos = leftEar.position
    }

    // If contour detection was enabled:
    val leftEyeContour = face.getContour(FirebaseVisionFaceContour.LEFT_EYE).points
    val upperLipBottomContour = face.getContour(FirebaseVisionFaceContour.UPPER_LIP_BOTTOM).points

    // If classification was enabled:
    if (face.smilingProbability != FirebaseVisionFace.UNCOMPUTED_PROBABILITY) {
        val smileProb = face.smilingProbability
    }
    if (face.rightEyeOpenProbability != FirebaseVisionFace.UNCOMPUTED_PROBABILITY) {
        val rightEyeOpenProb = face.rightEyeOpenProbability
    }

    // If face tracking was enabled:
    if (face.trackingId != FirebaseVisionFace.INVALID_ID) {
        val id = face.trackingId
    }
}
```

### Example of face contours

When you have face contour detection enabled, you get a list of points for
each facial feature that was detected. These points represent the shape of the
feature. See the [Face
Detection Concepts Overview](https://firebase.google.com/docs/ml-kit/face-detection-concepts#contours) for details about how contours are
represented.

The following image illustrates how these points map to a face (click the
image to enlarge):
[![](https://firebase.google.com/static/docs/ml-kit/images/examples/face_contours.svg)](https://firebase.google.com/static/docs/ml-kit/images/examples/face_contours.svg)

## Real-time face detection

If you want to use face detection in a real-time application, follow these
guidelines to achieve the best framerates:

- [Configure the face detector](https://firebase.google.com/docs/ml-kit/android/detect-faces#1-configure-the-face-detector) to use either
  face contour detection or classification and landmark detection, but not both:

  Contour detection  

  Landmark detection  

  Classification  

  Landmark detection and classification  

  Contour detection and landmark detection  

  Contour detection and classification  

  Contour detection, landmark detection, and classification  
- Enable `FAST` mode (enabled by default).

- Consider capturing images at a lower resolution. However, also keep in mind
  this API's image dimension requirements.

- Throttle calls to the detector. If a new video frame becomes available while the detector is running, drop the frame.
- If you are using the output of the detector to overlay graphics on the input image, first get the result from ML Kit, then render the image and overlay in a single step. By doing so, you render to the display surface only once for each input frame.
- If you use the Camera2 API, capture images in
  `ImageFormat.YUV_420_888` format.

  If you use the older Camera API, capture images in
  `ImageFormat.NV21` format.