# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAIKt.md.txt

# FirebaseAIKt

# FirebaseAIKt


```
public final class FirebaseAIKt
```

<br />

*** ** * ** ***

## Summary

| ### Public fields |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/package-summary#(com.google.firebase.Firebase).ai()` The `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI` instance for the default `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` using the Google AI Backend. |

| ### Public methods |
|---|---|
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAIKt.https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAIKt#(com.google.firebase.Firebase).ai(com.google.firebase.FirebaseApp,com.google.firebase.ai.type.GenerativeBackend)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/Firebase receiver, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp app, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerativeBackend backend )` Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI` instance for the provided `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` and `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/package-summary#(com.google.firebase.Firebase).ai(com.google.firebase.FirebaseApp,com.google.firebase.ai.type.GenerativeBackend)`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAIKt.https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAIKt#(com.google.firebase.Firebase).ai(com.google.firebase.FirebaseApp,com.google.firebase.ai.type.GenerativeBackend,kotlin.Boolean)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/Firebase receiver, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp app, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerativeBackend backend, boolean useLimitedUseAppCheckTokens )` Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI` instance for the provided `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` and `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/package-summary#(com.google.firebase.Firebase).ai(com.google.firebase.FirebaseApp,com.google.firebase.ai.type.GenerativeBackend,kotlin.Boolean)`. |

## Public fields

### ai

```
public final @NonNull FirebaseAI ai
```

The `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI` instance for the default `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` using the Google AI Backend.

## Public methods

### FirebaseAIKt.ai

```
public static final @NonNull FirebaseAI FirebaseAIKt.ai(
    @NonNull Firebase receiver,
    @NonNull FirebaseApp app,
    @NonNull GenerativeBackend backend
)
```

Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI` instance for the provided `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` and `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/package-summary#(com.google.firebase.Firebase).ai(com.google.firebase.FirebaseApp,com.google.firebase.ai.type.GenerativeBackend)`.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerativeBackend backend` | the backend reference to make generative AI requests to. |

### FirebaseAIKt.ai

```
public static final @NonNull FirebaseAI FirebaseAIKt.ai(
    @NonNull Firebase receiver,
    @NonNull FirebaseApp app,
    @NonNull GenerativeBackend backend,
    boolean useLimitedUseAppCheckTokens
)
```

Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI` instance for the provided `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` and `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/package-summary#(com.google.firebase.Firebase).ai(com.google.firebase.FirebaseApp,com.google.firebase.ai.type.GenerativeBackend,kotlin.Boolean)`.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerativeBackend backend` | the backend reference to make generative AI requests to. |
| `boolean useLimitedUseAppCheckTokens` | use App Check's limited-use tokens when sending requests to the backend. Learn more about [limited-use tokens](https://firebase.google.com/docs/ai-logic/app-check), including their nuances, when to use them, and best practices for integrating them into your app. |