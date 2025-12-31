# Source: https://firebase.google.com/docs/ai-logic/system-instructions.md.txt

<br />

*System instructions*are like a "preamble" that you add before the model gets exposed to any further instructions from the end user. It lets you steer the behavior of the model based on your specific needs and use cases.

System instructions are supported by allGeminimodels. They aren't supported by theImagenmodels.

[arrow_downwardJump to code samples](https://firebase.google.com/docs/ai-logic/system-instructions#set-si)

<br />

When you set a system instruction, you give the model additional context to understand the task, provide more customized responses, and adhere to specific guidelines over the full user interaction with the model. You can specify product-level behavior in system instructions, separate from prompts provided by end users. For example, you can include things like the role or persona, contextual information, and formatting instructions.

You can use system instructions in many ways, including:

- Defining a persona or role (for a chatbot, for example)
- Defining output format (Markdown, YAML, etc.)
- Defining output style and tone (for example, verbosity, formality, and target reading level)
- Defining goals or rules for the task (for example, returning a code snippet without further explanations)
- Providing additional context for the prompt (for example, a knowledge cutoff)

When a system instruction is set, it applies to the entire request. It works across multiple user and model turns when included in the prompt. Though system instructions are separate from the contents of prompt, they are still part of your overall prompts and therefore are subject to standard data use policies.
| **Note:** System instructions can help guide the model to follow instructions, but they don't fully prevent jailbreaks or leaks. We recommend exercising caution around putting any sensitive information in system instructions.

## Set system instructions

|----------------------------------------------------------------------------------------------------------------------------------|
| *Click yourGemini APIprovider to view provider-specific content and code on this page.* Gemini Developer APIVertex AI Gemini API |

| **Note:** For the majority of use cases when accessing aGeminimodel, you set system instructions when creating the`GenerativeModel`instance. However, if you're[setting system instructions when using theGemini Live API](https://firebase.google.com/docs/ai-logic/system-instructions#si-gemini-live-api), you set them when creating the`LiveModel`instance.

### Set system instructions for general use cases

### Swift

You specify[`systemInstruction`](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Classes/FirebaseAI)when you create a`GenerativeModel`instance.  


    import FirebaseAILogic

    // Specify the system instructions as part of creating the `GenerativeModel` instance
    let model = FirebaseAI.firebaseAI(backend: .googleAI()).generativeModel(
      modelName: "<var translate="no">GEMINI_MODEL_NAME</var>",
      systemInstruction: ModelContent(role: "system", parts: "You are a cat. Your name is Neko.")
    )

### Kotlin

You specify[`systemInstruction`](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/FirebaseVertexAI#generativeModel(kotlin.String,com.google.firebase.vertexai.type.GenerationConfig,kotlin.collections.List,kotlin.collections.List,com.google.firebase.vertexai.type.ToolConfig,com.google.firebase.vertexai.type.Content,com.google.firebase.vertexai.type.RequestOptions))when you create a`GenerativeModel`instance.  


    // Specify the system instructions as part of creating the `GenerativeModel` instance
    val model = Firebase.ai(backend = GenerativeBackend.googleAI()).generativeModel(
      modelName = "<var translate="no">GEMINI_MODEL_NAME</var>",
      systemInstruction = content { text("You are a cat. Your name is Neko.") }
    )

### Java

You specify[`systemInstruction`](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseVertexAI#generativeModel(kotlin.String,com.google.firebase.vertexai.type.GenerationConfig,kotlin.collections.List,kotlin.collections.List,com.google.firebase.vertexai.type.ToolConfig,com.google.firebase.vertexai.type.Content,com.google.firebase.vertexai.type.RequestOptions))when you create a`GenerativeModel`instance.  


    // Specify the system instructions as part of creating the `GenerativeModel` instance
    GenerativeModel ai = FirebaseAI.getInstance(GenerativeBackend.googleAI())
        .generativeModel(
          /* modelName */ "<var translate="no">GEMINI_MODEL_NAME</var>",
          /* generationConfig (optional) */ null,
          /* safetySettings (optional) */ null,
          /* requestOptions (optional) */ new RequestOptions(),
          /* tools (optional) */ null,
          /* toolsConfig (optional) */ null,
          /* systemInstruction (optional) */ new Content.Builder().addText("You are a cat. Your name is Neko.").build()
        );

    GenerativeModelFutures model = GenerativeModelFutures.from(ai);

### Web

You specify[`systemInstruction`](https://firebase.google.com/docs/reference/js/ai.generativemodel#generativemodelsysteminstruction)when you create a`GenerativeModel`instance.  


    // ...

    const ai = getAI(firebaseApp, { backend: new GoogleAIBackend() });

    // Specify the system instructions as part of creating the `GenerativeModel` instance
    const model = getGenerativeModel(ai, {
      model: "<var translate="no">GEMINI_MODEL_NAME</var>",
      systemInstruction: "You are a cat. Your name is Neko."
    });

### Dart

You specify[`systemInstruction`](https://pub.dev/documentation/firebase_ai/latest/firebase_ai/FirebaseVertexAI/generativeModel.html)when you create a`GenerativeModel`instance.  


    // ...

    // Specify the system instructions as part of creating the `GenerativeModel` instance
    final model = FirebaseAI.googleAI().generativeModel(
      model: '<var translate="no">GEMINI_MODEL_NAME</var>',
      systemInstruction: Content.system('You are a cat. Your name is Neko.'),
    );

    // ...

### Unity

You specify[`systemInstruction`](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/firebase-a-i#getgenerativemodel)when you create a`GenerativeModel`instance.  


    // ...

    var ai = FirebaseAI.GetInstance(FirebaseAI.Backend.GoogleAI());

    // Specify the system instructions as part of creating the `GenerativeModel` instance
    var model = ai.GetGenerativeModel(
      modelName: "<var translate="no">GEMINI_MODEL_NAME</var>",
      systemInstruction: ModelContent.Text("You are a cat. Your name is Neko.")
    );

### Set system instructions for theGemini Live API

### Swift

You specify[`systemInstruction`](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Classes/FirebaseAI#parameters_3)when you create a`LiveModel`instance.  


    // ...

    // Specify the system instructions as part of creating the `liveModel` instance
    let liveModel = FirebaseAI.firebaseAI(backend: .googleAI()).liveModel(
      modelName: "<var translate="no">GEMINI_LIVE_MODEL_NAME</var>",
      systemInstruction: ModelContent(role: "system", parts: "You are a cat. Your name is Neko."),
      // ...
    )

    // ...

### Kotlin

You specify[`systemInstruction`](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/FirebaseVertexAI#liveModel(kotlin.String,com.google.firebase.vertexai.type.LiveGenerationConfig,kotlin.collections.List,com.google.firebase.vertexai.type.Content,com.google.firebase.vertexai.type.RequestOptions))when you create a`LiveModel`instance.  


    // ...

    // Specify the system instructions as part of creating the `LiveModel` instance
    val liveModel = Firebase.ai(backend = GenerativeBackend.googleAI()).liveModel(
        modelName = "<var translate="no">GEMINI_LIVE_MODEL_NAME</var>",
        systemInstruction = content { text("You are a cat. Your name is Neko.") },
        // ...
    )

    // ...

### Java

You specify[`systemInstruction`](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseVertexAI#liveModel(kotlin.String,com.google.firebase.vertexai.type.LiveGenerationConfig,kotlin.collections.List,com.google.firebase.vertexai.type.Content,com.google.firebase.vertexai.type.RequestOptions))when you create a`LiveModel`instance.  


    // ...

    // Specify the system instructions as part of creating the `LiveModel` instance
    LiveGenerativeModel lm = FirebaseAI.getInstance(GenerativeBackend.googleAI()).liveModel(
              /* modelName */ "<var translate="no">GEMINI_LIVE_MODEL_NAME</var>",
              /* systemInstruction (optional) */ new Content.Builder().addText("You are a cat. Your name is Neko.").build()
              // ...
    );

    LiveModelFutures liveModel = LiveModelFutures.from(lm);

    // ...

### Web

You specify[`systemInstruction`](https://firebase.google.com/docs/reference/js/ai.livegenerativemodel#livegenerativemodelsysteminstruction)when you create a`LiveGenerativeModel`instance.  


    // ...

    const ai = getAI(firebaseApp, { backend: new GoogleAIBackend() });

    // Specify the system instructions as part of creating the `LiveGenerativeModel` instance
    const liveModel = getLiveGenerativeModel(ai, {
      model: "<var translate="no">GEMINI_LIVE_MODEL_NAME</var>",
      systemInstruction: "You are a cat. Your name is Neko.",
      // ...
    });

    // ...

### Dart

You specify[`systemInstruction`](https://pub.dev/documentation/firebase_ai/latest/firebase_ai/FirebaseVertexAI/liveGenerativeModel.html)when you create a`LiveGenerativeModel`instance.  


    // ...

    // Specify the system instructions as part of creating the `liveGenerativeModel` instance
    final liveModel = FirebaseAI.googleAI().liveGenerativeModel(
      model: '<var translate="no">GEMINI_LIVE_MODEL_NAME</var>',
      systemInstruction: Content.system('You are a cat. Your name is Neko.'),
      // ...
    );

    // ...

### Unity

You specify[`systemInstruction`](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/firebase-a-i#getlivemodel)when you create a`LiveModel`instance.  


    // ...

    // Specify the system instructions as part of creating the `LiveModel` instance
    var liveModel = FirebaseAI.GetInstance(FirebaseAI.Backend.GoogleAI()).GetLiveModel(
      modelName: "<var translate="no">GEMINI_LIVE_MODEL_NAME</var>",
      systemInstruction: ModelContent.Text("You are a cat. Your name is Neko."),
      // ...
    );

    // ...

## Examples of system instructions

Here are some examples of system instructions that help steer the expected behavior of the model. Some examples also show an example prompt for which the system instruction would be helpful.

### Code generation

- **System instruction:**   
  You are a coding expert that specializes in rendering code for frontend interfaces. When I describe a component of a website I want to build, please return the HTML and CSS needed to do so. Do not give an explanation for this code. Also offer some UI design suggestions.

- **User prompt:**   
  Create a box in the middle of the page that contains a rotating selection of images each with a caption. The image in the center of the page should have shadowing behind it to make it stand out. It should also link to another page of the site. Leave the URL blank so that I can fill it in.

### Music chatbot

- **System instruction:**   
  You will respond as a music historian, demonstrating comprehensive knowledge across diverse musical genres and providing relevant examples. Your tone will be upbeat and enthusiastic, spreading the joy of music. If a question is not related to music, the response should be, "That is beyond my knowledge."

- **User prompt:**   
  If a person was born in the sixties, what was the most popular music genre being played? List five songs by bullet point.

### Formatted data generation

| **Note:** If you want more control and consistency for the generation of structured content (like JSON output), we recommend providing a`responseSchema`in your request. Learn more about[generating structured output](https://firebase.google.com/docs/ai-logic/generate-structured-output).

- **System instruction:**   
  You are an assistant for home cooks. You receive a list of ingredients and respond with a list of recipes that use those ingredients. Recipes which need no extra ingredients should always be listed before those that do.

  Your response must be a JSON object containing 3 recipes. A recipe object has the following schema:
  - name: The name of the recipe
  - usedIngredients: Ingredients in the recipe that were provided in the list
  - otherIngredients: Ingredients in the recipe that were not provided in the list (omitted if there are no other ingredients)
  - description: A brief description of the recipe, written positively as if to sell it
- **User prompt:**

  - 1 lb bag frozen broccoli
  - 1 pint heavy cream
  - 1 lb pack cheese ends and pieces

## Other options to control content generation

- Learn more about[prompt design](https://firebase.google.com/docs/ai-logic/prompt-design)so that you can influence the model to generate output specific to your needs.
- Configure[model parameters](https://firebase.google.com/docs/ai-logic/model-parameters)to control how the model generates a response. ForGeminimodels, these parameters include max output tokens, temperature, topK, and topP. ForImagenmodels, these include aspect ratio, person generation, watermarking, etc.
- Use[safety settings](https://firebase.google.com/docs/ai-logic/safety-settings)to adjust the likelihood of getting responses that may be considered harmful, including hate speech and sexually explicit content.
- Pass a[*response schema*](https://firebase.google.com/docs/ai-logic/generate-structured-output)along with the prompt to specify a specific output schema. This feature is most commonly used when[generating JSON output](https://firebase.google.com/docs/ai-logic/generate-structured-output#generate-json-basic), but it can also be used for[classification tasks](https://firebase.google.com/docs/ai-logic/generate-structured-output#generate-enum-basic)(like when you want the model to use specific labels or tags).