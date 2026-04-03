# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/functions/HttpsCallableOptions.md.txt

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

|                                                                                                                                                            ### Nested types                                                                                                                                                             |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `class `[HttpsCallableOptions.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableOptions.Builder) A builder for creating [com.google.firebase.functions.HttpsCallableOptions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableOptions). |

|                                ### Public functions                                |
|------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | [getLimitedUseAppCheckTokens](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableOptions#getLimitedUseAppCheckTokens())`()` |

|                               ### Public properties                                |
|------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | [limitedUseAppCheckTokens](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableOptions#limitedUseAppCheckTokens()) Returns the setting indicating if limited-use App Check tokens are enforced for this function. |

## Public functions

### getLimitedUseAppCheckTokens

```
funÂ getLimitedUseAppCheckTokens():Â Boolean
```  

## Public properties

### limitedUseAppCheckTokens

```
valÂ limitedUseAppCheckTokens:Â Boolean
```

Returns the setting indicating if limited-use App Check tokens are enforced for this function.