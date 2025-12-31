# Source: https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityAsyncTask.md.txt

# PriorityAsyncTask

public abstract class **PriorityAsyncTask** extends [AsyncTask](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/AsyncTask)\<Params, Progress, Result\>  
implements [Dependency](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Dependency)\<[Task](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Task)\> [PriorityProvider](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityProvider) [Task](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Task) [DelegateProvider](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/DelegateProvider)  
AsyncTask that provides priority for [PriorityThreadPoolExecutor](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityThreadPoolExecutor)  

### Inherited Field Summary

From class [io.fabric.sdk.android.services.concurrency.AsyncTask](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/AsyncTask)  

|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| public static final Executor | [SERIAL_EXECUTOR](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/AsyncTask#SERIAL_EXECUTOR)           | An [Executor](https://firebase.google.com/docs/reference/androidreference/java/util/concurrent/Executor) that executes tasks one at a time in serial order. |
| public static final Executor | [THREAD_POOL_EXECUTOR](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/AsyncTask#THREAD_POOL_EXECUTOR) | An [Executor](https://firebase.google.com/docs/reference/androidreference/java/util/concurrent/Executor) that can be used to execute tasks in parallel.     |

### Public Constructor Summary

|---|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   | [PriorityAsyncTask](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityAsyncTask#PriorityAsyncTask())() |

### Public Method Summary

|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| void                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | [addDependency](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityAsyncTask#addDependency(io.fabric.sdk.android.services.concurrency.Task))([Task](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Task) task) Adds a [Dependency](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Dependency) |
| boolean                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | [areDependenciesMet](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityAsyncTask#areDependenciesMet())() Returns true when the dependencies have been met                                                                                                                                                                                                                                                |
| int                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | [compareTo](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityAsyncTask#compareTo(java.lang.Object))(Object another)                                                                                                                                                                                                                                                                                     |
| final void                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | [executeOnExecutor](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityAsyncTask#executeOnExecutor(java.util.concurrent.ExecutorService, Params...))(ExecutorService exec, Params... params)                                                                                                                                                                                                              |
| \<T extends [Dependency](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Dependency)\<[Task](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Task)\> \& [PriorityProvider](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityProvider) \& [Task](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Task)\> T | [getDelegate](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityAsyncTask#getDelegate())() Returns a delegate to be used when the parent class of the implementor can extend from a [PriorityTask](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityTask)                                                                                    |
| Collection\<[Task](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Task)\>                                                                                                                                                                                                                                                                                                                                                                                                      | [getDependencies](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityAsyncTask#getDependencies())() fulfilled before the Dependency instance.                                                                                                                                                                                                                                                             |
| Throwable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | [getError](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityAsyncTask#getError())()                                                                                                                                                                                                                                                                                                                     |
| [Priority](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Priority)                                                                                                                                                                                                                                                                                                                                                                                                            | [getPriority](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityAsyncTask#getPriority())()                                                                                                                                                                                                                                                                                                               |
| boolean                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | [isFinished](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityAsyncTask#isFinished())()                                                                                                                                                                                                                                                                                                                 |
| void                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | [setError](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityAsyncTask#setError(java.lang.Throwable))(Throwable throwable)                                                                                                                                                                                                                                                                               |
| void                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | [setFinished](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityAsyncTask#setFinished(boolean))(boolean finished) Marks Task as finished                                                                                                                                                                                                                                                                 |

### Inherited Method Summary

From class [io.fabric.sdk.android.services.concurrency.AsyncTask](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/AsyncTask)  

|---------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| final boolean                                                                                                                                                 | [cancel](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/AsyncTask#cancel(boolean))(boolean mayInterruptIfRunning) Attempts to cancel execution of this task.                                                                                                                                                                                                                                                                                                                               |
| abstract Result                                                                                                                                               | [doInBackground](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/AsyncTask#doInBackground(Params...))(Params... params) Override this method to perform a computation on a background thread.                                                                                                                                                                                                                                                                                               |
| final [AsyncTask](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/AsyncTask)\<Params, Progress, Result\> | [execute](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/AsyncTask#execute(Params...))(Params... params) Executes the task with the specified parameters.                                                                                                                                                                                                                                                                                                                                  |
| static void                                                                                                                                                   | [execute](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/AsyncTask#execute(java.lang.Runnable))(Runnable runnable) Convenience version of [execute(Object)](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/AsyncTask#execute(Params...)) for use with a simple Runnable object.                                                                                                                                                      |
| final [AsyncTask](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/AsyncTask)\<Params, Progress, Result\> | [executeOnExecutor](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/AsyncTask#executeOnExecutor(java.util.concurrent.Executor, Params...))(Executor exec, Params... params) Executes the task with the specified parameters.                                                                                                                                                                                                                                                                |
| final Result                                                                                                                                                  | [get](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/AsyncTask#get(long, java.util.concurrent.TimeUnit))(long timeout, TimeUnit unit) Waits if necessary for at most the given time for the computation to complete, and then retrieves its result.                                                                                                                                                                                                                                        |
| final Result                                                                                                                                                  | [get](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/AsyncTask#get())() Waits if necessary for the computation to complete, and then retrieves its result.                                                                                                                                                                                                                                                                                                                                 |
| final [AsyncTask.Status](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/AsyncTask.Status)               | [getStatus](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/AsyncTask#getStatus())() Returns the current status of this task.                                                                                                                                                                                                                                                                                                                                                               |
| final boolean                                                                                                                                                 | [isCancelled](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/AsyncTask#isCancelled())() Returns true if this task was cancelled before it completed normally.                                                                                                                                                                                                                                                                                                                              |
| void                                                                                                                                                          | [onCancelled](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/AsyncTask#onCancelled())() Applications should preferably override [onCancelled(Object)](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/AsyncTask#onCancelled(Result)).                                                                                                                                                                                                 |
| void                                                                                                                                                          | [onCancelled](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/AsyncTask#onCancelled(Result))(Result result) Runs on the UI thread after [cancel(boolean)](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/AsyncTask#cancel(boolean)) is invoked and [doInBackground(Object[])](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/AsyncTask#doInBackground(Params...)) has finished. |
| void                                                                                                                                                          | [onPostExecute](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/AsyncTask#onPostExecute(Result))(Result result) Runs on the UI thread after [doInBackground(Params...)](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/AsyncTask#doInBackground(Params...)).                                                                                                                                                                          |
| void                                                                                                                                                          | [onPreExecute](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/AsyncTask#onPreExecute())() Runs on the UI thread before [doInBackground(Params...)](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/AsyncTask#doInBackground(Params...)).                                                                                                                                                                                              |
| void                                                                                                                                                          | [onProgressUpdate](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/AsyncTask#onProgressUpdate(Progress...))(Progress... values) Runs on the UI thread after [publishProgress(Progress...)](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/AsyncTask#publishProgress(Progress...)) is invoked.                                                                                                                                         |
| final void                                                                                                                                                    | [publishProgress](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/AsyncTask#publishProgress(Progress...))(Progress... values) This method can be invoked from [doInBackground(Params...)](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/AsyncTask#doInBackground(Params...)) to publish updates on the UI thread while the background computation is still running.                                                                  |

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

From interface [io.fabric.sdk.android.services.concurrency.Dependency](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Dependency)  

|------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| abstract void                                                                                                                            | [addDependency](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Dependency#addDependency(T))([Task](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Task) dependable) Assign dependency on specified T. |
| abstract boolean                                                                                                                         | [areDependenciesMet](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Dependency#areDependenciesMet())() Returns true when the dependencies have been met                                                                                                     |
| abstract Collection\<[Task](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Task)\> | [getDependencies](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Dependency#getDependencies())() fulfilled before the Dependency instance.                                                                                                                  |

From interface [io.fabric.sdk.android.services.concurrency.PriorityProvider](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityProvider)  

|------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| abstract [Priority](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Priority) | [getPriority](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityProvider#getPriority())() |

From interface [io.fabric.sdk.android.services.concurrency.Task](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Task)  

|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| abstract Throwable | [getError](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Task#getError())()                                                     |
| abstract boolean   | [isFinished](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Task#isFinished())()                                                 |
| abstract void      | [setError](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Task#setError(java.lang.Throwable))(Throwable throwable)               |
| abstract void      | [setFinished](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Task#setFinished(boolean))(boolean finished) Marks Task as finished |

From interface [io.fabric.sdk.android.services.concurrency.DelegateProvider](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/DelegateProvider)  

|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| abstract \<T extends [Dependency](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Dependency)\<[Task](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Task)\> \& [PriorityProvider](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityProvider) \& [Task](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Task)\> T | [getDelegate](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/DelegateProvider#getDelegate())() Returns a delegate to be used when the parent class of the implementor can extend from a [PriorityTask](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityTask) |

From interface java.lang.Comparable  

|--------------|-------------------|
| abstract int | compareTo(T arg0) |

## Public Constructors

#### public
**PriorityAsyncTask**
()

<br />

## Public Methods

#### public void
**addDependency**
([Task](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Task) task)

Adds a [Dependency](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Dependency)  

##### Parameters

|------|---|
| task |   |

##### Throws

|-----------------------|---------------------------------------------|
| IllegalStateException | if @{link Fabric} has not been initialized. |

#### public boolean
**areDependenciesMet**
()

Returns true when the dependencies have been met  

#### public int
**compareTo**
(Object another)

<br />

##### Parameters

|---------|---|
| another |   |

#### public final void
**executeOnExecutor**
(ExecutorService exec, Params... params)

<br />

##### Parameters

|--------|---|
| exec   |   |
| params |   |

#### public T
**getDelegate**
()

Returns a delegate to be used when the parent class of the implementor can extend from a
[PriorityTask](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityTask)  

#### public Collection\<[Task](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Task)\>
**getDependencies**
()

fulfilled before the Dependency instance.  

##### Returns

- Collection of T to be fulfilled before the Dependency instance.  

#### public Throwable
**getError**
()

<br />

#### public [Priority](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Priority)
**getPriority**
()

<br />

#### public boolean
**isFinished**
()

<br />

#### public void
**setError**
(Throwable throwable)

<br />

##### Parameters

|-----------|---|
| throwable |   |

#### public void
**setFinished**
(boolean finished)

Marks Task as finished  

##### Parameters

|----------|---|
| finished |   |