# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionCloudImageLabelerOptions.md.txt

# FirebaseVisionCloudImageLabelerOptions

public class **FirebaseVisionCloudImageLabelerOptions** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
Options for cloud image labeler. Confidence threshold could be provided for the label
detection.

For example, if the confidence threshold is set to 0.7, only labels with confidence \>=
0.7 would be returned. The default threshold is 0.5.

Note: at most 20 labels will be returned for cloud image labeler.  

### Nested Class Summary

|-------|---|---|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| class | [FirebaseVisionCloudImageLabelerOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionCloudImageLabelerOptions.Builder) || Builder of [FirebaseVisionOnDeviceImageLabelerOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionOnDeviceImageLabelerOptions). |

### Public Method Summary

|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| boolean | [equals](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionCloudImageLabelerOptions#equals(java.lang.Object))([Object](https://developer.android.com/reference/java/lang/Object.html) o)                                                                             |
| float   | [getConfidenceThreshold](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionCloudImageLabelerOptions#getConfidenceThreshold())() Gets the confidence threshold of labels to be detected.                                                                              |
| int     | [hashCode](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionCloudImageLabelerOptions#hashCode())()                                                                                                                                                                  |
| boolean | [isEnforceCertFingerprintMatch](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionCloudImageLabelerOptions#isEnforceCertFingerprintMatch())() Checks if Cloud Vision API can only be used by registered application instances with matching certificate fingerprint. |

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

#### public boolean **equals** ([Object](https://developer.android.com/reference/java/lang/Object.html) o)

#### public float **getConfidenceThreshold** ()

Gets the confidence threshold of labels to be detected.  

#### public int **hashCode** ()

#### public boolean **isEnforceCertFingerprintMatch** ()

Checks if Cloud Vision API can only be used by registered application instances with
matching certificate fingerprint.