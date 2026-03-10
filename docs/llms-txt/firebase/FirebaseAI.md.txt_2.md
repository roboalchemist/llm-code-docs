# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/FirebaseAI.md.txt

# FirebaseAI

# FirebaseAI


```
class FirebaseAI
```

<br />

*** ** * ** ***

Entry point for all *Firebase AI* functionality.

## Summary

| ### Public companion functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/FirebaseAI` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/FirebaseAI.Companion#getInstance(com.google.firebase.FirebaseApp)(app: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp)` The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/FirebaseAI` instance for the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` using the Google AI Backend. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/FirebaseAI` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/FirebaseAI.Companion#getInstance(com.google.firebase.FirebaseApp,com.google.firebase.ai.type.GenerativeBackend)(app: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp, backend: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerativeBackend)` Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/FirebaseAI` instance for the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` and `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/FirebaseAI.Companion#getInstance(com.google.firebase.FirebaseApp,com.google.firebase.ai.type.GenerativeBackend)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/FirebaseAI` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/FirebaseAI.Companion#getInstance(com.google.firebase.FirebaseApp,com.google.firebase.ai.type.GenerativeBackend,kotlin.Boolean)( app: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp, backend: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerativeBackend, useLimitedUseAppCheckTokens: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html )` Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/FirebaseAI` instance for the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` and `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/FirebaseAI.Companion#getInstance(com.google.firebase.FirebaseApp,com.google.firebase.ai.type.GenerativeBackend,kotlin.Boolean)`. |

| ### Public companion properties |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/FirebaseAI` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/FirebaseAI.Companion#instance()` The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/FirebaseAI` instance for the default `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` using the Google AI Backend. |

| ### Public functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/GenerativeModel` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/FirebaseAI#generativeModel(kotlin.String,com.google.firebase.ai.type.GenerationConfig,kotlin.collections.List,kotlin.collections.List,com.google.firebase.ai.type.ToolConfig,com.google.firebase.ai.type.Content,com.google.firebase.ai.type.RequestOptions)( modelName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, generationConfig: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig?, safetySettings: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/SafetySetting>?, tools: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Tool>?, toolConfig: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ToolConfig?, systemInstruction: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content?, requestOptions: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/RequestOptions )` Instantiates a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/GenerativeModel` given the provided parameters. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/GenerativeModel` | `@https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/PublicPreviewAPI https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/FirebaseAI#generativeModel(kotlin.String,com.google.firebase.ai.type.GenerationConfig,kotlin.collections.List,kotlin.collections.List,com.google.firebase.ai.type.ToolConfig,com.google.firebase.ai.type.Content,com.google.firebase.ai.type.RequestOptions,com.google.firebase.ai.OnDeviceConfig)( modelName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, generationConfig: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig?, safetySettings: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/SafetySetting>?, tools: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Tool>?, toolConfig: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ToolConfig?, systemInstruction: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content?, requestOptions: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/RequestOptions, onDeviceConfig: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/OnDeviceConfig )` Instantiates a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/GenerativeModel` given the provided parameters. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/ImagenModel` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/FirebaseAI#imagenModel(kotlin.String,com.google.firebase.ai.type.ImagenGenerationConfig,com.google.firebase.ai.type.ImagenSafetySettings,com.google.firebase.ai.type.RequestOptions)( modelName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, generationConfig: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig?, safetySettings: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenSafetySettings?, requestOptions: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/RequestOptions )` Instantiates a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/ImagenModel` given the provided parameters. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/LiveGenerativeModel` | `@https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/PublicPreviewAPI https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/FirebaseAI#liveModel(kotlin.String,com.google.firebase.ai.type.LiveGenerationConfig,kotlin.collections.List,com.google.firebase.ai.type.Content,com.google.firebase.ai.type.RequestOptions)( modelName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, generationConfig: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveGenerationConfig?, tools: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Tool>?, systemInstruction: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content?, requestOptions: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/RequestOptions )` Instantiates a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveGenerationConfig` given the provided parameters. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/TemplateGenerativeModel` | `@https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/PublicPreviewAPI https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/FirebaseAI#templateGenerativeModel(com.google.firebase.ai.type.RequestOptions)(requestOptions: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/RequestOptions)` Instantiates a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/TemplateGenerativeModel` given the provided parameters. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/TemplateImagenModel` | `@https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/PublicPreviewAPI https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/FirebaseAI#templateImagenModel(com.google.firebase.ai.type.RequestOptions)(requestOptions: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/RequestOptions)` Instantiates a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/TemplateImagenModel` given the provided parameters. |

## Public companion functions

### getInstance

```
fun getInstance(app: FirebaseApp): FirebaseAI
```

The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/FirebaseAI` instance for the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` using the Google AI Backend.

### getInstance

```
fun getInstance(app: FirebaseApp = Firebase.app, backend: GenerativeBackend): FirebaseAI
```

Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/FirebaseAI` instance for the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` and `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/FirebaseAI.Companion#getInstance(com.google.firebase.FirebaseApp,com.google.firebase.ai.type.GenerativeBackend)`.

| Parameters |
|---|---|
| `backend: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerativeBackend` | the backend reference to make generative AI requests to. |

### getInstance

```
fun getInstance(
    app: FirebaseApp = Firebase.app,
    backend: GenerativeBackend,
    useLimitedUseAppCheckTokens: Boolean
): FirebaseAI
```

Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/FirebaseAI` instance for the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` and `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/FirebaseAI.Companion#getInstance(com.google.firebase.FirebaseApp,com.google.firebase.ai.type.GenerativeBackend,kotlin.Boolean)`.

| Parameters |
|---|---|
| `backend: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerativeBackend` | the backend reference to make generative AI requests to. |
| `useLimitedUseAppCheckTokens: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | when sending tokens to the backend, this option enables the usage of App Check's limited-use tokens instead of the standard cached tokens. Learn more about [limited-use tokens](https://firebase.google.com/docs/ai-logic/app-check), including their nuances, when to use them, and best practices for integrating them into your app. *This flag is set to `false` by default.* |

## Public companion properties

### instance

```
val instance: FirebaseAI
```

The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/FirebaseAI` instance for the default `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` using the Google AI Backend.

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

Instantiates a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/GenerativeModel` given the provided parameters.

| Parameters |
|---|---|
| `modelName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the model to use. See the documentation for a list of [supported models](https://firebase.google.com/docs/ai-logic/models). |
| `generationConfig: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig? = null` | The configuration parameters to use for content generation. |
| `safetySettings: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/SafetySetting>? = null` | The safety bounds the model will abide to during content generation. |
| `tools: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Tool>? = null` | A list of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Tool`s the model may use to generate content. |
| `toolConfig: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ToolConfig? = null` | The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ToolConfig` that defines how the model handles the tools provided. |
| `systemInstruction: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content? = null` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content` instructions that direct the model to behave a certain way. Currently only text content is supported. |
| `requestOptions: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/RequestOptions = RequestOptions()` | Configuration options for sending requests to the backend. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/GenerativeModel` | The initialized `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/GenerativeModel` instance. |

### generativeModel

```
@PublicPreviewAPI
fun generativeModel(
    modelName: String,
    generationConfig: GenerationConfig? = null,
    safetySettings: List<SafetySetting>? = null,
    tools: List<Tool>? = null,
    toolConfig: ToolConfig? = null,
    systemInstruction: Content? = null,
    requestOptions: RequestOptions = RequestOptions(),
    onDeviceConfig: OnDeviceConfig
): GenerativeModel
```

Instantiates a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/GenerativeModel` given the provided parameters.

| Parameters |
|---|---|
| `modelName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the model to use. See the documentation for a list of [supported models](https://firebase.google.com/docs/ai-logic/models). |
| `generationConfig: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig? = null` | The configuration parameters to use for content generation. |
| `safetySettings: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/SafetySetting>? = null` | The safety bounds the model will abide to during content generation. |
| `tools: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Tool>? = null` | A list of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Tool`s the model may use to generate content. |
| `toolConfig: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ToolConfig? = null` | The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ToolConfig` that defines how the model handles the tools provided. |
| `systemInstruction: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content? = null` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content` instructions that direct the model to behave a certain way. Currently only text content is supported. |
| `requestOptions: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/RequestOptions = RequestOptions()` | Configuration options for sending requests to the backend. |
| `onDeviceConfig: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/OnDeviceConfig` | Configuration for on-device inference. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/GenerativeModel` | The initialized `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/GenerativeModel` instance. |

### imagenModel

```
fun imagenModel(
    modelName: String,
    generationConfig: ImagenGenerationConfig? = null,
    safetySettings: ImagenSafetySettings? = null,
    requestOptions: RequestOptions = RequestOptions()
): ImagenModel
```

Instantiates a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/ImagenModel` given the provided parameters.

| Parameters |
|---|---|
| `modelName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the model to use. See the documentation for a list of [supported models](https://firebase.google.com/docs/ai-logic/models). |
| `generationConfig: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig? = null` | The configuration parameters to use for image generation. |
| `safetySettings: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenSafetySettings? = null` | The safety bounds the model will abide by during image generation. |
| `requestOptions: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/RequestOptions = RequestOptions()` | Configuration options for sending requests to the backend. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/ImagenModel` | The initialized `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/ImagenModel` instance. |

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

Instantiates a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveGenerationConfig` given the provided parameters.

| Parameters |
|---|---|
| `modelName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the model to use. See the documentation for a list of [supported models](https://firebase.google.com/docs/ai-logic/models). |
| `generationConfig: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveGenerationConfig? = null` | The configuration parameters to use for content generation. |
| `tools: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Tool>? = null` | A list of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Tool`s the model may use to generate content. |
| `systemInstruction: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content? = null` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content` instructions that direct the model to behave a certain way. Currently only text content is supported. |
| `requestOptions: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/RequestOptions = RequestOptions()` | Configuration options for sending requests to the backend. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/LiveGenerativeModel` | The initialized `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/LiveGenerativeModel` instance. |

### templateGenerativeModel

```
@PublicPreviewAPI
fun templateGenerativeModel(requestOptions: RequestOptions = RequestOptions()): TemplateGenerativeModel
```

Instantiates a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/TemplateGenerativeModel` given the provided parameters.

| Parameters |
|---|---|
| `requestOptions: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/RequestOptions = RequestOptions()` | Configuration options for sending requests to the backend. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/TemplateGenerativeModel` | The initialized `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/TemplateGenerativeModel` instance. |

### templateImagenModel

```
@PublicPreviewAPI
fun templateImagenModel(requestOptions: RequestOptions = RequestOptions()): TemplateImagenModel
```

Instantiates a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/TemplateImagenModel` given the provided parameters.

| Parameters |
|---|---|
| `requestOptions: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/RequestOptions = RequestOptions()` | Configuration options for sending requests to the backend. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/TemplateImagenModel` | The initialized `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/TemplateImagenModel` instance. |