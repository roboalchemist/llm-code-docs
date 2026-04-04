# Source: https://firebase.google.com/docs/ai-logic/analyze-documents.md.txt

<br />

You can ask aGeminimodel to analyze document files (like PDFs and plain-text files) that you provide either inline (base64-encoded) or via URL. When you useFirebase AI Logic, you can make this request directly from your app.

With this capability, you can do things like:

- Analyze diagrams, charts, and tables inside documents
- Extract information into structured output formats
- Answer questions about visual and text contents in documents
- Summarize documents
- Transcribe document content (for example, into HTML), preserving layouts and formatting, for use in downstream applications (such as in RAG pipelines)

[arrow_downwardJump to code samples](https://firebase.google.com/docs/ai-logic/analyze-documents#base64)[arrow_downwardJump to code for streamed responses](https://firebase.google.com/docs/ai-logic/analyze-documents#streaming)

<br />

|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **See other guides for additional options for working with documents (like PDFs)** [Generate structured output](https://firebase.google.com/docs/ai-logic/generate-structured-output)[Multi-turn chat](https://firebase.google.com/docs/ai-logic/chat) |

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

<br />

Need a sample PDF file?

<br />

> You can use this publicly available file with a MIME type of`application/pdf`([view or download file](https://storage.googleapis.com/cloud-samples-data/generative-ai/pdf/2403.05530.pdf)).`https://storage.googleapis.com/cloud-samples-data/generative-ai/pdf/2403.05530.pdf`

<br />

<br />

| **Note:** Firebase AI Logicdoes*not*yet support configuring the input media resolution, but that feature is coming soon!

## Generate text from PDF files (base64-encoded)

<br />

|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *Before trying this sample, complete the[Before you begin](https://firebase.google.com/docs/ai-logic/analyze-documents#before-you-begin)section of this guide to set up your project and app. **In that section, you'll also click a button for your chosenGemini APIprovider so that you see provider-specific content on this page**.* |

<br />

You can ask aGeminimodel to generate text by prompting with text and PDFs---providing each input file's`mimeType`and the file itself. Find[requirements and recommendations for input files](https://firebase.google.com/docs/ai-logic/analyze-documents#requirements-recommendations-for-input)later on this page.

<br />

| **Important** :**The total request size limit is 20 MB.** To send large files, review the[options for providing files in multimodal requests](https://firebase.google.com/docs/ai-logic/input-file-requirements).

<br />

### Swift

You can call[`generateContent()`](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Classes/GenerativeModel#generatecontent_:)to generate text from multimodal input of text and PDFs.  


    import FirebaseAILogic

    // Initialize the Gemini Developer API backend service
    let ai = FirebaseAI.firebaseAI(backend: .googleAI())

    // Create a `GenerativeModel` instance with a model that supports your use case
    let model = ai.generativeModel(modelName: "gemini-2.5-flash")


    // Provide the PDF as \`Data\` with the appropriate MIME type
    let pdf = try InlineDataPart(data: Data(contentsOf: pdfURL), mimeType: "application/pdf")
    // Provide a text prompt to include with the PDF file
    let prompt = "Summarize the important results in this report."
    // To generate text output, call \`generateContent\` with the PDF file and text prompt
    let response = try await model.generateContent(pdf, prompt)
    // Print the generated text, handling the case where it might be nil
    print(response.text ?? "No text in response.")

### Kotlin

You can call[`generateContent()`](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/GenerativeModel#generateContent(kotlin.Array))to generate text from multimodal input of text and PDFs.
^*For Kotlin, the methods in this SDK are suspend functions and need to be called from a[Coroutine scope](https://developer.android.com/kotlin/coroutines).*^  


    // Initialize the Gemini Developer API backend service
    // Create a `GenerativeModel` instance with a model that supports your use case
    val model = Firebase.ai(backend = GenerativeBackend.googleAI())
                            .generativeModel("gemini-2.5-flash")


    val contentResolver = applicationContext.contentResolver
    // Provide the URI for the PDF file you want to send to the model
    val inputStream = contentResolver.openInputStream(pdfUri)
    if (inputStream != null) { // Check if the PDF file loaded successfully
    inputStream.use { stream -\>
    // Provide a prompt that includes the PDF file specified above and text
    val prompt = content {
    inlineData(
    bytes = stream.readBytes(),
    mimeType = "application/pdf" // Specify the appropriate PDF file MIME type
    )
    text("Summarize the important results in this report.")
    }
    // To generate text output, call \`generateContent\` with the prompt
    val response = model.generateContent(prompt)
    // Log the generated text, handling the case where it might be null
    Log.d(TAG, response.text ?: "")
    }
    } else {
    Log.e(TAG, "Error getting input stream for file.")
    // Handle the error appropriately
    }

### Java

You can call[`generateContent()`](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/GenerativeModel#generateContent(kotlin.Array))to generate text from multimodal input of text and PDFs.
^*For Java, the methods in this SDK return a[`ListenableFuture`](https://developer.android.com/guide/background/asynchronous/listenablefuture).*^  


    // Initialize the Gemini Developer API backend service
    // Create a `GenerativeModel` instance with a model that supports your use case
    GenerativeModel ai = FirebaseAI.getInstance(GenerativeBackend.googleAI())
            .generativeModel("gemini-2.5-flash");

    // Use the GenerativeModelFutures Java compatibility layer which offers
    // support for ListenableFuture and Publisher APIs
    GenerativeModelFutures model = GenerativeModelFutures.from(ai);


    ContentResolver resolver = getApplicationContext().getContentResolver();
    // Provide the URI for the PDF file you want to send to the model
    try (InputStream stream = resolver.openInputStream(pdfUri)) {
    if (stream != null) {
    byte\[\] audioBytes = stream.readAllBytes();
    stream.close();
    // Provide a prompt that includes the PDF file specified above and text
    Content prompt = new Content.Builder()
    .addInlineData(audioBytes, "application/pdf") // Specify the appropriate PDF file MIME type
    .addText("Summarize the important results in this report.")
    .build();
    // To generate text output, call \`generateContent\` with the prompt
    ListenableFuture\<GenerateContentResponse\> response = model.generateContent(prompt);
    Futures.addCallback(response, new FutureCallback\<GenerateContentResponse\>() {
    @Override
    public void onSuccess(GenerateContentResponse result) {
    String text = result.getText();
    Log.d(TAG, (text == null) ? "" : text);
    }
    @Override
    public void onFailure(Throwable t) {
    Log.e(TAG, "Failed to generate a response", t);
    }
    }, executor);
    } else {
    Log.e(TAG, "Error getting input stream for file.");
    // Handle the error appropriately
    }
    } catch (IOException e) {
    Log.e(TAG, "Failed to read the pdf file", e);
    } catch (URISyntaxException e) {
    Log.e(TAG, "Invalid pdf file", e);
    }

### Web

You can call[`generateContent()`](https://firebase.google.com/docs/reference/js/ai.generativemodel#generativemodelgeneratecontent)to generate text from multimodal input of text and PDFs.  


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
    const model = getGenerativeModel(ai, { model: "gemini-2.5-flash" });


    // Converts a File object to a Part object.
    async function fileToGenerativePart(file) {
    const base64EncodedDataPromise = new Promise((resolve) =\> {
    const reader = new FileReader();
    reader.onloadend = () =\> resolve(reader.result.split(','));
    reader.readAsDataURL(file);
    });
    return {
    inlineData: { data: await base64EncodedDataPromise, mimeType: file.type },
    };
    }
    async function run() {
    // Provide a text prompt to include with the PDF file
    const prompt = "Summarize the important results in this report.";
    // Prepare PDF file for input
    const fileInputEl = document.querySelector("input\[type=file\]");
    const pdfPart = await fileToGenerativePart(fileInputEl.files);
    // To generate text output, call \`generateContent\` with the text and PDF file
    const result = await model.generateContent(\[prompt, pdfPart\]);
    // Log the generated text, handling the case where it might be undefined
    console.log(result.response.text() ?? "No text in response.");
    }
    run();

### Dart

You can call[`generateContent()`](https://pub.dev/documentation/firebase_ai/latest/firebase_ai/GenerativeModel/generateContent.html)to generate text from multimodal input of text and PDFs.  


    import 'package:firebase_ai/firebase_ai.dart';
    import 'package:firebase_core/firebase_core.dart';
    import 'firebase_options.dart';

    // Initialize FirebaseApp
    await Firebase.initializeApp(
      options: DefaultFirebaseOptions.currentPlatform,
    );

    // Initialize the Gemini Developer API backend service
    // Create a `GenerativeModel` instance with a model that supports your use case
    final model =
          FirebaseAI.googleAI().generativeModel(model: 'gemini-2.5-flash');


    // Provide a text prompt to include with the PDF file
    final prompt = TextPart("Summarize the important results in this report.");
    // Prepare the PDF file for input
    final doc = await File('document0.pdf').readAsBytes();
    // Provide the PDF file as \`Data\` with the appropriate PDF file MIME type
    final docPart = InlineDataPart('application/pdf', doc);
    // To generate text output, call \`generateContent\` with the text and PDF file
    final response = await model.generateContent(\[
    Content.multi(\[prompt,docPart\])
    \]);
    // Print the generated text
    print(response.text);

### Unity

You can call[`GenerateContentAsync()`](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/generative-model#generatecontentasync)to generate text from multimodal input of text and PDFs.  


    using Firebase;
    using Firebase.AI;

    // Initialize the Gemini Developer API backend service
    var ai = FirebaseAI.GetInstance(FirebaseAI.Backend.GoogleAI());

    // Create a `GenerativeModel` instance with a model that supports your use case
    var model = ai.GetGenerativeModel(modelName: "gemini-2.5-flash");


    // Provide a text prompt to include with the PDF file
    var prompt = ModelContent.Text("Summarize the important results in this report.");
    // Provide the PDF file as \`data\` with the appropriate PDF file MIME type
    var doc = ModelContent.InlineData("application/pdf",
    System.IO.File.ReadAllBytes(System.IO.Path.Combine(
    UnityEngine.Application.streamingAssetsPath, "document0.pdf")));
    // To generate text output, call \`GenerateContentAsync\` with the text and PDF file
    var response = await model.GenerateContentAsync(new \[\] { prompt, doc });
    // Print the generated text
    UnityEngine.Debug.Log(response.Text ?? "No text in response.");

Learn how to choose a[model](https://firebase.google.com/docs/ai-logic/models)appropriate for your use case and app.

## Stream the response

<br />

|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *Before trying this sample, complete the[Before you begin](https://firebase.google.com/docs/ai-logic/analyze-documents#before-you-begin)section of this guide to set up your project and app. **In that section, you'll also click a button for your chosenGemini APIprovider so that you see provider-specific content on this page**.* |

<br />

You can achieve faster interactions by not waiting for the entire result from the model generation, and instead use streaming to handle partial results. To stream the response, call`generateContentStream`.

<br />

#### View example: Stream generated text from PDF files

<br />

### Swift

You can call[`generateContentStream()`](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Classes/GenerativeModel#generatecontentstream_:)to stream generated text from multimodal input of text and PDFs.  


    import FirebaseAILogic

    // Initialize the Gemini Developer API backend service
    let ai = FirebaseAI.firebaseAI(backend: .googleAI())

    // Create a `GenerativeModel` instance with a model that supports your use case
    let model = ai.generativeModel(modelName: "gemini-2.5-flash")


    // Provide the PDF as \`Data\` with the appropriate MIME type
    let pdf = try InlineDataPart(data: Data(contentsOf: pdfURL), mimeType: "application/pdf")
    // Provide a text prompt to include with the PDF file
    let prompt = "Summarize the important results in this report."
    // To stream generated text output, call \`generateContentStream\` with the PDF file and text prompt
    let contentStream = try model.generateContentStream(pdf, prompt)
    // Print the generated text, handling the case where it might be nil
    for try await chunk in contentStream {
    if let text = chunk.text {
    print(text)
    }
    }

### Kotlin

You can call[`generateContentStream()`](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/GenerativeModel#generateContentStream(kotlin.Array))to stream generated text from multimodal input of text and PDFs.
^*For Kotlin, the methods in this SDK are suspend functions and need to be called from a[Coroutine scope](https://developer.android.com/kotlin/coroutines).*^  


    // Initialize the Gemini Developer API backend service
    // Create a `GenerativeModel` instance with a model that supports your use case
    val model = Firebase.ai(backend = GenerativeBackend.googleAI())
                            .generativeModel("gemini-2.5-flash")


    val contentResolver = applicationContext.contentResolver
    // Provide the URI for the PDF you want to send to the model
    val inputStream = contentResolver.openInputStream(pdfUri)
    if (inputStream != null) { // Check if the PDF file loaded successfully
    inputStream.use { stream -\>
    // Provide a prompt that includes the PDF file specified above and text
    val prompt = content {
    inlineData(
    bytes = stream.readBytes(),
    mimeType = "application/pdf" // Specify the appropriate PDF file MIME type
    )
    text("Summarize the important results in this report.")
    }
    // To stream generated text output, call \`generateContentStream\` with the prompt
    var fullResponse = ""
    model.generateContentStream(prompt).collect { chunk -\>
    // Log the generated text, handling the case where it might be null
    val chunkText = chunk.text ?: ""
    Log.d(TAG, chunkText)
    fullResponse += chunkText
    }
    }
    } else {
    Log.e(TAG, "Error getting input stream for file.")
    // Handle the error appropriately
    }

### Java

You can call[`generateContentStream()`](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/GenerativeModel#generateContentStream(kotlin.Array))to stream generated text from multimodal input of text and PDFs.
^*For Java, the streaming methods in this SDK return a`Publisher`type from the[Reactive Streams library](https://www.reactive-streams.org/).*^  


    // Initialize the Gemini Developer API backend service
    // Create a `GenerativeModel` instance with a model that supports your use case
    GenerativeModel ai = FirebaseAI.getInstance(GenerativeBackend.googleAI())
            .generativeModel("gemini-2.5-flash");

    // Use the GenerativeModelFutures Java compatibility layer which offers
    // support for ListenableFuture and Publisher APIs
    GenerativeModelFutures model = GenerativeModelFutures.from(ai);


    ContentResolver resolver = getApplicationContext().getContentResolver();
    // Provide the URI for the PDF file you want to send to the model
    try (InputStream stream = resolver.openInputStream(pdfUri)) {
    if (stream != null) {
    byte\[\] audioBytes = stream.readAllBytes();
    stream.close();
    // Provide a prompt that includes the PDF file specified above and text
    Content prompt = new Content.Builder()
    .addInlineData(audioBytes, "application/pdf") // Specify the appropriate PDF file MIME type
    .addText("Summarize the important results in this report.")
    .build();
    // To stream generated text output, call \`generateContentStream\` with the prompt
    Publisher\<GenerateContentResponse\> streamingResponse =
    model.generateContentStream(prompt);
    StringBuilder fullResponse = new StringBuilder();
    streamingResponse.subscribe(new Subscriber\<GenerateContentResponse\>() {
    @Override
    public void onNext(GenerateContentResponse generateContentResponse) {
    String chunk = generateContentResponse.getText();
    String text = (chunk == null) ? "" : chunk;
    Log.d(TAG, text);
    fullResponse.append(text);
    }
    @Override
    public void onComplete() {
    Log.d(TAG, fullResponse.toString());
    }
    @Override
    public void onError(Throwable t) {
    Log.e(TAG, "Failed to generate a response", t);
    }
    @Override
    public void onSubscribe(Subscription s) {
    }
    });
    } else {
    Log.e(TAG, "Error getting input stream for file.");
    // Handle the error appropriately
    }
    } catch (IOException e) {
    Log.e(TAG, "Failed to read the pdf file", e);
    } catch (URISyntaxException e) {
    Log.e(TAG, "Invalid pdf file", e);
    }

### Web

You can call[`generateContentStream()`](https://firebase.google.com/docs/reference/js/ai.generativemodel#generativemodelgeneratecontentstream)to stream generated text from multimodal input of text and PDFs.  


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
    const model = getGenerativeModel(ai, { model: "gemini-2.5-flash" });


    // Converts a File object to a Part object.
    async function fileToGenerativePart(file) {
    const base64EncodedDataPromise = new Promise((resolve) =\> {
    const reader = new FileReader();
    reader.onloadend = () =\> resolve(reader.result.split(','));
    reader.readAsDataURL(file);
    });
    return {
    inlineData: { data: await base64EncodedDataPromise, mimeType: file.type },
    };
    }
    async function run() {
    // Provide a text prompt to include with the PDF file
    const prompt = "Summarize the important results in this report.";
    // Prepare PDF file for input
    const fileInputEl = document.querySelector("input\[type=file\]");
    const pdfPart = await fileToGenerativePart(fileInputEl.files);
    // To stream generated text output, call \`generateContentStream\` with the text and PDF file
    const result = await model.generateContentStream(\[prompt, pdfPart\]);
    // Log the generated text
    for await (const chunk of result.stream) {
    const chunkText = chunk.text();
    console.log(chunkText);
    }
    }
    run();

### Dart

You can call[`generateContentStream()`](https://pub.dev/documentation/firebase_ai/latest/firebase_ai/GenerativeModel/generateContentStream.html)to stream generated text from multimodal input of text and PDFs.  


    import 'package:firebase_ai/firebase_ai.dart';
    import 'package:firebase_core/firebase_core.dart';
    import 'firebase_options.dart';

    // Initialize FirebaseApp
    await Firebase.initializeApp(
      options: DefaultFirebaseOptions.currentPlatform,
    );

    // Initialize the Gemini Developer API backend service
    // Create a `GenerativeModel` instance with a model that supports your use case
    final model =
          FirebaseAI.googleAI().generativeModel(model: 'gemini-2.5-flash');


    // Provide a text prompt to include with the PDF file
    final prompt = TextPart("Summarize the important results in this report.");
    // Prepare the PDF file for input
    final doc = await File('document0.pdf').readAsBytes();
    // Provide the PDF file as \`Data\` with the appropriate PDF file MIME type
    final docPart = InlineDataPart('application/pdf', doc);
    // To generate text output, call \`generateContentStream\` with the text and PDF file
    final response = await model.generateContentStream(\[
    Content.multi(\[prompt,docPart\])
    \]);
    // Print the generated text
    await for (final chunk in response) {
    print(chunk.text);
    }

### Unity

You can call[`GenerateContentStreamAsync()`](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/generative-model#generatecontentstreamasync)to stream generated text from multimodal input of text and PDFs.  


    using Firebase;
    using Firebase.AI;

    // Initialize the Gemini Developer API backend service
    var ai = FirebaseAI.GetInstance(FirebaseAI.Backend.GoogleAI());

    // Create a `GenerativeModel` instance with a model that supports your use case
    var model = ai.GetGenerativeModel(modelName: "gemini-2.5-flash");


    // Provide a text prompt to include with the PDF file
    var prompt = ModelContent.Text("Summarize the important results in this report.");
    // Provide the PDF file as \`data\` with the appropriate PDF file MIME type
    var doc = ModelContent.InlineData("application/pdf",
    System.IO.File.ReadAllBytes(System.IO.Path.Combine(
    UnityEngine.Application.streamingAssetsPath, "document0.pdf")));
    // To stream generated text output, call \`GenerateContentStreamAsync\` with the text and PDF file
    var responseStream = model.GenerateContentStreamAsync(new \[\] { prompt, doc });
    // Print the generated text
    await foreach (var response in responseStream) {
    if (!string.IsNullOrWhiteSpace(response.Text)) {
    UnityEngine.Debug.Log(response.Text);
    }
    }

Learn how to choose a[model](https://firebase.google.com/docs/ai-logic/models)appropriate for your use case and app.

<br />

<br />

<br />

*** ** * ** ***

## Requirements and recommendations for input documents

<br />

| **Important** :**The total request size limit is 20 MB.** To send large files, review the[options for providing files in multimodal requests](https://firebase.google.com/docs/ai-logic/input-file-requirements).

<br />

Note that a file provided as inline data is encoded to base64 in transit, which increases the size of the request. You get an HTTP 413 error if a request is too large.

See "Supported input files and requirements" page to learn detailed information about the following:

- [Different options for providing a file in a request](https://firebase.google.com/docs/ai-logic/input-file-requirements#options-for-input-files)(either inline or using the file's URL or URI)
- [Requirements and best practices for document files](https://firebase.google.com/docs/ai-logic/input-file-requirements#documents)

#### Supported document MIME types

Geminimultimodal models support the following document MIME types:

- PDF -`application/pdf`
- Text -`text/plain`

<br />

#### Limits per request

<br />

PDFs are treated as images, so a single page of a PDF is treated as one image. The number of pages allowed in a prompt is limited to the number of images theGeminimultimodal models can support.

- Maximum files per request: 3,000 files
- Maximum pages per file: 1,000 pages per file
- Maximum size per file: 50 MB per file

<br />

<br />

*** ** * ** ***

## What else can you do?

- Learn how to[count tokens](https://firebase.google.com/docs/ai-logic/count-tokens)before sending long prompts to the model.
- [Set upCloud Storage for Firebase](https://firebase.google.com/docs/ai-logic/solutions/cloud-storage)so that you can include large files in your multimodal requests and have a more managed solution for providing files in prompts. Files can include images, PDFs, video, and audio.
- Start thinking about preparing for production (see the[production checklist](https://firebase.google.com/docs/ai-logic/production-checklist)), including:
  - [Setting upFirebase App Check](https://firebase.google.com/docs/ai-logic/app-check)to protect theGemini APIfrom abuse by unauthorized clients.
  - [IntegratingFirebase Remote Config](https://firebase.google.com/docs/ai-logic/solutions/remote-config)to update values in your app (like model name) without releasing a new app version.

<br />

#### Try out other capabilities

<br />

- Build[multi-turn conversations (chat)](https://firebase.google.com/docs/ai-logic/chat).
- Generate text from[text-only prompts](https://firebase.google.com/docs/ai-logic/generate-text).
- Generate[structured output (like JSON)](https://firebase.google.com/docs/ai-logic/generate-structured-output)from both text and multimodal prompts.
- Generate images from text prompts ([Gemini](https://firebase.google.com/docs/ai-logic/generate-images-gemini)or[Imagen](https://firebase.google.com/docs/ai-logic/generate-images-imagen)).
- Use tools (like[function calling](https://firebase.google.com/docs/ai-logic/function-calling)and[grounding with Google Search](https://firebase.google.com/docs/ai-logic/grounding-google-search)) to connect aGeminimodel to other parts of your app and external systems and information.

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