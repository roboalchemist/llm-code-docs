# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableOptions.Builder.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/functions/HttpsCallableOptions.Builder.md.txt

# HttpsCallableOptions.Builder

# HttpsCallableOptions.Builder


```
public final class HttpsCallableOptions.Builder
```

<br />

*** ** * ** ***

A builder for creating [com.google.firebase.functions.HttpsCallableOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/functions/HttpsCallableOptions).

## Summary

| ### Public fields |
|-------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `final boolean`   | [limitedUseAppCheckTokens](https://firebase.google.com/docs/reference/android/com/google/firebase/functions/HttpsCallableOptions.Builder#limitedUseAppCheckTokens()) |

|                                                        ### Public constructors                                                         |
|----------------------------------------------------------------------------------------------------------------------------------------|
| [Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/functions/HttpsCallableOptions.Builder#Builder())`()` |

|                                                                                                                 ### Public methods                                                                                                                  |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[HttpsCallableOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/functions/HttpsCallableOptions)                 | [build](https://firebase.google.com/docs/reference/android/com/google/firebase/functions/HttpsCallableOptions.Builder#build())`()` Builds a new [com.google.firebase.functions.HttpsCallableOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/functions/HttpsCallableOptions).  |
| `final boolean`                                                                                                                                                                                                                                     | [getLimitedUseAppCheckTokens](https://firebase.google.com/docs/reference/android/com/google/firebase/functions/HttpsCallableOptions.Builder#getLimitedUseAppCheckTokens())`()` Returns the setting indicating if limited-use App Check tokens are enforced.                                                   |
| `final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[HttpsCallableOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/functions/HttpsCallableOptions.Builder) | [setLimitedUseAppCheckTokens](https://firebase.google.com/docs/reference/android/com/google/firebase/functions/HttpsCallableOptions.Builder#setLimitedUseAppCheckTokens(kotlin.Boolean))`(boolean limitedUse)` Sets whether or not to use limited-use App Check tokens when invoking the associated function. |

## Public fields

### limitedUseAppCheckTokens

```
publicÂ finalÂ booleanÂ limitedUseAppCheckTokens
```  

## Public constructors

### Builder

```
publicÂ Builder()
```  

## Public methods

### build

```
publicÂ finalÂ @NonNull HttpsCallableOptionsÂ build()
```

Builds a new [com.google.firebase.functions.HttpsCallableOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/functions/HttpsCallableOptions).  

### getLimitedUseAppCheckTokens

```
publicÂ finalÂ booleanÂ getLimitedUseAppCheckTokens()
```

Returns the setting indicating if limited-use App Check tokens are enforced.  

### setLimitedUseAppCheckTokens

```
publicÂ finalÂ @NonNull HttpsCallableOptions.BuilderÂ setLimitedUseAppCheckTokens(booleanÂ limitedUse)
```

Sets whether or not to use limited-use App Check tokens when invoking the associated function.