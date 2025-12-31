# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/languageid/FirebaseLanguageIdentification.md.txt

# FirebaseLanguageIdentification

public class **FirebaseLanguageIdentification** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
implements [Closeable](https://developer.android.com/reference/java/io/Closeable.html)  
**This class is deprecated.**   

The standalone ML Kit SDK replaces this API. For more information, refer to the [migration guide](https://developers.google.com/ml-kit/migration).

Entry point for Language Identification.

This class can be used from any thread.  

### Constant Summary

|-------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| float                                                                   | [DEFAULT_IDENTIFY_LANGUAGE_CONFIDENCE_THRESHOLD](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/languageid/FirebaseLanguageIdentification#DEFAULT_IDENTIFY_LANGUAGE_CONFIDENCE_THRESHOLD)                     | The default confidence threshold for the [identifyLanguage(String)](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/languageid/FirebaseLanguageIdentification#identifyLanguage(java.lang.String)) call.                   |
| float                                                                   | [DEFAULT_IDENTIFY_POSSIBLE_LANGUAGES_CONFIDENCE_THRESHOLD](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/languageid/FirebaseLanguageIdentification#DEFAULT_IDENTIFY_POSSIBLE_LANGUAGES_CONFIDENCE_THRESHOLD) | The default confidence threshold for the [identifyPossibleLanguages(String)](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/languageid/FirebaseLanguageIdentification#identifyPossibleLanguages(java.lang.String)) call. |
| [String](https://developer.android.com/reference/java/lang/String.html) | [UNDETERMINED_LANGUAGE_CODE](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/languageid/FirebaseLanguageIdentification#UNDETERMINED_LANGUAGE_CODE)                                                             | The BCP-47 code for "undetermined language"                                                                                                                                                                                                                         |

### Public Method Summary

|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| void                                                                                                                                                                                                                                                                                                                   | [close](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/languageid/FirebaseLanguageIdentification#close())() Releases resources when the client is finished using the instance.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)\<[String](https://developer.android.com/reference/java/lang/String.html)\>                                                                                                                                              | [identifyLanguage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/languageid/FirebaseLanguageIdentification#identifyLanguage(java.lang.String))([String](https://developer.android.com/reference/java/lang/String.html) text) Identifies the language in a supplied [String](https://developer.android.com/reference/java/lang/String.html) and returns the most likely language.                                                                                                                                                                                                                                                                                                      |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)\<[List](https://developer.android.com/reference/java/util/List.html)\<[IdentifiedLanguage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/languageid/IdentifiedLanguage)\>\> | [identifyPossibleLanguages](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/languageid/FirebaseLanguageIdentification#identifyPossibleLanguages(java.lang.String))([String](https://developer.android.com/reference/java/lang/String.html) text) Identifies the language in a supplied [String](https://developer.android.com/reference/java/lang/String.html) and returns a list of possible languages, cutting off any languages whose confidence score falls below the threshold in [getConfidenceThreshold()](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/languageid/FirebaseLanguageIdentificationOptions#getConfidenceThreshold()). |

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

From interface java.io.Closeable  

|---------------|---------|
| abstract void | close() |

From interface java.lang.AutoCloseable  

|---------------|---------|
| abstract void | close() |

## Constants

#### public static final float
**DEFAULT_IDENTIFY_LANGUAGE_CONFIDENCE_THRESHOLD**

The default confidence threshold for the [identifyLanguage(String)](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/languageid/FirebaseLanguageIdentification#identifyLanguage(java.lang.String)) call.  
Constant Value: 0.5  

#### public static final float
**DEFAULT_IDENTIFY_POSSIBLE_LANGUAGES_CONFIDENCE_THRESHOLD**

The default confidence threshold for the [identifyPossibleLanguages(String)](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/languageid/FirebaseLanguageIdentification#identifyPossibleLanguages(java.lang.String)) call.  
Constant Value: 0.01  

#### public static final [String](https://developer.android.com/reference/java/lang/String.html)
**UNDETERMINED_LANGUAGE_CODE**

The BCP-47 code for "undetermined language"  
Constant Value: "und"

## Public Methods

#### public void **close** ()

Releases resources when the client is finished using the instance.

The instance can still be used after a call to this method, but might take slightly
longer to produce a result, because it will have to load the model again.  

#### public [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)\<[String](https://developer.android.com/reference/java/lang/String.html)\>
**identifyLanguage** ([String](https://developer.android.com/reference/java/lang/String.html) text)

Identifies the language in a supplied [String](https://developer.android.com/reference/java/lang/String.html) and returns
the most likely language.  

##### Parameters

| text | The text for which to identify the language. Inputs longer than 200 characters are truncated to 200 characters, as longer input does not improve the detection accuracy. |
|------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

##### Returns

- A [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html) that returns a [String](https://developer.android.com/reference/java/lang/String.html) with the BCP-47 language code of the most likely language, or [UNDETERMINED_LANGUAGE_CODE](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/languageid/FirebaseLanguageIdentification#UNDETERMINED_LANGUAGE_CODE) if the confidence was below the threshold of `0.5`.  

#### public [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)\<[List](https://developer.android.com/reference/java/util/List.html)\<[IdentifiedLanguage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/languageid/IdentifiedLanguage)\>\>
**identifyPossibleLanguages** ([String](https://developer.android.com/reference/java/lang/String.html) text)

Identifies the language in a supplied [String](https://developer.android.com/reference/java/lang/String.html) and returns
a list of possible languages, cutting off any languages whose confidence score falls
below the threshold in [getConfidenceThreshold()](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/languageid/FirebaseLanguageIdentificationOptions#getConfidenceThreshold()).

Note that this API assumes the `text` is in a single language; the
returned list contains all estimations for what that language could be, along with a
confidence score for each possible language. The API does *not* detect multiple
languages in a single text.  

##### Parameters

| text | The text for which to identify the language. Inputs longer than 200 characters are truncated to 200 characters, as longer input does not improve the detection accuracy. |
|------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

##### Returns

- A [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html) that returns a [List](https://developer.android.com/reference/java/util/List.html) of [IdentifiedLanguage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/languageid/IdentifiedLanguage)s. The returned list will never be empty; if all languages have lower confidence scores than the threshold, the list will contain a single item with the [UNDETERMINED_LANGUAGE_CODE](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/languageid/FirebaseLanguageIdentification#UNDETERMINED_LANGUAGE_CODE).