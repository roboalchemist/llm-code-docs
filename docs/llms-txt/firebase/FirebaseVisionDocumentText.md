# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionDocumentText.md.txt

# FirebaseVisionDocumentText

public class **FirebaseVisionDocumentText** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
Represents detected text by [FirebaseVisionDocumentTextRecognizer](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionDocumentTextRecognizer).  

### Nested Class Summary

|-------|---|---|----------------------------------------------------------------------------|
| class | [FirebaseVisionDocumentText.Block](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionDocumentText.Block) || A logical element on the page.                                             |
| class | [FirebaseVisionDocumentText.Paragraph](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionDocumentText.Paragraph) || A structural unit of text representing a number of words in certain order. |
| class | [FirebaseVisionDocumentText.RecognizedBreak](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionDocumentText.RecognizedBreak) || Detected start or end of a structural component.                           |
| class | [FirebaseVisionDocumentText.Symbol](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionDocumentText.Symbol) || A single symbol representation.                                            |
| class | [FirebaseVisionDocumentText.Word](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionDocumentText.Word) || A single word representation.                                              |

### Public Method Summary

|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [List](https://developer.android.com/reference/java/util/List.html)\<[FirebaseVisionDocumentText.Block](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionDocumentText.Block)\> | [getBlocks](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionDocumentText#getBlocks())() Gets the [List](https://developer.android.com/reference/java/util/List.html) of [FirebaseVisionDocumentText.Block](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionDocumentText.Block)s. |
| [String](https://developer.android.com/reference/java/lang/String.html)                                                                                                                                                               | [getText](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionDocumentText#getText())() Gets the detected text.                                                                                                                                                                                                                              |

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

#### public [List](https://developer.android.com/reference/java/util/List.html)\<[FirebaseVisionDocumentText.Block](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionDocumentText.Block)\>
**getBlocks** ()

Gets the [List](https://developer.android.com/reference/java/util/List.html) of
[FirebaseVisionDocumentText.Block](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionDocumentText.Block)s.  

#### public [String](https://developer.android.com/reference/java/lang/String.html) **getText** ()

Gets the detected text. Returns empty string if nothing is found.