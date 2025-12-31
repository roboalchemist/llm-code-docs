# Source: https://firebase.google.com/docs/ai-logic/safety-settings.md.txt

<br />

You can use safety settings to adjust the likelihood of getting responses that may be considered harmful. By default, safety settings block content with medium and/or high probability of being unsafe content across all dimensions.

[arrow_downwardJump toGeminisafety settings](https://firebase.google.com/docs/ai-logic/safety-settings#gemini)[arrow_downwardJump toImagensafety settings](https://firebase.google.com/docs/ai-logic/safety-settings#imagen)

## Safety settings forGeminimodels

|----------------------------------------------------------------------------------------------------------------------------------|
| *Click yourGemini APIprovider to view provider-specific content and code on this page.* Gemini Developer APIVertex AI Gemini API |

Learn more about[safety settings](https://ai.google.dev/gemini-api/docs/safety-settings)forGeminimodels in theGemini Developer APIdocumentation.**Note:** Safety settings aren't applicable if you're using the[Gemini Live API](https://firebase.google.com/docs/ai-logic/live-api).  

### Swift

You configure[`SafetySettings`](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/SafetySetting)when you create a`GenerativeModel`instance.

Example with one safety setting:  


    import FirebaseAILogic

    // Specify the safety settings as part of creating the `GenerativeModel` instance
    let model = FirebaseAI.firebaseAI(backend: .googleAI()).generativeModel(
      modelName: "<var translate="no">GEMINI_MODEL_NAME</var>",
      safetySettings: [
        SafetySetting(harmCategory: .harassment, threshold: .blockOnlyHigh)
      ]
    )

    // ...

Example with multiple safety settings:  


    import FirebaseAILogic

    let harassmentSafety = SafetySetting(harmCategory: .harassment, threshold: .blockOnlyHigh)
    let hateSpeechSafety = SafetySetting(harmCategory: .hateSpeech, threshold: .blockMediumAndAbove)

    // Specify the safety settings as part of creating the `GenerativeModel` instance
    let model = FirebaseAI.firebaseAI(backend: .googleAI()).generativeModel(
      modelName: "<var translate="no">GEMINI_MODEL_NAME</var>",
      safetySettings: [harassmentSafety, hateSpeechSafety]
    )

    // ...

### Kotlin

You configure[`SafetySettings`](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/SafetySetting)when you create a`GenerativeModel`instance.

Example with one safety setting:  


    import com.google.firebase.vertexai.type.HarmBlockThreshold
    import com.google.firebase.vertexai.type.HarmCategory
    import com.google.firebase.vertexai.type.SafetySetting

    // Specify the safety settings as part of creating the `GenerativeModel` instance
    val model = Firebase.ai(backend = GenerativeBackend.googleAI()).generativeModel(
        modelName = "<var translate="no">GEMINI_MODEL_NAME</var>",
        safetySettings = listOf(
            SafetySetting(HarmCategory.HARASSMENT, HarmBlockThreshold.ONLY_HIGH)
        )
    )

    // ...

Example with multiple safety settings:  


    import com.google.firebase.vertexai.type.HarmBlockThreshold
    import com.google.firebase.vertexai.type.HarmCategory
    import com.google.firebase.vertexai.type.SafetySetting

    val harassmentSafety = SafetySetting(HarmCategory.HARASSMENT, HarmBlockThreshold.ONLY_HIGH)
    val hateSpeechSafety = SafetySetting(HarmCategory.HATE_SPEECH, HarmBlockThreshold.MEDIUM_AND_ABOVE)

    // Specify the safety settings as part of creating the `GenerativeModel` instance
    val model = Firebase.ai(backend = GenerativeBackend.googleAI()).generativeModel(
        modelName = "<var translate="no">GEMINI_MODEL_NAME</var>",
        safetySettings = listOf(harassmentSafety, hateSpeechSafety)
    )

    // ...

### Java

You configure[`SafetySettings`](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/SafetySetting)when you create a`GenerativeModel`instance.  


    SafetySetting harassmentSafety = new SafetySetting(HarmCategory.HARASSMENT,
    HarmBlockThreshold.ONLY_HIGH);

    // Specify the safety settings as part of creating the `GenerativeModel` instance
    GenerativeModelFutures model = GenerativeModelFutures.from(
            FirebaseAI.getInstance(GenerativeBackend.googleAI())
                    .generativeModel(
                      /* modelName */ "<var translate="no">GEMINI_MODEL_NAME</var>",
                      /* generationConfig is optional */ null,
                      Collections.singletonList(harassmentSafety)
                    );
    );

    // ...

Example with multiple safety settings:  


    SafetySetting harassmentSafety = new SafetySetting(HarmCategory.HARASSMENT,
    HarmBlockThreshold.ONLY_HIGH);

    SafetySetting hateSpeechSafety = new SafetySetting(HarmCategory.HATE_SPEECH,
    HarmBlockThreshold.MEDIUM_AND_ABOVE);

    // Specify the safety settings as part of creating the `GenerativeModel` instance
    GenerativeModelFutures model = GenerativeModelFutures.from(
            FirebaseAI.getInstance(GenerativeBackend.googleAI())
                    .generativeModel(
                      /* modelName */ "<var translate="no">GEMINI_MODEL_NAME</var>",
                      /* generationConfig is optional */ null,
                      List.of(harassmentSafety, hateSpeechSafety)
                    );
    );

    // ...

### Web

You configure[`SafetySettings`](https://firebase.google.com/docs/reference/js/ai.safetysetting)when you create a`GenerativeModel`instance.

Example with one safety setting:  


    import { HarmBlockThreshold, HarmCategory, getAI, getGenerativeModel, GoogleAIBackend } from "firebase/ai";

    // ...

    const ai = getAI(firebaseApp, { backend: new GoogleAIBackend() });

    const safetySettings = [
      {
        category: HarmCategory.HARM_CATEGORY_HARASSMENT,
        threshold: HarmBlockThreshold.BLOCK_ONLY_HIGH,
      },
    ];

    // Specify the safety settings as part of creating the `GenerativeModel` instance
    const model = getGenerativeModel(ai, { model: "<var translate="no">GEMINI_MODEL_NAME</var>", safetySettings });

    // ...

Example with multiple safety settings:  


    import { HarmBlockThreshold, HarmCategory, getAI, getGenerativeModel, GoogleAIBackend } from "firebase/ai";

    // ...

    const ai = getAI(firebaseApp, { backend: new GoogleAIBackend() });

    const safetySettings = [
      {
        category: HarmCategory.HARM_CATEGORY_HARASSMENT,
        threshold: HarmBlockThreshold.BLOCK_ONLY_HIGH,
      },
      {
        category: HarmCategory.HARM_CATEGORY_HATE_SPEECH,
        threshold: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
      },
    ];

    // Specify the safety settings as part of creating the `GenerativeModel` instance
    const model = getGenerativeModel(ai, { model: "<var translate="no">GEMINI_MODEL_NAME</var>", safetySettings });

    // ...

### Dart

You configure[`SafetySettings`](https://pub.dev/documentation/firebase_ai/latest/firebase_ai/SafetySetting-class.html)when you create a`GenerativeModel`instance.

Example with one safety setting:  


    // ...

    final safetySettings = [
      SafetySetting(HarmCategory.harassment, HarmBlockThreshold.high)
    ];

    // Specify the safety settings as part of creating the `GenerativeModel` instance
    final model = FirebaseAI.googleAI().generativeModel(
      model: '<var translate="no">GEMINI_MODEL_NAME</var>',
      safetySettings: safetySettings,
    );

    // ...

Example with multiple safety settings:  


    // ...

    final safetySettings = [
      SafetySetting(HarmCategory.harassment, HarmBlockThreshold.high),
      SafetySetting(HarmCategory.hateSpeech, HarmBlockThreshold.high),
    ];

    // Specify the safety settings as part of creating the `GenerativeModel` instance
    final model = FirebaseAI.googleAI().generativeModel(
      model: '<var translate="no">GEMINI_MODEL_NAME</var>',
      safetySettings: safetySettings,
    );

    // ...

### Unity

You configure[`SafetySettings`](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/safety-setting)when you create a`GenerativeModel`instance.

Example with one safety setting:  


    // ...

    // Specify the safety settings as part of creating the `GenerativeModel` instance
    var ai = FirebaseAI.GetInstance(FirebaseAI.Backend.GoogleAI());
    var model = ai.GetGenerativeModel(
      modelName: "<var translate="no">GEMINI_MODEL_NAME</var>",
      safetySettings: new SafetySetting[] {
        new SafetySetting(HarmCategory.Harassment, SafetySetting.HarmBlockThreshold.OnlyHigh)
      }
    );

    // ...

Example with multiple safety settings:  


    // ...

    var harassmentSafety = new SafetySetting(HarmCategory.Harassment, SafetySetting.HarmBlockThreshold.OnlyHigh);
    var hateSpeechSafety = new SafetySetting(HarmCategory.HateSpeech, SafetySetting.HarmBlockThreshold.MediumAndAbove);

    // Specify the safety settings as part of creating the `GenerativeModel` instance
    var ai = FirebaseAI.GetInstance(FirebaseAI.Backend.GoogleAI());
    var model = ai.GetGenerativeModel(
      modelName: "<var translate="no">GEMINI_MODEL_NAME</var>",
      safetySettings: new SafetySetting[] { harassmentSafety, hateSpeechSafety }
    );

    // ...

## Safety settings forImagenmodels

|----------------------------------------------------------------------------------------------------------------------------------|
| *Click yourGemini APIprovider to view provider-specific content and code on this page.* Gemini Developer APIVertex AI Gemini API |

Learn about all the[supported safety settings and their available values](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/imagen-api#parameter_list)forImagenmodels in theGoogle Clouddocumentation.  

### Swift

You configure[`ImagenSafetySettings`](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/ImagenSafetySettings)when you create an`ImagenModel`instance.  


    import FirebaseAILogic

    // Specify the safety settings as part of creating the `ImagenModel` instance
    let model = FirebaseAI.firebaseAI(backend: .googleAI()).imagenModel(
      modelName: "<var translate="no">IMAGEN_MODEL_NAME</var>",
      safetySettings: ImagenSafetySettings(
        safetyFilterLevel: .blockLowAndAbove,
        personFilterLevel: .allowAdult
      )
    )

    // ...

### Kotlin

You configure[`ImagenSafetySettings`](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenSafetySettings)when you create an`ImagenModel`instance.  


    // Specify the safety settings as part of creating the `ImagenModel` instance
    val model = Firebase.ai(backend = GenerativeBackend.googleAI()).imagenModel(
      modelName = "<var translate="no">IMAGEN_MODEL_NAME</var>",
      safetySettings = ImagenSafetySettings(
        safetyFilterLevel = ImagenSafetyFilterLevel.BLOCK_LOW_AND_ABOVE,
        personFilterLevel = ImagenPersonFilterLevel.BLOCK_ALL
      )
    )

    // ...

### Java

You configure[`ImagenSafetySettings`](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenSafetySettings)when you create an`ImagenModel`instance.  


    // Specify the safety settings as part of creating the `ImagenModel` instance
    ImagenModelFutures model = ImagenModelFutures.from(
            FirebaseAI.getInstance(GenerativeBackend.googleAI())
                    .imagenModel(
                      /* modelName */ "<var translate="no">IMAGEN_MODEL_NAME</var>",
                      /* imageGenerationConfig */ null);
    );

    // ...

### Web

You configure[`ImagenSafetySettings`](https://firebase.google.com/docs/reference/js/ai.imagensafetysettings)when you create an`ImagenModel`instance.  


    // ...

    const ai = getAI(firebaseApp, { backend: new GoogleAIBackend() });

    // Specify the safety settings as part of creating the `ImagenModel` instance
    const model = getImagenModel(
      ai,
      {
        model: "<var translate="no">IMAGEN_MODEL_NAME</var>",
        safetySettings: {
          safetyFilterLevel: ImagenSafetyFilterLevel.BLOCK_LOW_AND_ABOVE,
          personFilterLevel: ImagenPersonFilterLevel.ALLOW_ADULT,
        }
      }
    );

    // ...

### Dart

You configure[`ImagenSafetySettings`](https://pub.dev/documentation/firebase_ai/latest/firebase_ai/ImagenSafetySettings-class.html)when you create an`ImagenModel`instance.  


    // ...

    // Specify the safety settings as part of creating the `ImagenModel` instance
    final model = FirebaseAI.googleAI().imagenModel(
      model: '<var translate="no">IMAGEN_MODEL_NAME</var>',
      safetySettings: ImagenSafetySettings(
        ImagenSafetyFilterLevel.blockLowAndAbove,
        ImagenPersonFilterLevel.allowAdult,
      ),
    );

    // ...

### Unity

You configure[`ImagenSafetySettings`](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/imagen-safety-settings)when you create an`ImagenModel`instance.  


    using Firebase.AI;

    // Specify the safety settings as part of creating the `ImagenModel` instance
    var model = FirebaseAI.GetInstance(FirebaseAI.Backend.GoogleAI()).GetImagenModel(
      modelName: "<var translate="no">IMAGEN_MODEL_NAME</var>",
      safetySettings: new ImagenSafetySettings(
        safetyFilterLevel: ImagenSafetySettings.SafetyFilterLevel.BlockLowAndAbove,
        personFilterLevel: ImagenSafetySettings.PersonFilterLevel.AllowAdult
      )
    );

    // ...

## Other options to control content generation

- Learn more about[prompt design](https://firebase.google.com/docs/ai-logic/prompt-design)so that you can influence the model to generate output specific to your needs.
- Configure[model parameters](https://firebase.google.com/docs/ai-logic/model-parameters)to control how the model generates a response. ForGeminimodels, these parameters include max output tokens, temperature, topK, and topP. ForImagenmodels, these include aspect ratio, person generation, watermarking, etc.
- Set[system instructions](https://firebase.google.com/docs/ai-logic/system-instructions)to steer the behavior of the model. This feature is like a preamble that you add before the model gets exposed to any further instructions from the end user.
- Pass a[*response schema*](https://firebase.google.com/docs/ai-logic/generate-structured-output)along with the prompt to specify a specific output schema. This feature is most commonly used when[generating JSON output](https://firebase.google.com/docs/ai-logic/generate-structured-output#generate-json-basic), but it can also be used for[classification tasks](https://firebase.google.com/docs/ai-logic/generate-structured-output#generate-enum-basic)(like when you want the model to use specific labels or tags).