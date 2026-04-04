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

| ### Public functions |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `@https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeResult.Operation https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeUrl#getOperation()()` Returns the mapping of the mode string in the action code URL to a . |
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeUrl?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeUrl#parseLink(java.lang.String)(link: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?)` Returns an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeUrl` instance if the `link` is valid, otherwise null. |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeUrl#apiKey()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeUrl#code()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeUrl#continueUrl()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeUrl#languageCode()` |

## Public functions

### getOperation

```
@ActionCodeResult.Operation
fun getOperation(): Int
```

Returns the mapping of the mode string in the action code URL to a .

### parseLink

```
java-static fun parseLink(link: String?): ActionCodeUrl?
```

Returns an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeUrl` instance if the `link` is valid, otherwise null.

| Throws |
|---|---|
| `https://developer.android.com/reference/java/lang/IllegalArgumentException.html` | if `link` is null or empty |

## Public properties

### apiKey

```
val apiKey: String!
```

### code

```
val code: String!
```

### continueUrl

```
val continueUrl: String?
```

### languageCode

```
val languageCode: String?
```