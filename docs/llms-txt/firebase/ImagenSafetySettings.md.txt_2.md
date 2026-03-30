# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenSafetySettings.md.txt

# ImagenSafetySettings

# ImagenSafetySettings


```
public final class ImagenSafetySettings
```

<br />

*** ** * ** ***

A configuration for filtering unsafe content or images containing people.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenSafetySettings#ImagenSafetySettings(com.google.firebase.ai.type.ImagenSafetyFilterLevel,com.google.firebase.ai.type.ImagenPersonFilterLevel)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenSafetyFilterLevel safetyFilterLevel, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenPersonFilterLevel personFilterLevel )` |

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
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenSafetyFilterLevel safetyFilterLevel` | Used to filter unsafe content. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenPersonFilterLevel personFilterLevel` | Used to filter images containing people. |