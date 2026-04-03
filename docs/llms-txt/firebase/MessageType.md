# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/MessageType.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/MessageType.md.txt

# MessageType

# MessageType


```
@Keep
enum MessageType
```

<br />

*** ** * ** ***

Template type of an in-app message

## Summary

|                                                          ### Enum Values                                                          |
|-----------------------------------------------------------------------------------------------------------------------------------|---|
| [BANNER](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/MessageType#BANNER)           |   |
| [CARD](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/MessageType#CARD)               |   |
| [IMAGE_ONLY](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/MessageType#IMAGE_ONLY)   |   |
| [MODAL](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/MessageType#MODAL)             |   |
| [UNSUPPORTED](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/MessageType#UNSUPPORTED) |   |

|                                                                                                   ### Public functions                                                                                                    |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `java-static `[MessageType](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/MessageType)`!`                                                                                    | [valueOf](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/MessageType#valueOf(java.lang.String))`(name: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!)` Returns the enum constant of this type with the specified name. |
| `java-static `[Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)`<`[MessageType](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/MessageType)`!>!` | [values](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/MessageType#values())`()` Returns an array containing the constants of this enum type, in the order they're declared.                                                                                |

## Enum Values

### BANNER

```
@Keep
valÂ MessageType.BANNER:Â MessageType
```  

### CARD

```
@Keep
valÂ MessageType.CARD:Â MessageType
```  

### IMAGE_ONLY

```
@Keep
valÂ MessageType.IMAGE_ONLY:Â MessageType
```  

### MODAL

```
@Keep
valÂ MessageType.MODAL:Â MessageType
```  

### UNSUPPORTED

```
@Keep
valÂ MessageType.UNSUPPORTED:Â MessageType
```  

## Public functions

### valueOf

```
java-staticÂ funÂ valueOf(name:Â String!):Â MessageType!
```

Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)  

|                                                         Returns                                                          |
|--------------------------------------------------------------------------------------------------------------------------|-------------------------------------------|
| [MessageType](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/MessageType)`!` | the enum constant with the specified name |

|                                                                               Throws                                                                               |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| `java.lang.IllegalArgumentException: `[java.lang.IllegalArgumentException](https://developer.android.com/reference/kotlin/java/lang/IllegalArgumentException.html) | if this enum type has no constant with the specified name |

### values

```
java-staticÂ funÂ values():Â Array<MessageType!>!
```

Returns an array containing the constants of this enum type, in the order they're declared. This method may be used to iterate over the constants.  

|                                                                                                   Returns                                                                                                   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| [Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)`<`[MessageType](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/MessageType)`!>!` | an array containing the constants of this enum type, in the order they're declared |