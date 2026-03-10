# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenImagePlacement.md.txt

# ImagenImagePlacement

# ImagenImagePlacement


```
class ImagenImagePlacement
```

<br />

*** ** * ** ***

Represents where the placement of an image is within a new, larger image, usually in the context of an outpainting request.

## Summary

| ### Public companion functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenImagePlacement` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenImagePlacement.Companion#fromCoordinate(kotlin.Int,kotlin.Int)(x: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, y: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Creates an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenImagePlacement` that represents a placement in an image described by two coordinates. |

| ### Public companion properties |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenImagePlacement` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenImagePlacement.Companion#BOTTOM_CENTER()` Center the image horizontally and aligned with the bottom edge of the larger image |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenImagePlacement` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenImagePlacement.Companion#BOTTOM_LEFT()` Align the image with the bottom left corner of the larger image |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenImagePlacement` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenImagePlacement.Companion#BOTTOM_RIGHT()` Align the image with the bottom right corner of the larger image |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenImagePlacement` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenImagePlacement.Companion#CENTER()` Center the image horizontally and vertically within the larger image |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenImagePlacement` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenImagePlacement.Companion#LEFT_CENTER()` Center the image vertically and aligned with the left edge of the larger image |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenImagePlacement` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenImagePlacement.Companion#RIGHT_CENTER()` Center the image vertically and aligned with the right edge of the larger image |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenImagePlacement` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenImagePlacement.Companion#TOP_CENTER()` Center the image horizontally and aligned with the top edge of the larger image |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenImagePlacement` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenImagePlacement.Companion#TOP_LEFT()` Align the image with the top left corner of the larger image |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenImagePlacement` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenImagePlacement.Companion#TOP_RIGHT()` Align the image with the top right corner of the larger image |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenImagePlacement#x()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenImagePlacement#y()` |

## Public companion functions

### fromCoordinate

```
fun fromCoordinate(x: Int, y: Int): ImagenImagePlacement
```

Creates an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenImagePlacement` that represents a placement in an image described by two coordinates. The coordinate system has 0,0 in the top left corner, and the x and y coordinates represent the location of the top left corner of the original image.

| Parameters |
|---|---|
| `x: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | the x coordinate of the top left corner of the original image |
| `y: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | the y coordinate of the top left corner of the original image |

## Public companion properties

### BOTTOM_CENTER

```
val BOTTOM_CENTER: ImagenImagePlacement
```

Center the image horizontally and aligned with the bottom edge of the larger image

### BOTTOM_LEFT

```
val BOTTOM_LEFT: ImagenImagePlacement
```

Align the image with the bottom left corner of the larger image

### BOTTOM_RIGHT

```
val BOTTOM_RIGHT: ImagenImagePlacement
```

Align the image with the bottom right corner of the larger image

### CENTER

```
val CENTER: ImagenImagePlacement
```

Center the image horizontally and vertically within the larger image

### LEFT_CENTER

```
val LEFT_CENTER: ImagenImagePlacement
```

Center the image vertically and aligned with the left edge of the larger image

### RIGHT_CENTER

```
val RIGHT_CENTER: ImagenImagePlacement
```

Center the image vertically and aligned with the right edge of the larger image

### TOP_CENTER

```
val TOP_CENTER: ImagenImagePlacement
```

Center the image horizontally and aligned with the top edge of the larger image

### TOP_LEFT

```
val TOP_LEFT: ImagenImagePlacement
```

Align the image with the top left corner of the larger image

### TOP_RIGHT

```
val TOP_RIGHT: ImagenImagePlacement
```

Align the image with the top right corner of the larger image

## Public properties

### x

```
val x: Int?
```

### y

```
val y: Int?
```