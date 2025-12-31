# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeUrl.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeUrl.md.txt

# ActionCodeUrl

# ActionCodeUrl


```
class ActionCodeUrl
```

<br />

*** ** * ** ***

A utility class to parse parameters in action code URLs from out of band email flows.

## Summary

|                                                    ### Public functions                                                    |
|----------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)                                                 | `@`[ActionCodeResult.Operation](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeResult.Operation) [getOperation](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeUrl#getOperation())`()` Returns the mapping of the mode string in the action code URL to a .                                                              |
| `java-static `[ActionCodeUrl](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeUrl)`?` | [parseLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeUrl#parseLink(java.lang.String))`(link: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?)` Returns an [ActionCodeUrl](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeUrl) instance if the `link` is valid, otherwise null. |

|                                ### Public properties                                |
|-------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [apiKey](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeUrl#apiKey())             |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [code](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeUrl#code())                 |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?` | [continueUrl](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeUrl#continueUrl())   |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?` | [languageCode](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeUrl#languageCode()) |

## Public functions

### getOperation

```
@ActionCodeResult.Operation
funÂ getOperation():Â Int
```

Returns the mapping of the mode string in the action code URL to a .  

### parseLink

```
java-staticÂ funÂ parseLink(link:Â String?):Â ActionCodeUrl?
```

Returns an [ActionCodeUrl](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeUrl) instance if the `link` is valid, otherwise null.  

|                                                        Throws                                                         |
|-----------------------------------------------------------------------------------------------------------------------|----------------------------|
| [java.lang.IllegalArgumentException](https://developer.android.com/reference/java/lang/IllegalArgumentException.html) | if `link` is null or empty |

## Public properties

### apiKey

```
valÂ apiKey:Â String!
```  

### code

```
valÂ code:Â String!
```  

### continueUrl

```
valÂ continueUrl:Â String?
```  

### languageCode

```
valÂ languageCode:Â String?
```