# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenEditingConfig.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenEditingConfig.md.txt

# ImagenEditingConfig

# ImagenEditingConfig


```
@PublicPreviewAPI
class ImagenEditingConfig
```

<br />

*** ** * ** ***

Contains the editing settings which are not specific to a reference image

## Summary

|                                                                                                                                                                                                   ### Public constructors                                                                                                                                                                                                    |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ImagenEditingConfig](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenEditingConfig#ImagenEditingConfig(com.google.firebase.ai.type.ImagenEditMode,kotlin.Int))`(editMode: `[ImagenEditMode](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenEditMode)`?, editSteps: `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)`?)` |

## Public constructors

### ImagenEditingConfig

```
ImagenEditingConfig(editMode:Â ImagenEditMode? = null,Â editSteps:Â Int? = null)
```  

|                                                              Parameters                                                              |
|--------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| `editMode: `[ImagenEditMode](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenEditMode)`? = null` | holds the editing mode if the request is for inpainting or outpainting |
| `editSteps: `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)`? = null`                                    | the number of intermediate steps to include in the editing process     |