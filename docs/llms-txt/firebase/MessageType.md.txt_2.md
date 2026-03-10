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

| ### Enum Values |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/MessageType#BANNER` |   |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/MessageType#CARD` |   |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/MessageType#IMAGE_ONLY` |   |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/MessageType#MODAL` |   |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/MessageType#UNSUPPORTED` |   |

| ### Public functions |
|---|---|
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/MessageType!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/MessageType#valueOf(java.lang.String)(name: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!)` Returns the enum constant of this type with the specified name. |
| `java-static https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/MessageType!>!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/MessageType#values()()` Returns an array containing the constants of this enum type, in the order they're declared. |

## Enum Values

### BANNER

```
@Keep
val MessageType.BANNER: MessageType
```

### CARD

```
@Keep
val MessageType.CARD: MessageType
```

### IMAGE_ONLY

```
@Keep
val MessageType.IMAGE_ONLY: MessageType
```

### MODAL

```
@Keep
val MessageType.MODAL: MessageType
```

### UNSUPPORTED

```
@Keep
val MessageType.UNSUPPORTED: MessageType
```

## Public functions

### valueOf

```
java-static fun valueOf(name: String!): MessageType!
```

Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/MessageType!` | the enum constant with the specified name |

| Throws |
|---|---|
| `java.lang.IllegalArgumentException: https://developer.android.com/reference/kotlin/java/lang/IllegalArgumentException.html` | if this enum type has no constant with the specified name |

### values

```
java-static fun values(): Array<MessageType!>!
```

Returns an array containing the constants of this enum type, in the order they're declared. This method may be used to iterate over the constants.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/MessageType!>!` | an array containing the constants of this enum type, in the order they're declared |