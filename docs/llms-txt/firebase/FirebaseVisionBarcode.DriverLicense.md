# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.DriverLicense.md.txt

# FirebaseVisionBarcode.DriverLicense

public static class **FirebaseVisionBarcode.DriverLicense** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
A driver license or ID card.  

### Public Method Summary

|-------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [String](https://developer.android.com/reference/java/lang/String.html) | [getAddressCity](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.DriverLicense#getAddressCity())() Gets city of holder's address.                      |
| [String](https://developer.android.com/reference/java/lang/String.html) | [getAddressState](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.DriverLicense#getAddressState())() Gets state of holder's address.                   |
| [String](https://developer.android.com/reference/java/lang/String.html) | [getAddressStreet](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.DriverLicense#getAddressStreet())() Gets holder's street address.                   |
| [String](https://developer.android.com/reference/java/lang/String.html) | [getAddressZip](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.DriverLicense#getAddressZip())() Gets zip code of holder's address.                    |
| [String](https://developer.android.com/reference/java/lang/String.html) | [getBirthDate](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.DriverLicense#getBirthDate())() Gets birth date of the holder.                          |
| [String](https://developer.android.com/reference/java/lang/String.html) | [getDocumentType](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.DriverLicense#getDocumentType())() Gets "DL" for driver licenses, "ID" for ID cards. |
| [String](https://developer.android.com/reference/java/lang/String.html) | [getExpiryDate](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.DriverLicense#getExpiryDate())() Gets expiry date of the license.                      |
| [String](https://developer.android.com/reference/java/lang/String.html) | [getFirstName](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.DriverLicense#getFirstName())() Gets holder's first name.                               |
| [String](https://developer.android.com/reference/java/lang/String.html) | [getGender](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.DriverLicense#getGender())() Gets holder's gender.                                         |
| [String](https://developer.android.com/reference/java/lang/String.html) | [getIssueDate](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.DriverLicense#getIssueDate())() Gets issue date of the license.                         |
| [String](https://developer.android.com/reference/java/lang/String.html) | [getIssuingCountry](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.DriverLicense#getIssuingCountry())() Gets country in which DL/ID was issued.       |
| [String](https://developer.android.com/reference/java/lang/String.html) | [getLastName](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.DriverLicense#getLastName())() Gets holder's last name.                                  |
| [String](https://developer.android.com/reference/java/lang/String.html) | [getLicenseNumber](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.DriverLicense#getLicenseNumber())() Gets driver license ID number.                  |
| [String](https://developer.android.com/reference/java/lang/String.html) | [getMiddleName](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.DriverLicense#getMiddleName())() Gets holder's middle name.                            |

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

#### public [String](https://developer.android.com/reference/java/lang/String.html) **getAddressCity** ()

Gets city of holder's address.  

#### public [String](https://developer.android.com/reference/java/lang/String.html) **getAddressState** ()

Gets state of holder's address.  

#### public [String](https://developer.android.com/reference/java/lang/String.html) **getAddressStreet** ()

Gets holder's street address.  

#### public [String](https://developer.android.com/reference/java/lang/String.html) **getAddressZip** ()

Gets zip code of holder's address.  

#### public [String](https://developer.android.com/reference/java/lang/String.html) **getBirthDate** ()

Gets birth date of the holder.  

#### public [String](https://developer.android.com/reference/java/lang/String.html) **getDocumentType** ()

Gets "DL" for driver licenses, "ID" for ID cards.  

#### public [String](https://developer.android.com/reference/java/lang/String.html) **getExpiryDate** ()

Gets expiry date of the license.  

#### public [String](https://developer.android.com/reference/java/lang/String.html) **getFirstName** ()

Gets holder's first name.  

#### public [String](https://developer.android.com/reference/java/lang/String.html) **getGender** ()

Gets holder's gender. 1 - male, 2 - female.  

#### public [String](https://developer.android.com/reference/java/lang/String.html) **getIssueDate** ()

Gets issue date of the license.

The date format depends on the issuing country. MMDDYYYY for the US, YYYYMMDD for
Canada.  

#### public [String](https://developer.android.com/reference/java/lang/String.html) **getIssuingCountry** ()

Gets country in which DL/ID was issued. US = "USA", Canada = "CAN".  

#### public [String](https://developer.android.com/reference/java/lang/String.html) **getLastName** ()

Gets holder's last name.  

#### public [String](https://developer.android.com/reference/java/lang/String.html) **getLicenseNumber** ()

Gets driver license ID number.  

#### public [String](https://developer.android.com/reference/java/lang/String.html) **getMiddleName** ()

Gets holder's middle name.