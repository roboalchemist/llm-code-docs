# Source: https://firebase.google.com/docs/ml/android/label-images-deprecated.md.txt

> [!CAUTION]
> This page describes an old version of labeling objects recognized in an image using the
> deprecated Firebase ML Vision SDK. As an alternative, you may
> [call
> Cloud Vision APIs using Firebase Auth and Callable Functions](https://firebase.google.com/docs/ml/android/label-images) to allow only users logged
> into your app to access the API.

You can use Firebase ML to label objects recognized in an image. See the
[overview](https://firebase.google.com/docs/ml/label-images) for information about this API's
features.
Use of the Cloud Vision APIs is subject to the [Google Cloud Platform License
Agreement](https://cloud.google.com/terms/) and [Service
Specific Terms](https://cloud.google.com/terms/service-terms), and billed accordingly. For billing information, see the [Pricing](https://cloud.google.com/vision/pricing) page.

> [!NOTE]
> **Looking for on-device image labeling?** Try the [standalone ML Kit library](https://developers.google.com/ml-kit/vision/image-labeling).

<br />

## Before you begin

1. If you haven't already, [add Firebase to your Android project](https://firebase.google.com/docs/android/setup).
2. In your **module (app-level) Gradle file** (usually `<project>/<app-module>/build.gradle.kts` or `<project>/<app-module>/build.gradle`), add the dependency for the Firebase ML Vision library for Android. We recommend using the [Firebase Android BoM](https://firebase.google.com/docs/android/learn-more#bom) to control library versioning.

   ```
   dependencies {
       // Import the BoM for the Firebase platform
       implementation(platform("com.google.firebase:firebase-bom:34.10.0"))

       // Add the dependency for the Firebase ML Vision library
       // When using the BoM, you don't specify versions in Firebase library dependencies
       implementation 'com.google.firebase:firebase-ml-vision'
   }
   ```

   By using the [Firebase Android BoM](https://firebase.google.com/docs/android/learn-more#bom),
   your app will always use compatible versions of Firebase Android libraries.
   *(Alternative)*
   Add Firebase library dependencies *without* using the BoM

   If you choose not to use the Firebase BoM, you must specify each Firebase library version
   in its dependency line.

   **Note that if you use *multiple* Firebase libraries in your app, we strongly
   recommend using the BoM to manage library versions, which ensures that all versions are
   compatible.**

   ```groovy
   dependencies {
       // Add the dependency for the Firebase ML Vision library
       // When NOT using the BoM, you must specify versions in Firebase library dependencies
       implementation 'com.google.firebase:firebase-ml-vision:24.1.0'
   }
   ```
3. If you haven't already enabled Cloud-based APIs for your project, do so
   now:

   1. Open the [Firebase ML
      APIs page](https://console.firebase.google.com/project/_/ml/apis) in the Firebase console.
   2. If you haven't already upgraded your project to the
      [pay-as-you-go Blaze pricing plan](https://firebase.google.com/pricing), click **Upgrade** to do so. (You'll be
      prompted to upgrade only if your project isn't on the
      Blaze pricing plan.)

      Only projects on the Blaze pricing plan can use
      Cloud-based APIs.
   3. If Cloud-based APIs aren't already enabled, click **Enable Cloud-based APIs**.

   Before you deploy to production an app that uses a Cloud API, you should take some additional steps to [prevent and mitigate the
   effect of unauthorized API access](https://firebase.google.com/docs/ml/android/secure-api-key).

Now you are ready to label images.

## 1. Prepare the input image

Create a [`FirebaseVisionImage`](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage) object from your image. The image labeler runs fastest when you use a `Bitmap` or, if you use the camera2 API, a JPEG-formatted `media.Image`, which are recommended when possible.

<br />

-
  To create a `FirebaseVisionImage` object from a
  `media.Image` object, such as when capturing an image from a
  device's camera, pass the `media.Image` object and the image's
  rotation to `FirebaseVisionImage.fromMediaImage()`.


  If you use the
  [CameraX](https://developer.android.com/training/camerax) library, the `OnImageCapturedListener` and
  `ImageAnalysis.Analyzer` classes calculate the rotation value
  for you, so you just need to convert the rotation to one of Firebase ML's
  `ROTATION_` constants before calling
  `FirebaseVisionImage.fromMediaImage()`:

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
              // Pass image to an ML Vision API
              // ...
          }
      }
  }
  ```

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
          // Pass image to an ML Vision API
          // ...
      }
  }
  ```


  If you don't use a camera library that gives you the image's rotation, you
  can calculate it from the device's rotation and the orientation of camera
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
  rotation value to `FirebaseVisionImage.fromMediaImage()`:

  ### Kotlin

  ```kotlin
  val image = FirebaseVisionImage.fromMediaImage(mediaImage, rotation)
  ```

  ### Java

  ```java
  FirebaseVisionImage image = FirebaseVisionImage.fromMediaImage(mediaImage, rotation);
  ```
- To create a `FirebaseVisionImage` object from a file URI, pass the app context and file URI to `FirebaseVisionImage.fromFilePath()`. This is useful when you use an `ACTION_GET_CONTENT` intent to prompt the user to select an image from their gallery app.

  ### Kotlin

  ```kotlin
  val image: FirebaseVisionImage
  try {
      image = FirebaseVisionImage.fromFilePath(context, uri)
  } catch (e: IOException) {
      e.printStackTrace()
  }
  ```

  ### Java

  ```java
  FirebaseVisionImage image;
  try {
      image = FirebaseVisionImage.fromFilePath(context, uri);
  } catch (IOException e) {
      e.printStackTrace();
  }
  ```
- To create a `FirebaseVisionImage` object from a `ByteBuffer` or a byte array, first calculate the image rotation as described above for `media.Image` input.

  Then, create a `FirebaseVisionImageMetadata` object
  that contains the image's height, width, color encoding format,
  and rotation:

  ### Kotlin

  ```kotlin
  val metadata = FirebaseVisionImageMetadata.Builder()
      .setWidth(480) // 480x360 is typically sufficient for
      .setHeight(360) // image recognition
      .setFormat(FirebaseVisionImageMetadata.IMAGE_FORMAT_NV21)
      .setRotation(rotation)
      .build()
  ```

  ### Java

  ```java
  FirebaseVisionImageMetadata metadata = new FirebaseVisionImageMetadata.Builder()
          .setWidth(480)   // 480x360 is typically sufficient for
          .setHeight(360)  // image recognition
          .setFormat(FirebaseVisionImageMetadata.IMAGE_FORMAT_NV21)
          .setRotation(rotation)
          .build();
  ```

  Use the buffer or array, and the metadata object, to create a
  `FirebaseVisionImage` object:

  ### Kotlin

  ```kotlin
  val image = FirebaseVisionImage.fromByteBuffer(buffer, metadata)
  // Or: val image = FirebaseVisionImage.fromByteArray(byteArray, metadata)https://github.com/firebase/snippets-android/blob/a413b0658ff2fc7a72c4b0c59e84a889ff7fac45/mlkit/app/src/main/java/com/google/firebase/example/mlkit/kotlin/VisionImage.kt#L59-L59
  ```

  ### Java

  ```java
  FirebaseVisionImage image = FirebaseVisionImage.fromByteBuffer(buffer, metadata);
  // Or: FirebaseVisionImage image = FirebaseVisionImage.fromByteArray(byteArray, metadata);https://github.com/firebase/snippets-android/blob/a413b0658ff2fc7a72c4b0c59e84a889ff7fac45/mlkit/app/src/main/java/com/google/firebase/example/mlkit/VisionImage.java#L65-L65
  ```
- To create a `FirebaseVisionImage` object from a `Bitmap` object:

  ### Kotlin

  ```kotlin
  val image = FirebaseVisionImage.fromBitmap(bitmap)
  ```

  ### Java

  ```java
  FirebaseVisionImage image = FirebaseVisionImage.fromBitmap(bitmap);
  ```
  The image represented by the `Bitmap` object must be upright, with no additional rotation required.

## 2. Configure and run the image labeler

To label objects in an image, pass the `FirebaseVisionImage` object to the `FirebaseVisionImageLabeler`'s `processImage` method.

<br />

1. First, get an instance of
   [`FirebaseVisionImageLabeler`](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionLabelDetector).

   ### Kotlin

       val labeler = FirebaseVision.getInstance().getCloudImageLabeler()

       // Or, to set the minimum confidence required:
       // val options = FirebaseVisionCloudImageLabelerOptions.Builder()
       //     .setConfidenceThreshold(0.7f)
       //     .build()
       // val labeler = FirebaseVision.getInstance().getCloudImageLabeler(options)

   <br />

   ### Java

       FirebaseVisionImageLabeler labeler = FirebaseVision.getInstance()
           .getCloudImageLabeler();

       // Or, to set the minimum confidence required:
       // FirebaseVisionCloudImageLabelerOptions options =
       //     new FirebaseVisionCloudImageLabelerOptions.Builder()
       //         .setConfidenceThreshold(0.7f)
       //         .build();
       // FirebaseVisionImageLabeler labeler = FirebaseVision.getInstance()
       //     .getCloudImageLabeler(options);

   <br />

2. Then, pass the image to the `processImage()` method:

   ### Kotlin

       labeler.processImage(image)
           .addOnSuccessListener { labels ->
             // Task completed successfully
             // ...
           }
           .addOnFailureListener { e ->
             // Task failed with an exception
             // ...
           }

   <br />

   ### Java

       labeler.processImage(image)
           .addOnSuccessListener(new OnSuccessListener<List<FirebaseVisionImageLabel>>() {
             @Override
             public void onSuccess(List<FirebaseVisionImageLabel> labels) {
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

   <br />

## 3. Get information about labeled objects

If the image labeling operation succeeds, a list of [`FirebaseVisionImageLabel`](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionLabel) objects will be passed to the success listener. Each `FirebaseVisionImageLabel` object represents something that was labeled in the image. For each label, you can get the label's text description, its [Knowledge Graph entity ID](https://developers.google.com/knowledge-graph/) (if available), and the confidence score of the match. For example:

<br />

### Kotlin

    for (label in labels) {
      val text = label.text
      val entityId = label.entityId
      val confidence = label.confidence
    }

<br />

### Java

    for (FirebaseVisionImageLabel label: labels) {
      String text = label.getText();
      String entityId = label.getEntityId();
      float confidence = label.getConfidence();
    }

<br />

## Next steps

- Before you deploy to production an app that uses a Cloud API, you should take some additional steps to [prevent and mitigate the
  effect of unauthorized API access](https://firebase.google.com/docs/ml/android/secure-api-key).