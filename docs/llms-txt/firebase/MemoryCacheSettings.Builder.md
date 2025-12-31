# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MemoryCacheSettings.Builder.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryCacheSettings.Builder.md.txt

# MemoryCacheSettings.Builder

# MemoryCacheSettings.Builder


```
class MemoryCacheSettings.Builder
```

<br />

*** ** * ** ***

A Builder for creating `MemoryCacheSettings` instance.

## Summary

|                                                            ### Public functions                                                            |
|--------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [MemoryCacheSettings](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryCacheSettings)                 | [build](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryCacheSettings.Builder#build())`()` Creates a `MemoryCacheSettings` instance.                                                                                                                                                                                                                                                                      |
| [MemoryCacheSettings.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryCacheSettings.Builder) | [setGcSettings](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryCacheSettings.Builder#setGcSettings(com.google.firebase.firestore.MemoryGarbageCollectorSettings))`(gcSettings: `[MemoryGarbageCollectorSettings](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryGarbageCollectorSettings)`)` Uses the given garbage collector settings to configure memory cache. |

## Public functions

### build

```
funÂ build():Â MemoryCacheSettings
```

Creates a `MemoryCacheSettings` instance.  

### setGcSettings

```
funÂ setGcSettings(gcSettings:Â MemoryGarbageCollectorSettings):Â MemoryCacheSettings.Builder
```

Uses the given garbage collector settings to configure memory cache.