# Source: https://firebase.google.com/docs/ml/ios/recognize-text-deprecated.md.txt

# Source: https://firebase.google.com/docs/ml/android/recognize-text-deprecated.md.txt

This page describes an old version of recognizing text in images using the deprecatedFirebase MLVision sdk. As an alternative, you may[call Cloud Vision APIs using Firebase Auth and Callable Functions](https://firebase.google.com/docs/ml/android/recognize-text)to allow only users logged into your app to access the API.  

You can useFirebase MLto recognize text in images.Firebase MLhas both a general-purpose API suitable for recognizing text in images, such as the text of a street sign, and an API optimized for recognizing the text of documents.
| Use of the Cloud Vision APIs is subject to the[Google Cloud Platform License Agreement](https://cloud.google.com/terms/)and[Service Specific Terms](https://cloud.google.com/terms/service-terms), and billed accordingly. For billing information, see the[Pricing](https://cloud.google.com/vision/pricing)page.
| **Looking for on-device text recognition?** Try the[standalone ML Kit library](https://developers.google.com/ml-kit/vision/text-recognition).

## Before you begin

1. If you haven't already,[add Firebase to your Android project](https://firebase.google.com/docs/android/setup).
2. In your**module (app-level) Gradle file** (usually`<project>/<app-module>/build.gradle.kts`or`<project>/<app-module>/build.gradle`), add the dependency for theFirebase MLVision library for Android. We recommend using the[Firebase Android BoM](https://firebase.google.com/docs/android/learn-more#bom)to control library versioning.  

   ```carbon
   dependencies {
       // Import the BoM for the Firebase platform
       implementation(platform("com.google.firebase:firebase-bom:34.7.0"))

       // Add the dependency for the Firebase ML Vision library
       // When using the BoM, you don't specify versions in Firebase library dependencies
       implementation 'com.google.firebase:firebase-ml-vision'
   }
   ```

   By using the[Firebase Android BoM](https://firebase.google.com/docs/android/learn-more#bom), your app will always use compatible versions of Firebase Android libraries.
   *(Alternative)* Add Firebase library dependencies*without* using theBoM

   If you choose not to use theFirebase BoM, you must specify each Firebase library version in its dependency line.

   **Note that if you use*multiple* Firebase libraries in your app, we strongly recommend using theBoMto manage library versions, which ensures that all versions are compatible.**  

   ```groovy
   dependencies {
       // Add the dependency for the Firebase ML Vision library
       // When NOT using the BoM, you must specify versions in Firebase library dependencies
       implementation 'com.google.firebase:firebase-ml-vision:24.1.0'
   }
   ```
3. If you haven't already enabled Cloud-based APIs for your project, do so now:

   1. Open the[Firebase MLAPIs page](https://console.firebase.google.com/project/_/ml/apis)in theFirebaseconsole.
   2. If you haven't already upgraded your project to the[pay-as-you-go Blaze pricing plan](https://firebase.google.com/pricing), click**Upgrade**to do so. (You'll be prompted to upgrade only if your project isn't on the Blaze pricing plan.)

      Only projects on the Blaze pricing plan can use Cloud-based APIs.
   3. If Cloud-based APIs aren't already enabled, click**Enable Cloud-based APIs**.

   | Before you deploy to production an app that uses a Cloud API, you should take some additional steps to[prevent and mitigate the effect of unauthorized API access](https://firebase.google.com/docs/ml/android/secure-api-key).

Now you are ready to start recognizing text in images.

## Input image guidelines

- ForFirebase MLto accurately recognize text, input images must contain text that is represented by sufficient pixel data. Ideally, for Latin text, each character should be at least 16x16 pixels. For Chinese, Japanese, and Korean text, each character should be 24x24 pixels. For all languages, there is generally no accuracy benefit for characters to be larger than 24x24 pixels.

  So, for example, a 640x480 image might work well to scan a business card that occupies the full width of the image. To scan a document printed on letter-sized paper, a 720x1280 pixel image might be required.
- Poor image focus can hurt text recognition accuracy. If you aren't getting acceptable results, try asking the user to recapture the image.

*** ** * ** ***

## Recognize text in images

To recognize text in an image, run the text recognizer as described below.

### 1. Run the text recognizer

To recognize text in an image, create a`FirebaseVisionImage`object from either a`Bitmap`,`media.Image`,`ByteBuffer`, byte array, or a file on the device. Then, pass the`FirebaseVisionImage`object to the`FirebaseVisionTextRecognizer`'s`processImage`method.

<br />

1. Create a[`FirebaseVisionImage`](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage)object from your image.

   - To create a`FirebaseVisionImage`object from a`media.Image`object, such as when capturing an image from a device's camera, pass the`media.Image`object and the image's rotation to`FirebaseVisionImage.fromMediaImage()`.

     If you use the[CameraX](https://developer.android.com/training/camerax)library, the`OnImageCapturedListener`and`ImageAnalysis.Analyzer`classes calculate the rotation value for you, so you just need to convert the rotation to one ofFirebase ML's`ROTATION_`constants before calling`FirebaseVisionImage.fromMediaImage()`:  

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

     If you don't use a camera library that gives you the image's rotation, you can calculate it from the device's rotation and the orientation of camera sensor in the device:  

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
     }https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/mlkit/app/src/main/java/com/google/firebase/example/mlkit/kotlin/VisionImage.kt#L75-L110
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
     }https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/mlkit/app/src/main/java/com/google/firebase/example/mlkit/VisionImage.java#L81-L131
     ```

     Then, pass the`media.Image`object and the rotation value to`FirebaseVisionImage.fromMediaImage()`:  

     ### Kotlin

     ```kotlin
     val image = FirebaseVisionImage.fromMediaImage(mediaImage, rotation)https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/mlkit/app/src/main/java/com/google/firebase/example/mlkit/kotlin/VisionImage.kt#L33-L33
     ```

     ### Java

     ```java
     FirebaseVisionImage image = FirebaseVisionImage.fromMediaImage(mediaImage, rotation);https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/mlkit/app/src/main/java/com/google/firebase/example/mlkit/VisionImage.java#L39-L39
     ```
   - To create a`FirebaseVisionImage`object from a file URI, pass the app context and file URI to`FirebaseVisionImage.fromFilePath()`. This is useful when you use an`ACTION_GET_CONTENT`intent to prompt the user to select an image from their gallery app.  

     ### Kotlin

     ```kotlin
     val image: FirebaseVisionImage
     try {
         image = FirebaseVisionImage.fromFilePath(context, uri)
     } catch (e: IOException) {
         e.printStackTrace()
     }https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/mlkit/app/src/main/java/com/google/firebase/example/mlkit/kotlin/VisionImage.kt#L65-L70
     ```

     ### Java

     ```java
     FirebaseVisionImage image;
     try {
         image = FirebaseVisionImage.fromFilePath(context, uri);
     } catch (IOException e) {
         e.printStackTrace();
     }https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/mlkit/app/src/main/java/com/google/firebase/example/mlkit/VisionImage.java#L71-L76
     ```
   - To create a`FirebaseVisionImage`object from a`ByteBuffer`or a byte array, first calculate the image rotation as described above for`media.Image`input.

     Then, create a`FirebaseVisionImageMetadata`object that contains the image's height, width, color encoding format, and rotation:  

     ### Kotlin

     ```kotlin
     val metadata = FirebaseVisionImageMetadata.Builder()
         .setWidth(480) // 480x360 is typically sufficient for
         .setHeight(360) // image recognition
         .setFormat(FirebaseVisionImageMetadata.IMAGE_FORMAT_NV21)
         .setRotation(rotation)
         .build()https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/mlkit/app/src/main/java/com/google/firebase/example/mlkit/kotlin/VisionImage.kt#L39-L44
     ```

     ### Java

     ```java
     FirebaseVisionImageMetadata metadata = new FirebaseVisionImageMetadata.Builder()
             .setWidth(480)   // 480x360 is typically sufficient for
             .setHeight(360)  // image recognition
             .setFormat(FirebaseVisionImageMetadata.IMAGE_FORMAT_NV21)
             .setRotation(rotation)
             .build();https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/mlkit/app/src/main/java/com/google/firebase/example/mlkit/VisionImage.java#L45-L50
     ```

     Use the buffer or array, and the metadata object, to create a`FirebaseVisionImage`object:  

     ### Kotlin

     ```kotlin
     val image = FirebaseVisionImage.fromByteBuffer(buffer, metadata)
     // Or: val image = FirebaseVisionImage.fromByteArray(byteArray, metadata)  
     https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/mlkit/app/src/main/java/com/google/firebase/example/mlkit/kotlin/VisionImage.kt#L59-L59
     ```

     ### Java

     ```java
     FirebaseVisionImage image = FirebaseVisionImage.fromByteBuffer(buffer, metadata);
     // Or: FirebaseVisionImage image = FirebaseVisionImage.fromByteArray(byteArray, metadata);  
     https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/mlkit/app/src/main/java/com/google/firebase/example/mlkit/VisionImage.java#L65-L65
     ```
   - To create a`FirebaseVisionImage`object from a`Bitmap`object:  

     ### Kotlin

     ```kotlin
     val image = FirebaseVisionImage.fromBitmap(bitmap)https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/mlkit/app/src/main/java/com/google/firebase/example/mlkit/kotlin/VisionImage.kt#L26-L26
     ```

     ### Java

     ```java
     FirebaseVisionImage image = FirebaseVisionImage.fromBitmap(bitmap);https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/mlkit/app/src/main/java/com/google/firebase/example/mlkit/VisionImage.java#L32-L32
     ```
     The image represented by the`Bitmap`object must be upright, with no additional rotation required.

   <br />

2. Get an instance of[`FirebaseVisionTextRecognizer`](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionTextRecognizer).

   ### Kotlin

   ```java
   val detector = FirebaseVision.getInstance().cloudTextRecognizer
   // Or, to change the default settings:
   // val detector = FirebaseVision.getInstance().getCloudTextRecognizer(options)  
   https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/mlkit/app/src/main/java/com/google/firebase/example/mlkit/kotlin/TextRecognitionActivity.kt#L57-L59
   ```  

   ```java
   // Or, to provide language hints to assist with language detection:
   // See https://cloud.google.com/vision/docs/languages for supported languages
   val options = FirebaseVisionCloudTextRecognizerOptions.Builder()
       .setLanguageHints(listOf("en", "hi"))
       .build()https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/mlkit/app/src/main/java/com/google/firebase/example/mlkit/kotlin/TextRecognitionActivity.kt#L51-L53
   ```

   ### Java

   ```java
   FirebaseVisionTextRecognizer detector = FirebaseVision.getInstance()
           .getCloudTextRecognizer();
   // Or, to change the default settings:
   //   FirebaseVisionTextRecognizer detector = FirebaseVision.getInstance()
   //          .getCloudTextRecognizer(options);  
   https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/mlkit/app/src/main/java/com/google/firebase/example/mlkit/TextRecognitionActivity.java#L84-L88
   ```  

   ```java
   // Or, to provide language hints to assist with language detection:
   // See https://cloud.google.com/vision/docs/languages for supported languages
   FirebaseVisionCloudTextRecognizerOptions options = new FirebaseVisionCloudTextRecognizerOptions.Builder()
           .setLanguageHints(Arrays.asList("en", "hi"))
           .build();https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/mlkit/app/src/main/java/com/google/firebase/example/mlkit/TextRecognitionActivity.java#L78-L80
   ```
3. Finally, pass the image to the`processImage`method:

   ### Kotlin

   ```kotlin
   val result = detector.processImage(image)
       .addOnSuccessListener { firebaseVisionText ->
           // Task completed successfully
           // ...
       }
       .addOnFailureListener { e ->
           // Task failed with an exception
           // ...
       }https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/mlkit/app/src/main/java/com/google/firebase/example/mlkit/kotlin/TextRecognitionActivity.kt#L22-L45
   ```

   ### Java

   ```java
   Task<FirebaseVisionText> result =
           detector.processImage(image)
                   .addOnSuccessListener(new OnSuccessListener<FirebaseVisionText>() {
                       @Override
                       public void onSuccess(FirebaseVisionText firebaseVisionText) {
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
                           });https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/mlkit/app/src/main/java/com/google/firebase/example/mlkit/TextRecognitionActivity.java#L41-L72
   ```

### 2. Extract text from blocks of recognized text

If the text recognition operation succeeds, a[`FirebaseVisionText`](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionText)object will be passed to the success listener. A`FirebaseVisionText`object contains the full text recognized in the image and zero or more[`TextBlock`](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionText.TextBlock)objects.

<br />

Each`TextBlock`represents a rectangular block of text, which contains zero or more[`Line`](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionText.Line)objects. Each`Line`object contains zero or more[`Element`](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionText.Element)objects, which represent words and word-like entities (dates, numbers, and so on).

For each`TextBlock`,`Line`, and`Element`object, you can get the text recognized in the region and the bounding coordinates of the region.

For example:  

### Kotlin

```kotlin
val resultText = result.text
for (block in result.textBlocks) {
    val blockText = block.text
    val blockConfidence = block.confidence
    val blockLanguages = block.recognizedLanguages
    val blockCornerPoints = block.cornerPoints
    val blockFrame = block.boundingBox
    for (line in block.lines) {
        val lineText = line.text
        val lineConfidence = line.confidence
        val lineLanguages = line.recognizedLanguages
        val lineCornerPoints = line.cornerPoints
        val lineFrame = line.boundingBox
        for (element in line.elements) {
            val elementText = element.text
            val elementConfidence = element.confidence
            val elementLanguages = element.recognizedLanguages
            val elementCornerPoints = element.cornerPoints
            val elementFrame = element.boundingBox
        }
    }
}https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/mlkit/app/src/main/java/com/google/firebase/example/mlkit/kotlin/TextRecognitionActivity.kt#L92-L113
```

### Java

```java
String resultText = result.getText();
for (FirebaseVisionText.TextBlock block: result.getTextBlocks()) {
    String blockText = block.getText();
    Float blockConfidence = block.getConfidence();
    List<RecognizedLanguage> blockLanguages = block.getRecognizedLanguages();
    Point[] blockCornerPoints = block.getCornerPoints();
    Rect blockFrame = block.getBoundingBox();
    for (FirebaseVisionText.Line line: block.getLines()) {
        String lineText = line.getText();
        Float lineConfidence = line.getConfidence();
        List<RecognizedLanguage> lineLanguages = line.getRecognizedLanguages();
        Point[] lineCornerPoints = line.getCornerPoints();
        Rect lineFrame = line.getBoundingBox();
        for (FirebaseVisionText.Element element: line.getElements()) {
            String elementText = element.getText();
            Float elementConfidence = element.getConfidence();
            List<RecognizedLanguage> elementLanguages = element.getRecognizedLanguages();
            Point[] elementCornerPoints = element.getCornerPoints();
            Rect elementFrame = element.getBoundingBox();
        }
    }
}https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/mlkit/app/src/main/java/com/google/firebase/example/mlkit/TextRecognitionActivity.java#L127-L148
```

### Next steps

- Before you deploy to production an app that uses a Cloud API, you should take some additional steps to[prevent and mitigate the effect of unauthorized API access](https://firebase.google.com/docs/ml/android/secure-api-key).

*** ** * ** ***

## Recognize text in images of documents

To recognize the text of a document, configure and run the document text recognizer as described below.

The document text recognition API, described below, provides an interface that is intended to be more convenient for working with images of documents. However, if you prefer the interface provided by the`FirebaseVisionTextRecognizer`API, you can use it instead to scan documents by configuring the cloud text recognizer to[use the dense text model](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionCloudTextRecognizerOptions.Builder#setModelType(int)).

To use the document text recognition API:

### 1. Run the text recognizer

To recognize text in an image, create a`FirebaseVisionImage`object from either a`Bitmap`,`media.Image`,`ByteBuffer`, byte array, or a file on the device. Then, pass the`FirebaseVisionImage`object to the`FirebaseVisionDocumentTextRecognizer`'s`processImage`method.

<br />

1. Create a[`FirebaseVisionImage`](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage)object from your image.

   - To create a`FirebaseVisionImage`object from a`media.Image`object, such as when capturing an image from a device's camera, pass the`media.Image`object and the image's rotation to`FirebaseVisionImage.fromMediaImage()`.

     If you use the[CameraX](https://developer.android.com/training/camerax)library, the`OnImageCapturedListener`and`ImageAnalysis.Analyzer`classes calculate the rotation value for you, so you just need to convert the rotation to one ofFirebase ML's`ROTATION_`constants before calling`FirebaseVisionImage.fromMediaImage()`:  

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

     If you don't use a camera library that gives you the image's rotation, you can calculate it from the device's rotation and the orientation of camera sensor in the device:  

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
     }https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/mlkit/app/src/main/java/com/google/firebase/example/mlkit/kotlin/VisionImage.kt#L75-L110
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
     }https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/mlkit/app/src/main/java/com/google/firebase/example/mlkit/VisionImage.java#L81-L131
     ```

     Then, pass the`media.Image`object and the rotation value to`FirebaseVisionImage.fromMediaImage()`:  

     ### Kotlin

     ```kotlin
     val image = FirebaseVisionImage.fromMediaImage(mediaImage, rotation)https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/mlkit/app/src/main/java/com/google/firebase/example/mlkit/kotlin/VisionImage.kt#L33-L33
     ```

     ### Java

     ```java
     FirebaseVisionImage image = FirebaseVisionImage.fromMediaImage(mediaImage, rotation);https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/mlkit/app/src/main/java/com/google/firebase/example/mlkit/VisionImage.java#L39-L39
     ```
   - To create a`FirebaseVisionImage`object from a file URI, pass the app context and file URI to`FirebaseVisionImage.fromFilePath()`. This is useful when you use an`ACTION_GET_CONTENT`intent to prompt the user to select an image from their gallery app.  

     ### Kotlin

     ```kotlin
     val image: FirebaseVisionImage
     try {
         image = FirebaseVisionImage.fromFilePath(context, uri)
     } catch (e: IOException) {
         e.printStackTrace()
     }https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/mlkit/app/src/main/java/com/google/firebase/example/mlkit/kotlin/VisionImage.kt#L65-L70
     ```

     ### Java

     ```java
     FirebaseVisionImage image;
     try {
         image = FirebaseVisionImage.fromFilePath(context, uri);
     } catch (IOException e) {
         e.printStackTrace();
     }https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/mlkit/app/src/main/java/com/google/firebase/example/mlkit/VisionImage.java#L71-L76
     ```
   - To create a`FirebaseVisionImage`object from a`ByteBuffer`or a byte array, first calculate the image rotation as described above for`media.Image`input.

     Then, create a`FirebaseVisionImageMetadata`object that contains the image's height, width, color encoding format, and rotation:  

     ### Kotlin

     ```kotlin
     val metadata = FirebaseVisionImageMetadata.Builder()
         .setWidth(480) // 480x360 is typically sufficient for
         .setHeight(360) // image recognition
         .setFormat(FirebaseVisionImageMetadata.IMAGE_FORMAT_NV21)
         .setRotation(rotation)
         .build()https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/mlkit/app/src/main/java/com/google/firebase/example/mlkit/kotlin/VisionImage.kt#L39-L44
     ```

     ### Java

     ```java
     FirebaseVisionImageMetadata metadata = new FirebaseVisionImageMetadata.Builder()
             .setWidth(480)   // 480x360 is typically sufficient for
             .setHeight(360)  // image recognition
             .setFormat(FirebaseVisionImageMetadata.IMAGE_FORMAT_NV21)
             .setRotation(rotation)
             .build();https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/mlkit/app/src/main/java/com/google/firebase/example/mlkit/VisionImage.java#L45-L50
     ```

     Use the buffer or array, and the metadata object, to create a`FirebaseVisionImage`object:  

     ### Kotlin

     ```kotlin
     val image = FirebaseVisionImage.fromByteBuffer(buffer, metadata)
     // Or: val image = FirebaseVisionImage.fromByteArray(byteArray, metadata)  
     https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/mlkit/app/src/main/java/com/google/firebase/example/mlkit/kotlin/VisionImage.kt#L59-L59
     ```

     ### Java

     ```java
     FirebaseVisionImage image = FirebaseVisionImage.fromByteBuffer(buffer, metadata);
     // Or: FirebaseVisionImage image = FirebaseVisionImage.fromByteArray(byteArray, metadata);  
     https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/mlkit/app/src/main/java/com/google/firebase/example/mlkit/VisionImage.java#L65-L65
     ```
   - To create a`FirebaseVisionImage`object from a`Bitmap`object:  

     ### Kotlin

     ```kotlin
     val image = FirebaseVisionImage.fromBitmap(bitmap)https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/mlkit/app/src/main/java/com/google/firebase/example/mlkit/kotlin/VisionImage.kt#L26-L26
     ```

     ### Java

     ```java
     FirebaseVisionImage image = FirebaseVisionImage.fromBitmap(bitmap);https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/mlkit/app/src/main/java/com/google/firebase/example/mlkit/VisionImage.java#L32-L32
     ```
     The image represented by the`Bitmap`object must be upright, with no additional rotation required.

   <br />

2. Get an instance of[`FirebaseVisionDocumentTextRecognizer`](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionDocumentTextRecognizer):

   ### Kotlin

   <br />

   ```java
   val detector = FirebaseVision.getInstance()
       .cloudDocumentTextRecognizer  
   https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/mlkit/app/src/main/java/com/google/firebase/example/mlkit/kotlin/TextRecognitionActivity.kt#L119-L120
   ```  

   ```java
   // Or, to provide language hints to assist with language detection:
   // See https://cloud.google.com/vision/docs/languages for supported languages
   val options = FirebaseVisionCloudDocumentRecognizerOptions.Builder()
       .setLanguageHints(listOf("en", "hi"))
       .build()
   val detector = FirebaseVision.getInstance()
       .getCloudDocumentTextRecognizer(options)https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/mlkit/app/src/main/java/com/google/firebase/example/mlkit/kotlin/TextRecognitionActivity.kt#L128-L134
   ```

   <br />

   ### Java

   <br />

   ```java
   FirebaseVisionDocumentTextRecognizer detector = FirebaseVision.getInstance()
           .getCloudDocumentTextRecognizer();https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/mlkit/app/src/main/java/com/google/firebase/example/mlkit/TextRecognitionActivity.java#L154-L155
   ```  

   ```java
   // Or, to provide language hints to assist with language detection:
   // See https://cloud.google.com/vision/docs/languages for supported languages
   FirebaseVisionCloudDocumentRecognizerOptions options =
           new FirebaseVisionCloudDocumentRecognizerOptions.Builder()
                   .setLanguageHints(Arrays.asList("en", "hi"))
                   .build();
   FirebaseVisionDocumentTextRecognizer detector = FirebaseVision.getInstance()
           .getCloudDocumentTextRecognizer(options);https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/mlkit/app/src/main/java/com/google/firebase/example/mlkit/TextRecognitionActivity.java#L163-L170
   ```

   <br />

3. Finally, pass the image to the`processImage`method:

   ### Kotlin

   ```kotlin
   detector.processImage(myImage)
       .addOnSuccessListener { firebaseVisionDocumentText ->
           // Task completed successfully
           // ...
       }
       .addOnFailureListener { e ->
           // Task failed with an exception
           // ...
       }https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/mlkit/app/src/main/java/com/google/firebase/example/mlkit/kotlin/TextRecognitionActivity.kt#L149-L157
   ```

   ### Java

   ```java
   detector.processImage(myImage)
           .addOnSuccessListener(new OnSuccessListener<FirebaseVisionDocumentText>() {
               @Override
               public void onSuccess(FirebaseVisionDocumentText result) {
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
           });https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/mlkit/app/src/main/java/com/google/firebase/example/mlkit/TextRecognitionActivity.java#L183-L197
   ```

### 2. Extract text from blocks of recognized text

If the text recognition operation succeeds, it will return a[`FirebaseVisionDocumentText`](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionDocumentText)object. A`FirebaseVisionDocumentText`object contains the full text recognized in the image and a hierarchy of objects that reflect the structure of the recognized document:

- [`FirebaseVisionDocumentText.Block`](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionDocumentText)
- [`FirebaseVisionDocumentText.Paragraph`](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionDocumentText)
- [`FirebaseVisionDocumentText.Word`](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionDocumentText)
- [`FirebaseVisionDocumentText.Symbol`](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionDocumentText)

For each`Block`,`Paragraph`,`Word`, and`Symbol`object, you can get the text recognized in the region and the bounding coordinates of the region.

For example:  

### Kotlin

```kotlin
val resultText = result.text
for (block in result.blocks) {
    val blockText = block.text
    val blockConfidence = block.confidence
    val blockRecognizedLanguages = block.recognizedLanguages
    val blockFrame = block.boundingBox
    for (paragraph in block.paragraphs) {
        val paragraphText = paragraph.text
        val paragraphConfidence = paragraph.confidence
        val paragraphRecognizedLanguages = paragraph.recognizedLanguages
        val paragraphFrame = paragraph.boundingBox
        for (word in paragraph.words) {
            val wordText = word.text
            val wordConfidence = word.confidence
            val wordRecognizedLanguages = word.recognizedLanguages
            val wordFrame = word.boundingBox
            for (symbol in word.symbols) {
                val symbolText = symbol.text
                val symbolConfidence = symbol.confidence
                val symbolRecognizedLanguages = symbol.recognizedLanguages
                val symbolFrame = symbol.boundingBox
            }
        }
    }
}https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/mlkit/app/src/main/java/com/google/firebase/example/mlkit/kotlin/TextRecognitionActivity.kt#L163-L187
```

### Java

```java
String resultText = result.getText();
for (FirebaseVisionDocumentText.Block block: result.getBlocks()) {
    String blockText = block.getText();
    Float blockConfidence = block.getConfidence();
    List<RecognizedLanguage> blockRecognizedLanguages = block.getRecognizedLanguages();
    Rect blockFrame = block.getBoundingBox();
    for (FirebaseVisionDocumentText.Paragraph paragraph: block.getParagraphs()) {
        String paragraphText = paragraph.getText();
        Float paragraphConfidence = paragraph.getConfidence();
        List<RecognizedLanguage> paragraphRecognizedLanguages = paragraph.getRecognizedLanguages();
        Rect paragraphFrame = paragraph.getBoundingBox();
        for (FirebaseVisionDocumentText.Word word: paragraph.getWords()) {
            String wordText = word.getText();
            Float wordConfidence = word.getConfidence();
            List<RecognizedLanguage> wordRecognizedLanguages = word.getRecognizedLanguages();
            Rect wordFrame = word.getBoundingBox();
            for (FirebaseVisionDocumentText.Symbol symbol: word.getSymbols()) {
                String symbolText = symbol.getText();
                Float symbolConfidence = symbol.getConfidence();
                List<RecognizedLanguage> symbolRecognizedLanguages = symbol.getRecognizedLanguages();
                Rect symbolFrame = symbol.getBoundingBox();
            }
        }
    }
}https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/mlkit/app/src/main/java/com/google/firebase/example/mlkit/TextRecognitionActivity.java#L203-L227
```

### Next steps

- Before you deploy to production an app that uses a Cloud API, you should take some additional steps to[prevent and mitigate the effect of unauthorized API access](https://firebase.google.com/docs/ml/android/secure-api-key).