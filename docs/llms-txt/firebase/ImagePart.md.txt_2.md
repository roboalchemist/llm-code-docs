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

| ### Public fields |
|---|---|
| `final https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagePart#displayName()` |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagePart#image()` |
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagePart#isThought()` |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagePart#ImagePart(android.graphics.Bitmap)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html image)` |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagePart#ImagePart(android.graphics.Bitmap,kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html image, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html displayName)` |

## Public fields

### displayName

```
public final String displayName
```

### image

```
public final @NonNull Bitmap image
```

### isThought

```
public boolean isThought
```

## Public constructors

### ImagePart

```
public ImagePart(@NonNull Bitmap image)
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html image` | `https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html` to convert into a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Part` |

### ImagePart

```
public ImagePart(@NonNull Bitmap image, @NonNull String displayName)
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html image` | `https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html` to convert into a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Part` |