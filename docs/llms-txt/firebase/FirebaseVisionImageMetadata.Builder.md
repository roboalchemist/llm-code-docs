# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImageMetadata.Builder.md.txt

# FirebaseVisionImageMetadata.Builder

public static class **FirebaseVisionImageMetadata.Builder** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
Builder class of [FirebaseVisionImageMetadata](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImageMetadata).  

### Public Constructor Summary

|---|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   | [FirebaseVisionImageMetadata.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImageMetadata.Builder#FirebaseVisionImageMetadata.Builder())() Creates a new builder to build [FirebaseVisionImageMetadata](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImageMetadata). |

### Public Method Summary

|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [FirebaseVisionImageMetadata](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImageMetadata)                 | [build](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImageMetadata.Builder#build())() Builds an instance of [FirebaseVisionImageMetadata](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImageMetadata). |
| [FirebaseVisionImageMetadata.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImageMetadata.Builder) | [setFormat](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImageMetadata.Builder#setFormat(int))(int format) Sets the format of the image stored in [ByteBuffer](https://developer.android.com/reference/java/nio/ByteBuffer.html).                               |
| [FirebaseVisionImageMetadata.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImageMetadata.Builder) | [setHeight](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImageMetadata.Builder#setHeight(int))(int height) Sets height of the image, which must be a positive integer.                                                                                          |
| [FirebaseVisionImageMetadata.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImageMetadata.Builder) | [setRotation](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImageMetadata.Builder#setRotation(int))(int rotation) Sets rotation of the image, indicating the rotation from the upright orientation.                                                              |
| [FirebaseVisionImageMetadata.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImageMetadata.Builder) | [setWidth](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImageMetadata.Builder#setWidth(int))(int width) Sets width of the image, which must be a positive integer.                                                                                              |

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

## Public Constructors

#### public **FirebaseVisionImageMetadata.Builder** ()

Creates a new builder to build [FirebaseVisionImageMetadata](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImageMetadata).

## Public Methods

#### public [FirebaseVisionImageMetadata](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImageMetadata) **build**
()

Builds an instance of [FirebaseVisionImageMetadata](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImageMetadata).  

#### public [FirebaseVisionImageMetadata.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImageMetadata.Builder) **setFormat** (int format)

Sets the format of the image stored in [ByteBuffer](https://developer.android.com/reference/java/nio/ByteBuffer.html). It
must be one of [FirebaseVisionImageMetadata.ImageFormat](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImageMetadata.ImageFormat).  

#### public [FirebaseVisionImageMetadata.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImageMetadata.Builder) **setHeight** (int height)

Sets height of the image, which must be a positive integer.  

#### public [FirebaseVisionImageMetadata.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImageMetadata.Builder) **setRotation** (int rotation)

Sets rotation of the image, indicating the rotation from the upright
orientation.

Since the camera may deliver images that are rotated (e.g., if the user holds the
device upside down), specifying the rotation with the image indicates how to make the
image upright.

Currently, only [ROTATION_0](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImageMetadata#ROTATION_0), [ROTATION_90](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImageMetadata#ROTATION_90), [ROTATION_180](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImageMetadata#ROTATION_180) and [ROTATION_270](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImageMetadata#ROTATION_270) are supported.  

#### public [FirebaseVisionImageMetadata.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImageMetadata.Builder) **setWidth** (int width)

Sets width of the image, which must be a positive integer.