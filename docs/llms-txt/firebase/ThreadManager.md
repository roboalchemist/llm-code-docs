# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/ThreadManager.md.txt

# ThreadManager

public abstract class **ThreadManager** extends Object  
An interface that controls the thread pools and thread factories used by the Admin SDK. Each
instance of [FirebaseApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp) uses an implementation of this interface to create and manage
threads.

Multiple app instances may use the same `ThreadManager` instance.
Methods in this interface may get invoked multiple times by the same
app, during its lifetime. Apps may also invoke methods of this interface concurrently and
so implementations should provide any synchronization necessary.  

### Public Constructor Summary

|---|--------------------------------------------------------------------------------------------------------------------------------------|
|   | [ThreadManager](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/ThreadManager#ThreadManager())() |

### Protected Method Summary

|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| abstract ExecutorService | [getExecutor](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/ThreadManager#getExecutor(com.google.firebase.FirebaseApp))([FirebaseApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp) app) Returns the main thread pool for an app.                                                                                  |
| abstract ThreadFactory   | [getThreadFactory](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/ThreadManager#getThreadFactory())() Returns the `ThreadFactory` to be used for creating long-lived threads.                                                                                                                                                                                          |
| abstract void            | [releaseExecutor](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/ThreadManager#releaseExecutor(com.google.firebase.FirebaseApp, java.util.concurrent.ExecutorService))([FirebaseApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp) app, ExecutorService executor) Cleans up the thread pool associated with an app. |

### Inherited Method Summary

From class java.lang.Object  

|------------------|---------------------------|
| Object           | clone()                   |
| boolean          | equals(Object arg0)       |
| void             | finalize()                |
| final Class\<?\> | getClass()                |
| int              | hashCode()                |
| final void       | notify()                  |
| final void       | notifyAll()               |
| String           | toString()                |
| final void       | wait(long arg0, int arg1) |
| final void       | wait(long arg0)           |
| final void       | wait()                    |

## Public Constructors

#### public
**ThreadManager**
()

<br />

## Protected Methods

#### protected abstract ExecutorService
**getExecutor**
([FirebaseApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp) app)

Returns the main thread pool for an app. Implementations may return the same instance of
`ExecutorService` for multiple apps. The returned thread pool is used for
short-lived tasks by all components of an app.

For long-lived tasks (such as the ones started by the Realtime Database client), the SDK
creates dedicated executors using the `ThreadFactory` returned by the
[getThreadFactory()](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/ThreadManager#getThreadFactory()) method.  

##### Parameters

| app | A [FirebaseApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp) instance. |
|-----|----------------------------------------------------------------------------------------------------------------------------|

##### Returns

- A non-null `ExecutorService` instance.  

#### protected abstract ThreadFactory
**getThreadFactory**
()

Returns the `ThreadFactory` to be used for creating long-lived threads. This is
used mainly to create the long-lived worker threads for the Realtime Database client, and
other scheduled (periodic) tasks started by the SDK. The SDK guarantees
clean termination of all threads started via this `ThreadFactory`, when the user
calls [delete()](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp#delete()).

If long-lived threads cannot be supported in the current runtime, this method may
throw a `RuntimeException`.  

##### Returns

- A non-null `ThreadFactory`.  

#### protected abstract void
**releaseExecutor**
([FirebaseApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp) app, ExecutorService executor)

Cleans up the thread pool associated with an app. This method is invoked when an app
is deleted. This is guaranteed to be called with the `ExecutorService` previously
returned by [getExecutor(FirebaseApp)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/ThreadManager#getExecutor(com.google.firebase.FirebaseApp)) for the corresponding app.  

##### Parameters

| app | A [FirebaseApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp) instance. |
|-----|----------------------------------------------------------------------------------------------------------------------------|