# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.md.txt

# FirebaseVisionCloudText

public class **FirebaseVisionCloudText** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
Represents detected text by [FirebaseVisionCloudTextDetector](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudTextDetector) or [FirebaseVisionCloudDocumentTextDetector](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudDocumentTextDetector).  

### Nested Class Summary

|-------|---|---|----------------------------------------------------------------------------|
| class | [FirebaseVisionCloudText.Block](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.Block) || A logical element on the page.                                             |
| class | [FirebaseVisionCloudText.DetectedBreak](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.DetectedBreak) || Detected start or end of a structural component.                           |
| class | [FirebaseVisionCloudText.DetectedLanguage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.DetectedLanguage) || Detected language for a structural component.                              |
| class | [FirebaseVisionCloudText.Page](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.Page) || Detected page from cloud OCR engine.                                       |
| class | [FirebaseVisionCloudText.Paragraph](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.Paragraph) || A structural unit of text representing a number of words in certain order. |
| class | [FirebaseVisionCloudText.Symbol](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.Symbol) || A single symbol representation.                                            |
| class | [FirebaseVisionCloudText.TextProperty](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.TextProperty) || Additional information detected on the structural component.               |
| class | [FirebaseVisionCloudText.Word](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.Word) || A single word representation.                                              |

### Public Method Summary

|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [List](https://developer.android.com/reference/java/util/List.html)\<[FirebaseVisionCloudText.Page](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.Page)\> | [getPages](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText#getPages())() Gets the [List](https://developer.android.com/reference/java/util/List.html) of [FirebaseVisionCloudText.Page](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.Page)s. |
| [String](https://developer.android.com/reference/java/lang/String.html)                                                                                                                                                         | [getText](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText#getText())() Gets the detected text.                                                                                                                                                                                                                      |

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

#### public [List](https://developer.android.com/reference/java/util/List.html)\<[FirebaseVisionCloudText.Page](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.Page)\>
**getPages** ()

Gets the [List](https://developer.android.com/reference/java/util/List.html) of
[FirebaseVisionCloudText.Page](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.Page)s.  

#### public [String](https://developer.android.com/reference/java/lang/String.html) **getText** ()

Gets the detected text. Returns empty string if nothing is found.