# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.Word.md.txt

# FirebaseVisionCloudText.Word

public static class **FirebaseVisionCloudText.Word** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
A single word representation.  

### Public Method Summary

|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Rect](https://developer.android.com/reference/android/graphics/Rect.html)                                                                                                                                                          | [getBoundingBox](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.Word#getBoundingBox())() Gets the bounding box for the [FirebaseVisionCloudText.Word](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.Word).                                                                                                                                                                                                                |
| float                                                                                                                                                                                                                               | [getConfidence](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.Word#getConfidence())() Gets confidence of the OCR results for the word.                                                                                                                                                                                                                                                                                                                                                         |
| [List](https://developer.android.com/reference/java/util/List.html)\<[FirebaseVisionCloudText.Symbol](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.Symbol)\> | [getSymbols](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.Word#getSymbols())() Gets the [List](https://developer.android.com/reference/java/util/List.html) of [FirebaseVisionCloudText.Symbol](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.Symbol)s in the [FirebaseVisionCloudText.Word](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.Word). |
| [FirebaseVisionCloudText.TextProperty](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.TextProperty)                                                            | [getTextProperty](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.Word#getTextProperty())() Gets additional information detected for the [FirebaseVisionCloudText.Word](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.Word).                                                                                                                                                                                               |

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

Gets the bounding box for the [FirebaseVisionCloudText.Word](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.Word).  

#### public float **getConfidence** ()

Gets confidence of the OCR results for the word. Range \[0.0f, 1.0f\].  

#### public [List](https://developer.android.com/reference/java/util/List.html)\<[FirebaseVisionCloudText.Symbol](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.Symbol)\>
**getSymbols** ()

Gets the [List](https://developer.android.com/reference/java/util/List.html) of
[FirebaseVisionCloudText.Symbol](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.Symbol)s in the [FirebaseVisionCloudText.Word](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.Word). The order of the symbols follows the natural
reading order.  

#### public [FirebaseVisionCloudText.TextProperty](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.TextProperty) **getTextProperty** ()

Gets additional information detected for the [FirebaseVisionCloudText.Word](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.Word).