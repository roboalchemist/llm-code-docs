# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/label/FirebaseVisionCloudLabel.md.txt

# FirebaseVisionCloudLabel

public class **FirebaseVisionCloudLabel** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
Represents an image label detected by [FirebaseVisionCloudLabelDetector](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/label/FirebaseVisionCloudLabelDetector).  

### Public Method Summary

|-------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| float                                                                   | [getConfidence](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/label/FirebaseVisionCloudLabel#getConfidence())() Gets overall confidence of the result. |
| [String](https://developer.android.com/reference/java/lang/String.html) | [getEntityId](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/label/FirebaseVisionCloudLabel#getEntityId())() Gets opaque entity ID.                     |
| [String](https://developer.android.com/reference/java/lang/String.html) | [getLabel](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/label/FirebaseVisionCloudLabel#getLabel())() Gets a detected label from the given image.      |

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

#### public float **getConfidence** ()

Gets overall confidence of the result. Range \[0.0f, 1.0f\].  

#### public [String](https://developer.android.com/reference/java/lang/String.html) **getEntityId** ()

Gets opaque entity ID. IDs are available in [Google Knowledge Graph Search API](https://developers.google.com/knowledge-graph/)  

#### public [String](https://developer.android.com/reference/java/lang/String.html) **getLabel** ()

Gets a detected label from the given image. The label returned here is in English
only. The end developer should use [getEntityId()](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/label/FirebaseVisionCloudLabel#getEntityId()) to retrieve unique id.