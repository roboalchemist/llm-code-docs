# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionText.md.txt

# FirebaseVisionText

public class **FirebaseVisionText** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
A hierarchical representation of texts.

A [FirebaseVisionText](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionText)
contains a list of [FirebaseVisionText.TextBlock](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionText.TextBlock), and a [FirebaseVisionText.TextBlock](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionText.TextBlock) contains a list of [FirebaseVisionText.Line](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionText.Line)
which is composed of a list of [FirebaseVisionText.Element](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionText.Element).  

### Nested Class Summary

|-------|---|---|---------------------------------------------------------------------------------------------------|
| class | [FirebaseVisionText.Element](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionText.Element) || Roughly equivalent to a space-separated "word" in most Latin languages, or a character in others. |
| class | [FirebaseVisionText.Line](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionText.Line) || Represents a line of text.                                                                        |
| class | [FirebaseVisionText.TextBlock](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionText.TextBlock) || A block of text (think of it as a paragraph) as deemed by the OCR engine.                         |

### Public Method Summary

|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [String](https://developer.android.com/reference/java/lang/String.html)                                                                                                                                                   | [getText](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionText#getText())() Retrieve the recognized text as a string.                                                                                                                                                                                                                                                                                                                                                                  |
| [List](https://developer.android.com/reference/java/util/List.html)\<[FirebaseVisionText.TextBlock](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionText.TextBlock)\> | [getTextBlocks](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionText#getTextBlocks())() Gets an unmodifiable list of [FirebaseVisionText.TextBlock](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionText.TextBlock), which is a block of text and can be further decomposed to a list of [FirebaseVisionText.Line](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionText.Line). |

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

#### public [String](https://developer.android.com/reference/java/lang/String.html) **getText** ()

Retrieve the recognized text as a string.  

#### public [List](https://developer.android.com/reference/java/util/List.html)\<[FirebaseVisionText.TextBlock](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionText.TextBlock)\>
**getTextBlocks** ()

Gets an unmodifiable list of [FirebaseVisionText.TextBlock](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionText.TextBlock), which is a block of text and can be further
decomposed to a list of [FirebaseVisionText.Line](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionText.Line).