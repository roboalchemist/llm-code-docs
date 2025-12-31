# Source: https://firebase.google.com/docs/reference/js/firestore_.loadbundletaskprogress.md.txt

# LoadBundleTaskProgress interface

Represents a progress update or a final state from loading bundles.

**Signature:**  

    export declare interface LoadBundleTaskProgress 

## Properties

|                                                                  Property                                                                   |                                        Type                                        |                    Description                     |
|---------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|----------------------------------------------------|
| [bytesLoaded](https://firebase.google.com/docs/reference/js/firestore_.loadbundletaskprogress.md#loadbundletaskprogressbytesloaded)         | number                                                                             | How many bytes have been loaded.                   |
| [documentsLoaded](https://firebase.google.com/docs/reference/js/firestore_.loadbundletaskprogress.md#loadbundletaskprogressdocumentsloaded) | number                                                                             | How many documents have been loaded.               |
| [taskState](https://firebase.google.com/docs/reference/js/firestore_.loadbundletaskprogress.md#loadbundletaskprogresstaskstate)             | [TaskState](https://firebase.google.com/docs/reference/js/firestore_.md#taskstate) | Current task state.                                |
| [totalBytes](https://firebase.google.com/docs/reference/js/firestore_.loadbundletaskprogress.md#loadbundletaskprogresstotalbytes)           | number                                                                             | How many bytes are in the bundle being loaded.     |
| [totalDocuments](https://firebase.google.com/docs/reference/js/firestore_.loadbundletaskprogress.md#loadbundletaskprogresstotaldocuments)   | number                                                                             | How many documents are in the bundle being loaded. |

## LoadBundleTaskProgress.bytesLoaded

How many bytes have been loaded.

**Signature:**  

    bytesLoaded: number;

## LoadBundleTaskProgress.documentsLoaded

How many documents have been loaded.

**Signature:**  

    documentsLoaded: number;

## LoadBundleTaskProgress.taskState

Current task state.

**Signature:**  

    taskState: TaskState;

## LoadBundleTaskProgress.totalBytes

How many bytes are in the bundle being loaded.

**Signature:**  

    totalBytes: number;

## LoadBundleTaskProgress.totalDocuments

How many documents are in the bundle being loaded.

**Signature:**  

    totalDocuments: number;