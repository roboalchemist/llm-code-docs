# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/load-bundle-task-progress.md.txt

# firebase::firestore::LoadBundleTaskProgress Class Reference

# firebase::firestore::LoadBundleTaskProgress


`#include <load_bundle_task_progress.h>`

Represents a progress update or the final state from loading bundles.

## Summary

| ### Constructors and Destructors ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/load-bundle-task-progress#classfirebase_1_1firestore_1_1_load_bundle_task_progress_1af77ef737d4161af6057fe3dc75dea8fe()` ||
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/load-bundle-task-progress#classfirebase_1_1firestore_1_1_load_bundle_task_progress_1a8c7ff9781dd9490b14fa61fe2e3c3444(int32_t documents_loaded, int32_t total_documents, int64_t bytes_loaded, int64_t total_bytes, https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/load-bundle-task-progress#classfirebase_1_1firestore_1_1_load_bundle_task_progress_1a430b4e8cd45932452037b66885bd9d07 state)` Construct a [LoadBundleTaskProgress](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/load-bundle-task-progress#classfirebase_1_1firestore_1_1_load_bundle_task_progress) with specific state. ||

| ### Public types ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/load-bundle-task-progress#classfirebase_1_1firestore_1_1_load_bundle_task_progress_1a430b4e8cd45932452037b66885bd9d07` | enumRepresents the state of bundle loading tasks. |

| ### Public functions ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/load-bundle-task-progress#classfirebase_1_1firestore_1_1_load_bundle_task_progress_1adb5df37968d7776708d0c94c1dd8f6df() const ` | `int64_t` Returns how many bytes have been loaded. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/load-bundle-task-progress#classfirebase_1_1firestore_1_1_load_bundle_task_progress_1a64671d665b3a660b67bce09a765eb506() const ` | `int32_t` Returns how many documents have been loaded. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/load-bundle-task-progress#classfirebase_1_1firestore_1_1_load_bundle_task_progress_1aa3e4dae1ed7e69b9437d53ea84802a67() const ` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/load-bundle-task-progress#classfirebase_1_1firestore_1_1_load_bundle_task_progress_1a430b4e8cd45932452037b66885bd9d07` Returns the current state of the loading progress. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/load-bundle-task-progress#classfirebase_1_1firestore_1_1_load_bundle_task_progress_1aeebe37be4ae3d25419d662023798e80b() const ` | `int64_t` Returns the total number of bytes in the bundle. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/load-bundle-task-progress#classfirebase_1_1firestore_1_1_load_bundle_task_progress_1aa11aaa424493fede2bfcc6eeae4c3e79() const ` | `int32_t` Returns the total number of documents in the bundle. |

## Public types

### State

```c++
 State
```
Represents the state of bundle loading tasks.

Both `kSuccess` and `kError` are final states: the task will abort or complete and there will be no more updates after they are reported.

## Public functions

### LoadBundleTaskProgress

```c++
 LoadBundleTaskProgress()=default
```

### LoadBundleTaskProgress

```c++
 LoadBundleTaskProgress(
  int32_t documents_loaded,
  int32_t total_documents,
  int64_t bytes_loaded,
  int64_t total_bytes,
  State state
)
```
Construct a [LoadBundleTaskProgress](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/load-bundle-task-progress#classfirebase_1_1firestore_1_1_load_bundle_task_progress) with specific state.

### bytes_loaded

```c++
int64_t bytes_loaded() const 
```
Returns how many bytes have been loaded.

### documents_loaded

```c++
int32_t documents_loaded() const 
```
Returns how many documents have been loaded.

### state

```c++
State state() const 
```
Returns the current state of the loading progress.

### total_bytes

```c++
int64_t total_bytes() const 
```
Returns the total number of bytes in the bundle.

Returns 0 if the bundle failed to parse.

### total_documents

```c++
int32_t total_documents() const 
```
Returns the total number of documents in the bundle.

Returns 0 if the bundle failed to parse.