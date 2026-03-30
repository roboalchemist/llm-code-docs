# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/CustomSignals.Builder.md.txt

# CustomSignals.Builder

# CustomSignals.Builder


```
public class CustomSignals.Builder
```

<br />

*** ** * ** ***

Builder for constructing `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/CustomSignals` instances.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/CustomSignals.Builder#Builder()()` |

| ### Public methods |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/CustomSignals` | `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/CustomSignals.Builder#build()()` Creates a `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/CustomSignals` instance with the added custom signals. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/CustomSignals.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/CustomSignals.Builder#put(java.lang.String,java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key, @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html value)` Adds a custom signal with a value that can be a string or null to the builder. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/CustomSignals.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/CustomSignals.Builder#put(java.lang.String,long)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key, long value)` Adds a custom signal with a long value to the builder. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/CustomSignals.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/CustomSignals.Builder#put(java.lang.String,double)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key, double value)` Adds a custom signal with a double value to the builder. |

## Public constructors

### Builder

```
public Builder()
```

## Public methods

### build

```
public @NonNull CustomSignals build()
```

Creates a `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/CustomSignals` instance with the added custom signals.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/CustomSignals` | The constructed `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/CustomSignals` instance. |

### put

```
public @NonNull CustomSignals.Builder put(@NonNull String key, @Nullable String value)
```

Adds a custom signal with a value that can be a string or null to the builder.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key` | The key for the custom signal. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html value` | The string value associated with the key. Can be null. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/CustomSignals.Builder` | This Builder instance to allow chaining of method calls. |

### put

```
public @NonNull CustomSignals.Builder put(@NonNull String key, long value)
```

Adds a custom signal with a long value to the builder.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key` | The key for the custom signal. |
| `long value` | The long value for the custom signal. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/CustomSignals.Builder` | This Builder instance to allow chaining of method calls. |

### put

```
public @NonNull CustomSignals.Builder put(@NonNull String key, double value)
```

Adds a custom signal with a double value to the builder.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key` | The key for the custom signal. |
| `double value` | The double value for the custom signal. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/CustomSignals.Builder` | This Builder instance to allow chaining of method calls. |