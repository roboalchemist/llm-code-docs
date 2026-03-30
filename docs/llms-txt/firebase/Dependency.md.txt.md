# Source: https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Dependency.md.txt

# Dependency

public interface **Dependency**

|---|---|---|
| Known Indirect Subclasses [PriorityAsyncTask](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityAsyncTask)\<Params, Progress, Result\>, [PriorityCallable](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityCallable)\<V\>, [PriorityFutureTask](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityFutureTask)\<V\>, [PriorityRunnable](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityRunnable), [PriorityTask](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityTask) |---|---| | [PriorityAsyncTask](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityAsyncTask)\<Params, Progress, Result\> | AsyncTask that provides priority for `https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityThreadPoolExecutor` | | [PriorityCallable](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityCallable)\<V\> | Callable that provides priority for `https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityThreadPoolExecutor` | | [PriorityFutureTask](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityFutureTask)\<V\> | FutureTask that provides priority for `https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityThreadPoolExecutor` Tries to cast runnable/callable to type that implements `https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Dependency`, `https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityProvider`, and `https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Task`. | | [PriorityRunnable](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityRunnable) | Runnable that provides priority for `https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityThreadPoolExecutor` | | [PriorityTask](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityTask) | Base class for `https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Priority` based worker Can also be used as delegate for non extensible existing classes, such as `https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/AsyncTask` | |||

Represents dependency to be used with `https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityThreadPoolExecutor`

### Public Method Summary

|---|---|
| abstract void | [addDependency](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Dependency#addDependency(T))(T dependable) Assign dependency on specified T. |
| abstract boolean | [areDependenciesMet](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Dependency#areDependenciesMet())() Returns true when the dependencies have been met |
| abstract Collection\<T\> | [getDependencies](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Dependency#getDependencies())() fulfilled before the Dependency instance. |

## Public Methods

#### public abstract void
**addDependency**
(T dependable)

Assign dependency on specified T.

##### Parameters

|---|---|
| dependable |   |

#### public abstract boolean
**areDependenciesMet**
()

Returns true when the dependencies have been met

#### public abstract Collection\<T\>
**getDependencies**
()

fulfilled before the Dependency instance.

##### Returns

- Collection of T to be fulfilled before the Dependency instance.