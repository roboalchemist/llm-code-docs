# Source: https://firebase.google.com/docs/reference/js/firestore_.persistentcachesettings.md.txt

# PersistentCacheSettings interface

An settings object to configure an `PersistentLocalCache` instance.

Persistent cache cannot be used in a Node.js environment.

**Signature:**  

    export declare interface PersistentCacheSettings 

## Properties

|                                                                  Property                                                                   |                                                   Type                                                   |                                                                                                                                                                                                                           Description                                                                                                                                                                                                                           |
|---------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [cacheSizeBytes](https://firebase.google.com/docs/reference/js/firestore_.persistentcachesettings.md#persistentcachesettingscachesizebytes) | number                                                                                                   | An approximate cache size threshold for the on-disk data. If the cache grows beyond this size, Firestore will start removing data that hasn't been recently used. The SDK does not guarantee that the cache will stay below that size, only that if the cache exceeds the given size, cleanup will be attempted.The default value is 40 MB. The threshold must be set to at least 1 MB, and can be set to `CACHE_SIZE_UNLIMITED` to disable garbage collection. |
| [tabManager](https://firebase.google.com/docs/reference/js/firestore_.persistentcachesettings.md#persistentcachesettingstabmanager)         | [PersistentTabManager](https://firebase.google.com/docs/reference/js/firestore_.md#persistenttabmanager) | Specifies how multiple tabs/windows will be managed by the SDK.                                                                                                                                                                                                                                                                                                                                                                                                 |

## PersistentCacheSettings.cacheSizeBytes

An approximate cache size threshold for the on-disk data. If the cache grows beyond this size, Firestore will start removing data that hasn't been recently used. The SDK does not guarantee that the cache will stay below that size, only that if the cache exceeds the given size, cleanup will be attempted.

The default value is 40 MB. The threshold must be set to at least 1 MB, and can be set to `CACHE_SIZE_UNLIMITED` to disable garbage collection.

**Signature:**  

    cacheSizeBytes?: number;

## PersistentCacheSettings.tabManager

Specifies how multiple tabs/windows will be managed by the SDK.

**Signature:**  

    tabManager?: PersistentTabManager;