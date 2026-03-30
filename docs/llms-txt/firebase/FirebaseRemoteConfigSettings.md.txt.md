# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings.md.txt

# FirebaseRemoteConfigSettings

# FirebaseRemoteConfigSettings


```
public class FirebaseRemoteConfigSettings
```

<br />

*** ** * ** ***

Wraps the settings for `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfig` operations.

## Summary

| ### Nested types |
|---|
| `public class https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings.Builder` Builder for a `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings`. |

| ### Public fields |
|---|---|
| `final long` | `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings#fetchTimeoutInSeconds()` |

| ### Public methods |
|---|---|
| `long` | `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings#getFetchTimeoutInSeconds()()` Returns the fetch timeout in seconds. |
| `long` | `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings#getMinimumFetchIntervalInSeconds()()` Returns the minimum interval between successive fetches calls in seconds. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings#toBuilder()()` Constructs a builder initialized with the current `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings`. |

## Public fields

### fetchTimeoutInSeconds

```
public final long fetchTimeoutInSeconds
```

## Public methods

### getFetchTimeoutInSeconds

```
public long getFetchTimeoutInSeconds()
```

Returns the fetch timeout in seconds.

The timeout specifies how long the client should wait for a connection to the Firebase Remote Config server.

### getMinimumFetchIntervalInSeconds

```
public long getMinimumFetchIntervalInSeconds()
```

Returns the minimum interval between successive fetches calls in seconds.

### toBuilder

```
public @NonNull FirebaseRemoteConfigSettings.Builder toBuilder()
```

Constructs a builder initialized with the current `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings`.