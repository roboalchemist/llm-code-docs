# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings.Builder.md.txt

# FirebaseRemoteConfigSettings.Builder

# FirebaseRemoteConfigSettings.Builder


```
public class FirebaseRemoteConfigSettings.Builder
```

<br />

*** ** * ** ***

Builder for a `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings`.

## Summary

| ### Public fields |
|---|---|
| `long` | `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings.Builder#fetchTimeoutInSeconds()` |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings.Builder#Builder()()` |

| ### Public methods |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings` | `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings.Builder#build()()` Returns a `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings` with the settings provided to this builder. |
| `long` | `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings.Builder#getFetchTimeoutInSeconds()()` Returns the fetch timeout in seconds. |
| `long` | `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings.Builder#getMinimumFetchIntervalInSeconds()()` Returns the minimum interval between successive fetches calls in seconds. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings.Builder#setFetchTimeoutInSeconds(long)(long duration)` Sets the connection and read timeouts for fetch requests to the Firebase Remote Config servers in seconds. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings.Builder#setMinimumFetchIntervalInSeconds(long)(long duration)` Sets the minimum interval between successive fetch calls. |

## Public fields

### fetchTimeoutInSeconds

```
public long fetchTimeoutInSeconds
```

## Public constructors

### Builder

```
public Builder()
```

## Public methods

### build

```
public @NonNull FirebaseRemoteConfigSettings build()
```

Returns a `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings` with the settings provided to this builder.

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

### setFetchTimeoutInSeconds

```
public @NonNull FirebaseRemoteConfigSettings.Builder setFetchTimeoutInSeconds(long duration)
```

Sets the connection and read timeouts for fetch requests to the Firebase Remote Config servers in seconds.

A fetch call will fail if it takes longer than the specified timeout to connect to or read from the Remote Config server.

| Parameters |
|---|---|
| `long duration` | Timeout duration in seconds. Should be a non-negative number. |

### setMinimumFetchIntervalInSeconds

```
public @NonNull FirebaseRemoteConfigSettings.Builder setMinimumFetchIntervalInSeconds(long duration)
```

Sets the minimum interval between successive fetch calls.

Fetches less than `duration` seconds after the last fetch from the Firebase Remote Config server would use values returned during the last fetch.

| Parameters |
|---|---|
| `long duration` | Interval duration in seconds. Should be a non-negative number. |