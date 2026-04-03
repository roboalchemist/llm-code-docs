# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionDocumentText.Symbol.md.txt

# FirebaseVisionDocumentText.Symbol

public static class **FirebaseVisionDocumentText.Symbol** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
A single symbol representation.  

### Public Method Summary

|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Rect](https://developer.android.com/reference/android/graphics/Rect.html)                                                                                                                            | [getBoundingBox](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionDocumentText.Symbol#getBoundingBox())() Gets the bounding box for the recognized text.            |
| [Float](https://developer.android.com/reference/java/lang/Float.html)                                                                                                                                 | [getConfidence](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionDocumentText.Symbol#getConfidence())() Gets confidence of the OCR results for the recognized text. |
| [FirebaseVisionDocumentText.RecognizedBreak](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionDocumentText.RecognizedBreak)                    | [getRecognizedBreak](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionDocumentText.Symbol#getRecognizedBreak())() Gets the recognized break.                        |
| [List](https://developer.android.com/reference/java/util/List.html)\<[RecognizedLanguage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/RecognizedLanguage)\> | [getRecognizedLanguages](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionDocumentText.Symbol#getRecognizedLanguages())() Gets the recognized languages.            |
| [String](https://developer.android.com/reference/java/lang/String.html)                                                                                                                               | [getText](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionDocumentText.Symbol#getText())() Gets the UTF-8 representation of the recognized text.                   |

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

Gets the bounding box for the recognized text.  

#### public [Float](https://developer.android.com/reference/java/lang/Float.html) **getConfidence** ()

Gets confidence of the OCR results for the recognized text.

Returns null if no confidence available. Otherwise, its range is \[0.0f, 1.0f\].  

#### public [FirebaseVisionDocumentText.RecognizedBreak](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionDocumentText.RecognizedBreak) **getRecognizedBreak** ()

Gets the recognized break.  

#### public [List](https://developer.android.com/reference/java/util/List.html)\<[RecognizedLanguage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/RecognizedLanguage)\>
**getRecognizedLanguages** ()

Gets the recognized languages.  

#### public [String](https://developer.android.com/reference/java/lang/String.html) **getText** ()

Gets the UTF-8 representation of the recognized text.

Returns an empty string if nothing is found.