# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionText.Element.md.txt

# FirebaseVisionText.Element

public static class **FirebaseVisionText.Element** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
Roughly equivalent to a space-separated "word" in most Latin languages, or a character in
others. For instance, if a word is split between two lines by a hyphen, each part is encoded
as a separate Element.  

### Public Method Summary

|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Rect](https://developer.android.com/reference/android/graphics/Rect.html)                                                                                                                            | [getBoundingBox](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionText.Element#getBoundingBox())() Returns the axis-aligned bounding rectangle of the detected text.             |
| [Float](https://developer.android.com/reference/java/lang/Float.html)                                                                                                                                 | [getConfidence](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionText.Element#getConfidence())() The confidence of the recognized text.                                          |
| [Point\[\]](https://developer.android.com/reference/android/graphics/Point.html)                                                                                                                      | [getCornerPoints](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionText.Element#getCornerPoints())() Gets the four corner points in clockwise direction starting with top-left.  |
| [List](https://developer.android.com/reference/java/util/List.html)\<[RecognizedLanguage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/RecognizedLanguage)\> | [getRecognizedLanguages](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionText.Element#getRecognizedLanguages())() Gets a list of recognized languages together with confidence. |
| [String](https://developer.android.com/reference/java/lang/String.html)                                                                                                                               | [getText](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionText.Element#getText())() Gets the recognized text as a string.                                                       |

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

Returns the axis-aligned bounding rectangle of the detected text.  

#### public [Float](https://developer.android.com/reference/java/lang/Float.html) **getConfidence** ()

The confidence of the recognized text.

The value is returned only for cloud recognizers that are configured with
[DENSE_MODEL](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionCloudTextRecognizerOptions#DENSE_MODEL).  

#### public [Point\[\]](https://developer.android.com/reference/android/graphics/Point.html)
**getCornerPoints** ()

Gets the four corner points in clockwise direction starting with top-left. Due to
the possible perspective distortions, this is not necessarily a rectangle. Parts of the
region could be outside of the image.

The value is only valid for on-device text recognition.  

#### public [List](https://developer.android.com/reference/java/util/List.html)\<[RecognizedLanguage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/RecognizedLanguage)\>
**getRecognizedLanguages** ()

Gets a list of recognized languages together with confidence. (Cloud API only.)  

#### public [String](https://developer.android.com/reference/java/lang/String.html) **getText** ()

Gets the recognized text as a string. Returned in reading order for the language.
For Latin, this is top to bottom within a TextBlock, and left-to-right within a
Line.

Returns an empty string if nothing is found.