# Source: https://firebase.google.com/docs/ai-logic/generate-structured-output.md.txt

<br />

TheGemini APIreturns responses as unstructured text by default. However, some use cases require structured text, like JSON. For example, you might be using the response for other downstream tasks that require an established data schema.

To ensure that the model's generated output always adheres to a specific schema, you can define a*response schema*which works like a blueprint for model responses. You can then directly extract data from the model's output with less post-processing.

Here are some examples:

- **Ensure that a model's response produces valid JSON and conforms to your provided schema.**   
  For example, the model can generate structured entries for recipes that always include the recipe name, list of ingredients, and steps. You can then more easily parse and display this information in the UI of your app.

- **Constrain how a model can respond during classification tasks.**   
  For example, you can have the model annotate text with a specific set of labels (for instance, a specific set of enums like`positive`and`negative`), rather than labels that the model produces (which could have a degree of variability like`good`,`positive`,`negative`, or`bad`).

| **Note:** Using a response schema to generate structured output is sometimes called "JSON mode" or "controlled generation".

This guide shows you how to generate JSON output by providing a`responseSchema`in a call to`generateContent`. It focuses on text-only input, but Gemini can also produce structured responses to multimodal requests that include images, videos, and audio as input.

At the bottom of this page are more examples, like how to[generate enum values as output](https://firebase.google.com/docs/ai-logic/generate-structured-output#generate-enum-basic).

## Before you begin

<br />

|----------------------------------------------------------------------------------------------------------------------------------|
| *Click yourGemini APIprovider to view provider-specific content and code on this page.* Gemini Developer APIVertex AI Gemini API |

<br />

If you haven't already, complete the[getting started guide](https://firebase.google.com/docs/ai-logic/get-started), which describes how to set up your Firebase project, connect your app to Firebase, add the SDK, initialize the backend service for your chosenGemini APIprovider, and create a`GenerativeModel`instance.

<br />

| All our docs assume that you're using the[](https://firebase.google.com/support/releases)latest versionsof theFirebase AI LogicSDKs.

<br />

For testing and iterating on your prompts, we recommend using[Google AI Studio](https://aistudio.google.com).

## **Step 1**: Define a response schema

Define a response schema to specify the structure of a model's output, the field names, and the expected data type for each field.

When a model generates its response, it uses the field name and context from your prompt. To make sure that your intent is clear, we recommend using a clear structure, unambiguous field names, and even descriptions as needed.

### Considerations for response schemas

Keep the following in mind when writing your response schema:

- The size of the response schema counts towards the input token limit.

- The response schema feature supports the following response MIME types:

  - **`application/json`**: output JSON as defined in the response schema (useful for structured output requirements)

  - **`text/x.enum`**: output an enum value as defined in the response schema (useful for classification tasks)

- The response schema feature supports the following schema fields:

  |----------------|-----------------------|-------------------------|
  | `enum` `items` | `maxItems` `nullable` | `properties` `required` |

  If you use an unsupported field, the model can still handle your request, but it ignores the field. Note that the list above is a subset of the OpenAPI 3.0 schema object.
- By default, forFirebase AI LogicSDKs, all fields are considered*required* unless you specify them as optional in an`optionalProperties`array. For these optional fields, the model can populate the fields or skip them. Note that this is opposite from the default behavior of the twoGemini APIproviders if you use their server SDKs or their API directly.

## **Step 2**: Generate JSON output using your response schema

<br />

|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *Before trying this sample, complete the[Before you begin](https://firebase.google.com/docs/ai-logic/generate-structured-output#before-you-begin)section of this guide to set up your project and app. **In that section, you'll also click a button for your chosenGemini APIprovider so that you see provider-specific content on this page**.* |

<br />

The following example shows how to generate structured JSON output.

When you create the`GenerativeModel`instance, specify the appropriate`responseMimeType`(in this example,`application/json`) as well as the`responseSchema`that you want the model to use.  

### Swift


    import FirebaseAILogic

    // Provide a JSON schema object using a standard format.
    // Later, pass this schema object into `responseSchema` in the generation config.
    let jsonSchema = Schema.object(
      properties: [
        "characters": Schema.array(
          items: .object(
            properties: [
              "name": .string(),
              "age": .integer(),
              "species": .string(),
              "accessory": .enumeration(values: ["hat", "belt", "shoes"]),
            ],
            optionalProperties: ["accessory"]
          )
        ),
      ]
    )

    // Initialize the Gemini Developer API backend service
    let ai = FirebaseAI.firebaseAI(backend: .googleAI())

    // Create a `GenerativeModel` instance with a model that supports your use case
    let model = ai.generativeModel(
      modelName: "gemini-2.5-flash",
      // In the generation config, set the `responseMimeType` to `application/json`
      // and pass the JSON schema object into `responseSchema`.
      generationConfig: GenerationConfig(
        responseMIMEType: "application/json",
        responseSchema: jsonSchema
      )
    )

    let prompt = "For use in a children's card game, generate 10 animal-based characters."

    let response = try await model.generateContent(prompt)
    print(response.text ?? "No text in response.")

### Kotlin

^*For Kotlin, the methods in this SDK are suspend functions and need to be called from a[Coroutine scope](https://developer.android.com/kotlin/coroutines).*^  


    // Provide a JSON schema object using a standard format.
    // Later, pass this schema object into `responseSchema` in the generation config.
    val jsonSchema = Schema.obj(
        mapOf("characters" to Schema.array(
            Schema.obj(
                mapOf(
                    "name" to Schema.string(),
                    "age" to Schema.integer(),
                    "species" to Schema.string(),
                    "accessory" to Schema.enumeration(listOf("hat", "belt", "shoes")),
                ),
                optionalProperties = listOf("accessory")
            )
        ))
    )

    // Initialize the Gemini Developer API backend service
    // Create a `GenerativeModel` instance with a model that supports your use case
    val model = Firebase.ai(backend = GenerativeBackend.googleAI()).generativeModel(
        modelName = "gemini-2.5-flash",
        // In the generation config, set the `responseMimeType` to `application/json`
        // and pass the JSON schema object into `responseSchema`.
        generationConfig = generationConfig {
            responseMimeType = "application/json"
            responseSchema = jsonSchema
        })

    val prompt = "For use in a children's card game, generate 10 animal-based characters."
    val response = generativeModel.generateContent(prompt)
    print(response.text)

### Java

^*For Java, the streaming methods in this SDK return a`Publisher`type from the[Reactive Streams library](https://www.reactive-streams.org/).*^  


    // Provide a JSON schema object using a standard format.
    // Later, pass this schema object into `responseSchema` in the generation config.
    Schema jsonSchema = Schema.obj(
            /* properties */
            Map.of(
                    "characters", Schema.array(
                            /* items */ Schema.obj(
                                    /* properties */
                                    Map.of("name", Schema.str(),
                                            "age", Schema.numInt(),
                                            "species", Schema.str(),
                                            "accessory",
                                            Schema.enumeration(
                                                    List.of("hat", "belt", "shoes")))
                            ))),
            List.of("accessory"));

    // In the generation config, set the `responseMimeType` to `application/json`
    // and pass the JSON schema object into `responseSchema`.
    GenerationConfig.Builder configBuilder = new GenerationConfig.Builder();
    configBuilder.responseMimeType = "application/json";
    configBuilder.responseSchema = jsonSchema;

    GenerationConfig generationConfig = configBuilder.build();

    // Initialize the Gemini Developer API backend service
    // Create a `GenerativeModel` instance with a model that supports your use case
    GenerativeModel ai = FirebaseAI.getInstance(GenerativeBackend.googleAI())
            .generativeModel(
                /* modelName */ "gemini-2.5-flash",
                /* generationConfig */ generationConfig);
    GenerativeModelFutures model = GenerativeModelFutures.from(ai);

    Content content = new Content.Builder()
        .addText("For use in a children's card game, generate 10 animal-based characters.")
        .build();

    // For illustrative purposes only. You should use an executor that fits your needs.
    Executor executor = Executors.newSingleThreadExecutor();

    ListenableFuture<GenerateContentResponse> response = model.generateContent(content);
    Futures.addCallback(
        response,
        new FutureCallback<GenerateContentResponse>() {
          @Override
          public void onSuccess(GenerateContentResponse result) {
            String resultText = result.getText();
            System.out.println(resultText);
          }

          @Override
          public void onFailure(Throwable t) {
            t.printStackTrace();
          }
        },
        executor);

### Web


    import { initializeApp } from "firebase/app";
    import { getAI, getGenerativeModel, GoogleAIBackend, Schema } from "firebase/ai";

    // TODO(developer) Replace the following with your app's Firebase configuration
    // See: https://firebase.google.com/docs/web/learn-more#config-object
    const firebaseConfig = {
      // ...
    };

    // Initialize FirebaseApp
    const firebaseApp = initializeApp(firebaseConfig);

    // Initialize the Gemini Developer API backend service
    const ai = getAI(firebaseApp, { backend: new GoogleAIBackend() });

    // Provide a JSON schema object using a standard format.
    // Later, pass this schema object into `responseSchema` in the generation config.
    const jsonSchema = Schema.object({
     properties: {
        characters: Schema.array({
          items: Schema.object({
            properties: {
              name: Schema.string(),
              accessory: Schema.string(),
              age: Schema.number(),
              species: Schema.string(),
            },
            optionalProperties: ["accessory"],
          }),
        }),
      }
    });

    // Create a `GenerativeModel` instance with a model that supports your use case
    const model = getGenerativeModel(ai, {
      model: "gemini-2.5-flash",
      // In the generation config, set the `responseMimeType` to `application/json`
      // and pass the JSON schema object into `responseSchema`.
      generationConfig: {
        responseMimeType: "application/json",
        responseSchema: jsonSchema
      },
    });


    let prompt = "For use in a children's card game, generate 10 animal-based characters.";

    let result = await model.generateContent(prompt)
    console.log(result.response.text());

### Dart


    import 'package:firebase_ai/firebase_ai.dart';
    import 'package:firebase_core/firebase_core.dart';
    import 'firebase_options.dart';

    // Provide a JSON schema object using a standard format.
    // Later, pass this schema object into `responseSchema` in the generation config.
    final jsonSchema = Schema.object(
            properties: {
              'characters': Schema.array(
                items: Schema.object(
                  properties: {
                    'name': Schema.string(),
                    'age': Schema.integer(),
                    'species': Schema.string(),
                    'accessory':
                        Schema.enumString(enumValues: ['hat', 'belt', 'shoes']),
                  },
                ),
              ),
            },
            optionalProperties: ['accessory'],
          );


    // Initialize FirebaseApp
    await Firebase.initializeApp(
      options: DefaultFirebaseOptions.currentPlatform,
    );

    // Initialize the Gemini Developer API backend service
    // Create a `GenerativeModel` instance with a model that supports your use case
    final model =
          FirebaseAI.googleAI().generativeModel(
            model: 'gemini-2.5-flash',
            // In the generation config, set the `responseMimeType` to `application/json`
            // and pass the JSON schema object into `responseSchema`.
            generationConfig: GenerationConfig(
                responseMimeType: 'application/json', responseSchema: jsonSchema));

    final prompt = "For use in a children's card game, generate 10 animal-based characters.";
    final response = await model.generateContent([Content.text(prompt)]);
    print(response.text);

### Unity


    using Firebase;
    using Firebase.AI;

    // Provide a JSON schema object using a standard format.
    // Later, pass this schema object into `responseSchema` in the generation config.
    var jsonSchema = Schema.Object(
      properties: new System.Collections.Generic.Dictionary<string, Schema> {
        { "characters", Schema.Array(
          items: Schema.Object(
            properties: new System.Collections.Generic.Dictionary<string, Schema> {
              { "name", Schema.String() },
              { "age", Schema.Int() },
              { "species", Schema.String() },
              { "accessory", Schema.Enum(new string[] { "hat", "belt", "shoes" }) },
            },
            optionalProperties: new string[] { "accessory" }
          )
        ) },
      }
    );

    // Initialize the Gemini Developer API backend service
    // Create a `GenerativeModel` instance with a model that supports your use case
    var model = FirebaseAI.DefaultInstance.GetGenerativeModel(
      modelName: "gemini-2.5-flash",
      // In the generation config, set the `responseMimeType` to `application/json`
      // and pass the JSON schema object into `responseSchema`.
      generationConfig: new GenerationConfig(
        responseMimeType: "application/json",
        responseSchema: jsonSchema
      )
    );

    var prompt = "For use in a children's card game, generate 10 animal-based characters.";

    var response = await model.GenerateContentAsync(prompt);
    UnityEngine.Debug.Log(response.Text ?? "No text in response.");

Learn how to choose a[model](https://firebase.google.com/docs/ai-logic/models)appropriate for your use case and app.

## Additional examples

Here are some additional examples of how you can use and generate structured output.

### Generate enum values as output

<br />

|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *Before trying this sample, complete the[Before you begin](https://firebase.google.com/docs/ai-logic/generate-structured-output#before-you-begin)section of this guide to set up your project and app. **In that section, you'll also click a button for your chosenGemini APIprovider so that you see provider-specific content on this page**.* |

<br />

The following example shows how to use a response schema for a classification task. The model is asked to identify the genre of a movie based on its description. The output is one plain-text enum value that the model selects from a list of values that are defined in the provided response schema.

To perform this structured classification task, you need to specify during model initialization the appropriate`responseMimeType`(in this example,`text/x.enum`) as well as the`responseSchema`that you want the model to use.  

### Swift


    import FirebaseAILogic

    // Provide an enum schema object using a standard format.
    // Later, pass this schema object into `responseSchema` in the generation config.
    let enumSchema = Schema.enumeration(values: ["drama", "comedy", "documentary"])

    // Initialize the Gemini Developer API backend service
    let ai = FirebaseAI.firebaseAI(backend: .googleAI())

    // Create a `GenerativeModel` instance with a model that supports your use case
    let model = ai.generativeModel(
      modelName: "gemini-2.5-flash",
      // In the generation config, set the `responseMimeType` to `text/x.enum`
      // and pass the enum schema object into `responseSchema`.
      generationConfig: GenerationConfig(
        responseMIMEType: "text/x.enum",
        responseSchema: enumSchema
      )
    )

    let prompt = """
    The film aims to educate and inform viewers about real-life subjects, events, or people.
    It offers a factual record of a particular topic by combining interviews, historical footage,
    and narration. The primary purpose of a film is to present information and provide insights
    into various aspects of reality.
    """

    let response = try await model.generateContent(prompt)
    print(response.text ?? "No text in response.")

### Kotlin

^*For Kotlin, the methods in this SDK are suspend functions and need to be called from a[Coroutine scope](https://developer.android.com/kotlin/coroutines).*^  


    // Provide an enum schema object using a standard format.
    // Later, pass this schema object into `responseSchema` in the generation config.
    val enumSchema = Schema.enumeration(listOf("drama", "comedy", "documentary"))

    // Initialize the Gemini Developer API backend service
    // Create a `GenerativeModel` instance with a model that supports your use case
    val model = Firebase.ai(backend = GenerativeBackend.googleAI()).generativeModel(
        modelName = "gemini-2.5-flash",
        // In the generation config, set the `responseMimeType` to `text/x.enum`
        // and pass the enum schema object into `responseSchema`.
        generationConfig = generationConfig {
            responseMimeType = "text/x.enum"
            responseSchema = enumSchema
        })

    val prompt = """
        The film aims to educate and inform viewers about real-life subjects, events, or people.
        It offers a factual record of a particular topic by combining interviews, historical footage,
        and narration. The primary purpose of a film is to present information and provide insights
        into various aspects of reality.
        """
    val response = generativeModel.generateContent(prompt)
    print(response.text)

### Java

^*For Java, the streaming methods in this SDK return a`Publisher`type from the[Reactive Streams library](https://www.reactive-streams.org/).*^  


    // Provide an enum schema object using a standard format.
    // Later, pass this schema object into `responseSchema` in the generation config.
    Schema enumSchema = Schema.enumeration(List.of("drama", "comedy", "documentary"));

    // In the generation config, set the `responseMimeType` to `text/x.enum`
    // and pass the enum schema object into `responseSchema`.
    GenerationConfig.Builder configBuilder = new GenerationConfig.Builder();
    configBuilder.responseMimeType = "text/x.enum";
    configBuilder.responseSchema = enumSchema;

    GenerationConfig generationConfig = configBuilder.build();

    // Initialize the Gemini Developer API backend service
    // Create a `GenerativeModel` instance with a model that supports your use case
    GenerativeModel ai = FirebaseAI.getInstance(GenerativeBackend.googleAI())
            .generativeModel(
                /* modelName */ "gemini-2.5-flash",
                /* generationConfig */ generationConfig);
    GenerativeModelFutures model = GenerativeModelFutures.from(ai);

    String prompt = "The film aims to educate and inform viewers about real-life subjects," +
                    " events, or people. It offers a factual record of a particular topic by" +
                    " combining interviews, historical footage, and narration. The primary purpose" +
                    " of a film is to present information and provide insights into various aspects" +
                    " of reality.";

    Content content = new Content.Builder().addText(prompt).build();

    // For illustrative purposes only. You should use an executor that fits your needs.
    Executor executor = Executors.newSingleThreadExecutor();

    ListenableFuture<GenerateContentResponse> response = model.generateContent(content);
    Futures.addCallback(
        response,
        new FutureCallback<GenerateContentResponse>() {
          @Override
          public void onSuccess(GenerateContentResponse result) {
            String resultText = result.getText();
            System.out.println(resultText);
          }

          @Override
          public void onFailure(Throwable t) {
            t.printStackTrace();
          }
        },
        executor);

### Web


    import { initializeApp } from "firebase/app";
    import { getAI, getGenerativeModel, GoogleAIBackend, Schema } from "firebase/ai";

    // TODO(developer) Replace the following with your app's Firebase configuration
    // See: https://firebase.google.com/docs/web/learn-more#config-object
    const firebaseConfig = {
      // ...
    };

    // Initialize FirebaseApp
    const firebaseApp = initializeApp(firebaseConfig);

    // Initialize the Gemini Developer API backend service
    const ai = getAI(firebaseApp, { backend: new GoogleAIBackend() });

    // Provide an enum schema object using a standard format.
    // Later, pass this schema object into `responseSchema` in the generation config.
    const enumSchema = Schema.enumString({
      enum: ["drama", "comedy", "documentary"],
    });

    // Create a `GenerativeModel` instance with a model that supports your use case
    const model = getGenerativeModel(ai, {
      model: "gemini-2.5-flash",
      // In the generation config, set the `responseMimeType` to `text/x.enum`
      // and pass the JSON schema object into `responseSchema`.
      generationConfig: {
        responseMimeType: "text/x.enum",
        responseSchema: enumSchema,
      },
    });

    let prompt = `The film aims to educate and inform viewers about real-life
    subjects, events, or people. It offers a factual record of a particular topic
    by combining interviews, historical footage, and narration. The primary purpose
    of a film is to present information and provide insights into various aspects
    of reality.`;

    let result = await model.generateContent(prompt);
    console.log(result.response.text());

### Dart


    import 'package:firebase_ai/firebase_ai.dart';
    import 'package:firebase_core/firebase_core.dart';
    import 'firebase_options.dart';

    // Provide an enum schema object using a standard format.
    // Later, pass this schema object into `responseSchema` in the generation config.
    final enumSchema = Schema.enumString(enumValues: ['drama', 'comedy', 'documentary']);

    // Initialize FirebaseApp
    await Firebase.initializeApp(
      options: DefaultFirebaseOptions.currentPlatform,
    );

    // Initialize the Gemini Developer API backend service
    // Create a `GenerativeModel` instance with a model that supports your use case
    final model =
          FirebaseAI.googleAI().generativeModel(
            model: 'gemini-2.5-flash',
            // In the generation config, set the `responseMimeType` to `text/x.enum`
            // and pass the enum schema object into `responseSchema`.
            generationConfig: GenerationConfig(
                responseMimeType: 'text/x.enum', responseSchema: enumSchema));

    final prompt = """
          The film aims to educate and inform viewers about real-life subjects, events, or people.
          It offers a factual record of a particular topic by combining interviews, historical footage, 
          and narration. The primary purpose of a film is to present information and provide insights
          into various aspects of reality.
          """;
    final response = await model.generateContent([Content.text(prompt)]);
    print(response.text);

### Unity


    using Firebase;
    using Firebase.AI;

    // Provide an enum schema object using a standard format.
    // Later, pass this schema object into `responseSchema` in the generation config.
    var enumSchema = Schema.Enum(new string[] { "drama", "comedy", "documentary" });

    // Initialize the Gemini Developer API backend service
    // Create a `GenerativeModel` instance with a model that supports your use case
    var model = FirebaseAI.DefaultInstance.GetGenerativeModel(
      modelName: "gemini-2.5-flash",
      // In the generation config, set the `responseMimeType` to `text/x.enum`
      // and pass the enum schema object into `responseSchema`.
      generationConfig: new GenerationConfig(
        responseMimeType: "text/x.enum",
        responseSchema: enumSchema
      )
    );

    var prompt = @"
    The film aims to educate and inform viewers about real-life subjects, events, or people.
    It offers a factual record of a particular topic by combining interviews, historical footage,
    and narration. The primary purpose of a film is to present information and provide insights
    into various aspects of reality.
    ";

    var response = await model.GenerateContentAsync(prompt);
    UnityEngine.Debug.Log(response.Text ?? "No text in response.");

Learn how to choose a[model](https://firebase.google.com/docs/ai-logic/models)appropriate for your use case and app.

## Other options to control content generation

- Learn more about[prompt design](https://firebase.google.com/docs/ai-logic/prompt-design)so that you can influence the model to generate output specific to your needs.
- Configure[model parameters](https://firebase.google.com/docs/ai-logic/model-parameters)to control how the model generates a response. ForGeminimodels, these parameters include max output tokens, temperature, topK, and topP. ForImagenmodels, these include aspect ratio, person generation, watermarking, etc.
- Use[safety settings](https://firebase.google.com/docs/ai-logic/safety-settings)to adjust the likelihood of getting responses that may be considered harmful, including hate speech and sexually explicit content.
- Set[system instructions](https://firebase.google.com/docs/ai-logic/system-instructions)to steer the behavior of the model. This feature is like a preamble that you add before the model gets exposed to any further instructions from the end user.

<br />

[Give feedback about your experience withFirebase AI Logic](https://firebase.google.com/docs/ai-logic/feedback)

<br />