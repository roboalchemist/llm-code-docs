# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableOptions.Builder.md.txt

# HttpsCallableOptions.Builder

# HttpsCallableOptions.Builder


```
class HttpsCallableOptions.Builder
```

<br />

*** ** * ** ***

A builder for creating `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableOptions`.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableOptions.Builder#Builder()()` |

| ### Public functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableOptions` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableOptions.Builder#build()()` Builds a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableOptions`. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableOptions.Builder#getLimitedUseAppCheckTokens()()` Returns the setting indicating if limited-use App Check tokens are enforced. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableOptions.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableOptions.Builder#setLimitedUseAppCheckTokens(kotlin.Boolean)(limitedUse: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` Sets whether or not to use limited-use App Check tokens when invoking the associated function. |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableOptions.Builder#limitedUseAppCheckTokens()` |

## Public constructors

### Builder

```
Builder()
```

## Public functions

### build

```
fun build(): HttpsCallableOptions
```

Builds a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableOptions`.

### getLimitedUseAppCheckTokens

```
fun getLimitedUseAppCheckTokens(): Boolean
```

Returns the setting indicating if limited-use App Check tokens are enforced.

### setLimitedUseAppCheckTokens

```
fun setLimitedUseAppCheckTokens(limitedUse: Boolean): HttpsCallableOptions.Builder
```

Sets whether or not to use limited-use App Check tokens when invoking the associated function.

## Public properties

### limitedUseAppCheckTokens

```
var limitedUseAppCheckTokens: Boolean
```