# Source: https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityFutureTask.md.txt

# PriorityFutureTask

public class **PriorityFutureTask** extends FutureTask\<V\>  
implements [Dependency](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Dependency)\<[Task](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Task)\> [PriorityProvider](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityProvider) [Task](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Task) [DelegateProvider](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/DelegateProvider)  
FutureTask that provides priority for [PriorityThreadPoolExecutor](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityThreadPoolExecutor)
Tries to cast runnable/callable to type that implements [Dependency](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Dependency),
[PriorityProvider](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityProvider), and [Task](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Task).
This classes uses [PriorityTask](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityTask) as default if
cast cannot happen.  

### Public Constructor Summary

|---|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   | [PriorityFutureTask](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityFutureTask#PriorityFutureTask(java.util.concurrent.Callable<V>))(Callable\<V\> callable) |
|   | [PriorityFutureTask](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityFutureTask#PriorityFutureTask(java.lang.Runnable, V))(Runnable runnable, V result)       |

### Public Method Summary

|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| void                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | [addDependency](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityFutureTask#addDependency(io.fabric.sdk.android.services.concurrency.Task))([Task](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Task) task)                                                   |
| boolean                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | [areDependenciesMet](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityFutureTask#areDependenciesMet())() Returns true when the dependencies have been met                                                                                                                                                             |
| int                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | [compareTo](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityFutureTask#compareTo(java.lang.Object))(Object another)                                                                                                                                                                                                  |
| \<T extends [Dependency](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Dependency)\<[Task](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Task)\> \& [PriorityProvider](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityProvider) \& [Task](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Task)\> T | [getDelegate](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityFutureTask#getDelegate())() Returns a delegate to be used when the parent class of the implementor can extend from a [PriorityTask](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityTask) |
| Collection\<[Task](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Task)\>                                                                                                                                                                                                                                                                                                                                                                                                      | [getDependencies](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityFutureTask#getDependencies())() fulfilled before the Dependency instance.                                                                                                                                                                          |
| Throwable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | [getError](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityFutureTask#getError())()                                                                                                                                                                                                                                  |
| [Priority](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Priority)                                                                                                                                                                                                                                                                                                                                                                                                            | [getPriority](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityFutureTask#getPriority())()                                                                                                                                                                                                                            |
| boolean                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | [isFinished](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityFutureTask#isFinished())()                                                                                                                                                                                                                              |
| void                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | [setError](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityFutureTask#setError(java.lang.Throwable))(Throwable throwable)                                                                                                                                                                                            |
| void                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | [setFinished](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityFutureTask#setFinished(boolean))(boolean finished) Marks Task as finished                                                                                                                                                                              |

### Protected Method Summary

|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| \<T extends [Dependency](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Dependency)\<[Task](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Task)\> \& [PriorityProvider](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityProvider) \& [Task](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Task)\> T | [checkAndInitDelegate](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityFutureTask#checkAndInitDelegate(java.lang.Object))(Object object) |

### Inherited Method Summary

From class java.util.concurrent.FutureTask  

|---------|-------------------------------|
| boolean | cancel(boolean arg0)          |
| void    | done()                        |
| V       | get(long arg0, TimeUnit arg1) |
| V       | get()                         |
| boolean | isCancelled()                 |
| boolean | isDone()                      |
| void    | run()                         |
| boolean | runAndReset()                 |
| void    | set(V arg0)                   |
| void    | setException(Throwable arg0)  |

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

From interface java.util.concurrent.RunnableFuture  

|---------------|-------|
| abstract void | run() |

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

From interface java.lang.Runnable  

|---------------|-------|
| abstract void | run() |

From interface java.util.concurrent.Future  

|------------------|-------------------------------|
| abstract boolean | cancel(boolean arg0)          |
| abstract V       | get(long arg0, TimeUnit arg1) |
| abstract V       | get()                         |
| abstract boolean | isCancelled()                 |
| abstract boolean | isDone()                      |

From interface java.lang.Comparable  

|--------------|-------------------|
| abstract int | compareTo(T arg0) |

## Public Constructors

#### public
**PriorityFutureTask**
(Callable\<V\> callable)

<br />

##### Parameters

|----------|---|
| callable |   |

#### public
**PriorityFutureTask**
(Runnable runnable, V result)

<br />

##### Parameters

|----------|---|
| runnable |   |
| result   |   |

## Public Methods

#### public void
**addDependency**
([Task](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Task) task)

<br />

##### Parameters

|------|---|
| task |   |

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

## Protected Methods

#### protected T
**checkAndInitDelegate**
(Object object)

<br />

##### Parameters

|--------|---|
| object |   |