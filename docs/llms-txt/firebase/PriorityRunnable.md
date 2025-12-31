# Source: https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityRunnable.md.txt

# PriorityRunnable

public abstract class **PriorityRunnable** extends [PriorityTask](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityTask)  
implements Runnable  
Runnable that provides priority for [PriorityThreadPoolExecutor](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityThreadPoolExecutor)  

### Public Constructor Summary

|---|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   | [PriorityRunnable](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityRunnable#PriorityRunnable())() |

### Inherited Method Summary

From class [io.fabric.sdk.android.services.concurrency.PriorityTask](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityTask)  

|----------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| synchronized void                                                                                                                            | [addDependency](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityTask#addDependency(io.fabric.sdk.android.services.concurrency.Task))([Task](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Task) task) |
| boolean                                                                                                                                      | [areDependenciesMet](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityTask#areDependenciesMet())() Returns true when the dependencies have been met                                                                                                           |
| int                                                                                                                                          | [compareTo](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityTask#compareTo(java.lang.Object))(Object other)                                                                                                                                                  |
| synchronized Collection\<[Task](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Task)\> | [getDependencies](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityTask#getDependencies())() fulfilled before the Dependency instance.                                                                                                                        |
| Throwable                                                                                                                                    | [getError](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityTask#getError())()                                                                                                                                                                                |
| [Priority](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Priority)                    | [getPriority](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityTask#getPriority())()                                                                                                                                                                          |
| boolean                                                                                                                                      | [isFinished](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityTask#isFinished())()                                                                                                                                                                            |
| static boolean                                                                                                                               | [isProperDelegate](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityTask#isProperDelegate(java.lang.Object))(Object object)                                                                                                                                   |
| void                                                                                                                                         | [setError](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityTask#setError(java.lang.Throwable))(Throwable throwable)                                                                                                                                          |
| synchronized void                                                                                                                            | [setFinished](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityTask#setFinished(boolean))(boolean finished) Marks Task as finished                                                                                                                            |

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

From interface java.lang.Runnable  

|---------------|-------|
| abstract void | run() |

From interface java.lang.Comparable  

|--------------|-------------------|
| abstract int | compareTo(T arg0) |

## Public Constructors

#### public
**PriorityRunnable**
()

<br />