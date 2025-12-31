# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/RecognizedLanguage.md.txt

# RecognizedLanguage

public class **RecognizedLanguage** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
Recognized language for a structural component.  

### Public Method Summary

|-------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| boolean                                                                 | [equals](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/RecognizedLanguage#equals(java.lang.Object))([Object](https://developer.android.com/reference/java/lang/Object.html) o) |
| [String](https://developer.android.com/reference/java/lang/String.html) | [getLanguageCode](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/RecognizedLanguage#getLanguageCode())() The BCP-47 language code, such as "en-US" or "sr-Latn".                |
| int                                                                     | [hashCode](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/RecognizedLanguage#hashCode())()                                                                                      |

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

#### public [String](https://developer.android.com/reference/java/lang/String.html) **getLanguageCode** ()

The BCP-47 language code, such as "en-US" or "sr-Latn". For more information, see
[Unicode Locale Identifier](https://www.unicode.org/reports/tr35/#Unicode_locale_identifier)  

#### public int **hashCode** ()