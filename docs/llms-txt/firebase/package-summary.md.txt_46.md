# Source: https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/package-summary.md.txt

# io.fabric.sdk.android.services.concurrency

### Annotations

|---|---|
| [DependsOn](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/DependsOn) | Allows a `https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Kit` to specify a `https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Dependency` for initialization. |

### Interfaces

|---|---|
| [DelegateProvider](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/DelegateProvider) | Allows the implementer to provide a delegate to proxy concurrency methods |
| [Dependency](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Dependency)\<T\> | Represents dependency to be used with `https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityThreadPoolExecutor` |
| [PriorityProvider](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityProvider)\<T\> |   |
| [Task](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Task) | Represents a Task to be processed |

### Classes

|---|---|
| [AsyncTask](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/AsyncTask)\<Params, Progress, Result\> | AsyncTask enables proper and easy use of the UI thread. |
| [DependencyPriorityBlockingQueue](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/DependencyPriorityBlockingQueue)\<E extends [Dependency](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Dependency) \& [Task](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Task) \& [PriorityProvider](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityProvider)\> | The DependencyPriorityBlockingQueue provides all functionality of a `https://firebase.google.com/docs/reference/androidreference/java/util/concurrent/PriorityBlockingQueue` while simultaneously supporting task dependencies using the `https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Dependency` interface. |
| [PriorityAsyncTask](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityAsyncTask)\<Params, Progress, Result\> | AsyncTask that provides priority for `https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityThreadPoolExecutor` |
| [PriorityCallable](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityCallable)\<V\> | Callable that provides priority for `https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityThreadPoolExecutor` |
| [PriorityFutureTask](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityFutureTask)\<V\> | FutureTask that provides priority for `https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityThreadPoolExecutor` Tries to cast runnable/callable to type that implements `https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Dependency`, `https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityProvider`, and `https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Task`. |
| [PriorityRunnable](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityRunnable) | Runnable that provides priority for `https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityThreadPoolExecutor` |
| [PriorityTask](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityTask) | Base class for `https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Priority` based worker Can also be used as delegate for non extensible existing classes, such as `https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/AsyncTask` |
| [PriorityThreadPoolExecutor](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityThreadPoolExecutor) | ThreadPoolExecutor that implements a `https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/DependencyPriorityBlockingQueue`. |
| [PriorityThreadPoolExecutor.PriorityThreadFactory](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityThreadPoolExecutor.PriorityThreadFactory) |   |

### Enums

|---|---|
| [AsyncTask.Status](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/AsyncTask.Status) | Indicates the current status of the task. |
| [Priority](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Priority) | enum to define ordering for PriorityBlockingQueue in `https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityThreadPoolExecutor` |

### Exceptions

|---|---|
| [UnmetDependencyException](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/UnmetDependencyException) | Used when a dependency is required but not met. |