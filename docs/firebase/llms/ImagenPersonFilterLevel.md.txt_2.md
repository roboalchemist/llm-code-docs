# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ImagenPersonFilterLevel.md.txt

# ImagenPersonFilterLevel

# ImagenPersonFilterLevel


```
@PublicPreviewAPI
public final class ImagenPersonFilterLevel
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

A filter used to prevent images from containing depictions of children or people.

## Summary

| ### Nested types |
|---|
| `public static class https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ImagenPersonFilterLevel.Companion` |

| ### Public fields |
|---|---|
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ImagenPersonFilterLevel` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ImagenPersonFilterLevel.Companion#ALLOW_ADULT()` Filters out any images containing depictions of children. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ImagenPersonFilterLevel` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ImagenPersonFilterLevel.Companion#ALLOW_ALL()` No filters applied. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ImagenPersonFilterLevel` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ImagenPersonFilterLevel.Companion#BLOCK_ALL()` Filters out any images containing depictions of people. |

## Public fields

### ALLOW_ADULT

```
public static final @NonNull ImagenPersonFilterLevel ALLOW_ADULT
```

Filters out any images containing depictions of children.

### ALLOW_ALL

```
public static final @NonNull ImagenPersonFilterLevel ALLOW_ALL
```

No filters applied.

### BLOCK_ALL

```
public static final @NonNull ImagenPersonFilterLevel BLOCK_ALL
```

Filters out any images containing depictions of people.