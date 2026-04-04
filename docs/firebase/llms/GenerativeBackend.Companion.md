# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerativeBackend.Companion.md.txt

# GenerativeBackend.Companion


```
public static class GenerativeBackend.Companion
```

<br />

*** ** * ** ***

## Summary

|                                                                                                         ### Public methods                                                                                                         |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[GenerativeBackend](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerativeBackend) | [googleAI](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerativeBackend.Companion#googleAI())`()` References the Google Developer API backend.                                                                                                                                                                                                    |
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[GenerativeBackend](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerativeBackend) | [vertexAI](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerativeBackend.Companion#vertexAI(kotlin.String))`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` location)` References the VertexAI Gemini API backend. |

## Public methods

### googleAI

```
publicÂ staticÂ finalÂ @NonNull GenerativeBackendÂ googleAI()
```

References the Google Developer API backend.  

### vertexAI

```
publicÂ staticÂ finalÂ @NonNull GenerativeBackendÂ vertexAI(@NonNull StringÂ location)
```

References the VertexAI Gemini API backend.  

|                                                                                        Parameters                                                                                         |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` location` | passes a valid cloud server location, defaults to "us-central1" |