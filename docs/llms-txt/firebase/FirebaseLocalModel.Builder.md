# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseLocalModel.Builder.md.txt

# FirebaseLocalModel.Builder

public static class **FirebaseLocalModel.Builder** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
Builder class of [FirebaseLocalModel](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseLocalModel).  

### Public Constructor Summary

|---|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   | [FirebaseLocalModel.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseLocalModel.Builder#FirebaseLocalModel.Builder(java.lang.String))([String](https://developer.android.com/reference/java/lang/String.html) modelName) Creates a new builder to build [FirebaseLocalModel](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseLocalModel). |

### Public Method Summary

|---------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [FirebaseLocalModel](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseLocalModel)                 | [build](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseLocalModel.Builder#build())()                                                                                                                                                                                                                                                   |
| [FirebaseLocalModel.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseLocalModel.Builder) | [setAssetFilePath](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseLocalModel.Builder#setAssetFilePath(java.lang.String))([String](https://developer.android.com/reference/java/lang/String.html) assetFilePath) Sets the asset subpath of the asset model file Make sure your model asset file is not compressed by using aaptOptions. |
| [FirebaseLocalModel.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseLocalModel.Builder) | [setFilePath](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseLocalModel.Builder#setFilePath(java.lang.String))([String](https://developer.android.com/reference/java/lang/String.html) filePath) Sets the absolute file path of the local model file.                                                                                  |

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

#### public **FirebaseLocalModel.Builder** ([String](https://developer.android.com/reference/java/lang/String.html) modelName)

Creates a new builder to build [FirebaseLocalModel](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseLocalModel).

## Public Methods

#### public [FirebaseLocalModel](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseLocalModel) **build**
()

##### Returns

- an instance of [FirebaseLocalModel](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseLocalModel) with provided info.  

#### public [FirebaseLocalModel.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseLocalModel.Builder) **setAssetFilePath** ([String](https://developer.android.com/reference/java/lang/String.html) assetFilePath)

Sets the asset subpath of the asset model file

Make sure your model asset file is not compressed by using aaptOptions. For more
details, refer to [documentation](https://firebase.google.com/docs/ml/android/use-custom-models#local_model).  

#### public [FirebaseLocalModel.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseLocalModel.Builder) **setFilePath** ([String](https://developer.android.com/reference/java/lang/String.html) filePath)

Sets the absolute file path of the local model file.