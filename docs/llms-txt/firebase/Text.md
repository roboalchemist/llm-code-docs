# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/Text.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/Text.md.txt

# Text

# Text


```
public class Text
```

<br />

*** ** * ** ***

Encapsulates any text used in a Firebase In App Message.

## Summary

|                                                                                   ### Public fields                                                                                    |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)   | [hexColor](https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/Text#hexColor())                                                     |
| `final @`[Nullable](https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html) | [text](https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/Text#text()) !!!!!WARNING!!!!! We are overriding equality in this class. |

|                                                                                ### Public methods                                                                                |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)   | [getHexColor](https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/Text#getHexColor())`()` Gets the hex color of this text |
| `@`[Nullable](https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html) | [getText](https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/Text#getText())`()` Gets the text                           |

## Public fields

### hexColor

```
publicÂ finalÂ @NonNull StringÂ hexColor
```  

### text

```
publicÂ finalÂ @Nullable StringÂ text
```

!!!!!WARNING!!!!! We are overriding equality in this class. Please add equality checks for all new private class members.  

## Public methods

### getHexColor

```
publicÂ @NonNull StringÂ getHexColor()
```

Gets the hex color of this text  

### getText

```
publicÂ @Nullable StringÂ getText()
```

Gets the text