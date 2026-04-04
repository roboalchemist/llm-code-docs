# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.Address.md.txt

# FirebaseVisionBarcode.Address

public static class **FirebaseVisionBarcode.Address** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
An address.  

### Nested Class Summary

|------------|---|---|-------------------------|
| @interface | [FirebaseVisionBarcode.Address.AddressType](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.Address.AddressType) || Address type constants. |

### Constant Summary

|-----|-----------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|
| int | [TYPE_HOME](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.Address#TYPE_HOME)       | Address type home.    |
| int | [TYPE_UNKNOWN](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.Address#TYPE_UNKNOWN) | Address type unknown. |
| int | [TYPE_WORK](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.Address#TYPE_WORK)       | Address type work.    |

### Public Method Summary

|-----------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [String\[\]](https://developer.android.com/reference/java/lang/String.html) | [getAddressLines](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.Address#getAddressLines())() Gets formatted address, multiple lines when appropriate. |
| int                                                                         | [getType](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.Address#getType())() Gets type of the address.                                                |

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

Address type home.  
Constant Value: 2  

#### public static final int
**TYPE_UNKNOWN**

Address type unknown.  
Constant Value: 0  

#### public static final int
**TYPE_WORK**

Address type work.  
Constant Value: 1

## Public Methods

#### public [String\[\]](https://developer.android.com/reference/java/lang/String.html) **getAddressLines** ()

Gets formatted address, multiple lines when appropriate. This field always contains
at least one line.  

#### public int **getType** ()

Gets type of the address.

See also [FirebaseVisionBarcode.Address.AddressType](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.Address.AddressType)