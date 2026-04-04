# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LocalCacheSettings.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LocalCacheSettings.md.txt

# LocalCacheSettings

# LocalCacheSettings


```
interface LocalCacheSettings
```

<br />

Known direct subclasses  
[MemoryCacheSettings](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryCacheSettings), [PersistentCacheSettings](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PersistentCacheSettings)  

|------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| [MemoryCacheSettings](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryCacheSettings)         | Configures the SDK to use a memory cache.     |
| [PersistentCacheSettings](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PersistentCacheSettings) | Configures the SDK to use a persistent cache. |

*** ** * ** ***

Marker interface implemented by all supported cache settings.

[PersistentCacheSettings](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PersistentCacheSettings) and [MemoryCacheSettings](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryCacheSettings) are the two only cache types supported by the SDK. Custom implementation is not supported.