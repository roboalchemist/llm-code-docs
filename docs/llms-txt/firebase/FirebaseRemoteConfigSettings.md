# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings.md.txt

# FirebaseRemoteConfigSettings

# FirebaseRemoteConfigSettings


```
public class FirebaseRemoteConfigSettings
```

<br />

*** ** * ** ***

Wraps the settings for [FirebaseRemoteConfig](https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfig) operations.

## Summary

|                                                                                                                                                                ### Nested types                                                                                                                                                                 |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `public class `[FirebaseRemoteConfigSettings.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings.Builder) Builder for a [FirebaseRemoteConfigSettings](https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings). |

| ### Public fields |
|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `final long`      | [fetchTimeoutInSeconds](https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings#fetchTimeoutInSeconds()) |

|                                                                                                                        ### Public methods                                                                                                                        |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `long`                                                                                                                                                                                                                                                           | [getFetchTimeoutInSeconds](https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings#getFetchTimeoutInSeconds())`()` Returns the fetch timeout in seconds.                                                                                                                                 |
| `long`                                                                                                                                                                                                                                                           | [getMinimumFetchIntervalInSeconds](https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings#getMinimumFetchIntervalInSeconds())`()` Returns the minimum interval between successive fetches calls in seconds.                                                                             |
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseRemoteConfigSettings.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings.Builder) | [toBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings#toBuilder())`()` Constructs a builder initialized with the current [FirebaseRemoteConfigSettings](https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings). |

## Public fields

### fetchTimeoutInSeconds

```
publicÂ finalÂ longÂ fetchTimeoutInSeconds
```  

## Public methods

### getFetchTimeoutInSeconds

```
publicÂ longÂ getFetchTimeoutInSeconds()
```

Returns the fetch timeout in seconds.

The timeout specifies how long the client should wait for a connection to the Firebase Remote Config server.  

### getMinimumFetchIntervalInSeconds

```
publicÂ longÂ getMinimumFetchIntervalInSeconds()
```

Returns the minimum interval between successive fetches calls in seconds.  

### toBuilder

```
publicÂ @NonNull FirebaseRemoteConfigSettings.BuilderÂ toBuilder()
```

Constructs a builder initialized with the current [FirebaseRemoteConfigSettings](https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings).