# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAIKt.md.txt

# FirebaseAIKt


```
public final class FirebaseAIKt
```

<br />

*** ** * ** ***

## Summary

|                                                                                            ### Public fields                                                                                             |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseAI](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI) | [ai](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/package-summary#(com.google.firebase.Firebase).ai()) The [FirebaseAI](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI) instance for the default [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp) using the Google AI Backend. |

|                                                                                               ### Public methods                                                                                                |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseAI](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI) | [FirebaseAIKt](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAIKt)`.`[ai](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAIKt#(com.google.firebase.Firebase).ai(com.google.firebase.FirebaseApp,com.google.firebase.ai.type.GenerativeBackend))`(` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Firebase](https://firebase.google.com/docs/reference/android/com/google/firebase/Firebase)` receiver,` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp)` app,` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[GenerativeBackend](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerativeBackend)` backend` `)` Returns the [FirebaseAI](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI) instance for the provided [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp) and [backend](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/package-summary#(com.google.firebase.Firebase).ai(com.google.firebase.FirebaseApp,com.google.firebase.ai.type.GenerativeBackend)).                                                                       |
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseAI](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI) | [FirebaseAIKt](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAIKt)`.`[ai](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAIKt#(com.google.firebase.Firebase).ai(com.google.firebase.FirebaseApp,com.google.firebase.ai.type.GenerativeBackend,kotlin.Boolean))`(` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Firebase](https://firebase.google.com/docs/reference/android/com/google/firebase/Firebase)` receiver,` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp)` app,` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[GenerativeBackend](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerativeBackend)` backend,` ` boolean useLimitedUseAppCheckTokens` `)` Returns the [FirebaseAI](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI) instance for the provided [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp) and [backend](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/package-summary#(com.google.firebase.Firebase).ai(com.google.firebase.FirebaseApp,com.google.firebase.ai.type.GenerativeBackend,kotlin.Boolean)). |

## Public fields

### ai

```
publicÂ finalÂ @NonNull FirebaseAIÂ ai
```

The [FirebaseAI](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI) instance for the default [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp) using the Google AI Backend.  

## Public methods

### FirebaseAIKt.ai

```
publicÂ staticÂ finalÂ @NonNull FirebaseAIÂ FirebaseAIKt.ai(
Â Â Â Â @NonNull FirebaseÂ receiver,
Â Â Â Â @NonNull FirebaseAppÂ app,
Â Â Â Â @NonNull GenerativeBackendÂ backend
)
```

Returns the [FirebaseAI](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI) instance for the provided [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp) and [backend](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/package-summary#(com.google.firebase.Firebase).ai(com.google.firebase.FirebaseApp,com.google.firebase.ai.type.GenerativeBackend)).  

|                                                                                                           Parameters                                                                                                            |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[GenerativeBackend](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerativeBackend)` backend` | the backend reference to make generative AI requests to. |

### FirebaseAIKt.ai

```
publicÂ staticÂ finalÂ @NonNull FirebaseAIÂ FirebaseAIKt.ai(
Â Â Â Â @NonNull FirebaseÂ receiver,
Â Â Â Â @NonNull FirebaseAppÂ app,
Â Â Â Â @NonNull GenerativeBackendÂ backend,
Â Â Â Â booleanÂ useLimitedUseAppCheckTokens
)
```

Returns the [FirebaseAI](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI) instance for the provided [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp) and [backend](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/package-summary#(com.google.firebase.Firebase).ai(com.google.firebase.FirebaseApp,com.google.firebase.ai.type.GenerativeBackend,kotlin.Boolean)).  

|                                                                                                           Parameters                                                                                                            |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[GenerativeBackend](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerativeBackend)` backend` | the backend reference to make generative AI requests to.                                                                                                                                                                                                               |
| `boolean useLimitedUseAppCheckTokens`                                                                                                                                                                                           | use App Check's limited-use tokens when sending requests to the backend. Learn more about [limited-use tokens](https://firebase.google.com/docs/ai-logic/app-check), including their nuances, when to use them, and best practices for integrating them into your app. |