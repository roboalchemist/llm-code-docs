# Source: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Classes/ImagenModel.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/ImagenModel.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/ImagenModel.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Classes/ImagenModel.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/ImagenModel.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Classes/ImagenModel.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/ImagenModel.md.txt

# ImagenModel

# ImagenModel


```
@PublicPreviewAPI
class ImagenModel
```

<br />

*** ** * ** ***

| **This class is deprecated.**   
| The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

Represents a generative model (like Imagen), capable of generating images based on various input types.

## Summary

|                                                                                                                                ### Public functions                                                                                                                                |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `suspend `[ImagenGenerationResponse](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ImagenGenerationResponse)`<`[ImagenInlineImage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ImagenInlineImage)`>` | [generateImages](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/ImagenModel#generateImages(kotlin.String))`(prompt: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`)` Generates an image, returning the result directly to the caller. |

## Public functions

### generateImages

```
suspendÂ funÂ generateImages(prompt:Â String):Â ImagenGenerationResponse<ImagenInlineImage>
```

Generates an image, returning the result directly to the caller.  

|                                         Parameters                                         |
|--------------------------------------------------------------------------------------------|----------------------------------------------|
| `prompt: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | The input(s) given to the model as a prompt. |