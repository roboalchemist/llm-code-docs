# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/ImageData.md.txt

# ImageData

# ImageData


```
public class ImageData
```

<br />

*** ** * ** ***

Encapsulates an image to be displayed within a Firebase In App Message.

## Summary

| ### Public fields |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/ImageData#bitmapData()` |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/ImageData#imageUrl()` !!!!!WARNING!!!!! We are overriding equality in this class. |

| ### Public methods |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/ImageData#getBitmapData()()` Gets the bitmap associated with this image |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/ImageData#getImageUrl()()` Gets the URL associated with this image |

## Public fields

### bitmapData

```
public final @Nullable Bitmap bitmapData
```

### imageUrl

```
public final @NonNull String imageUrl
```

!!!!!WARNING!!!!! We are overriding equality in this class. Please add equality checks for all new private class members.

## Public methods

### getBitmapData

```
public @Nullable Bitmap getBitmapData()
```

Gets the bitmap associated with this image

### getImageUrl

```
public @NonNull String getImageUrl()
```

Gets the URL associated with this image