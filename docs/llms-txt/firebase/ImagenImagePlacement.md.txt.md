# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImagePlacement.md.txt

# ImagenImagePlacement

# ImagenImagePlacement


```
public final class ImagenImagePlacement
```

<br />

*** ** * ** ***

Represents where the placement of an image is within a new, larger image, usually in the context of an outpainting request.

## Summary

| ### Nested types |
|---|
| `public static class https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImagePlacement.Companion` |

| ### Public fields |
|---|---|
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImagePlacement` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImagePlacement.Companion#BOTTOM_CENTER()` Center the image horizontally and aligned with the bottom edge of the larger image |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImagePlacement` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImagePlacement.Companion#BOTTOM_LEFT()` Align the image with the bottom left corner of the larger image |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImagePlacement` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImagePlacement.Companion#BOTTOM_RIGHT()` Align the image with the bottom right corner of the larger image |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImagePlacement` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImagePlacement.Companion#CENTER()` Center the image horizontally and vertically within the larger image |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImagePlacement` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImagePlacement.Companion#LEFT_CENTER()` Center the image vertically and aligned with the left edge of the larger image |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImagePlacement` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImagePlacement.Companion#RIGHT_CENTER()` Center the image vertically and aligned with the right edge of the larger image |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImagePlacement` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImagePlacement.Companion#TOP_CENTER()` Center the image horizontally and aligned with the top edge of the larger image |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImagePlacement` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImagePlacement.Companion#TOP_LEFT()` Align the image with the top left corner of the larger image |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImagePlacement` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImagePlacement.Companion#TOP_RIGHT()` Align the image with the top right corner of the larger image |
| `final https://developer.android.com/reference/kotlin/java/lang/Integer.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImagePlacement#x()` |
| `final https://developer.android.com/reference/kotlin/java/lang/Integer.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImagePlacement#y()` |

| ### Public methods |
|---|---|
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImagePlacement` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImagePlacement.Companion#fromCoordinate(kotlin.Int,kotlin.Int)(int x, int y)` Creates an `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImagePlacement` that represents a placement in an image described by two coordinates. |

## Public fields

### BOTTOM_CENTER

```
public static final @NonNull ImagenImagePlacement BOTTOM_CENTER
```

Center the image horizontally and aligned with the bottom edge of the larger image

### BOTTOM_LEFT

```
public static final @NonNull ImagenImagePlacement BOTTOM_LEFT
```

Align the image with the bottom left corner of the larger image

### BOTTOM_RIGHT

```
public static final @NonNull ImagenImagePlacement BOTTOM_RIGHT
```

Align the image with the bottom right corner of the larger image

### CENTER

```
public static final @NonNull ImagenImagePlacement CENTER
```

Center the image horizontally and vertically within the larger image

### LEFT_CENTER

```
public static final @NonNull ImagenImagePlacement LEFT_CENTER
```

Center the image vertically and aligned with the left edge of the larger image

### RIGHT_CENTER

```
public static final @NonNull ImagenImagePlacement RIGHT_CENTER
```

Center the image vertically and aligned with the right edge of the larger image

### TOP_CENTER

```
public static final @NonNull ImagenImagePlacement TOP_CENTER
```

Center the image horizontally and aligned with the top edge of the larger image

### TOP_LEFT

```
public static final @NonNull ImagenImagePlacement TOP_LEFT
```

Align the image with the top left corner of the larger image

### TOP_RIGHT

```
public static final @NonNull ImagenImagePlacement TOP_RIGHT
```

Align the image with the top right corner of the larger image

### x

```
public final Integer x
```

### y

```
public final Integer y
```

## Public methods

### fromCoordinate

```
public static final @NonNull ImagenImagePlacement fromCoordinate(int x, int y)
```

Creates an `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImagePlacement` that represents a placement in an image described by two coordinates. The coordinate system has 0,0 in the top left corner, and the x and y coordinates represent the location of the top left corner of the original image.

| Parameters |
|---|---|
| `int x` | the x coordinate of the top left corner of the original image |
| `int y` | the y coordinate of the top left corner of the original image |