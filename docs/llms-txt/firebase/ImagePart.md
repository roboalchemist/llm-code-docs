# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ImagePart.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ImagePart.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagePart.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagePart.md.txt

# ImagePart

# ImagePart


```
public final class ImagePart implements Part
```

<br />

*** ** * ** ***

Represents image data sent to and received from requests. The image is converted client-side to JPEG encoding at 80% quality before being sent to the server.

## Summary

|                                                                                      ### Public fields                                                                                      |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| `final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Bitmap](https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html) | [image](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagePart#image())         |
| `boolean`                                                                                                                                                                                   | [isThought](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagePart#isThought()) |

|                                                                                                                                                         ### Public constructors                                                                                                                                                         |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ImagePart](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagePart#ImagePart(android.graphics.Bitmap))`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Bitmap](https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html)` image)` |

## Public fields

### image

```
publicÂ finalÂ @NonNull BitmapÂ image
```  

### isThought

```
publicÂ booleanÂ isThought
```  

## Public constructors

### ImagePart

```
publicÂ ImagePart(@NonNull BitmapÂ image)
```  

|                                                                                          Parameters                                                                                           |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Bitmap](https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html)` image` | [Bitmap](https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html) to convert into a [Part](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Part) |