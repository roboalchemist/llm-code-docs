# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenControlType.md.txt

# ImagenControlType

# ImagenControlType


```
class ImagenControlType
```

<br />

*** ** * ** ***

Represents a control type for controlled Imagen generation/editing

## Summary

| ### Public companion properties |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenControlType` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenControlType.Companion#CANNY()` Use edge detection to ensure the new image follows the same outlines as the reference image. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenControlType` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenControlType.Companion#COLOR_SUPERPIXEL()` Use color superpixels to ensure that the new image is similar in shape and color to the reference image. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenControlType` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenControlType.Companion#FACE_MESH()` Use face mesh control to ensure that the new image has the same facial expressions as the reference image. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenControlType` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenControlType.Companion#SCRIBBLE()` Use enhanced edge detection to ensure the new image follows the same outlines as the reference image. |

## Public companion properties

### CANNY

```
val CANNY: ImagenControlType
```

Use edge detection to ensure the new image follows the same outlines as the reference image.

### COLOR_SUPERPIXEL

```
val COLOR_SUPERPIXEL: ImagenControlType
```

Use color superpixels to ensure that the new image is similar in shape and color to the reference image.

### FACE_MESH

```
val FACE_MESH: ImagenControlType
```

Use face mesh control to ensure that the new image has the same facial expressions as the reference image.

### SCRIBBLE

```
val SCRIBBLE: ImagenControlType
```

Use enhanced edge detection to ensure the new image follows the same outlines as the reference image.