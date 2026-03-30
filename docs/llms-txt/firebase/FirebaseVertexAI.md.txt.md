# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/FirebaseVertexAI.md.txt

# FirebaseVertexAI

# FirebaseVertexAI


```
public final class FirebaseVertexAI
```

<br />

*** ** * ** ***

Entry point for all *Vertex AI in Firebase* functionality.

## Summary

| ### Nested types |
|---|
| `public static class https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/FirebaseVertexAI.Companion` |

| ### Public fields |
|---|---|
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/FirebaseVertexAI` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/FirebaseVertexAI.Companion#instance()` The `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/FirebaseVertexAI` instance for the default `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` |

| ### Public methods |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/GenerativeModel` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/FirebaseVertexAI#generativeModel(kotlin.String,com.google.firebase.vertexai.type.GenerationConfig,kotlin.collections.List,kotlin.collections.List,com.google.firebase.vertexai.type.ToolConfig,com.google.firebase.vertexai.type.Content,com.google.firebase.vertexai.type.RequestOptions)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html modelName, https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/GenerationConfig generationConfig, https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/SafetySetting> safetySettings, https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Tool> tools, https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ToolConfig toolConfig, https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content systemInstruction, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/RequestOptions requestOptions )` Instantiates a new `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/GenerativeModel` given the provided parameters. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/FirebaseVertexAI` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/FirebaseVertexAI.Companion#getInstance(com.google.firebase.FirebaseApp)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp app)` |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/FirebaseVertexAI` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/FirebaseVertexAI.Companion#getInstance(com.google.firebase.FirebaseApp,kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp app, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html location)` Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/FirebaseVertexAI` instance for the provided `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` and `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/FirebaseVertexAI.Companion#getInstance(com.google.firebase.FirebaseApp,kotlin.String)`. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/ImagenModel` | `@https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/PublicPreviewAPI https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/FirebaseVertexAI#imagenModel(kotlin.String,com.google.firebase.vertexai.type.ImagenGenerationConfig,com.google.firebase.vertexai.type.ImagenSafetySettings,com.google.firebase.vertexai.type.RequestOptions)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html modelName, https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ImagenGenerationConfig generationConfig, https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ImagenSafetySettings safetySettings, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/RequestOptions requestOptions )` Instantiates a new `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/ImagenModel` given the provided parameters. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/LiveGenerativeModel` | `@https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/PublicPreviewAPI https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/FirebaseVertexAI#liveModel(kotlin.String,com.google.firebase.vertexai.type.LiveGenerationConfig,kotlin.collections.List,com.google.firebase.vertexai.type.Content,com.google.firebase.vertexai.type.RequestOptions)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html modelName, https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveGenerationConfig generationConfig, https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Tool> tools, https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content systemInstruction, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/RequestOptions requestOptions )` Instantiates a new `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveGenerationConfig` given the provided parameters. |

## Public fields

### instance

```
public static final @NonNull FirebaseVertexAI instance
```

The `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/FirebaseVertexAI` instance for the default `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`

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

Instantiates a new `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/GenerativeModel` given the provided parameters.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html modelName` | The name of the model to use, for example `"gemini-2.0-flash-exp"`. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/GenerationConfig generationConfig` | The configuration parameters to use for content generation. |
| `https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/SafetySetting> safetySettings` | The safety bounds the model will abide to during content generation. |
| `https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Tool> tools` | A list of `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Tool`s the model may use to generate content. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ToolConfig toolConfig` | The `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ToolConfig` that defines how the model handles the tools provided. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content systemInstruction` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content` instructions that direct the model to behave a certain way. Currently only text content is supported. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/RequestOptions requestOptions` | Configuration options for sending requests to the backend. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/GenerativeModel` | The initialized `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/GenerativeModel` instance. |

### getInstance

```
public static final @NonNull FirebaseVertexAI getInstance(@NonNull FirebaseApp app)
```

### getInstance

```
public static final @NonNull FirebaseVertexAI getInstance(@NonNull FirebaseApp app, @NonNull String location)
```

Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/FirebaseVertexAI` instance for the provided `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` and `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/FirebaseVertexAI.Companion#getInstance(com.google.firebase.FirebaseApp,kotlin.String)`.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html location` | location identifier, defaults to `us-central1`; see available [Vertex AI regions](https://firebase.google.com/docs/vertex-ai/locations?platform=android#available-locations) . |

### imagenModel

```
@PublicPreviewAPI
public final @NonNull ImagenModel imagenModel(
    @NonNull String modelName,
    ImagenGenerationConfig generationConfig,
    ImagenSafetySettings safetySettings,
    @NonNull RequestOptions requestOptions
)
```

Instantiates a new `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/ImagenModel` given the provided parameters.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html modelName` | The name of the model to use, for example `"imagen-3.0-generate-001"`. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ImagenGenerationConfig generationConfig` | The configuration parameters to use for image generation. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ImagenSafetySettings safetySettings` | The safety bounds the model will abide by during image generation. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/RequestOptions requestOptions` | Configuration options for sending requests to the backend. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/ImagenModel` | The initialized `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/ImagenModel` instance. |

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

Instantiates a new `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveGenerationConfig` given the provided parameters.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html modelName` | The name of the model to use, for example `"gemini-2.0-flash-exp"`. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveGenerationConfig generationConfig` | The configuration parameters to use for content generation. |
| `https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Tool> tools` | A list of `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Tool`s the model may use to generate content. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content systemInstruction` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content` instructions that direct the model to behave a certain way. Currently only text content is supported. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/RequestOptions requestOptions` | Configuration options for sending requests to the backend. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/LiveGenerativeModel` | The initialized `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/LiveGenerativeModel` instance. |