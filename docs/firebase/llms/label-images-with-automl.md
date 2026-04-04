# Source: https://firebase.google.com/docs/ml/android/label-images-with-automl.md.txt

# Source: https://firebase.google.com/docs/ml-kit/ios/label-images-with-automl.md.txt

# Source: https://firebase.google.com/docs/ml/ios/label-images-with-automl.md.txt

# Source: https://firebase.google.com/docs/ml-kit/android/label-images-with-automl.md.txt

| This page describes an old version of the AutoML Vision Edge API, which was part of ML Kit for Firebase. Development of this API has been moved to the standalone ML Kit SDK, which you can use with or without Firebase.[Learn more](https://developers.google.com/ml-kit/migration).
|
| See[Label images with an AutoML-trained model on Android](https://developers.google.com/ml-kit/vision/auto-ml-vision-edge/android)for the latest documentation.

<br />

After you[train your own model using AutoML Vision Edge](https://firebase.google.com/docs/ml-kit/train-image-labeler), you can use it in your app to label images.

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
     implementation 'com.google.firebase:firebase-ml-vision-automl:18.0.5'
   }
   ```

## 1. Load the model

ML Kit runs your AutoML-generated models on the device. However, you can configure ML Kit to load your model either remotely from Firebase, from local storage, or both.

By hosting the model on Firebase, you can update the model without releasing a new app version, and you can useRemote ConfigandA/B Testingto dynamically serve different models to different sets of users.

If you choose to only provide the model by hosting it with Firebase, and not bundle it with your app, you can reduce the initial download size of your app. Keep in mind, though, that if the model is not bundled with your app, any model-related functionality will not be available until your app downloads the model for the first time.

By bundling your model with your app, you can ensure your app's ML features still work when the Firebase-hosted model isn't available.

### Configure a Firebase-hosted model source

To use the remotely-hosted model, create a`FirebaseAutoMLRemoteModel`object, specifying the name you assigned the model when you published it:  

### Java

    // Specify the name you assigned in the Firebase console.
    FirebaseAutoMLRemoteModel remoteModel =
        new FirebaseAutoMLRemoteModel.Builder("your_remote_model").build();

### Kotlin

    // Specify the name you assigned in the Firebase console.
    val remoteModel = FirebaseAutoMLRemoteModel.Builder("your_remote_model").build()

Then, start the model download task, specifying the conditions under which you want to allow downloading. If the model isn't on the device, or if a newer version of the model is available, the task will asynchronously download the model from Firebase:  

### Java

    FirebaseModelDownloadConditions conditions = new FirebaseModelDownloadConditions.Builder()
            .requireWifi()
            .build();
    FirebaseModelManager.getInstance().download(remoteModel, conditions)
            .addOnCompleteListener(new OnCompleteListener<Void>() {
                @Override
                public void onComplete(@NonNull Task<Void> task) {
                    // Success.
                }
            });

### Kotlin

    val conditions = FirebaseModelDownloadConditions.Builder()
        .requireWifi()
        .build()
    FirebaseModelManager.getInstance().download(remoteModel, conditions)
        .addOnCompleteListener {
            // Success.
        }

Many apps start the download task in their initialization code, but you can do so at any point before you need to use the model.

### Configure a local model source

To bundle the model with your app:

1. Extract the model and its metadata from the zip archive you downloaded fromFirebaseconsole. We recommend you use the files as you downloaded them, without modification (including the file names).
2. Include your model and its metadata files in your app package:

   1. If you don't have an assets folder in your project, create one by right-clicking the`app/`folder, then clicking**New \> Folder \> Assets Folder**.
   2. Create a sub-folder under the assets folder to contain the model files.
   3. Copy the files`model.tflite`,`dict.txt`, and`manifest.json`to the sub-folder (all three files must be in the same folder).
3. Add the following to your app's`build.gradle`file to ensure Gradle doesn't compress the model file when building the app:  

   ```
   android {
       // ...
       aaptOptions {
           noCompress "tflite"
       }
   }
   ```
   The model file will be included in the app package and available to ML Kit as a raw asset.
4. Create a`FirebaseAutoMLLocalModel`object, specifying the path to the model manifest file:  

   ### Java

       FirebaseAutoMLLocalModel localModel = new FirebaseAutoMLLocalModel.Builder()
               .setAssetFilePath("manifest.json")
               .build();

   ### Kotlin

       val localModel = FirebaseAutoMLLocalModel.Builder()
               .setAssetFilePath("manifest.json")
               .build()

### Create an image labeler from your model

After you configure your model sources, create a`FirebaseVisionImageLabeler`object from one of them.

If you only have a locally-bundled model, just create a labeler from your`FirebaseAutoMLLocalModel`object and configure the confidence score threshold you want to require (see[Evaluate your model](https://firebase.google.com/docs/ml-kit/train-image-labeler#evaluate_the_model)):  

### Java

    FirebaseVisionImageLabeler labeler;
    try {
        FirebaseVisionOnDeviceAutoMLImageLabelerOptions options =
                new FirebaseVisionOnDeviceAutoMLImageLabelerOptions.Builder(localModel)
                        .setConfidenceThreshold(0.0f)  // Evaluate your model in the Firebase console
                                                       // to determine an appropriate value.
                        .build();
        labeler = FirebaseVision.getInstance().getOnDeviceAutoMLImageLabeler(options);
    } catch (FirebaseMLException e) {
        // ...
    }

### Kotlin

    val options = FirebaseVisionOnDeviceAutoMLImageLabelerOptions.Builder(localModel)
        .setConfidenceThreshold(0)  // Evaluate your model in the Firebase console
                                    // to determine an appropriate value.
        .build()
    val labeler = FirebaseVision.getInstance().getOnDeviceAutoMLImageLabeler(options)

If you have a remotely-hosted model, you will have to check that it has been downloaded before you run it. You can check the status of the model download task using the model manager's`isModelDownloaded()`method.

Although you only have to confirm this before running the labeler, if you have both a remotely-hosted model and a locally-bundled model, it might make sense to perform this check when instantiating the image labeler: create a labeler from the remote model if it's been downloaded, and from the local model otherwise.  

### Java

    FirebaseModelManager.getInstance().isModelDownloaded(remoteModel)
            .addOnSuccessListener(new OnSuccessListener<Boolean>() {
                @Override
                public void onSuccess(Boolean isDownloaded) {
                    FirebaseVisionOnDeviceAutoMLImageLabelerOptions.Builder optionsBuilder;
                    if (isDownloaded) {
                        optionsBuilder = new FirebaseVisionOnDeviceAutoMLImageLabelerOptions.Builder(remoteModel);
                    } else {
                        optionsBuilder = new FirebaseVisionOnDeviceAutoMLImageLabelerOptions.Builder(localModel);
                    }
                    FirebaseVisionOnDeviceAutoMLImageLabelerOptions options = optionsBuilder
                            .setConfidenceThreshold(0.0f)  // Evaluate your model in the Firebase console
                                                           // to determine an appropriate threshold.
                            .build();

                    FirebaseVisionImageLabeler labeler;
                    try {
                        labeler = FirebaseVision.getInstance().getOnDeviceAutoMLImageLabeler(options);
                    } catch (FirebaseMLException e) {
                        // Error.
                    }
                }
            });

### Kotlin

    FirebaseModelManager.getInstance().isModelDownloaded(remoteModel)
        .addOnSuccessListener { isDownloaded -> 
        val optionsBuilder =
            if (isDownloaded) {
                FirebaseVisionOnDeviceAutoMLImageLabelerOptions.Builder(remoteModel)
            } else {
                FirebaseVisionOnDeviceAutoMLImageLabelerOptions.Builder(localModel)
            }
        // Evaluate your model in the Firebase console to determine an appropriate threshold.
        val options = optionsBuilder.setConfidenceThreshold(0.0f).build()
        val labeler = FirebaseVision.getInstance().getOnDeviceAutoMLImageLabeler(options)
    }

If you only have a remotely-hosted model, you should disable model-related functionality---for example, grey-out or hide part of your UI---until you confirm the model has been downloaded. You can do so by attaching a listener to the model manager's`download()`method:  

### Java

    FirebaseModelManager.getInstance().download(remoteModel, conditions)
            .addOnSuccessListener(new OnSuccessListener<Void>() {
                @Override
                public void onSuccess(Void v) {
                  // Download complete. Depending on your app, you could enable
                  // the ML feature, or switch from the local model to the remote
                  // model, etc.
                }
            });

### Kotlin

    FirebaseModelManager.getInstance().download(remoteModel, conditions)
        .addOnCompleteListener {
            // Download complete. Depending on your app, you could enable the ML
            // feature, or switch from the local model to the remote model, etc.
        }

## 2. Prepare the input image

Then, for each image you want to label, create a`FirebaseVisionImage`object using one of the options described in this section and pass it to an instance of`FirebaseVisionImageLabeler`(described in the next section).

You can create a`FirebaseVisionImage`object from a`media.Image`object, a file on the device, a byte array, or a`Bitmap`object:

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

## 3. Run the image labeler

To label objects in an image, pass the`FirebaseVisionImage`object to the`FirebaseVisionImageLabeler`'s`processImage()`method.  

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

If image labeling succeeds, an array of`FirebaseVisionImageLabel`objects will be passed to the success listener. From each object, you can get information about a feature recognized in the image.

For example:  

### Java

    for (FirebaseVisionImageLabel label: labels) {
        String text = label.getText();
        float confidence = label.getConfidence();
    }

### Kotlin

    for (label in labels) {
        val text = label.text
        val confidence = label.confidence
    }

| **Note:** when using an AutoML-trained model,`getEntityId()`from the returned labels always returns`null`.

## Tips to improve real-time performance

- Throttle calls to the detector. If a new video frame becomes available while the detector is running, drop the frame.
- If you are using the output of the detector to overlay graphics on the input image, first get the result from ML Kit, then render the image and overlay in a single step. By doing so, you render to the display surface only once for each input frame.
- If you use the Camera2 API, capture images in`ImageFormat.YUV_420_888`format.

  If you use the older Camera API, capture images in`ImageFormat.NV21`format.