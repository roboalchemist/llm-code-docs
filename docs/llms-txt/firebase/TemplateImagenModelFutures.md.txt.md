# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/TemplateImagenModelFutures.md.txt

# TemplateImagenModelFutures

# TemplateImagenModelFutures


```
public abstract class TemplateImagenModelFutures
```

<br />

*** ** * ** ***

Wrapper class providing Java compatible methods for `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/TemplateImagenModel`.

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/TemplateImagenModel` |   |

## Summary

| ### Nested types |
|---|
| `public static class https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/TemplateImagenModelFutures.Companion` |

| ### Public methods |
|---|---|
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/TemplateImagenModelFutures` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/TemplateImagenModelFutures.Companion#from(com.google.firebase.ai.TemplateImagenModel)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/TemplateImagenModel model)` |
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/common/util/concurrent/ListenableFuture<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenGenerationResponse<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenInlineImage>>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/TemplateImagenModelFutures#generateImages(kotlin.String,kotlin.collections.Map)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html templateId, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/Map.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html> inputs )` Generates an image, returning the result directly to the caller. |
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/TemplateImagenModel` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/TemplateImagenModelFutures#getImageModel()()` Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/TemplateImagenModel` object wrapped by this object. |

## Public methods

### from

```
public static final @NonNull TemplateImagenModelFutures from(@NonNull TemplateImagenModel model)
```

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/TemplateImagenModelFutures` | a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/TemplateImagenModelFutures` created around the provided `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/TemplateImagenModel` |

### generateImages

```
public abstract @NonNull ListenableFuture<@NonNull ImagenGenerationResponse<@NonNull ImagenInlineImage>> generateImages(
    @NonNull String templateId,
    @NonNull Map<@NonNull String, @NonNull Object> inputs
)
```

Generates an image, returning the result directly to the caller.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html templateId` | The ID of server prompt template. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/Map.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html> inputs` | the inputs needed to fill in the prompt |

### getImageModel

```
public abstract @NonNull TemplateImagenModel getImageModel()
```

Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/TemplateImagenModel` object wrapped by this object.