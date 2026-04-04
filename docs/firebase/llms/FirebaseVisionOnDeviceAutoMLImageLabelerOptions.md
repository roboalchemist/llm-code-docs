# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionOnDeviceAutoMLImageLabelerOptions.md.txt

# FirebaseVisionOnDeviceAutoMLImageLabelerOptions

public class **FirebaseVisionOnDeviceAutoMLImageLabelerOptions** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
**This class is deprecated.**   

The standalone ML Kit SDK replaces this API. For more information, refer to the [migration guide](https://developers.google.com/ml-kit/migration).

Options for on device automl image labeler. Confidence threshold could be provided for the
label detection.

For example, if the confidence threshold is set to 0.7, only labels with confidence \>=
0.7 would be returned. The default threshold is 0.5.  

### Nested Class Summary

|-------|---|---|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| class | [FirebaseVisionOnDeviceAutoMLImageLabelerOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionOnDeviceAutoMLImageLabelerOptions.Builder) || Builder of [FirebaseVisionOnDeviceImageLabelerOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionOnDeviceImageLabelerOptions). |

### Public Method Summary

|---------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| boolean | [equals](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionOnDeviceAutoMLImageLabelerOptions#equals(java.lang.Object))([Object](https://developer.android.com/reference/java/lang/Object.html) o) |
| int     | [hashCode](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionOnDeviceAutoMLImageLabelerOptions#hashCode())()                                                                                      |

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