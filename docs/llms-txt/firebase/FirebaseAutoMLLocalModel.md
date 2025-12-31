# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/automl/FirebaseAutoMLLocalModel.md.txt

# FirebaseAutoMLLocalModel

public class **FirebaseAutoMLLocalModel** extends [FirebaseLocalModel](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseLocalModel)  
**This class is deprecated.**   

The standalone ML Kit SDK replaces this API. For more information, refer to the [migration guide](https://developers.google.com/ml-kit/migration).

Describes a local model created from local or asset files.

Defines the model's location (either absolute file path in local directory, or subpath in
the app's asset directory) and the model name.  

### Nested Class Summary

|-------|---|---|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| class | [FirebaseAutoMLLocalModel.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/automl/FirebaseAutoMLLocalModel.Builder) || Builder class of [FirebaseAutoMLLocalModel](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/automl/FirebaseAutoMLLocalModel). |

### Inherited Method Summary

From class com.google.firebase.ml.common.modeldownload.FirebaseLocalModel  

|---------|--------------------------------------------------------------------------------------|
| boolean | equals([Object](https://developer.android.com/reference/java/lang/Object.html) arg0) |
| int     | hashCode()                                                                           |

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