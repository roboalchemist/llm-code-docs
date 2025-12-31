# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImageMetadata.md.txt

# FirebaseVisionImageMetadata

public class **FirebaseVisionImageMetadata** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
Image metadata used by [FirebaseVision](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/FirebaseVision)
detectors.  

### Nested Class Summary

|------------|---|---|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| class      | [FirebaseVisionImageMetadata.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImageMetadata.Builder) || Builder class of [FirebaseVisionImageMetadata](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImageMetadata). |
| @interface | [FirebaseVisionImageMetadata.ImageFormat](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImageMetadata.ImageFormat) || Accepted image format of vision APIs.                                                                                                                                |
| @interface | [FirebaseVisionImageMetadata.Rotation](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImageMetadata.Rotation) || Indicates the image rotation.                                                                                                                                        |

### Constant Summary

|-----|------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| int | [IMAGE_FORMAT_NV21](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImageMetadata#IMAGE_FORMAT_NV21) | See [NV21](https://developer.android.com/reference/android/graphics/ImageFormat.html#NV21) |
| int | [IMAGE_FORMAT_YV12](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImageMetadata#IMAGE_FORMAT_YV12) | See [YV12](https://developer.android.com/reference/android/graphics/ImageFormat.html#YV12) |
| int | [ROTATION_0](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImageMetadata#ROTATION_0)               | 0 degree rotation (natural orientation).                                                   |
| int | [ROTATION_180](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImageMetadata#ROTATION_180)           | 180 degree rotation.                                                                       |
| int | [ROTATION_270](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImageMetadata#ROTATION_270)           | 270 degree rotation.                                                                       |
| int | [ROTATION_90](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImageMetadata#ROTATION_90)             | 90 degree rotation.                                                                        |

### Public Constructor Summary

|---|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   | [FirebaseVisionImageMetadata](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImageMetadata#FirebaseVisionImageMetadata(com.google.firebase.ml.vision.common.FirebaseVisionImageMetadata))([FirebaseVisionImageMetadata](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImageMetadata) metadata) Copies the content of another [FirebaseVisionImageMetadata](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImageMetadata). |

### Public Method Summary

|-----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| int | [getFormat](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImageMetadata#getFormat())() Gets the specified format of the image.       |
| int | [getHeight](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImageMetadata#getHeight())() Gets the specified height of the image.       |
| int | [getRotation](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImageMetadata#getRotation())() Gets the specified rotation of the image. |
| int | [getWidth](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImageMetadata#getWidth())() Gets the specified width of the image.          |

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

## Constants

#### public static final int
**IMAGE_FORMAT_NV21**

See [NV21](https://developer.android.com/reference/android/graphics/ImageFormat.html#NV21)  
Constant Value: 17  

#### public static final int
**IMAGE_FORMAT_YV12**

See [YV12](https://developer.android.com/reference/android/graphics/ImageFormat.html#YV12)  
Constant Value: 842094169  

#### public static final int
**ROTATION_0**

0 degree rotation (natural orientation).  
Constant Value: 0  

#### public static final int
**ROTATION_180**

180 degree rotation.  
Constant Value: 2  

#### public static final int
**ROTATION_270**

270 degree rotation.  
Constant Value: 3  

#### public static final int
**ROTATION_90**

90 degree rotation.  
Constant Value: 1

## Public Constructors

#### public **FirebaseVisionImageMetadata** ([FirebaseVisionImageMetadata](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImageMetadata) metadata)

Copies the content of another [FirebaseVisionImageMetadata](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImageMetadata).

## Public Methods

#### public int **getFormat** ()

Gets the specified format of the image.  

#### public int **getHeight** ()

Gets the specified height of the image.  

#### public int **getRotation** ()

Gets the specified rotation of the image.  

#### public int **getWidth** ()

Gets the specified width of the image.