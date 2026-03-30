# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI.md.txt

# FirebaseAI

# FirebaseAI


```
public final class FirebaseAI
```

<br />

*** ** * ** ***

Entry point for all *Firebase AI* functionality.

## Summary

| ### Nested types |
|---|
| `public static class https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI.Companion` |

| ### Public fields |
|---|---|
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI.Companion#instance()` The `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI` instance for the default `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` using the Google AI Backend. |

| ### Public methods |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/GenerativeModel` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI#generativeModel(kotlin.String,com.google.firebase.ai.type.GenerationConfig,kotlin.collections.List,kotlin.collections.List,com.google.firebase.ai.type.ToolConfig,com.google.firebase.ai.type.Content,com.google.firebase.ai.type.RequestOptions)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html modelName, https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig generationConfig, https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/SafetySetting> safetySettings, https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Tool> tools, https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ToolConfig toolConfig, https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content systemInstruction, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/RequestOptions requestOptions )` Instantiates a new `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/GenerativeModel` given the provided parameters. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/GenerativeModel` | `@https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/PublicPreviewAPI https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI#generativeModel(kotlin.String,com.google.firebase.ai.type.GenerationConfig,kotlin.collections.List,kotlin.collections.List,com.google.firebase.ai.type.ToolConfig,com.google.firebase.ai.type.Content,com.google.firebase.ai.type.RequestOptions,com.google.firebase.ai.OnDeviceConfig)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html modelName, https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig generationConfig, https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/SafetySetting> safetySettings, https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Tool> tools, https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ToolConfig toolConfig, https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content systemInstruction, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/RequestOptions requestOptions, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/OnDeviceConfig onDeviceConfig )` Instantiates a new `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/GenerativeModel` given the provided parameters. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI.Companion#getInstance(com.google.firebase.FirebaseApp)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp app)` The `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI` instance for the provided `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` using the Google AI Backend. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI.Companion#getInstance(com.google.firebase.FirebaseApp,com.google.firebase.ai.type.GenerativeBackend)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp app, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerativeBackend backend)` Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI` instance for the provided `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` and `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI.Companion#getInstance(com.google.firebase.FirebaseApp,com.google.firebase.ai.type.GenerativeBackend)`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI.Companion#getInstance(com.google.firebase.FirebaseApp,com.google.firebase.ai.type.GenerativeBackend,kotlin.Boolean)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp app, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerativeBackend backend, boolean useLimitedUseAppCheckTokens )` Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI` instance for the provided `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` and `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI.Companion#getInstance(com.google.firebase.FirebaseApp,com.google.firebase.ai.type.GenerativeBackend,kotlin.Boolean)`. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/ImagenModel` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI#imagenModel(kotlin.String,com.google.firebase.ai.type.ImagenGenerationConfig,com.google.firebase.ai.type.ImagenSafetySettings,com.google.firebase.ai.type.RequestOptions)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html modelName, https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenGenerationConfig generationConfig, https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenSafetySettings safetySettings, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/RequestOptions requestOptions )` Instantiates a new `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/ImagenModel` given the provided parameters. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/LiveGenerativeModel` | `@https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/PublicPreviewAPI https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI#liveModel(kotlin.String,com.google.firebase.ai.type.LiveGenerationConfig,kotlin.collections.List,com.google.firebase.ai.type.Content,com.google.firebase.ai.type.RequestOptions)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html modelName, https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveGenerationConfig generationConfig, https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Tool> tools, https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content systemInstruction, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/RequestOptions requestOptions )` Instantiates a new `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveGenerationConfig` given the provided parameters. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/TemplateGenerativeModel` | `@https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/PublicPreviewAPI https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI#templateGenerativeModel(com.google.firebase.ai.type.RequestOptions)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/RequestOptions requestOptions)` Instantiates a new `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/TemplateGenerativeModel` given the provided parameters. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/TemplateImagenModel` | `@https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/PublicPreviewAPI https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI#templateImagenModel(com.google.firebase.ai.type.RequestOptions)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/RequestOptions requestOptions)` Instantiates a new `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/TemplateImagenModel` given the provided parameters. |

## Public fields

### instance

```
public static final @NonNull FirebaseAI instance
```

The `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI` instance for the default `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` using the Google AI Backend.

## Public methods

### generativeModel

```
public final @NonNull GenerativeModel generativeModel(
    @NonNull String modelName,
    GenerationConfig generationConfig,
    List<@NonNull SafetySetting> safetySettings,
    List<@NonNull Tool> tools,
    ToolConfig toolConfig,
    Content systemInstruction,
    @NonNull RequestOptions requestOptions
)
```

Instantiates a new `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/GenerativeModel` given the provided parameters.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html modelName` | The name of the model to use. See the documentation for a list of [supported models](https://firebase.google.com/docs/ai-logic/models). |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig generationConfig` | The configuration parameters to use for content generation. |
| `https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/SafetySetting> safetySettings` | The safety bounds the model will abide to during content generation. |
| `https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Tool> tools` | A list of `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Tool`s the model may use to generate content. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ToolConfig toolConfig` | The `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ToolConfig` that defines how the model handles the tools provided. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content systemInstruction` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content` instructions that direct the model to behave a certain way. Currently only text content is supported. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/RequestOptions requestOptions` | Configuration options for sending requests to the backend. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/GenerativeModel` | The initialized `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/GenerativeModel` instance. |

### generativeModel

```
@PublicPreviewAPI
public final @NonNull GenerativeModel generativeModel(
    @NonNull String modelName,
    GenerationConfig generationConfig,
    List<@NonNull SafetySetting> safetySettings,
    List<@NonNull Tool> tools,
    ToolConfig toolConfig,
    Content systemInstruction,
    @NonNull RequestOptions requestOptions,
    @NonNull OnDeviceConfig onDeviceConfig
)
```

Instantiates a new `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/GenerativeModel` given the provided parameters.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html modelName` | The name of the model to use. See the documentation for a list of [supported models](https://firebase.google.com/docs/ai-logic/models). |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig generationConfig` | The configuration parameters to use for content generation. |
| `https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/SafetySetting> safetySettings` | The safety bounds the model will abide to during content generation. |
| `https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Tool> tools` | A list of `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Tool`s the model may use to generate content. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ToolConfig toolConfig` | The `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ToolConfig` that defines how the model handles the tools provided. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content systemInstruction` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content` instructions that direct the model to behave a certain way. Currently only text content is supported. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/RequestOptions requestOptions` | Configuration options for sending requests to the backend. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/OnDeviceConfig onDeviceConfig` | Configuration for on-device inference. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/GenerativeModel` | The initialized `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/GenerativeModel` instance. |

### getInstance

```
public static final @NonNull FirebaseAI getInstance(@NonNull FirebaseApp app)
```

The `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI` instance for the provided `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` using the Google AI Backend.

### getInstance

```
public static final @NonNull FirebaseAI getInstance(@NonNull FirebaseApp app, @NonNull GenerativeBackend backend)
```

Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI` instance for the provided `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` and `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI.Companion#getInstance(com.google.firebase.FirebaseApp,com.google.firebase.ai.type.GenerativeBackend)`.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerativeBackend backend` | the backend reference to make generative AI requests to. |

### getInstance

```
public static final @NonNull FirebaseAI getInstance(
    @NonNull FirebaseApp app,
    @NonNull GenerativeBackend backend,
    boolean useLimitedUseAppCheckTokens
)
```

Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI` instance for the provided `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` and `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI.Companion#getInstance(com.google.firebase.FirebaseApp,com.google.firebase.ai.type.GenerativeBackend,kotlin.Boolean)`.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerativeBackend backend` | the backend reference to make generative AI requests to. |
| `boolean useLimitedUseAppCheckTokens` | when sending tokens to the backend, this option enables the usage of App Check's limited-use tokens instead of the standard cached tokens. Learn more about [limited-use tokens](https://firebase.google.com/docs/ai-logic/app-check), including their nuances, when to use them, and best practices for integrating them into your app. *This flag is set to `false` by default.* |

### imagenModel

```
public final @NonNull ImagenModel imagenModel(
    @NonNull String modelName,
    ImagenGenerationConfig generationConfig,
    ImagenSafetySettings safetySettings,
    @NonNull RequestOptions requestOptions
)
```

Instantiates a new `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/ImagenModel` given the provided parameters.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html modelName` | The name of the model to use. See the documentation for a list of [supported models](https://firebase.google.com/docs/ai-logic/models). |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenGenerationConfig generationConfig` | The configuration parameters to use for image generation. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenSafetySettings safetySettings` | The safety bounds the model will abide by during image generation. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/RequestOptions requestOptions` | Configuration options for sending requests to the backend. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/ImagenModel` | The initialized `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/ImagenModel` instance. |

### liveModel

```
@PublicPreviewAPI
public final @NonNull LiveGenerativeModel liveModel(
    @NonNull String modelName,
    LiveGenerationConfig generationConfig,
    List<@NonNull Tool> tools,
    Content systemInstruction,
    @NonNull RequestOptions requestOptions
)
```

Instantiates a new `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveGenerationConfig` given the provided parameters.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html modelName` | The name of the model to use. See the documentation for a list of [supported models](https://firebase.google.com/docs/ai-logic/models). |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveGenerationConfig generationConfig` | The configuration parameters to use for content generation. |
| `https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Tool> tools` | A list of `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Tool`s the model may use to generate content. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content systemInstruction` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content` instructions that direct the model to behave a certain way. Currently only text content is supported. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/RequestOptions requestOptions` | Configuration options for sending requests to the backend. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/LiveGenerativeModel` | The initialized `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/LiveGenerativeModel` instance. |

### templateGenerativeModel

```
@PublicPreviewAPI
public final @NonNull TemplateGenerativeModel templateGenerativeModel(@NonNull RequestOptions requestOptions)
```

Instantiates a new `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/TemplateGenerativeModel` given the provided parameters.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/RequestOptions requestOptions` | Configuration options for sending requests to the backend. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/TemplateGenerativeModel` | The initialized `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/TemplateGenerativeModel` instance. |

### templateImagenModel

```
@PublicPreviewAPI
public final @NonNull TemplateImagenModel templateImagenModel(@NonNull RequestOptions requestOptions)
```

Instantiates a new `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/TemplateImagenModel` given the provided parameters.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/RequestOptions requestOptions` | Configuration options for sending requests to the backend. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/TemplateImagenModel` | The initialized `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/TemplateImagenModel` instance. |