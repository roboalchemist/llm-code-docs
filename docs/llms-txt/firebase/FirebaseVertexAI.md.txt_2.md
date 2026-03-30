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

| ### Public companion functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/FirebaseVertexAI` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/FirebaseVertexAI.Companion#getInstance(com.google.firebase.FirebaseApp)(app: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp)` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/FirebaseVertexAI` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/FirebaseVertexAI.Companion#getInstance(com.google.firebase.FirebaseApp,kotlin.String)(app: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp, location: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/FirebaseVertexAI` instance for the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` and `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/FirebaseVertexAI.Companion#getInstance(com.google.firebase.FirebaseApp,kotlin.String)`. |

| ### Public companion properties |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/FirebaseVertexAI` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/FirebaseVertexAI.Companion#instance()` The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/FirebaseVertexAI` instance for the default `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` |

| ### Public functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/GenerativeModel` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/FirebaseVertexAI#generativeModel(kotlin.String,com.google.firebase.vertexai.type.GenerationConfig,kotlin.collections.List,kotlin.collections.List,com.google.firebase.vertexai.type.ToolConfig,com.google.firebase.vertexai.type.Content,com.google.firebase.vertexai.type.RequestOptions)( modelName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, generationConfig: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/GenerationConfig?, safetySettings: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/SafetySetting>?, tools: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Tool>?, toolConfig: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ToolConfig?, systemInstruction: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content?, requestOptions: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/RequestOptions )` Instantiates a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/GenerativeModel` given the provided parameters. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/ImagenModel` | `@https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/PublicPreviewAPI https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/FirebaseVertexAI#imagenModel(kotlin.String,com.google.firebase.vertexai.type.ImagenGenerationConfig,com.google.firebase.vertexai.type.ImagenSafetySettings,com.google.firebase.vertexai.type.RequestOptions)( modelName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, generationConfig: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ImagenGenerationConfig?, safetySettings: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ImagenSafetySettings?, requestOptions: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/RequestOptions )` Instantiates a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/ImagenModel` given the provided parameters. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/LiveGenerativeModel` | `@https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/PublicPreviewAPI https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/FirebaseVertexAI#liveModel(kotlin.String,com.google.firebase.vertexai.type.LiveGenerationConfig,kotlin.collections.List,com.google.firebase.vertexai.type.Content,com.google.firebase.vertexai.type.RequestOptions)( modelName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, generationConfig: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig?, tools: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Tool>?, systemInstruction: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content?, requestOptions: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/RequestOptions )` Instantiates a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig` given the provided parameters. |

## Public companion functions

### getInstance

```
fun getInstance(app: FirebaseApp): FirebaseVertexAI
```

### getInstance

```
fun getInstance(app: FirebaseApp = Firebase.app, location: String): FirebaseVertexAI
```

Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/FirebaseVertexAI` instance for the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` and `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/FirebaseVertexAI.Companion#getInstance(com.google.firebase.FirebaseApp,kotlin.String)`.

| Parameters |
|---|---|
| `location: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | location identifier, defaults to `us-central1`; see available [Vertex AI regions](https://firebase.google.com/docs/vertex-ai/locations?platform=android#available-locations) . |

## Public companion properties

### instance

```
val instance: FirebaseVertexAI
```

The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/FirebaseVertexAI` instance for the default `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`

## Public functions

### generativeModel

```
fun generativeModel(
    modelName: String,
    generationConfig: GenerationConfig? = null,
    safetySettings: List<SafetySetting>? = null,
    tools: List<Tool>? = null,
    toolConfig: ToolConfig? = null,
    systemInstruction: Content? = null,
    requestOptions: RequestOptions = RequestOptions()
): GenerativeModel
```

Instantiates a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/GenerativeModel` given the provided parameters.

| Parameters |
|---|---|
| `modelName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the model to use, for example `"gemini-2.0-flash-exp"`. |
| `generationConfig: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/GenerationConfig? = null` | The configuration parameters to use for content generation. |
| `safetySettings: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/SafetySetting>? = null` | The safety bounds the model will abide to during content generation. |
| `tools: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Tool>? = null` | A list of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Tool`s the model may use to generate content. |
| `toolConfig: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ToolConfig? = null` | The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ToolConfig` that defines how the model handles the tools provided. |
| `systemInstruction: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content? = null` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content` instructions that direct the model to behave a certain way. Currently only text content is supported. |
| `requestOptions: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/RequestOptions = RequestOptions()` | Configuration options for sending requests to the backend. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/GenerativeModel` | The initialized `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/GenerativeModel` instance. |

### imagenModel

```
@PublicPreviewAPI
fun imagenModel(
    modelName: String,
    generationConfig: ImagenGenerationConfig? = null,
    safetySettings: ImagenSafetySettings? = null,
    requestOptions: RequestOptions = RequestOptions()
): ImagenModel
```

Instantiates a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/ImagenModel` given the provided parameters.

| Parameters |
|---|---|
| `modelName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the model to use, for example `"imagen-3.0-generate-001"`. |
| `generationConfig: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ImagenGenerationConfig? = null` | The configuration parameters to use for image generation. |
| `safetySettings: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ImagenSafetySettings? = null` | The safety bounds the model will abide by during image generation. |
| `requestOptions: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/RequestOptions = RequestOptions()` | Configuration options for sending requests to the backend. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/ImagenModel` | The initialized `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/ImagenModel` instance. |

### liveModel

```
@PublicPreviewAPI
fun liveModel(
    modelName: String,
    generationConfig: LiveGenerationConfig? = null,
    tools: List<Tool>? = null,
    systemInstruction: Content? = null,
    requestOptions: RequestOptions = RequestOptions()
): LiveGenerativeModel
```

Instantiates a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig` given the provided parameters.

| Parameters |
|---|---|
| `modelName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the model to use, for example `"gemini-2.0-flash-exp"`. |
| `generationConfig: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig? = null` | The configuration parameters to use for content generation. |
| `tools: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Tool>? = null` | A list of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Tool`s the model may use to generate content. |
| `systemInstruction: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content? = null` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content` instructions that direct the model to behave a certain way. Currently only text content is supported. |
| `requestOptions: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/RequestOptions = RequestOptions()` | Configuration options for sending requests to the backend. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/LiveGenerativeModel` | The initialized `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/LiveGenerativeModel` instance. |