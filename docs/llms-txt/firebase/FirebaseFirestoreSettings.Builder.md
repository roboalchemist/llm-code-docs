# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder.md.txt

# FirebaseFirestoreSettings.Builder

# FirebaseFirestoreSettings.Builder


```
class FirebaseFirestoreSettings.Builder
```

<br />

*** ** * ** ***

A Builder for creating `FirebaseFirestoreSettings`.

## Summary

|                                                                                                                                                                                                                      ### Public constructors                                                                                                                                                                                                                       |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder#Builder())`()` Constructs a new `FirebaseFirestoreSettings` Builder object.                                                                                                                                                                                                                                                            |
| [Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder#Builder(com.google.firebase.firestore.FirebaseFirestoreSettings))`(settings: `[FirebaseFirestoreSettings](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings)`)` Constructs a new `FirebaseFirestoreSettings` Builder based on an existing ` FirebaseFirestoreSettings` object. |

|                                                                  ### Public functions                                                                  |
|--------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [FirebaseFirestoreSettings](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings)                 | [build](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder#build())`()`                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)                                                                     | ~~[isPersistenceEnabled](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder#isPersistenceEnabled())~~`()` **This function is deprecated.** Instead, build the [FirebaseFirestoreSettings](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings) instance to check the SDK cache configurations. <br />                                                                                                                                                   |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)                                                                     | [isSslEnabled](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder#isSslEnabled())`()`                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [FirebaseFirestoreSettings.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder) | [setLocalCacheSettings](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder#setLocalCacheSettings(com.google.firebase.firestore.LocalCacheSettings))`(settings: `[LocalCacheSettings](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LocalCacheSettings)`)` Specifies the cache used by the SDK.                                                                                                                                                                              |
| [FirebaseFirestoreSettings.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder) | ~~[setPersistenceEnabled](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder#setPersistenceEnabled(boolean))~~`(value: `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)`)` **This function is deprecated.** Instead, use [setLocalCacheSettings](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder#setLocalCacheSettings(com.google.firebase.firestore.LocalCacheSettings)) to configure SDK cache. <br /> |
| [FirebaseFirestoreSettings.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder) | [setSslEnabled](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder#setSslEnabled(boolean))`(value: `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)`)` Enables or disables SSL for communication.                                                                                                                                                                                                                                                                          |

|                                ### Public properties                                |
|-------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)        | [cacheSizeBytes](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder#cacheSizeBytes()) |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [host](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder#host())                     |

## Public constructors

### Builder

```
Builder()
```

Constructs a new `FirebaseFirestoreSettings` Builder object.  

### Builder

```
Builder(settings:Â FirebaseFirestoreSettings)
```

Constructs a new `FirebaseFirestoreSettings` Builder based on an existing `
FirebaseFirestoreSettings` object.  

## Public functions

### build

```
funÂ build():Â FirebaseFirestoreSettings
```  

### isPersistenceEnabled

```
funÂ [isPersistenceEnabled](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder#isPersistenceEnabled())():Â Boolean
```
| **This function is deprecated.**   
|
Instead, build the [FirebaseFirestoreSettings](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings) instance to check the SDK cache configurations.  

|                                      Returns                                       |
|------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | boolean indicating whether local persistent storage is enabled or not. |

### isSslEnabled

```
funÂ isSslEnabled():Â Boolean
```  

|                                      Returns                                       |
|------------------------------------------------------------------------------------|---------------------------------------------------|
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | boolean indicating whether SSL is enabled or not. |

### setLocalCacheSettings

```
funÂ setLocalCacheSettings(settings:Â LocalCacheSettings):Â FirebaseFirestoreSettings.Builder
```

Specifies the cache used by the SDK. Available options are [PersistentCacheSettings](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PersistentCacheSettings) and [MemoryCacheSettings](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryCacheSettings), each with different configuration options.

When unspecified, [PersistentCacheSettings](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PersistentCacheSettings) will be used by default.

NOTE: Calling this setter and `setPersistenceEnabled()` or `
setCacheSizeBytes()` at the same time will throw an exception during SDK initialization. Instead, use the configuration in the [PersistentCacheSettings](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PersistentCacheSettings) object to specify the cache size.  

|                                                                        Returns                                                                         |
|--------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| [FirebaseFirestoreSettings.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder) | A settings object on which the cache settings is configured as specified by the given `settings`. |

### setPersistenceEnabled

```
funÂ [setPersistenceEnabled](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder#setPersistenceEnabled(boolean))(value:Â Boolean):Â FirebaseFirestoreSettings.Builder
```
| **This function is deprecated.**   
|
| Instead, use [setLocalCacheSettings](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder#setLocalCacheSettings(com.google.firebase.firestore.LocalCacheSettings)) to configure SDK cache.

Enables or disables local persistent storage. The default is to use local persistent storage.  

|                                                                        Returns                                                                         |
|--------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| [FirebaseFirestoreSettings.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder) | A settings object that uses local persistent storage as specified by the given value. |

### setSslEnabled

```
funÂ setSslEnabled(value:Â Boolean):Â FirebaseFirestoreSettings.Builder
```

Enables or disables SSL for communication. The default is to use SSL.  

|                                                                        Returns                                                                         |
|--------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------|
| [FirebaseFirestoreSettings.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder) | A settings object that uses SSL as specified by the value. |

## Public properties

### cacheSizeBytes

```
varÂ cacheSizeBytes:Â Long
```  

### host

```
varÂ host:Â String!
```