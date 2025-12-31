# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.ContactInfo.md.txt

# FirebaseVisionBarcode.ContactInfo

public static class **FirebaseVisionBarcode.ContactInfo** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
A person's or organization's business card. For example a VCARD.  

### Public Method Summary

|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [List](https://developer.android.com/reference/java/util/List.html)\<[FirebaseVisionBarcode.Address](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.Address)\> | [getAddresses](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.ContactInfo#getAddresses())() Gets contact person's addresses.          |
| [List](https://developer.android.com/reference/java/util/List.html)\<[FirebaseVisionBarcode.Email](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.Email)\>     | [getEmails](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.ContactInfo#getEmails())() Gets contact person's emails.                   |
| [FirebaseVisionBarcode.PersonName](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.PersonName)                                                                  | [getName](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.ContactInfo#getName())() Gets contact person's name.                         |
| [String](https://developer.android.com/reference/java/lang/String.html)                                                                                                                                                        | [getOrganization](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.ContactInfo#getOrganization())() Gets contact person's organization. |
| [List](https://developer.android.com/reference/java/util/List.html)\<[FirebaseVisionBarcode.Phone](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.Phone)\>     | [getPhones](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.ContactInfo#getPhones())() Gets contact person's phones.                   |
| [String](https://developer.android.com/reference/java/lang/String.html)                                                                                                                                                        | [getTitle](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.ContactInfo#getTitle())() Gets contact person's title.                      |
| [String\[\]](https://developer.android.com/reference/java/lang/String.html)                                                                                                                                                    | [getUrls](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.ContactInfo#getUrls())() Gets contact person's urls.                         |

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

#### public [List](https://developer.android.com/reference/java/util/List.html)\<[FirebaseVisionBarcode.Address](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.Address)\>
**getAddresses** ()

Gets contact person's addresses.

Returns an empty list if nothing found.  

#### public [List](https://developer.android.com/reference/java/util/List.html)\<[FirebaseVisionBarcode.Email](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.Email)\>
**getEmails** ()

Gets contact person's emails.

Returns an empty list if nothing found.  

#### public [FirebaseVisionBarcode.PersonName](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.PersonName) **getName** ()

Gets contact person's name.  

#### public [String](https://developer.android.com/reference/java/lang/String.html) **getOrganization** ()

Gets contact person's organization.  

#### public [List](https://developer.android.com/reference/java/util/List.html)\<[FirebaseVisionBarcode.Phone](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.Phone)\>
**getPhones** ()

Gets contact person's phones.

Returns an empty list if nothing found.  

#### public [String](https://developer.android.com/reference/java/lang/String.html) **getTitle** ()

Gets contact person's title.  

#### public [String\[\]](https://developer.android.com/reference/java/lang/String.html) **getUrls** ()

Gets contact person's urls.