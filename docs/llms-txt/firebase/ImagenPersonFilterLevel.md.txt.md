# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenPersonFilterLevel.md.txt

# ImagenPersonFilterLevel

# ImagenPersonFilterLevel


```
public final class ImagenPersonFilterLevel
```

<br />

*** ** * ** ***

A filter used to prevent images from containing depictions of children or people.

## Summary

| ### Nested types |
|---|
| `public static class https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenPersonFilterLevel.Companion` |

| ### Public fields |
|---|---|
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenPersonFilterLevel` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenPersonFilterLevel.Companion#ALLOW_ADULT()` Allow generation of images containing adults only; images of children are filtered out. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenPersonFilterLevel` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenPersonFilterLevel.Companion#ALLOW_ALL()` Allow generation of images containing people of all ages. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenPersonFilterLevel` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenPersonFilterLevel.Companion#BLOCK_ALL()` Disallow generation of images containing people or faces; images of people are filtered out. |

## Public fields

### ALLOW_ADULT

```
public static final @NonNull ImagenPersonFilterLevel ALLOW_ADULT
```

Allow generation of images containing adults only; images of children are filtered out.
> Important: Generation of images containing people or faces may require your use case to be reviewed and approved by Cloud support; see the [Responsible AI and usage guidelines](https://cloud.google.com/vertex-ai/generative-ai/docs/image/responsible-ai-imagen#person-face-gen) for more details.

### ALLOW_ALL

```
public static final @NonNull ImagenPersonFilterLevel ALLOW_ALL
```

Allow generation of images containing people of all ages.
> Important: Generation of images containing people or faces may require your use case to be reviewed and approved by Cloud support; see the [Responsible AI and usage guidelines](https://cloud.google.com/vertex-ai/generative-ai/docs/image/responsible-ai-imagen#person-face-gen) for more details.

### BLOCK_ALL

```
public static final @NonNull ImagenPersonFilterLevel BLOCK_ALL
```

Disallow generation of images containing people or faces; images of people are filtered out.