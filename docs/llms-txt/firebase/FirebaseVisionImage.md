# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage.md.txt

# FirebaseVisionImage

public class **FirebaseVisionImage** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
Represents an image object that can be used for both on-device and cloud API
detectors.  

### Public Method Summary

|-------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| static [FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage) | [fromBitmap](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage#fromBitmap(android.graphics.Bitmap))([Bitmap](https://developer.android.com/reference/android/graphics/Bitmap.html) bitmap) Creates a [FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage) from a [Bitmap](https://developer.android.com/reference/android/graphics/Bitmap.html), where the object in the image should be already up-right and no rotation is needed.                                                                                                                                                    |
| static [FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage) | [fromByteArray](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage#fromByteArray(byte[], com.google.firebase.ml.vision.common.FirebaseVisionImageMetadata))(byte\[\] byteArray, [FirebaseVisionImageMetadata](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImageMetadata) metadata) Creates a [FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage) from a byte array, e.g.                                                                                                                                                      |
| static [FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage) | [fromByteBuffer](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage#fromByteBuffer(java.nio.ByteBuffer, com.google.firebase.ml.vision.common.FirebaseVisionImageMetadata))([ByteBuffer](https://developer.android.com/reference/java/nio/ByteBuffer.html) byteBuffer, [FirebaseVisionImageMetadata](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImageMetadata) metadata) Creates a [FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage) from a [ByteBuffer](https://developer.android.com/reference/java/nio/ByteBuffer.html). |
| static [FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage) | [fromFilePath](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage#fromFilePath(android.content.Context, android.net.Uri))([Context](https://developer.android.com/reference/android/content/Context.html) context, [Uri](https://developer.android.com/reference/android/net/Uri.html) imageUri) Creates a [FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage) from a local image file Uri.                                                                                                                                                                                             |
| static [FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage) | [fromMediaImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage#fromMediaImage(android.media.Image, int))([Image](https://developer.android.com/reference/android/media/Image.html) image, int rotation) Creates a [FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage) from a [Image](https://developer.android.com/reference/android/media/Image.html) object, e.g.                                                                                                                                                                                                                |
| [Bitmap](https://developer.android.com/reference/android/graphics/Bitmap.html)                                                            | [getBitmap](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage#getBitmap())() Returns its bitmap representation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

### Inherited Method Summary

From class java.lang.Object  

|----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| [Object](https://developer.android.com/reference/java/lang/Object.html)          | clone()                                                                              |
| boolean                                                                          | equals([Object](https://developer.android.com/reference/java/lang/Object.html) arg0) |
| void                                                                             | finalize()                                                                           |
| final [Class](https://developer.android.com/reference/java/lang/Class.html)\<?\> | getClass()                                                                           |
| int                                                                              | hashCode()                                                                           |
| final void                                                                       | notify()                                                                             |
| final void                                                                       | notifyAll()                                                                          |
| [String](https://developer.android.com/reference/java/lang/String.html)          | toString()                                                                           |
| final void                                                                       | wait(long arg0, int arg1)                                                            |
| final void                                                                       | wait(long arg0)                                                                      |
| final void                                                                       | wait()                                                                               |

## Public Methods

#### public static [FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage)
**fromBitmap** ([Bitmap](https://developer.android.com/reference/android/graphics/Bitmap.html) bitmap)

Creates a [FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage) from a [Bitmap](https://developer.android.com/reference/android/graphics/Bitmap.html),
where the object in the image should be already up-right and no rotation is needed.  

#### public static [FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage)
**fromByteArray** (byte\[\] byteArray, [FirebaseVisionImageMetadata](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImageMetadata) metadata)

Creates a [FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage) from a byte array, e.g. what you get from [Camera](https://developer.android.com/reference/android/hardware/Camera.html)
callback.  

#### public static [FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage)
**fromByteBuffer** ([ByteBuffer](https://developer.android.com/reference/java/nio/ByteBuffer.html) byteBuffer, [FirebaseVisionImageMetadata](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImageMetadata) metadata)

Creates a [FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage) from a [ByteBuffer](https://developer.android.com/reference/java/nio/ByteBuffer.html).

We assume the entire buffer from position zero to its limit is all image data.  

#### public static [FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage)
**fromFilePath** ([Context](https://developer.android.com/reference/android/content/Context.html) context, [Uri](https://developer.android.com/reference/android/net/Uri.html) imageUri)

Creates a [FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage) from a local image file Uri.  

##### Throws

| [IOException](https://developer.android.com/reference/java/io/IOException.html) | if the image could not be retrieved from the specified imageUri. This could happen even if the Uri came from content chooser, e.g. some users might have content providers for remote resources. |
|---------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

#### public static [FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage)
**fromMediaImage** ([Image](https://developer.android.com/reference/android/media/Image.html) image, int rotation)

Creates a [FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage) from a [Image](https://developer.android.com/reference/android/media/Image.html) object,
e.g. what you obtained from [android.hardware.camera2
API](https://developer.android.com/reference/android/hardware/camera2/package-summary).

Note that we only support JPEG / YUV_420_888 formats at this moment. If you are
using cloud vision detectors, JPEG format is recommended; if you are using on-device
detectors, YUV_420_888 will be more efficient.

After you get back a [FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage), it's safe to close the input [Image](https://developer.android.com/reference/android/media/Image.html).  

##### Parameters

|  image   |                                                                                                                                                                                                                                                        |
| rotation | The camera rotation, e.g. `ROTATION_90` for back camera landscape mode. See also [FirebaseVisionImageMetadata.Rotation](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImageMetadata.Rotation). |
|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

#### public [Bitmap](https://developer.android.com/reference/android/graphics/Bitmap.html)
**getBitmap** ()

Returns its bitmap representation.

The image will be rotated to up-right if it's created with rotation info via
[setRotation(int)](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImageMetadata.Builder#setRotation(int)).