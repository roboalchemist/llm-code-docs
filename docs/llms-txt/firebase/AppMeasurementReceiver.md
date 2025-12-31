# Source: https://firebase.google.com/docs/reference/android/com/google/android/gms/measurement/AppMeasurementReceiver.md.txt

# AppMeasurementReceiver

public final class **AppMeasurementReceiver** extends WakefulBroadcastReceiver  
A [BroadcastReceiver](https://developer.android.com/reference/android/content/BroadcastReceiver.html)
for Firebase Analytics. Firebase Analytics requires this receiver to be correctly declared in
AndroidManifest.xml and enabled:  

    <manifest>
       <application>
         <!-- ... -->

         <receiver android:name="com.google.android.gms.measurement.AppMeasurementReceiver"
             android:enabled="true">
             <intent-filter>
                 <action android:name="com.google.android.gms.measurement.UPLOAD" />
                 <action android:name="com.android.vending.INSTALL_REFERRER"/>
             </intent-filter>
         </receiver>

         <!-- ... -->
       </application>
     </manifest>
     
### Public Constructor Summary

|---|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   | [AppMeasurementReceiver](https://firebase.google.com/docs/reference/android/com/google/android/gms/measurement/AppMeasurementReceiver#AppMeasurementReceiver())() |

### Public Method Summary

|---------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [BroadcastReceiver.PendingResult](https://developer.android.com/reference/android/content/BroadcastReceiver.PendingResult.html) | [doGoAsync](https://firebase.google.com/docs/reference/android/com/google/android/gms/measurement/AppMeasurementReceiver#doGoAsync())()                                                                                                                                                                                                                                          |
| void                                                                                                                            | [doStartService](https://firebase.google.com/docs/reference/android/com/google/android/gms/measurement/AppMeasurementReceiver#doStartService(android.content.Context,%20android.content.Intent))([Context](https://developer.android.com/reference/android/content/Context.html) context, [Intent](https://developer.android.com/reference/android/content/Intent.html) service) |
| void                                                                                                                            | [onReceive](https://firebase.google.com/docs/reference/android/com/google/android/gms/measurement/AppMeasurementReceiver#onReceive(android.content.Context,%20android.content.Intent))([Context](https://developer.android.com/reference/android/content/Context.html) context, [Intent](https://developer.android.com/reference/android/content/Intent.html) intent)            |

### Inherited Method Summary

From class androidx.legacy.content.WakefulBroadcastReceiver  

|----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| static boolean                                                                                     | completeWakefulIntent([Intent](https://developer.android.com/reference/android/content/Intent.html) arg0)                                                                                     |
| static [ComponentName](https://developer.android.com/reference/android/content/ComponentName.html) | startWakefulService([Context](https://developer.android.com/reference/android/content/Context.html) arg0, [Intent](https://developer.android.com/reference/android/content/Intent.html) arg1) |

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

#### public **AppMeasurementReceiver** ()

## Public Methods

#### public [BroadcastReceiver.PendingResult](https://developer.android.com/reference/android/content/BroadcastReceiver.PendingResult.html)
**doGoAsync** ()

#### public void **doStartService** ([Context](https://developer.android.com/reference/android/content/Context.html) context, [Intent](https://developer.android.com/reference/android/content/Intent.html) service)

#### public void **onReceive** ([Context](https://developer.android.com/reference/android/content/Context.html) context, [Intent](https://developer.android.com/reference/android/content/Intent.html) intent)