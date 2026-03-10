# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/MessageType.md.txt

# MessageType

# MessageType


```
@Keep
public enum MessageType
```

<br />

*** ** * ** ***

Template type of an in-app message

## Summary

| ### Enum Values |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/MessageType#BANNER` |   |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/MessageType#CARD` |   |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/MessageType#IMAGE_ONLY` |   |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/MessageType#MODAL` |   |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/MessageType#UNSUPPORTED` |   |

| ### Public methods |
|---|---|
| `static https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/MessageType` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/MessageType#valueOf(java.lang.String)(https://developer.android.com/reference/kotlin/java/lang/String.html name)` Returns the enum constant of this type with the specified name. |
| `static MessageType[]` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/MessageType#values()()` Returns an array containing the constants of this enum type, in the order they're declared. |

## Enum Values

### BANNER

```
@Keep
MessageType MessageType.BANNER
```

### CARD

```
@Keep
MessageType MessageType.CARD
```

### IMAGE_ONLY

```
@Keep
MessageType MessageType.IMAGE_ONLY
```

### MODAL

```
@Keep
MessageType MessageType.MODAL
```

### UNSUPPORTED

```
@Keep
MessageType MessageType.UNSUPPORTED
```

## Public methods

### valueOf

```
public static MessageType valueOf(String name)
```

Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/MessageType` | the enum constant with the specified name |

| Throws |
|---|---|
| `https://developer.android.com/reference/kotlin/java/lang/IllegalArgumentException.html java.lang.IllegalArgumentException` | if this enum type has no constant with the specified name |

### values

```
public static MessageType[] values()
```

Returns an array containing the constants of this enum type, in the order they're declared. This method may be used to iterate over the constants.

| Returns |
|---|---|
| `MessageType[]` | an array containing the constants of this enum type, in the order they're declared |