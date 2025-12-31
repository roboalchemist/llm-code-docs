# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelDataType.md.txt

# FirebaseModelDataType

public final class **FirebaseModelDataType** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
**This class is deprecated.**   

For more information refer to the [custom model implementation
instructions](https://firebase.google.com/docs/ml/android/use-custom-models).

Data types supported by [FirebaseModelInputs](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelInputs).  

### Nested Class Summary

|------------|---|---|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| @interface | [FirebaseModelDataType.DataType](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelDataType.DataType) || Supported data types for [FirebaseModelInputs](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelInputs). |

### Constant Summary

|-----|---------------------------------------------------------------------------------------------------------------------------|---------------------------|
| int | [BYTE](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelDataType#BYTE)       | Byte data type.           |
| int | [FLOAT32](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelDataType#FLOAT32) | 32 bit float data type.   |
| int | [INT32](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelDataType#INT32)     | 32 bit integer data type. |
| int | [LONG](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelDataType#LONG)       | Long data type.           |

### Public Constructor Summary

|---|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
|   | [FirebaseModelDataType](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelDataType#FirebaseModelDataType())() |

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

## Constants

#### public static final int
**BYTE**

Byte data type.  
Constant Value: 3  

#### public static final int
**FLOAT32**

32 bit float data type.  
Constant Value: 1  

#### public static final int
**INT32**

32 bit integer data type.  
Constant Value: 2  

#### public static final int
**LONG**

Long data type.  
Constant Value: 4

## Public Constructors

#### public **FirebaseModelDataType** ()