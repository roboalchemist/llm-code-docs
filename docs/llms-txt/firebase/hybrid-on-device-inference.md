# Source: https://firebase.google.com/docs/ai-logic/hybrid-on-device-inference.md.txt

<br />

| **Preview** : Using theFirebase AI LogicSDKs to build hybrid experiences is a Preview feature, which means that it isn't subject to any SLA or deprecation policy and could change in backwards-incompatible ways.
|
| This initial release only**supports on-device inference for web apps running on Chrome on Desktop.**

<br />

Build AI-powered apps and features with hybrid inference usingFirebase AI Logic. Hybrid inference enables running inference using on-device models when available and seamlessly falling back to cloud-hosted models otherwise (and vice versa).

With this release, hybrid inference is available using theFirebase AI Logicclient SDK for Web with support for on-device inference for Chrome on Desktop.

[Jump to the code examples](https://firebase.google.com/docs/ai-logic/hybrid-on-device-inference#call-api)

## Recommended use cases and supported capabilities

**Recommended use cases:**

- Using an on-device model for inference offers:

  - Enhanced privacy
  - Local context
  - Inference at no-cost
  - Offline functionality
- Using hybrid functionality offers:

  - Reach 100% of your audience, regardless of on-device model availability or internet connectivity

**Supported capabilities and features for on-device inference:**

- Single-turn content generation, streaming and non-streaming
- Generating[text from text-only input](https://firebase.google.com/docs/ai-logic/hybrid-on-device-inference#text-in-text-out)
- Generating[text from text-and-image input](https://firebase.google.com/docs/ai-logic/hybrid-on-device-inference#image-in-text-out), specifically input image types of JPEG and PNG
- Generating[structured output](https://firebase.google.com/docs/ai-logic/hybrid-on-device-inference#model-config-structured-output), including JSON and enums

## Get started

This guide shows you how to get started using theFirebase AI LogicSDK for Web to perform hybrid inference.

Inference using an on-device model uses the[Prompt API from Chrome](https://developer.chrome.com/docs/extensions/ai/prompt-api); whereas inference using a cloud-hosted model uses your chosenGemini APIprovider (either theGemini Developer APIor theVertex AIGemini API).

Get started developing using localhost, as described in this section (you can also learn more about[using APIs on localhost](https://developer.chrome.com/docs/ai/get-started#use_apis_on_localhost)in the Chrome documentation). Then, once you've implemented your feature, you can optionally[enable end-users to try out your feature](https://firebase.google.com/docs/ai-logic/hybrid-on-device-inference#enable-end-users-to-try-feature).

### **Step 1**: Set up Chrome and the Prompt API for on-device inference

1. Make sure you're using a recent version of Chrome. Update in<chrome://settings/help>.  
   On-device inference is available from Chrome v139 and higher.

2. Enable the on-device multimodal model by setting the following flag to**Enabled**:

   - `chrome://flags/#prompt-api-for-gemini-nano-multimodal-input`
3. Restart Chrome.

4. *(Optional)*Download the on-device model before the first request.

   The Prompt API is built into Chrome; however, the on-device model isn't available by default. If you haven't yet downloaded the model before your first request for on-device inference, the request will automatically start the model download in the background.
   | **Note:** Downloading the model can take several minutes, so waiting to auto-download with the first request can significantly delay receiving a response to that request.

   <br />

   View instructions to download the on-device model

   <br />

   1. Open**Developer Tools \> Console**.

   2. Run the following:

          await LanguageModel.availability();

   3. Make sure that the output is`available`,`downloading`, or`downloadable`.

   4. If the output is`downloadable`, start the model download by running:

          await LanguageModel.create();

   5. You can use the following`monitor`callback to listen for download progress and make sure that the model is`available`before making requests:

          const session = await LanguageModel.create({
            monitor(m) {
              m.addEventListener("downloadprogress", (e) => {
                console.log(`Downloaded ${e.loaded * 100}%`);
              });
            },
          });

   <br />

   <br />

### **Step 2**: Set up a Firebase project and connect your app to Firebase

1. Sign into the[Firebaseconsole](https://console.firebase.google.com/), and then select your Firebase project.

   <br />

   Don't already have a Firebase project?

   <br />

   If you don't already have a Firebase project, click the button to create a new Firebase project, and then use either of the following options:
   - **Option 1** : Create a wholly new Firebase project (and its underlyingGoogle Cloudproject automatically) by entering a new project name in the first step of the workflow.

   - **Option 2** : "Add Firebase" to an existingGoogle Cloudproject by clicking**Add Firebase to Google Cloud project** (at bottom of page). In the first step of the workflow, start entering the**project name**of the existing project, and then select the project from the displayed list.

   Complete the remaining steps of the on-screen workflow to create a Firebase project. Note that when prompted, you do***not*** need to set upGoogle Analyticsto use theFirebase AI LogicSDKs.

   <br />

   <br />

2. In theFirebaseconsole, go to the[**Firebase AI Logic**page](https://console.firebase.google.com/project/_/ailogic).

3. Click**Get started** to launch a guided workflow that helps you set up the[required APIs](https://firebase.google.com/docs/ai-logic/faq-and-troubleshooting#required-apis)and resources for your project.

4. Select the "Gemini API" provider that you'd like to use with theFirebase AI LogicSDKs.Gemini Developer APIis recommended for first-time users. You can always add billing or set upVertex AIGemini APIlater, if you'd like.

   - **Gemini Developer API** ---[billing optional](https://firebase.google.com/docs/ai-logic/pricing?api=dev#api-provider-pricing-plans)(available on the no-cost Spark pricing plan, and you can upgrade later if desired)  
     The console will enable the required APIs and create aGeminiAPI key in your project.  
     *Do**not** add thisGeminiAPI key into your app's codebase.* [Learn more.](https://firebase.google.com/docs/ai-logic/faq-and-troubleshooting#add-gemini-api-key-to-codebase)

   - **Vertex AIGemini API** ---[billing required](https://firebase.google.com/docs/ai-logic/pricing?api=vertex#api-provider-pricing-plans)(requires the pay-as-you-go Blaze pricing plan)  
     The console will help you set up billing and enable the required APIs in your project.

5. If prompted in the console's workflow, follow the on-screen instructions to register your app and connect it to Firebase.

6. Continue to the next step in this guide to add the SDK to your app.

| **Note:** In theFirebaseconsole, you're strongly encouraged to[set upFirebase App Check](https://firebase.google.com/docs/ai-logic/app-check). If you're just trying out theGemini API, you don't need to set upApp Checkright away; however, we recommend setting it up as soon as you start seriously developing your app.

### **Step 3**: Add the SDK

The Firebase library provides access to the APIs for interacting with generative models. The library is included as part of the Firebase JavaScript SDK for Web.

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

### **Step 4**: Initialize the service and create a model instance

|----------------------------------------------------------------------------------------------------------------------------------|
| *Click yourGemini APIprovider to view provider-specific content and code on this page.* Gemini Developer APIVertex AI Gemini API |

Before sending a prompt to aGeminimodel, initialize the service for your chosen API provider and create a`GenerativeModel`instance.

Set the`mode`to one of:

- **`PREFER_ON_DEVICE`**: Configures the SDK to use the on-device model if it's available, or fall back to the cloud-hosted model.

- **`ONLY_ON_DEVICE`**: Configures the SDK to use the on-device model or throw an exception.

- **`PREFER_IN_CLOUD`**: Configures the SDK to use the cloud-hosted model if it's available, or fall back to the on-device model.

- **`ONLY_IN_CLOUD`**: Configures the SDK to never use the on-device model.

When you use`PREFER_ON_DEVICE`,`PREFER_IN_CLOUD`, or`ONLY_IN_CLOUD`the**default cloud-hosted model is`gemini-2.0-flash-lite`** , but you can[override the default](https://firebase.google.com/docs/ai-logic/hybrid-on-device-inference#override-default-cloud-model).  

    import { initializeApp } from "firebase/app";
    import { getAI, getGenerativeModel, GoogleAIBackend, InferenceMode } from "firebase/ai";

    // TODO(developer) Replace the following with your app's Firebase configuration
    // See: https://firebase.google.com/docs/web/learn-more#config-object
    const firebaseConfig = {
      // ...
    };

    // Initialize FirebaseApp
    const firebaseApp = initializeApp(firebaseConfig);

    // Initialize the Gemini Developer API backend service
    const ai = getAI(firebaseApp, { backend: new GoogleAIBackend() });
    // Create a \`GenerativeModel\` instance
    // Set the mode, for example to use on-device model when possible
    const model = getGenerativeModel(ai, { mode: InferenceMode.PREFER_ON_DEVICE });

| **Note:** **Downloading the on-device model can take several minutes.**   
| If you haven't yet[downloaded the model before your first request for on-device inference](https://firebase.google.com/docs/ai-logic/hybrid-on-device-inference#instructions-to-download-on-device-model), the request will automatically start the model download in the background (which can significantly delay receiving a response to that request).

## Send a prompt request to a model

This section provides examples for how to send various types of input to generate different types of output, including:

- [Generate text from text-only input](https://firebase.google.com/docs/ai-logic/hybrid-on-device-inference#text-in-text-out)
- [Generate text from text-and-image (multimodal) input](https://firebase.google.com/docs/ai-logic/hybrid-on-device-inference#image-in-text-out)

If you want to generate structured output (like JSON or enums), then use one of the following "generate text" examples and additionally[configure the model to respond according to a provided schema](https://firebase.google.com/docs/ai-logic/hybrid-on-device-inference#model-config-structured-output).

### Generate text from text-only input

|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *Before trying this sample, make sure that you've completed the[Get started](https://firebase.google.com/docs/ai-logic/hybrid-on-device-inference#get-started)section of this guide.* |

You can use[`generateContent()`](https://firebase.google.com/docs/reference/js/vertexai.generativemodel#generativemodelgeneratecontent)to generate text from a prompt that contains text:  

    // Imports + initialization of FirebaseApp and backend service + creation of model instance

    // Wrap in an async function so you can use await
    async function run() {
      // Provide a prompt that contains text
      const prompt = "Write a story about a magic backpack."

      // To generate text output, call `generateContent` with the text input
      const result = await model.generateContent(prompt);

      const response = result.response;
      const text = response.text();
      console.log(text);
    }

    run();

Note thatFirebase AI Logicalso supports streaming of text responses using`generateContentStream`(instead of`generateContent`).

### Generate text from text-and-image (multimodal) input

|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *Before trying this sample, make sure that you've completed the[Get started](https://firebase.google.com/docs/ai-logic/hybrid-on-device-inference#get-started)section of this guide.* |

You can use[`generateContent()`](https://firebase.google.com/docs/reference/js/vertexai.generativemodel#generativemodelgeneratecontent)to generate text from a prompt that contains text and image files---providing each input file's`mimeType`and the file itself.

The supported input image types for on-device inference are PNG and JPEG.
**Important:** For on-device inference, the maximum token limit is 6000 tokens.  

    // Imports + initialization of FirebaseApp and backend service + creation of model instance

    // Converts a File object to a Part object.
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

    async function run() {
      // Provide a text prompt to include with the image
      const prompt = "Write a poem about this picture:";

      const fileInputEl = document.querySelector("input[type=file]");
      const imagePart = await fileToGenerativePart(fileInputEl.files[0]);

      // To generate text output, call `generateContent` with the text and image
      const result = await model.generateContent([prompt, imagePart]);

      const response = result.response;
      const text = response.text();
      console.log(text);
    }

    run();

Note thatFirebase AI Logicalso supports streaming of text responses using`generateContentStream`(instead of`generateContent`).

## What else can you do?

In addition to the examples above, you can also[enable end-users to try out your feature](https://firebase.google.com/docs/ai-logic/hybrid-on-device-inference#enable-end-users-to-try-feature),[use alternative inference modes](https://firebase.google.com/docs/ai-logic/hybrid-on-device-inference#inference-modes),[override the default fallback model](https://firebase.google.com/docs/ai-logic/hybrid-on-device-inference#override-default-cloud-model), and[use model configuration to control responses](https://firebase.google.com/docs/ai-logic/hybrid-on-device-inference#model-config).

### Enable end-users to try out your feature

To enable end-users to try out your feature, you can[enroll in the Chrome Origin Trials](https://developer.chrome.com/docs/web-platform/origin-trials). Note that there's a limited duration and usage for these trials.

1. Register for the[Prompt API Chrome Origin Trial](https://developer.chrome.com/origintrials/#/view_trial/2533837740349325313). You'll be given a token.

2. Provide the token on every web page for which you want the trial feature to be enabled. Use one of the following options:

   - Provide the token as a meta tag in the`<head>`tag:`<meta http-equiv="origin-trial" content="`<var translate="no">TOKEN</var>`">`

   - Provide the token as an HTTP header:`Origin-Trial: `<var translate="no">TOKEN</var>

   - Provide the token[programmatically](https://developer.chrome.com/docs/web-platform/origin-trials#programmatic).

### Use alternative inference modes

The examples above used the`PREFER_ON_DEVICE`mode to configure the SDK to use an on-device model if it's available, or fall back to a cloud-hosted model. The SDK offers three alternative[inference modes](https://github.com/firebase/firebase-js-sdk/blob/firebase-ai-hybridinference/docs-devsite/ai.hybridparams.md#hybridparamsmode):`ONLY_ON_DEVICE`,`ONLY_IN_CLOUD`, and`PREFER_IN_CLOUD`.

- Use`ONLY_ON_DEVICE`mode so that the SDK can only use an on-device model. In this configuration, the API will throw an error if an on-device model is not available.

      const model = getGenerativeModel(ai, { mode: InferenceMode.ONLY_ON_DEVICE });

- Use`ONLY_IN_CLOUD`mode so that the SDK can only use a cloud-hosted model.

      const model = getGenerativeModel(ai, { mode: InferenceMode.ONLY_IN_CLOUD });

- Use`PREFER_IN_CLOUD`mode so that the SDK will attempt to use the cloud-hosted model, but will fall back to the on-device model if the cloud-hosted model is unavailable (for example, the device is offline).

      const model = getGenerativeModel(ai, { mode: InferenceMode.PREFER_IN_CLOUD });

| **Note:** **Downloading the on-device model can take several minutes.**   
| If you haven't yet[downloaded the model before your first request for on-device inference](https://firebase.google.com/docs/ai-logic/hybrid-on-device-inference#instructions-to-download-on-device-model), the request will automatically start the model download in the background (which can significantly delay receiving a response to that request).

#### Determine whether on-device or in-cloud inference was used

If you use`PREFER_ON_DEVICE`or`PREFER_IN_CLOUD`inference modes, then it might be helpful to know which mode was used for given requests. This information is provided by the`inferenceSource`property of each response (available starting with JS SDK v12.5.0).

When you access this property, the returned value will be either`ON_DEVICE`or`IN_CLOUD`.  

    // ...

    console.log('You used: ' + result.response.inferenceSource);

    console.log(result.response.text());

### Override the default fallback model

**The default cloud-hosted model is`gemini-2.0-flash-lite`.**

This model is the fallback cloud-hosted model when you use the`PREFER_ON_DEVICE`mode. It's also the default model when you use the`ONLY_IN_CLOUD`mode or the`PREFER_IN_CLOUD`mode.

You can use the[`inCloudParams`](https://github.com/firebase/firebase-js-sdk/blob/vaihi-exp-google-ai/docs-devsite/vertexai.hybridparams.md#hybridparamsincloudparams)configuration option to specify an alternative default cloud-hosted model.  

    const model = getGenerativeModel(ai, {
      mode: InferenceMode.<var translate="no"><span class="devsite-syntax-nx">INFERENCE_MODE</span></var>,
      inCloudParams: {
        model: "<var translate="no">GEMINI_MODEL_NAME</var>"
      }
    });

Find model names for all[supported Gemini models](https://firebase.google.com/docs/ai-logic/models).

### Use model configuration to control responses

In each request to a model, you can send along a model configuration to control how the model generates a response. Cloud-hosted models and on-device models offer different configuration options.

The configuration is maintained for the lifetime of the instance. If you want to use a different config, create a new`GenerativeModel`instance with that config.

#### Set the configuration for a cloud-hosted model

Use the[`inCloudParams`](https://github.com/firebase/firebase-js-sdk/blob/vaihi-exp-google-ai/docs-devsite/vertexai.hybridparams.md#hybridparamsincloudparams)option to configure a cloud-hostedGeminimodel. Learn about[available parameters](https://firebase.google.com/docs/ai-logic/model-parameters#parameters-descriptions-gemini).  

    const model = getGenerativeModel(ai, {
      mode: InferenceMode.<var translate="no"><span class="devsite-syntax-nx">INFERENCE_MODE</span></var>,
      inCloudParams: {
        model: "<var translate="no">GEMINI_MODEL_NAME</var>"
        temperature: 0.8,
        topK: 10
      }
    });

#### Set the configuration for an on-device model

Note that inference using an on-device model uses the[Prompt API from Chrome](https://developer.chrome.com/docs/extensions/ai/prompt-api).

Use the[`onDeviceParams`](https://github.com/firebase/firebase-js-sdk/blob/vaihi-exp-google-ai/docs-devsite/vertexai.hybridparams.md#hybridparams-interface)option to configure an on-device model. Learn about[available parameters](https://github.com/webmachinelearning/prompt-api?tab=readme-ov-file#configuration-of-per-session-parameters).  

    const model = getGenerativeModel(ai, {
      mode: InferenceMode.<var translate="no"><span class="devsite-syntax-nx">INFERENCE_MODE</span></var>,
      onDeviceParams: {
        createOptions: {
          temperature: 0.8,
          topK: 8
        }
      }
    });

#### Set the configuration for structured output (like JSON)

Generating structured output (like JSON and enums) is supported for inference using both cloud-hosted and on-device models.

For hybrid inference, use both[`inCloudParams`](https://github.com/firebase/firebase-js-sdk/blob/vaihi-exp-google-ai/docs-devsite/vertexai.hybridparams.md#hybridparamsincloudparams)and[`onDeviceParams`](https://github.com/firebase/firebase-js-sdk/blob/vaihi-exp-google-ai/docs-devsite/vertexai.hybridparams.md#hybridparams-interface)to configure the model to respond with structured output. For the other modes, use only the applicable configuration.

- **For`inCloudParams`** : Specify the appropriate`responseMimeType`(in this example,`application/json`) as well as the`responseSchema`that you want the model to use.

- **For`onDeviceParams`** : Specify the`responseConstraint`that you want the model to use.

##### JSON output

The following example adapts the[general JSON output example](https://firebase.google.com/docs/ai-logic/generate-structured-output#generate-json-basic)for hybrid inference:  

    import {
      getAI,
      getGenerativeModel,
      Schema
    } from "firebase/ai";

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

    const model = getGenerativeModel(ai, {
      mode: InferenceMode.<var translate="no"><span class="devsite-syntax-nx">INFERENCE_MODE</span></var>,
      inCloudParams: {
        model: "gemini-2.5-flash"
        generationConfig: {
          responseMimeType: "application/json",
          responseSchema: jsonSchema
        },
      }
      onDeviceParams: {
        promptOptions: {
          responseConstraint: jsonSchema
        }
      }
    });

##### Enum output

As above, but adapting the[documentation on enum output](https://firebase.google.com/docs/ai-logic/generate-structured-output#generate-enum-basic)for hybrid inference:  

    // ...

    const enumSchema = Schema.enumString({
      enum: ["drama", "comedy", "documentary"],
    });

    const model = getGenerativeModel(ai, {

    // ...

        generationConfig: {
          responseMimeType: "text/x.enum",
          responseSchema: enumSchema
        },

    // ...
    });

    // ...

## Features not yet available for on-device inference

As an experimental release, not all the capabilities of the Web SDK are available for*on-device* inference.**The following features are*not yet supported for on-device inference*(but they are usually available for cloud-based inference).**
| **Note:** For many of these features, if you set the mode to`PREFER_ON_DEVICE`, the SDK will just automatically fall back to use the cloud-hosted model for these not-yet-available capabilities.

- Generating text from image file input types other than JPEG and PNG

  - Can fallback to the cloud-hosted model; however,`ONLY_ON_DEVICE`mode will throw an error.
- Generating text from audio, video, and documents (like PDFs) inputs

  - Can fallback to the cloud-hosted model; however,`ONLY_ON_DEVICE`mode will throw an error.
- Generating images usingGeminiorImagenmodels

  - Can fallback to the cloud-hosted model; however,`ONLY_ON_DEVICE`mode will throw an error.
- Providing files using URLs in multimodal requests. You must provide files as inline data to on-device models.

- Multi-turn chat

  - Can fallback to the cloud-hosted model; however,`ONLY_ON_DEVICE`mode will throw an error.
- Bi-directional streaming with theGemini Live API

- Providing the model with*tools*to help it generate its response (like function calling, code execution, and grounding with Google Search)

- Count tokens

  - Always throws an error. The count will differ between cloud-hosted and on-device models, so there is no intuitive fallback.
- AI monitoring in theFirebaseconsole for on-device inference.

  - Note that any inference using the cloud-hosted models can be monitored just like other inference using theFirebase AI Logicclient SDK for Web.

<br />

[Give feedback about your experience withFirebase AI Logic](https://firebase.google.com/docs/ai-logic/feedback)

<br />