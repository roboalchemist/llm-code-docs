# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.Block.md.txt

# FirebaseVisionCloudText.Block

public static class **FirebaseVisionCloudText.Block** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
A logical element on the page. A [FirebaseVisionCloudText.Block](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.Block) could contain multiple [FirebaseVisionCloudText.Paragraph](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.Paragraph)s.  

### Public Method Summary

|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Rect](https://developer.android.com/reference/android/graphics/Rect.html)                                                                                                                                                                | [getBoundingBox](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.Block#getBoundingBox())() Gets the bounding box for the block.                                                                                                                                                                                                                                                                                                                                                                                 |
| float                                                                                                                                                                                                                                     | [getConfidence](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.Block#getConfidence())() Gets confidence of the OCR results for the block.                                                                                                                                                                                                                                                                                                                                                                      |
| [List](https://developer.android.com/reference/java/util/List.html)\<[FirebaseVisionCloudText.Paragraph](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.Paragraph)\> | [getParagraphs](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.Block#getParagraphs())() Gets the [List](https://developer.android.com/reference/java/util/List.html) of [FirebaseVisionCloudText.Paragraph](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.Paragraph)s in the [FirebaseVisionCloudText.Block](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.Block). |
| [FirebaseVisionCloudText.TextProperty](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.TextProperty)                                                                  | [getTextProperty](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.Block#getTextProperty())() Gets additional information detected for the block.                                                                                                                                                                                                                                                                                                                                                                |

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

Gets the bounding box for the block.  

#### public float **getConfidence** ()

Gets confidence of the OCR results for the block. Range \[0.0f, 1.0f\].  

#### public [List](https://developer.android.com/reference/java/util/List.html)\<[FirebaseVisionCloudText.Paragraph](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.Paragraph)\>
**getParagraphs** ()

Gets the [List](https://developer.android.com/reference/java/util/List.html) of
[FirebaseVisionCloudText.Paragraph](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.Paragraph)s in the [FirebaseVisionCloudText.Block](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.Block).

Returns an empty list if no `Paragraph` is found.  

#### public [FirebaseVisionCloudText.TextProperty](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.TextProperty) **getTextProperty** ()

Gets additional information detected for the block.