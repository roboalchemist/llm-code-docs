# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenControlType.md.txt

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

|                                                                        ### Nested types                                                                         |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `public static class `[ImagenControlType.Companion](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenControlType.Companion) |

|                                                                                                         ### Public fields                                                                                                          |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[ImagenControlType](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenControlType) | [CANNY](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenControlType.Companion#CANNY()) Use edge detection to ensure the new image follows the same outlines as the reference image.                                   |
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[ImagenControlType](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenControlType) | [COLOR_SUPERPIXEL](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenControlType.Companion#COLOR_SUPERPIXEL()) Use color superpixels to ensure that the new image is similar in shape and color to the reference image. |
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[ImagenControlType](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenControlType) | [FACE_MESH](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenControlType.Companion#FACE_MESH()) Use face mesh control to ensure that the new image has the same facial expressions as the reference image.             |
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[ImagenControlType](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenControlType) | [SCRIBBLE](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenControlType.Companion#SCRIBBLE()) Use enhanced edge detection to ensure the new image follows the same outlines as the reference image.                    |

## Public fields

### CANNY

```
publicÂ staticÂ finalÂ @NonNull ImagenControlTypeÂ CANNY
```

Use edge detection to ensure the new image follows the same outlines as the reference image.  

### COLOR_SUPERPIXEL

```
publicÂ staticÂ finalÂ @NonNull ImagenControlTypeÂ COLOR_SUPERPIXEL
```

Use color superpixels to ensure that the new image is similar in shape and color to the reference image.  

### FACE_MESH

```
publicÂ staticÂ finalÂ @NonNull ImagenControlTypeÂ FACE_MESH
```

Use face mesh control to ensure that the new image has the same facial expressions as the reference image.  

### SCRIBBLE

```
publicÂ staticÂ finalÂ @NonNull ImagenControlTypeÂ SCRIBBLE
```

Use enhanced edge detection to ensure the new image follows the same outlines as the reference image.