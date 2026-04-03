# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelOutputs.md.txt

# FirebaseModelOutputs

public final class **FirebaseModelOutputs** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
**This class is deprecated.**   

For more information refer to the [custom model implementation
instructions](https://firebase.google.com/docs/ml/android/use-custom-models).

Stores inference results.  

### Public Method Summary

|---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| \<T\> T | [getOutput](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelOutputs#getOutput(int))(int index) Gets index-th output. |

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

#### public T **getOutput** (int index)

Gets index-th output.

Example: byte\[\]\[\] probs = firebaseModelResult.getOutput(0);  

##### Throws

| [IllegalArgumentException](https://developer.android.com/reference/java/lang/IllegalArgumentException.html) |                                        if the index does not exist.                                        |
|       [ClassCastException](https://developer.android.com/reference/java/lang/ClassCastException.html)       | if type argument 'T' does not match the corresponding data type and dimension specified in the model file. |
|-------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|