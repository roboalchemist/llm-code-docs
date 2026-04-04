# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LocalCacheSettings.md.txt

# LocalCacheSettings

# LocalCacheSettings


```
public interface LocalCacheSettings
```

<br />

Known direct subclasses [MemoryCacheSettings](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MemoryCacheSettings), [PersistentCacheSettings](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PersistentCacheSettings)

|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MemoryCacheSettings` | Configures the SDK to use a memory cache. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PersistentCacheSettings` | Configures the SDK to use a persistent cache. |

*** ** * ** ***

Marker interface implemented by all supported cache settings.

`https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PersistentCacheSettings` and `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MemoryCacheSettings` are the two only cache types supported by the SDK. Custom implementation is not supported.