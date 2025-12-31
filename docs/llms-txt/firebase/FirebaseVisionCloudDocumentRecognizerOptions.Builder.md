# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionCloudDocumentRecognizerOptions.Builder.md.txt

# FirebaseVisionCloudDocumentRecognizerOptions.Builder

public static class **FirebaseVisionCloudDocumentRecognizerOptions.Builder** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
Builder of [FirebaseVisionCloudDocumentRecognizerOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionCloudDocumentRecognizerOptions).  

### Public Constructor Summary

|---|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   | [FirebaseVisionCloudDocumentRecognizerOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionCloudDocumentRecognizerOptions.Builder#FirebaseVisionCloudDocumentRecognizerOptions.Builder())() |

### Public Method Summary

|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [FirebaseVisionCloudDocumentRecognizerOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionCloudDocumentRecognizerOptions)                 | [build](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionCloudDocumentRecognizerOptions.Builder#build())() Builds the [FirebaseVisionCloudDocumentRecognizerOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionCloudDocumentRecognizerOptions).                                       |
| [FirebaseVisionCloudDocumentRecognizerOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionCloudDocumentRecognizerOptions.Builder) | [enforceCertFingerprintMatch](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionCloudDocumentRecognizerOptions.Builder#enforceCertFingerprintMatch())() Only allow registered application instances with matching certificate fingerprint to use Cloud Vision API.                                                                                   |
| [FirebaseVisionCloudDocumentRecognizerOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionCloudDocumentRecognizerOptions.Builder) | [setLanguageHints](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionCloudDocumentRecognizerOptions.Builder#setLanguageHints(java.util.List<java.lang.String>))([List](https://developer.android.com/reference/java/util/List.html)\<[String](https://developer.android.com/reference/java/lang/String.html)\> hintedLanguages) Sets language hints. |

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

#### public **FirebaseVisionCloudDocumentRecognizerOptions.Builder**
()

## Public Methods

#### public [FirebaseVisionCloudDocumentRecognizerOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionCloudDocumentRecognizerOptions) **build** ()

Builds the [FirebaseVisionCloudDocumentRecognizerOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionCloudDocumentRecognizerOptions).  

#### public [FirebaseVisionCloudDocumentRecognizerOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionCloudDocumentRecognizerOptions.Builder) **enforceCertFingerprintMatch** ()

Only allow registered application instances with matching certificate fingerprint to
use Cloud Vision API.

Do not set this for debug build if you use simulators to test.  

#### public [FirebaseVisionCloudDocumentRecognizerOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionCloudDocumentRecognizerOptions.Builder) **setLanguageHints** ([List](https://developer.android.com/reference/java/util/List.html)\<[String](https://developer.android.com/reference/java/lang/String.html)\> hintedLanguages)

Sets language hints. In most cases, an empty value yields the best results since it
enables automatic language detection. For languages based on the Latin alphabet,
setting language hints is not needed. In rare cases, when the language of the text in
the image is known, setting a hint will help get better results (although it will be a
significant hindrance if the hint is wrong).

Each language code parameter typically consists of a BCP-47 identifier. See
//cloud.google.com/vision/docs/languages for more details.