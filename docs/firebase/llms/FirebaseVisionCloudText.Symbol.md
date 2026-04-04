# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.Symbol.md.txt

# FirebaseVisionCloudText.Symbol

public static class **FirebaseVisionCloudText.Symbol** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
A single symbol representation.  

### Public Method Summary

|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Rect](https://developer.android.com/reference/android/graphics/Rect.html)                                                                                               | [getBoundingBox](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.Symbol#getBoundingBox())() Gets the bounding box for the symbol.                  |
| float                                                                                                                                                                    | [getConfidence](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.Symbol#getConfidence())() Gets confidence of the OCR results for the symbol.       |
| [String](https://developer.android.com/reference/java/lang/String.html)                                                                                                  | [getText](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.Symbol#getText())() Gets the UTF-8 representation of the symbol.                         |
| [FirebaseVisionCloudText.TextProperty](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.TextProperty) | [getTextProperty](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.Symbol#getTextProperty())() Gets additional information detected for the symbol. |

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

Gets the bounding box for the symbol.  

#### public float **getConfidence** ()

Gets confidence of the OCR results for the symbol. Range \[0.0f, 1.0f\].  

#### public [String](https://developer.android.com/reference/java/lang/String.html) **getText** ()

Gets the UTF-8 representation of the symbol.

Returns an empty string if nothing is found.  

#### public [FirebaseVisionCloudText.TextProperty](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.TextProperty) **getTextProperty** ()

Gets additional information detected for the symbol.