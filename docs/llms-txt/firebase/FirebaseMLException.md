# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/FirebaseMLException.md.txt

# FirebaseMLException

public class **FirebaseMLException** extends [FirebaseException](https://developers.google.com/android/reference/com/google/firebase/FirebaseException.html)  
A class of exceptions thrown by Firebase Machine Learning  

### Nested Class Summary

|------------|---|---|--------------------------------------|
| @interface | [FirebaseMLException.Code](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/FirebaseMLException.Code) || The set of Firebase ML status codes. |

### Constant Summary

|-----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| int | [ABORTED](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/FirebaseMLException#ABORTED)                                               | The operation was aborted, typically due to a concurrency issue like transaction aborts, etc.                  |
| int | [ALREADY_EXISTS](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/FirebaseMLException#ALREADY_EXISTS)                                 | Some resource that we attempted to create already exists.                                                      |
| int | [CANCELLED](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/FirebaseMLException#CANCELLED)                                           | The operation was cancelled (typically by the caller).                                                         |
| int | [DATA_LOSS](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/FirebaseMLException#DATA_LOSS)                                           | Unrecoverable data loss or corruption.                                                                         |
| int | [DEADLINE_EXCEEDED](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/FirebaseMLException#DEADLINE_EXCEEDED)                           | Deadline expired before operation could complete.                                                              |
| int | [FAILED_PRECONDITION](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/FirebaseMLException#FAILED_PRECONDITION)                       | Operation was rejected because the system is not in a state required for the operation's execution.            |
| int | [INTERNAL](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/FirebaseMLException#INTERNAL)                                             | Internal errors.                                                                                               |
| int | [INVALID_ARGUMENT](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/FirebaseMLException#INVALID_ARGUMENT)                             | Client specified an invalid argument.                                                                          |
| int | [MODEL_HASH_MISMATCH](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/FirebaseMLException#MODEL_HASH_MISMATCH)                       | The downloaded model's hash doesn't match the expected value.                                                  |
| int | [MODEL_INCOMPATIBLE_WITH_TFLITE](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/FirebaseMLException#MODEL_INCOMPATIBLE_WITH_TFLITE) | The downloaded model isn't compatible with the TFLite runtime.                                                 |
| int | [NOT_ENOUGH_SPACE](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/FirebaseMLException#NOT_ENOUGH_SPACE)                             | There is not enough space left on the device.                                                                  |
| int | [NOT_FOUND](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/FirebaseMLException#NOT_FOUND)                                           | Some requested resource was not found.                                                                         |
| int | [OK](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/FirebaseMLException#OK)                                                         | The operation completed successfully.                                                                          |
| int | [OUT_OF_RANGE](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/FirebaseMLException#OUT_OF_RANGE)                                     | Operation was attempted past the valid range.                                                                  |
| int | [PERMISSION_DENIED](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/FirebaseMLException#PERMISSION_DENIED)                           | The caller does not have permission to execute the specified operation.                                        |
| int | [RESOURCE_EXHAUSTED](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/FirebaseMLException#RESOURCE_EXHAUSTED)                         | Some resource has been exhausted, perhaps a per-user quota, or perhaps the entire file system is out of space. |
| int | [UNAUTHENTICATED](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/FirebaseMLException#UNAUTHENTICATED)                               | The request does not have valid authentication credentials for the operation.                                  |
| int | [UNAVAILABLE](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/FirebaseMLException#UNAVAILABLE)                                       | The service is currently unavailable.                                                                          |
| int | [UNIMPLEMENTED](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/FirebaseMLException#UNIMPLEMENTED)                                   | Operation is not implemented or not supported/enabled.                                                         |
| int | [UNKNOWN](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/FirebaseMLException#UNKNOWN)                                               | Unknown error or an error from a different error domain.                                                       |

### Public Method Summary

|-----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| int | [getCode](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/FirebaseMLException#getCode())() Gets the error code for the Firebase ML operation that failed. |

### Inherited Method Summary

From class java.lang.Throwable  

|------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| synchronized final void                                                                              | addSuppressed([Throwable](https://developer.android.com/reference/java/lang/Throwable.html) arg0)                     |
| synchronized [Throwable](https://developer.android.com/reference/java/lang/Throwable.html)           | fillInStackTrace()                                                                                                    |
| synchronized [Throwable](https://developer.android.com/reference/java/lang/Throwable.html)           | getCause()                                                                                                            |
| [String](https://developer.android.com/reference/java/lang/String.html)                              | getLocalizedMessage()                                                                                                 |
| [String](https://developer.android.com/reference/java/lang/String.html)                              | getMessage()                                                                                                          |
| [StackTraceElement\[\]](https://developer.android.com/reference/java/lang/StackTraceElement.html)    | getStackTrace()                                                                                                       |
| synchronized final [Throwable\[\]](https://developer.android.com/reference/java/lang/Throwable.html) | getSuppressed()                                                                                                       |
| synchronized [Throwable](https://developer.android.com/reference/java/lang/Throwable.html)           | initCause([Throwable](https://developer.android.com/reference/java/lang/Throwable.html) arg0)                         |
| void                                                                                                 | printStackTrace()                                                                                                     |
| void                                                                                                 | printStackTrace([PrintWriter](https://developer.android.com/reference/java/io/PrintWriter.html) arg0)                 |
| void                                                                                                 | printStackTrace([PrintStream](https://developer.android.com/reference/java/io/PrintStream.html) arg0)                 |
| void                                                                                                 | setStackTrace([StackTraceElement\[\]](https://developer.android.com/reference/java/lang/StackTraceElement.html) arg0) |
| [String](https://developer.android.com/reference/java/lang/String.html)                              | toString()                                                                                                            |

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
**ABORTED**

The operation was aborted, typically due to a concurrency issue like transaction
aborts, etc.  
Constant Value: 10  

#### public static final int
**ALREADY_EXISTS**

Some resource that we attempted to create already exists.  
Constant Value: 6  

#### public static final int
**CANCELLED**

The operation was cancelled (typically by the caller).  
Constant Value: 1  

#### public static final int
**DATA_LOSS**

Unrecoverable data loss or corruption.  
Constant Value: 15  

#### public static final int
**DEADLINE_EXCEEDED**

Deadline expired before operation could complete. For operations that change the
state of the system, this error may be returned even if the operation has completed
successfully. For example, a successful response from a server could have been delayed
long enough for the deadline to expire.  
Constant Value: 4  

#### public static final int
**FAILED_PRECONDITION**

Operation was rejected because the system is not in a state required for the
operation's execution.  
Constant Value: 9  

#### public static final int
**INTERNAL**

Internal errors. Means some invariants expected by underlying system has been
broken. If you see one of these errors, something is very broken.  
Constant Value: 13  

#### public static final int
**INVALID_ARGUMENT**

Client specified an invalid argument. Note that this differs from
FAILED_PRECONDITION. INVALID_ARGUMENT indicates arguments that are problematic
regardless of the state of the system (e.g., an invalid field name).  
Constant Value: 3  

#### public static final int
**MODEL_HASH_MISMATCH**

The downloaded model's hash doesn't match the expected value.  
Constant Value: 102  

#### public static final int
**MODEL_INCOMPATIBLE_WITH_TFLITE**

The downloaded model isn't compatible with the TFLite runtime.  
Constant Value: 100  

#### public static final int
**NOT_ENOUGH_SPACE**

There is not enough space left on the device.  
Constant Value: 101  

#### public static final int
**NOT_FOUND**

Some requested resource was not found.  
Constant Value: 5  

#### public static final int
**OK**

The operation completed successfully. FirebaseMLException will never have a status
of OK.  
Constant Value: 0  

#### public static final int
**OUT_OF_RANGE**

Operation was attempted past the valid range.  
Constant Value: 11  

#### public static final int
**PERMISSION_DENIED**

The caller does not have permission to execute the specified operation.  
Constant Value: 7  

#### public static final int
**RESOURCE_EXHAUSTED**

Some resource has been exhausted, perhaps a per-user quota, or perhaps the entire
file system is out of space.  
Constant Value: 8  

#### public static final int
**UNAUTHENTICATED**

The request does not have valid authentication credentials for the operation.  
Constant Value: 16  

#### public static final int
**UNAVAILABLE**

The service is currently unavailable. This is a most likely a transient condition
and may be corrected by retrying with a backoff.

In ML Kit, this error is mostly about the models being not available yet.  
Constant Value: 14  

#### public static final int
**UNIMPLEMENTED**

Operation is not implemented or not supported/enabled.  
Constant Value: 12  

#### public static final int
**UNKNOWN**

Unknown error or an error from a different error domain.  
Constant Value: 2

## Public Methods

#### public int **getCode** ()

Gets the error code for the Firebase ML operation that failed.