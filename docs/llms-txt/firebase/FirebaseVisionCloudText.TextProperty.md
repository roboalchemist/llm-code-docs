# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.TextProperty.md.txt

# FirebaseVisionCloudText.TextProperty

public static class **FirebaseVisionCloudText.TextProperty** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
Additional information detected on the structural component.  

### Public Method Summary

|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [FirebaseVisionCloudText.DetectedBreak](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.DetectedBreak)                                                                              | [getDetectedBreak](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.TextProperty#getDetectedBreak())() Gets detected start or end of a text segment.                       |
| [List](https://developer.android.com/reference/java/util/List.html)\<[FirebaseVisionCloudText.DetectedLanguage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.DetectedLanguage)\> | [getDetectedLanguages](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.TextProperty#getDetectedLanguages())() Gets a list of detected languages together with confidence. |

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

#### public [FirebaseVisionCloudText.DetectedBreak](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.DetectedBreak) **getDetectedBreak** ()

Gets detected start or end of a text segment.  

#### public [List](https://developer.android.com/reference/java/util/List.html)\<[FirebaseVisionCloudText.DetectedLanguage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.DetectedLanguage)\>
**getDetectedLanguages** ()

Gets a list of detected languages together with confidence.

Returns an empty list if no language is detected.