# Source: https://firebase.google.com/docs/reference/js/firestore_.memoryeagergarbagecollector.md.txt

# MemoryEagerGarbageCollector interface

A garbage collector deletes documents whenever they are not part of any active queries, and have no local mutations attached to them.

This collector tries to ensure lowest memory footprints from the SDK, at the risk of documents not being cached for offline queries or for direct queries to the cache.

Use factory function to create an instance of this collector.

**Signature:**  

    export declare interface MemoryEagerGarbageCollector 

## Properties

|                                                            Property                                                             |     Type      | Description |
|---------------------------------------------------------------------------------------------------------------------------------|---------------|-------------|
| [kind](https://firebase.google.com/docs/reference/js/firestore_.memoryeagergarbagecollector.md#memoryeagergarbagecollectorkind) | 'memoryEager' |             |

## MemoryEagerGarbageCollector.kind

**Signature:**  

    kind: 'memoryEager';