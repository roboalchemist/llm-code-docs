# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/SpeechConfig.md.txt

# SpeechConfig

# SpeechConfig


```
@PublicPreviewAPI
class SpeechConfig
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

Speech configuration class for setting up the voice of the server's response.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/SpeechConfig#SpeechConfig(com.google.firebase.vertexai.type.Voices)(voice: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Voices)` |

| ### Public properties |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Voices` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/SpeechConfig#voice()` The voice to be used for the server's speech response. |

## Public constructors

### SpeechConfig

```
SpeechConfig(voice: Voices)
```

## Public properties

### voice

```
val voice: Voices
```

The voice to be used for the server's speech response.