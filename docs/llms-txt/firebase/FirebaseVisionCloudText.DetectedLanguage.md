# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.DetectedLanguage.md.txt

# FirebaseVisionCloudText.DetectedLanguage

public static class **FirebaseVisionCloudText.DetectedLanguage** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
Detected language for a structural component.  

### Public Method Summary

|-------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| float                                                                   | [getConfidence](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.DetectedLanguage#getConfidence())() Gets confidence of detected language.                       |
| [String](https://developer.android.com/reference/java/lang/String.html) | [getLanguageCode](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.DetectedLanguage#getLanguageCode())() The BCP-47 language code, such as "en-US" or "sr-Latn". |

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

Gets confidence of detected language. Range \[0.0f, 1.0f\].  

#### public [String](https://developer.android.com/reference/java/lang/String.html) **getLanguageCode** ()

The BCP-47 language code, such as "en-US" or "sr-Latn". For more information, see
[Unicode Locale Identifier](https://www.unicode.org/reports/tr35/#Unicode_locale_identifier)