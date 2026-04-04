# Source: https://firebase.google.com/docs/ai-logic/hybrid/android/get-started.md.txt

> [!WARNING]
> **Experimental:** Using the Firebase AI Logic SDK to build hybrid experiences is an Experimental feature (and ML Kit's Prompt API is in beta), which means that this feature isn't subject to any SLA or deprecation policy and could change in backwards-incompatible ways.

<br />

You can build AI-powered Android apps and features with hybrid inference using
Firebase AI Logic. Hybrid inference enables running inference using
on-device models when available and seamlessly falling back to
cloud-hosted models otherwise (and vice versa).

This page describes how to
[get started using the client SDK](https://firebase.google.com/docs/ai-logic/hybrid/android/get-started#get-started),
as well as showing
[additional configuration options and capabilities](https://firebase.google.com/docs/ai-logic/hybrid/android/configuration-options),
like temperature.

Note that on-device inference via Firebase AI Logic is supported for Android
apps running on
[specific devices](https://developers.google.com/ml-kit/genai#prompt-device)
and is governed by the
[ML Kit terms](https://developers.google.com/ml-kit/terms),
as well as
[terms specific to the Gen AI aspects of ML Kit](https://developers.google.com/ml-kit/genai-terms).

## Recommended use cases and supported capabilities

#### Recommended use cases

- Using an **on-device model for inference** offers:

  - Enhanced privacy
  - Local context
  - Inference at no-cost
  - Offline functionality
- Using **hybrid** functionality offers:

  - Reach more of your audience by accommodating on-device model availability and internet connectivity

#### Supported capabilities and features for on-device inference

On-device inference only supports **single-turn text generation (*not* chat)**,
with streaming or non-streaming output. It supports the following
text-generation capabilities:

- Generating [text from text-only input](https://firebase.google.com/docs/ai-logic/hybrid/android/get-started#text-in-text-out)

- Generating [text from text-and-image input](https://firebase.google.com/docs/ai-logic/hybrid/android/get-started#image-in-text-out), specifically
  a single Bitmap image as input

Make sure to review the list of
[not-yet-available features for on-device inference](https://firebase.google.com/docs/ai-logic/hybrid/android/get-started#features-not-yet-available)
at the bottom of this page.

## Before you begin

Take note of the following:

- Supported APIs:

  - In-cloud inference uses your chosen Gemini API provider (either the
    Gemini Developer API or the Vertex AI Gemini API).

  - On-device inference uses the
    [Prompt API from ML Kit](https://developers.google.com/ml-kit/genai/prompt/android),
    which is in beta and only available on
    [specific devices](https://developers.google.com/ml-kit/genai#prompt-device).

    On-device models usage is governed by the [ML Kit terms](https://developers.google.com/ml-kit/terms), as well as [terms
    specific to the Gen AI aspects of ML Kit](https://developers.google.com/ml-kit/genai-terms).
- This page describes how to **get started**.

  After completing this standard setup, check out the
  [additional configuration options and capabilities](https://firebase.google.com/docs/ai-logic/hybrid/android/configuration-options)
  (like setting temperature).

### Supported Android devices and their on-device models

For on-device inference (which uses ML Kit's Prompt API), you can find a list of
[supported devices and their on-device models](https://developers.google.com/ml-kit/genai#prompt-device)
in the ML Kit documentation.

## Get started

These get started steps describe the required general setup for any supported
prompt request that you want to send.

### **Step 1**: Set up a Firebase project and connect your app to Firebase

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

### **Step 2**: Add the required SDKs

The Firebase AI Logic SDK for Android
(`firebase-ai`) along with the
Firebase AI Logic On-Device SDK
(`firebase-ai-ondevice`)
provide access to the APIs for interacting with generative models.

> [!IMPORTANT]
> **Important:** The `firebase-ai-ondevice` library transitively includes ML Kit's Prompt API and requires that your Android project target *at minimum* API level 26 (whereas the `firebase-ai` library only requires *at minimum* level 23).

In your **module (app-level) Gradle file**
(like `<project>/<app-module>/build.gradle.kts`), add the dependencies for the
Firebase AI Logic libraries for Android:

### Kotlin

```groovy
dependencies {
  // ... other androidx dependencies

  // Add the dependencies for the Firebase AI Logic libraries
  // Note that the on-device SDK is not yet included in the Firebase Android BoM
  implementation("com.google.firebase:firebase-ai:17.10.0")
  implementation("com.google.firebase:firebase-ai-ondevice:16.0.0-beta01")
}
```

### Java

For Java, you need to add two additional libraries.

```groovy
dependencies {
  // ... other androidx dependencies

  // Add the dependencies for the Firebase AI Logic libraries
  // Note that the on-device SDK is not yet included in the Firebase Android BoM
  implementation("com.google.firebase:firebase-ai:17.10.0")
  implementation("com.google.firebase:firebase-ai-ondevice:16.0.0-beta01")

  // Required for one-shot operations (to use `ListenableFuture` from Guava Android)
  implementation("com.google.guava:guava:31.0.1-android")

  // Required for streaming operations (to use `Publisher` from Reactive Streams)
  implementation("org.reactivestreams:reactive-streams:1.0.4")
}
```

### **Step 3**: Check if the on-device model is available

Using
[`FirebaseAIOnDevice`](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/ondevice/FirebaseAIOnDevice),
check if the on-device model is available, and download the model if it's not
available.

Once downloaded, AICore will automatically keep the model updated. Check out the
notes after the snippet for more details about AICore and managing the
on-device model download.

### Kotlin

    val status = FirebaseAIOnDevice.checkStatus()
    when (status) {
      OnDeviceModelStatus.UNAVAILABLE -> {
        Log.w(TAG, "On-device model is unavailable")
      }

      OnDeviceModelStatus.DOWNLOADABLE -> {
        FirebaseAIOnDevice.download().collect { status ->
          when (status) {
            is DownloadStatus.DownloadStarted ->
              Log.w(TAG, "Starting download - ${status.bytesToDownload}")

            is DownloadStatus.DownloadInProgress ->
              Log.w(TAG, "Download in progress ${status.totalBytesDownloaded} bytes downloaded")

            is DownloadStatus.DownloadCompleted ->
              Log.w(TAG, "On-device model download complete")

            is DownloadStatus.DownloadFailed ->
              Log.e(TAG, "Download failed ${status}")
          }
        }
      }
      OnDeviceModelStatus.DOWNLOADING -> {
        Log.w(TAG, "On-device model is being downloaded")
      }

      OnDeviceModelStatus.AVAILABLE -> {
        Log.w(TAG, "On-device model is available")
      }
    }

### Java

    Checking for and downloading the model is not yet available for Java.

    However, all other APIs and interactions in this guide are available for Java.

Note the following about downloading the on-device model:

- The time it takes to download the on-device model depends on many factors,
  including your network.

- If your code uses an on-device model for its primary or fallback inference,
  make sure the model is downloaded early in your app's lifecycle so that the
  on-device model is available before your end-users encounter the code in your
  app.

- If the on-device model is *not available* when an on-device inference request
  is made, the SDK will *not automatically* trigger the download of the
  on-device model. The SDK will either fall back to the cloud-hosted model or
  throw an exception (see details about the behavior of
  [inference modes](https://firebase.google.com/docs/ai-logic/hybrid/android/configuration-options#inference-modes)).

- [AICore](https://android-developers.googleblog.com/2023/12/a-new-foundation-for-ai-on-android.html)
  (an Android system service) manages for you which model and version is
  downloaded, keeping the model updated, etc. Note that the device will only
  have one model downloaded, so if another app on the device has previously
  successfully downloaded the on-device model, then this check will return
  that the model is available.

#### Latency optimization

To optimize for the first inference call, you can have your app call
[`warmup()`](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/GenerativeModel#warmUp()).
This loads the on-device model into memory and initializes runtime components.

### **Step 4**: Initialize the service and create a model instance

|---|
| *Click your Gemini API provider to view provider-specific content and code on this page.* <button value="dev" default="">Gemini Developer API</button> <button value="vertex">Vertex AI Gemini API</button> |

Set up the following before you send a prompt request to the model.

1. Initialize the service for your chosen API provider.

2. Create a `GenerativeModel` instance, and set the `mode` to one of the
   following. The descriptions here are very high-level, but you can learn
   details about the behavior of these modes in
   [Set an inference mode](https://firebase.google.com/docs/ai-logic/hybrid/android/configuration-options#inference-modes).

   - **`PREFER_ON_DEVICE`** : Attempt to use on-device model;
     otherwise, *fall back to the cloud-hosted model*.

   - **`ONLY_ON_DEVICE`** : Attempt to use on-device model;
     otherwise, *throw an exception*.

   - **`PREFER_IN_CLOUD`** : Attempt to use the cloud-hosted model;
     otherwise, *fall back to the on-device model*.

   - **`ONLY_IN_CLOUD`** : Attempt to use the cloud-hosted model;
     otherwise, *throw an exception*.

   > [!NOTE]
   > **Note** : Keep the following in mind:
   > - To use an on-device model, make sure to review the list of [not-yet-available
   >   features](https://firebase.google.com/docs/ai-logic/hybrid/android/get-started#features-not-yet-available) at the bottom of this page.
   > - To use a cloud-hosted model, the device must be online and you must explicitly [specify
   >   a cloud-hosted model to use](https://firebase.google.com/docs/ai-logic/hybrid/android/configuration-options#specify-cloud-model).
   > - As part of the response, the SDK tells you [whether
   >   on-device or in-cloud inference was used](https://firebase.google.com/docs/ai-logic/hybrid/android/configuration-options#determine-inference-mode).

### Kotlin

    // Using this SDK to access on-device inference is an Experimental release and requires opt-in
    @OptIn(PublicPreviewAPI::class)

    // ...

    // Initialize the Gemini Developer API backend service
    // Create a GenerativeModel instance with a model that supports your use case
    // Set the inference mode (like PREFER_ON_DEVICE to use the on-device model if available)
    val model = Firebase.ai(backend = GenerativeBackend.googleAI())
        .generativeModel(
            modelName = "MODEL_NAME",
            onDeviceConfig = OnDeviceConfig(mode = InferenceMode.PREFER_ON_DEVICE)
        )

### Java

    // Initialize the Gemini Developer API backend service
    // Create a GenerativeModel instance with a model that supports your use case
    // Set the inference mode (like PREFER_ON_DEVICE to use the on-device model if available)
    GenerativeModel ai = FirebaseAI.getInstance(GenerativeBackend.googleAI())
        .generativeModel(
            "MODEL_NAME",
            new OnDeviceConfig(InferenceMode.PREFER_ON_DEVICE)
        );

    // Use the GenerativeModelFutures Java compatibility layer which offers
    // support for ListenableFuture and Publisher APIs
    GenerativeModelFutures model = GenerativeModelFutures.from(ai);

### **Step 5**: Send a prompt request to a model

This section shows you how to send various types of input to generate different
types of output, including:

- [Generate text from text-only input](https://firebase.google.com/docs/ai-logic/hybrid/android/get-started#text-in-text-out)

- [Generate text from text-and-image (multimodal) input](https://firebase.google.com/docs/ai-logic/hybrid/android/get-started#image-in-text-out)

> [!IMPORTANT]
> **Important:** Make sure to review the [list of ***not-yet-supported features and limitations for on-device inference***](https://firebase.google.com/docs/ai-logic/hybrid/android/get-started#features-not-yet-available). For many of these, the SDK will automatically fall back to the cloud-hosted model (if you allow that capability by your specified inference mode).

#### Generate text from text-only input

|---|
| *Before trying this sample, make sure that you've completed the [Get started](https://firebase.google.com/docs/ai-logic/hybrid/android/get-started#get-started) section of this guide.* |

You can use
[`generateContent()`](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/GenerativeModel#generateContent(kotlin.String))
to generate text from a prompt that contains text:

### Kotlin

    // Imports + initialization of Gemini API backend service + creation of model instance

    // Provide a prompt that contains text
    val prompt = "Write a story about a magic backpack."

    // To generate text output, call generateContent with the text input
    val response = model.generateContent(prompt)
    print(response.text)

### Java

    // Imports + initialization of Gemini API backend service + creation of model instance

    // Provide a prompt that contains text
    Content prompt = new Content.Builder()
        .addText("Write a story about a magic backpack.")
        .build();

    // To generate text output, call generateContent with the text input
    ListenableFuture<GenerateContentResponse> response = model.generateContent(prompt);
    Futures.addCallback(response, new FutureCallback<GenerateContentResponse>() {
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

Note that Firebase AI Logic also supports streaming of text responses using
[`generateContentStream`](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/GenerativeModel#generateContentStream(kotlin.String))
(instead of `generateContent`).

#### Generate text from text-and-image (multimodal) input

|---|
| *Before trying this sample, make sure that you've completed the [Get started](https://firebase.google.com/docs/ai-logic/hybrid/android/get-started#get-started) section of this guide.* |

You can use
[`generateContent()`](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/GenerativeModel#generateContent(kotlin.String))
to generate text from a prompt that contains text and *up to **one** image file
(Bitmap only)* --- providing each input file's `mimeType` and the file itself.

### Kotlin

    // Imports + initialization of Gemini API backend service + creation of model instance

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

### Java

    // Imports + initialization of Gemini API backend service + creation of model instance

    Bitmap bitmap = BitmapFactory.decodeResource(getResources(), R.drawable.sparky);

    // Provide a prompt that includes the image specified above and text
    Content content = new Content.Builder()
            .addImage(bitmap)
            .addText("What developer tool is this mascot from?")
            .build();

    // To generate text output, call generateContent with the prompt
    ListenableFuture<GenerateContentResponse> response = model.generateContent(content);
    Futures.addCallback(response, new FutureCallback<GenerateContentResponse>() {
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

Note that Firebase AI Logic also supports streaming of text responses using
[`generateContentStream`](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/GenerativeModel#generateContentStream(kotlin.Array))
(instead of `generateContent`).

## What else can you do?

You can use various additional configuration options and capabilities for your
hybrid experiences:

- [Set an inference mode.](https://firebase.google.com/docs/ai-logic/hybrid/android/configuration-options#inference-modes)

- [Determine whether on-device or in-cloud inference was used.](https://firebase.google.com/docs/ai-logic/hybrid/android/configuration-options#determine-inference-mode)

- [Specify a cloud-hosted model to use.](https://firebase.google.com/docs/ai-logic/hybrid/android/configuration-options#specify-cloud-model)

- [Use model configuration to control responses (like temperature).](https://firebase.google.com/docs/ai-logic/hybrid/android/configuration-options#model-config)

## Features not yet available for on-device inference

As an experimental release, not all the capabilities of cloud models are
available for *on-device* inference.

**The features listed in this section are *not yet available for on-device
inference.*** If you want to use any of these features, then we recommend using
the `ONLY_IN_CLOUD` inference mode for a more consistent experience.

- Generating structured output (like JSON or enums)

- Generating text from image file input types other than Bitmap
  (image loaded into memory)

- Generating text from more than one image file

- Generating text from audio, video, and documents (like PDFs) inputs

- Generating images using Gemini or Imagen models

- Providing files using URLs in multimodal requests. You must provide files as
  inline data to on-device models

- Sending requests that exceed 4000 tokens
  (or approximately 3000 English words).

- Multi-turn chat

- Providing the model with *tools* to help it generate its response
  (like function calling, code execution, URL context, and grounding with
  Google Search)

AI monitoring in the Firebase console does ***not*** show any data for
on-device inference (including on-device logs). However, any inference that uses
a cloud-hosted model can be monitored just like other inference via
Firebase AI Logic.

> [!NOTE]
> **Note:** The following are ***not supported for hybrid implementations*** : Imagen models, the Gemini Live API, and prompt templates. Also, count tokens shouldn't be relied upon because the count will differ between cloud-hosted and on-device models, so there's no intuitive fall back.

### Additional limitations

In addition to the above, ***on-device* inference has the following
limitations** (learn more in the
[ML Kit documentation](https://developers.google.com/ml-kit/genai/prompt/android/get-started#supported-features)):

- The end-user of your app must be using a
  [supported device](https://developers.google.com/ml-kit/genai#prompt-device)
  for on-device inference.

- Your app can only run on-device inference when it's in the foreground.

- Only English and Korean have been validated for on-device inference.

- The maximum token limit for the entire on-device inference request is
  4000 tokens. If your requests might exceed this limit, then make sure to
  configure an inference mode that can use a cloud-hosted model.

- We recommend avoiding on-device inference use cases that require long
  output (more than 256 tokens).

- [AICore](https://android-developers.googleblog.com/2023/12/a-new-foundation-for-ai-on-android.html)
  (an Android system service that manages the on-device models) enforces an
  inference quota *per app* . Making too many API requests in a short period
  will result in an `ErrorCode.BUSY` response. If you're receiving this
  error, consider using exponential backoff to retry the request. Also,
  `ErrorCode.PER_APP_BATTERY_USE_QUOTA_EXCEEDED` can be returned if an app
  exceeds a long-duration quota (for example, daily quota).

<br />

[Give feedback
about your experience with Firebase AI Logic](https://firebase.google.com/docs/ai-logic/feedback)

<br />