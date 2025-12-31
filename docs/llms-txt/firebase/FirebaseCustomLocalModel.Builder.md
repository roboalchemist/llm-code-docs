# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseCustomLocalModel.Builder.md.txt

# FirebaseCustomLocalModel.Builder

public static class **FirebaseCustomLocalModel.Builder** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
Builder class of [FirebaseCustomLocalModel](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseCustomLocalModel).  

### Public Constructor Summary

|---|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   | [FirebaseCustomLocalModel.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseCustomLocalModel.Builder#FirebaseCustomLocalModel.Builder())() Creates a new builder to build [FirebaseCustomLocalModel](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseCustomLocalModel). |

### Public Method Summary

|-------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [FirebaseCustomLocalModel](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseCustomLocalModel)                 | [build](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseCustomLocalModel.Builder#build())()                                                                                                                                                                                                                                                   |
| [FirebaseCustomLocalModel.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseCustomLocalModel.Builder) | [setAssetFilePath](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseCustomLocalModel.Builder#setAssetFilePath(java.lang.String))([String](https://developer.android.com/reference/java/lang/String.html) assetFilePath) Sets the asset subpath of the asset model file Make sure your model asset file is not compressed by using aaptOptions. |
| [FirebaseCustomLocalModel.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseCustomLocalModel.Builder) | [setFilePath](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseCustomLocalModel.Builder#setFilePath(java.lang.String))([String](https://developer.android.com/reference/java/lang/String.html) filePath) Sets the absolute file path of the local model file.                                                                                  |

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

#### public **FirebaseCustomLocalModel.Builder** ()

Creates a new builder to build [FirebaseCustomLocalModel](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseCustomLocalModel).

## Public Methods

#### public [FirebaseCustomLocalModel](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseCustomLocalModel)
**build** ()

##### Returns

- an instance of [FirebaseCustomLocalModel](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseCustomLocalModel) with provided info.  

#### public [FirebaseCustomLocalModel.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseCustomLocalModel.Builder) **setAssetFilePath** ([String](https://developer.android.com/reference/java/lang/String.html) assetFilePath)

Sets the asset subpath of the asset model file

Make sure your model asset file is not compressed by using aaptOptions. For more
details, refer to [documentation](https://firebase.google.com/docs/ml/android/use-custom-models#local_model).  

#### public [FirebaseCustomLocalModel.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseCustomLocalModel.Builder) **setFilePath** ([String](https://developer.android.com/reference/java/lang/String.html) filePath)

Sets the absolute file path of the local model file.