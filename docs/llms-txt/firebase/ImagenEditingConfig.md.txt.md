# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenEditingConfig.md.txt

# ImagenEditingConfig

# ImagenEditingConfig


```
@PublicPreviewAPI
public final class ImagenEditingConfig
```

<br />

*** ** * ** ***

Contains the editing settings which are not specific to a reference image

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenEditingConfig#ImagenEditingConfig(com.google.firebase.ai.type.ImagenEditMode,kotlin.Int)(https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenEditMode editMode, https://developer.android.com/reference/kotlin/java/lang/Integer.html editSteps)` |

## Public constructors

### ImagenEditingConfig

```
public ImagenEditingConfig(ImagenEditMode editMode, Integer editSteps)
```

| Parameters |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenEditMode editMode` | holds the editing mode if the request is for inpainting or outpainting |
| `https://developer.android.com/reference/kotlin/java/lang/Integer.html editSteps` | the number of intermediate steps to include in the editing process |