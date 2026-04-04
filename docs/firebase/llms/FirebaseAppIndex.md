# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/FirebaseAppIndex.md.txt

# FirebaseAppIndex

public abstract class **FirebaseAppIndex** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
Provides methods for managing the index, by inserting, updating and removing
[Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable)s
in the app.

This is a simple example for inserting a user's recipe into the index:  

    FirebaseAppIndex appIndex = FirebaseAppIndex.getInstance(getApplicationContext());
     Indexable recipe = new Indexable.Builder()
         .setName("My new brownie recipe")
         .setUrl("//example.net/recipes/02101984")
         .build();
     appIndex.update(recipe);
     
The unique identifier for an [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable) is
the URL. This means that there cannot be multiple different [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable)s
with the same URL, but you can call [update(Indexable...)](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/FirebaseAppIndex#update(com.google.firebase.appindexing.Indexable...)) multiple times to update the same [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable) as
it changes over time.

The app should handle the [ACTION_UPDATE_INDEX](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/FirebaseAppIndex#ACTION_UPDATE_INDEX) intent so that Google Play services can update the on-device
index in the following situations:

- When the app is installed on a device.
- If an existing version of the app is updated to a version that supports the intent.
- Periodic calls over time to accurately refresh the index.
- If the on-device index is lost for any reason (e.g., if the index is corrupted).

The static accessors and object methods of FirebaseAppIndex are thread-safe. However,
Indexables are not. Therefore, you should not insert, update, or remove the same Indexable
from different threads.  

### Constant Summary

|-------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [String](https://developer.android.com/reference/java/lang/String.html) | [ACTION_UPDATE_INDEX](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/FirebaseAppIndex#ACTION_UPDATE_INDEX)                             | The intent action that will be used by the indexing service to request an app to update all its [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable)s.                                                                                                                         |
| [String](https://developer.android.com/reference/java/lang/String.html) | [APP_INDEXING_API_TAG](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/FirebaseAppIndex#APP_INDEXING_API_TAG)                           | The tag used for logging debug information for calls to [FirebaseAppIndex](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/FirebaseAppIndex) class.                                                                                                                                              |
| [String](https://developer.android.com/reference/java/lang/String.html) | [EXTRA_UPDATE_INDEX_REASON](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/FirebaseAppIndex#EXTRA_UPDATE_INDEX_REASON)                 | Used as an int extra field in [ACTION_UPDATE_INDEX](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/FirebaseAppIndex#ACTION_UPDATE_INDEX) intent to indicate the reason for the update request.                                                                                                  |
| int                                                                     | [EXTRA_UPDATE_INDEX_REASON_REBUILD](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/FirebaseAppIndex#EXTRA_UPDATE_INDEX_REASON_REBUILD) | An int value for [EXTRA_UPDATE_INDEX_REASON](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/FirebaseAppIndex#EXTRA_UPDATE_INDEX_REASON) when the update request is sent because the index needs to be fully rebuilt.                                                                            |
| int                                                                     | [EXTRA_UPDATE_INDEX_REASON_REFRESH](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/FirebaseAppIndex#EXTRA_UPDATE_INDEX_REASON_REFRESH) | An int value for [EXTRA_UPDATE_INDEX_REASON](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/FirebaseAppIndex#EXTRA_UPDATE_INDEX_REASON) when the update request is sent because some content has not been re-indexed in some time (\>30 days), and needs to be re-indexed to stay in the index. |

### Public Constructor Summary

|---|----------------------------------------------------------------------------------------------------------------------------------------------|
|   | [FirebaseAppIndex](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/FirebaseAppIndex#FirebaseAppIndex())() |

### Public Method Summary

|---------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| synchronized static [FirebaseAppIndex](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/FirebaseAppIndex) | [getInstance](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/FirebaseAppIndex#getInstance(android.content.Context))([Context](https://developer.android.com/reference/android/content/Context.html) context) Returns an instance of [FirebaseAppIndex](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/FirebaseAppIndex).                                                        |
| abstract Task\<[Void](https://developer.android.com/reference/java/lang/Void.html)\>                                                        | [remove](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/FirebaseAppIndex#remove(java.lang.String...))([String...](https://developer.android.com/reference/java/lang/String.html) urls) Removes one or multiple [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable)s from the index.                                                                           |
| abstract Task\<[Void](https://developer.android.com/reference/java/lang/Void.html)\>                                                        | [removeAll](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/FirebaseAppIndex#removeAll())() Removes all data from the index.                                                                                                                                                                                                                                                                                         |
| abstract Task\<[Void](https://developer.android.com/reference/java/lang/Void.html)\>                                                        | [update](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/FirebaseAppIndex#update(com.google.firebase.appindexing.Indexable...))([Indexable...](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable) indexables) Inserts or updates one or multiple [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable)s in the index. |

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
**ACTION_UPDATE_INDEX**

The intent action that will be used by the indexing service to request an app to
update all its [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable)s.
When specifying the intent in the Manifest file you can also define a permission so
that Google Play services is the only app allowed to trigger the intent.  

Example entry for the Manifest file:  

```
 <receiver android:name=".MyIndexingReceiver"
     android:exported="true"
     android:permission="com.google.android.gms.permission.APPINDEXING">
     <intent-filter>
         <action android:name="com.google.firebase.appindexing.UPDATE_INDEX"/>
     </intent-filter>
 </receiver>

 
```
The receiver needs to schedule the indexing work to happen asynchronously in the background. An example implementation is documented in the [developer guide](https://firebase.google.com/docs/app-indexing/android/personal-content#generate-and-refresh-the-index).  
Constant Value: "com.google.firebase.appindexing.UPDATE_INDEX"  

#### public static final [String](https://developer.android.com/reference/java/lang/String.html)
**APP_INDEXING_API_TAG**

The tag used for logging debug information for calls to [FirebaseAppIndex](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/FirebaseAppIndex)
class.

To enable logging:  

`adb shell setprop `*log.tag.FirebaseAppIndex*` `*DEBUG*  
Constant Value: "FirebaseAppIndex"  

#### public static final [String](https://developer.android.com/reference/java/lang/String.html)
**EXTRA_UPDATE_INDEX_REASON**

Used as an int extra field in [ACTION_UPDATE_INDEX](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/FirebaseAppIndex#ACTION_UPDATE_INDEX) intent to indicate the reason for the update request.
Possible values are [EXTRA_UPDATE_INDEX_REASON_REBUILD](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/FirebaseAppIndex#EXTRA_UPDATE_INDEX_REASON_REBUILD) and [EXTRA_UPDATE_INDEX_REASON_REFRESH](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/FirebaseAppIndex#EXTRA_UPDATE_INDEX_REASON_REFRESH).  
Constant Value: "com.google.firebase.appindexing.extra.REASON"  

#### public static final int
**EXTRA_UPDATE_INDEX_REASON_REBUILD**

An int value for [EXTRA_UPDATE_INDEX_REASON](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/FirebaseAppIndex#EXTRA_UPDATE_INDEX_REASON) when the update request is sent because the index
needs to be fully rebuilt. This could be for several reasons, including app
installation (the app is newly installed on the device) or index resets (for example
because of temporary storage constraints).  
Constant Value: 1  

#### public static final int
**EXTRA_UPDATE_INDEX_REASON_REFRESH**

An int value for [EXTRA_UPDATE_INDEX_REASON](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/FirebaseAppIndex#EXTRA_UPDATE_INDEX_REASON) when the update request is sent because some
content has not been re-indexed in some time (\>30 days), and needs to be re-indexed
to stay in the index.  
Constant Value: 2

## Public Constructors

#### public **FirebaseAppIndex** ()

## Public Methods

#### public static synchronized [FirebaseAppIndex](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/FirebaseAppIndex)
**getInstance** ([Context](https://developer.android.com/reference/android/content/Context.html) context)

Returns an instance of [FirebaseAppIndex](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/FirebaseAppIndex).

This method does not require FirebaseApp initialization. Instead, the application
context is inferred from the `context` that is explicitly passed in.  

#### public abstract Task\<[Void](https://developer.android.com/reference/java/lang/Void.html)\> **remove** ([String...](https://developer.android.com/reference/java/lang/String.html) urls)

Removes one or multiple [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable)s
from the index.  

##### Parameters

| urls | One or multiple URLs of the [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable)s to be removed from the index. The total number of URLs that can be passed in a single call is limited to [Indexable.MAX_INDEXABLES_TO_BE_UPDATED_IN_ONE_CALL](https://firebase.google.com/docs/reference/android). |
|------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

##### Returns

- A [Task](https://firebase.google.com/docs/reference/android/com/google/android/gms/tasks/Task) indicating the result of the operation  

#### public abstract Task\<[Void](https://developer.android.com/reference/java/lang/Void.html)\> **removeAll** ()

Removes all data from the index.  

##### Returns

- A [Task](https://firebase.google.com/docs/reference/android/com/google/android/gms/tasks/Task) indicating the result of the operation.  

#### public abstract Task\<[Void](https://developer.android.com/reference/java/lang/Void.html)\> **update** ([Indexable...](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable) indexables)

Inserts or updates one or multiple [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable)s
in the index. The [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable)s
are identified by their URL, and the update is a complete replacement (all previously
indexed information for a given [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable)
is replaced with the new one).  

##### Parameters

| indexables | One or multiple [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable)s to be inserted or updated in the index. The total number of [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable)s that can be passed in a single call is limited to [Indexable.MAX_INDEXABLES_TO_BE_UPDATED_IN_ONE_CALL](https://firebase.google.com/docs/reference/android)). |
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

##### Returns

- A [Task](https://firebase.google.com/docs/reference/android/com/google/android/gms/tasks/Task) indicating the result of the operation.