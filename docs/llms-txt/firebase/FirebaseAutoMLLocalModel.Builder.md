# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/automl/FirebaseAutoMLLocalModel.Builder.md.txt

# FirebaseAutoMLLocalModel.Builder

public static class **FirebaseAutoMLLocalModel.Builder** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
Builder class of [FirebaseAutoMLLocalModel](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/automl/FirebaseAutoMLLocalModel).  

### Public Constructor Summary

|---|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   | [FirebaseAutoMLLocalModel.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/automl/FirebaseAutoMLLocalModel.Builder#FirebaseAutoMLLocalModel.Builder())() Creates a new builder to build [FirebaseAutoMLLocalModel](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/automl/FirebaseAutoMLLocalModel). |

### Public Method Summary

|--------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [FirebaseAutoMLLocalModel](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/automl/FirebaseAutoMLLocalModel)                 | [build](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/automl/FirebaseAutoMLLocalModel.Builder#build())()                                                                                                                                                                                                                                                   |
| [FirebaseAutoMLLocalModel.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/automl/FirebaseAutoMLLocalModel.Builder) | [setAssetFilePath](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/automl/FirebaseAutoMLLocalModel.Builder#setAssetFilePath(java.lang.String))([String](https://developer.android.com/reference/java/lang/String.html) assetFilePath) Sets the asset subpath of the asset model file Make sure your model asset file is not compressed by using aaptOptions. |
| [FirebaseAutoMLLocalModel.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/automl/FirebaseAutoMLLocalModel.Builder) | [setFilePath](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/automl/FirebaseAutoMLLocalModel.Builder#setFilePath(java.lang.String))([String](https://developer.android.com/reference/java/lang/String.html) filePath) Sets the absolute file path of the local model file.                                                                                  |

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

## Public Constructors

#### public **FirebaseAutoMLLocalModel.Builder** ()

Creates a new builder to build [FirebaseAutoMLLocalModel](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/automl/FirebaseAutoMLLocalModel).

## Public Methods

#### public [FirebaseAutoMLLocalModel](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/automl/FirebaseAutoMLLocalModel) **build**
()

##### Returns

- an instance of [FirebaseAutoMLLocalModel](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/automl/FirebaseAutoMLLocalModel) with provided info.  

#### public [FirebaseAutoMLLocalModel.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/automl/FirebaseAutoMLLocalModel.Builder) **setAssetFilePath** ([String](https://developer.android.com/reference/java/lang/String.html) assetFilePath)

Sets the asset subpath of the asset model file

Make sure your model asset file is not compressed by using aaptOptions. For more
details, refer to [documentation](https://firebase.google.com/docs/ml/android/use-custom-models#local_model).  

#### public [FirebaseAutoMLLocalModel.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/automl/FirebaseAutoMLLocalModel.Builder) **setFilePath** ([String](https://developer.android.com/reference/java/lang/String.html) filePath)

Sets the absolute file path of the local model file.