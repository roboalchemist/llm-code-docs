# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionCloudTextRecognizerOptions.md.txt

# FirebaseVisionCloudTextRecognizerOptions

public class **FirebaseVisionCloudTextRecognizerOptions** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
Represents the cloud text recognizer options.  

### Nested Class Summary

|------------|---|---|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| class      | [FirebaseVisionCloudTextRecognizerOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionCloudTextRecognizerOptions.Builder) || Builder of [FirebaseVisionCloudTextRecognizerOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionCloudTextRecognizerOptions). |
| @interface | [FirebaseVisionCloudTextRecognizerOptions.CloudTextModelType](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionCloudTextRecognizerOptions.CloudTextModelType) || Cloud model types for text recognition.                                                                                                                                                |

### Constant Summary

|-----|-------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|
| int | [DENSE_MODEL](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionCloudTextRecognizerOptions#DENSE_MODEL)   | Dense model type.  |
| int | [SPARSE_MODEL](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionCloudTextRecognizerOptions#SPARSE_MODEL) | Sparse model type. |

### Public Method Summary

|------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| boolean                                                                                                                                        | [equals](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionCloudTextRecognizerOptions#equals(java.lang.Object))([Object](https://developer.android.com/reference/java/lang/Object.html) o) |
| [List](https://developer.android.com/reference/java/util/List.html)\<[String](https://developer.android.com/reference/java/lang/String.html)\> | [getHintedLanguages](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionCloudTextRecognizerOptions#getHintedLanguages())() Gets the hinted language list in the options.                    |
| int                                                                                                                                            | [getModelType](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionCloudTextRecognizerOptions#getModelType())() Gets the cloud model type in the options.                                    |
| int                                                                                                                                            | [hashCode](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionCloudTextRecognizerOptions#hashCode())()                                                                                      |

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

## Constants

#### public static final int
**DENSE_MODEL**

Dense model type. It is more suitable for well-formatted dense text.  
Constant Value: 2  

#### public static final int
**SPARSE_MODEL**

Sparse model type. It is more suitable for sparse text.  
Constant Value: 1

## Public Methods

#### public boolean **equals** ([Object](https://developer.android.com/reference/java/lang/Object.html) o)

#### public [List](https://developer.android.com/reference/java/util/List.html)\<[String](https://developer.android.com/reference/java/lang/String.html)\>
**getHintedLanguages** ()

Gets the hinted language list in the options.  

#### public int **getModelType** ()

Gets the cloud model type in the options.

Default is [SPARSE_MODEL](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionCloudTextRecognizerOptions#SPARSE_MODEL)  

#### public int **hashCode** ()