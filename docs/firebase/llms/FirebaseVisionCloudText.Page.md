# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.Page.md.txt

# FirebaseVisionCloudText.Page

public static class **FirebaseVisionCloudText.Page** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
Detected page from cloud OCR engine.  

### Public Method Summary

|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [List](https://developer.android.com/reference/java/util/List.html)\<[FirebaseVisionCloudText.Block](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.Block)\> | [getBlocks](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.Page#getBlocks())() List of [FirebaseVisionCloudText.Block](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.Block) in the [FirebaseVisionCloudText.Page](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.Page). |
| float                                                                                                                                                                                                                             | [getConfidence](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.Page#getConfidence())() Gets confidence of the OCR results for the page.                                                                                                                                                                                                                                                                            |
| int                                                                                                                                                                                                                               | [getHeight](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.Page#getHeight())() Gets the height of the page.                                                                                                                                                                                                                                                                                                        |
| [FirebaseVisionCloudText.TextProperty](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.TextProperty)                                                          | [getTextProperty](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.Page#getTextProperty())() Gets additional information detected for the page, such as language, text breaks.                                                                                                                                                                                                                                       |
| int                                                                                                                                                                                                                               | [getWidth](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.Page#getWidth())() Gets the width of the page.                                                                                                                                                                                                                                                                                                           |

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

#### public [List](https://developer.android.com/reference/java/util/List.html)\<[FirebaseVisionCloudText.Block](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.Block)\>
**getBlocks** ()

List of [FirebaseVisionCloudText.Block](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.Block) in the [FirebaseVisionCloudText.Page](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.Page).  

#### public float **getConfidence** ()

Gets confidence of the OCR results for the page. Range \[0.0f, 1.0f\].  

#### public int **getHeight** ()

Gets the height of the page.  

#### public [FirebaseVisionCloudText.TextProperty](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/text/FirebaseVisionCloudText.TextProperty) **getTextProperty** ()

Gets additional information detected for the page, such as language, text
breaks.  

#### public int **getWidth** ()

Gets the width of the page.