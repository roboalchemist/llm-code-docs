# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigException.Code.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigException.Code.md.txt

# FirebaseRemoteConfigException.Code

# FirebaseRemoteConfigException.Code


```
enum FirebaseRemoteConfigException.Code
```

<br />

*** ** * ** ***

## Summary

|                                                                                   ### Enum Values                                                                                    |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| [CONFIG_UPDATE_MESSAGE_INVALID](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigException.Code#CONFIG_UPDATE_MESSAGE_INVALID) | A config update stream message from the real-time RC backend is unparsable. |
| [CONFIG_UPDATE_NOT_FETCHED](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigException.Code#CONFIG_UPDATE_NOT_FETCHED)         | Unable to fetch the latest config.                                          |
| [CONFIG_UPDATE_STREAM_ERROR](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigException.Code#CONFIG_UPDATE_STREAM_ERROR)       | Unable to make a connection to the real-time RC backend.                    |
| [CONFIG_UPDATE_UNAVAILABLE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigException.Code#CONFIG_UPDATE_UNAVAILABLE)         | The real-time RC backend is unavailable.                                    |
| [UNKNOWN](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigException.Code#UNKNOWN)                                             | Unknown code value.                                                         |

|                                                                                                                      ### Public functions                                                                                                                       |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)                                                                                                                                                                                      | [value](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigException.Code#value())`()`                                                                                                                                                                              |
| `java-static `[FirebaseRemoteConfigException.Code](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigException.Code)`!`                                                                                    | [valueOf](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigException.Code#valueOf(java.lang.String))`(name: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!)` Returns the enum constant of this type with the specified name. |
| `java-static `[Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)`<`[FirebaseRemoteConfigException.Code](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigException.Code)`!>!` | [values](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigException.Code#values())`()` Returns an array containing the constants of this enum type, in the order they're declared.                                                                                |

## Enum Values

### CONFIG_UPDATE_MESSAGE_INVALID

```
valÂ FirebaseRemoteConfigException.Code.CONFIG_UPDATE_MESSAGE_INVALID:Â FirebaseRemoteConfigException.Code
```

A config update stream message from the real-time RC backend is unparsable.  

### CONFIG_UPDATE_NOT_FETCHED

```
valÂ FirebaseRemoteConfigException.Code.CONFIG_UPDATE_NOT_FETCHED:Â FirebaseRemoteConfigException.Code
```

Unable to fetch the latest config.  

### CONFIG_UPDATE_STREAM_ERROR

```
valÂ FirebaseRemoteConfigException.Code.CONFIG_UPDATE_STREAM_ERROR:Â FirebaseRemoteConfigException.Code
```

Unable to make a connection to the real-time RC backend.  

### CONFIG_UPDATE_UNAVAILABLE

```
valÂ FirebaseRemoteConfigException.Code.CONFIG_UPDATE_UNAVAILABLE:Â FirebaseRemoteConfigException.Code
```

The real-time RC backend is unavailable.  

### UNKNOWN

```
valÂ FirebaseRemoteConfigException.Code.UNKNOWN:Â FirebaseRemoteConfigException.Code
```

Unknown code value.  

## Public functions

### value

```
funÂ value():Â Int
```  

### valueOf

```
java-staticÂ funÂ valueOf(name:Â String!):Â FirebaseRemoteConfigException.Code!
```

Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)  

|                                                                            Returns                                                                             |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------|
| [FirebaseRemoteConfigException.Code](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigException.Code)`!` | the enum constant with the specified name |

|                                                                               Throws                                                                               |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| `java.lang.IllegalArgumentException: `[java.lang.IllegalArgumentException](https://developer.android.com/reference/kotlin/java/lang/IllegalArgumentException.html) | if this enum type has no constant with the specified name |

### values

```
java-staticÂ funÂ values():Â Array<FirebaseRemoteConfigException.Code!>!
```

Returns an array containing the constants of this enum type, in the order they're declared. This method may be used to iterate over the constants.  

|                                                                                                                      Returns                                                                                                                      |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| [Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)`<`[FirebaseRemoteConfigException.Code](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigException.Code)`!>!` | an array containing the constants of this enum type, in the order they're declared |