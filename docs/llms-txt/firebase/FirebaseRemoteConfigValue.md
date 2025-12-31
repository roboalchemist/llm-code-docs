# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigValue.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigValue.md.txt

# FirebaseRemoteConfigValue

# FirebaseRemoteConfigValue


```
interface FirebaseRemoteConfigValue
```

<br />

*** ** * ** ***

Wrapper for a Remote Config parameter value, with methods to get it as different types.

## Summary

|                                                                           ### Public functions                                                                            |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)                                                                                        | [asBoolean](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigValue#asBoolean())`()` Gets the value as a `boolean`.                  |
| [ByteArray](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html)`<`[Byte](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte/index.html)`>` | [asByteArray](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigValue#asByteArray())`()` Gets the value as a `byte[]`.               |
| [Double](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html)                                                                                          | [asDouble](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigValue#asDouble())`()` Gets the value as a `double`.                     |
| [Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)                                                                                              | [asLong](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigValue#asLong())`()` Gets the value as a `long`.                           |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)                                                                                          | [asString](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigValue#asString())`()` Gets the value as a `String`.                     |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)                                                                                                | [getSource](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigValue#getSource())`()` Indicates at which source this value came from. |

## Public functions

### asBoolean

```
funÂ asBoolean():Â Boolean
```

Gets the value as a `boolean`.  

|                                      Returns                                       |
|------------------------------------------------------------------------------------|---------------------------------------------------|
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `boolean` representation of this parameter value. |

|                                                                               Throws                                                                               |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------|
| `java.lang.IllegalArgumentException: `[java.lang.IllegalArgumentException](https://developer.android.com/reference/kotlin/java/lang/IllegalArgumentException.html) | If the value cannot be converted to a `boolean`. |

### asByteArray

```
funÂ asByteArray():Â ByteArray<Byte>
```

Gets the value as a `byte[]`.  

|                                                                                  Returns                                                                                  |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------|
| [ByteArray](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html)`<`[Byte](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte/index.html)`>` | `byte[]` representation of this parameter value. |

### asDouble

```
funÂ asDouble():Â Double
```

Gets the value as a `double`.  

|                                     Returns                                      |
|----------------------------------------------------------------------------------|--------------------------------------------------|
| [Double](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html) | `double` representation of this parameter value. |

|                                                                               Throws                                                                               |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------|
| `java.lang.IllegalArgumentException: `[java.lang.IllegalArgumentException](https://developer.android.com/reference/kotlin/java/lang/IllegalArgumentException.html) | If the value cannot be converted to a `double`. |

### asLong

```
funÂ asLong():Â Long
```

Gets the value as a `long`.  

|                                   Returns                                    |
|------------------------------------------------------------------------------|------------------------------------------------|
| [Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html) | `long` representation of this parameter value. |

|                                                                               Throws                                                                               |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| `java.lang.IllegalArgumentException: `[java.lang.IllegalArgumentException](https://developer.android.com/reference/kotlin/java/lang/IllegalArgumentException.html) | If the value cannot be converted to a `long`. |

### asString

```
funÂ asString():Â String
```

Gets the value as a `String`.  

|                                     Returns                                      |
|----------------------------------------------------------------------------------|--------------------------------------------------|
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | `String` representation of this parameter value. |

### getSource

```
funÂ getSource():Â Int
```

Indicates at which source this value came from.  

|                                  Returns                                   |
|----------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [VALUE_SOURCE_REMOTE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#VALUE_SOURCE_REMOTE()) if the value was retrieved from the server, [VALUE_SOURCE_DEFAULT](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#VALUE_SOURCE_DEFAULT()) if the value was set as a default, or [VALUE_SOURCE_STATIC](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#VALUE_SOURCE_STATIC()) if no value was found and a static default value was returned instead. |