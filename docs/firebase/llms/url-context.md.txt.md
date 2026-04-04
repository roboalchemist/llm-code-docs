# Source: https://firebase.google.com/docs/ai-logic/url-context.md.txt

<br />

The URL context tool lets you provide additional context to the model in the
form of URLs. The model can access the content from those URLs to inform and
enhance its response.

The URL context has the following benefits:

- **Extract data**: Provide specific information like prices, names, or
  key findings from an article or multiple URLs.

- **Compare information**: Analyze multiple reports, articles, or PDFs
  to identify differences and track trends.

- **Synthesize and create content**: Combine information from several
  source URLs to generate accurate summaries, blog posts, reports, or test
  questions.

- **Analyze code and technical content**: Provide URLs to a GitHub repository or
  technical documentation to explain code, generate setup instructions, or
  answer questions.

Make sure that you review the [best practices](https://firebase.google.com/docs/ai-logic/url-context#best-practices) and the
[limitations](https://firebase.google.com/docs/ai-logic/url-context#limitations) when using the URL context tool.

### Supported models

- `gemini-3.1-pro-preview`
- `gemini-3-flash-preview`
- `gemini-3.1-flash-lite-preview`
- `gemini-2.5-pro`
- `gemini-2.5-flash`
- `gemini-2.5-flash-lite`

### Supported languages

See [supported languages](https://firebase.google.com/docs/ai-logic/models#languages) for Gemini
models.

## Use the URL context tool

You can use the URL context tool in two main ways:

- [URL context tool only](https://firebase.google.com/docs/ai-logic/url-context#use-tool-only)

- Combined with [grounding with Google Search](https://firebase.google.com/docs/ai-logic/url-context#use-tool-with-google-search)

### URL context tool only

|---|
| *Click your Gemini API provider to view provider-specific content and code on this page.* <button value="dev" default="">Gemini Developer API</button> <button value="vertex">Vertex AI Gemini API</button> |

When you create the `GenerativeModel` instance, provide `UrlContext` as a tool.
Then, directly into your prompt, provide the specific URLs that you want the
model to access and analyze.

The following example shows how to compare two recipes from different websites:

### Swift


    import FirebaseAILogic

    // Initialize the Gemini Developer API backend service
    let ai = FirebaseAI.firebaseAI(backend: .googleAI())

    // Create a `GenerativeModel` instance with a model that supports your use case
    let model = ai.generativeModel(
        modelName: "GEMINI_MODEL_NAME",
        // Enable the URL context tool.
        tools: [Tool.urlContext()]
    )

    // Specify one or more URLs for the tool to access.
    let url1 = "FIRST_RECIPE_URL"
    let url2 = "SECOND_RECIPE_URL"

    // Provide the URLs in the prompt sent in the request.
    let prompt = "Compare the ingredients and cooking times from the recipes at \(url1) and \(url2)"

    // Get and handle the model's response.
    let response = try await model.generateContent(prompt)
    print(response.text ?? "No text in response.")

### Kotlin


    // Initialize the Gemini Developer API backend service
    // Create a `GenerativeModel` instance with a model that supports your use case
    val model = Firebase.ai(backend = GenerativeBackend.googleAI()).generativeModel(
        modelName = "GEMINI_MODEL_NAME",
        // Enable the URL context tool.
        tools = listOf(Tool.urlContext())
    )

    // Specify one or more URLs for the tool to access.
    val url1 = "FIRST_RECIPE_URL"
    val url2 = "SECOND_RECIPE_URL"

    // Provide the URLs in the prompt sent in the request.
    val prompt = "Compare the ingredients and cooking times from the recipes at $url1 and $url2"

    // Get and handle the model's response.
    val response = model.generateContent(prompt)
    print(response.text)

### Java


    // Initialize the Gemini Developer API backend service
    // Create a `GenerativeModel` instance with a model that supports your use case
    GenerativeModel ai = FirebaseAI.getInstance(GenerativeBackend.googleAI())
                    .generativeModel("GEMINI_MODEL_NAME",
                            null,
                            null,
                            // Enable the URL context tool.
                            List.of(Tool.urlContext(new UrlContext())));

    // Use the GenerativeModelFutures Java compatibility layer which offers
    // support for ListenableFuture and Publisher APIs
    GenerativeModelFutures model = GenerativeModelFutures.from(ai);

    // Specify one or more URLs for the tool to access.
    String url1 = "FIRST_RECIPE_URL";
    String url2 = "SECOND_RECIPE_URL";

    // Provide the URLs in the prompt sent in the request.
    String prompt = "Compare the ingredients and cooking times from the recipes at " + url1 + " and " + url2 + "";

    ListenableFuture response = model.generateContent(prompt);
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

    // Create a `GenerativeModel` instance with a model that supports your use case
    const model = getGenerativeModel(
      ai,
      {
        model: "GEMINI_MODEL_NAME",
        // Enable the URL context tool.
        tools: [{ urlContext: {} }]
      }
    );

    // Specify one or more URLs for the tool to access.
    const url1 = "FIRST_RECIPE_URL"
    const url2 = "SECOND_RECIPE_URL"

    // Provide the URLs in the prompt sent in the request.
    const prompt = `Compare the ingredients and cooking times from the recipes at ${url1} and ${url2}`

    // Get and handle the model's response.
    const result = await model.generateContent(prompt);
    console.log(result.response.text());

### Dart


    import 'package:firebase_core/firebase_core.dart';
    import 'package:firebase_ai/firebase_ai.dart';
    import 'firebase_options.dart';

    // Initialize FirebaseApp
    await Firebase.initializeApp(
      options: DefaultFirebaseOptions.currentPlatform,
    );

    // Initialize the Gemini Developer API backend service
    // Create a `GenerativeModel` instance with a model that supports your use case
    final model = FirebaseAI.googleAI().generativeModel(
      model: 'GEMINI_MODEL_NAME',
      // Enable the URL context tool.
      tools: [
        Tool.urlContext(),
      ],
    );

    // Specify one or more URLs for the tool to access.
    final url1 = "FIRST_RECIPE_URL";
    final url2 = "SECOND_RECIPE_URL";

    // Provide the URLs in the prompt sent in the request.
    final prompt = "Compare the ingredients and cooking times from the recipes at $url1 and $url2";

    // Get and handle the model's response.
    final response = await model.generateContent([Content.text(prompt)]);
    print(response.text);

### Unity


    using Firebase;
    using Firebase.AI;

    // Initialize the Gemini Developer API backend service
    var ai = FirebaseAI.GetInstance(FirebaseAI.Backend.GoogleAI());

    // Create a `GenerativeModel` instance with a model that supports your use case
    var model = ai.GetGenerativeModel(
      modelName: "GEMINI_MODEL_NAME",
      // Enable the URL context tool.
      tools: new[] { new Tool(new UrlContext()) }
    );

    // Specify one or more URLs for the tool to access.
    var url1 = "FIRST_RECIPE_URL";
    var url2 = "SECOND_RECIPE_URL";

    // Provide the URLs in the prompt sent in the request.
    var prompt = $"Compare the ingredients and cooking times from the recipes at {url1} and {url2}";

    // Get and handle the model's response.
    var response = await model.GenerateContentAsync(prompt);
    UnityEngine.Debug.Log(response.Text ?? "No text in response.");


Learn how to choose a [model](https://firebase.google.com/docs/ai-logic/models)

appropriate for your use case and app.

### URL context combined with grounding with Google Search

|---|
| *Click your Gemini API provider to view provider-specific content and code on this page.* <button value="dev" default="">Gemini Developer API</button> <button value="vertex">Vertex AI Gemini API</button> |

You can enable both URL context and
[grounding with Google Search](https://firebase.google.com/docs/ai-logic/grounding-google-search).
With this configuration, you can write prompts with or without specific URLs.

When grounding with Google Search is also enabled, the model may first use
Google Search to find relevant information and then use the URL context tool to
read the content of the search results for a more in-depth understanding of the
information. This approach is powerful for prompts that require both broad
searching and deep analysis of specific pages.

Here are some use cases:

- You provide a URL in the prompt to help with some of the generated response.
  However, to generate a proper response, the model still needs more information
  about other topics, so it uses the grounding with Google Search tool.

  Example prompt:  

  `Give me a three day event schedule based on YOUR_URL.
  Also what do I need to pack according to the weather?`
- You don't provide a URL in the prompt at all. So, to generate a proper
  response, the model uses the grounding with Google Search tool to find
  relevant URLs and then uses the URL context tool to analyze their content.

  Example prompt:  

  `Recommend 3 beginner-level books to learn about the latest
  YOUR_SUBJECT.`

The following example shows how to enable and use both tools --- URL context and
grounding with Google Search:

### Swift


    import FirebaseAILogic

    // Initialize the Gemini Developer API backend service
    let ai = FirebaseAI.firebaseAI(backend: .googleAI())

    // Create a `GenerativeModel` instance with a model that supports your use case
    let model = ai.generativeModel(
        modelName: "GEMINI_MODEL_NAME",
        // Enable both the URL context tool and Google Search tool.
        tools: [
          Tool.urlContex(),
          Tool.googleSearch()
        ]
    )

    // Specify one or more URLs for the tool to access.
    let url = "YOUR_URL"

    // Provide the URLs in the prompt sent in the request.
    // If the model can't generate a response using its own knowledge or the content in the specified URL,
    // then the model will use the grounding with Google Search tool.
    let prompt = "Give me a three day event schedule based on \(url). Also what do I need to pack according to the weather?"

    // Get and handle the model's response.
    let response = try await model.generateContent(prompt)
    print(response.text ?? "No text in response.")

    // Make sure to comply with the "Grounding with Google Search" usage requirements,
    // which includes how you https://firebase.google.com/docs/ai-logic/grounding-google-search#use-and-display-grounded-result

### Kotlin


    // Initialize the Gemini Developer API backend service
    // Create a `GenerativeModel` instance with a model that supports your use case
    val model = Firebase.ai(backend = GenerativeBackend.googleAI()).generativeModel(
        modelName = "GEMINI_MODEL_NAME",
        // Enable both the URL context tool and Google Search tool.
        tools = listOf(Tool.urlContext(), Tool.googleSearch())
    )

    // Specify one or more URLs for the tool to access.
    val url = "YOUR_URL"

    // Provide the URLs in the prompt sent in the request.
    // If the model can't generate a response using its own knowledge or the content in the specified URL,
    // then the model will use the grounding with Google Search tool.
    val prompt = "Give me a three day event schedule based on $url. Also what do I need to pack according to the weather?"

    // Get and handle the model's response.
    val response = model.generateContent(prompt)
    print(response.text)

    // Make sure to comply with the "Grounding with Google Search" usage requirements,
    // which includes how you https://firebase.google.com/docs/ai-logic/grounding-google-search#use-and-display-grounded-result

### Java


    // Initialize the Gemini Developer API backend service
    // Create a `GenerativeModel` instance with a model that supports your use case
    GenerativeModel ai = FirebaseAI.getInstance(GenerativeBackend.googleAI())
                    .generativeModel("GEMINI_MODEL_NAME",
                            null,
                            null,
                            // Enable both the URL context tool and Google Search tool.
                            List.of(Tool.urlContext(new UrlContext()), Tool.googleSearch(new GoogleSearch())));

    // Use the GenerativeModelFutures Java compatibility layer which offers
    // support for ListenableFuture and Publisher APIs
    GenerativeModelFutures model = GenerativeModelFutures.from(ai);

    // Specify one or more URLs for the tool to access.
    String url = "YOUR_URL";

    // Provide the URLs in the prompt sent in the request.
    // If the model can't generate a response using its own knowledge or the content in the specified URL,
    // then the model will use the grounding with Google Search tool.
    String prompt = "Give me a three day event schedule based on " + url + ". Also what do I need to pack according to the weather?";

    ListenableFuture response = model.generateContent(prompt);
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
    // which includes how you https://firebase.google.com/docs/ai-logic/grounding-google-search#use-and-display-grounded-result

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

    // Create a `GenerativeModel` instance with a model that supports your use case
    const model = getGenerativeModel(
      ai,
      {
        model: "GEMINI_MODEL_NAME",
        // Enable both the URL context tool and Google Search tool.
        tools: [{ urlContext: {} }, { googleSearch: {} }],
      }
    );

    // Specify one or more URLs for the tool to access.
    const url = "YOUR_URL"

    // Provide the URLs in the prompt sent in the request.
    // If the model can't generate a response using its own knowledge or the content in the specified URL,
    // then the model will use the grounding with Google Search tool.
    const prompt = `Give me a three day event schedule based on ${url}. Also what do I need to pack according to the weather?`

    // Get and handle the model's response.
    const result = await model.generateContent(prompt);
    console.log(result.response.text());

    // Make sure to comply with the "Grounding with Google Search" usage requirements,
    // which includes how you https://firebase.google.com/docs/ai-logic/grounding-google-search#use-and-display-grounded-result

### Dart


    import 'package:firebase_core/firebase_core.dart';
    import 'package:firebase_ai/firebase_ai.dart';
    import 'firebase_options.dart';

    // Initialize FirebaseApp
    await Firebase.initializeApp(
      options: DefaultFirebaseOptions.currentPlatform,
    );

    // Initialize the Gemini Developer API backend service
    // Create a `GenerativeModel` instance with a model that supports your use case
    final model = FirebaseAI.googleAI().generativeModel(
      model: 'GEMINI_MODEL_NAME',
      // Enable both the URL context tool and Google Search tool.
      tools: [
        Tool.urlContext(),
        Tool.googleSearch(),
      ],
    );

    // Specify one or more URLs for the tool to access.
    final url = "YOUR_URL";

    // Provide the URLs in the prompt sent in the request.
    // If the model can't generate a response using its own knowledge or the content in the specified URL,
    // then the model will use the grounding with Google Search tool.
    final prompt = "Give me a three day event schedule based on $url. Also what do I need to pack according to the weather?";

    final response = await model.generateContent([Content.text(prompt)]);
    print(response.text);

    // Make sure to comply with the "Grounding with Google Search" usage requirements,
    // which includes how you https://firebase.google.com/docs/ai-logic/grounding-google-search#use-and-display-grounded-result

### Unity


    using Firebase;
    using Firebase.AI;

    // Initialize the Gemini Developer API backend service
    var ai = FirebaseAI.GetInstance(FirebaseAI.Backend.GoogleAI());

    // Create a `GenerativeModel` instance with a model that supports your use case
    var model = ai.GetGenerativeModel(
      modelName: "GEMINI_MODEL_NAME",
      // Enable both the URL context tool and Google Search tool.
      tools: new[] { new Tool(new GoogleSearch()), new Tool(new UrlContext()) }
    );

    // Specify one or more URLs for the tool to access.
    var url = "YOUR_URL";

    // Provide the URLs in the prompt sent in the request.
    // If the model can't generate a response using its own knowledge or the content in the specified URL,
    // then the model will use the grounding with Google Search tool.
    var prompt = $"Give me a three day event schedule based on {url}. Also what do I need to pack according to the weather?";

    // Get and handle the model's response.
    var response = await model.GenerateContentAsync(prompt);
    UnityEngine.Debug.Log(response.Text ?? "No text in response.");

    // Make sure to comply with the "Grounding with Google Search" usage requirements,
    // which includes how you https://firebase.google.com/docs/ai-logic/grounding-google-search#use-and-display-grounded-result


Learn how to choose a [model](https://firebase.google.com/docs/ai-logic/models)

appropriate for your use case and app.

> [!IMPORTANT]
> **Important:** If you use grounding with Google Search, make sure that you comply with the "Grounding with Google Search" usage requirements, which includes how you display the result. Learn how to [use and display a grounded result](https://firebase.google.com/docs/ai-logic/grounding-google-search#use-and-display-grounded-result).

## How the URL context tool works

The URL context tool uses a two-step retrieval process to balance speed, cost,
and access to fresh data.

**Step 1**: When you provide a specific URL, the tool first attempts to fetch
the content from an internal index cache. This acts as a highly optimized cache.

**Step 2**: If a URL is not available in the index (for example, if it's a very
new page), the tool automatically falls back to do a live fetch. This directly
accesses the URL to retrieve its content in real-time.

> [!NOTE]
> **Note:** When grounding with Google Search is also enabled, any URLs passed to the URL context tool will always be a live fetch of the URL.

### Best practices

- **Provide specific URLs**: For the best results, provide direct URLs to the
  content you want the model to analyze. The model will only retrieve content
  from the URLs you provide, not any content from nested links.

- **Check for accessibility**: Verify that the URLs you provide don't lead to
  pages that require a login or are behind a paywall.

- **Use the complete URL** : Provide the full URL, including the protocol
  (for example, `https://www.example.com` instead of only `example.com`).

## Understand the response

The model's response will be based on the content it retrieved from the URLs.

If the model retrieved content from URLs, the response will include
`url_context_metadata`. Such a response might look something like the following
(parts of the response have been omitted for brevity):

    {
      "candidates": [
        {
          "content": {
            "parts": [
              {
                "text": "... \n"
              }
            ],
            "role": "model"
          },
          ...
          "url_context_metadata":
          {
              "url_metadata":
              [
                {
                  "retrieved_url": "https://www.example.com",
                  "url_retrieval_status": "URL_RETRIEVAL_STATUS_SUCCESS"
                },
                {
                  "retrieved_url": "https://www.example.org",
                  "url_retrieval_status": "URL_RETRIEVAL_STATUS_SUCCESS"
                },
              ]
            }
        }
      ]
    }

### Safety checks

The system performs a content moderation check on the URL to confirm they meet
safety standards. If the URL you provided fails this check, you'll get an
`url_retrieval_status` of `URL_RETRIEVAL_STATUS_UNSAFE`.

## Limitations

Here are some limitations of the URL context tool:

- **Combining with function calling** : The URL context tool *cannot* be used in
  a request that also uses
  [function calling](https://firebase.google.com/docs/ai-logic/function-calling).

- **URLs per request limit**: The maximum number of URLs per request is 20 URLs.

- **URL content size limit**: The maximum size for content retrieved from a
  single URL is 34MB.

- **Freshness** : The tool does *not* fetch live versions of web pages, so there
  may be some issues with freshness or potentially out-of-date information.

- **URL public accessibility** : The provided URLs must be publicly accessible on
  the web. The following are ***not*** supported: paywalled content, content
  that requires user sign-in, private networks, localhost addresses (like
  `localhost` or `127.0.0.1`), and tunneling services (like ngrok or pinggy).

### Supported and unsupported content types

Yes **Supported**: The tool can extract content
from URLs with the following content types:

- Text (`text/html`, `application/json`, `text/plain`, `text/xml`, `text/css`,
  `text/javascript`, `text/csv`, `text/rtf`)

- Image (`image/png`, `image/jpeg`, `image/bmp`, `image/webp`)

- PDF (`application/pdf`)

No **Not supported** : The tool does ***not***
support the following content types:

- YouTube videos (instead, see [analyze videos](https://firebase.google.com/docs/ai-logic/analyze-video))

- Video and audio files (instead, see
  [analyze videos](https://firebase.google.com/docs/ai-logic/analyze-video) or
  [analyze audio](https://firebase.google.com/docs/ai-logic/analyze-audio))

- Google workspace files, like Google docs or spreadsheets

- *(if using the Vertex AI Gemini API)* Cloud Storage URLs  

  These types of URLs aren't supported by the Gemini Developer API
  no matter how you access it.

- Content that's not publicly accessible. The following are ***not*** supported:
  paywalled content, content that requires user sign-in, private networks,
  localhost addresses (like `localhost` or `127.0.0.1`), and tunneling services
  (like ngrok or pinggy).

## Pricing and counting tool tokens

Content retrieved from URLs counts as input tokens.

You can see the token count for your prompt and usage of tools in the
`usage_metadata` object of the model output. The following is an example output:

    'usage_metadata': {
      'candidates_token_count': 45,
      'prompt_token_count': 27,
      'prompt_tokens_details': [{'modality': <MediaModality.TEXT: 'TEXT'>,
        'token_count': 27}],
      'thoughts_token_count': 31,
      'tool_use_prompt_token_count': 10309,
      'tool_use_prompt_tokens_details': [{'modality': <MediaModality.TEXT: 'TEXT'>,
        'token_count': 10309}],
      'total_token_count': 10412
      }

Rate limit and pricing is based on the model used. Learn more about pricing for
the URL context tool in your chosen Gemini API provider documentation:
[Gemini Developer API](https://ai.google.dev/gemini-api/docs/pricing)
\|
[Vertex AI Gemini API](https://cloud.google.com/vertex-ai/generative-ai/pricing).

> [!NOTE]
> **Note:** Tool-use tokens aren't yet displayed in the dashboards when you use [AI monitoring in the Firebase console](https://firebase.google.com/docs/ai-logic/monitoring#ai-monitoring-in-console)