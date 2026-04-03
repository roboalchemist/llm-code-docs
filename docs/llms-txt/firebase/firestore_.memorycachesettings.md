# Source: https://firebase.google.com/docs/reference/js/firestore_.memorycachesettings.md.txt

# MemoryCacheSettings interface

An settings object to configure an `MemoryLocalCache` instance.

**Signature:**  

    export declare interface MemoryCacheSettings 

## Properties

|                                                                Property                                                                 |                                                     Type                                                     |                                                        Description                                                        |
|-----------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| [garbageCollector](https://firebase.google.com/docs/reference/js/firestore_.memorycachesettings.md#memorycachesettingsgarbagecollector) | [MemoryGarbageCollector](https://firebase.google.com/docs/reference/js/firestore_.md#memorygarbagecollector) | The garbage collector to use, for the memory cache layer. A `MemoryEagerGarbageCollector` is used when this is undefined. |

## MemoryCacheSettings.garbageCollector

The garbage collector to use, for the memory cache layer. A `MemoryEagerGarbageCollector` is used when this is undefined.

**Signature:**  

    garbageCollector?: MemoryGarbageCollector;