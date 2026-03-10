# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableOptions.md.txt

# HttpsCallableOptions

# HttpsCallableOptions


```
class HttpsCallableOptions
```

<br />

*** ** * ** ***

Options for configuring the callable function.

These properties are immutable once a callable function reference is instantiated.

## Summary

| ### Nested types |
|---|
| `class https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableOptions.Builder` A builder for creating `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableOptions`. |

| ### Public functions |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableOptions#getLimitedUseAppCheckTokens()()` |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableOptions#limitedUseAppCheckTokens()` Returns the setting indicating if limited-use App Check tokens are enforced for this function. |

## Public functions

### getLimitedUseAppCheckTokens

```
fun getLimitedUseAppCheckTokens(): Boolean
```

## Public properties

### limitedUseAppCheckTokens

```
val limitedUseAppCheckTokens: Boolean
```

Returns the setting indicating if limited-use App Check tokens are enforced for this function.