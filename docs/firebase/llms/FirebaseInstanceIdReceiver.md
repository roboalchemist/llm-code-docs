# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/iid/FirebaseInstanceIdReceiver.md.txt

# FirebaseInstanceIdReceiver

public final class **FirebaseInstanceIdReceiver** extends CloudMessagingReceiver  
Implementation of `CloudMessagingReceiver` that passes Intents to the
`FirebaseMessagingService`.  

### Public Constructor Summary

|---|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   | [FirebaseInstanceIdReceiver](https://firebase.google.com/docs/reference/android/com/google/firebase/iid/FirebaseInstanceIdReceiver#FirebaseInstanceIdReceiver())() |

### Inherited Method Summary

From class com.google.android.gms.cloudmessaging.CloudMessagingReceiver  

|----------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Executor](https://developer.android.com/reference/java/util/concurrent/Executor.html) | getBroadcastExecutor()                                                                                                                                                                       |
| abstract int                                                                           | onMessageReceive([Context](https://developer.android.com/reference/android/content/Context.html) arg0, CloudMessage arg1)                                                                    |
| void                                                                                   | onNotificationDismissed([Context](https://developer.android.com/reference/android/content/Context.html) arg0, [Bundle](https://developer.android.com/reference/android/os/Bundle.html) arg1) |
| void                                                                                   | onNotificationOpen([Context](https://developer.android.com/reference/android/content/Context.html) arg0, [Bundle](https://developer.android.com/reference/android/os/Bundle.html) arg1)      |
| final void                                                                             | onReceive([Context](https://developer.android.com/reference/android/content/Context.html) arg0, [Intent](https://developer.android.com/reference/android/content/Intent.html) arg1)          |

From class android.content.BroadcastReceiver  

|---------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| final void                                                                                                                            | abortBroadcast()                                                                                                                                                                      |
| final void                                                                                                                            | clearAbortBroadcast()                                                                                                                                                                 |
| final boolean                                                                                                                         | getAbortBroadcast()                                                                                                                                                                   |
| final boolean                                                                                                                         | getDebugUnregister()                                                                                                                                                                  |
| final int                                                                                                                             | getResultCode()                                                                                                                                                                       |
| final [String](https://developer.android.com/reference/java/lang/String.html)                                                         | getResultData()                                                                                                                                                                       |
| final [Bundle](https://developer.android.com/reference/android/os/Bundle.html)                                                        | getResultExtras(boolean arg0)                                                                                                                                                         |
| final [UserHandle](https://developer.android.com/reference/android/os/UserHandle.html)                                                | getSendingUser()                                                                                                                                                                      |
| final [BroadcastReceiver.PendingResult](https://developer.android.com/reference/android/content/BroadcastReceiver.PendingResult.html) | goAsync()                                                                                                                                                                             |
| final boolean                                                                                                                         | isInitialStickyBroadcast()                                                                                                                                                            |
| final boolean                                                                                                                         | isOrderedBroadcast()                                                                                                                                                                  |
| abstract void                                                                                                                         | onReceive([Context](https://developer.android.com/reference/android/content/Context.html) arg0, [Intent](https://developer.android.com/reference/android/content/Intent.html) arg1)   |
| [IBinder](https://developer.android.com/reference/android/os/IBinder.html)                                                            | peekService([Context](https://developer.android.com/reference/android/content/Context.html) arg0, [Intent](https://developer.android.com/reference/android/content/Intent.html) arg1) |
| final void                                                                                                                            | setDebugUnregister(boolean arg0)                                                                                                                                                      |
| final void                                                                                                                            | setOrderedHint(boolean arg0)                                                                                                                                                          |
| final void                                                                                                                            | setResult(int arg0, [String](https://developer.android.com/reference/java/lang/String.html) arg1, [Bundle](https://developer.android.com/reference/android/os/Bundle.html) arg2)      |
| final void                                                                                                                            | setResultCode(int arg0)                                                                                                                                                               |
| final void                                                                                                                            | setResultData([String](https://developer.android.com/reference/java/lang/String.html) arg0)                                                                                           |
| final void                                                                                                                            | setResultExtras([Bundle](https://developer.android.com/reference/android/os/Bundle.html) arg0)                                                                                        |

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

#### public **FirebaseInstanceIdReceiver** ()