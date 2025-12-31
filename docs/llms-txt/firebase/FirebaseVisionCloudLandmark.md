# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/landmark/FirebaseVisionCloudLandmark.md.txt

# FirebaseVisionCloudLandmark

public class **FirebaseVisionCloudLandmark** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
Represents a detected landmark by [FirebaseVisionCloudLandmark](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/landmark/FirebaseVisionCloudLandmark).  

### Public Method Summary

|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Rect](https://developer.android.com/reference/android/graphics/Rect.html)                                                                                                                                  | [getBoundingBox](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/landmark/FirebaseVisionCloudLandmark#getBoundingBox())() Gets image region of the detected landmark.        |
| float                                                                                                                                                                                                       | [getConfidence](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/landmark/FirebaseVisionCloudLandmark#getConfidence())() Gets overall confidence of the result.               |
| [String](https://developer.android.com/reference/java/lang/String.html)                                                                                                                                     | [getEntityId](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/landmark/FirebaseVisionCloudLandmark#getEntityId())() Gets opaque entity ID.                                   |
| [String](https://developer.android.com/reference/java/lang/String.html)                                                                                                                                     | [getLandmark](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/landmark/FirebaseVisionCloudLandmark#getLandmark())() Gets the detected landmark.                              |
| [List](https://developer.android.com/reference/java/util/List.html)\<[FirebaseVisionLatLng](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionLatLng)\> | [getLocations](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/landmark/FirebaseVisionCloudLandmark#getLocations())() Gets the location information for the detected entity. |

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

#### public [Rect](https://developer.android.com/reference/android/graphics/Rect.html) **getBoundingBox** ()

Gets image region of the detected landmark. Returns null if nothing was
detected.  

#### public float **getConfidence** ()

Gets overall confidence of the result. Range \[0.0f, 1.0f\].  

#### public [String](https://developer.android.com/reference/java/lang/String.html) **getEntityId** ()

Gets opaque entity ID. Some IDs may be available in [Google Knowledge Graph Search API](https://developers.google.com/knowledge-graph/)  

#### public [String](https://developer.android.com/reference/java/lang/String.html) **getLandmark** ()

Gets the detected landmark.  

#### public [List](https://developer.android.com/reference/java/util/List.html)\<[FirebaseVisionLatLng](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionLatLng)\>
**getLocations** ()

Gets the location information for the detected entity. Multiple [FirebaseVisionLatLng](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionLatLng) elements can be present because one location may
indicate the location of the scene in the image, and another location may indicate the
location of the place where the image was taken. Location information is usually
present for landmarks.