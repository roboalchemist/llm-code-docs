# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.Phone.md.txt

# FirebaseVisionBarcode.Phone

public static class **FirebaseVisionBarcode.Phone** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
Phone number info.  

### Nested Class Summary

|------------|---|---|-------------------------------------|
| @interface | [FirebaseVisionBarcode.Phone.FormatType](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.Phone.FormatType) || Phone number format type constants. |

### Constant Summary

|-----|---------------------------------------------------------------------------------------------------------------------------------------------------|---------------------|
| int | [TYPE_FAX](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.Phone#TYPE_FAX)         | Fax machine.        |
| int | [TYPE_HOME](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.Phone#TYPE_HOME)       | Home phone.         |
| int | [TYPE_MOBILE](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.Phone#TYPE_MOBILE)   | Mobile phone.       |
| int | [TYPE_UNKNOWN](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.Phone#TYPE_UNKNOWN) | Unknown phone type. |
| int | [TYPE_WORK](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.Phone#TYPE_WORK)       | Work phone.         |

### Public Method Summary

|-------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [String](https://developer.android.com/reference/java/lang/String.html) | [getNumber](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.Phone#getNumber())() Gets phone number.         |
| int                                                                     | [getType](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.Phone#getType())() Gets type of the phone number. |

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
**TYPE_FAX**

Fax machine.  
Constant Value: 3  

#### public static final int
**TYPE_HOME**

Home phone.  
Constant Value: 2  

#### public static final int
**TYPE_MOBILE**

Mobile phone.  
Constant Value: 4  

#### public static final int
**TYPE_UNKNOWN**

Unknown phone type.  
Constant Value: 0  

#### public static final int
**TYPE_WORK**

Work phone.  
Constant Value: 1

## Public Methods

#### public [String](https://developer.android.com/reference/java/lang/String.html) **getNumber** ()

Gets phone number.  

#### public int **getType** ()

Gets type of the phone number.

See also [FirebaseVisionBarcode.Phone.FormatType](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.Phone.FormatType)