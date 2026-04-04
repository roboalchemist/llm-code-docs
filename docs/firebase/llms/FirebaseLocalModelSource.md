# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/model/FirebaseLocalModelSource.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseLocalModelSource.md.txt

# FirebaseLocalModelSource

public class **FirebaseLocalModelSource** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
The model source for models created from local/asset files.

The model source defines the model's location (either absolute file path in local
directory, or sub-path in the app asset directory), and the model name.  

### Nested Class Summary

|-------|---|---|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| class | [FirebaseLocalModelSource.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseLocalModelSource.Builder) || Builder class of [FirebaseLocalModelSource](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseLocalModelSource). |

### Public Method Summary

|-------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| boolean                                                                 | [equals](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseLocalModelSource#equals(java.lang.Object))([Object](https://developer.android.com/reference/java/lang/Object.html) o) |
| [String](https://developer.android.com/reference/java/lang/String.html) | [getAssetFilePath](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseLocalModelSource#getAssetFilePath())() Gets the sub path of the model under app's asset folder.             |
| [String](https://developer.android.com/reference/java/lang/String.html) | [getFilePath](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseLocalModelSource#getFilePath())() Gets the file path of the local model source.                                  |
| [String](https://developer.android.com/reference/java/lang/String.html) | [getModelName](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseLocalModelSource#getModelName())() Gets the model name of the local model source.                               |
| int                                                                     | [hashCode](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseLocalModelSource#hashCode())()                                                                                      |

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

#### public boolean **equals** ([Object](https://developer.android.com/reference/java/lang/Object.html) o)

#### public [String](https://developer.android.com/reference/java/lang/String.html) **getAssetFilePath** ()

Gets the sub path of the model under app's asset folder.  

#### public [String](https://developer.android.com/reference/java/lang/String.html) **getFilePath** ()

Gets the file path of the local model source.  

#### public [String](https://developer.android.com/reference/java/lang/String.html) **getModelName** ()

Gets the model name of the local model source.  

#### public int **hashCode** ()