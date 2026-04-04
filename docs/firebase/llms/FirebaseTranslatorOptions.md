# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/translate/FirebaseTranslatorOptions.md.txt

# FirebaseTranslatorOptions

public class **FirebaseTranslatorOptions** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
**This class is deprecated.**   

The standalone ML Kit SDK replaces this API. For more information, refer to the [migration guide](https://developers.google.com/ml-kit/migration).

Options for [FirebaseTranslator](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/translate/FirebaseTranslator)  

### Nested Class Summary

|-------|---|---|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| class | [FirebaseTranslatorOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/translate/FirebaseTranslatorOptions.Builder) || Builder to create a [FirebaseTranslatorOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/translate/FirebaseTranslatorOptions) instance. |

### Public Method Summary

|-------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| boolean                                                                 | [equals](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/translate/FirebaseTranslatorOptions#equals(java.lang.Object))([Object](https://developer.android.com/reference/java/lang/Object.html) o)                                                                                                                                                            |
| int                                                                     | [getSourceLanguage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/translate/FirebaseTranslatorOptions#getSourceLanguage())() Returns the [FirebaseTranslateLanguage.TranslateLanguage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/translate/FirebaseTranslateLanguage.TranslateLanguage) to translate from. |
| [String](https://developer.android.com/reference/java/lang/String.html) | [getSourceLanguageCode](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/translate/FirebaseTranslatorOptions#getSourceLanguageCode())() Returns BCP-47 language code for the language to translate from.                                                                                                                                                      |
| int                                                                     | [getTargetLanguage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/translate/FirebaseTranslatorOptions#getTargetLanguage())() Returns the [FirebaseTranslateLanguage.TranslateLanguage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/translate/FirebaseTranslateLanguage.TranslateLanguage) to translate to.   |
| [String](https://developer.android.com/reference/java/lang/String.html) | [getTargetLanguageCode](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/translate/FirebaseTranslatorOptions#getTargetLanguageCode())() Returns BCP-47 language tag for the language to translate to.                                                                                                                                                         |
| int                                                                     | [hashCode](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/translate/FirebaseTranslatorOptions#hashCode())()                                                                                                                                                                                                                                                 |

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

#### public int **getSourceLanguage** ()

Returns the [FirebaseTranslateLanguage.TranslateLanguage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/translate/FirebaseTranslateLanguage.TranslateLanguage) to translate from.  

#### public [String](https://developer.android.com/reference/java/lang/String.html) **getSourceLanguageCode** ()

Returns BCP-47 language code for the language to translate from.  

#### public int **getTargetLanguage** ()

Returns the [FirebaseTranslateLanguage.TranslateLanguage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/translate/FirebaseTranslateLanguage.TranslateLanguage) to translate to.  

#### public [String](https://developer.android.com/reference/java/lang/String.html) **getTargetLanguageCode** ()

Returns BCP-47 language tag for the language to translate to.  

#### public int **hashCode** ()