# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/translate/FirebaseTranslatorOptions.Builder.md.txt

# FirebaseTranslatorOptions.Builder

public static class **FirebaseTranslatorOptions.Builder** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
Builder to create a [FirebaseTranslatorOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/translate/FirebaseTranslatorOptions) instance.  

### Public Constructor Summary

|---|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   | [FirebaseTranslatorOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/translate/FirebaseTranslatorOptions.Builder#FirebaseTranslatorOptions.Builder())() |

### Public Method Summary

|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [FirebaseTranslatorOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/translate/FirebaseTranslatorOptions)                 | [build](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/translate/FirebaseTranslatorOptions.Builder#build())() Creates a new [FirebaseTranslatorOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/translate/FirebaseTranslatorOptions) instance. |
| [FirebaseTranslatorOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/translate/FirebaseTranslatorOptions.Builder) | [setSourceLanguage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/translate/FirebaseTranslatorOptions.Builder#setSourceLanguage(int))(int sourceLanguage) Sets the language to translate from.                                                                                                  |
| [FirebaseTranslatorOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/translate/FirebaseTranslatorOptions.Builder) | [setTargetLanguage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/translate/FirebaseTranslatorOptions.Builder#setTargetLanguage(int))(int targetLanguage) Sets the language to translate to.                                                                                                    |

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

#### public **FirebaseTranslatorOptions.Builder** ()

## Public Methods

#### public [FirebaseTranslatorOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/translate/FirebaseTranslatorOptions) **build**
()

Creates a new [FirebaseTranslatorOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/translate/FirebaseTranslatorOptions) instance. The source and target language should be
set before calling this method.  

#### public [FirebaseTranslatorOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/translate/FirebaseTranslatorOptions.Builder) **setSourceLanguage** (int sourceLanguage)

Sets the language to translate from.  

##### Parameters

| sourceLanguage | the [FirebaseTranslateLanguage.TranslateLanguage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/translate/FirebaseTranslateLanguage.TranslateLanguage) to translate from. |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

##### Returns

- This object, for chaining method calls.  

#### public [FirebaseTranslatorOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/translate/FirebaseTranslatorOptions.Builder) **setTargetLanguage** (int targetLanguage)

Sets the language to translate to.  

##### Parameters

| targetLanguage | the [FirebaseTranslateLanguage.TranslateLanguage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/translate/FirebaseTranslateLanguage.TranslateLanguage) to translate to. |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

##### Returns

- This object, for chaining method calls.