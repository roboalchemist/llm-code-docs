# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImagePlacement.Companion.md.txt

# ImagenImagePlacement.Companion

# ImagenImagePlacement.Companion


```
public static class ImagenImagePlacement.Companion
```

<br />

*** ** * ** ***

## Summary

|                                                                                                            ### Public methods                                                                                                            |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[ImagenImagePlacement](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImagePlacement) | [fromCoordinate](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImagePlacement.Companion#fromCoordinate(kotlin.Int,kotlin.Int))`(int x, int y)` Creates an [ImagenImagePlacement](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImagePlacement) that represents a placement in an image described by two coordinates. |

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