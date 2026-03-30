# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ImagenSafetySettings.md.txt

# ImagenSafetySettings

# ImagenSafetySettings


```
@PublicPreviewAPI
public final class ImagenSafetySettings
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
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ImagenSafetySettings#ImagenSafetySettings(com.google.firebase.vertexai.type.ImagenSafetyFilterLevel,com.google.firebase.vertexai.type.ImagenPersonFilterLevel)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ImagenSafetyFilterLevel safetyFilterLevel, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ImagenPersonFilterLevel personFilterLevel )` |

## Public constructors

### ImagenSafetySettings

```
public ImagenSafetySettings(
    @NonNull ImagenSafetyFilterLevel safetyFilterLevel,
    @NonNull ImagenPersonFilterLevel personFilterLevel
)
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ImagenSafetyFilterLevel safetyFilterLevel` | Used to filter unsafe content. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ImagenPersonFilterLevel personFilterLevel` | Used to filter images containing people. |