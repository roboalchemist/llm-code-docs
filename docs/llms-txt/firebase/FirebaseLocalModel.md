# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseLocalModel.md.txt

# FirebaseLocalModel

public class **FirebaseLocalModel** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
Describes a local model created from local or asset files.

Defines the model's location (either absolute file path in local directory, or subpath in
the app's asset directory) and the model name.  

### Nested Class Summary

|-------|---|---|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| class | [FirebaseLocalModel.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseLocalModel.Builder) || Builder class of [FirebaseLocalModel](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseLocalModel). |

### Public Method Summary

|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| boolean | [equals](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseLocalModel#equals(java.lang.Object))([Object](https://developer.android.com/reference/java/lang/Object.html) o) |
| int     | [hashCode](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseLocalModel#hashCode())()                                                                                      |

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

#### public int **hashCode** ()