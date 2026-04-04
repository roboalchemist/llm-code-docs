# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.Paragraph.md.txt

# FirebaseVisionCloudText.Paragraph

public static class **FirebaseVisionCloudText.Paragraph** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
A structural unit of text representing a number of words in certain order.  

### Public Method Summary

|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Rect](https://developer.android.com/reference/android/graphics/Rect.html)                                                                                                                                                      | [getBoundingBox](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.Paragraph#getBoundingBox())() Gets the bounding box for the [FirebaseVisionCloudText.Paragraph](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.Paragraph).                                                                                                                                                                                                        |
| float                                                                                                                                                                                                                           | [getConfidence](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.Paragraph#getConfidence())() Gets confidence of the OCR results for the [FirebaseVisionCloudText.Paragraph](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.Paragraph).                                                                                                                                                                                             |
| [FirebaseVisionCloudText.TextProperty](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.TextProperty)                                                        | [getTextProperty](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.Paragraph#getTextProperty())() Gets additional information detected for the [FirebaseVisionCloudText.Paragraph](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.Paragraph).                                                                                                                                                                                       |
| [List](https://developer.android.com/reference/java/util/List.html)\<[FirebaseVisionCloudText.Word](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.Word)\> | [getWords](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.Paragraph#getWords())() Gets the [List](https://developer.android.com/reference/java/util/List.html) of [FirebaseVisionCloudText.Word](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.Word)s in the [FirebaseVisionCloudText.Paragraph](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.Paragraph). |

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

Gets the bounding box for the [FirebaseVisionCloudText.Paragraph](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.Paragraph).  

#### public float **getConfidence** ()

Gets confidence of the OCR results for the [FirebaseVisionCloudText.Paragraph](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.Paragraph). Range \[0.0f, 1.0f\].  

#### public [FirebaseVisionCloudText.TextProperty](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.TextProperty) **getTextProperty** ()

Gets additional information detected for the [FirebaseVisionCloudText.Paragraph](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.Paragraph).  

#### public [List](https://developer.android.com/reference/java/util/List.html)\<[FirebaseVisionCloudText.Word](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.Word)\>
**getWords** ()

Gets the [List](https://developer.android.com/reference/java/util/List.html) of
[FirebaseVisionCloudText.Word](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.Word)s in the [FirebaseVisionCloudText.Paragraph](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.Paragraph).

Returns an empty list if no `Word` is found.