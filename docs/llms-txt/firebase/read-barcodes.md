# Source: https://firebase.google.com/docs/ml-kit/read-barcodes.md.txt

# Source: https://firebase.google.com/docs/ml-kit/ios/read-barcodes.md.txt

# Source: https://firebase.google.com/docs/ml-kit/android/read-barcodes.md.txt

| This page describes an old version of the Barcode Scanning API, which was part of ML Kit for Firebase. Development of this API has been moved to the standalone ML Kit SDK, which you can use with or without Firebase.[Learn more](https://developers.google.com/ml-kit/migration).
|
| See[Scan Barcodes with ML Kit on Android](https://developers.google.com/ml-kit/vision/barcode-scanning/android)for the latest documentation.

<br />

You can use ML Kit to recognize and decode barcodes.

<br />

| Version 24.0.0 of`firebase-ml-vision`introduces a new barcode scanning model, which comes with significant improvements in both latency and accuracy over the older model. In addition, with the latest API, you now can access the raw bytes for non UTF-8 encoded barcode data.
|
| Be sure to add the new`firebase-ml-vision-barcode-model`module to your project dependencies to use the new model.

## Before you begin

1. If you haven't already,[add Firebase to your Android project](https://firebase.google.com/docs/android/setup).
2. Add the dependencies for the ML Kit Android libraries to your module (app-level) Gradle file (usually`app/build.gradle`):  

   ```carbon
   apply plugin: 'com.android.application'
   apply plugin: 'com.google.gms.google-services'

   dependencies {
     // ...

     implementation 'com.google.firebase:firebase-ml-vision:24.0.3'
     implementation 'com.google.firebase:firebase-ml-vision-barcode-model:16.0.1'
   }
   ```

## Input image guidelines

- For ML Kit to accurately read barcodes, input images must contain barcodes that are represented by sufficient pixel data.

  The specific pixel data requirements are dependent on both the type of barcode and the amount of data that is encoded in it (since most barcodes support a variable length payload). In general, the smallest meaningful unit of the barcode should be at least 2 pixels wide (and for 2-dimensional codes, 2 pixels tall).

  For example, EAN-13 barcodes are made up of bars and spaces that are 1, 2, 3, or 4 units wide, so an EAN-13 barcode image ideally has bars and spaces that are at least 2, 4, 6, and 8 pixels wide. Because an EAN-13 barcode is 95 units wide in total, the barcode should be at least 190 pixels wide.

  Denser formats, such as PDF417, need greater pixel dimensions for ML Kit to reliably read them. For example, a PDF417 code can have up to 34 17-unit wide "words" in a single row, which would ideally be at least 1156 pixels wide.
- Poor image focus can hurt scanning accuracy. If you aren't getting acceptable results, try asking the user to recapture the image.

- For typical applications, it is recommended to provide a higher resolution image (such as 1280x720 or 1920x1080), which makes barcodes detectable from a larger distance away from the camera.

  However, in applications where latency is critical, you can improve performance by capturing images at a lower resolution, but requiring that the barcode make up the majority of the input image. Also see[Tips to improve real-time performance](https://firebase.google.com/docs/ml-kit/android/read-barcodes#performance_tips).

## 1. Configure the barcode detector

If you know which barcode formats you expect to read, you can improve the speed of the barcode detector by configuring it to only detect those formats.

<br />

For example, to detect only Aztec code and QR codes, build a[`FirebaseVisionBarcodeDetectorOptions`](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcodeDetectorOptions.Builder)object as in the following example:  

### Java

```java
FirebaseVisionBarcodeDetectorOptions options =
        new FirebaseVisionBarcodeDetectorOptions.Builder()
        .setBarcodeFormats(
                FirebaseVisionBarcode.FORMAT_QR_CODE,
                FirebaseVisionBarcode.FORMAT_AZTEC)
        .build();
```

### Kotlin

```kotlin
val options = FirebaseVisionBarcodeDetectorOptions.Builder()
        .setBarcodeFormats(
                FirebaseVisionBarcode.FORMAT_QR_CODE,
                FirebaseVisionBarcode.FORMAT_AZTEC)
        .build()
```

The following formats are supported:

- Code 128 (`FORMAT_CODE_128`)
- Code 39 (`FORMAT_CODE_39`)
- Code 93 (`FORMAT_CODE_93`)
- Codabar (`FORMAT_CODABAR`)
- EAN-13 (`FORMAT_EAN_13`)
- EAN-8 (`FORMAT_EAN_8`)
- ITF (`FORMAT_ITF`)
- UPC-A (`FORMAT_UPC_A`)
- UPC-E (`FORMAT_UPC_E`)
- QR Code (`FORMAT_QR_CODE`)
- PDF417 (`FORMAT_PDF417`)
- Aztec (`FORMAT_AZTEC`)
- Data Matrix (`FORMAT_DATA_MATRIX`)

| **Note:** For a Data Matrix code to be recognized, the code must intersect the center point of the input image. Consequently, only one Data Matrix code can be recognized in an image.

## 2. Run the barcode detector

To recognize barcodes in an image, create a`FirebaseVisionImage`object from either a`Bitmap`,`media.Image`,`ByteBuffer`, byte array, or a file on the device. Then, pass the`FirebaseVisionImage`object to the`FirebaseVisionBarcodeDetector`'s`detectInImage`method.

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

2. Get an instance of[`FirebaseVisionBarcodeDetector`](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcodeDetector):

   ### Java

   ```java
   FirebaseVisionBarcodeDetector detector = FirebaseVision.getInstance()
           .getVisionBarcodeDetector();
   // Or, to specify the formats to recognize:
   // FirebaseVisionBarcodeDetector detector = FirebaseVision.getInstance()
   //        .getVisionBarcodeDetector(options);
   ```

   ### Kotlin

   ```kotlin
   val detector = FirebaseVision.getInstance()
           .visionBarcodeDetector
   // Or, to specify the formats to recognize:
   // val detector = FirebaseVision.getInstance()
   //        .getVisionBarcodeDetector(options)
   ```
3. Finally, pass the image to the`detectInImage`method:

   ### Java

   ```java
   Task<List<FirebaseVisionBarcode>> result = detector.detectInImage(image)
           .addOnSuccessListener(new OnSuccessListener<List<FirebaseVisionBarcode>>() {
               @Override
               public void onSuccess(List<FirebaseVisionBarcode> barcodes) {
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
           .addOnSuccessListener { barcodes ->
               // Task completed successfully
               // ...
           }
           .addOnFailureListener {
               // Task failed with an exception
               // ...
           }
   ```

## 3. Get information from barcodes

If the barcode recognition operation succeeds, a list of[`FirebaseVisionBarcode`](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode)objects will be passed to the success listener. Each`FirebaseVisionBarcode`object represents a barcode that was detected in the image. For each barcode, you can get its bounding coordinates in the input image, as well as the raw data encoded by the barcode. Also, if the barcode detector was able to determine the type of data encoded by the barcode, you can get an object containing parsed data.

<br />

For example:  

### Java

```java
for (FirebaseVisionBarcode barcode: barcodes) {
    Rect bounds = barcode.getBoundingBox();
    Point[] corners = barcode.getCornerPoints();

    String rawValue = barcode.getRawValue();

    int valueType = barcode.getValueType();
    // See API reference for complete list of supported types
    switch (valueType) {
        case FirebaseVisionBarcode.TYPE_WIFI:
            String ssid = barcode.getWifi().getSsid();
            String password = barcode.getWifi().getPassword();
            int type = barcode.getWifi().getEncryptionType();
            break;
        case FirebaseVisionBarcode.TYPE_URL:
            String title = barcode.getUrl().getTitle();
            String url = barcode.getUrl().getUrl();
            break;
    }
}
```

### Kotlin

```kotlin
for (barcode in barcodes) {
    val bounds = barcode.boundingBox
    val corners = barcode.cornerPoints

    val rawValue = barcode.rawValue

    val valueType = barcode.valueType
    // See API reference for complete list of supported types
    when (valueType) {
        FirebaseVisionBarcode.TYPE_WIFI -> {
            val ssid = barcode.wifi!!.ssid
            val password = barcode.wifi!!.password
            val type = barcode.wifi!!.encryptionType
        }
        FirebaseVisionBarcode.TYPE_URL -> {
            val title = barcode.url!!.title
            val url = barcode.url!!.url
        }
    }
}
```

## Tips to improve real-time performance

If you want to scan barcodes in a real-time application, follow these guidelines to achieve the best framerates:

- Don't capture input at the camera's native resolution. On some devices, capturing input at the native resolution produces extremely large (10+ megapixels) images, which results in very poor latency with no benefit to accuracy. Instead, only request the size from the camera that is required for barcode detection: usually no more than 2 megapixels.

  If scanning speed is important, you can further lower the image capture resolution. However, bear in mind the minimum barcode size requirements outlined above.
- Throttle calls to the detector. If a new video frame becomes available while the detector is running, drop the frame.
- If you are using the output of the detector to overlay graphics on the input image, first get the result from ML Kit, then render the image and overlay in a single step. By doing so, you render to the display surface only once for each input frame.
- If you use the Camera2 API, capture images in`ImageFormat.YUV_420_888`format.

  If you use the older Camera API, capture images in`ImageFormat.NV21`format.