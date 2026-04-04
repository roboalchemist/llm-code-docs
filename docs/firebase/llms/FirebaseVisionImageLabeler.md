# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionImageLabeler.md.txt

# FirebaseVisionImageLabeler

public class **FirebaseVisionImageLabeler** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
implements [Closeable](https://developer.android.com/reference/java/io/Closeable.html)  
Used for finding [FirebaseVisionImageLabel](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionImageLabel)s
in a supplied image.

There are two types of image labeler, one runs inference on device, the other on cloud. On
device image labler is created via [getOnDeviceImageLabeler(FirebaseVisionOnDeviceImageLabelerOptions)](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/FirebaseVision#getOnDeviceImageLabeler(com.google.firebase.ml.vision.label.FirebaseVisionOnDeviceImageLabelerOptions)) or
[getOnDeviceImageLabeler()](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/FirebaseVision#getOnDeviceImageLabeler()) if you wish to use the default options. For example, the
code below creates an on device image labler with default options. Cloud image labler is
created via [getCloudImageLabeler(FirebaseVisionCloudImageLabelerOptions)](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/FirebaseVision#getCloudImageLabeler(com.google.firebase.ml.vision.label.FirebaseVisionCloudImageLabelerOptions)), or [getCloudImageLabeler()](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/FirebaseVision#getCloudImageLabeler()) if you wish to use the default options. For example, the
code below creates a cloud image labler with default options.  

     getOnDeviceImageLabeler imageLabeler =
        FirebaseVision.getInstance().getOnDeviceImageLabeler();
     
or  

     getOnDeviceImageLabeler imageLabeler =
        FirebaseVision.getInstance().getCloudImageLabeler();
     
To perform label detection in an image, you first need to create an instance of [FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage) from a [Bitmap](https://developer.android.com/reference/android/graphics/Bitmap.html), [ByteBuffer](https://developer.android.com/reference/java/nio/ByteBuffer.html), etc. See [FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage) documentation for more details. For example, the code below creates a [FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage) from a [Bitmap](https://developer.android.com/reference/android/graphics/Bitmap.html).  

          FirebaseVisionImage image = FirebaseVisionImage.fromBitmap(bitmap);

Then the code below can detect labels in the supplied [FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage).  


     Task<List<FirebaseVisionImageLabel>> task = imageLabeler.processImage(image);
     task.addOnSuccessListener(...).addOnFailureListener(...);
     
### Nested Class Summary

|------------|---|---|----------------------|
| @interface | [FirebaseVisionImageLabeler.ImageLabelerType](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionImageLabeler.ImageLabelerType) || Image Labeler types. |

### Constant Summary

|-----|--------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| int | [CLOUD](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionImageLabeler#CLOUD)                       | Indicates that the labeler is using a cloud model, meaning that the model inference occurs in the cloud. |
| int | [ON_DEVICE](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionImageLabeler#ON_DEVICE)               | Indicates that the labeler is using an on-device base model.                                             |
| int | [ON_DEVICE_AUTOML](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionImageLabeler#ON_DEVICE_AUTOML) | Indicates that the labeler is using an on-device AutoML model.                                           |

### Public Method Summary

|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| void                                                                                                                                                                                                                                                                                                                 | [close](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionImageLabeler#close())()                                                                                                                                                                                                                                                         |
| int                                                                                                                                                                                                                                                                                                                  | [getImageLabelerType](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionImageLabeler#getImageLabelerType())() Gets image labeler type.                                                                                                                                                                                                    |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)\<[List](https://developer.android.com/reference/java/util/List.html)\<[FirebaseVisionImageLabel](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionImageLabel)\>\> | [processImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionImageLabeler#processImage(com.google.firebase.ml.vision.common.FirebaseVisionImage))([FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage) image) Detects image labels from supplied image. |

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

From interface java.io.Closeable  

|---------------|---------|
| abstract void | close() |

From interface java.lang.AutoCloseable  

|---------------|---------|
| abstract void | close() |

## Constants

#### public static final int
**CLOUD**

Indicates that the labeler is using a cloud model, meaning that the model inference
occurs in the cloud.  
Constant Value: 2  

#### public static final int
**ON_DEVICE**

Indicates that the labeler is using an on-device base model.  
Constant Value: 1  

#### public static final int
**ON_DEVICE_AUTOML**

Indicates that the labeler is using an on-device AutoML model.  
Constant Value: 3

## Public Methods

#### public void **close** ()

##### Throws

| [IOException](https://developer.android.com/reference/java/io/IOException.html) |   |
|---------------------------------------------------------------------------------|---|

#### public int **getImageLabelerType** ()

Gets image labeler type.  

##### See Also

- [FirebaseVisionImageLabeler.ImageLabelerType](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionImageLabeler.ImageLabelerType)  

#### public [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)\<[List](https://developer.android.com/reference/java/util/List.html)\<[FirebaseVisionImageLabel](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionImageLabel)\>\>
**processImage** ([FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage) image)

Detects image labels from supplied image.

For best efficiency, create a [FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage) object from [fromBitmap(android.graphics.Bitmap)](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage#fromBitmap(android.graphics.Bitmap)). All other [FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage) factory methods will work as well, but possibly slightly
slower.  

##### Returns

- A [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html) that asynchronously returns a [List](https://developer.android.com/reference/java/util/List.html) of detected [FirebaseVisionImageLabel](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionImageLabel)s.