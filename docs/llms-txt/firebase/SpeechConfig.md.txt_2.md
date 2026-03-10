# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/SpeechConfig.md.txt

# SpeechConfig

# SpeechConfig


```
@PublicPreviewAPI
public final class SpeechConfig
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

Speech configuration class for setting up the voice of the server's response.

## Summary

| ### Public fields |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Voices` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/SpeechConfig#voice()` The voice to be used for the server's speech response. |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/SpeechConfig#SpeechConfig(com.google.firebase.vertexai.type.Voices)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Voices voice)` |

## Public fields

### voice

```
public final @NonNull Voices voice
```

The voice to be used for the server's speech response.

## Public constructors

### SpeechConfig

```
public SpeechConfig(@NonNull Voices voice)
```