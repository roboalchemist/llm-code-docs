# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/FirebaseVertexAI.Companion.md.txt

# FirebaseVertexAI.Companion

# FirebaseVertexAI.Companion


```
public static class FirebaseVertexAI.Companion
```

<br />

*** ** * ** ***

## Summary

|                                                                                                         ### Public fields                                                                                                         |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseVertexAI](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/FirebaseVertexAI) | [instance](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/FirebaseVertexAI.Companion#instance()) The [FirebaseVertexAI](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/FirebaseVertexAI) instance for the default [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp) |

|                                                                                                        ### Public methods                                                                                                         |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseVertexAI](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/FirebaseVertexAI) | [getInstance](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/FirebaseVertexAI.Companion#getInstance(com.google.firebase.FirebaseApp))`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp)` app)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseVertexAI](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/FirebaseVertexAI) | [getInstance](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/FirebaseVertexAI.Companion#getInstance(com.google.firebase.FirebaseApp,kotlin.String))`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp)` app, @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` location)` Returns the [FirebaseVertexAI](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/FirebaseVertexAI) instance for the provided [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp) and [location](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/FirebaseVertexAI.Companion#getInstance(com.google.firebase.FirebaseApp,kotlin.String)). |

## Public fields

### instance

```
publicÂ staticÂ finalÂ @NonNull FirebaseVertexAIÂ instance
```

The [FirebaseVertexAI](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/FirebaseVertexAI) instance for the default [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp)  

## Public methods

### getInstance

```
publicÂ staticÂ finalÂ @NonNull FirebaseVertexAIÂ getInstance(@NonNull FirebaseAppÂ app)
```  

### getInstance

```
publicÂ staticÂ finalÂ @NonNull FirebaseVertexAIÂ getInstance(@NonNull FirebaseAppÂ app,Â @NonNull StringÂ location)
```

Returns the [FirebaseVertexAI](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/FirebaseVertexAI) instance for the provided [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp) and [location](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/FirebaseVertexAI.Companion#getInstance(com.google.firebase.FirebaseApp,kotlin.String)).  

|                                                                                        Parameters                                                                                         |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` location` | location identifier, defaults to `us-central1`; see available [Vertex AI regions](https://firebase.google.com/docs/vertex-ai/locations?platform=android#available-locations) . |