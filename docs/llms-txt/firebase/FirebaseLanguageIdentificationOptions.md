# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/languageid/FirebaseLanguageIdentificationOptions.md.txt

# FirebaseLanguageIdentificationOptions

public class **FirebaseLanguageIdentificationOptions** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
**This class is deprecated.**   

The standalone ML Kit SDK replaces this API. For more information, refer to the [migration guide](https://developers.google.com/ml-kit/migration).

Options for [FirebaseLanguageIdentification](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/languageid/FirebaseLanguageIdentification)  

### Nested Class Summary

|-------|---|---|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| class | [FirebaseLanguageIdentificationOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/languageid/FirebaseLanguageIdentificationOptions.Builder) || Builder to create a [FirebaseLanguageIdentificationOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/languageid/FirebaseLanguageIdentificationOptions) instance. |

### Public Method Summary

|-----------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| boolean                                                               | [equals](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/languageid/FirebaseLanguageIdentificationOptions#equals(java.lang.Object))([Object](https://developer.android.com/reference/java/lang/Object.html) o)                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [Float](https://developer.android.com/reference/java/lang/Float.html) | [getConfidenceThreshold](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/languageid/FirebaseLanguageIdentificationOptions#getConfidenceThreshold())() Returns the minimum confidence for the [identifyLanguage(String)](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/languageid/FirebaseLanguageIdentification#identifyLanguage(java.lang.String)) or [identifyPossibleLanguages(String)](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/languageid/FirebaseLanguageIdentification#identifyPossibleLanguages(java.lang.String)) call, or `null` if the default value should be used. |
| int                                                                   | [hashCode](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/languageid/FirebaseLanguageIdentificationOptions#hashCode())()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

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

#### public boolean **equals** ([Object](https://developer.android.com/reference/java/lang/Object.html) o)

#### public [Float](https://developer.android.com/reference/java/lang/Float.html) **getConfidenceThreshold** ()

Returns the minimum confidence for the [identifyLanguage(String)](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/languageid/FirebaseLanguageIdentification#identifyLanguage(java.lang.String)) or [identifyPossibleLanguages(String)](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/languageid/FirebaseLanguageIdentification#identifyPossibleLanguages(java.lang.String)) call, or `null` if the default
value should be used.  

#### public int **hashCode** ()