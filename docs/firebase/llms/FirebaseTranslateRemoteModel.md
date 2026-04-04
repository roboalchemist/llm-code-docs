# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/translate/FirebaseTranslateRemoteModel.md.txt

# FirebaseTranslateRemoteModel

public class **FirebaseTranslateRemoteModel** extends [FirebaseRemoteModel](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseRemoteModel)  
**This class is deprecated.**   

The standalone ML Kit SDK replaces this API. For more information, refer to the [migration guide](https://developers.google.com/ml-kit/migration).

Information about a downloaded or to-be-downloaded model for translation.  

### Nested Class Summary

|-------|---|---|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| class | [FirebaseTranslateRemoteModel.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/translate/FirebaseTranslateRemoteModel.Builder) || Builder for a [FirebaseTranslateRemoteModel](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/translate/FirebaseTranslateRemoteModel). |

### Public Method Summary

|-------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| boolean                                                                 | [equals](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/translate/FirebaseTranslateRemoteModel#equals(java.lang.Object))([Object](https://developer.android.com/reference/java/lang/Object.html) o)                                                                                                                                                 |
| int                                                                     | [getLanguage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/translate/FirebaseTranslateRemoteModel#getLanguage())() The [FirebaseTranslateLanguage.TranslateLanguage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/translate/FirebaseTranslateLanguage.TranslateLanguage) associated with this model. |
| [String](https://developer.android.com/reference/java/lang/String.html) | [getLanguageCode](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/translate/FirebaseTranslateRemoteModel#getLanguageCode())() The BCP-47 language code associated with this model.                                                                                                                                                                   |
| int                                                                     | [hashCode](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/translate/FirebaseTranslateRemoteModel#hashCode())()                                                                                                                                                                                                                                      |

### Inherited Method Summary

From class com.google.firebase.ml.common.modeldownload.FirebaseRemoteModel  

|---------|--------------------------------------------------------------------------------------|
| boolean | equals([Object](https://developer.android.com/reference/java/lang/Object.html) arg0) |
| int     | hashCode()                                                                           |

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

#### public int **getLanguage** ()

The [FirebaseTranslateLanguage.TranslateLanguage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/translate/FirebaseTranslateLanguage.TranslateLanguage) associated with this model.  

#### public [String](https://developer.android.com/reference/java/lang/String.html) **getLanguageCode** ()

The BCP-47 language code associated with this model.  

#### public int **hashCode** ()