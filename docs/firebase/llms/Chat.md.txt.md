# Source: https://firebase.google.com/docs/ai-logic/chat.md.txt

Using the Gemini API, you can build freeform conversations across
multiple turns. The Firebase AI Logic SDK simplifies the process by managing
the state of the conversation, so unlike with `generateContent()`
(or `generateContentStream()`), you don't have to store the conversation history
yourself.

[Jump to code for text-only chat](https://firebase.google.com/docs/ai-logic/chat#chat-prompt)
[Jump to code for iterative image editing](https://firebase.google.com/docs/ai-logic/chat#iterative-image-editing)
[Jump to code for streamed responses](https://firebase.google.com/docs/ai-logic/chat#streaming)

## Before you begin


|---|
| *Click your Gemini API provider to view provider-specific content and code on this page.* <button value="dev" default="">Gemini Developer API</button> <button value="vertex">Vertex AI Gemini API</button> |

<br />

If you haven't already, complete the
[getting started guide](https://firebase.google.com/docs/ai-logic/get-started), which describes how to
set up your Firebase project, connect your app to Firebase, add the SDK,
initialize the backend service for your chosen Gemini API provider, and
create a `GenerativeModel` instance.


> [!NOTE]
> All our docs assume that you're using the [](https://firebase.google.com/support/releases)latest versions of the Firebase AI Logic SDKs.

<br />

For testing and iterating on your prompts, we recommend using [Google AI Studio](https://aistudio.google.com).

## Build a text-only chat experience


|---|
| *Before trying this sample, complete the [Before you begin](https://firebase.google.com/docs/ai-logic/chat#before-you-begin) section of this guide to set up your project and app. **In that section, you'll also click a button for your chosen Gemini API provider so that you see provider-specific content on this page**.* |

<br />

To build a multi-turn conversation (like chat), start off by initializing the
chat by calling `startChat()`. Then use
`sendMessage()` to send a new user message, which
will also append the message and the response to the chat history.

There are two possible options for `role` associated with the content in a
conversation:

- `user`: the role which provides the prompts. This value is the default for
  calls to `sendMessage()`, and the function throws
  an exception if a different role is passed.

- `model`: the role which provides the responses. This role can be used when
  calling `startChat()` with existing `history`.

> [!NOTE]
> **Note:** If you'd like to provide more initial context for the model to help steer its behavior based on your specific needs and use cases, consider [setting system instructions](https://firebase.google.com/docs/ai-logic/system-instructions).

### Swift

You can call
[`startChat()`](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Classes/GenerativeModel#startchathistory:)
and
[`sendMessage()`](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Classes/Chat#sendmessage_:)
to send a new user message:


    import FirebaseAILogic

    // Initialize the Gemini Developer API backend service
    let ai = FirebaseAI.firebaseAI(backend: .googleAI())

    // Create a `GenerativeModel` instance with a model that supports your use case
    let model = ai.generativeModel(modelName: "gemini-3-flash-preview")


    // Optionally specify existing chat history
    let history = \[
    ModelContent(role: "user", parts: "Hello, I have 2 dogs in my house."),
    ModelContent(role: "model", parts: "Great to meet you. What would you like to know?"),
    \]
    // Initialize the chat with optional chat history
    let chat = model.startChat(history: history)
    // To generate text output, call sendMessage and pass in the message
    let response = try await chat.sendMessage("How many paws are in my house?")
    print(response.text ?? "No text in response.")

### Kotlin

You can call [`startChat()`](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/GenerativeModel#startChat(kotlin.collections.List))
and
[`sendMessage()`](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/Chat)
to send a new user message:
^*For Kotlin, the methods in this SDK are suspend functions and need to be called
from a [Coroutine scope](https://developer.android.com/kotlin/coroutines).*^


    // Initialize the Gemini Developer API backend service
    // Create a `GenerativeModel` instance with a model that supports your use case
    val model = Firebase.ai(backend = GenerativeBackend.googleAI())
                            .generativeModel("gemini-3-flash-preview")


    // Initialize the chat
    val chat = model.startChat(
    history = listOf(
    content(role = "user") { text("Hello, I have 2 dogs in my house.") },
    content(role = "model") { text("Great to meet you. What would you like to know?") }
    )
    )
    val response = chat.sendMessage("How many paws are in my house?")
    print(response.text)

### Java

You can call
[`startChat()`](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/GenerativeModel#startChat(kotlin.collections.List))
and
[`sendMessage()`](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/Chat)
to send a new user message:
^*For Java, the methods in this SDK return a
[`ListenableFuture`](https://developer.android.com/guide/background/asynchronous/listenablefuture).*^


    // Initialize the Gemini Developer API backend service
    // Create a `GenerativeModel` instance with a model that supports your use case
    GenerativeModel ai = FirebaseAI.getInstance(GenerativeBackend.googleAI())
            .generativeModel("gemini-3-flash-preview");

    // Use the GenerativeModelFutures Java compatibility layer which offers
    // support for ListenableFuture and Publisher APIs
    GenerativeModelFutures model = GenerativeModelFutures.from(ai);


    // (optional) Create previous chat history for context
    Content.Builder userContentBuilder = new Content.Builder();
    userContentBuilder.setRole("user");
    userContentBuilder.addText("Hello, I have 2 dogs in my house.");
    Content userContent = userContentBuilder.build();
    Content.Builder modelContentBuilder = new Content.Builder();
    modelContentBuilder.setRole("model");
    modelContentBuilder.addText("Great to meet you. What would you like to know?");
    Content modelContent = userContentBuilder.build();
    List\<Content\> history = Arrays.asList(userContent, modelContent);
    // Initialize the chat
    ChatFutures chat = model.startChat(history);
    // Create a new user message
    Content.Builder messageBuilder = new Content.Builder();
    messageBuilder.setRole("user");
    messageBuilder.addText("How many paws are in my house?");
    Content message = messageBuilder.build();
    // Send the message
    ListenableFuture\<GenerateContentResponse\> response = chat.sendMessage(message);
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

### Web

You can call
[`startChat()`](https://firebase.google.com/docs/reference/js/ai.generativemodel#generativemodelstartchat)
and
[`sendMessage()`](https://firebase.google.com/docs/reference/js/ai.chatsession#chatsessionsendmessage)
to send a new user message:


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
    const model = getGenerativeModel(ai, { model: "gemini-3-flash-preview" });


    async function run() {
    const chat = model.startChat({
    history: \[
    {
    role: "user",
    parts: \[{ text: "Hello, I have 2 dogs in my house." }\],
    },
    {
    role: "model",
    parts: \[{ text: "Great to meet you. What would you like to know?" }\],
    },
    \],
    generationConfig: {
    maxOutputTokens: 100,
    },
    });
    const msg = "How many paws are in my house?";
    const result = await chat.sendMessage(msg);
    const text = result.response.text();
    console.log(text);
    }
    run();

### Dart

You can call
[`startChat()`](https://pub.dev/documentation/firebase_ai/latest/firebase_ai/StartChatExtension/startChat.html)
and
[`sendMessage()`](https://pub.dev/documentation/firebase_ai/latest/firebase_ai/ChatSession/sendMessage.html)
to send a new user message:


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
          FirebaseAI.googleAI().generativeModel(model: 'gemini-3-flash-preview');


    final chat = model.startChat();
    // Provide a prompt that contains text
    final prompt = \[Content.text('Write a story about a magic backpack.')\];
    final response = await chat.sendMessage(prompt);
    print(response.text);

### Unity

You can call
[`StartChat()`](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/generative-model#startchat)
and
[`SendMessageAsync()`](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/chat#sendmessageasync)
to send a new user message:


    using Firebase;
    using Firebase.AI;

    // Initialize the Gemini Developer API backend service
    var ai = FirebaseAI.GetInstance(FirebaseAI.Backend.GoogleAI());

    // Create a `GenerativeModel` instance with a model that supports your use case
    var model = ai.GetGenerativeModel(modelName: "gemini-3-flash-preview");


    // Optionally specify existing chat history
    var history = new \[\] {
    ModelContent.Text("Hello, I have 2 dogs in my house."),
    new ModelContent("model", new ModelContent.TextPart("Great to meet you. What would you like to know?")),
    };
    // Initialize the chat with optional chat history
    var chat = model.StartChat(history);
    // To generate text output, call SendMessageAsync and pass in the message
    var response = await chat.SendMessageAsync("How many paws are in my house?");
    UnityEngine.Debug.Log(response.Text ?? "No text in response.");


Learn how to choose a [model](https://firebase.google.com/docs/ai-logic/models)

appropriate for your use case and app.

## Iterate and edit images using multi-turn chat


|---|
| *Before trying this sample, complete the [Before you begin](https://firebase.google.com/docs/ai-logic/chat#before-you-begin) section of this guide to set up your project and app. **In that section, you'll also click a button for your chosen Gemini API provider so that you see provider-specific content on this page**.* |

<br />

> [!IMPORTANT]
> **Important:** Image output from Gemini is supported by `gemini-2.5-flash-image`, but it's *not* supported by the standard Flash models like `gemini-2.5-flash`.

Using multi-turn chat, you can iterate with a Gemini model on the
images that it generates or that you supply.

Make sure to create a `GenerativeModel` instance, include
`responseModalities: ["TEXT", "IMAGE"]` in your model
configuration, and call `startChat()` and `sendMessage()` to send new user
messages.

> [!IMPORTANT]
> **Important:** If you're not familiar with the chat capability of the SDKs, we recommend reviewing the [text-only chat example](https://firebase.google.com/docs/ai-logic/chat#chat-prompt).

### Swift


    import FirebaseAILogic

    // Initialize the Gemini Developer API backend service
    // Create a `GenerativeModel` instance with a Gemini model that supports image output
    let generativeModel = FirebaseAI.firebaseAI(backend: .googleAI()).generativeModel(
      modelName: "gemini-2.5-flash-image",
      // Configure the model to respond with text and images (required)
      generationConfig: GenerationConfig(responseModalities: [.text, .image])
    )

    // Initialize the chat
    let chat = model.startChat()

    guard let image = UIImage(named: "scones") else { fatalError("Image file not found.") }

    // Provide an initial text prompt instructing the model to edit the image
    let prompt = "Edit this image to make it look like a cartoon"

    // To generate an initial response, send a user message with the image and text prompt
    let response = try await chat.sendMessage(image, prompt)

    // Inspect the generated image
    guard let inlineDataPart = response.inlineDataParts.first else {
      fatalError("No image data in response.")
    }
    guard let uiImage = UIImage(data: inlineDataPart.data) else {
      fatalError("Failed to convert data to UIImage.")
    }

    // Follow up requests do not need to specify the image again
    let followUpResponse = try await chat.sendMessage("But make it old-school line drawing style")

    // Inspect the edited image after the follow up request
    guard let followUpInlineDataPart = followUpResponse.inlineDataParts.first else {
      fatalError("No image data in response.")
    }
    guard let followUpUIImage = UIImage(data: followUpInlineDataPart.data) else {
      fatalError("Failed to convert data to UIImage.")
    }

### Kotlin


    // Initialize the Gemini Developer API backend service
    // Create a `GenerativeModel` instance with a Gemini model that supports image output
    val model = Firebase.ai(backend = GenerativeBackend.googleAI()).generativeModel(
        modelName = "gemini-2.5-flash-image",
        // Configure the model to respond with text and images (required)
        generationConfig = generationConfig {
    responseModalities = listOf(ResponseModality.TEXT, ResponseModality.IMAGE) }
    )

    // Provide an image for the model to edit
    val bitmap = BitmapFactory.decodeResource(context.resources, R.drawable.scones)

    // Create the initial prompt instructing the model to edit the image
    val prompt = content {
        image(bitmap)
        text("Edit this image to make it look like a cartoon")
    }

    // Initialize the chat
    val chat = model.startChat()

    // To generate an initial response, send a user message with the image and text prompt
    var response = chat.sendMessage(prompt)
    // Inspect the returned image
    var generatedImageAsBitmap = response
        .candidates.first().content.parts.filterIsInstance<ImagePart>().firstOrNull()?.image

    // Follow up requests do not need to specify the image again
    response = chat.sendMessage("But make it old-school line drawing style")
    generatedImageAsBitmap = response
        .candidates.first().content.parts.filterIsInstance<ImagePart>().firstOrNull()?.image

### Java


    // Initialize the Gemini Developer API backend service
    // Create a `GenerativeModel` instance with a Gemini model that supports image output
    GenerativeModel ai = FirebaseAI.getInstance(GenerativeBackend.googleAI()).generativeModel(
        "gemini-2.5-flash-image",
        // Configure the model to respond with text and images (required)
        new GenerationConfig.Builder()
            .setResponseModalities(Arrays.asList(ResponseModality.TEXT, ResponseModality.IMAGE))
            .build()
    );

    GenerativeModelFutures model = GenerativeModelFutures.from(ai);

    // Provide an image for the model to edit
    Bitmap bitmap = BitmapFactory.decodeResource(resources, R.drawable.scones);

    // Initialize the chat
    ChatFutures chat = model.startChat();

    // Create the initial prompt instructing the model to edit the image
    Content prompt = new Content.Builder()
            .setRole("user")
            .addImage(bitmap)
            .addText("Edit this image to make it look like a cartoon")
            .build();

    // To generate an initial response, send a user message with the image and text prompt
    ListenableFuture<GenerateContentResponse> response = chat.sendMessage(prompt);
    // Extract the image from the initial response
    ListenableFuture<@Nullable Bitmap> initialRequest = Futures.transform(response, result -> {
        for (Part part : result.getCandidates().get(0).getContent().getParts()) {
            if (part instanceof ImagePart) {
                ImagePart imagePart = (ImagePart) part;
                return imagePart.getImage();
            }
        }
        return null;
    }, executor);

    // Follow up requests do not need to specify the image again
    ListenableFuture<GenerateContentResponse> modelResponseFuture = Futures.transformAsync(
            initialRequest,
            generatedImage -> {
                Content followUpPrompt = new Content.Builder()
                        .addText("But make it old-school line drawing style")
                        .build();
                return chat.sendMessage(followUpPrompt);
            },
            executor);

    // Add a final callback to check the reworked image
    Futures.addCallback(modelResponseFuture, new FutureCallback<GenerateContentResponse>() {
        @Override
        public void onSuccess(GenerateContentResponse result) {
            for (Part part : result.getCandidates().get(0).getContent().getParts()) {
                if (part instanceof ImagePart) {
                    ImagePart imagePart = (ImagePart) part;
                    Bitmap generatedImageAsBitmap = imagePart.getImage();
                    break;
                }
            }
        }

        @Override
        public void onFailure(Throwable t) {
            t.printStackTrace();
        }
    }, executor);

### Web


    import { initializeApp } from "firebase/app";
    import { getAI, getGenerativeModel, GoogleAIBackend, ResponseModality } from "firebase/ai";

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
    const model = getGenerativeModel(ai, {
      model: "gemini-2.5-flash-image",
      // Configure the model to respond with text and images (required)
      generationConfig: {
        responseModalities: [ResponseModality.TEXT, ResponseModality.IMAGE],
      },
    });

    // Prepare an image for the model to edit
    async function fileToGenerativePart(file) {
      const base64EncodedDataPromise = new Promise((resolve) => {
        const reader = new FileReader();
        reader.onloadend = () => resolve(reader.result.split(',')[1]);
        reader.readAsDataURL(file);
      });
      return {
        inlineData: { data: await base64EncodedDataPromise, mimeType: file.type },
      };
    }

    const fileInputEl = document.querySelector("input[type=file]");
    const imagePart = await fileToGenerativePart(fileInputEl.files[0]);

    // Provide an initial text prompt instructing the model to edit the image
    const prompt = "Edit this image to make it look like a cartoon";

    // Initialize the chat
    const chat = model.startChat();

    // To generate an initial response, send a user message with the image and text prompt
    const result = await chat.sendMessage([prompt, imagePart]);

    // Request and inspect the generated image
    try {
      const inlineDataParts = result.response.inlineDataParts();
      if (inlineDataParts?.[0]) {
        // Inspect the generated image
        const image = inlineDataParts[0].inlineData;
        console.log(image.mimeType, image.data);
      }
    } catch (err) {
      console.error('Prompt or candidate was blocked:', err);
    }

    // Follow up requests do not need to specify the image again
    const followUpResult = await chat.sendMessage("But make it old-school line drawing style");

    // Request and inspect the returned image
    try {
      const followUpInlineDataParts = followUpResult.response.inlineDataParts();
      if (followUpInlineDataParts?.[0]) {
        // Inspect the generated image
        const followUpImage = followUpInlineDataParts[0].inlineData;
        console.log(followUpImage.mimeType, followUpImage.data);
      }
    } catch (err) {
      console.error('Prompt or candidate was blocked:', err);
    }

### Dart


    import 'package:firebase_ai/firebase_ai.dart';
    import 'package:firebase_core/firebase_core.dart';
    import 'firebase_options.dart';

    await Firebase.initializeApp(
      options: DefaultFirebaseOptions.currentPlatform,
    );

    // Initialize the Gemini Developer API backend service
    // Create a `GenerativeModel` instance with a Gemini model that supports image output
    final model = FirebaseAI.googleAI().generativeModel(
      model: 'gemini-2.5-flash-image',
      // Configure the model to respond with text and images (required)
      generationConfig: GenerationConfig(responseModalities: [ResponseModalities.text, ResponseModalities.image]),
    );

    // Prepare an image for the model to edit
    final image = await File('scones.jpg').readAsBytes();
    final imagePart = InlineDataPart('image/jpeg', image);

    // Provide an initial text prompt instructing the model to edit the image
    final prompt = TextPart("Edit this image to make it look like a cartoon");

    // Initialize the chat
    final chat = model.startChat();

    // To generate an initial response, send a user message with the image and text prompt
    final response = await chat.sendMessage([
      Content.multi([prompt,imagePart])
    ]);

    // Inspect the returned image
    if (response.inlineDataParts.isNotEmpty) {
      final imageBytes = response.inlineDataParts[0].bytes;
      // Process the image
    } else {
      // Handle the case where no images were generated
      print('Error: No images were generated.');
    }

    // Follow up requests do not need to specify the image again
    final followUpResponse = await chat.sendMessage([
      Content.text("But make it old-school line drawing style")
    ]);

    // Inspect the returned image
    if (followUpResponse.inlineDataParts.isNotEmpty) {
      final followUpImageBytes = response.inlineDataParts[0].bytes;
      // Process the image
    } else {
      // Handle the case where no images were generated
      print('Error: No images were generated.');
    }

### Unity


    using Firebase;
    using Firebase.AI;

    // Initialize the Gemini Developer API backend service
    // Create a `GenerativeModel` instance with a Gemini model that supports image output
    var model = FirebaseAI.GetInstance(FirebaseAI.Backend.GoogleAI()).GetGenerativeModel(
      modelName: "gemini-2.5-flash-image",
      // Configure the model to respond with text and images (required)
      generationConfig: new GenerationConfig(
        responseModalities: new[] { ResponseModality.Text, ResponseModality.Image })
    );

    // Prepare an image for the model to edit
    var imageFile = System.IO.File.ReadAllBytes(System.IO.Path.Combine(
      UnityEngine.Application.streamingAssetsPath, "scones.jpg"));
    var image = ModelContent.InlineData("image/jpeg", imageFile);

    // Provide an initial text prompt instructing the model to edit the image
    var prompt = ModelContent.Text("Edit this image to make it look like a cartoon.");

    // Initialize the chat
    var chat = model.StartChat();

    // To generate an initial response, send a user message with the image and text prompt
    var response = await chat.SendMessageAsync(new [] { prompt, image });

    // Inspect the returned image
    var imageParts = response.Candidates.First().Content.Parts
                             .OfType<ModelContent.InlineDataPart>()
                             .Where(part => part.MimeType == "image/png");
    // Load the image into a Unity Texture2D object
    UnityEngine.Texture2D texture2D = new(2, 2);
    if (texture2D.LoadImage(imageParts.First().Data.ToArray())) {
      // Do something with the image
    }

    // Follow up requests do not need to specify the image again
    var followUpResponse = await chat.SendMessageAsync("But make it old-school line drawing style");

    // Inspect the returned image
    var followUpImageParts = followUpResponse.Candidates.First().Content.Parts
                             .OfType<ModelContent.InlineDataPart>()
                             .Where(part => part.MimeType == "image/png");
    // Load the image into a Unity Texture2D object
    UnityEngine.Texture2D followUpTexture2D = new(2, 2);
    if (followUpTexture2D.LoadImage(followUpImageParts.First().Data.ToArray())) {
      // Do something with the image
    }

## Stream the response


|---|
| *Before trying this sample, complete the [Before you begin](https://firebase.google.com/docs/ai-logic/chat#before-you-begin) section of this guide to set up your project and app. **In that section, you'll also click a button for your chosen Gemini API provider so that you see provider-specific content on this page**.* |

<br />

You can achieve faster interactions by not waiting for the entire result from
the model generation, and instead use streaming to handle partial results.
To stream the response, call `sendMessageStream()`.

<br />

#### View example: Stream chat responses

<br />

### Swift

You can call
[`startChat()`](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Classes/GenerativeModel#startchathistory:)
and
[`sendMessageStream()`](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Classes/Chat#sendmessagestream_:)
to stream responses from the model:


    import FirebaseAILogic

    // Initialize the Gemini Developer API backend service
    let ai = FirebaseAI.firebaseAI(backend: .googleAI())

    // Create a `GenerativeModel` instance with a model that supports your use case
    let model = ai.generativeModel(modelName: "gemini-3-flash-preview")


    // Optionally specify existing chat history
    let history = \[
    ModelContent(role: "user", parts: "Hello, I have 2 dogs in my house."),
    ModelContent(role: "model", parts: "Great to meet you. What would you like to know?"),
    \]
    // Initialize the chat with optional chat history
    let chat = model.startChat(history: history)
    // To stream generated text output, call sendMessageStream and pass in the message
    let contentStream = try chat.sendMessageStream("How many paws are in my house?")
    for try await chunk in contentStream {
    if let text = chunk.text {
    print(text)
    }
    }

### Kotlin

You can call
[`startChat()`](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/GenerativeModel#startChat(kotlin.collections.List))
and
[`sendMessageStream()`](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/Chat)
to stream responses from the model:
^*For Kotlin, the methods in this SDK are suspend functions and need to be called
from a [Coroutine scope](https://developer.android.com/kotlin/coroutines).*^


    // Initialize the Gemini Developer API backend service
    // Create a `GenerativeModel` instance with a model that supports your use case
    val model = Firebase.ai(backend = GenerativeBackend.googleAI())
                            .generativeModel("gemini-3-flash-preview")


    // Initialize the chat
    val chat = model.startChat(
    history = listOf(
    content(role = "user") { text("Hello, I have 2 dogs in my house.") },
    content(role = "model") { text("Great to meet you. What would you like to know?") }
    )
    )
    chat.sendMessageStream("How many paws are in my house?").collect { chunk -\>
    print(chunk.text)
    }

### Java

You can call
[`startChat()`](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/GenerativeModel#startChat(kotlin.collections.List))
and
[`sendMessageStream()`](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/Chat)
to stream responses from the model:
^*For Java, the streaming methods in this SDK return a
`Publisher` type from the [Reactive Streams library](https://www.reactive-streams.org/).*^


    // Initialize the Gemini Developer API backend service
    // Create a `GenerativeModel` instance with a model that supports your use case
    GenerativeModel ai = FirebaseAI.getInstance(GenerativeBackend.googleAI())
            .generativeModel("gemini-3-flash-preview");

    // Use the GenerativeModelFutures Java compatibility layer which offers
    // support for ListenableFuture and Publisher APIs
    GenerativeModelFutures model = GenerativeModelFutures.from(ai);


    // (optional) Create previous chat history for context
    Content.Builder userContentBuilder = new Content.Builder();
    userContentBuilder.setRole("user");
    userContentBuilder.addText("Hello, I have 2 dogs in my house.");
    Content userContent = userContentBuilder.build();
    Content.Builder modelContentBuilder = new Content.Builder();
    modelContentBuilder.setRole("model");
    modelContentBuilder.addText("Great to meet you. What would you like to know?");
    Content modelContent = userContentBuilder.build();
    List\<Content\> history = Arrays.asList(userContent, modelContent);
    // Initialize the chat
    ChatFutures chat = model.startChat(history);
    // Create a new user message
    Content.Builder messageBuilder = new Content.Builder();
    messageBuilder.setRole("user");
    messageBuilder.addText("How many paws are in my house?");
    Content message = messageBuilder.build();
    // Send the message
    Publisher\<GenerateContentResponse\> streamingResponse =
    chat.sendMessageStream(message);
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
    // ... other methods omitted for brevity
    });

### Web

You can call
[`startChat()`](https://firebase.google.com/docs/reference/js/ai.generativemodel#generativemodelstartchat)
and
[`sendMessageStream()`](https://firebase.google.com/docs/reference/js/ai.chatsession#chatsessionsendmessagestream)
to stream responses from the model:


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
    const model = getGenerativeModel(ai, { model: "gemini-3-flash-preview" });


    async function run() {
    const chat = model.startChat({
    history: \[
    {
    role: "user",
    parts: \[{ text: "Hello, I have 2 dogs in my house." }\],
    },
    {
    role: "model",
    parts: \[{ text: "Great to meet you. What would you like to know?" }\],
    },
    \],
    generationConfig: {
    maxOutputTokens: 100,
    },
    });
    const msg = "How many paws are in my house?";
    const result = await chat.sendMessageStream(msg);
    let text = '';
    for await (const chunk of result.stream) {
    const chunkText = chunk.text();
    console.log(chunkText);
    text += chunkText;
    }
    }
    run();

### Dart

You can call
[`startChat()`](https://pub.dev/documentation/firebase_ai/latest/firebase_ai/StartChatExtension/startChat.html)
and
[`sendMessageStream()`](https://pub.dev/documentation/firebase_ai/latest/firebase_ai/ChatSession/sendMessageStream.html)
to stream responses from the model:


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
          FirebaseAI.googleAI().generativeModel(model: 'gemini-3-flash-preview');


    final chat = model.startChat();
    // Provide a prompt that contains text
    final prompt = \[Content.text('Write a story about a magic backpack.')\];
    final response = await chat.sendMessageStream(prompt);
    await for (final chunk in response) {
    print(chunk.text);
    }

### Unity

You can call
[`StartChat()`](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/generative-model#startchat)
and
[`SendMessageStreamAsync()`](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/chat#sendmessagestreamasync)
to stream responses from the model:


    using Firebase;
    using Firebase.AI;

    // Initialize the Gemini Developer API backend service
    var ai = FirebaseAI.GetInstance(FirebaseAI.Backend.GoogleAI());

    // Create a `GenerativeModel` instance with a model that supports your use case
    var model = ai.GetGenerativeModel(modelName: "gemini-3-flash-preview");


    // Optionally specify existing chat history
    var history = new \[\] {
    ModelContent.Text("Hello, I have 2 dogs in my house."),
    new ModelContent("model", new ModelContent.TextPart("Great to meet you. What would you like to know?")),
    };
    // Initialize the chat with optional chat history
    var chat = model.StartChat(history);
    // To stream generated text output, call SendMessageStreamAsync and pass in the message
    var responseStream = chat.SendMessageStreamAsync("How many paws are in my house?");
    await foreach (var response in responseStream) {
    if (!string.IsNullOrWhiteSpace(response.Text)) {
    UnityEngine.Debug.Log(response.Text);
    }
    }


Learn how to choose a [model](https://firebase.google.com/docs/ai-logic/models)

appropriate for your use case and app.

<br />

<br />

<br />

*** ** * ** ***

## What else can you do?

- Learn how to [count tokens](https://firebase.google.com/docs/ai-logic/count-tokens) before sending long prompts to the model.
- [Set up Cloud Storage for Firebase](https://firebase.google.com/docs/ai-logic/solutions/cloud-storage) so that you can include large files in your multimodal requests and have a more managed solution for providing files in prompts. Files can include images, PDFs, video, and audio.
- Start thinking about preparing for production (see the [production checklist](https://firebase.google.com/docs/ai-logic/production-checklist)), including:
  - [Setting up Firebase App Check](https://firebase.google.com/docs/ai-logic/app-check) to protect the Gemini API from abuse by unauthorized clients.
  - [Integrating Firebase Remote Config](https://firebase.google.com/docs/ai-logic/solutions/remote-config) to update values in your app (like model name) without releasing a new app version.


#### Try out other capabilities

<br />

- Generate text from [text-only prompts](https://firebase.google.com/docs/ai-logic/generate-text).
- Generate text by prompting with various file types, like [images](https://firebase.google.com/docs/ai-logic/analyze-images), [PDFs](https://firebase.google.com/docs/ai-logic/analyze-documents), [video](https://firebase.google.com/docs/ai-logic/analyze-video), and [audio](https://firebase.google.com/docs/ai-logic/analyze-audio).
- Generate [structured output (like JSON)](https://firebase.google.com/docs/ai-logic/generate-structured-output) from both text and multimodal prompts.
- Generate images from text prompts ([Gemini](https://firebase.google.com/docs/ai-logic/generate-images-gemini) or [Imagen](https://firebase.google.com/docs/ai-logic/generate-images-imagen)).
- Use tools (like [function calling](https://firebase.google.com/docs/ai-logic/function-calling) and [grounding with Google Search](https://firebase.google.com/docs/ai-logic/grounding-google-search)) to connect a Gemini model to other parts of your app and external systems and information.


#### Learn how to control content generation

- [Understand prompt design](https://firebase.google.com/docs/ai-logic/prompt-design), including best practices, strategies, and example prompts.
- [Configure model parameters](https://firebase.google.com/docs/ai-logic/model-parameters) like temperature and maximum output tokens (for Gemini) or aspect ratio and person generation (for Imagen).
- [Use safety settings](https://firebase.google.com/docs/ai-logic/safety-settings) to adjust the likelihood of getting responses that may be considered harmful.

You can also experiment with prompts and model configurations and even get a generated code snippet using [Google AI Studio](https://aistudio.google.com).

<br />


#### Learn more about the supported models

Learn about the [models available for various use cases](https://firebase.google.com/docs/ai-logic/models) and their [quotas](https://firebase.google.com/docs/ai-logic/quotas) and [pricing](https://firebase.google.com/docs/ai-logic/pricing).

<br />

<br />

[Give feedback
about your experience with Firebase AI Logic](https://firebase.google.com/docs/ai-logic/feedback)

<br />