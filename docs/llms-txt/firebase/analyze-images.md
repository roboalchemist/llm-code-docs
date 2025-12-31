# Source: https://firebase.google.com/docs/ai-logic/analyze-images.md.txt

<br />

You can ask aGeminimodel to analyze image files that you provide either inline (base64-encoded) or via URL. When you useFirebase AI Logic, you can make this request directly from your app.

With this capability, you can do things like:

- Create captions or answer questions about images
- Write a short story or a poem about an image
- Detect objects in an image and return bounding box coordinates for them
- Label or categorize a set of images for sentiment, style, or other characteristic

[arrow_downwardJump to code samples](https://firebase.google.com/docs/ai-logic/analyze-images#base64)[arrow_downwardJump to code for streamed responses](https://firebase.google.com/docs/ai-logic/analyze-images#streaming)

<br />

|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **See other guides for additional options for working with images** [Generate structured output](https://firebase.google.com/docs/ai-logic/generate-structured-output)[Multi-turn chat](https://firebase.google.com/docs/ai-logic/chat)[Analyze images on-device](https://firebase.google.com/docs/ai-logic/hybrid-and-on-device-inference)[Generate images](https://firebase.google.com/docs/ai-logic/generate-images-gemini) |

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

Need a sample image file?

<br />

> You can use this publicly available file with a MIME type of`image/jpeg`([view or download file](https://storage.googleapis.com/cloud-samples-data/generative-ai/image/scones.jpg)).`https://storage.googleapis.com/cloud-samples-data/generative-ai/image/scones.jpg`

<br />

<br />

| **Note:** Firebase AI Logicdoes*not*yet support configuring the input media resolution, but that feature is coming soon!

## Generate text from image files (base64-encoded)

<br />

|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *Before trying this sample, complete the[Before you begin](https://firebase.google.com/docs/ai-logic/analyze-images#before-you-begin)section of this guide to set up your project and app. **In that section, you'll also click a button for your chosenGemini APIprovider so that you see provider-specific content on this page**.* |

<br />

You can ask aGeminimodel to generate text by prompting with text and images---providing each input file's`mimeType`and the file itself. Find[requirements and recommendations for input files](https://firebase.google.com/docs/ai-logic/analyze-images#requirements-recommendations-for-input)later on this page.

<br />

| **Important** :**The total request size limit is 20 MB.** To send large files, review the[options for providing files in multimodal requests](https://firebase.google.com/docs/ai-logic/input-file-requirements).

<br />

### Swift

You can call[`generateContent()`](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Classes/GenerativeModel#generatecontent_:)to generate text from multimodal input of text and images.  

### Single file input


    import FirebaseAILogic

    // Initialize the Gemini Developer API backend service
    let ai = FirebaseAI.firebaseAI(backend: .googleAI())

    // Create a `GenerativeModel` instance with a model that supports your use case
    let model = ai.generativeModel(modelName: "gemini-2.5-flash")


    guard let image = UIImage(systemName: "bicycle") else { fatalError() }
    // Provide a text prompt to include with the image
    let prompt = "What's in this picture?"
    // To generate text output, call generateContent and pass in the prompt
    let response = try await model.generateContent(image, prompt)
    print(response.text ?? "No text in response.")

### Multiple file input


    import FirebaseAILogic

    // Initialize the Gemini Developer API backend service
    let ai = FirebaseAI.firebaseAI(backend: .googleAI())

    // Create a `GenerativeModel` instance with a model that supports your use case
    let model = ai.generativeModel(modelName: "gemini-2.5-flash")


    guard let image1 = UIImage(systemName: "car") else { fatalError() }
    guard let image2 = UIImage(systemName: "car.2") else { fatalError() }
    // Provide a text prompt to include with the images
    let prompt = "What's different between these pictures?"
    // To generate text output, call generateContent and pass in the prompt
    let response = try await model.generateContent(image1, image2, prompt)
    print(response.text ?? "No text in response.")

| **Note** : The example above takes advantage of a simplified way to handle platform-native image types provided as inline data, which means the MIME type doesn't need to be specified.[Learn more](https://firebase.google.com/docs/ai-logic/faq-and-troubleshooting#inline-img-sdk-handling)about this feature and options for providing images inline.

### Kotlin

You can call[`generateContent()`](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/GenerativeModel#generateContent(kotlin.Array))to generate text from multimodal input of text and images.
^*For Kotlin, the methods in this SDK are suspend functions and need to be called from a[Coroutine scope](https://developer.android.com/kotlin/coroutines).*^  

### Single file input


    // Initialize the Gemini Developer API backend service
    // Create a `GenerativeModel` instance with a model that supports your use case
    val model = Firebase.ai(backend = GenerativeBackend.googleAI())
                            .generativeModel("gemini-2.5-flash")


    // Loads an image from the app/res/drawable/ directory
    val bitmap: Bitmap = BitmapFactory.decodeResource(resources, R.drawable.sparky)
    // Provide a prompt that includes the image specified above and text
    val prompt = content {
    image(bitmap)
    text("What developer tool is this mascot from?")
    }
    // To generate text output, call generateContent with the prompt
    val response = model.generateContent(prompt)
    print(response.text)

### Multiple file input

^*For Kotlin, the methods in this SDK are suspend functions and need to be called from a[Coroutine scope](https://developer.android.com/kotlin/coroutines).*^  


    // Initialize the Gemini Developer API backend service
    // Create a `GenerativeModel` instance with a model that supports your use case
    val model = Firebase.ai(backend = GenerativeBackend.googleAI())
                            .generativeModel("gemini-2.5-flash")


    // Loads an image from the app/res/drawable/ directory
    val bitmap1: Bitmap = BitmapFactory.decodeResource(resources, R.drawable.sparky)
    val bitmap2: Bitmap = BitmapFactory.decodeResource(resources, R.drawable.sparky_eats_pizza)
    // Provide a prompt that includes the images specified above and text
    val prompt = content {
    image(bitmap1)
    image(bitmap2)
    text("What is different between these pictures?")
    }
    // To generate text output, call generateContent with the prompt
    val response = model.generateContent(prompt)
    print(response.text)

| **Note** : The example above takes advantage of a simplified way to handle platform-native image types provided as inline data, which means the MIME type doesn't need to be specified.[Learn more](https://firebase.google.com/docs/ai-logic/faq-and-troubleshooting#inline-img-sdk-handling)about this feature and options for providing images inline.

### Java

You can call[`generateContent()`](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/GenerativeModel#generateContent(kotlin.Array))to generate text from multimodal input of text and images.
^*For Java, the methods in this SDK return a[`ListenableFuture`](https://developer.android.com/guide/background/asynchronous/listenablefuture).*^  

### Single file input


    // Initialize the Gemini Developer API backend service
    // Create a `GenerativeModel` instance with a model that supports your use case
    GenerativeModel ai = FirebaseAI.getInstance(GenerativeBackend.googleAI())
            .generativeModel("gemini-2.5-flash");

    // Use the GenerativeModelFutures Java compatibility layer which offers
    // support for ListenableFuture and Publisher APIs
    GenerativeModelFutures model = GenerativeModelFutures.from(ai);


    Bitmap bitmap = BitmapFactory.decodeResource(getResources(), R.drawable.sparky);
    // Provide a prompt that includes the image specified above and text
    Content content = new Content.Builder()
    .addImage(bitmap)
    .addText("What developer tool is this mascot from?")
    .build();
    // To generate text output, call generateContent with the prompt
    ListenableFuture\<GenerateContentResponse\> response = model.generateContent(content);
    Futures.addCallback(response, new FutureCallback\<GenerateContentResponse\>() {
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

### Multiple file input


    // Initialize the Gemini Developer API backend service
    // Create a `GenerativeModel` instance with a model that supports your use case
    GenerativeModel ai = FirebaseAI.getInstance(GenerativeBackend.googleAI())
            .generativeModel("gemini-2.5-flash");

    // Use the GenerativeModelFutures Java compatibility layer which offers
    // support for ListenableFuture and Publisher APIs
    GenerativeModelFutures model = GenerativeModelFutures.from(ai);


    Bitmap bitmap1 = BitmapFactory.decodeResource(getResources(), R.drawable.sparky);
    Bitmap bitmap2 = BitmapFactory.decodeResource(getResources(), R.drawable.sparky_eats_pizza);
    // Provide a prompt that includes the images specified above and text
    Content prompt = new Content.Builder()
    .addImage(bitmap1)
    .addImage(bitmap2)
    .addText("What's different between these pictures?")
    .build();
    // To generate text output, call generateContent with the prompt
    ListenableFuture\<GenerateContentResponse\> response = model.generateContent(prompt);
    Futures.addCallback(response, new FutureCallback\<GenerateContentResponse\>() {
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

| **Note** : The example above takes advantage of a simplified way to handle platform-native image types provided as inline data, which means the MIME type doesn't need to be specified.[Learn more](https://firebase.google.com/docs/ai-logic/faq-and-troubleshooting#inline-img-sdk-handling)about this feature and options for providing images inline.

### Web

You can call[`generateContent()`](https://firebase.google.com/docs/reference/js/ai.generativemodel#generativemodelgeneratecontent)to generate text from multimodal input of text and images.  

### Single file input


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
    reader.onloadend = () =\> resolve(reader.result.split(',')\[1\]);
    reader.readAsDataURL(file);
    });
    return {
    inlineData: { data: await base64EncodedDataPromise, mimeType: file.type },
    };
    }
    async function run() {
    // Provide a text prompt to include with the image
    const prompt = "What do you see?";
    const fileInputEl = document.querySelector("input\[type=file\]");
    const imagePart = await fileToGenerativePart(fileInputEl.files\[0\]);
    // To generate text output, call generateContent with the text and image
    const result = await model.generateContent(\[prompt, imagePart\]);
    const response = result.response;
    const text = response.text();
    console.log(text);
    }
    run();

### Multiple file input


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
    reader.onloadend = () =\> resolve(reader.result.split(',')\[1\]);
    reader.readAsDataURL(file);
    });
    return {
    inlineData: { data: await base64EncodedDataPromise, mimeType: file.type },
    };
    }
    async function run() {
    // Provide a text prompt to include with the images
    const prompt = "What's different between these pictures?";
    // Prepare images for input
    const fileInputEl = document.querySelector("input\[type=file\]");
    const imageParts = await Promise.all(
    \[...fileInputEl.files\].map(fileToGenerativePart)
    );
    // To generate text output, call generateContent with the text and images
    const result = await model.generateContent(\[prompt, ...imageParts\]);
    const response = result.response;
    const text = response.text();
    console.log(text);
    }
    run();

### Dart

You can call[`generateContent()`](https://pub.dev/documentation/firebase_ai/latest/firebase_ai/GenerativeModel/generateContent.html)to generate text from multimodal input of text and images.  

### Single file input


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


    // Provide a text prompt to include with the image
    final prompt = TextPart("What's in the picture?");
    // Prepare images for input
    final image = await File('image0.jpg').readAsBytes();
    final imagePart = InlineDataPart('image/jpeg', image);
    // To generate text output, call generateContent with the text and image
    final response = await model.generateContent(\[
    Content.multi(\[prompt,imagePart\])
    \]);
    print(response.text);

### Multiple file input


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


    final (firstImage, secondImage) = await (
    File('image0.jpg').readAsBytes(),
    File('image1.jpg').readAsBytes()
    ).wait;
    // Provide a text prompt to include with the images
    final prompt = TextPart("What's different between these pictures?");
    // Prepare images for input
    final imageParts = \[
    InlineDataPart('image/jpeg', firstImage),
    InlineDataPart('image/jpeg', secondImage),
    \];
    // To generate text output, call generateContent with the text and images
    final response = await model.generateContent(\[
    Content.multi(\[prompt, ...imageParts\])
    \]);
    print(response.text);

### Unity

You can call[`GenerateContentAsync()`](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/generative-model#generatecontentasync)to generate text from multimodal input of text and images.  

### Single file input


    using Firebase;
    using Firebase.AI;

    // Initialize the Gemini Developer API backend service
    var ai = FirebaseAI.GetInstance(FirebaseAI.Backend.GoogleAI());

    // Create a `GenerativeModel` instance with a model that supports your use case
    var model = ai.GetGenerativeModel(modelName: "gemini-2.5-flash");


    // Convert a Texture2D into InlineDataParts
    var grayImage = ModelContent.InlineData("image/png",
    UnityEngine.ImageConversion.EncodeToPNG(UnityEngine.Texture2D.grayTexture));
    // Provide a text prompt to include with the image
    var prompt = ModelContent.Text("What's in this picture?");
    // To generate text output, call GenerateContentAsync and pass in the prompt
    var response = await model.GenerateContentAsync(new \[\] { grayImage, prompt });
    UnityEngine.Debug.Log(response.Text ?? "No text in response.");

### Multiple file input


    using Firebase;
    using Firebase.AI;

    // Initialize the Gemini Developer API backend service
    var ai = FirebaseAI.GetInstance(FirebaseAI.Backend.GoogleAI());

    // Create a `GenerativeModel` instance with a model that supports your use case
    var model = ai.GetGenerativeModel(modelName: "gemini-2.5-flash");


    // Convert Texture2Ds into InlineDataParts
    var blackImage = ModelContent.InlineData("image/png",
    UnityEngine.ImageConversion.EncodeToPNG(UnityEngine.Texture2D.blackTexture));
    var whiteImage = ModelContent.InlineData("image/png",
    UnityEngine.ImageConversion.EncodeToPNG(UnityEngine.Texture2D.whiteTexture));
    // Provide a text prompt to include with the images
    var prompt = ModelContent.Text("What's different between these pictures?");
    // To generate text output, call GenerateContentAsync and pass in the prompt
    var response = await model.GenerateContentAsync(new \[\] { blackImage, whiteImage, prompt });
    UnityEngine.Debug.Log(response.Text ?? "No text in response.");

Learn how to choose a[model](https://firebase.google.com/docs/ai-logic/models)appropriate for your use case and app.

## Stream the response

<br />

|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *Before trying this sample, complete the[Before you begin](https://firebase.google.com/docs/ai-logic/analyze-images#before-you-begin)section of this guide to set up your project and app. **In that section, you'll also click a button for your chosenGemini APIprovider so that you see provider-specific content on this page**.* |

<br />

You can achieve faster interactions by not waiting for the entire result from the model generation, and instead use streaming to handle partial results. To stream the response, call`generateContentStream`.

<br />

#### View example: Stream generated text from image files

<br />

### Swift

You can call[`generateContentStream()`](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Classes/GenerativeModel#generatecontentstream_:)to stream generated text from multimodal input of text and images.  

### Single file input


    import FirebaseAILogic

    // Initialize the Gemini Developer API backend service
    let ai = FirebaseAI.firebaseAI(backend: .googleAI())

    // Create a `GenerativeModel` instance with a model that supports your use case
    let model = ai.generativeModel(modelName: "gemini-2.5-flash")


    guard let image = UIImage(systemName: "bicycle") else { fatalError() }
    // Provide a text prompt to include with the image
    let prompt = "What's in this picture?"
    // To stream generated text output, call generateContentStream and pass in the prompt
    let contentStream = try model.generateContentStream(image, prompt)
    for try await chunk in contentStream {
    if let text = chunk.text {
    print(text)
    }
    }

### Multiple file input


    import FirebaseAILogic

    // Initialize the Gemini Developer API backend service
    let ai = FirebaseAI.firebaseAI(backend: .googleAI())

    // Create a `GenerativeModel` instance with a model that supports your use case
    let model = ai.generativeModel(modelName: "gemini-2.5-flash")


    guard let image1 = UIImage(systemName: "car") else { fatalError() }
    guard let image2 = UIImage(systemName: "car.2") else { fatalError() }
    // Provide a text prompt to include with the images
    let prompt = "What's different between these pictures?"
    // To stream generated text output, call generateContentStream and pass in the prompt
    let contentStream = try model.generateContentStream(image1, image2, prompt)
    for try await chunk in contentStream {
    if let text = chunk.text {
    print(text)
    }
    }

| **Note** : The example above takes advantage of a simplified way to handle platform-native image types provided as inline data, which means the MIME type doesn't need to be specified.[Learn more](https://firebase.google.com/docs/ai-logic/faq-and-troubleshooting#inline-img-sdk-handling)about this feature and options for providing images inline.

### Kotlin

You can call[`generateContentStream()`](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/GenerativeModel#generateContentStream(kotlin.Array))to stream generated text from multimodal input of text and images.
^*For Kotlin, the methods in this SDK are suspend functions and need to be called from a[Coroutine scope](https://developer.android.com/kotlin/coroutines).*^  

### Single file input


    // Initialize the Gemini Developer API backend service
    // Create a `GenerativeModel` instance with a model that supports your use case
    val model = Firebase.ai(backend = GenerativeBackend.googleAI())
                            .generativeModel("gemini-2.5-flash")


    // Loads an image from the app/res/drawable/ directory
    val bitmap: Bitmap = BitmapFactory.decodeResource(resources, R.drawable.sparky)
    // Provide a prompt that includes the image specified above and text
    val prompt = content {
    image(bitmap)
    text("What developer tool is this mascot from?")
    }
    // To stream generated text output, call generateContentStream with the prompt
    var fullResponse = ""
    model.generateContentStream(prompt).collect { chunk -\>
    print(chunk.text)
    fullResponse += chunk.text
    }

### Multiple file input


    // Initialize the Gemini Developer API backend service
    // Create a `GenerativeModel` instance with a model that supports your use case
    val model = Firebase.ai(backend = GenerativeBackend.googleAI())
                            .generativeModel("gemini-2.5-flash")


    // Loads an image from the app/res/drawable/ directory
    val bitmap1: Bitmap = BitmapFactory.decodeResource(resources, R.drawable.sparky)
    val bitmap2: Bitmap = BitmapFactory.decodeResource(resources, R.drawable.sparky_eats_pizza)
    // Provide a prompt that includes the images specified above and text
    val prompt = content {
    image(bitmap1)
    image(bitmap2)
    text("What's different between these pictures?")
    }
    // To stream generated text output, call generateContentStream with the prompt
    var fullResponse = ""
    model.generateContentStream(prompt).collect { chunk -\>
    print(chunk.text)
    fullResponse += chunk.text
    }

| **Note** : The example above takes advantage of a simplified way to handle platform-native image types provided as inline data, which means the MIME type doesn't need to be specified.[Learn more](https://firebase.google.com/docs/ai-logic/faq-and-troubleshooting#inline-img-sdk-handling)about this feature and options for providing images inline.

### Java

You can call[`generateContentStream()`](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/GenerativeModel#generateContentStream(kotlin.Array))to stream generated text from multimodal input of text and images.
^*For Java, the streaming methods in this SDK return a`Publisher`type from the[Reactive Streams library](https://www.reactive-streams.org/).*^  

### Single file input


    // Initialize the Gemini Developer API backend service
    // Create a `GenerativeModel` instance with a model that supports your use case
    GenerativeModel ai = FirebaseAI.getInstance(GenerativeBackend.googleAI())
            .generativeModel("gemini-2.5-flash");

    // Use the GenerativeModelFutures Java compatibility layer which offers
    // support for ListenableFuture and Publisher APIs
    GenerativeModelFutures model = GenerativeModelFutures.from(ai);


    Bitmap bitmap = BitmapFactory.decodeResource(getResources(), R.drawable.sparky);
    // Provide a prompt that includes the image specified above and text
    Content prompt = new Content.Builder()
    .addImage(bitmap)
    .addText("What developer tool is this mascot from?")
    .build();
    // To stream generated text output, call generateContentStream with the prompt
    Publisher\<GenerateContentResponse\> streamingResponse = model.generateContentStream(prompt);
    final String\[\] fullResponse = {""};
    streamingResponse.subscribe(new Subscriber\<GenerateContentResponse\>() {
    @Override
    public void onNext(GenerateContentResponse generateContentResponse) {
    String chunk = generateContentResponse.getText();
    fullResponse\[0\] += chunk;
    }
    @Override
    public void onComplete() {
    System.out.println(fullResponse\[0\]);
    }
    @Override
    public void onError(Throwable t) {
    t.printStackTrace();
    }
    @Override
    public void onSubscribe(Subscription s) {
    }
    });

### Multiple file input


    // Initialize the Gemini Developer API backend service
    // Create a `GenerativeModel` instance with a model that supports your use case
    GenerativeModel ai = FirebaseAI.getInstance(GenerativeBackend.googleAI())
            .generativeModel("gemini-2.5-flash");

    // Use the GenerativeModelFutures Java compatibility layer which offers
    // support for ListenableFuture and Publisher APIs
    GenerativeModelFutures model = GenerativeModelFutures.from(ai);


    Bitmap bitmap1 = BitmapFactory.decodeResource(getResources(), R.drawable.sparky);
    Bitmap bitmap2 = BitmapFactory.decodeResource(getResources(), R.drawable.sparky_eats_pizza);
    // Provide a prompt that includes the images specified above and text
    Content prompt = new Content.Builder()
    .addImage(bitmap1)
    .addImage(bitmap2)
    .addText("What's different between these pictures?")
    .build();
    // To stream generated text output, call generateContentStream with the prompt
    Publisher\<GenerateContentResponse\> streamingResponse = model.generateContentStream(prompt);
    final String\[\] fullResponse = {""};
    streamingResponse.subscribe(new Subscriber\<GenerateContentResponse\>() {
    @Override
    public void onNext(GenerateContentResponse generateContentResponse) {
    String chunk = generateContentResponse.getText();
    fullResponse\[0\] += chunk;
    }
    @Override
    public void onComplete() {
    System.out.println(fullResponse\[0\]);
    }
    @Override
    public void onError(Throwable t) {
    t.printStackTrace();
    }
    @Override
    public void onSubscribe(Subscription s) {
    }
    });

| **Note** : The example above takes advantage of a simplified way to handle platform-native image types provided as inline data, which means the MIME type doesn't need to be specified.[Learn more](https://firebase.google.com/docs/ai-logic/faq-and-troubleshooting#inline-img-sdk-handling)about this feature and options for providing images inline.

### Web

You can call[`generateContentStream()`](https://firebase.google.com/docs/reference/js/ai.generativemodel#generativemodelgeneratecontentstream)to stream generated text from multimodal input of text and images.  

### Single file input


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
    reader.onloadend = () =\> resolve(reader.result.split(',')\[1\]);
    reader.readAsDataURL(file);
    });
    return {
    inlineData: { data: await base64EncodedDataPromise, mimeType: file.type },
    };
    }
    async function run() {
    // Provide a text prompt to include with the image
    const prompt = "What do you see?";
    // Prepare image for input
    const fileInputEl = document.querySelector("input\[type=file\]");
    const imagePart = await fileToGenerativePart(fileInputEl.files\[0\]);
    // To stream generated text output, call generateContentStream with the text and image
    const result = await model.generateContentStream(\[prompt, imagePart\]);
    for await (const chunk of result.stream) {
    const chunkText = chunk.text();
    console.log(chunkText);
    }
    }
    run();

### Multiple file input


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
    reader.onloadend = () =\> resolve(reader.result.split(',')\[1\]);
    reader.readAsDataURL(file);
    });
    return {
    inlineData: { data: await base64EncodedDataPromise, mimeType: file.type },
    };
    }
    async function run() {
    // Provide a text prompt to include with the images
    const prompt = "What's different between these pictures?";
    const fileInputEl = document.querySelector("input\[type=file\]");
    const imageParts = await Promise.all(
    \[...fileInputEl.files\].map(fileToGenerativePart)
    );
    // To stream generated text output, call generateContentStream with the text and images
    const result = await model.generateContentStream(\[prompt, ...imageParts\]);
    for await (const chunk of result.stream) {
    const chunkText = chunk.text();
    console.log(chunkText);
    }
    }
    run();

### Dart

You can call[`generateContentStream()`](https://pub.dev/documentation/firebase_ai/latest/firebase_ai/GenerativeModel/generateContentStream.html)to stream generated text from multimodal input of text and images.  

### Single file input


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


    // Provide a text prompt to include with the image
    final prompt = TextPart("What's in the picture?");
    // Prepare images for input
    final image = await File('image0.jpg').readAsBytes();
    final imagePart = InlineDataPart('image/jpeg', image);
    // To stream generated text output, call generateContentStream with the text and image
    final response = await model.generateContentStream(\[
    Content.multi(\[prompt,imagePart\])
    \]);
    await for (final chunk in response) {
    print(chunk.text);
    }

### Multiple file input


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


    final (firstImage, secondImage) = await (
    File('image0.jpg').readAsBytes(),
    File('image1.jpg').readAsBytes()
    ).wait;
    // Provide a text prompt to include with the images
    final prompt = TextPart("What's different between these pictures?");
    // Prepare images for input
    final imageParts = \[
    InlineDataPart('image/jpeg', firstImage),
    InlineDataPart('image/jpeg', secondImage),
    \];
    // To stream generated text output, call generateContentStream with the text and images
    final response = await model.generateContentStream(\[
    Content.multi(\[prompt, ...imageParts\])
    \]);
    await for (final chunk in response) {
    print(chunk.text);
    }

### Unity

You can call[`GenerateContentStreamAsync()`](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/generative-model#generatecontentstreamasync)to stream generated text from multimodal input of text and images.  

### Single file input


    using Firebase;
    using Firebase.AI;

    // Initialize the Gemini Developer API backend service
    var ai = FirebaseAI.GetInstance(FirebaseAI.Backend.GoogleAI());

    // Create a `GenerativeModel` instance with a model that supports your use case
    var model = ai.GetGenerativeModel(modelName: "gemini-2.5-flash");


    // Convert a Texture2D into InlineDataParts
    var gray = ModelContent.InlineData("image/png",
    UnityEngine.ImageConversion.EncodeToPNG(UnityEngine.Texture2D.grayTexture));
    // Provide a text prompt to include with the image
    var prompt = ModelContent.Text("What's in this picture?");
    // To stream generated text output, call GenerateContentStreamAsync and pass in the prompt
    var responseStream = model.GenerateContentStreamAsync(new \[\] { gray, prompt });
    await foreach (var response in responseStream) {
    if (!string.IsNullOrWhiteSpace(response.Text)) {
    UnityEngine.Debug.Log(response.Text);
    }
    }

### Multiple file input


    using Firebase;
    using Firebase.AI;

    // Initialize the Gemini Developer API backend service
    var ai = FirebaseAI.GetInstance(FirebaseAI.Backend.GoogleAI());

    // Create a `GenerativeModel` instance with a model that supports your use case
    var model = ai.GetGenerativeModel(modelName: "gemini-2.5-flash");


    // Convert Texture2Ds into InlineDataParts
    var black = ModelContent.InlineData("image/png",
    UnityEngine.ImageConversion.EncodeToPNG(UnityEngine.Texture2D.blackTexture));
    var white = ModelContent.InlineData("image/png",
    UnityEngine.ImageConversion.EncodeToPNG(UnityEngine.Texture2D.whiteTexture));
    // Provide a text prompt to include with the images
    var prompt = ModelContent.Text("What's different between these pictures?");
    // To stream generated text output, call GenerateContentStreamAsync and pass in the prompt
    var responseStream = model.GenerateContentStreamAsync(new \[\] { black, white, prompt });
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

## Requirements and recommendations for input image files

<br />

| **Important** :**The total request size limit is 20 MB.** To send large files, review the[options for providing files in multimodal requests](https://firebase.google.com/docs/ai-logic/input-file-requirements).

<br />

Note that a file provided as inline data is encoded to base64 in transit, which increases the size of the request. You get an HTTP 413 error if a request is too large.

See "Supported input files and requirements" page to learn detailed information about the following:

- [Different options for providing a file in a request](https://firebase.google.com/docs/ai-logic/input-file-requirements#options-for-input-files)(either inline or using the file's URL)
- [Requirements and best practices for image files](https://firebase.google.com/docs/ai-logic/input-file-requirements#images)

#### Supported image MIME types

Geminimultimodal models support the following image MIME types:

- PNG -`image/png`
- JPEG -`image/jpeg`
- WebP -`image/webp`

<br />

#### Limits per request

<br />

There isn't a specific limit to the number of pixels in an image. However, larger images are scaled down and padded to fit a maximum resolution of 3072 x 3072 while preserving their original aspect ratio.

Maximum files per request: 3,000 image files

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