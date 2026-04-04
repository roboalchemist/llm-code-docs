# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/load-bundle-task-progress.md.txt

# Source: https://firebase.google.com/docs/reference/unity/class/firebase/firestore/load-bundle-task-progress.md.txt

# Firebase.Firestore.LoadBundleTaskProgress Class Reference

# Firebase.Firestore.LoadBundleTaskProgress

## Summary

### Inheritance

Inherits from: EventArgs

| ### Constructors and Destructors ||
|---|---|
| [LoadBundleTaskProgress](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/load-bundle-task-progress#class_firebase_1_1_firestore_1_1_load_bundle_task_progress_1a3fc706bdecc0de6e207cabb59ced7ff0)`(int documentsLoaded, int totalDocuments, long bytesLoaded, long totalBytes, `[LoadBundleTaskState](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/load-bundle-task-progress#class_firebase_1_1_firestore_1_1_load_bundle_task_progress_1a3ced94039be5ccc15dcceee1740c2156)` state)` Creates a new instance of the class. ||

|                                                                                                                               ### Public types                                                                                                                               ||
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| [LoadBundleTaskState](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/load-bundle-task-progress#class_firebase_1_1_firestore_1_1_load_bundle_task_progress_1a3ced94039be5ccc15dcceee1740c2156) | enum Represents the state of bundle loading tasks. |

|                                                                                                                                                                                                                                         ### Properties                                                                                                                                                                                                                                         ||
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [BytesLoaded](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/load-bundle-task-progress#class_firebase_1_1_firestore_1_1_load_bundle_task_progress_1a8e1f2f240a52dadbf25787c534dacd35)` = 0`    | `long` The number of bytes that have been loaded.                                                                                                                                                                                                                   |
| [DocumentsLoaded](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/load-bundle-task-progress#class_firebase_1_1_firestore_1_1_load_bundle_task_progress_1ad14eb3e28964f8c5827fe77592bf8a26)      | `int` The number of documents that have been loaded.                                                                                                                                                                                                                |
| [State](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/load-bundle-task-progress#class_firebase_1_1_firestore_1_1_load_bundle_task_progress_1a043a7320f008eb0e46b12e37e0706453)` = 0`          | [LoadBundleTaskState](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/load-bundle-task-progress#class_firebase_1_1_firestore_1_1_load_bundle_task_progress_1a3ced94039be5ccc15dcceee1740c2156) The current state of the loading progress. |
| [TotalBytes](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/load-bundle-task-progress#class_firebase_1_1_firestore_1_1_load_bundle_task_progress_1ae6118310f9317af22d325ff0104b9070)` = 0`     | `long` The total number of bytes in the bundle.                                                                                                                                                                                                                     |
| [TotalDocuments](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/load-bundle-task-progress#class_firebase_1_1_firestore_1_1_load_bundle_task_progress_1a321e2f673b14d10dafb7d162dcaa9d4b)` = 0` | `int` The total number of documents in the bundle.                                                                                                                                                                                                                  |

|                                                                                                            ### Public functions                                                                                                            ||
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|
| [Equals](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/load-bundle-task-progress#class_firebase_1_1_firestore_1_1_load_bundle_task_progress_1addbbc08b580e201392e2f1a74d9ac262)`(Object obj)` | `override bool` |
| [GetHashCode](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/load-bundle-task-progress#class_firebase_1_1_firestore_1_1_load_bundle_task_progress_1a8777de63bdfd2c93455e2708d33e013d)`()`      | `override int`  |

## Public types

### LoadBundleTaskState

```c#
 LoadBundleTaskState
```  
Represents the state of bundle loading tasks.

Both LoadBundleTaskState.Success and LoadBundleTaskState.Error are final states: the task will fail or complete and there will be no more updates after they are reported.

## Properties

### BytesLoaded

```c#
long BytesLoaded = 0
```  
The number of bytes that have been loaded.  

### DocumentsLoaded

```c#
int DocumentsLoaded
```  
The number of documents that have been loaded.  

### State

```c#
LoadBundleTaskState State = 0
```  
The current state of the loading progress.  

### TotalBytes

```c#
long TotalBytes = 0
```  
The total number of bytes in the bundle.

Zero if the bundle failed to parse.  

### TotalDocuments

```c#
int TotalDocuments = 0
```  
The total number of documents in the bundle.

Zero if the bundle failed to parse.

## Public functions

### Equals

```c#
override bool Equals(
  Object obj
)
```  

### GetHashCode

```c#
override int GetHashCode()
```  

### LoadBundleTaskProgress

```c#
 LoadBundleTaskProgress(
  int documentsLoaded,
  int totalDocuments,
  long bytesLoaded,
  long totalBytes,
  LoadBundleTaskState state
)
```  
Creates a new instance of the class.

This is to support testing against progress updates.