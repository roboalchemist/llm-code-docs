# Source: https://firebase.google.com/docs/crashlytics/debug-anr-errors.md.txt

<br />

Application Not Responding (ANR) errors are triggered when the UI thread of the application is not responding for more than5 seconds. You can read more about ANRs and diagnosing ANRs in the[Android documentation](https://developer.android.com/topic/performance/vitals/anr).

Additionally, Crashlytics can help pinpoint specific problematic threads. We analyze ANRs, and then, in the[Crashlyticsdashboard](https://console.firebase.google.com/project/_/crashlytics), we tag applicable threads to provide hints on how to debug the ANR.

The following sections on this page explain what each ANR tag means, shows an example ANR with that tag, and provides a recommended solution to debug the ANR.

## `Triggered ANR`

A thread which was blocked for too long and triggered the ANR is annotated with this`Triggered ANR`tag.

The problematic thread can be the main thread for the app, or any thread found to be unresponsive. However, the thread tagged as`Triggered ANR`may or may not be the*actual* cause of the ANR. To provide insights for debugging and fixing these ANRs,Crashlyticsalso tags any other threads that are involved in the ANR. In the following sections of this page, learn about the other tags that could be applied to a thread.

## `Deadlocked`

Any threads which are found to be involved in a deadlock that led to the ANR are annotated with this`Deadlocked`tag.

A deadlock occurs when a thread enters a waiting state because a required resource is held by another thread, which is also waiting for a resource held by the first thread. If the app's main thread is in this situation, ANRs are likely to happen.  

#### View example

Here are two threads involved in a deadlock:  

```text
main (unknown): tid=1 systid=1568
    com.android.server.pm.PackageManagerService$PackageManagerInternalImpl.getPackage(PackageManagerService.java:22701)
    com.android.server.pm.PackageManagerService$PackageManagerInternalImpl.filterOnlySystemPackages(PackageManagerService.java:22787)

    ...

    com.android.server.SystemServer.main(SystemServer.java:368)
     java.lang.reflect.Method.invoke(Native method)
    com.android.internal.os.RuntimeInit$MethodAndArgsCaller.run(RuntimeInit.java:517)
    com.android.internal.os.ZygoteInit.main(ZygoteInit.java:934)


ActivityManager (unknown): tid=21 systid=1902
    com.android.server.pm.PackageManagerService.getPackageSetting(PackageManagerService.java:23618)
    com.android.server.pm.PackageManagerService.getPackageUid(PackageManagerService.java:4542)

    ...

    android.os.Handler.handleCallback(Handler.java:907)
    android.os.Handler.dispatchMessage(Handler.java:99)
    android.os.Looper.loop(Looper.java:216)
    android.os.HandlerThread.run(HandlerThread.java:67)
    com.android.server.ServiceThread.run(ServiceThread.java:44)
  
```

#### Recommendation

Look at threads involved in the deadlock and check the resources/locks acquired by those threads. Refer to[Deadlock](https://en.wikipedia.org/wiki/Deadlock)and[Deadlock prevention algorithms](https://en.wikipedia.org/wiki/Deadlock_prevention_algorithms)for possible solutions.

## `IO Root blocking`

Any thread that was executing slow I/O operations and blocked the`Triggered ANR`thread is annotated with the`IO Root blocking`tag. If the`Triggered ANR`thread isn't blocked by other threads, then the`IO Root blocking`thread is also a`Root blocking`thread.  

#### View examples

```scdoc
Thread main(THREAD_STATE_TIMED_WAITING)
   sun.misc.Unsafe.park( Unsafe.java:0 )
   java.util.concurrent.locks.LockSupport.parkNanos( LockSupport.java:230 )
   android.database.sqlite.SQLiteConnectionPool.waitForConnection( SQLiteConnectionPool.java:756 )

   ...

   android.app.ActivityThread.main( ActivityThread.java:8192 )
  
```  

```scdoc
Thread main(THREAD_STATE_NATIVE_WAITING)
   Syscall
   art::ConditionVariable::WaitHoldingLocks(art::Thread*)
   art::GoToRunnable(art::Thread*)
   art::JniMethodEnd(unsigned int, art::Thread*)
   libcore.io.Linux.fdatasync( Linux.java:0 )
   libcore.io.ForwardingOs.fdatasync( ForwardingOs.java:105 )

...

   java.io.RandomAccessFile.write( RandomAccessFile.java:559 )

...

   android.app.ActivityThread.main( ActivityThread.java:8192 )
  
```

#### Recommendation

In general, your app shouldn't execute expensive I/O operations on the main thread. In the case of the main thread being`IO Root blocking`, you can also use[Strict Mode](https://developer.android.com/reference/android/os/StrictMode)to identify any unintentional I/O operations that are happening on the main thread.

## `Root blocking`

Any thread that blocked the thread tagged as`Triggered ANR`is annotated with the`Root blocking`tag. If a thread is tagged as both`Root blocking`and`Triggered ANR`, then there are no other threads that block that thread.

If any`Triggered ANR`threads were waiting (maybe transitively) for other threads, they are`Root blocking`. There could be various reasons why a thread is a root cause of the ANR.  

#### View examples

Here are a few examples based on thread state:  

```scdoc
Thread main(THREAD_STATE_RUNNABLE)
   android.os.Parcel.createTypedArray( Parcel.java:3086 )
   android.content.pm.PackageInfo.<init>( PackageInfo.java:546 )

...

   android.app.ActivityThread$H.handleMessage( ActivityThread.java:2166 )
   android.os.Handler.dispatchMessage( Handler.java:106 )
   android.os.Looper.loop( Looper.java:246 )
   android.app.ActivityThread.main( ActivityThread.java:8633 )
  
```  

```scdoc
Thread main(THREAD_STATE_BLOCKED)
   DBHelper.runOnDB( DBHelper.java:97 )
   DBHelper.runDb( DBHelper.java:125 )

...

   java.lang.reflect.Method.invoke( Method.java:0 )
   EventBus.invokeSubscriber( EventBus.java:510 )
   postToSubscription( EventBus.java:437 )

...

   android.os.Handler.handleCallback( Handler.java:938 )
   android.os.Handler.dispatchMessage( Handler.java:99 )
   android.os.Looper.loop( Looper.java:268 )
   android.app.ActivityThread.main( ActivityThread.java:7904 )
  
```

#### Recommendation

Minimize CPU intensive work in the main thread. Use worker or background threads for performing CPU intensive tasks.

Minimize I/O intensive work, like loading from a database, on the main thread.

## `Unknown root cause`

A thread is tagged with the`Unknown root cause`tag if it was the thread that triggered the ANR but was idle in the process when the ANR occurred.Crashlyticsdoesn't have sufficient information to determine the root cause. There is no evident reason why this ANR has occurred.  

#### View example

```scdoc
Thread main(THREAD_STATE_NATIVE_WAITING)    __epoll_pwait
    android::Looper::pollInner(int)
    android::Looper::pollOnce(int, int*, int*, void**)
    android::android_os_MessageQueue_nativePollOnce(_JNIEnv*, _jobject*, long, int)
    android.os.MessageQueue.nativePollOnce( MessageQueue.java:0 )
    android.os.MessageQueue.next( MessageQueue.java:335 )
    android.os.Looper.loop( Looper.java:193 )
    android.app.ActivityThread.main( ActivityThread.java:8019 )
  
```

#### Recommendation

Follow the general advice on how to prevent ANRs. For example, identify the places in your code where the app's main thread can be busy for more than5 seconds.