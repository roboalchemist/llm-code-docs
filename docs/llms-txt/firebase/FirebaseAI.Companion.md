# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI.Companion.md.txt

# FirebaseAI.Companion


```
public static class FirebaseAI.Companion
```

<br />

*** ** * ** ***

## Summary

|                                                                                                ### Public fields                                                                                                |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseAI](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI) | [instance](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI.Companion#instance()) The [FirebaseAI](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI) instance for the default [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp) using the Google AI Backend. |

|                                                                                               ### Public methods                                                                                                |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseAI](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI) | [getInstance](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI.Companion#getInstance(com.google.firebase.FirebaseApp))`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp)` app)` The [FirebaseAI](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI) instance for the provided [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp) using the Google AI Backend.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseAI](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI) | [getInstance](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI.Companion#getInstance(com.google.firebase.FirebaseApp,com.google.firebase.ai.type.GenerativeBackend))`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp)` app, @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[GenerativeBackend](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerativeBackend)` backend)` Returns the [FirebaseAI](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI) instance for the provided [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp) and [backend](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI.Companion#getInstance(com.google.firebase.FirebaseApp,com.google.firebase.ai.type.GenerativeBackend)).                                                                                 |
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseAI](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI) | [getInstance](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI.Companion#getInstance(com.google.firebase.FirebaseApp,com.google.firebase.ai.type.GenerativeBackend,kotlin.Boolean))`(` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp)` app,` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[GenerativeBackend](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerativeBackend)` backend,` ` boolean useLimitedUseAppCheckTokens` `)` Returns the [FirebaseAI](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI) instance for the provided [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp) and [backend](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI.Companion#getInstance(com.google.firebase.FirebaseApp,com.google.firebase.ai.type.GenerativeBackend,kotlin.Boolean)). |

## Public fields

### instance

```
publicÂ staticÂ finalÂ @NonNull FirebaseAIÂ instance
```

The [FirebaseAI](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI) instance for the default [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp) using the Google AI Backend.  

## Public methods

### getInstance

```
publicÂ staticÂ finalÂ @NonNull FirebaseAIÂ getInstance(@NonNull FirebaseAppÂ app)
```

The [FirebaseAI](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI) instance for the provided [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp) using the Google AI Backend.  

### getInstance

```
publicÂ staticÂ finalÂ @NonNull FirebaseAIÂ getInstance(@NonNull FirebaseAppÂ app,Â @NonNull GenerativeBackendÂ backend)
```

Returns the [FirebaseAI](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI) instance for the provided [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp) and [backend](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI.Companion#getInstance(com.google.firebase.FirebaseApp,com.google.firebase.ai.type.GenerativeBackend)).  

|                                                                                                           Parameters                                                                                                            |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[GenerativeBackend](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerativeBackend)` backend` | the backend reference to make generative AI requests to. |

### getInstance

```
publicÂ staticÂ finalÂ @NonNull FirebaseAIÂ getInstance(
Â Â Â Â @NonNull FirebaseAppÂ app,
Â Â Â Â @NonNull GenerativeBackendÂ backend,
Â Â Â Â booleanÂ useLimitedUseAppCheckTokens
)
```

Returns the [FirebaseAI](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI) instance for the provided [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp) and [backend](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI.Companion#getInstance(com.google.firebase.FirebaseApp,com.google.firebase.ai.type.GenerativeBackend,kotlin.Boolean)).  

|                                                                                                           Parameters                                                                                                            |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[GenerativeBackend](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerativeBackend)` backend` | the backend reference to make generative AI requests to.                                                                                                                                                                                                                                                                                                                           |
| `boolean useLimitedUseAppCheckTokens`                                                                                                                                                                                           | when sending tokens to the backend, this option enables the usage of App Check's limited-use tokens instead of the standard cached tokens. Learn more about [limited-use tokens](https://firebase.google.com/docs/ai-logic/app-check), including their nuances, when to use them, and best practices for integrating them into your app. *This flag is set to `false` by default.* |