# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenImagePlacement.md.txt

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

|                                                                           ### Nested types                                                                            |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `public static class `[ImagenImagePlacement.Companion](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImagePlacement.Companion) |

|                                                                                                            ### Public fields                                                                                                             |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[ImagenImagePlacement](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImagePlacement) | [BOTTOM_CENTER](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImagePlacement.Companion#BOTTOM_CENTER()) Center the image horizontally and aligned with the bottom edge of the larger image |
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[ImagenImagePlacement](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImagePlacement) | [BOTTOM_LEFT](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImagePlacement.Companion#BOTTOM_LEFT()) Align the image with the bottom left corner of the larger image                        |
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[ImagenImagePlacement](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImagePlacement) | [BOTTOM_RIGHT](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImagePlacement.Companion#BOTTOM_RIGHT()) Align the image with the bottom right corner of the larger image                     |
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[ImagenImagePlacement](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImagePlacement) | [CENTER](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImagePlacement.Companion#CENTER()) Center the image horizontally and vertically within the larger image                             |
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[ImagenImagePlacement](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImagePlacement) | [LEFT_CENTER](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImagePlacement.Companion#LEFT_CENTER()) Center the image vertically and aligned with the left edge of the larger image         |
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[ImagenImagePlacement](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImagePlacement) | [RIGHT_CENTER](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImagePlacement.Companion#RIGHT_CENTER()) Center the image vertically and aligned with the right edge of the larger image      |
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[ImagenImagePlacement](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImagePlacement) | [TOP_CENTER](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImagePlacement.Companion#TOP_CENTER()) Center the image horizontally and aligned with the top edge of the larger image          |
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[ImagenImagePlacement](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImagePlacement) | [TOP_LEFT](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImagePlacement.Companion#TOP_LEFT()) Align the image with the top left corner of the larger image                                 |
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[ImagenImagePlacement](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImagePlacement) | [TOP_RIGHT](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImagePlacement.Companion#TOP_RIGHT()) Align the image with the top right corner of the larger image                              |
| `final `[Integer](https://developer.android.com/reference/kotlin/java/lang/Integer.html)                                                                                                                                                 | [x](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImagePlacement#x())                                                                                                                      |
| `final `[Integer](https://developer.android.com/reference/kotlin/java/lang/Integer.html)                                                                                                                                                 | [y](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImagePlacement#y())                                                                                                                      |

|                                                                                                            ### Public methods                                                                                                            |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[ImagenImagePlacement](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImagePlacement) | [fromCoordinate](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImagePlacement.Companion#fromCoordinate(kotlin.Int,kotlin.Int))`(int x, int y)` Creates an [ImagenImagePlacement](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImagePlacement) that represents a placement in an image described by two coordinates. |

## Public fields

### BOTTOM_CENTER

```
publicÂ staticÂ finalÂ @NonNull ImagenImagePlacementÂ BOTTOM_CENTER
```

Center the image horizontally and aligned with the bottom edge of the larger image  

### BOTTOM_LEFT

```
publicÂ staticÂ finalÂ @NonNull ImagenImagePlacementÂ BOTTOM_LEFT
```

Align the image with the bottom left corner of the larger image  

### BOTTOM_RIGHT

```
publicÂ staticÂ finalÂ @NonNull ImagenImagePlacementÂ BOTTOM_RIGHT
```

Align the image with the bottom right corner of the larger image  

### CENTER

```
publicÂ staticÂ finalÂ @NonNull ImagenImagePlacementÂ CENTER
```

Center the image horizontally and vertically within the larger image  

### LEFT_CENTER

```
publicÂ staticÂ finalÂ @NonNull ImagenImagePlacementÂ LEFT_CENTER
```

Center the image vertically and aligned with the left edge of the larger image  

### RIGHT_CENTER

```
publicÂ staticÂ finalÂ @NonNull ImagenImagePlacementÂ RIGHT_CENTER
```

Center the image vertically and aligned with the right edge of the larger image  

### TOP_CENTER

```
publicÂ staticÂ finalÂ @NonNull ImagenImagePlacementÂ TOP_CENTER
```

Center the image horizontally and aligned with the top edge of the larger image  

### TOP_LEFT

```
publicÂ staticÂ finalÂ @NonNull ImagenImagePlacementÂ TOP_LEFT
```

Align the image with the top left corner of the larger image  

### TOP_RIGHT

```
publicÂ staticÂ finalÂ @NonNull ImagenImagePlacementÂ TOP_RIGHT
```

Align the image with the top right corner of the larger image  

### x

```
publicÂ finalÂ IntegerÂ x
```  

### y

```
publicÂ finalÂ IntegerÂ y
```  

## Public methods

### fromCoordinate

```
publicÂ staticÂ finalÂ @NonNull ImagenImagePlacementÂ fromCoordinate(intÂ x,Â intÂ y)
```

Creates an [ImagenImagePlacement](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImagePlacement) that represents a placement in an image described by two coordinates. The coordinate system has 0,0 in the top left corner, and the x and y coordinates represent the location of the top left corner of the original image.  

| Parameters |
|------------|---------------------------------------------------------------|
| `int x`    | the x coordinate of the top left corner of the original image |
| `int y`    | the y coordinate of the top left corner of the original image |