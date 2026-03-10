# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionTextDetector.md.txt

# FirebaseVisionTextDetector

public class **FirebaseVisionTextDetector** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
implements [Closeable](https://developer.android.com/reference/java/io/Closeable.html) [Closeable](https://developer.android.com/reference/java/io/Closeable.html) Detector for performing optical character recognition(OCR) on an input image.

A text detector is created via `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/FirebaseVision#getVisionTextDetector()`. See the code example below.

     FirebaseVisionTextDetector textDetector =
        FirebaseVision.getInstance().getVisionTextDetector();
     
To perform OCR on an image, you first need to create an instance of `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage` from a `https://developer.android.com/reference/java/nio/ByteBuffer.html`, `https://developer.android.com/reference/android/graphics/Bitmap.html`, etc. See `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage` documentation for more details. For example, the code below creates a `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage` from a `https://developer.android.com/reference/android/graphics/Bitmap.html`.

    FirebaseVisionImage image = FirebaseVisionImage.fromBitmap(bitmap);

Then the code below can detect texts in the supplied `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage`.


     Task<FirebaseVisionText> task = textDetector.detectInImage(image);
     task.addOnSuccessListener(...).addOnFailureListener(...);
     
### Public Method Summary

|---|---|
| void | [close](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionTextDetector#close())() Closes the text detector and release its model resources. |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)\<[FirebaseVisionText](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionText)\> | [detectInImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionTextDetector#detectInImage(com.google.firebase.ml.vision.common.FirebaseVisionImage))([FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage) image) Detects `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionText` from a `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage`. |

### Inherited Method Summary

From class java.lang.Object

|---|---|
| [Object](https://developer.android.com/reference/java/lang/Object.html) | clone() |
| boolean | equals([Object](https://developer.android.com/reference/java/lang/Object.html) arg0) |
| void | finalize() |
| final [Class](https://developer.android.com/reference/java/lang/Class.html)\<?\> | getClass() |
| int | hashCode() |
| final void | notify() |
| final void | notifyAll() |
| [String](https://developer.android.com/reference/java/lang/String.html) | toString() |
| final void | wait(long arg0, int arg1) |
| final void | wait(long arg0) |
| final void | wait() |

From interface java.io.Closeable

|---|---|
| abstract void | close() |

From interface java.lang.AutoCloseable

|---|---|
| abstract void | close() |

## Public Methods

#### public void **close** ()

Closes the text detector and release its model resources.

##### Throws

| [IOException](https://developer.android.com/reference/java/io/IOException.html) |   |
|---|---|

#### public [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)\<[FirebaseVisionText](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionText)\>
**detectInImage** ([FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage) image)

Detects `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionText`
from a `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage`. The OCR is performed asynchronously. Right now, only
the following input types are supported:

For best efficiency, create a `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage` object using one of the following ways:

- `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage#fromMediaImage(android.media.Image, int)` with a `https://developer.android.com/reference/android/graphics/ImageFormat.html#YUV_420_888` formatted image from `https://firebase.google.com/docs/reference/android/reference/android/hardware/camera2/package-summary`.
- `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage#fromByteArray(byte[], com.google.firebase.ml.vision.common.FirebaseVisionImageMetadata)` with a `https://developer.android.com/reference/android/graphics/ImageFormat.html#NV21` formatted image from `https://developer.android.com/reference/android/hardware/Camera.html` (deprecated).
- `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage#fromByteBuffer(java.nio.ByteBuffer, com.google.firebase.ml.vision.common.FirebaseVisionImageMetadata)` if you need to pre-process the image. E.g. allocate a direct `https://developer.android.com/reference/java/nio/ByteBuffer.html` and write processed pixels into the `https://developer.android.com/reference/java/nio/ByteBuffer.html`.

All other `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage` factory methods will work as well, but possibly slightly slower.

##### Returns

- A `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` for `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionText`.