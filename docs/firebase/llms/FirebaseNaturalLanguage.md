# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/FirebaseNaturalLanguage.md.txt

# FirebaseNaturalLanguage

public class **FirebaseNaturalLanguage** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
**This class is deprecated.**   

The standalone ML Kit SDK replaces this API. For more information, refer to the [migration guide](https://developers.google.com/ml-kit/migration).

Entry class for Firebase machine learning natural language services.

To use this class, get an instance via [getInstance()](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/FirebaseNaturalLanguage#getInstance()) or [getInstance(FirebaseApp)](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/FirebaseNaturalLanguage#getInstance(com.google.firebase.FirebaseApp)), and then get an instance of a detector. The code below
is an example of getting an instance of smart reply:  


     FirebaseSmartReply smartReply = FirebaseNaturalLanguage.getInstance().getSmartReply();
     Task task = smartReply.suggestReplies("How are you?");
     
### Public Method Summary

|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| static [FirebaseNaturalLanguage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/FirebaseNaturalLanguage)                   | [getInstance](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/FirebaseNaturalLanguage#getInstance())() Gets an instance of [FirebaseNaturalLanguage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/FirebaseNaturalLanguage) associated with the default [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp).                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| static [FirebaseNaturalLanguage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/FirebaseNaturalLanguage)                   | [getInstance](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/FirebaseNaturalLanguage#getInstance(com.google.firebase.FirebaseApp))([FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp) app) Gets an instance of [FirebaseNaturalLanguage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/FirebaseNaturalLanguage) associated with the supplied [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp).                                                                                                                                                                                                                                                                                                 |
| [FirebaseLanguageIdentification](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/languageid/FirebaseLanguageIdentification) | [getLanguageIdentification](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/FirebaseNaturalLanguage#getLanguageIdentification())() Gets an instance of [FirebaseLanguageIdentification](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/languageid/FirebaseLanguageIdentification), which identifies the language for a given text input.                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [FirebaseLanguageIdentification](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/languageid/FirebaseLanguageIdentification) | [getLanguageIdentification](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/FirebaseNaturalLanguage#getLanguageIdentification(com.google.firebase.ml.naturallanguage.languageid.FirebaseLanguageIdentificationOptions))([FirebaseLanguageIdentificationOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/languageid/FirebaseLanguageIdentificationOptions) options) Gets an instance of [FirebaseLanguageIdentification](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/languageid/FirebaseLanguageIdentification), which identifies the language for a given text input, with the given [options](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/languageid/FirebaseLanguageIdentificationOptions). |
| [FirebaseSmartReply](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/smartreply/FirebaseSmartReply)                         | [getSmartReply](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/FirebaseNaturalLanguage#getSmartReply())() Gets a [FirebaseSmartReply](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/smartreply/FirebaseSmartReply) that suggests replies for a given text input.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| FirebaseTranslator                                                                                                                                                    | [getTranslator](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/FirebaseNaturalLanguage#getTranslator(com.google.firebase.ml.naturallanguage.translate.FirebaseTranslatorOptions))(FirebaseTranslatorOptions options) Gets an instance of [FirebaseTranslator](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/translate/FirebaseTranslator) that can translate from the source language specified in [options](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/translate/FirebaseTranslatorOptions) to the target language specified in [options](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/translate/FirebaseTranslatorOptions).                                                                      |

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

#### public static [FirebaseNaturalLanguage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/FirebaseNaturalLanguage) **getInstance**
()

Gets an instance of [FirebaseNaturalLanguage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/FirebaseNaturalLanguage) associated with the default [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp).  

#### public static [FirebaseNaturalLanguage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/FirebaseNaturalLanguage) **getInstance**
([FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp) app)

Gets an instance of [FirebaseNaturalLanguage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/FirebaseNaturalLanguage) associated with the supplied [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp).  

##### Parameters

| app | the [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp) to associate this [FirebaseNaturalLanguage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/FirebaseNaturalLanguage) with. |
|-----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

#### public [FirebaseLanguageIdentification](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/languageid/FirebaseLanguageIdentification) **getLanguageIdentification** ()

Gets an instance of [FirebaseLanguageIdentification](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/languageid/FirebaseLanguageIdentification), which identifies the language for a given
text input.  

#### public [FirebaseLanguageIdentification](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/languageid/FirebaseLanguageIdentification) **getLanguageIdentification** ([FirebaseLanguageIdentificationOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/languageid/FirebaseLanguageIdentificationOptions) options)

Gets an instance of [FirebaseLanguageIdentification](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/languageid/FirebaseLanguageIdentification), which identifies the language for a given
text input, with the given [options](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/languageid/FirebaseLanguageIdentificationOptions).  

#### public [FirebaseSmartReply](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/smartreply/FirebaseSmartReply) **getSmartReply**
()

Gets a [FirebaseSmartReply](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/smartreply/FirebaseSmartReply) that suggests replies for a given text input.  

##### Returns

- an instance of [FirebaseSmartReply](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/smartreply/FirebaseSmartReply) associated with the default [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp). Note that multiple calls of this API always return the same instance and under the same [FirebaseNaturalLanguage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/FirebaseNaturalLanguage).  

#### public FirebaseTranslator
**getTranslator** (FirebaseTranslatorOptions options)

Gets an instance of [FirebaseTranslator](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/translate/FirebaseTranslator) that can translate from the source language specified in
[options](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/translate/FirebaseTranslatorOptions) to the target language specified in [options](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/translate/FirebaseTranslatorOptions).