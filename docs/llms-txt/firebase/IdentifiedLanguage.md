# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/languageid/IdentifiedLanguage.md.txt

# IdentifiedLanguage

public final class **IdentifiedLanguage** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
**This class is deprecated.**   

The standalone ML Kit SDK replaces this API. For more information, refer to the [migration guide](https://developers.google.com/ml-kit/migration).

A language identified by [identifyPossibleLanguages(String)](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/languageid/FirebaseLanguageIdentification#identifyPossibleLanguages(java.lang.String)).  

### Public Method Summary

|-------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| boolean                                                                 | [equals](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/languageid/IdentifiedLanguage#equals(java.lang.Object))([Object](https://developer.android.com/reference/java/lang/Object.html) o) |
| float                                                                   | [getConfidence](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/languageid/IdentifiedLanguage#getConfidence())() Returns the confidence score associated with the language.                 |
| [String](https://developer.android.com/reference/java/lang/String.html) | [getLanguageCode](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/languageid/IdentifiedLanguage#getLanguageCode())() Returns the BCP-47 language code for the language.                     |
| int                                                                     | [hashCode](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/languageid/IdentifiedLanguage#hashCode())()                                                                                      |
| [String](https://developer.android.com/reference/java/lang/String.html) | [toString](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/languageid/IdentifiedLanguage#toString())()                                                                                      |

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

#### public float **getConfidence** ()

Returns the confidence score associated with the language. The value is between 0
and 1, and greater or equal to the confidence threshold specified for [identifyPossibleLanguages(String)](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/languageid/FirebaseLanguageIdentification#identifyPossibleLanguages(java.lang.String)) in [FirebaseLanguageIdentificationOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/languageid/FirebaseLanguageIdentificationOptions).  

#### public [String](https://developer.android.com/reference/java/lang/String.html) **getLanguageCode** ()

Returns the BCP-47 language code for the language.  

##### See Also

- [BCP-47 spec](https://tools.ietf.org/html/bcp47)  

#### public int **hashCode** ()

#### public [String](https://developer.android.com/reference/java/lang/String.html) **toString** ()