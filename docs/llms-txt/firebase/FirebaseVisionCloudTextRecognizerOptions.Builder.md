# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionCloudTextRecognizerOptions.Builder.md.txt

# FirebaseVisionCloudTextRecognizerOptions.Builder

public static class **FirebaseVisionCloudTextRecognizerOptions.Builder** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
Builder of [FirebaseVisionCloudTextRecognizerOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionCloudTextRecognizerOptions).  

### Public Constructor Summary

|---|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   | [FirebaseVisionCloudTextRecognizerOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionCloudTextRecognizerOptions.Builder#FirebaseVisionCloudTextRecognizerOptions.Builder())() |

### Public Method Summary

|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [FirebaseVisionCloudTextRecognizerOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionCloudTextRecognizerOptions)                 | [build](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionCloudTextRecognizerOptions.Builder#build())() Builds the [FirebaseVisionCloudTextRecognizerOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionCloudTextRecognizerOptions).                                                   |
| [FirebaseVisionCloudTextRecognizerOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionCloudTextRecognizerOptions.Builder) | [enforceCertFingerprintMatch](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionCloudTextRecognizerOptions.Builder#enforceCertFingerprintMatch())() Only allow registered application instances with matching certificate fingerprint to use Cloud Vision API.                                                                                   |
| [FirebaseVisionCloudTextRecognizerOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionCloudTextRecognizerOptions.Builder) | [setLanguageHints](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionCloudTextRecognizerOptions.Builder#setLanguageHints(java.util.List<java.lang.String>))([List](https://developer.android.com/reference/java/util/List.html)\<[String](https://developer.android.com/reference/java/lang/String.html)\> hintedLanguages) Sets language hints. |
| [FirebaseVisionCloudTextRecognizerOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionCloudTextRecognizerOptions.Builder) | [setModelType](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionCloudTextRecognizerOptions.Builder#setModelType(int))(int modelType) Sets model type for cloud text recognition.                                                                                                                                                                |

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

#### public **FirebaseVisionCloudTextRecognizerOptions.Builder**
()

## Public Methods

#### public [FirebaseVisionCloudTextRecognizerOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionCloudTextRecognizerOptions) **build** ()

Builds the [FirebaseVisionCloudTextRecognizerOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionCloudTextRecognizerOptions).  

#### public [FirebaseVisionCloudTextRecognizerOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionCloudTextRecognizerOptions.Builder) **enforceCertFingerprintMatch** ()

Only allow registered application instances with matching certificate fingerprint to
use Cloud Vision API.

Do not set this for debug build if you use simulators to test.  

#### public [FirebaseVisionCloudTextRecognizerOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionCloudTextRecognizerOptions.Builder) **setLanguageHints** ([List](https://developer.android.com/reference/java/util/List.html)\<[String](https://developer.android.com/reference/java/lang/String.html)\> hintedLanguages)

Sets language hints. In most cases, an empty value yields the best results since it
enables automatic language detection. For languages based on the Latin alphabet,
setting language hints is not needed. In rare cases, when the language of the text in
the image is known, setting a hint will help get better results (although it will be a
significant hindrance if the hint is wrong).

Each language code parameter typically consists of a BCP-47 identifier. See
//cloud.google.com/vision/docs/languages for more details.  

#### public [FirebaseVisionCloudTextRecognizerOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionCloudTextRecognizerOptions.Builder) **setModelType** (int modelType)

Sets model type for cloud text recognition. The two model [SPARSE_MODEL](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionCloudTextRecognizerOptions#SPARSE_MODEL) and [DENSE_MODEL](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionCloudTextRecognizerOptions#DENSE_MODEL) are different models, which could handle different text
densities in an image.