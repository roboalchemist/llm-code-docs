# Source: https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-progress-t-.md.txt

# Firebase.Storage.StorageProgress Class Reference

# Firebase.Storage.StorageProgress\< T \>

A class that receives progress updates for storage uploads and downloads.

## Summary

### Inheritance

Inherits from: IProgress\< T \>

|                                                                                                                                                                               ### Public functions                                                                                                                                                                                ||
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| [Report](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-progress-t-#class_firebase_1_1_storage_1_1_storage_progress_3_01_t_01_4_1acbae86064a6bd682a6fbda1819aefd1e)`(T value)`                       | `virtual void` Called periodically during a long running operation, this method will pass value to the delegate passed in the constructor. |
| [StorageProgress](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-progress-t-#class_firebase_1_1_storage_1_1_storage_progress_3_01_t_01_4_1ade983506885d649b981855dd5b72ea1b)`(Action< T > callback)` | ` ` ` `Creates an instance of a StorageProgress class. ` `                                                                                 |

## Public functions

### Report

```c#
virtual void Report(
  T value
)
```  
Called periodically during a long running operation, this method will pass value to the delegate passed in the constructor.

<br />

|                                                              Details                                                              ||
|------------|-----------------------------------------------------------------------------------------------------------------------|
| Parameters | |---------|----------------------------------------------| | `value` | Current state of the long running operation. | |

### StorageProgress

```c#
 StorageProgress(
  Action< T > callback
)
```  
Creates an instance of a StorageProgress class.

<br />

|                                                                                                 Details                                                                                                 ||
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |------------|------------------------------------------------------------------------------| | `callback` | A delegate that will be called periodically during a long running operation. | |