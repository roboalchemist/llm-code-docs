# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.WiFi.md.txt

# FirebaseVisionBarcode.WiFi

public static class **FirebaseVisionBarcode.WiFi** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
A wifi network parameters from a 'WIFI:' or similar QRCode type.  

### Nested Class Summary

|------------|---|---|---------------------------------|
| @interface | [FirebaseVisionBarcode.WiFi.EncryptionType](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.WiFi.EncryptionType) || Wifi encryption type constants. |

### Constant Summary

|-----|--------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|
| int | [TYPE_OPEN](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.WiFi#TYPE_OPEN) | WiFi encryption type. |
| int | [TYPE_WEP](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.WiFi#TYPE_WEP)   |                       |
| int | [TYPE_WPA](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.WiFi#TYPE_WPA)   |                       |

### Public Method Summary

|-------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| int                                                                     | [getEncryptionType](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.WiFi#getEncryptionType())() Gets the encryption type of the WIFI. |
| [String](https://developer.android.com/reference/java/lang/String.html) | [getPassword](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.WiFi#getPassword())() Gets the password of the WIFI.                    |
| [String](https://developer.android.com/reference/java/lang/String.html) | [getSsid](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.WiFi#getSsid())() Gets the ssid of the WIFI.                                |

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
**TYPE_OPEN**

WiFi encryption type.  
Constant Value: 1  

#### public static final int
**TYPE_WEP**

Constant Value: 3  

#### public static final int
**TYPE_WPA**

Constant Value: 2

## Public Methods

#### public int **getEncryptionType** ()

Gets the encryption type of the WIFI.

See all [FirebaseVisionBarcode.WiFi.EncryptionType](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.WiFi.EncryptionType).  

#### public [String](https://developer.android.com/reference/java/lang/String.html) **getPassword** ()

Gets the password of the WIFI.  

#### public [String](https://developer.android.com/reference/java/lang/String.html) **getSsid** ()

Gets the ssid of the WIFI.