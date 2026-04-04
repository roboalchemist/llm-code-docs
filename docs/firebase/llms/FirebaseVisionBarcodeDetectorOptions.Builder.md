# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcodeDetectorOptions.Builder.md.txt

# FirebaseVisionBarcodeDetectorOptions.Builder

public static class **FirebaseVisionBarcodeDetectorOptions.Builder** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
Builder to build out a [FirebaseVisionBarcodeDetectorOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcodeDetectorOptions).  

### Public Constructor Summary

|---|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   | [FirebaseVisionBarcodeDetectorOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcodeDetectorOptions.Builder#FirebaseVisionBarcodeDetectorOptions.Builder())() Builder for [FirebaseVisionBarcodeDetectorOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcodeDetectorOptions). |

### Public Method Summary

|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [FirebaseVisionBarcodeDetectorOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcodeDetectorOptions)                 | [build](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcodeDetectorOptions.Builder#build())() Builds a [FirebaseVisionBarcodeDetectorOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcodeDetectorOptions) instance. |
| [FirebaseVisionBarcodeDetectorOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcodeDetectorOptions.Builder) | [setBarcodeFormats](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcodeDetectorOptions.Builder#setBarcodeFormats(int, int...))(int format, int... moreFormats) Sets all the supported barcode formats.                                                                                 |

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

#### public **FirebaseVisionBarcodeDetectorOptions.Builder** ()

Builder for [FirebaseVisionBarcodeDetectorOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcodeDetectorOptions).

## Public Methods

#### public [FirebaseVisionBarcodeDetectorOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcodeDetectorOptions) **build** ()

Builds a [FirebaseVisionBarcodeDetectorOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcodeDetectorOptions) instance.  

#### public [FirebaseVisionBarcodeDetectorOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcodeDetectorOptions.Builder) **setBarcodeFormats** (int format, int... moreFormats)

Sets all the supported barcode formats.

e.g. `setBarcodeFormats(FirebaseVisionBarcode.FORMAT_QR_CODE,
FirebaseVisionBarcode.FORMAT_UPC_A)`.

Reducing the number of supported formats will make the barcode detector faster.

Only the last call will be respected if calling this method multiple times

Default: all formats are supported.  

##### Parameters

|   format    | supported barcode format |
| moreFormats |                          |
|-------------|--------------------------|