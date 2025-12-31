# Source: https://firebase.google.com/docs/reference/js/firestore_.memorylocalcache.md.txt

# MemoryLocalCache interface

Provides an in-memory cache to the SDK. This is the default cache unless explicitly configured otherwise.

To use, create an instance using the factory function , then set the instance to `FirestoreSettings.cache` and call `initializeFirestore` using the settings object.

**Signature:**  

    export declare interface MemoryLocalCache 

## Properties

|                                                 Property                                                  |   Type   | Description |
|-----------------------------------------------------------------------------------------------------------|----------|-------------|
| [kind](https://firebase.google.com/docs/reference/js/firestore_.memorylocalcache.md#memorylocalcachekind) | 'memory' |             |

## MemoryLocalCache.kind

**Signature:**  

    kind: 'memory';