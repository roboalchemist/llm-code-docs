# Source: https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityThreadPoolExecutor.md.txt

# PriorityThreadPoolExecutor

public class **PriorityThreadPoolExecutor** extends ThreadPoolExecutor  
ThreadPoolExecutor that implements a [DependencyPriorityBlockingQueue](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/DependencyPriorityBlockingQueue).
This supports both [Dependency](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Dependency) and
[Priority](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Priority) functionality.  

### Nested Class Summary

|-------|---|---|---|
| class | [PriorityThreadPoolExecutor.PriorityThreadFactory](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityThreadPoolExecutor.PriorityThreadFactory) ||   |

### Public Method Summary

|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| static \<T extends Runnable \& [Dependency](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Dependency) \& [Task](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Task) \& [PriorityProvider](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityProvider)\> [PriorityThreadPoolExecutor](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityThreadPoolExecutor) | [create](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityThreadPoolExecutor#create(int, int))(int corePoolSize, int maxPoolSize)                                                                                                                                                                                                                                                                                  |
| static [PriorityThreadPoolExecutor](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityThreadPoolExecutor)                                                                                                                                                                                                                                                                                                                                                                                                                           | [create](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityThreadPoolExecutor#create())() Creates default [PriorityThreadPoolExecutor](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityThreadPoolExecutor) backed by a [PriorityBlockingQueue](https://firebase.google.com/docs/reference/androidreference/java/util/concurrent/PriorityBlockingQueue) |
| static [PriorityThreadPoolExecutor](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityThreadPoolExecutor)                                                                                                                                                                                                                                                                                                                                                                                                                           | [create](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityThreadPoolExecutor#create(int))(int threadCount)                                                                                                                                                                                                                                                                                                         |
| void                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | [execute](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityThreadPoolExecutor#execute(java.lang.Runnable))(Runnable command)                                                                                                                                                                                                                                                                                       |
| [DependencyPriorityBlockingQueue](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/DependencyPriorityBlockingQueue)                                                                                                                                                                                                                                                                                                                                                                                                                        | [getQueue](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityThreadPoolExecutor#getQueue())()                                                                                                                                                                                                                                                                                                                       |

### Protected Method Summary

|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| void                      | [afterExecute](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityThreadPoolExecutor#afterExecute(java.lang.Runnable, java.lang.Throwable))(Runnable runnable, Throwable throwable) |
| \<T\> RunnableFuture\<T\> | [newTaskFor](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityThreadPoolExecutor#newTaskFor(java.lang.Runnable, T))(Runnable runnable, T value)                                   |
| \<T\> RunnableFuture\<T\> | [newTaskFor](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityThreadPoolExecutor#newTaskFor(java.util.concurrent.Callable<T>))(Callable\<T\> callable)                            |

### Inherited Method Summary

From class java.util.concurrent.ThreadPoolExecutor  

|---------------------------|------------------------------------------------------------|
| void                      | afterExecute(Runnable arg0, Throwable arg1)                |
| void                      | allowCoreThreadTimeOut(boolean arg0)                       |
| boolean                   | allowsCoreThreadTimeOut()                                  |
| boolean                   | awaitTermination(long arg0, TimeUnit arg1)                 |
| void                      | beforeExecute(Thread arg0, Runnable arg1)                  |
| void                      | execute(Runnable arg0)                                     |
| void                      | finalize()                                                 |
| int                       | getActiveCount()                                           |
| long                      | getCompletedTaskCount()                                    |
| int                       | getCorePoolSize()                                          |
| long                      | getKeepAliveTime(TimeUnit arg0)                            |
| int                       | getLargestPoolSize()                                       |
| int                       | getMaximumPoolSize()                                       |
| int                       | getPoolSize()                                              |
| BlockingQueue\<Runnable\> | getQueue()                                                 |
| RejectedExecutionHandler  | getRejectedExecutionHandler()                              |
| long                      | getTaskCount()                                             |
| ThreadFactory             | getThreadFactory()                                         |
| boolean                   | isShutdown()                                               |
| boolean                   | isTerminated()                                             |
| boolean                   | isTerminating()                                            |
| int                       | prestartAllCoreThreads()                                   |
| boolean                   | prestartCoreThread()                                       |
| void                      | purge()                                                    |
| boolean                   | remove(Runnable arg0)                                      |
| void                      | setCorePoolSize(int arg0)                                  |
| void                      | setKeepAliveTime(long arg0, TimeUnit arg1)                 |
| void                      | setMaximumPoolSize(int arg0)                               |
| void                      | setRejectedExecutionHandler(RejectedExecutionHandler arg0) |
| void                      | setThreadFactory(ThreadFactory arg0)                       |
| void                      | shutdown()                                                 |
| List\<Runnable\>          | shutdownNow()                                              |
| void                      | terminated()                                               |
| String                    | toString()                                                 |

From class java.util.concurrent.AbstractExecutorService  

|---------------------------|---------------------------------------------------------------------------------|
| \<T\> List\<Future\<T\>\> | invokeAll(Collection\<? extends Callable\<T\>\> arg0)                           |
| \<T\> List\<Future\<T\>\> | invokeAll(Collection\<? extends Callable\<T\>\> arg0, long arg1, TimeUnit arg2) |
| \<T\> T                   | invokeAny(Collection\<? extends Callable\<T\>\> arg0)                           |
| \<T\> T                   | invokeAny(Collection\<? extends Callable\<T\>\> arg0, long arg1, TimeUnit arg2) |
| \<T\> RunnableFuture\<T\> | newTaskFor(Runnable arg0, T arg1)                                               |
| \<T\> RunnableFuture\<T\> | newTaskFor(Callable\<T\> arg0)                                                  |
| \<T\> Future\<T\>         | submit(Callable\<T\> arg0)                                                      |
| \<T\> Future\<T\>         | submit(Runnable arg0, T arg1)                                                   |
| Future\<?\>               | submit(Runnable arg0)                                                           |

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

From interface java.util.concurrent.ExecutorService  

|------------------------------------|---------------------------------------------------------------------------------|
| abstract boolean                   | awaitTermination(long arg0, TimeUnit arg1)                                      |
| abstract \<T\> List\<Future\<T\>\> | invokeAll(Collection\<? extends Callable\<T\>\> arg0)                           |
| abstract \<T\> List\<Future\<T\>\> | invokeAll(Collection\<? extends Callable\<T\>\> arg0, long arg1, TimeUnit arg2) |
| abstract \<T\> T                   | invokeAny(Collection\<? extends Callable\<T\>\> arg0)                           |
| abstract \<T\> T                   | invokeAny(Collection\<? extends Callable\<T\>\> arg0, long arg1, TimeUnit arg2) |
| abstract boolean                   | isShutdown()                                                                    |
| abstract boolean                   | isTerminated()                                                                  |
| abstract void                      | shutdown()                                                                      |
| abstract List\<Runnable\>          | shutdownNow()                                                                   |
| abstract \<T\> Future\<T\>         | submit(Callable\<T\> arg0)                                                      |
| abstract \<T\> Future\<T\>         | submit(Runnable arg0, T arg1)                                                   |
| abstract Future\<?\>               | submit(Runnable arg0)                                                           |

From interface java.util.concurrent.Executor  

|---------------|------------------------|
| abstract void | execute(Runnable arg0) |

## Public Methods

#### public static [PriorityThreadPoolExecutor](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityThreadPoolExecutor)
**create**
(int corePoolSize, int maxPoolSize)

<br />

##### Parameters

|--------------|-------------------------------------------------|
| corePoolSize | Number of threads to specify for core pool size |
| maxPoolSize  | Number of threads to specify for max pool size  |

##### Returns

- [PriorityThreadPoolExecutor](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityThreadPoolExecutor) backed by a [PriorityBlockingQueue](https://firebase.google.com/docs/reference/androidreference/java/util/concurrent/PriorityBlockingQueue)  

#### public static [PriorityThreadPoolExecutor](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityThreadPoolExecutor)
**create**
()

Creates default [PriorityThreadPoolExecutor](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityThreadPoolExecutor) backed by a
[PriorityBlockingQueue](https://firebase.google.com/docs/reference/androidreference/java/util/concurrent/PriorityBlockingQueue)  

#### public static [PriorityThreadPoolExecutor](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityThreadPoolExecutor)
**create**
(int threadCount)

<br />

##### Parameters

|-------------|----------------------------------------------|
| threadCount | Number of threads to specify for Thread Pool |

##### Returns

- [PriorityThreadPoolExecutor](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityThreadPoolExecutor) backed by a [PriorityBlockingQueue](https://firebase.google.com/docs/reference/androidreference/java/util/concurrent/PriorityBlockingQueue)  

#### public void
**execute**
(Runnable command)

<br />

##### Parameters

|---------|---|
| command |   |

#### public [DependencyPriorityBlockingQueue](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/DependencyPriorityBlockingQueue)
**getQueue**
()

<br />

## Protected Methods

#### protected void
**afterExecute**
(Runnable runnable, Throwable throwable)

<br />

##### Parameters

|-----------|---|
| runnable  |   |
| throwable |   |

#### protected RunnableFuture\<T\>
**newTaskFor**
(Runnable runnable, T value)

<br />

##### Parameters

|----------|---|
| runnable |   |
| value    |   |

#### protected RunnableFuture\<T\>
**newTaskFor**
(Callable\<T\> callable)

<br />

##### Parameters

|----------|---|
| callable |   |