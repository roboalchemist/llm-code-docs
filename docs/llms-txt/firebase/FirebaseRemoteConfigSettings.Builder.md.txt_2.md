# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings.Builder.md.txt

# FirebaseRemoteConfigSettings.Builder

# FirebaseRemoteConfigSettings.Builder


```
class FirebaseRemoteConfigSettings.Builder
```

<br />

*** ** * ** ***

Builder for a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings`.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings.Builder#Builder()()` |

| ### Public functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings.Builder#build()()` Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings` with the settings provided to this builder. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings.Builder#getMinimumFetchIntervalInSeconds()()` Returns the minimum interval between successive fetches calls in seconds. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings.Builder#setMinimumFetchIntervalInSeconds(long)(duration: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)` Sets the minimum interval between successive fetch calls. |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings.Builder#fetchTimeoutInSeconds()` |

## Public constructors

### Builder

```
Builder()
```

## Public functions

### build

```
fun build(): FirebaseRemoteConfigSettings
```

Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings` with the settings provided to this builder.

### getMinimumFetchIntervalInSeconds

```
fun getMinimumFetchIntervalInSeconds(): Long
```

Returns the minimum interval between successive fetches calls in seconds.

### setMinimumFetchIntervalInSeconds

```
fun setMinimumFetchIntervalInSeconds(duration: Long): FirebaseRemoteConfigSettings.Builder
```

Sets the minimum interval between successive fetch calls.

Fetches less than `duration` seconds after the last fetch from the Firebase Remote Config server would use values returned during the last fetch.

| Parameters |
|---|---|
| `duration: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | Interval duration in seconds. Should be a non-negative number. |

## Public properties

### fetchTimeoutInSeconds

```
var fetchTimeoutInSeconds: Long
```