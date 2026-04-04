# Source: https://firebase.google.com/docs/ai-logic/function-calling.md.txt

<br />

Generative models are powerful at solving many types of problems. However, they are constrained by limitations like:

- They are frozen after training, leading to stale knowledge.
- They can't query or modify external data.

Function calling can help you overcome some of these limitations. Function calling is sometimes referred to as*tool use*because it allows a model to use external tools such as APIs and functions to generate its final response.

<br />

This guide shows you how you might implement a function call setup similar to the scenario described in the next major section of this page. At a high-level, here are the steps to set up function calling in your app:

- **Step 1**: Write a function that can provide the model with information that it needs to generate its final response (for example, the function can call an external API).

- **Step 2**: Create a function declaration that describes the function and its parameters.

- **Step 3**: Provide the function declaration during model initialization so that the model knows how it can use the function, if needed.

- **Step 4**: Set up your app so that the model can send along the required information for your app to call the function.

- **Step 5**: Pass the function's response back to the model so that the model can generate its final response.

[Jump to code implementation](https://firebase.google.com/docs/ai-logic/function-calling#implement-function-calling)

## Overview of a function calling example

When you send a request to the model, you can also provide the model with a set of "tools" (like functions) that it can use to generate its final response. In order to utilize these functions and call them ("function calling"), the model and your app need to pass information back-and-forth to each other, so the recommended way to use function calling is through the multi-turn chat interface.

Imagine that you have an app where a user could enter a prompt like:`What was the weather in Boston on October 17, 2024?`.

TheGeminimodels may not know this weather information; however, imagine that you know of an external weather service API that can provide it. You can use function calling to give theGeminimodel a pathway to that API and its weather information.

First, you write a function`fetchWeather`in your app that interacts with this hypothetical external API, which has this input and output:

|     **Parameter**     | **Type** | **Required** |                                                                      **Description**                                                                      |
|-----------------------|----------|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Input                                                                                                                                                                                                    ||||
| `location`            | Object   | Yes          | The name of the city and its state for which to get the weather. Only cities in the USA are supported. Must always be a nested object of`city`and`state`. |
| `date`                | String   | Yes          | Date for which to fetch the weather (must always be in`YYYY-MM-DD`format).                                                                                |
| Output                                                                                                                                                                                                   ||||
| `temperature`         | Integer  | Yes          | Temperature (in Fahrenheit)                                                                                                                               |
| `chancePrecipitation` | String   | Yes          | Chance of precipitation (expressed as a percentage)                                                                                                       |
| `cloudConditions`     | String   | Yes          | Cloud conditions (one of`clear`,`partlyCloudy`,`mostlyCloudy`,`cloudy`)                                                                                   |

When initializing the model, you tell the model that this`fetchWeather`function exists and how it can be used to process incoming requests, if needed. This is called a "function declaration".*The model does not call the function**directly**.* Instead, as the model is processing the incoming request, it decides if the`fetchWeather`function can help it respond to the request. If the model decides that the function can indeed be useful, the model generates structured data that will help*your app call the function*.

Look again at the incoming request:`What was the weather in Boston on October 17, 2024?`. The model would likely decide that the`fetchWeather`function can help it generate a response. The model would look at what input parameters are needed for`fetchWeather`and then generate structured input data for the function that looks roughly like this:  

    {
      functionName: fetchWeather,
      location: {
        city: Boston,
        state: Massachusetts  // the model can infer the state from the prompt
      },
      date: 2024-10-17
    }

The model passes this structured input data to your app so that your app can call the`fetchWeather`function. When your app receives the weather conditions back from the API, it passes the information along to the model. This weather information allows the model to complete its final processing and generate its response to the initial request of`What was the weather in Boston on October 17, 2024?`

The model might provide a final natural-language response like:`On October 17, 2024, in Boston, it was 38 degrees Fahrenheit with partly cloudy skies.`

![Diagram showing how function calling involves the model interacting with a function in your app](https://firebase.google.com/static/docs/ai-logic/images/function-calling.png)  
You can[learn more about function calling](https://ai.google.dev/gemini-api/docs/function-calling)in theGemini Developer APIdocumentation.

## Implement function calling

The following steps in this guide show you how to implement a function call setup similar to the workflow described in[Overview of a function calling example](https://firebase.google.com/docs/ai-logic/function-calling#overview-of-example)(see the top section of this page).

### Before you begin

<br />

|----------------------------------------------------------------------------------------------------------------------------------|
| *Click yourGemini APIprovider to view provider-specific content and code on this page.* Gemini Developer APIVertex AI Gemini API |

<br />

If you haven't already, complete the[getting started guide](https://firebase.google.com/docs/ai-logic/get-started), which describes how to set up your Firebase project, connect your app to Firebase, add the SDK, initialize the backend service for your chosenGemini APIprovider, and create a`GenerativeModel`instance.

<br />

| All our docs assume that you're using the[](https://firebase.google.com/support/releases)latest versionsof theFirebase AI LogicSDKs.

<br />

For testing and iterating on your prompts, we recommend using[Google AI Studio](https://aistudio.google.com).

<br />

### **Step 1**: Write the function

Imagine that you have an app where a user could enter a prompt like:`What was the weather in Boston on October 17, 2024?`. TheGeminimodels may not know this weather information; however, imagine that you know of an external weather service API that can provide it. The scenario in this guide relies on this hypothetical external API.

Write the function in your app that will interact with the hypothetical external API and provide the model with the information it needs to generate its final request. In this weather example, it will be a`fetchWeather`function that makes the call to this hypothetical external API.
**Note:** The functions you provide to the model aren't required to call an external API. They could also do things like provide formulas for calculating a value, query a database, return search results across documents, etc.  

### Swift

    // This function calls a hypothetical external API that returns
    // a collection of weather information for a given location on a given date.
    func fetchWeather(city: String, state: String, date: String) -> JSONObject {

      // TODO(developer): Write a standard function that would call an external weather API.

      // For demo purposes, this hypothetical response is hardcoded here in the expected format.
      return [
        "temperature": .number(38),
        "chancePrecipitation": .string("56%"),
        "cloudConditions": .string("partlyCloudy"),
      ]
    }

### Kotlin

    // This function calls a hypothetical external API that returns
    // a collection of weather information for a given location on a given date.
    // `location` is an object of the form { city: string, state: string }
    data class Location(val city: String, val state: String)

    suspend fun fetchWeather(location: Location, date: String): JsonObject {

        // TODO(developer): Write a standard function that would call to an external weather API.

        // For demo purposes, this hypothetical response is hardcoded here in the expected format.
        return JsonObject(mapOf(
            "temperature" to JsonPrimitive(38),
            "chancePrecipitation" to JsonPrimitive("56%"),
            "cloudConditions" to JsonPrimitive("partlyCloudy")
        ))
    }

### Java

    // This function calls a hypothetical external API that returns
    // a collection of weather information for a given location on a given date.
    // `location` is an object of the form { city: string, state: string }
    public JsonObject fetchWeather(Location location, String date) {

      // TODO(developer): Write a standard function that would call to an external weather API.

      // For demo purposes, this hypothetical response is hardcoded here in the expected format.
      return new JsonObject(Map.of(
            "temperature", JsonPrimitive(38),
            "chancePrecipitation", JsonPrimitive("56%"),
            "cloudConditions", JsonPrimitive("partlyCloudy")));
    }

### Web

    // This function calls a hypothetical external API that returns
    // a collection of weather information for a given location on a given date.
    // `location` is an object of the form { city: string, state: string }
    async function fetchWeather({ location, date }) {

      // TODO(developer): Write a standard function that would call to an external weather API.

      // For demo purposes, this hypothetical response is hardcoded here in the expected format.
      return {
        temperature: 38,
        chancePrecipitation: "56%",
        cloudConditions: "partlyCloudy",
      };
    }

### Dart

    // This function calls a hypothetical external API that returns
    // a collection of weather information for a given location on a given date.
    // `location` is an object of the form { city: string, state: string }
    Future<Map<String, Object?>> fetchWeather(
      Location location, String date
    ) async {

      // TODO(developer): Write a standard function that would call to an external weather API.

      // For demo purposes, this hypothetical response is hardcoded here in the expected format.
      final apiResponse = {
        'temperature': 38,
        'chancePrecipitation': '56%',
        'cloudConditions': 'partlyCloudy',
      };
      return apiResponse;
    }

### Unity

    // This function calls a hypothetical external API that returns
    // a collection of weather information for a given location on a given date.
    System.Collections.Generic.Dictionary<string, object> FetchWeather(
        string city, string state, string date) {

      // TODO(developer): Write a standard function that would call an external weather API.

      // For demo purposes, this hypothetical response is hardcoded here in the expected format.
      return new System.Collections.Generic.Dictionary<string, object>() {
        {"temperature", 38},
        {"chancePrecipitation", "56%"},
        {"cloudConditions", "partlyCloudy"},
      };
    }

### **Step 2**: Create a function declaration

Create the function declaration that you'll later provide to the model (next step of this guide).
| **Note:** This guide's example demonstrates providing only one function declaration to the model, but you can provide**up to 128 function declarations**to the model for it to choose among.

In your declaration, include as much detail as possible in the descriptions for the function and its parameters.

The model uses the information in the function declaration to determine which function to select and how to provide parameter values for the actual call to the function. See[Additional behaviors and options](https://firebase.google.com/docs/ai-logic/function-calling#additional-behaviors-and-options)later on this page for how the model may choose among the functions, as well as how you can control that choice.

Note the following about the schema that you provide:

- You must provide function declarations in a schema format that's compatible with the[OpenAPI schema](https://spec.openapis.org/oas/v3.0.3#schema).Vertex AIoffers limited support of the OpenAPI schema.

  - The following attributes are supported:`type`,`nullable`,`required`,`format`,`description`,`properties`,`items`,`enum`.

  - The following attributes are*not* supported:`default`,`optional`,`maximum`,`oneOf`.

- By default, forFirebase AI LogicSDKs, all fields are considered*required* unless you specify them as optional in an`optionalProperties`array. For these optional fields, the model can populate the fields or skip them. Note that this is opposite from the default behavior of the twoGemini APIproviders if you use their server SDKs or their API directly.

For best practices related to the function declarations, including tips for names and descriptions, see[Best practices](https://ai.google.dev/gemini-api/docs/function-calling#best_practices)in theGemini Developer APIdocumentation.

Here's how you can write a function declaration:  

### Swift

    let fetchWeatherTool = FunctionDeclaration(
      name: "fetchWeather",
      description: "Get the weather conditions for a specific city on a specific date.",
      parameters: [
        "location": .object(
          properties: [
            "city": .string(description: "The city of the location."),
            "state": .string(description: "The US state of the location."),
          ],
          description: """
          The name of the city and its state for which to get the weather. Only cities in the
          USA are supported.
          """
        ),
        "date": .string(
          description: """
          The date for which to get the weather. Date must be in the format: YYYY-MM-DD.
          """
        ),
      ]
    )

### Kotlin

    val fetchWeatherTool = FunctionDeclaration(
        "fetchWeather",
        "Get the weather conditions for a specific city on a specific date.",
        mapOf(
            "location" to Schema.obj(
                mapOf(
                    "city" to Schema.string("The city of the location."),
                    "state" to Schema.string("The US state of the location."),
                ),
                description = "The name of the city and its state for which " +
                    "to get the weather. Only cities in the " +
                    "USA are supported."
            ),
            "date" to Schema.string("The date for which to get the weather." +
                                    " Date must be in the format: YYYY-MM-DD."
            ),
        ),
    )

### Java

    FunctionDeclaration fetchWeatherTool = new FunctionDeclaration(
            "fetchWeather",
            "Get the weather conditions for a specific city on a specific date.",
            Map.of("location",
                    Schema.obj(Map.of(
                            "city", Schema.str("The city of the location."),
                            "state", Schema.str("The US state of the location."))),
                    "date",
                    Schema.str("The date for which to get the weather. " +
                                  "Date must be in the format: YYYY-MM-DD.")),
            Collections.emptyList());

### Web

    const fetchWeatherTool: FunctionDeclarationsTool = {
      functionDeclarations: [
       {
          name: "fetchWeather",
          description:
            "Get the weather conditions for a specific city on a specific date",
          parameters: Schema.object({
            properties: {
              location: Schema.object({
                description:
                  "The name of the city and its state for which to get " +
                  "the weather. Only cities in the USA are supported.",
                properties: {
                  city: Schema.string({
                    description: "The city of the location."
                  }),
                  state: Schema.string({
                    description: "The US state of the location."
                  }),
                },
              }),
              date: Schema.string({
                description:
                  "The date for which to get the weather. Date must be in the" +
                  " format: YYYY-MM-DD.",
              }),
            },
          }),
        },
      ],
    };

### Dart

    final fetchWeatherTool = FunctionDeclaration(
        'fetchWeather',
        'Get the weather conditions for a specific city on a specific date.',
        parameters: {
          'location': Schema.object(
            description:
              'The name of the city and its state for which to get'
              'the weather. Only cities in the USA are supported.',
            properties: {
              'city': Schema.string(
                 description: 'The city of the location.'
               ),
              'state': Schema.string(
                 description: 'The US state of the location.'
              ),
            },
          ),
          'date': Schema.string(
            description:
              'The date for which to get the weather. Date must be in the format: YYYY-MM-DD.'
          ),
        },
      );

### Unity

    var fetchWeatherTool = new Tool(new FunctionDeclaration(
      name: "fetchWeather",
      description: "Get the weather conditions for a specific city on a specific date.",
      parameters: new System.Collections.Generic.Dictionary<string, Schema>() {
        { "location", Schema.Object(
          properties: new System.Collections.Generic.Dictionary<string, Schema>() {
            { "city", Schema.String(description: "The city of the location.") },
            { "state", Schema.String(description: "The US state of the location.")}
          },
          description: "The name of the city and its state for which to get the weather. Only cities in the USA are supported."
        ) },
        { "date", Schema.String(
          description: "The date for which to get the weather. Date must be in the format: YYYY-MM-DD."
        )}
      }
    ));

### **Step 3**: Provide the function declaration during model initialization

The maximum number of function declarations that you can provide with the request is 128. See[Additional behaviors and options](https://firebase.google.com/docs/ai-logic/function-calling#additional-behaviors-and-options)later on this page for how the model may choose among the functions, as well as how you can control that choice (using a`toolConfig`to set the*function calling mode*).  

### Swift


    import FirebaseAILogic

    // Initialize the Gemini Developer API backend service
    // Create a `GenerativeModel` instance with a model that supports your use case
    let model = FirebaseAI.firebaseAI(backend: .googleAI()).generativeModel(
      modelName: "gemini-2.5-flash",
      // Provide the function declaration to the model.
      tools: [.functionDeclarations([fetchWeatherTool])]
    )

### Kotlin


    // Initialize the Gemini Developer API backend service
    // Create a `GenerativeModel` instance with a model that supports your use case
    val model = Firebase.ai(backend = GenerativeBackend.googleAI()).generativeModel(
        modelName = "gemini-2.5-flash",
        // Provide the function declaration to the model.
        tools = listOf(Tool.functionDeclarations(listOf(fetchWeatherTool)))
    )

### Java


    // Initialize the Gemini Developer API backend service
    // Create a `GenerativeModel` instance with a model that supports your use case
    GenerativeModelFutures model = GenerativeModelFutures.from(
            FirebaseAI.getInstance(GenerativeBackend.googleAI())
                    .generativeModel("gemini-2.5-flash",
                            null,
                            null,
                            // Provide the function declaration to the model.
                            List.of(Tool.functionDeclarations(List.of(fetchWeatherTool)))));

### Web


    import { initializeApp } from "firebase/app";
    import { getAI, getGenerativeModel, GoogleAIBackend } from "firebase/ai";

    // TODO(developer) Replace the following with your app's Firebase configuration
    // See: https://firebase.google.com/docs/web/learn-more#config-object
    const firebaseConfig = {
      // ...
    };

    // Initialize FirebaseApp
    const firebaseApp = initializeApp(firebaseConfig);

    // Initialize the Gemini Developer API backend service
    const firebaseAI = getAI(firebaseApp, { backend: new GoogleAIBackend() });

    // Create a \`GenerativeModel\` instance with a model that supports your use case
    const model = getGenerativeModel(firebaseAI, {
    model: "gemini-2.5-flash",
    // Provide the function declaration to the model.
    tools: fetchWeatherTool
    });

### Dart


    import 'package:firebase_ai/firebase_ai.dart';
    import 'package:firebase_core/firebase_core.dart';
    import 'firebase_options.dart';

    // Initialize FirebaseApp
    await Firebase.initializeApp(
      options: DefaultFirebaseOptions.currentPlatform,
    );

    // Initialize the Gemini Developer API backend service
    // Create a `GenerativeModel` instance with a model that supports your use case
    _functionCallModel = FirebaseAI.googleAI().generativeModel(
           model: 'gemini-2.5-flash',
           // Provide the function declaration to the model.
           tools: [
             Tool.functionDeclarations([fetchWeatherTool]),
           ],
         );

### Unity


    using Firebase;
    using Firebase.AI;

    // Initialize the Gemini Developer API backend service
    // Create a `GenerativeModel` instance with a model that supports your use case
    var model = FirebaseAI.DefaultInstance.GetGenerativeModel(
      modelName: "gemini-2.5-flash",
      // Provide the function declaration to the model.
      tools: new Tool[] { fetchWeatherTool }
    );

Learn how to choose a[model](https://firebase.google.com/docs/ai-logic/models)appropriate for your use case and app.

### **Step 4**: Call the function to invoke the external API

If the model decides that the`fetchWeather`function can indeed help it generate a final response, your app needs to make the actual call to that function using the structured input data provided by the model.

Since information needs to be passed back-and-forth between the model and the app, the recommended way to use function calling is through the multi-turn chat interface.

The following code snippet shows how your app is told that the model wants to use the`fetchWeather`function. It also shows that the model has provided the necessary input parameter values for the function call (and its underlying external API).

In this example, the incoming request contained the prompt`What was the weather in Boston on October 17, 2024?`. From this prompt, the model inferred the input parameters that are required by the`fetchWeather`function (that is,`city`,`state`, and`date`).  

### Swift

    let chat = model.startChat()
    let prompt = "What was the weather in Boston on October 17, 2024?"

    // Send the user's question (the prompt) to the model using multi-turn chat.
    let response = try await chat.sendMessage(prompt)

    var functionResponses = [FunctionResponsePart]()

    // When the model responds with one or more function calls, invoke the function(s).
    for functionCall in response.functionCalls {
      if functionCall.name == "fetchWeather" {
        // TODO(developer): Handle invalid arguments.
        guard case let .object(location) = functionCall.args["location"] else { fatalError() }
        guard case let .string(city) = location["city"] else { fatalError() }
        guard case let .string(state) = location["state"] else { fatalError() }
        guard case let .string(date) = functionCall.args["date"] else { fatalError() }

        functionResponses.append(FunctionResponsePart(
          name: functionCall.name,
          // Forward the structured input data prepared by the model
          // to the hypothetical external API.
          response: fetchWeather(city: city, state: state, date: date)
        ))
      }
      // TODO(developer): Handle other potential function calls, if any.
    }

### Kotlin

    val prompt = "What was the weather in Boston on October 17, 2024?"
    val chat = model.startChat()
    // Send the user's question (the prompt) to the model using multi-turn chat.
    val result = chat.sendMessage(prompt)

    val functionCalls = result.functionCalls
    // When the model responds with one or more function calls, invoke the function(s).
    val fetchWeatherCall = functionCalls.find { it.name == "fetchWeather" }

    // Forward the structured input data prepared by the model
    // to the hypothetical external API.
    val functionResponse = fetchWeatherCall?.let {
        // Alternatively, if your `Location` class is marked as @Serializable, you can use
        // val location = Json.decodeFromJsonElement<Location>(it.args["location"]!!)
        val location = Location(
            it.args["location"]!!.jsonObject["city"]!!.jsonPrimitive.content,
            it.args["location"]!!.jsonObject["state"]!!.jsonPrimitive.content
        )
        val date = it.args["date"]!!.jsonPrimitive.content
        fetchWeather(location, date)
    }

### Java

    String prompt = "What was the weather in Boston on October 17, 2024?";
    ChatFutures chatFutures = model.startChat();
    // Send the user's question (the prompt) to the model using multi-turn chat.
    ListenableFuture<GenerateContentResponse> response =
            chatFutures.sendMessage(new Content("user", List.of(new TextPart(prompt))));

    ListenableFuture<JsonObject> handleFunctionCallFuture = Futures.transform(response, result -> {
        for (FunctionCallPart functionCall : result.getFunctionCalls()) {
            if (functionCall.getName().equals("fetchWeather")) {
                Map<String, JsonElement> args = functionCall.getArgs();
                JsonObject locationJsonObject =
                        JsonElementKt.getJsonObject(args.get("location"));
                String city =
                        JsonElementKt.getContentOrNull(
                                JsonElementKt.getJsonPrimitive(
                                        locationJsonObject.get("city")));
                String state =
                        JsonElementKt.getContentOrNull(
                                JsonElementKt.getJsonPrimitive(
                                        locationJsonObject.get("state")));
                Location location = new Location(city, state);

                String date = JsonElementKt.getContentOrNull(
                        JsonElementKt.getJsonPrimitive(
                                args.get("date")));
                return fetchWeather(location, date);
            }
        }
        return null;
    }, Executors.newSingleThreadExecutor());

### Web

    const chat = model.startChat();
    const prompt = "What was the weather in Boston on October 17, 2024?";

    // Send the user's question (the prompt) to the model using multi-turn chat.
    let result = await chat.sendMessage(prompt);
    const functionCalls = result.response.functionCalls();
    let functionCall;
    let functionResult;
    // When the model responds with one or more function calls, invoke the function(s).
    if (functionCalls.length > 0) {
      for (const call of functionCalls) {
        if (call.name === "fetchWeather") {
          // Forward the structured input data prepared by the model
          // to the hypothetical external API.
          functionResult = await fetchWeather(call.args);
          functionCall = call;
        }
      }
    }

### Dart

    final chat = _functionCallModel.startChat();
    const prompt = 'What was the weather in Boston on October 17, 2024?';

    // Send the user's question (the prompt) to the model using multi-turn chat.
    var response = await chat.sendMessage(Content.text(prompt));

    final functionCalls = response.functionCalls.toList();
    // When the model responds with one or more function calls, invoke the function(s).
    if (functionCalls.isNotEmpty) {
      for (final functionCall in functionCalls) {
        if (functionCall.name == 'fetchWeather') {
          Map<String, dynamic> location =
              functionCall.args['location']! as Map<String, dynamic>;
          var date = functionCall.args['date']! as String;
          var city = location['city'] as String;
          var state = location['state'] as String;
          final functionResult =
              await fetchWeather(Location(city, state), date);
          // Send the response to the model so that it can use the result to
          // generate text for the user.
          response = await functionCallChat.sendMessage(
            Content.functionResponse(functionCall.name, functionResult),
          );
        }
      }
    } else {
      throw UnimplementedError(
        'Function not declared to the model: ${functionCall.name}',
      );
    }

### Unity

    var chat = model.StartChat();
    var prompt = "What was the weather in Boston on October 17, 2024?";

    // Send the user's question (the prompt) to the model using multi-turn chat.
    var response = await chat.SendMessageAsync(prompt);

    var functionResponses = new List<ModelContent>();

    foreach (var functionCall in response.FunctionCalls) {
      if (functionCall.Name == "fetchWeather") {
        // TODO(developer): Handle invalid arguments.
        var city = functionCall.Args["city"] as string;
        var state = functionCall.Args["state"] as string;
        var date = functionCall.Args["date"] as string;

        functionResponses.Add(ModelContent.FunctionResponse(
          name: functionCall.Name,
          // Forward the structured input data prepared by the model
          // to the hypothetical external API.
          response: FetchWeather(city: city, state: state, date: date)
        ));
      }
      // TODO(developer): Handle other potential function calls, if any.
    }

### **Step 5**: Provide the function's output to the model to generate the final response

After the`fetchWeather`function returns the weather information, your app needs to pass it back to the model.

Then, the model performs its final processing, and generates a final natural-language response like:`On October 17, 2024 in Boston, it was 38 degrees Fahrenheit with partly cloudy skies.`  

### Swift

    // Send the response(s) from the function back to the model
    // so that the model can use it to generate its final response.
    let finalResponse = try await chat.sendMessage(
      [ModelContent(role: "function", parts: functionResponses)]
    )

    // Log the text response.
    print(finalResponse.text ?? "No text in response.")

### Kotlin

    // Send the response(s) from the function back to the model
    // so that the model can use it to generate its final response.
    val finalResponse = chat.sendMessage(content("function") {
        part(FunctionResponsePart("fetchWeather", functionResponse!!))
    })

    // Log the text response.
    println(finalResponse.text ?: "No text in response")

### Java

    ListenableFuture<GenerateContentResponse> modelResponseFuture = Futures.transformAsync(
      handleFunctionCallFuture,
      // Send the response(s) from the function back to the model
      // so that the model can use it to generate its final response.
      functionCallResult -> chatFutures.sendMessage(new Content("function",
      List.of(new FunctionResponsePart(
              "fetchWeather", functionCallResult)))),
      Executors.newSingleThreadExecutor());

    Futures.addCallback(modelResponseFuture, new FutureCallback<GenerateContentResponse>() {
    @Override
    public void onSuccess(GenerateContentResponse result) {
      if (result.getText() != null) {
          // Log the text response.
          System.out.println(result.getText());
      }
    }

    @Override
    public void onFailure(Throwable t) {
      // handle error
    }
    }, Executors.newSingleThreadExecutor());

### Web

    // Send the response from the function back to the model
    // so that the model can use it to generate its final response.
    result = await chat.sendMessage([
      {
        functionResponse: {
          name: functionCall.name, // "fetchWeather"
          response: functionResult,
        },
      },
    ]);
    console.log(result.response.text());

### Dart

    // Send the response from the function back to the model
    // so that the model can use it to generate its final response.
    response = await chat
         .sendMessage(Content.functionResponse(functionCall.name, functionResult));

### Unity

    // Send the response(s) from the function back to the model
    // so that the model can use it to generate its final response.
    var finalResponse = await chat.SendMessageAsync(functionResponses);

    // Log the text response.
    UnityEngine.Debug.Log(finalResponse.Text ?? "No text in response.");

## Additional behaviors and options

Here are some additional behaviors for function calling that you need to accommodate in your code and options that you can control.

### The model may ask to call a function again or another function.

If the response from one function call is insufficient for the model to generate its final response, then the model may ask for an additional function call, or ask for a call to an entirely different function. The latter can only happen if you provide more than one function to the model in your function declaration list.

Your app needs to accommodate that the model may ask for additional function calls.

### The model may ask to call multiple functions at the same time.

You can provide up to 128 functions in your function declaration list to the model. Given this, the model may decide that multiple functions are needed to help it generate its final response. And it might decide to call some of these functions at the same time -- this is called***parallel function calling***.

Your app needs to accommodate that the model may ask for multiple functions running at the same time, and your app needs to provide all the responses from the functions back to the model.

### You can control how and if the model can ask to call functions.

You can place some constraints on how and if the model should use the provided function declarations. This is called setting the***function calling mode***. Here are some examples:

- Instead of allowing the model to choose between an immediate natural language response and a function call, you can force it to always use function calls. This is called***forced function calling***.

- If you provide multiple function declarations, you can restrict the model to using only a subset of the functions provided.

You implement these constraints (or modes) by adding a tool configuration (`toolConfig`) along with the prompt and the function declarations. In the tool configuration, you can specify one of the following*modes* . The most useful mode is`ANY`.

| **Mode** |                                                                             **Description**                                                                              |
|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `AUTO`   | The default model behavior. The model decides whether to use a function call or a natural language response.                                                             |
| `ANY`    | The model must use function calls ("forced function calling"). To limit the model to a subset of functions, specify the allowed function names in`allowedFunctionNames`. |
| `NONE`   | The model must not use function calls. This behavior is equivalent to a model request without any associated function declarations.                                      |

<br />

*** ** * ** ***

## What else can you do?

<br />

#### Try out other capabilities

<br />

- Build[multi-turn conversations (chat)](https://firebase.google.com/docs/ai-logic/chat).
- Generate text from[text-only prompts](https://firebase.google.com/docs/ai-logic/generate-text).
- Generate text by prompting with various file types, like[images](https://firebase.google.com/docs/ai-logic/analyze-images),[PDFs](https://firebase.google.com/docs/ai-logic/analyze-documents),[video](https://firebase.google.com/docs/ai-logic/analyze-video), and[audio](https://firebase.google.com/docs/ai-logic/analyze-audio).

<br />

#### Learn how to control content generation

- [Understand prompt design](https://firebase.google.com/docs/ai-logic/prompt-design), including best practices, strategies, and example prompts.
- [Configure model parameters](https://firebase.google.com/docs/ai-logic/model-parameters)like temperature and maximum output tokens (forGemini) or aspect ratio and person generation (forImagen).
- [Use safety settings](https://firebase.google.com/docs/ai-logic/safety-settings)to adjust the likelihood of getting responses that may be considered harmful.

You can also experiment with prompts and model configurations and even get a generated code snippet using[Google AI Studio](https://aistudio.google.com).

<br />

<br />

#### Learn more about the supported models

Learn about the[models available for various use cases](https://firebase.google.com/docs/ai-logic/models)and their[quotas](https://firebase.google.com/docs/ai-logic/quotas)and[pricing](https://firebase.google.com/docs/ai-logic/pricing).

<br />

<br />

[Give feedback about your experience withFirebase AI Logic](https://firebase.google.com/docs/ai-logic/feedback)

<br />