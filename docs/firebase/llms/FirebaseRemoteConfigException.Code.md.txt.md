# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigException.Code.md.txt

# FirebaseRemoteConfigException.Code

# FirebaseRemoteConfigException.Code


```
public enum FirebaseRemoteConfigException.Code
```

<br />

*** ** * ** ***

## Summary

| ### Enum Values |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigException.Code#CONFIG_UPDATE_MESSAGE_INVALID` | A config update stream message from the real-time RC backend is unparsable. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigException.Code#CONFIG_UPDATE_NOT_FETCHED` | Unable to fetch the latest config. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigException.Code#CONFIG_UPDATE_STREAM_ERROR` | Unable to make a connection to the real-time RC backend. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigException.Code#CONFIG_UPDATE_UNAVAILABLE` | The real-time RC backend is unavailable. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigException.Code#UNKNOWN` | Unknown code value. |

| ### Public methods |
|---|---|
| `int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigException.Code#value()()` |
| `static https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigException.Code` | `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigException.Code#valueOf(java.lang.String)(https://developer.android.com/reference/kotlin/java/lang/String.html name)` Returns the enum constant of this type with the specified name. |
| `static FirebaseRemoteConfigException.Code[]` | `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigException.Code#values()()` Returns an array containing the constants of this enum type, in the order they're declared. |

## Enum Values

### CONFIG_UPDATE_MESSAGE_INVALID

```
FirebaseRemoteConfigException.Code FirebaseRemoteConfigException.Code.CONFIG_UPDATE_MESSAGE_INVALID
```

A config update stream message from the real-time RC backend is unparsable.

### CONFIG_UPDATE_NOT_FETCHED

```
FirebaseRemoteConfigException.Code FirebaseRemoteConfigException.Code.CONFIG_UPDATE_NOT_FETCHED
```

Unable to fetch the latest config.

### CONFIG_UPDATE_STREAM_ERROR

```
FirebaseRemoteConfigException.Code FirebaseRemoteConfigException.Code.CONFIG_UPDATE_STREAM_ERROR
```

Unable to make a connection to the real-time RC backend.

### CONFIG_UPDATE_UNAVAILABLE

```
FirebaseRemoteConfigException.Code FirebaseRemoteConfigException.Code.CONFIG_UPDATE_UNAVAILABLE
```

The real-time RC backend is unavailable.

### UNKNOWN

```
FirebaseRemoteConfigException.Code FirebaseRemoteConfigException.Code.UNKNOWN
```

Unknown code value.

## Public methods

### value

```
public int value()
```

### valueOf

```
public static FirebaseRemoteConfigException.Code valueOf(String name)
```

Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigException.Code` | the enum constant with the specified name |

| Throws |
|---|---|
| `https://developer.android.com/reference/kotlin/java/lang/IllegalArgumentException.html java.lang.IllegalArgumentException` | if this enum type has no constant with the specified name |

### values

```
public static FirebaseRemoteConfigException.Code[] values()
```

Returns an array containing the constants of this enum type, in the order they're declared. This method may be used to iterate over the constants.

| Returns |
|---|---|
| `FirebaseRemoteConfigException.Code[]` | an array containing the constants of this enum type, in the order they're declared |