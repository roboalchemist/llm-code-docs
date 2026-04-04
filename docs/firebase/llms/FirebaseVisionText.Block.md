# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionText.Block.md.txt

# FirebaseVisionText.Block

public static class **FirebaseVisionText.Block** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
A block of text (think of it as a paragraph) as deemed by the OCR engine.  

### Public Method Summary

|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Rect](https://developer.android.com/reference/android/graphics/Rect.html)                                                                                                                                                   | [getBoundingBox](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionText.Block#getBoundingBox())() Returns the axis-aligned bounding rectangle of the detected text.                                                                                                                        |
| [Point\[\]](https://developer.android.com/reference/android/graphics/Point.html)                                                                                                                                             | [getCornerPoints](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionText.Block#getCornerPoints())() Gets the four corner points in clockwise direction starting with top-left.                                                                                                             |
| synchronized [List](https://developer.android.com/reference/java/util/List.html)\<[FirebaseVisionText.Line](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionText.Line)\> | [getLines](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionText.Block#getLines())() Gets an unmodifiable list of [FirebaseVisionText.Line](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionText.Line)s that make up this text block. |
| [String](https://developer.android.com/reference/java/lang/String.html)                                                                                                                                                      | [getText](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionText.Block#getText())() Gets the recognized text as a string.                                                                                                                                                                  |

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

#### public [Point\[\]](https://developer.android.com/reference/android/graphics/Point.html)
**getCornerPoints** ()

Gets the four corner points in clockwise direction starting with top-left. Due to
the possible perspective distortions, this is not necessarily a rectangle. Parts of the
region could be outside of the image.  

#### public synchronized [List](https://developer.android.com/reference/java/util/List.html)\<[FirebaseVisionText.Line](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionText.Line)\>
**getLines** ()

Gets an unmodifiable list of [FirebaseVisionText.Line](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionText.Line)s that make up this text block.  

#### public [String](https://developer.android.com/reference/java/lang/String.html) **getText** ()

Gets the recognized text as a string. Returned in reading order for the language.
For Latin, this is top to bottom within a Block, and left-to-right within a Line.

Returns an empty string if nothing is found.