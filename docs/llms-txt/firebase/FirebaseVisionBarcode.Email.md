# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.Email.md.txt

# FirebaseVisionBarcode.Email

public static class **FirebaseVisionBarcode.Email** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
An email message from a 'MAILTO:' or similar QRCode type.  

### Nested Class Summary

|------------|---|---|------------------------------|
| @interface | [FirebaseVisionBarcode.Email.FormatType](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.Email.FormatType) || Email format type constants. |

### Constant Summary

|-----|---------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| int | [TYPE_HOME](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.Email#TYPE_HOME)       |             |
| int | [TYPE_UNKNOWN](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.Email#TYPE_UNKNOWN) | Email type. |
| int | [TYPE_WORK](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.Email#TYPE_WORK)       |             |

### Public Method Summary

|-------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [String](https://developer.android.com/reference/java/lang/String.html) | [getAddress](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.Email#getAddress())() Gets email's address. |
| [String](https://developer.android.com/reference/java/lang/String.html) | [getBody](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.Email#getBody())() Gets email's body.          |
| [String](https://developer.android.com/reference/java/lang/String.html) | [getSubject](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.Email#getSubject())() Gets email's subject. |
| int                                                                     | [getType](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.Email#getType())() Gets type of the email.     |

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
**TYPE_HOME**

Constant Value: 2  

#### public static final int
**TYPE_UNKNOWN**

Email type.  
Constant Value: 0  

#### public static final int
**TYPE_WORK**

Constant Value: 1

## Public Methods

#### public [String](https://developer.android.com/reference/java/lang/String.html) **getAddress** ()

Gets email's address.  

#### public [String](https://developer.android.com/reference/java/lang/String.html) **getBody** ()

Gets email's body.  

#### public [String](https://developer.android.com/reference/java/lang/String.html) **getSubject** ()

Gets email's subject.  

#### public int **getType** ()

Gets type of the email.

See also [FirebaseVisionBarcode.Email.FormatType](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.Email.FormatType).