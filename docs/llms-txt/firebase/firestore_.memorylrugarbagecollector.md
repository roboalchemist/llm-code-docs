# Source: https://firebase.google.com/docs/reference/js/firestore_.memorylrugarbagecollector.md.txt

# MemoryLruGarbageCollector interface

A garbage collector deletes Least-Recently-Used documents in multiple batches.

This collector is configured with a target size, and will only perform collection when the cached documents exceed the target size. It avoids querying backend repeated for the same query or document, at the risk of having a larger memory footprint.

Use factory function to create a instance of this collector.

**Signature:**  

    export declare interface MemoryLruGarbageCollector 

## Properties

|                                                          Property                                                           |    Type     | Description |
|-----------------------------------------------------------------------------------------------------------------------------|-------------|-------------|
| [kind](https://firebase.google.com/docs/reference/js/firestore_.memorylrugarbagecollector.md#memorylrugarbagecollectorkind) | 'memoryLru' |             |

## MemoryLruGarbageCollector.kind

**Signature:**  

    kind: 'memoryLru';