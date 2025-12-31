# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/FirebaseUserActions.md.txt

# FirebaseUserActions

public abstract class **FirebaseUserActions** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
Provides methods for logging actions that the user takes in the app.

This is a simple example for logging that the user has started to view an article:  

    FirebaseUserActions.getInstance(getApplicationContext()).start(
       Actions.newView(
         "Index your app with Google App Indexing",
         "//example.net/articles/02101984.html"));
     
### Constant Summary

|-------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [String](https://developer.android.com/reference/java/lang/String.html) | [APP_INDEXING_API_TAG](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/FirebaseUserActions#APP_INDEXING_API_TAG) | The tag used for logging debug information for calls to [FirebaseUserActions](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/FirebaseUserActions) class. |

### Public Constructor Summary

|---|-------------------------------------------------------------------------------------------------------------------------------------------------------|
|   | [FirebaseUserActions](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/FirebaseUserActions#FirebaseUserActions())() |

### Public Method Summary

|---------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| abstract Task\<[Void](https://developer.android.com/reference/java/lang/Void.html)\>                                                              | [end](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/FirebaseUserActions#end(com.google.firebase.appindexing.Action))([Action](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Action) action) Logs that the user has stopped doing something in the app.                                                                          |
| synchronized static [FirebaseUserActions](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/FirebaseUserActions) | [getInstance](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/FirebaseUserActions#getInstance(android.content.Context))([Context](https://developer.android.com/reference/android/content/Context.html) context) Returns an instance of [FirebaseUserActions](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/FirebaseUserActions). |
| abstract Task\<[Void](https://developer.android.com/reference/java/lang/Void.html)\>                                                              | [start](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/FirebaseUserActions#start(com.google.firebase.appindexing.Action))([Action](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Action) action) Logs that the user has started doing something in the app.                                                                      |

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

## Constants

#### public static final [String](https://developer.android.com/reference/java/lang/String.html)
**APP_INDEXING_API_TAG**

The tag used for logging debug information for calls to [FirebaseUserActions](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/FirebaseUserActions)
class.

To enable logging:  

`adb shell setprop `*log.tag.FirebaseUserActions*` `*DEBUG*  
Constant Value: "FirebaseUserActions"

## Public Constructors

#### public **FirebaseUserActions** ()

## Public Methods

#### public abstract Task\<[Void](https://developer.android.com/reference/java/lang/Void.html)\> **end** ([Action](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Action) action)

Logs that the user has stopped doing something in the app.

Use this method for a user action of some duration that has come to an end, like
when the user has finished viewing an article or stopped listening to a song, as well
as for instantaneous actions the user has taken, such as sending a message or adding a
song to a playlist. For these instantaneous actions, don't call [start(Action)](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/FirebaseUserActions#start(com.google.firebase.appindexing.Action)) at all, but just [end(Action)](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/FirebaseUserActions#end(com.google.firebase.appindexing.Action)).  

##### Parameters

| action | The [Action](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Action) describing either the instantaneous action the user has just taken, or the more long-lived activity the user has stopped doing in the app; for the latter [start(Action)](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/FirebaseUserActions#start(com.google.firebase.appindexing.Action)) should be called before calling [end(Action)](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/FirebaseUserActions#end(com.google.firebase.appindexing.Action)). |
|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

##### Returns

- A [Task](https://firebase.google.com/docs/reference/android/com/google/android/gms/tasks/Task) indicating the result of the operation.  

#### public static synchronized [FirebaseUserActions](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/FirebaseUserActions)
**getInstance** ([Context](https://developer.android.com/reference/android/content/Context.html) context)

Returns an instance of [FirebaseUserActions](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/FirebaseUserActions).

This method does not require FirebaseApp initialization. Instead, the application
context is inferred from the `context` that is explicitly passed in.  

#### public abstract Task\<[Void](https://developer.android.com/reference/java/lang/Void.html)\> **start** ([Action](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Action) action)

Logs that the user has started doing something in the app.

Use this method for a user action of some duration, like viewing an article or
listening to a song. If the action is instantaneous, such as sending a message or
adding a song to a playlist, then make a single call to [end(Action)](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/FirebaseUserActions#end(com.google.firebase.appindexing.Action)) instead.  

##### Parameters

| action | The [Action](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Action) describing what the user has started doing in the app. |
|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|

##### Returns

- A [Task](https://firebase.google.com/docs/reference/android/com/google/android/gms/tasks/Task) indicating the result of the operation.