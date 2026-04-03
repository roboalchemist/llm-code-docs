# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/translate/FirebaseTranslator.md.txt

# FirebaseTranslator

public class **FirebaseTranslator** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
implements [Closeable](https://developer.android.com/reference/java/io/Closeable.html)  
**This class is deprecated.**   

The standalone ML Kit SDK replaces this API. For more information, refer to the [migration guide](https://developers.google.com/ml-kit/migration).

Entry point for Translation.

This class can be used from any thread.  

### Public Method Summary

|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| void                                                                                                                                                                      | [close](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/translate/FirebaseTranslator#close())() Closes the translator object and releases any system resources associated with it.                                                                                                                                                                                                                                                                                                                               |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)\<[Void](https://developer.android.com/reference/java/lang/Void.html)\>     | [downloadModelIfNeeded](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/translate/FirebaseTranslator#downloadModelIfNeeded())() Downloads the model files required for translation, if they are not already present.                                                                                                                                                                                                                                                                                             |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)\<[Void](https://developer.android.com/reference/java/lang/Void.html)\>     | [downloadModelIfNeeded](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/translate/FirebaseTranslator#downloadModelIfNeeded(com.google.firebase.ml.common.modeldownload.FirebaseModelDownloadConditions))([FirebaseModelDownloadConditions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseModelDownloadConditions) conditions) Downloads the model files required for translation, if they are not already present, when the given `conditions` are met. |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)\<[String](https://developer.android.com/reference/java/lang/String.html)\> | [translate](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/translate/FirebaseTranslator#translate(java.lang.String))([String](https://developer.android.com/reference/java/lang/String.html) input) Translates the given `input` from the source language into the target language.                                                                                                                                                                                                                             |

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

## Public Methods

#### public void **close** ()

Closes the translator object and releases any system resources associated with
it.  

#### public [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)\<[Void](https://developer.android.com/reference/java/lang/Void.html)\>
**downloadModelIfNeeded** ()

Downloads the model files required for translation, if they are not already present.
The download will be triggered as soon as there is a network connection, with no other
conditions.  

##### Returns

- A [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html) that will be completed when the required files have been downloaded.  

#### public [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)\<[Void](https://developer.android.com/reference/java/lang/Void.html)\>
**downloadModelIfNeeded** ([FirebaseModelDownloadConditions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseModelDownloadConditions) conditions)

Downloads the model files required for translation, if they are not already present,
when the given `conditions` are met.  

##### Returns

- A [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html) that will be completed when the required files have been downloaded.  

#### public [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)\<[String](https://developer.android.com/reference/java/lang/String.html)\>
**translate** ([String](https://developer.android.com/reference/java/lang/String.html) input)

Translates the given `input` from the source language into the target
language. Source and target languages are provided in the [options](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/translate/FirebaseTranslatorOptions) object that was used to get the instance.  

##### Parameters

| input | A string in the source language |
|-------|---------------------------------|

##### Returns

- The translated string in the target language