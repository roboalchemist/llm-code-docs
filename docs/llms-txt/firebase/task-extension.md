# Source: https://firebase.google.com/docs/reference/unity/class/firebase/extensions/task-extension.md.txt

# Firebase.Extensions.TaskExtension Class Reference

# Firebase.Extensions.TaskExtension

Extension methods for System.Threading.Tasks.Task and System.Threading.Tasks.Task \< T \> that allow the continuation function to be executed on the main thread in Unity.

## Summary

This is compatible with both .NET 3.x and .NET 4.x.

To disable these extension methods entirely, uncheck all platform of /Assets/Firebase/Plugins/Firebase.TaskExtension.dll in Unity Editor.

|                                                                                                                                                               ### Public static functions                                                                                                                                                               ||
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|
| [ContinueWithOnMainThread](https://firebase.google.com/docs/reference/unity/class/firebase/extensions/task-extension#class_firebase_1_1_extensions_1_1_task_extension_1af1fc309e7e9b9e9a3655b8b47cb06014)`(this Task task, Action< Task > continuation)`                                                        | `Task` Extend Task.                    |
| [ContinueWithOnMainThread](https://firebase.google.com/docs/reference/unity/class/firebase/extensions/task-extension#class_firebase_1_1_extensions_1_1_task_extension_1aa561510941186ef7007646d1e3294fe0)`(this Task task, Action< Task > continuation, CancellationToken cancellationToken)`                   | `Task` Extend Task.                    |
| [ContinueWithOnMainThread< T >](https://firebase.google.com/docs/reference/unity/class/firebase/extensions/task-extension#class_firebase_1_1_extensions_1_1_task_extension_1a425456f6a0dc25d5a971ad59a82d9431)`(this Task< T > task, Action< Task< T >> continuation)`                                          | `Task` Extend Task \< T \>.            |
| [ContinueWithOnMainThread< TResult >](https://firebase.google.com/docs/reference/unity/class/firebase/extensions/task-extension#class_firebase_1_1_extensions_1_1_task_extension_1acde71a18613164f10de767e328b4f00c)`(this Task task, Func< Task, TResult > continuation)`                                      | `Task< TResult >` Extend Task.         |
| [ContinueWithOnMainThread< TResult >](https://firebase.google.com/docs/reference/unity/class/firebase/extensions/task-extension#class_firebase_1_1_extensions_1_1_task_extension_1a8fec69edcfa8c615141659cdaae3bf28)`(this Task task, Func< Task, TResult > continuation, CancellationToken cancellationToken)` | `Task< TResult >` Extend Task.         |
| [ContinueWithOnMainThread< TResult, T >](https://firebase.google.com/docs/reference/unity/class/firebase/extensions/task-extension#class_firebase_1_1_extensions_1_1_task_extension_1acd982e499b332981d0fc084376e2be57)`(this Task< T > task, Func< Task< T >, TResult > continuation)`                         | `Task< TResult >` Extend Task \< T \>. |

## Public static functions

### ContinueWithOnMainThread

```c#
Task ContinueWithOnMainThread(
  this Task task,
  Action< Task > continuation
)
```  
Extend Task.

Returns a Task which completes once the given task is complete and the given continuation function is called from the main thread in Unity.

<br />

|                                                                                                                                                                           Details                                                                                                                                                                            ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |----------------|--------------------------------------------------------------------------------------------| | `task`         | The task to continue with.                                                                 | | `continuation` | The continuation function to be executed on the main thread once the given task completes. | |
| **Returns** | A new Task that is complete after the continuation is executed on the main thread.                                                                                                                                                                                                                                                              |

### ContinueWithOnMainThread

```c#
Task ContinueWithOnMainThread(
  this Task task,
  Action< Task > continuation,
  CancellationToken cancellationToken
)
```  
Extend Task.

Returns a Task which completes once the given task is complete and the given continuation function is called from the main thread in Unity, with a cancellation token.

<br />

|                                                                                                                                                                                                                                             Details                                                                                                                                                                                                                                              ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------------------|--------------------------------------------------------------------------------------------| | `task`              | The task to continue with.                                                                 | | `continuation`      | The continuation function to be executed on the main thread once the given task completes. | | `cancellationToken` | The cancellation token.                                                                    | |
| **Returns** | A new Task that is complete after the continuation is executed on the main thread.                                                                                                                                                                                                                                                                                                                                                                                                  |

### ContinueWithOnMainThread\< T \>

```c#
Task ContinueWithOnMainThread< T >(
  this Task< T > task,
  Action< Task< T >> continuation
)
```  
Extend Task \< T \>.

Returns a Task which completes once the given task is complete and the given continuation function is called from the main thread in Unity.

<br />

|                                                                                                                                                                               Details                                                                                                                                                                                ||
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Template Parameters | |-----|-------------------------------------------------------------------------| | `T` | The Task template type used as an input parameter for the continuation. |                                                                                                                                                                             |
| Parameters          | |----------------|--------------------------------------------------------------------------------------------| | `task`         | The task to continue with.                                                                 | | `continuation` | The continuation function to be executed on the main thread once the given task completes. | |
| **Returns**         | A new Task that is complete after the continuation is executed on the main thread.                                                                                                                                                                                                                                                              |

### ContinueWithOnMainThread\< TResult \>

```c#
Task< TResult > ContinueWithOnMainThread< TResult >(
  this Task task,
  Func< Task, TResult > continuation
)
```  
Extend Task.

Returns a Task \< TResult \> which completes once the given task is complete and the given continuation function with return value TResult is called from the main thread in Unity.

<br />

|                                                                                                                                                                               Details                                                                                                                                                                                ||
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Template Parameters | |-----------|----------------------------------------| | `TResult` | The type returned by the continuation. |                                                                                                                                                                                                                                   |
| Parameters          | |----------------|--------------------------------------------------------------------------------------------| | `task`         | The task to continue with.                                                                 | | `continuation` | The continuation function to be executed on the main thread once the given task completes. | |
| **Returns**         | A new Task of type TResult, that is complete after the continuation is executed on the main thread.                                                                                                                                                                                                                                             |

### ContinueWithOnMainThread\< TResult \>

```c#
Task< TResult > ContinueWithOnMainThread< TResult >(
  this Task task,
  Func< Task, TResult > continuation,
  CancellationToken cancellationToken
)
```  
Extend Task.

Returns a Task \< TResult \> which completes once the given task is complete and the given continuation function with return value TResult is called from the main thread in Unity, with a cancellation token.

<br />

|                                                                                                                                                                                                                                                 Details                                                                                                                                                                                                                                                  ||
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Template Parameters | |-----------|----------------------------------------| | `TResult` | The type returned by the continuation. |                                                                                                                                                                                                                                                                                                                                                                       |
| Parameters          | |---------------------|--------------------------------------------------------------------------------------------| | `task`              | The task to continue with.                                                                 | | `continuation`      | The continuation function to be executed on the main thread once the given task completes. | | `cancellationToken` | The cancellation token.                                                                    | |
| **Returns**         | A new Task of type TResult, that is complete after the continuation is executed on the main thread.                                                                                                                                                                                                                                                                                                                                                                                 |

### ContinueWithOnMainThread\< TResult, T \>

```c#
Task< TResult > ContinueWithOnMainThread< TResult, T >(
  this Task< T > task,
  Func< Task< T >, TResult > continuation
)
```  
Extend Task \< T \>.

Returns a Task \< TResult \> which completes once the given task is complete and the given continuation function with return value TResult is called from the main thread in Unity.

<br />

|                                                                                                                                                                                                 Details                                                                                                                                                                                                  ||
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Template Parameters | |-----------|-------------------------------------------------------------------------------------------------------------| | `TResult` | The return type from continuation and the Task template return type of this extension method. continuation. | | `T`       | The Task template type used as an input parameter for the continuation.                                     | |
| Parameters          | |----------------|--------------------------------------------------------------------------------------------| | `task`         | The task to continue with.                                                                 | | `continuation` | The continuation function to be executed on the main thread once the given task completes. |                                     |
| **Returns**         | A new Task of type TResult, that is complete after the continuation is executed on the main thread.                                                                                                                                                                                                                                                                                 |