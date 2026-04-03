# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings.Builder.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings.Builder.md.txt

# FirebaseRemoteConfigSettings.Builder

# FirebaseRemoteConfigSettings.Builder


```
class FirebaseRemoteConfigSettings.Builder
```

<br />

*** ** * ** ***

Builder for a [FirebaseRemoteConfigSettings](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings).

## Summary

|                                                             ### Public constructors                                                              |
|--------------------------------------------------------------------------------------------------------------------------------------------------|
| [Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings.Builder#Builder())`()` |

|                                                                      ### Public functions                                                                       |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [FirebaseRemoteConfigSettings](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings)                 | [build](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings.Builder#build())`()` Returns a [FirebaseRemoteConfigSettings](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings) with the settings provided to this builder.       |
| [Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)                                                                                    | [getMinimumFetchIntervalInSeconds](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings.Builder#getMinimumFetchIntervalInSeconds())`()` Returns the minimum interval between successive fetches calls in seconds.                                                                             |
| [FirebaseRemoteConfigSettings.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings.Builder) | [setMinimumFetchIntervalInSeconds](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings.Builder#setMinimumFetchIntervalInSeconds(long))`(duration: `[Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)`)` Sets the minimum interval between successive fetch calls. |

|                            ### Public properties                             |
|------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html) | [fetchTimeoutInSeconds](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings.Builder#fetchTimeoutInSeconds()) |

## Public constructors

### Builder

```
Builder()
```  

## Public functions

### build

```
funÂ build():Â FirebaseRemoteConfigSettings
```

Returns a [FirebaseRemoteConfigSettings](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings) with the settings provided to this builder.  

### getMinimumFetchIntervalInSeconds

```
funÂ getMinimumFetchIntervalInSeconds():Â Long
```

Returns the minimum interval between successive fetches calls in seconds.  

### setMinimumFetchIntervalInSeconds

```
funÂ setMinimumFetchIntervalInSeconds(duration:Â Long):Â FirebaseRemoteConfigSettings.Builder
```

Sets the minimum interval between successive fetch calls.

Fetches less than `duration` seconds after the last fetch from the Firebase Remote Config server would use values returned during the last fetch.  

|                                        Parameters                                        |
|------------------------------------------------------------------------------------------|----------------------------------------------------------------|
| `duration: `[Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html) | Interval duration in seconds. Should be a non-negative number. |

## Public properties

### fetchTimeoutInSeconds

```
varÂ fetchTimeoutInSeconds:Â Long
```