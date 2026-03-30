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

| ### Public functions |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigValue#asBoolean()()` Gets the value as a `boolean`. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte/index.html>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigValue#asByteArray()()` Gets the value as a `byte[]`. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigValue#asDouble()()` Gets the value as a `double`. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigValue#asLong()()` Gets the value as a `long`. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigValue#asString()()` Gets the value as a `String`. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigValue#getSource()()` Indicates at which source this value came from. |

## Public functions

### asBoolean

```
fun asBoolean(): Boolean
```

Gets the value as a `boolean`.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `boolean` representation of this parameter value. |

| Throws |
|---|---|
| `java.lang.IllegalArgumentException: https://developer.android.com/reference/kotlin/java/lang/IllegalArgumentException.html` | If the value cannot be converted to a `boolean`. |

### asByteArray

```
fun asByteArray(): ByteArray<Byte>
```

Gets the value as a `byte[]`.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte/index.html>` | `byte[]` representation of this parameter value. |

### asDouble

```
fun asDouble(): Double
```

Gets the value as a `double`.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html` | `double` representation of this parameter value. |

| Throws |
|---|---|
| `java.lang.IllegalArgumentException: https://developer.android.com/reference/kotlin/java/lang/IllegalArgumentException.html` | If the value cannot be converted to a `double`. |

### asLong

```
fun asLong(): Long
```

Gets the value as a `long`.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `long` representation of this parameter value. |

| Throws |
|---|---|
| `java.lang.IllegalArgumentException: https://developer.android.com/reference/kotlin/java/lang/IllegalArgumentException.html` | If the value cannot be converted to a `long`. |

### asString

```
fun asString(): String
```

Gets the value as a `String`.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `String` representation of this parameter value. |

### getSource

```
fun getSource(): Int
```

Indicates at which source this value came from.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#VALUE_SOURCE_REMOTE()` if the value was retrieved from the server, `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#VALUE_SOURCE_DEFAULT()` if the value was set as a default, or `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#VALUE_SOURCE_STATIC()` if no value was found and a static default value was returned instead. |