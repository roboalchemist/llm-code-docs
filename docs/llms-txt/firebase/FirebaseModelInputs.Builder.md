# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelInputs.Builder.md.txt

# FirebaseModelInputs.Builder

public static class **FirebaseModelInputs.Builder** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
Builder class of `FirebaseModelInputs`.  

### Public Constructor Summary

|---|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   | [FirebaseModelInputs.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelInputs.Builder#FirebaseModelInputs.Builder())() Creates a new builder to build `FirebaseModelInputs`. |

### Public Method Summary

|---------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [FirebaseModelInputs.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelInputs.Builder) | [add](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelInputs.Builder#add(java.lang.Object))([Object](https://developer.android.com/reference/java/lang/Object.html) input) Adds an input for custom model inference. |
| [FirebaseModelInputs](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelInputs)                 | [build](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelInputs.Builder#build())() Builds a `FirebaseModelInputs`.                                                                                                    |

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

#### public **FirebaseModelInputs.Builder** ()

Creates a new builder to build `FirebaseModelInputs`.

## Public Methods

#### public [FirebaseModelInputs.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelInputs.Builder)
**add** ([Object](https://developer.android.com/reference/java/lang/Object.html) input)

Adds an input for custom model inference.

Inputs must be added in the same order as inputs of the corresponding model. It
accepts array, multidimensional array or a direct [ByteBuffer](https://developer.android.com/reference/java/nio/ByteBuffer.html) as
inputs of primitive types including int, float, long, and byte.

[ByteBuffer](https://developer.android.com/reference/java/nio/ByteBuffer.html) is
the preferred way to pass large input data. When [ByteBuffer](https://developer.android.com/reference/java/nio/ByteBuffer.html) is
used, its content should remain unchanged until model inference is done. Its type and
dimensions must match the corresponding configurations provided by [FirebaseModelInputOutputOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelInputOutputOptions).

Array and multidimensional array are also supported formats for input. However,
these formats have performance impact especially when the data size is large. Please
use it mainly for debugging or latency non-sensitive use cases.  

##### Parameters

| input | an array, multidimensional array, or a direct [ByteBuffer](https://developer.android.com/reference/java/nio/ByteBuffer.html) of primitive types including int, float, long, and byte. |
|-------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

##### Returns

- a builder to build the `FirebaseModelInputs`.  

##### Throws

|             [NullPointerException](https://developer.android.com/reference/java/lang/NullPointerException.html)             |                                                                                                                                                                if the input object is null.                                                                                                                                                                 |
|         [IllegalArgumentException](https://developer.android.com/reference/java/lang/IllegalArgumentException.html)         |                                                                                                     if the input object is not a [ByteBuffer](https://developer.android.com/reference/java/nio/ByteBuffer.html), an array or a multidimensional array.                                                                                                      |
| [FirebaseMLException](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/FirebaseMLException) | if the input is not a direct [ByteBuffer](https://developer.android.com/reference/java/nio/ByteBuffer.html) or is not in [nativeOrder()](https://developer.android.com/reference/java/nio/ByteOrder.html#nativeOrder()). See also [Direct VS non-direct buffers.](https://developer.android.com/reference/java/nio/ByteBuffer#direct-vs-non-direct-buffers) |
|-----------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

#### public [FirebaseModelInputs](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelInputs)
**build** ()

Builds a `FirebaseModelInputs`.