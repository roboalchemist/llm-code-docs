# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/FirebaseVertexAI.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/FirebaseVertexAI.md.txt

# FirebaseVertexAI

# FirebaseVertexAI


```
class FirebaseVertexAI
```

<br />

*** ** * ** ***

Entry point for all *Vertex AI in Firebase* functionality.

## Summary

|                                           ### Public companion functions                                            |
|---------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [FirebaseVertexAI](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/FirebaseVertexAI) | [getInstance](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/FirebaseVertexAI.Companion#getInstance(com.google.firebase.FirebaseApp))`(app: `[FirebaseApp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp)`)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [FirebaseVertexAI](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/FirebaseVertexAI) | [getInstance](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/FirebaseVertexAI.Companion#getInstance(com.google.firebase.FirebaseApp,kotlin.String))`(app: `[FirebaseApp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp)`, location: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`)` Returns the [FirebaseVertexAI](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/FirebaseVertexAI) instance for the provided [FirebaseApp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp) and [location](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/FirebaseVertexAI.Companion#getInstance(com.google.firebase.FirebaseApp,kotlin.String)). |

|                                           ### Public companion properties                                           |
|---------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [FirebaseVertexAI](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/FirebaseVertexAI) | [instance](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/FirebaseVertexAI.Companion#instance()) The [FirebaseVertexAI](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/FirebaseVertexAI) instance for the default [FirebaseApp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp) |

|                                                   ### Public functions                                                    |
|---------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [GenerativeModel](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/GenerativeModel)         | [generativeModel](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/FirebaseVertexAI#generativeModel(kotlin.String,com.google.firebase.vertexai.type.GenerationConfig,kotlin.collections.List,kotlin.collections.List,com.google.firebase.vertexai.type.ToolConfig,com.google.firebase.vertexai.type.Content,com.google.firebase.vertexai.type.RequestOptions))`(` ` modelName: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`,` ` generationConfig: `[GenerationConfig](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/GenerationConfig)`?,` ` safetySettings: `[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[SafetySetting](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/SafetySetting)`>?,` ` tools: `[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[Tool](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Tool)`>?,` ` toolConfig: `[ToolConfig](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ToolConfig)`?,` ` systemInstruction: `[Content](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content)`?,` ` requestOptions: `[RequestOptions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/RequestOptions) `)` Instantiates a new [GenerativeModel](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/GenerativeModel) given the provided parameters. |
| [ImagenModel](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/ImagenModel)                 | `@`[PublicPreviewAPI](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/PublicPreviewAPI) [imagenModel](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/FirebaseVertexAI#imagenModel(kotlin.String,com.google.firebase.vertexai.type.ImagenGenerationConfig,com.google.firebase.vertexai.type.ImagenSafetySettings,com.google.firebase.vertexai.type.RequestOptions))`(` ` modelName: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`,` ` generationConfig: `[ImagenGenerationConfig](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ImagenGenerationConfig)`?,` ` safetySettings: `[ImagenSafetySettings](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ImagenSafetySettings)`?,` ` requestOptions: `[RequestOptions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/RequestOptions) `)` Instantiates a new [ImagenModel](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/ImagenModel) given the provided parameters.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [LiveGenerativeModel](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/LiveGenerativeModel) | `@`[PublicPreviewAPI](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/PublicPreviewAPI) [liveModel](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/FirebaseVertexAI#liveModel(kotlin.String,com.google.firebase.vertexai.type.LiveGenerationConfig,kotlin.collections.List,com.google.firebase.vertexai.type.Content,com.google.firebase.vertexai.type.RequestOptions))`(` ` modelName: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`,` ` generationConfig: `[LiveGenerationConfig](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig)`?,` ` tools: `[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[Tool](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Tool)`>?,` ` systemInstruction: `[Content](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content)`?,` ` requestOptions: `[RequestOptions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/RequestOptions) `)` Instantiates a new [LiveGenerationConfig](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig) given the provided parameters.                                                                                                                                                                                                                                                                                                 |

## Public companion functions

### getInstance

```
funÂ getInstance(app:Â FirebaseApp):Â FirebaseVertexAI
```  

### getInstance

```
funÂ getInstance(app:Â FirebaseApp = Firebase.app,Â location:Â String):Â FirebaseVertexAI
```

Returns the [FirebaseVertexAI](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/FirebaseVertexAI) instance for the provided [FirebaseApp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp) and [location](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/FirebaseVertexAI.Companion#getInstance(com.google.firebase.FirebaseApp,kotlin.String)).  

|                                          Parameters                                          |
|----------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `location: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | location identifier, defaults to `us-central1`; see available [Vertex AI regions](https://firebase.google.com/docs/vertex-ai/locations?platform=android#available-locations) . |

## Public companion properties

### instance

```
valÂ instance:Â FirebaseVertexAI
```

The [FirebaseVertexAI](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/FirebaseVertexAI) instance for the default [FirebaseApp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp)  

## Public functions

### generativeModel

```
funÂ generativeModel(
Â Â Â Â modelName:Â String,
Â Â Â Â generationConfig:Â GenerationConfig? = null,
Â Â Â Â safetySettings:Â List<SafetySetting>? = null,
Â Â Â Â tools:Â List<Tool>? = null,
Â Â Â Â toolConfig:Â ToolConfig? = null,
Â Â Â Â systemInstruction:Â Content? = null,
Â Â Â Â requestOptions:Â RequestOptions = RequestOptions()
):Â GenerativeModel
```

Instantiates a new [GenerativeModel](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/GenerativeModel) given the provided parameters.  

|                                                                                                                 Parameters                                                                                                                 |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `modelName: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)                                                                                                                                              | The name of the model to use, for example `"gemini-2.0-flash-exp"`.                                                                                                                                          |
| `generationConfig: `[GenerationConfig](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/GenerationConfig)`? = null`                                                                                     | The configuration parameters to use for content generation.                                                                                                                                                  |
| `safetySettings: `[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[SafetySetting](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/SafetySetting)`>? = null` | The safety bounds the model will abide to during content generation.                                                                                                                                         |
| `tools: `[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[Tool](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Tool)`>? = null`                            | A list of [Tool](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Tool)s the model may use to generate content.                                                           |
| `toolConfig: `[ToolConfig](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ToolConfig)`? = null`                                                                                                       | The [ToolConfig](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ToolConfig) that defines how the model handles the tools provided.                                      |
| `systemInstruction: `[Content](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content)`? = null`                                                                                                      | [Content](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content) instructions that direct the model to behave a certain way. Currently only text content is supported. |
| `requestOptions: `[RequestOptions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/RequestOptions)` = RequestOptions()`                                                                                | Configuration options for sending requests to the backend.                                                                                                                                                   |

|                                                      Returns                                                      |
|-------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| [GenerativeModel](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/GenerativeModel) | The initialized [GenerativeModel](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/GenerativeModel) instance. |

### imagenModel

```
@PublicPreviewAPI
funÂ imagenModel(
Â Â Â Â modelName:Â String,
Â Â Â Â generationConfig:Â ImagenGenerationConfig? = null,
Â Â Â Â safetySettings:Â ImagenSafetySettings? = null,
Â Â Â Â requestOptions:Â RequestOptions = RequestOptions()
):Â ImagenModel
```

Instantiates a new [ImagenModel](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/ImagenModel) given the provided parameters.  

|                                                                             Parameters                                                                             |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| `modelName: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)                                                                      | The name of the model to use, for example `"imagen-3.0-generate-001"`. |
| `generationConfig: `[ImagenGenerationConfig](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ImagenGenerationConfig)`? = null` | The configuration parameters to use for image generation.              |
| `safetySettings: `[ImagenSafetySettings](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ImagenSafetySettings)`? = null`       | The safety bounds the model will abide by during image generation.     |
| `requestOptions: `[RequestOptions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/RequestOptions)` = RequestOptions()`        | Configuration options for sending requests to the backend.             |

|                                                  Returns                                                  |
|-----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| [ImagenModel](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/ImagenModel) | The initialized [ImagenModel](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/ImagenModel) instance. |

### liveModel

```
@PublicPreviewAPI
funÂ liveModel(
Â Â Â Â modelName:Â String,
Â Â Â Â generationConfig:Â LiveGenerationConfig? = null,
Â Â Â Â tools:Â List<Tool>? = null,
Â Â Â Â systemInstruction:Â Content? = null,
Â Â Â Â requestOptions:Â RequestOptions = RequestOptions()
):Â LiveGenerativeModel
```

Instantiates a new [LiveGenerationConfig](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig) given the provided parameters.  

|                                                                                                   Parameters                                                                                                    |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `modelName: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)                                                                                                                   | The name of the model to use, for example `"gemini-2.0-flash-exp"`.                                                                                                                                          |
| `generationConfig: `[LiveGenerationConfig](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig)`? = null`                                                  | The configuration parameters to use for content generation.                                                                                                                                                  |
| `tools: `[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[Tool](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Tool)`>? = null` | A list of [Tool](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Tool)s the model may use to generate content.                                                           |
| `systemInstruction: `[Content](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content)`? = null`                                                                           | [Content](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content) instructions that direct the model to behave a certain way. Currently only text content is supported. |
| `requestOptions: `[RequestOptions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/RequestOptions)` = RequestOptions()`                                                     | Configuration options for sending requests to the backend.                                                                                                                                                   |

|                                                          Returns                                                          |
|---------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| [LiveGenerativeModel](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/LiveGenerativeModel) | The initialized [LiveGenerativeModel](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/LiveGenerativeModel) instance. |