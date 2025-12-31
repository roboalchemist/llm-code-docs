# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/languageid/FirebaseLanguageIdentificationOptions.Builder.md.txt

# FirebaseLanguageIdentificationOptions.Builder

public static class **FirebaseLanguageIdentificationOptions.Builder** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
Builder to create a [FirebaseLanguageIdentificationOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/languageid/FirebaseLanguageIdentificationOptions) instance.  

### Public Constructor Summary

|---|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   | [FirebaseLanguageIdentificationOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/languageid/FirebaseLanguageIdentificationOptions.Builder#FirebaseLanguageIdentificationOptions.Builder())() |

### Public Method Summary

|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [FirebaseLanguageIdentificationOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/languageid/FirebaseLanguageIdentificationOptions)                 | [build](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/languageid/FirebaseLanguageIdentificationOptions.Builder#build())() Creates a new [FirebaseLanguageIdentificationOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/languageid/FirebaseLanguageIdentificationOptions) instance.                                                                                                                                                                                                                                                                                                                          |
| [FirebaseLanguageIdentificationOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/languageid/FirebaseLanguageIdentificationOptions.Builder) | [setConfidenceThreshold](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/languageid/FirebaseLanguageIdentificationOptions.Builder#setConfidenceThreshold(float))(float confidenceThreshold) Sets the minimum confidence for the [identifyLanguage(String)](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/languageid/FirebaseLanguageIdentification#identifyLanguage(java.lang.String)) or [identifyPossibleLanguages(String)](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/languageid/FirebaseLanguageIdentification#identifyPossibleLanguages(java.lang.String)) call. |

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

#### public **FirebaseLanguageIdentificationOptions.Builder** ()

## Public Methods

#### public [FirebaseLanguageIdentificationOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/languageid/FirebaseLanguageIdentificationOptions) **build** ()

Creates a new [FirebaseLanguageIdentificationOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/languageid/FirebaseLanguageIdentificationOptions) instance.  

#### public [FirebaseLanguageIdentificationOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/languageid/FirebaseLanguageIdentificationOptions.Builder) **setConfidenceThreshold** (float confidenceThreshold)

Sets the minimum confidence for the [identifyLanguage(String)](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/languageid/FirebaseLanguageIdentification#identifyLanguage(java.lang.String)) or [identifyPossibleLanguages(String)](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/languageid/FirebaseLanguageIdentification#identifyPossibleLanguages(java.lang.String)) call.

If no value is set, a default value is used, depending on the method call.  

##### Parameters

| confidenceThreshold | The minimum confidence for the [identifyLanguage(String)](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/languageid/FirebaseLanguageIdentification#identifyLanguage(java.lang.String)) or [identifyPossibleLanguages(String)](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/languageid/FirebaseLanguageIdentification#identifyPossibleLanguages(java.lang.String)) call. |
|---------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

##### Returns

- This object, for chaining method calls.