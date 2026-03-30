# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenControlType.md.txt

# ImagenControlType

# ImagenControlType


```
public final class ImagenControlType
```

<br />

*** ** * ** ***

Represents a control type for controlled Imagen generation/editing

## Summary

| ### Nested types |
|---|
| `public static class https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenControlType.Companion` |

| ### Public fields |
|---|---|
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenControlType` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenControlType.Companion#CANNY()` Use edge detection to ensure the new image follows the same outlines as the reference image. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenControlType` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenControlType.Companion#COLOR_SUPERPIXEL()` Use color superpixels to ensure that the new image is similar in shape and color to the reference image. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenControlType` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenControlType.Companion#FACE_MESH()` Use face mesh control to ensure that the new image has the same facial expressions as the reference image. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenControlType` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenControlType.Companion#SCRIBBLE()` Use enhanced edge detection to ensure the new image follows the same outlines as the reference image. |

## Public fields

### CANNY

```
public static final @NonNull ImagenControlType CANNY
```

Use edge detection to ensure the new image follows the same outlines as the reference image.

### COLOR_SUPERPIXEL

```
public static final @NonNull ImagenControlType COLOR_SUPERPIXEL
```

Use color superpixels to ensure that the new image is similar in shape and color to the reference image.

### FACE_MESH

```
public static final @NonNull ImagenControlType FACE_MESH
```

Use face mesh control to ensure that the new image has the same facial expressions as the reference image.

### SCRIBBLE

```
public static final @NonNull ImagenControlType SCRIBBLE
```

Use enhanced edge detection to ensure the new image follows the same outlines as the reference image.