# Source: https://firebase.google.com/docs/reference/js/firestore_.persistentlocalcache.md.txt

# PersistentLocalCache interface

Provides a persistent cache backed by IndexedDb to the SDK.

To use, create an instance using the factory function , then set the instance to `FirestoreSettings.cache` and call `initializeFirestore` using the settings object.

**Signature:**  

    export declare interface PersistentLocalCache 

## Properties

|                                                     Property                                                      |     Type     | Description |
|-------------------------------------------------------------------------------------------------------------------|--------------|-------------|
| [kind](https://firebase.google.com/docs/reference/js/firestore_.persistentlocalcache.md#persistentlocalcachekind) | 'persistent' |             |

## PersistentLocalCache.kind

**Signature:**  

    kind: 'persistent';