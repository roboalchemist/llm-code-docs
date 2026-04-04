# Source: https://firebase.google.com/docs/ai-logic/get-started.md.txt

This guide shows you how to get started making calls to the Gemini API
directly from your app using the Firebase AI Logic client SDKs
for your chosen platform.

You can also use this guide to get started with
[accessing Imagen models](https://firebase.google.com/docs/ai-logic/generate-images-imagen)
using the Firebase AI Logic SDKs.

## Prerequisites

### Swift

This guide assumes that you're familiar with using Xcode to develop apps for
Apple platforms (like iOS).

Make sure that your development environment and Apple platforms app meet
these requirements:

- Xcode 16.2 or higher
- Your app targets iOS 15 or higher, or macOS 12 or higher

### Kotlin

This guide assumes that you're familiar with using Android Studio to develop
apps for Android.

Make sure that your development environment and Android app meet these
requirements:

- Android Studio (latest version)
- Your app targets API level 21 or higher

### Java

This guide assumes that you're familiar with using Android Studio to develop
apps for Android.

Make sure that your development environment and Android app meet these
requirements:

- Android Studio (latest version)
- Your app targets API level 21 or higher

### Web

This guide assumes that you're familiar with using JavaScript to develop
web apps. This guide is framework-independent.

Make sure that your development environment and web app meet these
requirements:

- *(Optional)* Node.js
- Modern web browser

### Dart

This guide assumes that you're familiar with developing apps with Flutter.

Make sure that your development environment and Flutter app meet these
requirements:

- Dart 3.2.0+

### Unity

This guide assumes that you're familiar with developing games with Unity.

Make sure that your development environment and Unity game meet these
requirements:

- Unity Editor 2021 LTS or newer

### Check out helpful resources

### Swift

#### Try out the quickstart app

Use the quickstart app to try out the SDK quickly and see a complete
implementation of various use cases. Or use the quickstart app if you don't
have your own Apple platforms app. To use the quickstart app, you'll need to
[connect it to a Firebase project](https://firebase.google.com/docs/ai-logic/get-started#set-up-firebase).

[Go to the quickstart app](https://github.com/firebase/quickstart-ios/tree/main/firebaseai)

#### Watch a video tutorial

[Video](https://www.youtube.com/watch?v=ukyUxcXlwaI)

This video demonstrates how to get started with Firebase AI Logic by
building a real-world AI-powered meal planning app that generates recipes from
a text prompt.

You can also download and explore the codebase for the app in the video.

[View the codebase for the video's app](https://github.com/FirebaseExtended/firebase-video-samples/tree/main/firebase-ai-friendly-meals/apple)

<br />


<br />

### Kotlin

#### Try out the quickstart app

Use the quickstart app to try out the SDK quickly and see a complete
implementation of various use cases. Or use the quickstart app if you don't
have your own Android app. To use the quickstart app, you'll need to
[connect it to a Firebase project](https://firebase.google.com/docs/ai-logic/get-started#set-up-firebase).

[Go to the quickstart app](https://github.com/firebase/quickstart-android/tree/master/firebase-ai)

#### Watch a video tutorial

[Video](https://www.youtube.com/watch?v=0UoReIOwC-Q)

This video demonstrates how to get started with Firebase AI Logic by
building a real-world AI-powered meal planning app that generates recipes from
a text prompt.

You can also download and explore the codebase for the app in the video.

[View the codebase for the video's app](https://github.com/FirebaseExtended/firebase-video-samples/tree/main/firebase-ai-friendly-meals/android)

<br />


<br />

### Java

#### Try out the quickstart app

Use the quickstart app to try out the SDK quickly and see a complete
implementation of various use cases. Or use the quickstart app if you don't
have your own Android app. To use the quickstart app, you'll need to
[connect it to a Firebase project](https://firebase.google.com/docs/ai-logic/get-started#set-up-firebase).

[Go to the quickstart app](https://github.com/firebase/quickstart-android/tree/master/firebase-ai)

#### Watch a video tutorial

[Video](https://www.youtube.com/watch?v=0UoReIOwC-Q)

This video demonstrates how to get started with Firebase AI Logic by
building a real-world AI-powered meal planning app that generates recipes from
a text prompt.^**\***^

You can also download and explore the codebase for the app in the video.

[View the codebase for the video's app](https://github.com/FirebaseExtended/firebase-video-samples/tree/main/firebase-ai-friendly-meals/android)

^**\*** *This video and its app are in Kotlin, but they can still
help Java developers understand the basics about how to get started with
Firebase AI Logic.*^

### Web

#### Try out the quickstart app

Use the quickstart app to try out the SDK quickly and see a complete
implementation of various use cases. Or use the quickstart app if you don't
have your own web app. To use the quickstart app, you'll need to
[connect it to a Firebase project](https://firebase.google.com/docs/ai-logic/get-started#set-up-firebase).

[Go to the quickstart app](https://github.com/firebase/quickstart-js/tree/master/ai/ai-react-app)

### Dart

#### Try out the quickstart app

Use the quickstart app to try out the SDK quickly and see a complete
implementation of various use cases. Or use the quickstart app if you don't
have your own Flutter app. To use the quickstart app, you'll need to
[connect it to a Firebase project](https://firebase.google.com/docs/ai-logic/get-started#set-up-firebase).

[Go to the quickstart app](https://github.com/firebase/flutterfire/tree/main/packages/firebase_ai/firebase_ai/example)

#### Watch a video tutorial

[Video](https://www.youtube.com/watch?v=LEG50u4nwRc)

This video demonstrates how to get started with Firebase AI Logic by
building a real-world AI-powered meal planning app that generates recipes from
a text prompt.

You can also download and explore the codebase for the app in the video.

[View the codebase for the video's app](https://github.com/FirebaseExtended/firebase-video-samples/tree/main/firebase-ai-friendly-meals/flutter)

<br />


<br />

### Unity

#### Try out the quickstart app

Use the quickstart app to try out the SDK quickly and see a complete
implementation of various use cases. Or use the quickstart app if you don't
have your own Unity game. To use the quickstart app, you'll need to
[connect it to a Firebase project](https://firebase.google.com/docs/ai-logic/get-started#set-up-firebase).

[Go to the quickstart app](https://github.com/firebase/quickstart-unity/tree/master/firebaseai/testapp)

## **Step 1**: Set up a Firebase project and connect your app

1. Sign into the [Firebase console](https://console.firebase.google.com/),
   and then select your Firebase project.

   <br />

   Don't already have a Firebase project?

   <br />

   If you don't already have a Firebase project, click the button to create a
   new Firebase project, and then use either of the following options:
   - **Option 1** : Create a wholly new Firebase project (and its underlying
     Google Cloud project automatically) by entering a new project name in the
     first step of the workflow.

   - **Option 2** : "Add Firebase" to an existing Google Cloud project by
     clicking **Add Firebase to Google Cloud project** (at bottom of page).
     In the first step of the workflow, start entering the **project name** of
     the existing project, and then select the project from the displayed list.

   Complete the remaining steps of the on-screen workflow to create a Firebase
   project. Note that when prompted, you do ***not*** need to set up
   Google Analytics to use the Firebase AI Logic SDKs.

   <br />

   <br />

2. In the Firebase console, go to the [**Firebase AI Logic** page](https://console.firebase.google.com/project/_/ailogic).

3. Click **Get started** to launch a guided workflow that helps you set up the
   [required APIs](https://firebase.google.com/docs/ai-logic/faq-and-troubleshooting#required-apis)
   and resources for your project.

4. Set up your project to use a "Gemini API" provider.

   **We recommend getting started using the Gemini Developer API.**
   At any point, you can always
   [set up the Vertex AI Gemini API](https://console.firebase.google.com/project/_/ailogic?openVertexAiOnboarding=true)
   (and its requirement for billing).

   For the Gemini Developer API, the console will enable the required
   APIs and create a Gemini API key in your project.  

   *Do **not** add this Gemini API key into your app's codebase.*
   [Learn more.](https://firebase.google.com/docs/ai-logic/faq-and-troubleshooting#add-gemini-api-key-to-codebase)
5. If prompted in the console's workflow, follow the on-screen instructions to
   register your app and connect it to Firebase.

6. Continue to the next step in this guide to add the SDK to your app.

> [!NOTE]
> **Note:** In the Firebase console, you're strongly encouraged to [set up Firebase App Check](https://firebase.google.com/docs/ai-logic/app-check). If you're just trying out the Gemini API, you don't need to set up App Check right away; however, we recommend setting it up as soon as you start seriously developing your app.

## **Step 2**: Add the SDK

With your Firebase project set up and your app connected to Firebase
(see previous step), you can now add the Firebase AI Logic SDK to your app.

### Swift

Use Swift Package Manager to install and manage Firebase dependencies.

> [!NOTE]
> **Note:** Visit [our installation guide](https://firebase.google.com/docs/ios/installation-methods) to learn about the different ways you can add Firebase SDKs to your Apple project.

The Firebase AI Logic library provides access to the APIs for interacting
with Gemini and Imagen models. The library is included
as part of the Firebase SDK for Apple platforms (`firebase-ios-sdk`).

If you're already using Firebase, then make sure your Firebase package is
v12.5.0 or later.

1. In Xcode, with your app project open, navigate to
   **File \> Add Package Dependencies**.

2. When prompted, add the Firebase Apple platforms SDK repository:

       https://github.com/firebase/firebase-ios-sdk

3. Select the latest SDK version.

4. Select the **`FirebaseAILogic`** library.

When finished, Xcode will automatically begin resolving and downloading your
dependencies in the background.

### Kotlin

The Firebase AI Logic SDK for Android (`firebase-ai`) provides
access to the APIs for interacting with
Gemini and Imagen models.

In your **module (app-level) Gradle file**
(like `<project>/<app-module>/build.gradle.kts`),
add the dependency for the Firebase AI Logic library for Android.
We recommend using the
[Firebase Android BoM](https://firebase.google.com/docs/android/learn-more#bom)
to control library versioning.

```groovy
dependencies {
  // ... other androidx dependencies

  // Import the BoM for the Firebase platform
  implementation(platform("com.google.firebase:firebase-bom:34.10.0"))

  // Add the dependency for the Firebase AI Logic library
  // When using the BoM, you don't specify versions in Firebase library dependencies
  implementation("com.google.firebase:firebase-ai")
}
```

By using the [Firebase Android BoM](https://firebase.google.com/docs/android/learn-more#bom),
your app will always use compatible versions of Firebase Android libraries.


*(Alternative)*
Add Firebase library dependencies *without* using the BoM

<br />

If you choose not to use the Firebase BoM, you must specify each
Firebase library version in its dependency line.

**Note that if you use *multiple* Firebase libraries in your app, we
strongly recommend using the BoM to manage library versions, which
ensures that all versions are compatible.**

```groovy
dependencies {
  // Add the dependency for the Firebase AI Logic library
  // When NOT using the BoM, you must specify versions in Firebase library dependencies
  implementation("com.google.firebase:firebase-ai:17.10.0")
}
```

<br />

<br />

### Java

The Firebase AI Logic SDK for Android (`firebase-ai`) provides
access to the APIs for interacting with
Gemini and Imagen models.

In your **module (app-level) Gradle file**
(like `<project>/<app-module>/build.gradle.kts`),
add the dependency for the Firebase AI Logic library for Android.
We recommend using the
[Firebase Android BoM](https://firebase.google.com/docs/android/learn-more#bom)
to control library versioning.

For Java, you need to add two additional libraries.

```groovy
dependencies {
  // ... other androidx dependencies

  // Import the BoM for the Firebase platform
  implementation(platform("com.google.firebase:firebase-bom:34.10.0"))

  // Add the dependency for the Firebase AI Logic library
  // When using the BoM, you don't specify versions in Firebase library dependencies
  implementation("com.google.firebase:firebase-ai")

  // Required for one-shot operations (to use `ListenableFuture` from Guava Android)
  implementation("com.google.guava:guava:31.0.1-android")

  // Required for streaming operations (to use `Publisher` from Reactive Streams)
  implementation("org.reactivestreams:reactive-streams:1.0.4")
}
```

By using the [Firebase Android BoM](https://firebase.google.com/docs/android/learn-more#bom),
your app will always use compatible versions of Firebase Android libraries.


*(Alternative)*
Add Firebase library dependencies *without* using the BoM

<br />

If you choose not to use the Firebase BoM, you must specify each
Firebase library version in its dependency line.

**Note that if you use *multiple* Firebase libraries in your app, we
strongly recommend using the BoM to manage library versions, which
ensures that all versions are compatible.**

```groovy
dependencies {
  // Add the dependency for the Firebase AI Logic library
  // When NOT using the BoM, you must specify versions in Firebase library dependencies
  implementation("com.google.firebase:firebase-ai:17.10.0")
}
```

<br />

<br />

### Web

The Firebase AI Logic library provides access to the APIs for interacting
with Gemini and Imagen models. The library is included
as part of the Firebase JavaScript SDK for Web.

1. Install the Firebase JS SDK for Web using npm:

       npm install firebase

2. Initialize Firebase in your app:

       import { initializeApp } from "firebase/app";

       // TODO(developer) Replace the following with your app's Firebase configuration
       // See: https://firebase.google.com/docs/web/learn-more#config-object
       const firebaseConfig = {
         // ...
       };

       // Initialize FirebaseApp
       const firebaseApp = initializeApp(firebaseConfig);

### Dart

The Firebase AI Logic plugin for Flutter (`firebase_ai`) provides
access to the APIs for interacting with
Gemini and Imagen models.

1. From your Flutter project directory, run the following command to
   install the core plugin and the Firebase AI Logic plugin:

       flutter pub add firebase_core firebase_ai

2. In your `lib/main.dart` file, import the Firebase core plugin, the
   Firebase AI Logic plugin, and the configuration file you generated
   earlier:

       import 'package:firebase_core/firebase_core.dart';
       import 'package:firebase_ai/firebase_ai.dart';
       import 'firebase_options.dart';

3. Also in your `lib/main.dart` file, initialize Firebase using the
   `DefaultFirebaseOptions` object exported by the configuration file:

       await Firebase.initializeApp(
         options: DefaultFirebaseOptions.currentPlatform,
       );

4. Rebuild your Flutter application:

       flutter run

### Unity

1. Download the [Firebase Unity SDK](https://firebase.google.com/download/unity), then extract the SDK somewhere
   convenient.

   The Firebase Unity SDK is not platform-specific.
2. In your open Unity project, navigate to
   **Assets** \> **Import Package** \> **Custom Package**.

3. From the extracted SDK, select the `FirebaseAI` package.

4. In the *Import Unity Package* window, click **Import**.

5. Back in the Firebase console, in the setup workflow, click **Next**.

## **Step 3**: Initialize the service and create a model instance


|---|
| *Click your Gemini API provider to view provider-specific content and code on this page.* <button value="dev" default="">Gemini Developer API</button> <button value="vertex">Vertex AI Gemini API</button> |

<br />

Before sending a prompt to a Gemini model,
initialize the service for your chosen API provider and create a
`GenerativeModel` instance.

### Swift


    import FirebaseAILogic

    // Initialize the Gemini Developer API backend service
    let ai = FirebaseAI.firebaseAI(backend: .googleAI())

    // Create a `GenerativeModel` instance with a model that supports your use case
    let model = ai.generativeModel(modelName: "gemini-3-flash-preview")

### Kotlin


    // Initialize the Gemini Developer API backend service
    // Create a `GenerativeModel` instance with a model that supports your use case
    val model = Firebase.ai(backend = GenerativeBackend.googleAI())
                            .generativeModel("gemini-3-flash-preview")

### Java


    // Initialize the Gemini Developer API backend service
    // Create a `GenerativeModel` instance with a model that supports your use case
    GenerativeModel ai = FirebaseAI.getInstance(GenerativeBackend.googleAI())
            .generativeModel("gemini-3-flash-preview");

    // Use the GenerativeModelFutures Java compatibility layer which offers
    // support for ListenableFuture and Publisher APIs
    GenerativeModelFutures model = GenerativeModelFutures.from(ai);

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
    const model = getGenerativeModel(ai, { model: "gemini-3-flash-preview" });

### Dart


    import 'package:firebase_ai/firebase_ai.dart';
    import 'package:firebase_core/firebase_core.dart';
    import 'firebase_options.dart';

    // Initialize FirebaseApp
    await Firebase.initializeApp(
      options: DefaultFirebaseOptions.currentPlatform,
    );

    // Initialize the Gemini Developer API backend service
    // Create a \`GenerativeModel\` instance with a model that supports your use case
    final model =
    FirebaseAI.googleAI().generativeModel(model: 'gemini-3-flash-preview');

### Unity


    using Firebase;
    using Firebase.AI;

    // Initialize the Gemini Developer API backend service
    var ai = FirebaseAI.GetInstance(FirebaseAI.Backend.GoogleAI());

    // Create a `GenerativeModel` instance with a model that supports your use case
    var model = ai.GetGenerativeModel(modelName: "gemini-3-flash-preview");

Note that **depending on the capability you're using, you might not always
create a `GenerativeModel` instance**.

- To [access an Imagen model](https://firebase.google.com/docs/ai-logic/generate-images-imagen), create an `ImagenModel` instance.
- To [stream input and output using the Gemini Live API](https://firebase.google.com/docs/ai-logic/live-api), create a `LiveModel` instance.

Also, after you finish this getting started guide, learn how to choose a
[model](https://firebase.google.com/docs/ai-logic/models) for your use case and app.

> [!IMPORTANT]
> **Important:** Before going to production, we strongly recommend implementing Firebase Remote Config so that you can [remotely change the model name used in your app](https://firebase.google.com/docs/ai-logic/change-model-name-remotely).

## **Step 4**: Send a prompt request to a model

You're now set up to send a prompt request to a Gemini model.

You can use `generateContent()` to generate text from a prompt that contains
text:

### Swift


    import FirebaseAILogic

    // Initialize the Gemini Developer API backend service
    let ai = FirebaseAI.firebaseAI(backend: .googleAI())

    // Create a `GenerativeModel` instance with a model that supports your use case
    let model = ai.generativeModel(modelName: "gemini-3-flash-preview")

    // Provide a prompt that contains text
    let prompt = "Write a story about a magic backpack."
    // To generate text output, call generateContent with the text input
    let response = try await model.generateContent(prompt)
    print(response.text ?? "No text in response.")

### Kotlin

^*For Kotlin, the methods in this SDK are suspend functions and need to be called
from a [Coroutine scope](https://developer.android.com/kotlin/coroutines).*^


    // Initialize the Gemini Developer API backend service
    // Create a `GenerativeModel` instance with a model that supports your use case
    val model = Firebase.ai(backend = GenerativeBackend.googleAI())
                            .generativeModel("gemini-3-flash-preview")

    // Provide a prompt that contains text
    val prompt = "Write a story about a magic backpack."
    // To generate text output, call generateContent with the text input
    val response = model.generateContent(prompt)
    print(response.text)

### Java

^*For Java, the methods in this SDK return a
[`ListenableFuture`](https://developer.android.com/guide/background/asynchronous/listenablefuture).*^


    // Initialize the Gemini Developer API backend service
    // Create a `GenerativeModel` instance with a model that supports your use case
    GenerativeModel ai = FirebaseAI.getInstance(GenerativeBackend.googleAI())
            .generativeModel("gemini-3-flash-preview");

    // Use the GenerativeModelFutures Java compatibility layer which offers
    // support for ListenableFuture and Publisher APIs
    GenerativeModelFutures model = GenerativeModelFutures.from(ai);

    // Provide a prompt that contains text
    Content prompt = new Content.Builder()
    .addText("Write a story about a magic backpack.")
    .build();
    // To generate text output, call generateContent with the text input
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
    const model = getGenerativeModel(ai, { model: "gemini-3-flash-preview" });

    // Wrap in an async function so you can use await
    async function run() {
    // Provide a prompt that contains text
    const prompt = "Write a story about a magic backpack."
    // To generate text output, call generateContent with the text input
    const result = await model.generateContent(prompt);
    const response = result.response;
    const text = response.text();
    console.log(text);
    }
    run();

### Dart


    import 'package:firebase_ai/firebase_ai.dart';
    import 'package:firebase_core/firebase_core.dart';
    import 'firebase_options.dart';

    // Initialize FirebaseApp
    await Firebase.initializeApp(
      options: DefaultFirebaseOptions.currentPlatform,
    );

    // Initialize the Gemini Developer API backend service
    // Create a \`GenerativeModel\` instance with a model that supports your use case
    final model =
    FirebaseAI.googleAI().generativeModel(model: 'gemini-3-flash-preview');

    // Provide a prompt that contains text
    final prompt = \[Content.text('Write a story about a magic backpack.')\];
    // To generate text output, call generateContent with the text input
    final response = await model.generateContent(prompt);
    print(response.text);

### Unity


    using Firebase;
    using Firebase.AI;

    // Initialize the Gemini Developer API backend service
    var ai = FirebaseAI.GetInstance(FirebaseAI.Backend.GoogleAI());

    // Create a `GenerativeModel` instance with a model that supports your use case
    var model = ai.GetGenerativeModel(modelName: "gemini-3-flash-preview");

    // Provide a prompt that contains text
    var prompt = "Write a story about a magic backpack.";
    // To generate text output, call GenerateContentAsync with the text input
    var response = await model.GenerateContentAsync(prompt);
    UnityEngine.Debug.Log(response.Text ?? "No text in response.");

> [!NOTE]
> The Gemini API can also **stream responses** for faster interactions, as well as handle **multimodal prompts** that include content like images, video, audio, and PDFs. Later on this page, find links to guides for [various capabilities](https://firebase.google.com/docs/ai-logic/get-started#try-capabilities-of-gemini-api) of the Gemini API.

## What else can you do?


#### Learn more about the supported models

Learn about the [models available for various use cases](https://firebase.google.com/docs/ai-logic/models) and their [quotas](https://firebase.google.com/docs/ai-logic/quotas) and [pricing](https://firebase.google.com/docs/ai-logic/pricing).

<br />


#### Try out other capabilities

<br />

- Learn more about generating text from [text-only prompts](https://firebase.google.com/docs/ai-logic/generate-text), including how to stream the response.
- Generate text by prompting with various file types, like [images](https://firebase.google.com/docs/ai-logic/analyze-images), [PDFs](https://firebase.google.com/docs/ai-logic/analyze-documents), [video](https://firebase.google.com/docs/ai-logic/analyze-video), and [audio](https://firebase.google.com/docs/ai-logic/analyze-audio).
- Build [multi-turn conversations (chat)](https://firebase.google.com/docs/ai-logic/chat).
- Generate [structured output (like JSON)](https://firebase.google.com/docs/ai-logic/generate-structured-output) from both text and multimodal prompts.
- Generate images from text prompts ([Gemini](https://firebase.google.com/docs/ai-logic/generate-images-gemini) or [Imagen](https://firebase.google.com/docs/ai-logic/generate-images-imagen)).
- [Stream input and output](https://firebase.google.com/docs/ai-logic/live-api) (including audio) using the Gemini Live API.
- Use tools (like [function calling](https://firebase.google.com/docs/ai-logic/function-calling) and [grounding with Google Search](https://firebase.google.com/docs/ai-logic/grounding-google-search)) to connect a Gemini model to other parts of your app and external systems and information.


#### Learn how to control content generation

- [Understand prompt design](https://firebase.google.com/docs/ai-logic/prompt-design), including best practices, strategies, and example prompts.
- [Configure model parameters](https://firebase.google.com/docs/ai-logic/model-parameters) like temperature and maximum output tokens (for Gemini) or aspect ratio and person generation (for Imagen).
- [Use safety settings](https://firebase.google.com/docs/ai-logic/safety-settings) to adjust the likelihood of getting responses that may be considered harmful.

You can also experiment with prompts and model configurations and even get a generated code snippet using [Google AI Studio](https://aistudio.google.com).

<br />

<br />

[Give feedback
about your experience with Firebase AI Logic](https://firebase.google.com/docs/ai-logic/feedback)

<br />