# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI.Companion.md.txt

# FirebaseAI.Companion

# FirebaseAI.Companion


```
public static class FirebaseAI.Companion
```

<br />

*** ** * ** ***

## Summary

| ### Public fields |
|---|---|
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI.Companion#instance()` The `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI` instance for the default `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` using the Google AI Backend. |

| ### Public methods |
|---|---|
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI.Companion#getInstance(com.google.firebase.FirebaseApp)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp app)` The `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI` instance for the provided `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` using the Google AI Backend. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI.Companion#getInstance(com.google.firebase.FirebaseApp,com.google.firebase.ai.type.GenerativeBackend)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp app, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerativeBackend backend)` Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI` instance for the provided `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` and `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI.Companion#getInstance(com.google.firebase.FirebaseApp,com.google.firebase.ai.type.GenerativeBackend)`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI.Companion#getInstance(com.google.firebase.FirebaseApp,com.google.firebase.ai.type.GenerativeBackend,kotlin.Boolean)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp app, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerativeBackend backend, boolean useLimitedUseAppCheckTokens )` Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI` instance for the provided `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` and `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI.Companion#getInstance(com.google.firebase.FirebaseApp,com.google.firebase.ai.type.GenerativeBackend,kotlin.Boolean)`. |

## Public fields

### instance

```
public static final @NonNull FirebaseAI instance
```

The `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI` instance for the default `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` using the Google AI Backend.

## Public methods

### getInstance

```
public static final @NonNull FirebaseAI getInstance(@NonNull FirebaseApp app)
```

The `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI` instance for the provided `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` using the Google AI Backend.

### getInstance

```
public static final @NonNull FirebaseAI getInstance(@NonNull FirebaseApp app, @NonNull GenerativeBackend backend)
```

Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI` instance for the provided `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` and `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI.Companion#getInstance(com.google.firebase.FirebaseApp,com.google.firebase.ai.type.GenerativeBackend)`.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerativeBackend backend` | the backend reference to make generative AI requests to. |

### getInstance

```
public static final @NonNull FirebaseAI getInstance(
    @NonNull FirebaseApp app,
    @NonNull GenerativeBackend backend,
    boolean useLimitedUseAppCheckTokens
)
```

Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI` instance for the provided `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` and `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI.Companion#getInstance(com.google.firebase.FirebaseApp,com.google.firebase.ai.type.GenerativeBackend,kotlin.Boolean)`.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerativeBackend backend` | the backend reference to make generative AI requests to. |
| `boolean useLimitedUseAppCheckTokens` | when sending tokens to the backend, this option enables the usage of App Check's limited-use tokens instead of the standard cached tokens. Learn more about [limited-use tokens](https://firebase.google.com/docs/ai-logic/app-check), including their nuances, when to use them, and best practices for integrating them into your app. *This flag is set to `false` by default.* |