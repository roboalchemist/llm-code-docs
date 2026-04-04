# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.PersonName.md.txt

# FirebaseVisionBarcode.PersonName

public static class **FirebaseVisionBarcode.PersonName** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
A person's name, both formatted version and individual name components.  

### Public Method Summary

|-------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [String](https://developer.android.com/reference/java/lang/String.html) | [getFirst](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.PersonName#getFirst())() Gets first name.                                                                      |
| [String](https://developer.android.com/reference/java/lang/String.html) | [getFormattedName](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.PersonName#getFormattedName())() Gets the properly formatted name.                                     |
| [String](https://developer.android.com/reference/java/lang/String.html) | [getLast](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.PersonName#getLast())() Gets last name.                                                                         |
| [String](https://developer.android.com/reference/java/lang/String.html) | [getMiddle](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.PersonName#getMiddle())() Gets middle name.                                                                   |
| [String](https://developer.android.com/reference/java/lang/String.html) | [getPrefix](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.PersonName#getPrefix())() Gets prefix of the name.                                                            |
| [String](https://developer.android.com/reference/java/lang/String.html) | [getPronunciation](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.PersonName#getPronunciation())() Designates a text string to be set as the kana name in the phonebook. |
| [String](https://developer.android.com/reference/java/lang/String.html) | [getSuffix](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.PersonName#getSuffix())() Gets suffix of the person's name.                                                   |

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

#### public [String](https://developer.android.com/reference/java/lang/String.html) **getFirst** ()

Gets first name.  

#### public [String](https://developer.android.com/reference/java/lang/String.html) **getFormattedName** ()

Gets the properly formatted name.  

#### public [String](https://developer.android.com/reference/java/lang/String.html) **getLast** ()

Gets last name.  

#### public [String](https://developer.android.com/reference/java/lang/String.html) **getMiddle** ()

Gets middle name.  

#### public [String](https://developer.android.com/reference/java/lang/String.html) **getPrefix** ()

Gets prefix of the name.  

#### public [String](https://developer.android.com/reference/java/lang/String.html) **getPronunciation** ()

Designates a text string to be set as the kana name in the phonebook. Used for
Japanese contacts.  

#### public [String](https://developer.android.com/reference/java/lang/String.html) **getSuffix** ()

Gets suffix of the person's name.