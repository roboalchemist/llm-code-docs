# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/ImagenModelFutures.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/ImagenModelFutures.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/java/ImagenModelFutures.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/ImagenModelFutures.md.txt

# ImagenModelFutures

# ImagenModelFutures


```
@PublicPreviewAPI
abstract class ImagenModelFutures
```

<br />

*** ** * ** ***

Wrapper class providing Java compatible methods for [ImagenModel](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/ImagenModel).  

|                                              See also                                               |
|-----------------------------------------------------------------------------------------------------|---|
| [ImagenModel](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/ImagenModel) |   |

## Summary

|                                             ### Public companion functions                                             |
|------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ImagenModelFutures](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/ImagenModelFutures) | [from](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/ImagenModelFutures.Companion#from(com.google.firebase.ai.ImagenModel))`(model: `[ImagenModel](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/ImagenModel)`)` |

|                                                                                                                                                                                        ### Public functions                                                                                                                                                                                         |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `abstract `[ListenableFuture](https://firebase.google.com/docs/reference/kotlin/com/google/common/util/concurrent/ListenableFuture)`<`[ImagenGenerationResponse](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationResponse)`<`[ImagenInlineImage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenInlineImage)`>>` | [editImage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/ImagenModelFutures#editImage(kotlin.collections.List,kotlin.String))`(referenceImages: `[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[ImagenReferenceImage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenReferenceImage)`>, prompt: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`)` Generates an image from a single or set of base images, returning the result directly to the caller.                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `abstract `[ListenableFuture](https://firebase.google.com/docs/reference/kotlin/com/google/common/util/concurrent/ListenableFuture)`<`[ImagenGenerationResponse](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationResponse)`<`[ImagenInlineImage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenInlineImage)`>>` | [editImage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/ImagenModelFutures#editImage(kotlin.collections.List,kotlin.String,com.google.firebase.ai.type.ImagenEditingConfig))`(` ` referenceImages: `[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[ImagenReferenceImage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenReferenceImage)`>,` ` prompt: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`,` ` config: `[ImagenEditingConfig](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenEditingConfig)`?` `)` Generates an image from a single or set of base images, returning the result directly to the caller.                                                                                                                                                                                                                                                   |
| `abstract `[ListenableFuture](https://firebase.google.com/docs/reference/kotlin/com/google/common/util/concurrent/ListenableFuture)`<`[ImagenGenerationResponse](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationResponse)`<`[ImagenInlineImage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenInlineImage)`>>` | [generateImages](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/ImagenModelFutures#generateImages(kotlin.String))`(prompt: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`)` Generates an image, returning the result directly to the caller.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `abstract `[ImagenModel](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/ImagenModel)                                                                                                                                                                                                                                                                                      | [getImageModel](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/ImagenModelFutures#getImageModel())`()` Returns the [ImagenModel](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/ImagenModel) object wrapped by this object.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `abstract `[ListenableFuture](https://firebase.google.com/docs/reference/kotlin/com/google/common/util/concurrent/ListenableFuture)`<`[ImagenGenerationResponse](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationResponse)`<`[ImagenInlineImage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenInlineImage)`>>` | [inpaintImage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/ImagenModelFutures#inpaintImage(com.google.firebase.ai.type.ImagenInlineImage,kotlin.String,com.google.firebase.ai.type.ImagenMaskReference,com.google.firebase.ai.type.ImagenEditingConfig))`(` ` image: `[ImagenInlineImage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenInlineImage)`,` ` prompt: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`,` ` mask: `[ImagenMaskReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenMaskReference)`,` ` config: `[ImagenEditingConfig](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenEditingConfig) `)` Generates an image by inpainting a masked off part of a base image.                                                                                                                                                                                  |
| `abstract `[ListenableFuture](https://firebase.google.com/docs/reference/kotlin/com/google/common/util/concurrent/ListenableFuture)`<`[ImagenGenerationResponse](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationResponse)`<`[ImagenInlineImage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenInlineImage)`>>` | [outpaintImage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/ImagenModelFutures#outpaintImage(com.google.firebase.ai.type.ImagenInlineImage,com.google.firebase.ai.type.Dimensions,com.google.firebase.ai.type.ImagenImagePlacement,kotlin.String,com.google.firebase.ai.type.ImagenEditingConfig))`(` ` image: `[ImagenInlineImage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenInlineImage)`,` ` newDimensions: `[Dimensions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Dimensions)`,` ` newPosition: `[ImagenImagePlacement](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenImagePlacement)`,` ` prompt: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`,` ` config: `[ImagenEditingConfig](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenEditingConfig)`?` `)` Generates an image by outpainting the image, extending its borders |

## Public companion functions

### from

```
funÂ from(model:Â ImagenModel):Â ImagenModelFutures
```  

|                                                        Returns                                                         |
|------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ImagenModelFutures](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/ImagenModelFutures) | a [ImagenModelFutures](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/ImagenModelFutures) created around the provided [ImagenModel](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/ImagenModel) |

## Public functions

### editImage

```
abstractÂ funÂ editImage(referenceImages:Â List<ImagenReferenceImage>,Â prompt:Â String):Â ListenableFuture<ImagenGenerationResponse<ImagenInlineImage>>
```

Generates an image from a single or set of base images, returning the result directly to the caller.  

|                                                                                                                 Parameters                                                                                                                  |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------|
| `referenceImages: `[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[ImagenReferenceImage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenReferenceImage)`>` | the image inputs given to the model as a prompt |
| `prompt: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)                                                                                                                                                  | the text input given to the model as a prompt   |

### editImage

```
abstractÂ funÂ editImage(
Â Â Â Â referenceImages:Â List<ImagenReferenceImage>,
Â Â Â Â prompt:Â String,
Â Â Â Â config:Â ImagenEditingConfig? = null
):Â ListenableFuture<ImagenGenerationResponse<ImagenInlineImage>>
```

Generates an image from a single or set of base images, returning the result directly to the caller.  

|                                                                                                                 Parameters                                                                                                                  |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------|
| `referenceImages: `[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[ImagenReferenceImage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenReferenceImage)`>` | the image inputs given to the model as a prompt |
| `prompt: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)                                                                                                                                                  | the text input given to the model as a prompt   |
| `config: `[ImagenEditingConfig](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenEditingConfig)`? = null`                                                                                                | the editing configuration settings              |

### generateImages

```
abstractÂ funÂ generateImages(prompt:Â String):Â ListenableFuture<ImagenGenerationResponse<ImagenInlineImage>>
```

Generates an image, returning the result directly to the caller.  

|                                         Parameters                                         |
|--------------------------------------------------------------------------------------------|---------------------------------------------------------|
| `prompt: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | The main text prompt from which the image is generated. |

### getImageModel

```
abstractÂ funÂ getImageModel():Â ImagenModel
```

Returns the [ImagenModel](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/ImagenModel) object wrapped by this object.  

### inpaintImage

```
abstractÂ funÂ inpaintImage(
Â Â Â Â image:Â ImagenInlineImage,
Â Â Â Â prompt:Â String,
Â Â Â Â mask:Â ImagenMaskReference,
Â Â Â Â config:Â ImagenEditingConfig
):Â ListenableFuture<ImagenGenerationResponse<ImagenInlineImage>>
```

Generates an image by inpainting a masked off part of a base image.  

|                                                             Parameters                                                             |
|------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `image: `[ImagenInlineImage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenInlineImage)      | the base image                                                                                                                                                          |
| `prompt: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)                                         | the text input given to the model as a prompt                                                                                                                           |
| `mask: `[ImagenMaskReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenMaskReference)   | the mask which defines where in the image can be painted by imagen.                                                                                                     |
| `config: `[ImagenEditingConfig](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenEditingConfig) | the editing configuration settings, it should include an [ImagenEditMode](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenEditMode) |

### outpaintImage

```
abstractÂ funÂ outpaintImage(
Â Â Â Â image:Â ImagenInlineImage,
Â Â Â Â newDimensions:Â Dimensions,
Â Â Â Â newPosition:Â ImagenImagePlacement = ImagenImagePlacement.CENTER,
Â Â Â Â prompt:Â String = "",
Â Â Â Â config:Â ImagenEditingConfig? = null
):Â ListenableFuture<ImagenGenerationResponse<ImagenInlineImage>>
```

Generates an image by outpainting the image, extending its borders  

|                                                                                Parameters                                                                                 |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `image: `[ImagenInlineImage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenInlineImage)                                             | the base image                                                                                                                                                                                                                                                                                             |
| `newDimensions: `[Dimensions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Dimensions)                                                   | the new dimensions for the image, *must* be larger than the original image.                                                                                                                                                                                                                                |
| `newPosition: `[ImagenImagePlacement](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenImagePlacement)` = ImagenImagePlacement.CENTER` | the placement of the base image within the new image. This can either be coordinates (0,0 is the top left corner) or an alignment (ex: [ImagenImagePlacement.BOTTOM_CENTER](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenImagePlacement.Companion#BOTTOM_CENTER())) |
| `prompt: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` = ""`                                                                         | optional, but can be used to specify the background generated if context is insufficient                                                                                                                                                                                                                   |
| `config: `[ImagenEditingConfig](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenEditingConfig)`? = null`                              | the editing configuration settings                                                                                                                                                                                                                                                                         |

|                                                                                                                                                        See also                                                                                                                                                         |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| [generateMaskAndPadForOutpainting](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenMaskReference.Companion#generateMaskAndPadForOutpainting(com.google.firebase.ai.type.ImagenInlineImage,com.google.firebase.ai.type.Dimensions,com.google.firebase.ai.type.ImagenImagePlacement)) |   |