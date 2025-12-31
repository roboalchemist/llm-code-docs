# Source: https://firebase.google.com/docs/reference/js/storage.storageobserver.md.txt

# StorageObserver interface

A stream observer for Firebase Storage.

**Signature:**  

    export interface StorageObserver<T> 

## Properties

|                                                   Property                                                   |                                                                Type                                                                | Description |
|--------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|-------------|
| [complete](https://firebase.google.com/docs/reference/js/storage.storageobserver.md#storageobservercomplete) | [CompleteFn](https://firebase.google.com/docs/reference/js/util.md#completefn) \| null                                             |             |
| [error](https://firebase.google.com/docs/reference/js/storage.storageobserver.md#storageobservererror)       | (error: [StorageError](https://firebase.google.com/docs/reference/js/storage.storageerror.md#storageerror_class)) =\> void \| null |             |
| [next](https://firebase.google.com/docs/reference/js/storage.storageobserver.md#storageobservernext)         | [NextFn](https://firebase.google.com/docs/reference/js/util.md#nextfn)\<T\> \| null                                                |             |

## StorageObserver.complete

**Signature:**  

    complete?: CompleteFn | null;

## StorageObserver.error

**Signature:**  

    error?: (error: StorageError) => void | null;

## StorageObserver.next

**Signature:**  

    next?: NextFn<T> | null;