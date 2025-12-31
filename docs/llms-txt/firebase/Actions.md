# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/Actions.md.txt

# Actions

public final class **Actions** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
Provides convenience methods to construct common type of actions.  

### Public Constructor Summary

|---|----------------------------------------------------------------------------------------------------------------------------|
|   | [Actions](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/Actions#Actions())() |

### Public Method Summary

|------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| static [Action](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Action) | [newView](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/Actions#newView(java.lang.String,%20java.lang.String))([String](https://developer.android.com/reference/java/lang/String.html) name, [String](https://developer.android.com/reference/java/lang/String.html) url) Constructs a "view" action. |

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

#### public **Actions** ()

## Public Methods

#### public static [Action](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Action)
**newView** ([String](https://developer.android.com/reference/java/lang/String.html) name, [String](https://developer.android.com/reference/java/lang/String.html) url)

Constructs a "view" action.  

##### Parameters

| name |                         The name of the object being viewed (e.g. the title of an article).                         |
| url  | The URL of the object that is viewed (this URL needs to be handled by the app to take the user to the right place). |
|------|---------------------------------------------------------------------------------------------------------------------|