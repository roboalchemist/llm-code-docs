# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigValue.md.txt

# FirebaseRemoteConfigValue

# FirebaseRemoteConfigValue


```
public interface FirebaseRemoteConfigValue
```

<br />

*** ** * ** ***

Wrapper for a Remote Config parameter value, with methods to get it as different types.

## Summary

| ### Public methods |
|---|---|
| `abstract boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigValue#asBoolean()()` Gets the value as a `boolean`. |
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html byte[]` | `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigValue#asByteArray()()` Gets the value as a `byte[]`. |
| `abstract double` | `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigValue#asDouble()()` Gets the value as a `double`. |
| `abstract long` | `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigValue#asLong()()` Gets the value as a `long`. |
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigValue#asString()()` Gets the value as a `String`. |
| `abstract int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigValue#getSource()()` Indicates at which source this value came from. |

## Public methods

### asBoolean

```
abstract boolean asBoolean()
```

Gets the value as a `boolean`.

| Returns |
|---|---|
| `boolean` | `boolean` representation of this parameter value. |

| Throws |
|---|---|
| `https://developer.android.com/reference/kotlin/java/lang/IllegalArgumentException.html java.lang.IllegalArgumentException` | If the value cannot be converted to a `boolean`. |

### asByteArray

```
abstract @NonNull byte[] asByteArray()
```

Gets the value as a `byte[]`.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html byte[]` | `byte[]` representation of this parameter value. |

### asDouble

```
abstract double asDouble()
```

Gets the value as a `double`.

| Returns |
|---|---|
| `double` | `double` representation of this parameter value. |

| Throws |
|---|---|
| `https://developer.android.com/reference/kotlin/java/lang/IllegalArgumentException.html java.lang.IllegalArgumentException` | If the value cannot be converted to a `double`. |

### asLong

```
abstract long asLong()
```

Gets the value as a `long`.

| Returns |
|---|---|
| `long` | `long` representation of this parameter value. |

| Throws |
|---|---|
| `https://developer.android.com/reference/kotlin/java/lang/IllegalArgumentException.html java.lang.IllegalArgumentException` | If the value cannot be converted to a `long`. |

### asString

```
abstract @NonNull String asString()
```

Gets the value as a `String`.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `String` representation of this parameter value. |

### getSource

```
abstract int getSource()
```

Indicates at which source this value came from.

| Returns |
|---|---|
| `int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfig#VALUE_SOURCE_REMOTE()` if the value was retrieved from the server, `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfig#VALUE_SOURCE_DEFAULT()` if the value was set as a default, or `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfig#VALUE_SOURCE_STATIC()` if no value was found and a static default value was returned instead. |