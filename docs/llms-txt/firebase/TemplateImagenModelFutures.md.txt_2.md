# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/TemplateImagenModelFutures.md.txt

# TemplateImagenModelFutures

# TemplateImagenModelFutures


```
abstract class TemplateImagenModelFutures
```

<br />

*** ** * ** ***

Wrapper class providing Java compatible methods for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/TemplateImagenModel`.

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/TemplateImagenModel` |   |

## Summary

| ### Public companion functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/TemplateImagenModelFutures` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/TemplateImagenModelFutures.Companion#from(com.google.firebase.ai.TemplateImagenModel)(model: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/TemplateImagenModel)` |

| ### Public functions |
|---|---|
| `abstract https://firebase.google.com/docs/reference/kotlin/com/google/common/util/concurrent/ListenableFuture<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationResponse<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenInlineImage>>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/TemplateImagenModelFutures#generateImages(kotlin.String,kotlin.collections.Map)(templateId: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, inputs: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html>)` Generates an image, returning the result directly to the caller. |
| `abstract https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/TemplateImagenModel` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/TemplateImagenModelFutures#getImageModel()()` Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/TemplateImagenModel` object wrapped by this object. |

## Public companion functions

### from

```
fun from(model: TemplateImagenModel): TemplateImagenModelFutures
```

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/TemplateImagenModelFutures` | a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/TemplateImagenModelFutures` created around the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/TemplateImagenModel` |

## Public functions

### generateImages

```
abstract fun generateImages(templateId: String, inputs: Map<String, Any>): ListenableFuture<ImagenGenerationResponse<ImagenInlineImage>>
```

Generates an image, returning the result directly to the caller.

| Parameters |
|---|---|
| `templateId: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The ID of server prompt template. |
| `inputs: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html>` | the inputs needed to fill in the prompt |

### getImageModel

```
abstract fun getImageModel(): TemplateImagenModel
```

Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/TemplateImagenModel` object wrapped by this object.