# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigException.Code.md.txt

# FirebaseRemoteConfigException.Code

# FirebaseRemoteConfigException.Code


```
enum FirebaseRemoteConfigException.Code
```

<br />

*** ** * ** ***

## Summary

| ### Enum Values |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigException.Code#CONFIG_UPDATE_MESSAGE_INVALID` | A config update stream message from the real-time RC backend is unparsable. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigException.Code#CONFIG_UPDATE_NOT_FETCHED` | Unable to fetch the latest config. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigException.Code#CONFIG_UPDATE_STREAM_ERROR` | Unable to make a connection to the real-time RC backend. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigException.Code#CONFIG_UPDATE_UNAVAILABLE` | The real-time RC backend is unavailable. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigException.Code#UNKNOWN` | Unknown code value. |

| ### Public functions |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigException.Code#value()()` |
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigException.Code!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigException.Code#valueOf(java.lang.String)(name: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!)` Returns the enum constant of this type with the specified name. |
| `java-static https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigException.Code!>!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigException.Code#values()()` Returns an array containing the constants of this enum type, in the order they're declared. |

## Enum Values

### CONFIG_UPDATE_MESSAGE_INVALID

```
val FirebaseRemoteConfigException.Code.CONFIG_UPDATE_MESSAGE_INVALID: FirebaseRemoteConfigException.Code
```

A config update stream message from the real-time RC backend is unparsable.

### CONFIG_UPDATE_NOT_FETCHED

```
val FirebaseRemoteConfigException.Code.CONFIG_UPDATE_NOT_FETCHED: FirebaseRemoteConfigException.Code
```

Unable to fetch the latest config.

### CONFIG_UPDATE_STREAM_ERROR

```
val FirebaseRemoteConfigException.Code.CONFIG_UPDATE_STREAM_ERROR: FirebaseRemoteConfigException.Code
```

Unable to make a connection to the real-time RC backend.

### CONFIG_UPDATE_UNAVAILABLE

```
val FirebaseRemoteConfigException.Code.CONFIG_UPDATE_UNAVAILABLE: FirebaseRemoteConfigException.Code
```

The real-time RC backend is unavailable.

### UNKNOWN

```
val FirebaseRemoteConfigException.Code.UNKNOWN: FirebaseRemoteConfigException.Code
```

Unknown code value.

## Public functions

### value

```
fun value(): Int
```

### valueOf

```
java-static fun valueOf(name: String!): FirebaseRemoteConfigException.Code!
```

Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigException.Code!` | the enum constant with the specified name |

| Throws |
|---|---|
| `java.lang.IllegalArgumentException: https://developer.android.com/reference/kotlin/java/lang/IllegalArgumentException.html` | if this enum type has no constant with the specified name |

### values

```
java-static fun values(): Array<FirebaseRemoteConfigException.Code!>!
```

Returns an array containing the constants of this enum type, in the order they're declared. This method may be used to iterate over the constants.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigException.Code!>!` | an array containing the constants of this enum type, in the order they're declared |