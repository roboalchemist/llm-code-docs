# Source: https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Task.md.txt

# Task

public interface **Task**  

|---|---|---|
| Known Indirect Subclasses [PriorityAsyncTask](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityAsyncTask)\<Params, Progress, Result\>, [PriorityCallable](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityCallable)\<V\>, [PriorityFutureTask](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityFutureTask)\<V\>, [PriorityRunnable](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityRunnable), [PriorityTask](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityTask) |-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | [PriorityAsyncTask](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityAsyncTask)\<Params, Progress, Result\> | AsyncTask that provides priority for [PriorityThreadPoolExecutor](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityThreadPoolExecutor)                                                                                                                                                                                                                                                                                                                                                                                                                                                           | | [PriorityCallable](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityCallable)\<V\>                          | Callable that provides priority for [PriorityThreadPoolExecutor](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityThreadPoolExecutor)                                                                                                                                                                                                                                                                                                                                                                                                                                                            | | [PriorityFutureTask](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityFutureTask)\<V\>                      | FutureTask that provides priority for [PriorityThreadPoolExecutor](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityThreadPoolExecutor) Tries to cast runnable/callable to type that implements [Dependency](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Dependency), [PriorityProvider](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityProvider), and [Task](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Task). | | [PriorityRunnable](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityRunnable)                               | Runnable that provides priority for [PriorityThreadPoolExecutor](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityThreadPoolExecutor)                                                                                                                                                                                                                                                                                                                                                                                                                                                            | | [PriorityTask](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityTask)                                       | Base class for [Priority](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Priority) based worker Can also be used as delegate for non extensible existing classes, such as [AsyncTask](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/AsyncTask)                                                                                                                                                                                                                                                                                                  | |||

Represents a Task to be processed  

### Public Method Summary

|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| abstract Throwable | [getError](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Task#getError())()                                                     |
| abstract boolean   | [isFinished](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Task#isFinished())()                                                 |
| abstract void      | [setError](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Task#setError(java.lang.Throwable))(Throwable throwable)               |
| abstract void      | [setFinished](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Task#setFinished(boolean))(boolean finished) Marks Task as finished |

## Public Methods

#### public abstract Throwable
**getError**
()

<br />

##### Returns

- Error during completion of Task  

#### public abstract boolean
**isFinished**
()

<br />

##### Returns

- true if Task is finished  

#### public abstract void
**setError**
(Throwable throwable)

<br />

##### Parameters

|-----------|----------------------------|
| throwable | set during error condition |

#### public abstract void
**setFinished**
(boolean finished)

Marks Task as finished  

##### Parameters

|----------|---|
| finished |   |