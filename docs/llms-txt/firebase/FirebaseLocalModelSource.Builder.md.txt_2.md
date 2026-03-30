# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/model/FirebaseLocalModelSource.Builder.md.txt

# FirebaseLocalModelSource.Builder

public static class **FirebaseLocalModelSource.Builder** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
Builder class of `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/model/FirebaseLocalModelSource`.

### Public Constructor Summary

|---|---|
|   | [FirebaseLocalModelSource.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/model/FirebaseLocalModelSource.Builder#FirebaseLocalModelSource.Builder(java.lang.String))([String](https://developer.android.com/reference/java/lang/String.html) modelName) Creates a new builder to build `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/model/FirebaseLocalModelSource`. |

### Public Method Summary

|---|---|
| [FirebaseLocalModelSource](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/model/FirebaseLocalModelSource) | [build](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/model/FirebaseLocalModelSource.Builder#build())() |
| [FirebaseLocalModelSource.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/model/FirebaseLocalModelSource.Builder) | [setAssetFilePath](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/model/FirebaseLocalModelSource.Builder#setAssetFilePath(java.lang.String))([String](https://developer.android.com/reference/java/lang/String.html) assetFilePath) Sets the asset sub-path of the asset model file Please make sure your model asset file is not compressed by using aaptOptions. |
| [FirebaseLocalModelSource.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/model/FirebaseLocalModelSource.Builder) | [setFilePath](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/model/FirebaseLocalModelSource.Builder#setFilePath(java.lang.String))([String](https://developer.android.com/reference/java/lang/String.html) filePath) Sets the absolute file path of the local model file. |

### Inherited Method Summary

From class java.lang.Object

|---|---|
| [Object](https://developer.android.com/reference/java/lang/Object.html) | clone() |
| boolean | equals([Object](https://developer.android.com/reference/java/lang/Object.html) arg0) |
| void | finalize() |
| final [Class](https://developer.android.com/reference/java/lang/Class.html)\<?\> | getClass() |
| int | hashCode() |
| final void | notify() |
| final void | notifyAll() |
| [String](https://developer.android.com/reference/java/lang/String.html) | toString() |
| final void | wait(long arg0, int arg1) |
| final void | wait(long arg0) |
| final void | wait() |

## Public Constructors

#### public **FirebaseLocalModelSource.Builder** ([String](https://developer.android.com/reference/java/lang/String.html) modelName)

Creates a new builder to build `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/model/FirebaseLocalModelSource`.

## Public Methods

#### public [FirebaseLocalModelSource](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/model/FirebaseLocalModelSource) **build**
()

##### Returns

- an instance of `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/model/FirebaseLocalModelSource` with provided info.

#### public [FirebaseLocalModelSource.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/model/FirebaseLocalModelSource.Builder) **setAssetFilePath** ([String](https://developer.android.com/reference/java/lang/String.html) assetFilePath)

Sets the asset sub-path of the asset model file

Please make sure your model asset file is not compressed by using aaptOptions. For
more details, please refer to [documentation](https://firebase.google.com/docs/ml-kit/android/use-custom-models#make_models_available_locally).

#### public [FirebaseLocalModelSource.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/model/FirebaseLocalModelSource.Builder) **setFilePath** ([String](https://developer.android.com/reference/java/lang/String.html) filePath)

Sets the absolute file path of the local model file.