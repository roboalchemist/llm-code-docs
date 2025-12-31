# Source: https://firebase.google.com/docs/ai-logic/grounding-google-search.md.txt

<br />

Grounding with Google Search connects aGeminimodel to real-time, publicly-available web content. This allows the model to provide more accurate, up-to-date answers and cite verifiable sources beyond its knowledge cutoff.

Grounding with Google Search has the following benefits:

- **Increase factual accuracy**: Reduce model hallucinations by basing responses on real-world information.
- **Access real-time information**: Answer questions about recent events and topics.
- **Provide sources**: Build user trust or allow users to browse relevant sites by showing the sources for the model's claims.
- **Complete more complex tasks**: Retrieve artifacts and relevant images, videos, or other media to assist in reasoning tasks.
- **Improve region or language-specific responses**: Find region-specific information, or assist in translating content accurately.

| **Note for web publishers:** Grounding with Google Search does not use web pages for grounding that have disallowed Google-Extended. Web publishers can[manage inclusion in Google-Extended with a`robots.txt`file](https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers#google-extended).

### Supported models

- `gemini-3-pro-preview`
- `gemini-3-flash-preview`
- `gemini-3-pro-image-preview`(aka "nano banana pro")
- `gemini-2.5-pro`
- `gemini-2.5-flash`
- `gemini-2.5-flash-lite`
- `gemini-2.0-flash-001`(and its auto-updated alias`gemini-2.0-flash`)

### Supported languages

See[supported languages](https://firebase.google.com/docs/ai-logic/models#languages)forGeminimodels.

## Ground the model with Google Search

|----------------------------------------------------------------------------------------------------------------------------------|
| *Click yourGemini APIprovider to view provider-specific content and code on this page.* Gemini Developer APIVertex AI Gemini API |

| **Important:** If a response contains "Google Search suggestions" (the`searchEntryPoint`field within the`groundingMetadata`object), then that response is a "grounded result" so**you're required to comply with the "Grounding with Google Search" usage requirements, which includes how you display the result** . Learn how to[use and display a grounded result](https://firebase.google.com/docs/ai-logic/grounding-google-search#use-and-display-grounded-result)later on this page.

When you create the`GenerativeModel`instance, provide`GoogleSearch`as a`tool`that the model can use to generate its response.  

### Swift


    import FirebaseAILogic

    // Initialize the Gemini Developer API backend service
    let ai = FirebaseAI.firebaseAI(backend: .googleAI())

    // Create a \`GenerativeModel\` instance with a model that supports your use case
    let model = ai.generativeModel(
    modelName: "<var translate="no">GEMINI_MODEL_NAME</var>",
    // Provide Google Search as a tool that the model can use to generate its response
    tools: \[Tool.googleSearch()\]
    )

    let response = try await model.generateContent("Who won the euro 2024?")
    print(response.text ?? "No text in response.")

    // Make sure to comply with the "Grounding with Google Search" usage requirements,
    // which includes how you [use and display the grounded result](https://firebase.google.com/docs/ai-logic/grounding-google-search#use-and-display-grounded-result)

### Kotlin


    // Initialize the Gemini Developer API backend service
    // Create a \`GenerativeModel\` instance with a model that supports your use case
    val model = Firebase.ai(backend = GenerativeBackend.googleAI()).generativeModel(
    modelName = "<var translate="no">GEMINI_MODEL_NAME</var>",
    // Provide Google Search as a tool that the model can use to generate its response
    tools = listOf(Tool.googleSearch())
    )

    val response = model.generateContent("Who won the euro 2024?")
    print(response.text)

    // Make sure to comply with the "Grounding with Google Search" usage requirements,
    // which includes how you [use and display the grounded result](https://firebase.google.com/docs/ai-logic/grounding-google-search#use-and-display-grounded-result)

### Java


    // Initialize the Gemini Developer API backend service
    // Create a \`GenerativeModel\` instance with a model that supports your use case
    GenerativeModel ai = FirebaseAI.getInstance(GenerativeBackend.googleAI())
    .generativeModel("<var translate="no">GEMINI_MODEL_NAME</var>",
    null,
    null,
    // Provide Google Search as a tool that the model can use to generate its response
    List.of(Tool.GoogleSearch()));

    // Use the GenerativeModelFutures Java compatibility layer which offers
    // support for ListenableFuture and Publisher APIs
    GenerativeModelFutures model = GenerativeModelFutures.from(ai);

    ListenableFuture response = model.generateContent("Who won the euro 2024?");
      Futures.addCallback(response, new FutureCallback() {
          @Override
          public void onSuccess(GenerateContentResponse result) {
              String resultText = result.getText();
              System.out.println(resultText);
          }

          @Override
          public void onFailure(Throwable t) {
              t.printStackTrace();
          }
      }, executor);

    // Make sure to comply with the "Grounding with Google Search" usage requirements,
    // which includes how you [use and display the grounded result](https://firebase.google.com/docs/ai-logic/grounding-google-search#use-and-display-grounded-result)

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
    const ai = getAI(firebaseApp, { backend: new GoogleAIBackend() });

    // Create a \`GenerativeModel\` instance with a model that supports your use case
    const model = getGenerativeModel(
    ai,
    {
    model: "<var translate="no">GEMINI_MODEL_NAME</var>",
    // Provide Google Search as a tool that the model can use to generate its response
    tools: \[{ googleSearch: {} }\]
    }
    );

    const result = await model.generateContent("Who won the euro 2024?");

    console.log(result.response.text());

    // Make sure to comply with the "Grounding with Google Search" usage requirements,
    // which includes how you [use and display the grounded result](https://firebase.google.com/docs/ai-logic/grounding-google-search#use-and-display-grounded-result)

### Dart


    import 'package:firebase_core/firebase_core.dart';
    import 'package:firebase_ai/firebase_ai.dart';
    import 'firebase_options.dart';

    // Initialize FirebaseApp
    await Firebase.initializeApp(
      options: DefaultFirebaseOptions.currentPlatform,
    );

    // Initialize the Gemini Developer API backend service
    // Create a \`GenerativeModel\` instance with a model that supports your use case
    final model = FirebaseAI.googleAI().generativeModel(
    model: '<var translate="no">GEMINI_MODEL_NAME</var>',
    // Provide Google Search as a tool that the model can use to generate its response
    tools: \[
    Tool.googleSearch(),
    \],
    );

    final response = await model.generateContent([Content.text("Who won the euro 2024?")]);
    print(response.text);

    // Make sure to comply with the "Grounding with Google Search" usage requirements,
    // which includes how you [use and display the grounded result](https://firebase.google.com/docs/ai-logic/grounding-google-search#use-and-display-grounded-result)

### Unity


    using Firebase;
    using Firebase.AI;

    // Initialize the Gemini Developer API backend service
    var ai = FirebaseAI.GetInstance(FirebaseAI.Backend.GoogleAI());

    // Create a \`GenerativeModel\` instance with a model that supports your use case
    var model = ai.GetGenerativeModel(
    modelName: "<var translate="no">GEMINI_MODEL_NAME</var>",
    // Provide Google Search as a tool that the model can use to generate its response
    tools: new\[\] { new Tool(new GoogleSearch()) }
    );

    var response = await model.GenerateContentAsync("Who won the euro 2024?");
    UnityEngine.Debug.Log(response.Text ?? "No text in response.");

    // Make sure to comply with the "Grounding with Google Search" usage requirements,
    // which includes how you [use and display the grounded result](https://firebase.google.com/docs/ai-logic/grounding-google-search#use-and-display-grounded-result)

Learn how to choose a[model](https://firebase.google.com/docs/ai-logic/models)appropriate for your use case and app.

For ideal results, use a temperature of`1.0`(which is the default for all 2.5 models). Learn how to set temperature in the[model's configuration](https://firebase.google.com/docs/ai-logic/model-parameters#gemini).

## How grounding with Google Search works

When you use the`GoogleSearch`tool, the model handles the entire workflow of searching, processing, and citing information automatically.

Here's the workflow of the model:

1. **Receive prompt** : Your app sends a prompt to theGeminimodel with the`GoogleSearch`tool enabled.
2. **Analyze prompt**: The model analyzes the prompt and determines if Google Search can improve its response.
3. **Send queries to Google Search**: If needed, the model automatically generates one or multiple search queries and executes them.
4. **Process the Search results**: The model processes the Google Search results and formulates a response to the original prompt.
5. **Return a "grounded result"** : The model returns a final, user-friendly response that is grounded in the Google Search results. This response includes the model's text answer and`groundingMetadata`with the search queries, web results, and sources.

Note that providing Google Search as a tool to the model doesn't require the model to always use the Google Search tool to generate its response. In these cases, the response won't contain a`groundingMetadata`object and thus it's*not*a "grounded result".

![Diagram showing how grounding with Google Search involves the model interacting with Google Search](https://firebase.google.com/static/docs/ai-logic/images/grounding-google-search-workflow.png)

## Understand the grounded result

If the model grounds its response in Google Search results, then the response includes a`groundingMetadata`object that contains structured data that's essential for verifying claims and building a rich source experience in your application.
| **Important:** If a response contains "Google Search suggestions" (the`searchEntryPoint`field within the`groundingMetadata`object), then that response is a "grounded result" so**you're required to comply with the "Grounding with Google Search" usage requirements, which includes how you display the result** . Learn how to[use and display a grounded result](https://firebase.google.com/docs/ai-logic/grounding-google-search#use-and-display-grounded-result)later on this page.

The`groundingMetadata`object in a "grounded result" contains the following information:

- `webSearchQueries`: An array of the search queries sent to Google Search. This information is useful for debugging and understanding the model's reasoning process.

- `searchEntryPoint`: Contains the HTML and CSS to render the required "Google Search suggestions". You're required to comply with the "Grounding with Google Search" usage requirements for your chosen API provider:[Gemini Developer API](https://ai.google.dev/gemini-api/terms#grounding-with-google-search)orVertex AIGemini API(see[Service Terms](https://cloud.google.com/terms/service-terms)section within the Service Specific Terms). Learn how to[use and display a grounded result](https://firebase.google.com/docs/ai-logic/grounding-google-search#use-and-display-grounded-result)later on this page.

- `groundingChunks`: An array of objects containing the web sources (`uri`and`title`).

- `groundingSupports`: An array of chunks to connect model response`text`to the sources in`groundingChunks`. Each chunk links a text`segment`(defined by`startIndex`and`endIndex`) to one or more`groundingChunkIndices`. This field helps you build inline source links. Learn how to[use and display a grounded result](https://firebase.google.com/docs/ai-logic/grounding-google-search#use-and-display-grounded-result)later on this page.

Here's an example response that includes a`groundingMetadata`object:  

    {
      "candidates": [
        {
          "content": {
            "parts": [
              {
                "text": "Spain won Euro 2024, defeating England 2-1 in the final. This victory marks Spain's record fourth European Championship title."
              }
            ],
            "role": "model"
          },
          "groundingMetadata": {
            "webSearchQueries": [
              "UEFA Euro 2024 winner",
              "who won euro 2024"
            ],
            "searchEntryPoint": {
              "renderedContent": "<!-- HTML and CSS for the search widget -->"
            },
            "groundingChunks": [
              {"web": {"uri": "https://vertexaisearch.cloud.google.com.....", "title": "aljazeera.com"}},
              {"web": {"uri": "https://vertexaisearch.cloud.google.com.....", "title": "uefa.com"}}
            ],
            "groundingSupports": [
              {
                "segment": {"startIndex": 0, "endIndex": 85, "text": "Spain won Euro 2024, defeatin..."},
                "groundingChunkIndices": [0]
              },
              {
                "segment": {"startIndex": 86, "endIndex": 210, "text": "This victory marks Spain's..."},
                "groundingChunkIndices": [0, 1]
              }
            ]
          }
        }
      ]
    }

## Use and display a grounded result

If the model uses the Google Search tool to generate a response, it will provide a[`groundingMetadata`object](https://firebase.google.com/docs/ai-logic/grounding-google-search#understand-grounded-result)in the response.

**It's*required* to[display Google Search suggestions](https://firebase.google.com/docs/ai-logic/grounding-google-search#display-search-suggestions)and*required* to[display sources](https://firebase.google.com/docs/ai-logic/grounding-google-search#display-sources).**

Beyond complying with the requirements of using the Google Search tool, displaying this information helps you and your end users to validate responses and adds avenues for further learning.
| **Important:** This section describes basic guidance and a*general* pattern for how to use and display a grounded result.**Make sure that you review and comply with the*usage and display requirements* for your chosenGemini APIprovider** :[Gemini Developer API](https://ai.google.dev/gemini-api/terms#grounding-with-google-search)orVertex AIGemini API(see[Service Terms](https://cloud.google.com/terms/service-terms)section within the Service Specific Terms).

### *(Required)*Display Google Search suggestions

**If a response contains "Google Search suggestions", then you're required to comply with the "Grounding with Google Search" usage requirements, which includes how you display Google Search suggestions.**

The`groundingMetadata`object contains "Google Search suggestions", specifically the`searchEntryPoint`field, which has a`renderedContent`field that provides compliant HTML and CSS styling, which you need to implement to display Search suggestions in your app.

Review the detailed information about the[display and behavior requirements for Google Search suggestions](https://cloud.google.com/vertex-ai/generative-ai/docs/grounding/grounding-with-google-search#requirements)in theGoogle Clouddocumentation. Note that even though this detailed guidance is in theVertex AIGemini APIdocumentation, the guidance is applicable to theGemini Developer APIprovider, as well.

See[example code samples](https://firebase.google.com/docs/ai-logic/grounding-google-search#handle-grounded-result-code-samples)later in this section.
| **Note:** The HTML and CSS provided in the response automatically adapts to the device settings, displaying in either light or dark mode based on the preference indicated by`@media(prefers-color-scheme)`.

### *(Required)*Display sources

The`groundingMetadata`object contains structured source data, specifically the`groundingSupports`and`groundingChunks`fields. Use this information to link the model's statements directly to their sources within your UI (inline and in aggregate).

See[example code samples](https://firebase.google.com/docs/ai-logic/grounding-google-search#handle-grounded-result-code-samples)later in this section.

### Example code samples

These code samples provide*generalized*patterns for using and displaying the grounded result. However, it's your responsibility to make sure that your specific implementation aligns with the compliance requirements.  

### Swift

    // ...

    // Get the model's response
    let text = response.text

    // Get the grounding metadata
    if let candidate = response.candidates.first,
       let groundingMetadata = candidate.groundingMetadata {
      // REQUIRED - display Google Search suggestions
      // (renderedContent contains HTML and CSS for the search widget)
      if let renderedContent = groundingMetadata.searchEntryPoint?.renderedContent {
        // TODO(developer): Display Google Search suggestions using a WebView
      }

      // REQUIRED - display sources
      let groundingChunks = groundingMetadata.groundingChunks
      for chunk in groundingMetadata.groundingChunks {
        if let web = chunk.web {
          let title = web.title  // for example, "uefa.com"
          let uri = web.uri  // for example, "https://vertexaisearch.cloud.google.com..."
          // TODO(developer): show source in the UI
        }
      }
    }

### Kotlin

    // ...

    // Get the model's response
    val text = response.text

    // Get the grounding metadata
    val groundingMetadata = response.candidates.firstOrNull()?.groundingMetadata

    // REQUIRED - display Google Search suggestions
    // (renderedContent contains HTML and CSS for the search widget)
    val renderedContent = groundingMetadata?.searchEntryPoint?.renderedContent
    if (renderedContent != null) {
        // TODO(developer): Display Google Search suggestions using a WebView
    }

    // REQUIRED - display sources
    val groundingChunks = groundingMetadata?.groundingChunks
    groundingChunks?.let { chunks ->
      for (chunk in chunks) {
      	val title = chunk.web?.title  // for example, "uefa.com"
    	val uri = chunk.web?.uri  // for example, "https://vertexaisearch.cloud.google.com..."
    // TODO(developer): show source in the UI
      }
    }

### Java

    // ...

    Futures.addCallback(response, new FutureCallback() {
      @Override
      public void onSuccess(GenerateContentResponse result) {
      // Get the model's response
      String text = result.getText();

      // Get the grounding metadata
      GroundingMetadata groundingMetadata =
      result.getCandidates()[0].getGroundingMetadata();

      if (groundingMetadata != null) {
        // REQUIRED - display Google Search suggestions
      // (renderedContent contains HTML and CSS for the search widget)
        String renderedContent =
      groundingMetadata.getSearchEntryPoint().getRenderedContent();
        if (renderedContent != null) {
          // TODO(developer): Display Google Search suggestions using a WebView
        }

        // REQUIRED - display sources
        List chunks = groundingMetadata.getGroundingChunks();
        if (chunks != null) {
          for(GroundingChunk chunk : chunks) {
            WebGroundingChunk web = chunk.getWeb();
            if (web != null) {
              String title = web.getTitle();  // for example, "uefa.com"
              String uri = web.getUri();  // for example, "https://vertexaisearch.cloud.google.com..."
              // TODO(developer): show sources in the UI
            }
          }
        }
      }
      }

      @Override
      public void onFailure(Throwable t) {
      t.printStackTrace();
      }
      }, executor);

### Web

    // ...

    // Get the model's text response
    const text = result.response.text();

    // Get the grounding metadata
    const groundingMetadata = result.response.candidates?.[0]?.groundingMetadata;

    // REQUIRED - display Google Search suggestions
    // (renderedContent contains HTML and CSS for the search widget)
    const renderedContent = groundingMetadata?.searchEntryPoint?.renderedContent;
    if (renderedContent) {
      // TODO(developer): render this HTML and CSS in the UI
    }

    // REQUIRED - display sources
    const groundingChunks = groundingMetadata?.groundingChunks;
    if (groundingChunks) {
      for (const chunk of groundingChunks) {
        const title = chunk.web?.title;  // for example, "uefa.com"
        const uri = chunk.web?.uri;  // for example, "https://vertexaisearch.cloud.google.com..."
        // TODO(developer): show sources in the UI
      }
    }

### Dart

    // ...

    // Get the model's response
    final text = response.text;

    // Get the grounding metadata
    final groundingMetadata = response.candidates.first.groundingMetadata;

    // REQUIRED - display Google Search suggestions
    // (renderedContent contains HTML and CSS for the search widget)
    final renderedContent = groundingMetadata?.searchEntryPoint?.renderedContent;
    if (renderedContent != null) {
        // TODO(developer): Display Google Search suggestions using a WebView
    }

    // REQUIRED - display sources
    final groundingChunks = groundingMetadata?.groundingChunks;
    if (groundingChunks != null) {
      for (var chunk in groundingChunks) {
        final title = chunk.web?.title;  // for example, "uefa.com"
        final uri = chunk.web?.uri;  // for example, "https://vertexaisearch.cloud.google.com..."
        // TODO(developer): show sources in the UI
      }
    }

### Unity

    // ...

    // Get the model's response
    var text = response.Text;

    // Get the grounding metadata
    var groundingMetadata = response.Candidates.First().GroundingMetadata.Value;

    // REQUIRED - display Google Search suggestions
    // (renderedContent contains HTML and CSS for the search widget)
    if (groundingMetadata.SearchEntryPoint.HasValue) {
        var renderedContent = groundingMetadata.SearchEntryPoint.Value.RenderedContent;
        // TODO(developer): Display Google Search suggestions using a WebView
    }

    // REQUIRED - display sources
    foreach(GroundingChunk chunk in groundingMetadata.GroundingChunks) {
        var title = chunk.Web.Value.Title;  // for example, "uefa.com"
        var uri = chunk.Web.Value.Uri;  // for example, "https://vertexaisearch.cloud.google.com..."
        // TODO(developer): show sources in the UI
    }

### Grounded results and AI monitoring in theFirebaseconsole

If you've enabled[AI monitoring in theFirebaseconsole](https://firebase.google.com/docs/ai-logic/monitoring#ai-monitoring-in-console), responses are stored inCloud Logging. By default, this data has a 30-day retention period.

It's your responsibility to ensure that this retention period, or any custom period you set, fully aligns with your specific use case and any additional compliance requirements for your chosenGemini APIprovider:[Gemini Developer API](https://ai.google.dev/gemini-api/terms#grounding-with-google-search)orVertex AIGemini API(see[Service Terms](https://cloud.google.com/terms/service-terms)section within the Service Specific Terms). You may need to[adjust the retention period inCloud Logging](https://cloud.google.com/logging/docs/buckets)to meet these requirements.

## Pricing and limits

Make sure to review pricing, model availability, and limits for grounding with Google Search in your chosenGemini APIprovider documentation:[Gemini Developer API](https://ai.google.dev/gemini-api/docs/pricing)\|[Vertex AIGemini API](https://cloud.google.com/vertex-ai/generative-ai/pricing).