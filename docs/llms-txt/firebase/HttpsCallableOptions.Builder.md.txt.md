# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/functions/HttpsCallableOptions.Builder.md.txt

# HttpsCallableOptions.Builder

# HttpsCallableOptions.Builder


```
public final class HttpsCallableOptions.Builder
```

<br />

*** ** * ** ***

A builder for creating `https://firebase.google.com/docs/reference/android/com/google/firebase/functions/HttpsCallableOptions`.

## Summary

| ### Public fields |
|---|---|
| `final boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/functions/HttpsCallableOptions.Builder#limitedUseAppCheckTokens()` |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/functions/HttpsCallableOptions.Builder#Builder()()` |

| ### Public methods |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/functions/HttpsCallableOptions` | `https://firebase.google.com/docs/reference/android/com/google/firebase/functions/HttpsCallableOptions.Builder#build()()` Builds a new `https://firebase.google.com/docs/reference/android/com/google/firebase/functions/HttpsCallableOptions`. |
| `final boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/functions/HttpsCallableOptions.Builder#getLimitedUseAppCheckTokens()()` Returns the setting indicating if limited-use App Check tokens are enforced. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/functions/HttpsCallableOptions.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/functions/HttpsCallableOptions.Builder#setLimitedUseAppCheckTokens(kotlin.Boolean)(boolean limitedUse)` Sets whether or not to use limited-use App Check tokens when invoking the associated function. |

## Public fields

### limitedUseAppCheckTokens

```
public final boolean limitedUseAppCheckTokens
```

## Public constructors

### Builder

```
public Builder()
```

## Public methods

### build

```
public final @NonNull HttpsCallableOptions build()
```

Builds a new `https://firebase.google.com/docs/reference/android/com/google/firebase/functions/HttpsCallableOptions`.

### getLimitedUseAppCheckTokens

```
public final boolean getLimitedUseAppCheckTokens()
```

Returns the setting indicating if limited-use App Check tokens are enforced.

### setLimitedUseAppCheckTokens

```
public final @NonNull HttpsCallableOptions.Builder setLimitedUseAppCheckTokens(boolean limitedUse)
```

Sets whether or not to use limited-use App Check tokens when invoking the associated function.