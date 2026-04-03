# Source: https://firebase.google.com/docs/ai-logic/model-parameters.md.txt

<br />

In each call to a model, you can send along a model configuration to control how the model generates a response. Each model offers different configuration options.
You can also experiment with prompts and model configurations using[Google AI Studio](https://aistudio.google.com).

[arrow_downwardJump toGeminiconfig options](https://firebase.google.com/docs/ai-logic/model-parameters#gemini)[arrow_downwardJump toImagenconfig options](https://firebase.google.com/docs/ai-logic/model-parameters#imagen)

<br />

*** ** * ** ***

## ConfigureGeminimodels

|----------------------------------------------------------------------------------------------------------------------------------|
| *Click yourGemini APIprovider to view provider-specific content and code on this page.* Gemini Developer APIVertex AI Gemini API |

This section shows you how to[set up a configuration](https://firebase.google.com/docs/ai-logic/model-parameters#config-gemini)for use withGeminimodels and provides a[description of each parameter](https://firebase.google.com/docs/ai-logic/model-parameters#parameters-descriptions-gemini).

### Set up a model configuration (Gemini)

| **Note:** For the majority of use cases when accessing aGeminimodel, you configure the model using`GenerationConfig`. However, if you're[configuring a model for theGemini Live API](https://firebase.google.com/docs/ai-logic/model-parameters#config-gemini-live-api), you use a`LiveGenerationConfig`.

#### Config for generalGeminiuse cases

The configuration is maintained for the lifetime of the instance. If you want to use a different config, create a new`GenerativeModel`instance with that config.  

### Swift

Set the values of the parameters in a[`GenerationConfig`](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GenerationConfig)as part of creating a`GenerativeModel`instance.  


    import FirebaseAILogic

    // Set parameter values in a `GenerationConfig`.
    // IMPORTANT: Example values shown here. Make sure to update for your use case.
    let config = GenerationConfig(
      candidateCount: 1,
      temperature: 0.9,
      topP: 0.1,
      topK: 16,
      maxOutputTokens: 200,
      stopSequences: ["red"]
    )

    // Initialize the Gemini Developer API backend service
    // Specify the config as part of creating the `GenerativeModel` instance
    let model = FirebaseAI.firebaseAI(backend: .googleAI()).generativeModel(
      modelName: "<var translate="no">GEMINI_MODEL_NAME</var>",
      generationConfig: config
    )

    // ...

### Kotlin

Set the values of the parameters in a[`GenerationConfig`](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig)as part of creating a`GenerativeModel`instance.  


    // ...

    // Set parameter values in a `GenerationConfig`.
    // IMPORTANT: Example values shown here. Make sure to update for your use case.
    val config = generationConfig {
        candidateCount = 1
        maxOutputTokens = 200
        stopSequences = listOf("red")
        temperature = 0.9f
        topK = 16
        topP = 0.1f
    }

    // Initialize the Gemini Developer API backend service
    // Specify the config as part of creating the `GenerativeModel` instance
    val model = Firebase.ai(backend = GenerativeBackend.googleAI()).generativeModel(
        modelName = "<var translate="no">GEMINI_MODEL_NAME</var>",
        generationConfig = config
    )

    // ...

### Java

Set the values of the parameters in a[`GenerationConfig`](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig)as part of creating a`GenerativeModel`instance.  


    // ...

    // Set parameter values in a `GenerationConfig`.
    // IMPORTANT: Example values shown here. Make sure to update for your use case.
    GenerationConfig.Builder configBuilder = new GenerationConfig.Builder();
    configBuilder.candidateCount = 1;
    configBuilder.maxOutputTokens = 200;
    configBuilder.stopSequences = List.of("red");
    configBuilder.temperature = 0.9f;
    configBuilder.topK = 16;
    configBuilder.topP = 0.1f;

    GenerationConfig config = configBuilder.build();

    // Specify the config as part of creating the `GenerativeModel` instance
    GenerativeModelFutures model = GenerativeModelFutures.from(
            FirebaseAI.getInstance(GenerativeBackend.googleAI())
                    .generativeModel(
                        "<var translate="no">GEMINI_MODEL_NAME</var>",
                        config
                    );
    );

    // ...

### Web

Set the values of the parameters in a[`GenerationConfig`](https://firebase.google.com/docs/reference/js/ai.generationconfig)as part of creating a`GenerativeModel`instance.  


    // ...

    // Initialize the Gemini Developer API backend service
    const ai = getAI(firebaseApp, { backend: new GoogleAIBackend() });

    // Set parameter values in a `GenerationConfig`.
    // IMPORTANT: Example values shown here. Make sure to update for your use case.
    const generationConfig = {
      candidate_count: 1,
      maxOutputTokens: 200,
      stopSequences: ["red"],
      temperature: 0.9,
      topP: 0.1,
      topK: 16,
    };

    // Specify the config as part of creating the `GenerativeModel` instance
    const model = getGenerativeModel(ai, { model: "<var translate="no">GEMINI_MODEL_NAME</var>",  generationConfig });

    // ...

### Dart

Set the values of the parameters in a[`GenerationConfig`](https://pub.dev/documentation/firebase_ai/latest/firebase_ai/GenerationConfig-class.html)as part of creating a`GenerativeModel`instance.  


    // ...

    // Set parameter values in a `GenerationConfig`.
    // IMPORTANT: Example values shown here. Make sure to update for your use case.
    final generationConfig = GenerationConfig(
      candidateCount: 1,
      maxOutputTokens: 200,
      stopSequences: ["red"],
      temperature: 0.9,
      topP: 0.1,
      topK: 16,
    );

    // Initialize the Gemini Developer API backend service
    // Specify the config as part of creating the `GenerativeModel` instance
    final model = FirebaseAI.googleAI().generativeModel(
      model: '<var translate="no">GEMINI_MODEL_NAME</var>',
      config: generationConfig,
    );

    // ...

### Unity

Set the values of the parameters in a[`GenerationConfig`](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/generation-config)as part of creating a`GenerativeModel`instance.  


    // ...

    // Set parameter values in a `GenerationConfig`.
    // IMPORTANT: Example values shown here. Make sure to update for your use case.
    var generationConfig = new GenerationConfig(
      candidateCount: 1,
      maxOutputTokens: 200,
      stopSequences: new string[] { "red" },
      temperature: 0.9f,
      topK: 16,
      topP: 0.1f
    );

    // Specify the config as part of creating the `GenerativeModel` instance
    var ai = FirebaseAI.GetInstance(FirebaseAI.Backend.GoogleAI());
    var model = ai.GetGenerativeModel(
      modelName: "<var translate="no">GEMINI_MODEL_NAME</var>",
      generationConfig: generationConfig
    );

You can find a[description of each parameter](https://firebase.google.com/docs/ai-logic/model-parameters#parameters-descriptions-gemini)in the next section of this page.

#### Config for theGemini Live API

The configuration is maintained for the lifetime of the instance. If you want to use a different config, create a new`LiveModel`instance with that config.  

### Swift

Set the values of parameters in the[`liveGenerationConfig`](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/LiveGenerationConfig)during initialization of the`LiveModel`instance:  


    // ...

    // Set parameter values in a `LiveGenerationConfig` (example values shown here)
    let config = LiveGenerationConfig(
      temperature: 0.9,
      topP: 0.1,
      topK: 16,
      maxOutputTokens: 200,
      responseModalities: [.audio],
      speech: SpeechConfig(voiceName: "Fenrir"),
    )

    // Specify the config as part of creating the `liveModel` instance
    let liveModel = FirebaseAI.firebaseAI(backend: .googleAI()).liveModel(
      modelName: "<var translate="no">GEMINI_LIVE_MODEL_NAME</var>",
      generationConfig: config
    )

    // ...

### Kotlin

Set the values of parameters in a[`LiveGenerationConfig`](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveGenerationConfig)as part of creating a`LiveModel`instance.  


    // ...

    // Set parameter values in a `LiveGenerationConfig` (example values shown here)
    val config = liveGenerationConfig {
        maxOutputTokens = 200
        responseModality = ResponseModality.AUDIO
        speechConfig = SpeechConfig(voice = Voices.FENRIR)
        temperature = 0.9f
        topK = 16
        topP = 0.1f
    }

    // Specify the config as part of creating the `LiveModel` instance
    val liveModel = Firebase.ai(backend = GenerativeBackend.googleAI()).liveModel(
        modelName = "<var translate="no">GEMINI_LIVE_MODEL_NAME</var>",
        generationConfig = config
    )

    // ...

### Java

Set the values of parameters in a[`LiveGenerationConfig`](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveGenerationConfig)as part of creating a`LiveModel`instance.  


    // ...

    // Set parameter values in a `LiveGenerationConfig` (example values shown here)
    LiveGenerationConfig.Builder configBuilder = new LiveGenerationConfig.Builder();
    configBuilder.setMaxOutputTokens(200);
    configBuilder.setResponseModality(ResponseModality.AUDIO);

    configBuilder.setSpeechConfig(new SpeechConfig(Voices.FENRIR));
    configBuilder.setTemperature(0.9f);
    configBuilder.setTopK(16);
    configBuilder.setTopP(0.1f);

    LiveGenerationConfig config = configBuilder.build();

    // Specify the config as part of creating the `LiveModel` instance
    LiveGenerativeModel lm = FirebaseAI.getInstance(GenerativeBackend.googleAI()).liveModel(
              "<var translate="no">GEMINI_LIVE_MODEL_NAME</var>",
              config
    );

    // ...

### Web

Set the values of parameters in the[`LiveGenerationConfig`](https://firebase.google.com/docs/reference/js/ai.livegenerationconfig)during initialization of the`LiveGenerativeModel`instance:  


    // ...

    const ai = getAI(firebaseApp, { backend: new GoogleAIBackend() });

    // Set parameter values in a `LiveGenerationConfig` (example values shown here)
    const liveGenerationConfig = {
      maxOutputTokens: 200,
      responseModalities: [ResponseModality.AUDIO],
      speechConfig: {
        voiceConfig: {
          prebuiltVoiceConfig: { voiceName: "Fenrir" },
        },
      },
      temperature: 0.9,
      topP: 0.1,
      topK: 16,
    };

    // Specify the config as part of creating the `LiveGenerativeModel` instance
    const liveModel = getLiveGenerativeModel(ai, {
      model: "<var translate="no">GEMINI_LIVE_MODEL_NAME</var>",
      liveGenerationConfig,
    });

    // ...

### Dart

Set the values of parameters in a[`LiveGenerationConfig`](https://pub.dev/documentation/firebase_ai/latest/firebase_ai/LiveGenerationConfig-class.html)as part of creating a`LiveGenerativeModel`instance.  


    // ...

    // Set parameter values in a `LiveGenerationConfig` (example values shown here)
    final config = LiveGenerationConfig(
      maxOutputTokens: 200,
      responseModalities: [ResponseModalities.audio],
      speechConfig: SpeechConfig(voiceName: 'Fenrir'),
      temperature: 0.9,
      topP: 0.1,
      topK: 16,
    );

    // Specify the config as part of creating the `liveGenerativeModel` instance
    final liveModel = FirebaseAI.googleAI().liveGenerativeModel(
      model: '<var translate="no">GEMINI_LIVE_MODEL_NAME</var>',
      liveGenerationConfig: config,
    );

    // ...

### Unity

Set the values of parameters in a[`LiveGenerationConfig`](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/live-generation-config)as part of creating a`LiveModel`instance.  


    // ...

    // Set parameter values in a `LiveGenerationConfig` (example values shown here)
    var config = new LiveGenerationConfig(
      maxOutputTokens: 200,
      responseModalities: new[] { ResponseModality.Audio },
      speechConfig: SpeechConfig.UsePrebuiltVoice("Fenrir"),
      temperature: 0.9f,
      topK: 16,
      topP: 0.1f
    );

    // Specify the config as part of creating the `LiveModel` instance
    var liveModel = FirebaseAI.GetInstance(FirebaseAI.Backend.GoogleAI()).GetLiveModel(
      modelName: "<var translate="no">GEMINI_LIVE_MODEL_NAME</var>",
      liveGenerationConfig: config
    );

    // ...

You can find a[description of each parameter](https://firebase.google.com/docs/ai-logic/model-parameters#parameters-descriptions-gemini)in the next section of this page.

### Description of parameters (Gemini)

Here is a high-level overview of the available parameters, as applicable. You can find a[comprehensive list of parameters and their values](https://ai.google.dev/api/generate-content#generationconfig)in theGemini Developer APIdocumentation.

|              Parameter               |                                                                                                                                                                           Description                                                                                                                                                                           |    Default value     |
|--------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------|
| Audio timestamp `audioTimestamp`     | A boolean that enables timestamp understanding for audio-only input files. *Only applicable when using`generateContent`or`generateContentStream`calls and the input type is an audio-only file.*                                                                                                                                                                | `false`              |
| Candidate count `candidateCount`     | Specifies the number of response variations to return. For each request, you're charged for the output tokens of all candidates, but you're only charged once for the input tokens. Supported values:`1`-`8`(inclusive) *Only applicable when using`generateContent`and the latestGeminimodels. TheLive APImodels and`generateContentStream`are not supported.* | `1`                  |
| Frequency penalty `frequencyPenalty` | Controls the probability of including tokens that repeatedly appear in the generated response. Positive values penalize tokens that repeatedly appear in the generated content, decreasing the probability of repeating content.                                                                                                                                | ---                  |
| Max output tokens `maxOutputTokens`  | Specifies the maximum number of tokens that can be generated in the response.                                                                                                                                                                                                                                                                                   | ---                  |
| Presence penalty `presencePenalty`   | Controls the probability of including tokens that already appear in the generated response. Positive values penalize tokens that already appear in the generated content, increasing the probability of generating more diverse content.                                                                                                                        | ---                  |
| Stop sequences `stopSequences`       | Specifies a list of strings that tells the model to stop generating content if one of the strings is encountered in the response. *Only applicable when using a`GenerativeModel`configuration.*                                                                                                                                                                 | ---                  |
| Temperature `temperature`            | Controls the degree of randomness in the response. Lower temperatures result in more deterministic responses, and higher temperatures result in more diverse or creative responses.                                                                                                                                                                             | Depends on the model |
| Top-K `topK`                         | Limits the number of highest probability words used in the generated content. A top-K value of`1`means the next selected token should be*the most probable* among all tokens in the model's vocabulary, while a top-K value of`n`means that the next token should be selected from among*the*n*most probable*tokens (all based on the temperature that's set).  | Depends on the model |
| Top-P `topP`                         | Controls diversity of generated content. Tokens are selected from the most probable (see top-K above) to least probable until the sum of their probabilities equals the top-P value.                                                                                                                                                                            | Depends on the model |
| Response modality `responseModality` | Specifies the type of streamed output when using theLive APIor native multimodal output by aGeminimodel, for example text, audio, or images. *Only applicable when using theLive APImodels, or when using aGeminimodel capable of multimodal output.*                                                                                                           | ---                  |
| Speech (voice) `speechConfig`        | Specifies the voice used for the streamed audio output when using theLive API. *Only applicable when using theLive APImodels.*                                                                                                                                                                                                                                  | `Puck`               |

| **Note** : The following two configurations are also supported in the`GenerationConfig`:
|
| - [Generating structured output (like JSON)](https://firebase.google.com/docs/ai-logic/generate-structured-output)is controlled by using the`responseMimeType`and`responseSchema`parameters.
| - [Specifying a thinking-related configuration](https://firebase.google.com/docs/ai-logic/thinking)(like a*thinking budget* and whether to include*thought summaries* ) is controlled by using the`thinkingConfig`(only applicable forGemini 3andGemini 2.5models).

<br />

*** ** * ** ***

## ConfigureImagenmodels

|----------------------------------------------------------------------------------------------------------------------------------|
| *Click yourImagen APIprovider to view provider-specific content and code on this page.* Gemini Developer APIVertex AI Gemini API |

This section shows you how to[set up a configuration](https://firebase.google.com/docs/ai-logic/model-parameters#config-imagen)for use withImagenmodels and provides a[description of each parameter](https://firebase.google.com/docs/ai-logic/model-parameters#parameters-descriptions-imagen).

### Set up a model configuration (Imagen)

The configuration is maintained for the lifetime of the instance. If you want to use a different config, create a new`ImagenModel`instance with that config.  

### Swift

Set the values of the parameters in an[`ImagenGenerationConfig`](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/ImagenGenerationConfig)as part of creating an`ImagenModel`instance.  


    import FirebaseAILogic

    // Set parameter values in a `ImagenGenerationConfig` (example values shown here)
    let config = ImagenGenerationConfig(
      negativePrompt: "frogs",
      numberOfImages: 2,
      aspectRatio: .landscape16x9,
      imageFormat: .jpeg(compressionQuality: 100),
      addWatermark: false
    )

    // Initialize the Gemini Developer API backend service
    // Specify the config as part of creating the `ImagenModel` instance
    let model = FirebaseAI.firebaseAI(backend: .googleAI()).imagenModel(
      modelName: "<var translate="no">IMAGEN_MODEL_NAME</var>",
      generationConfig: config
    )

    // ...

### Kotlin

Set the values of the parameters in an[`ImagenGenerationConfig`](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig)as part of creating an`ImagenModel`instance.  


    // ...

    // Set parameter values in a `ImagenGenerationConfig` (example values shown here)
    val config = ImagenGenerationConfig {
        negativePrompt = "frogs",
        numberOfImages = 2,
        aspectRatio = ImagenAspectRatio.LANDSCAPE_16x9,
        imageFormat = ImagenImageFormat.jpeg(compressionQuality = 100),
        addWatermark = false
    }

    // Initialize the Gemini Developer API backend service
    // Specify the config as part of creating the `GenerativeModel` instance
    val model = Firebase.ai(backend = GenerativeBackend.vertexAI()).imagenModel(
        modelName = "<var translate="no">IMAGEN_MODEL_NAME</var>",
        generationConfig = config
    )

    // ...

### Java

Set the values of the parameters in an[`ImagenGenerationConfig`](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenGenerationConfig)as part of creating an`ImagenModel`instance.  


    // ...

    // Set parameter values in a `ImagenGenerationConfig` (example values shown here)
    ImagenGenerationConfig config = new ImagenGenerationConfig.Builder()
        .setNegativePrompt("frogs")
        .setNumberOfImages(2)
        .setAspectRatio(ImagenAspectRatio.LANDSCAPE_16x9)
        .setImageFormat(ImagenImageFormat.jpeg(100))
        .setAddWatermark(false)
        .build();

    // Specify the config as part of creating the `ImagenModel` instance
    ImagenModelFutures model = ImagenModelFutures.from(
            FirebaseAI.getInstance(GenerativeBackend.googleAI())
                    .imagenModel(
                        "<var translate="no">IMAGEN_MODEL_NAME</var>",
                        config
                    );
    );

    // ...

### Web

Set the values of the parameters in an[`ImagenGenerationConfig`](https://firebase.google.com/docs/reference/js/ai.imagengenerationconfig)as part of creating an`ImagenModel`instance.  


    // ...

    // Initialize the Gemini Developer API backend service
    const ai = getAI(firebaseApp, { backend: new GoogleAIBackend() });

    // Set parameter values in a `ImagenGenerationConfig` (example values shown here)
    const generationConfig = {
      negativePrompt: "frogs",
      numberOfImages: 2,
      aspectRatio: ImagenAspectRatio.LANDSCAPE_16x9,
      imageFormat: ImagenImageFormat.jpeg(100),
      addWatermark: false
    };

    // Specify the config as part of creating the `ImagenModel` instance
    const model = getImagenModel(ai, { model: "<var translate="no">IMAGEN_MODEL_NAME</var>", generationConfig });

    // ...

### Dart

Set the values of the parameters in an[`ImagenGenerationConfig`](https://pub.dev/documentation/firebase_ai/latest/firebase_ai/ImagenGenerationConfig-class.html)as part of creating an`ImagenModel`instance.  


    // ...

    // Set parameter values in a `ImagenGenerationConfig` (example values shown here)
    final generationConfig = ImagenGenerationConfig(
      negativePrompt: 'frogs',
      numberOfImages: 2,
      aspectRatio: ImagenAspectRatio.landscape16x9,
      imageFormat: ImagenImageFormat.jpeg(compressionQuality: 100)
      addWatermark: false
    );

    // Initialize the Gemini Developer API backend service
    // Specify the config as part of creating the `ImagenModel` instance
    final model = FirebaseAI.googleAI().imagenModel(
      model: '<var translate="no">IMAGEN_MODEL_NAME</var>',
      config: generationConfig,
    );

    // ...

### Unity

Set the values of the parameters in an[`ImagenGenerationConfig`](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/imagen-generation-config)as part of creating an`ImagenModel`instance.  


    using Firebase.AI;

    // Set parameter values in a `ImagenGenerationConfig` (example values shown here)
    var config = new ImagenGenerationConfig(
      numberOfImages: 2,
      aspectRatio: ImagenAspectRatio.Landscape16x9,
      imageFormat: ImagenImageFormat.Jpeg(100)
    );

    // Initialize the Gemini Developer API backend service
    // Specify the config as part of creating the `ImagenModel` instance
    var model = FirebaseAI.GetInstance(FirebaseAI.Backend.GoogleAI()).GetImagenModel(
      modelName: "imagen-4.0-generate-001",
      generationConfig: config
    );

    // ...

You can find a[description of each parameter](https://firebase.google.com/docs/ai-logic/model-parameters#parameters-descriptions-imagen)in the next section of this page.

### Description of parameters (Imagen)

Here is a high-level overview of the available parameters, as applicable. You can find a[comprehensive list of parameters and their values](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/imagen-api#parameter_list)in theGoogle Clouddocumentation.

|                                                            Parameter                                                            |                                                                                                                                                                     Description                                                                                                                                                                      |                                  Default value                                   |
|---------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| [Negative prompt](https://cloud.google.com/vertex-ai/generative-ai/docs/image/generate-images#negative-prompt) `negativePrompt` | A description of what you want to omit in generated images This parameter is not yet supported by`imagen-3.0-generate-002`.                                                                                                                                                                                                                          | ---                                                                              |
| Number of results `numberOfImages`                                                                                              | The number of generated images returned for each request                                                                                                                                                                                                                                                                                             | default is one image                                                             |
| [Aspect ratio](https://cloud.google.com/vertex-ai/generative-ai/docs/image/generate-images#aspect-ratio) `aspectRatio`          | The ratio of width to height of generated images                                                                                                                                                                                                                                                                                                     | default is square (1:1)                                                          |
| [Image format](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/imagen-api#output-options) `imageFormat`   | The output options, like the image format (MIME type) and level of compression of generated images                                                                                                                                                                                                                                                   | default MIME type is PNG default compression is 75 (if MIME type is set to JPEG) |
| Watermark `addWatermark`                                                                                                        | Whether to add a non-visible digital watermark (called a[SynthID](https://deepmind.google/technologies/synthid/?db=rachelsaunders)) to generated images                                                                                                                                                                                              | default is`true`                                                                 |
| [Person generation](https://cloud.google.com/vertex-ai/generative-ai/docs/image/overview#person-face-gen) `personGeneration`    | Whether to allow generation of people by the model                                                                                                                                                                                                                                                                                                   | default depends on the model                                                     |
| Include safety attributes `includeSafetyAttributes`                                                                             | Whether to enable rounded Responsible AI scores for a list of safety attributes in responses for unfiltered input and output Safety attribute categories:`"Death, Harm & Tragedy"`,`"Firearms & Weapons"`,`"Hate"`,`"Health"`,`"Illicit Drugs"`,`"Politics"`,`"Porn"`,`"Religion & Belief"`,`"Toxic"`,`"Violence"`,`"Vulgarity"`,`"War & Conflict"`. | default is`false`                                                                |

| **Note** :Firebase AI Logicdoes*not* yet support the following parameters:
|
| - Specifying a[seed number](https://cloud.google.com/vertex-ai/generative-ai/docs/image/generate-images#seed)(the`seed`parameter)
| - Setting aGoogle Cloud Storagebucket for storing generated images (the`storageUri`parameter)
| - Disabling[prompt enhancement](https://cloud.google.com/vertex-ai/generative-ai/docs/image/generate-images#prompt-rewriter)(the`enhancePrompt`parameter)

<br />

*** ** * ** ***

## Other options to control content generation

- Learn more about[prompt design](https://firebase.google.com/docs/ai-logic/prompt-design)so that you can influence the model to generate output specific to your needs.
- Use[safety settings](https://firebase.google.com/docs/ai-logic/safety-settings)to adjust the likelihood of getting responses that may be considered harmful, including hate speech and sexually explicit content.
- Set[system instructions](https://firebase.google.com/docs/ai-logic/system-instructions)to steer the behavior of the model. This feature is like a preamble that you add before the model gets exposed to any further instructions from the end user.
- Pass a[*response schema*](https://firebase.google.com/docs/ai-logic/generate-structured-output)along with the prompt to specify a specific output schema. This feature is most commonly used when[generating JSON output](https://firebase.google.com/docs/ai-logic/generate-structured-output#generate-json-basic), but it can also be used for[classification tasks](https://firebase.google.com/docs/ai-logic/generate-structured-output#generate-enum-basic)(like when you want the model to use specific labels or tags).