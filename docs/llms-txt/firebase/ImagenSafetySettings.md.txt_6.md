# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ImagenSafetySettings.md.txt

# ImagenSafetySettings

# ImagenSafetySettings


```
@PublicPreviewAPI
class ImagenSafetySettings
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

A configuration for filtering unsafe content or images containing people.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ImagenSafetySettings#ImagenSafetySettings(com.google.firebase.vertexai.type.ImagenSafetyFilterLevel,com.google.firebase.vertexai.type.ImagenPersonFilterLevel)( safetyFilterLevel: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ImagenSafetyFilterLevel, personFilterLevel: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ImagenPersonFilterLevel )` |

## Public constructors

### ImagenSafetySettings

```
ImagenSafetySettings(
    safetyFilterLevel: ImagenSafetyFilterLevel,
    personFilterLevel: ImagenPersonFilterLevel
)
```

| Parameters |
|---|---|
| `safetyFilterLevel: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ImagenSafetyFilterLevel` | Used to filter unsafe content. |
| `personFilterLevel: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ImagenPersonFilterLevel` | Used to filter images containing people. |