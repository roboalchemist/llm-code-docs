# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/automl/FirebaseAutoMLRemoteModel.md.txt

# FirebaseAutoMLRemoteModel

public class **FirebaseAutoMLRemoteModel** extends [FirebaseRemoteModel](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseRemoteModel)  
**This class is deprecated.**   

The standalone ML Kit SDK replaces this API. For more information, refer to the [migration guide](https://developers.google.com/ml-kit/migration).

Describes a remote model to be downloaded to the device.

Defines the download conditions of the model, whether or not to download updated versions
of the model, and the model's name specified by the developer in the cloud console.  

### Nested Class Summary

|-------|---|---|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| class | [FirebaseAutoMLRemoteModel.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/automl/FirebaseAutoMLRemoteModel.Builder) || Builder of [FirebaseAutoMLRemoteModel](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/automl/FirebaseAutoMLRemoteModel). |

### Inherited Method Summary

From class com.google.firebase.ml.common.modeldownload.FirebaseRemoteModel  

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