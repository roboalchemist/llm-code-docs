# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelInputOutputOptions.Builder.md.txt

# FirebaseModelInputOutputOptions.Builder

public static class **FirebaseModelInputOutputOptions.Builder** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
Builder class to build [FirebaseModelInputOutputOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelInputOutputOptions).  

### Public Constructor Summary

|---|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   | [FirebaseModelInputOutputOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelInputOutputOptions.Builder#FirebaseModelInputOutputOptions.Builder())() Creates a builder to build [FirebaseModelInputOutputOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelInputOutputOptions).                                                                                                                                                                                                                              |
|   | [FirebaseModelInputOutputOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelInputOutputOptions.Builder#FirebaseModelInputOutputOptions.Builder(com.google.firebase.ml.custom.FirebaseModelInputOutputOptions))([FirebaseModelInputOutputOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelInputOutputOptions) options) Gets a builder from an existing [FirebaseModelInputOutputOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelInputOutputOptions). |

### Public Method Summary

|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [FirebaseModelInputOutputOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelInputOutputOptions)                 | [build](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelInputOutputOptions.Builder#build())() Builds a [FirebaseModelInputOutputOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelInputOutputOptions). |
| [FirebaseModelInputOutputOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelInputOutputOptions.Builder) | [setInputFormat](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelInputOutputOptions.Builder#setInputFormat(int, int, int[]))(int index, int dataType, int\[\] dims) Sets type and dimensions for index-th input.                                            |
| [FirebaseModelInputOutputOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelInputOutputOptions.Builder) | [setOutputFormat](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelInputOutputOptions.Builder#setOutputFormat(int, int, int[]))(int index, int dataType, int\[\] dims) Sets type and dimensions for index-th output.                                         |

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

#### public **FirebaseModelInputOutputOptions.Builder** ()

Creates a builder to build [FirebaseModelInputOutputOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelInputOutputOptions).  

#### public **FirebaseModelInputOutputOptions.Builder** ([FirebaseModelInputOutputOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelInputOutputOptions) options)

Gets a builder from an existing [FirebaseModelInputOutputOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelInputOutputOptions).  

##### Parameters

| options | an instance of [FirebaseModelInputOutputOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelInputOutputOptions). |
|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Public Methods

#### public [FirebaseModelInputOutputOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelInputOutputOptions) **build** ()

Builds a [FirebaseModelInputOutputOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelInputOutputOptions).  

##### Throws

| [FirebaseMLException](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/FirebaseMLException) |   |
|-----------------------------------------------------------------------------------------------------------------------------|---|

#### public [FirebaseModelInputOutputOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelInputOutputOptions.Builder) **setInputFormat** (int index, int dataType, int\[\] dims)

Sets type and dimensions for index-th input.  

##### Parameters

|  index   |                                                              index of the input data to set type and dimensions for.                                                              |
| dataType | data type of the input data. It should be one of [FirebaseModelDataType](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelDataType). |
|   dims   |                                                                an int array for the dimensions of the input data.                                                                 |
|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

##### Returns

- a builder to build the [FirebaseModelInputOutputOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelInputOutputOptions).  

#### public [FirebaseModelInputOutputOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelInputOutputOptions.Builder) **setOutputFormat** (int index, int dataType, int\[\] dims)

Sets type and dimensions for index-th output.  

##### Parameters

|  index   |                                                              index of the output data to set type \& dimensions for.                                                               |
| dataType | data type of the output data. It should be one of [FirebaseModelDataType](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelDataType). |
|   dims   |                                                                an int array for the dimensions of the output data.                                                                 |
|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

##### Returns

- a builder to build the [FirebaseModelInputOutputOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelInputOutputOptions).