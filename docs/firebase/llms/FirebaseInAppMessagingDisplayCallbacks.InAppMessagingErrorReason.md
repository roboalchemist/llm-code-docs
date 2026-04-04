# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/FirebaseInAppMessagingDisplayCallbacks.InAppMessagingErrorReason.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingDisplayCallbacks.InAppMessagingErrorReason.md.txt

# FirebaseInAppMessagingDisplayCallbacks.InAppMessagingErrorReason

# FirebaseInAppMessagingDisplayCallbacks.InAppMessagingErrorReason


```
enum FirebaseInAppMessagingDisplayCallbacks.InAppMessagingErrorReason
```

<br />

*** ** * ** ***

## Summary

|                                                                                              ### Enum Values                                                                                               |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| [IMAGE_DISPLAY_ERROR](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingDisplayCallbacks.InAppMessagingErrorReason#IMAGE_DISPLAY_ERROR)           |   |
| [IMAGE_FETCH_ERROR](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingDisplayCallbacks.InAppMessagingErrorReason#IMAGE_FETCH_ERROR)               |   |
| [IMAGE_UNSUPPORTED_FORMAT](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingDisplayCallbacks.InAppMessagingErrorReason#IMAGE_UNSUPPORTED_FORMAT) |   |
| [UNSPECIFIED_RENDER_ERROR](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingDisplayCallbacks.InAppMessagingErrorReason#UNSPECIFIED_RENDER_ERROR) |   |

|                                                                                                                                                     ### Public functions                                                                                                                                                      |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `java-static `[FirebaseInAppMessagingDisplayCallbacks.InAppMessagingErrorReason](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingDisplayCallbacks.InAppMessagingErrorReason)`!`                                                                                    | [valueOf](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingDisplayCallbacks.InAppMessagingErrorReason#valueOf(java.lang.String))`(name: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!)` Returns the enum constant of this type with the specified name. |
| `java-static `[Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)`<`[FirebaseInAppMessagingDisplayCallbacks.InAppMessagingErrorReason](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingDisplayCallbacks.InAppMessagingErrorReason)`!>!` | [values](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingDisplayCallbacks.InAppMessagingErrorReason#values())`()` Returns an array containing the constants of this enum type, in the order they're declared.                                                                                |

## Enum Values

### IMAGE_DISPLAY_ERROR

```
valÂ FirebaseInAppMessagingDisplayCallbacks.InAppMessagingErrorReason.IMAGE_DISPLAY_ERROR:Â FirebaseInAppMessagingDisplayCallbacks.InAppMessagingErrorReason
```  

### IMAGE_FETCH_ERROR

```
valÂ FirebaseInAppMessagingDisplayCallbacks.InAppMessagingErrorReason.IMAGE_FETCH_ERROR:Â FirebaseInAppMessagingDisplayCallbacks.InAppMessagingErrorReason
```  

### IMAGE_UNSUPPORTED_FORMAT

```
valÂ FirebaseInAppMessagingDisplayCallbacks.InAppMessagingErrorReason.IMAGE_UNSUPPORTED_FORMAT:Â FirebaseInAppMessagingDisplayCallbacks.InAppMessagingErrorReason
```  

### UNSPECIFIED_RENDER_ERROR

```
valÂ FirebaseInAppMessagingDisplayCallbacks.InAppMessagingErrorReason.UNSPECIFIED_RENDER_ERROR:Â FirebaseInAppMessagingDisplayCallbacks.InAppMessagingErrorReason
```  

## Public functions

### valueOf

```
java-staticÂ funÂ valueOf(name:Â String!):Â FirebaseInAppMessagingDisplayCallbacks.InAppMessagingErrorReason!
```

Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)  

|                                                                                                           Returns                                                                                                            |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------|
| [FirebaseInAppMessagingDisplayCallbacks.InAppMessagingErrorReason](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingDisplayCallbacks.InAppMessagingErrorReason)`!` | the enum constant with the specified name |

|                                                                               Throws                                                                               |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| `java.lang.IllegalArgumentException: `[java.lang.IllegalArgumentException](https://developer.android.com/reference/kotlin/java/lang/IllegalArgumentException.html) | if this enum type has no constant with the specified name |

### values

```
java-staticÂ funÂ values():Â Array<FirebaseInAppMessagingDisplayCallbacks.InAppMessagingErrorReason!>!
```

Returns an array containing the constants of this enum type, in the order they're declared. This method may be used to iterate over the constants.  

|                                                                                                                                                     Returns                                                                                                                                                     |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| [Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)`<`[FirebaseInAppMessagingDisplayCallbacks.InAppMessagingErrorReason](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingDisplayCallbacks.InAppMessagingErrorReason)`!>!` | an array containing the constants of this enum type, in the order they're declared |