# Source: https://firebase.google.com/docs/ai-logic/migrate-from-preview.md.txt

<br />

| **This guide helps you migrate from the Preview (or beta) versions of the "Vertex AI in Firebase" SDKs to theFirebase AI Logicclient SDKs** .  
| These client SDKs are available in Swift for Apple platforms, Kotlin and Java for Android, JavaScript for Web, Dart for Flutter, and Unity.
|
| If you're using a GA version of a "Vertex AI in Firebase" SDK, then go to the guide for[migrating from the GA version of the SDK](https://firebase.google.com/docs/ai-logic/migrate-to-latest-sdk).

<br />

Firebase AI Logicand its client SDKs were formerly called "Vertex AI in Firebase". To better reflect our expanded services and features (for example, we now support theGemini Developer API!),**we renamed and repackaged our services intoFirebase AI Logic**.

To securely access Google's generative AI models directly from your mobile or web apps,**you can now choose a "Gemini API" provider --- either the long-availableVertex AIGemini APIor now theGemini Developer API** . This means that you now have the option to use theGemini Developer API, which provides a**no-cost tier**with reasonable rate limits and quotas.

#### Overview of steps to migrate to theFirebase AI LogicSDKs

- **Step 1**: Choose the best "Gemini API" provider for your app and use cases.

- **Step 2**: Enable the required APIs.

- **Step 3**: Update the library used in your app.

- **Step 4**: Update the initialization in your app.

- **Step 5**: Update your code depending on the features that you use.

## **Step 1**: Choose the best "Gemini API" provider for your app

With this migration, you have a choice in "Gemini API" provider:

- The old "Vertex AI in Firebase" SDKs could only use theVertex AIGemini API.

- The newFirebase AI LogicSDKs let you choose which "Gemini API" provider you want to call directly from your mobile or web app -- either theGemini Developer APIor theVertex AIGemini API.

Review the[differences between using the twoGemini APIproviders](https://firebase.google.com/docs/ai-logic/faq-and-troubleshooting#differences-between-gemini-api-providers), especially in terms of supported features, pricing, and rate limits. For just one example, theGemini Developer APIdoesn't support providing files usingCloud StorageURLs, but it might be a good choice if you want to take advantage of its no-cost tier and reasonable quota.
| **Important** : If you want to use the "free tier" for theGemini Developer API, you need to[downgrade](https://console.firebase.google.com/project/_/overview?purchaseBillingPlan=free)the Firebase project that you currently use with the client SDKs to the no-cost Spark pricing plan (that is, unlink theCloud Billingaccount). Before downgrading, make sure that you're not depending on any other services or quotas that require the Blaze pricing plan.
|
| If your Firebase project stays on the Blaze pricing plan, then you'll be on one of the["paid tiers" for theGemini Developer API](https://ai.google.dev/gemini-api/docs/pricing).

## **Step 2**: Enable the required APIs

Ensure that all required APIs are enabled in your Firebase project to use your chosen "Gemini API" provider.

Note that you can have both of API providers enabled in your project at the same time.

1. Sign into the[Firebaseconsole](https://console.firebase.google.com/), and then select your Firebase project.

2. In theFirebaseconsole, go to the[**Firebase AI Logic**page](https://console.firebase.google.com/project/_/ailogic).

3. Click**Get started** to launch a guided workflow that helps you set up the[required APIs](https://firebase.google.com/docs/ai-logic/faq-and-troubleshooting#required-apis)and resources for your project.

4. Select the "Gemini API" provider that you'd like to use with theFirebase AI LogicSDKs. You can always set up and use the other API provider later, if you'd like.

   - **Gemini Developer API** ---[billing optional](https://firebase.google.com/docs/ai-logic/pricing?api=dev#api-provider-pricing-plans)(available on the no-cost Spark pricing plan)  
     The console's workflow will enable the required APIs and create aGeminiAPI key in your project.  
     *Do**not** add thisGeminiAPI key into your app's codebase.* [Learn more.](https://firebase.google.com/docs/ai-logic/faq-and-troubleshooting#add-gemini-api-key-to-codebase)

   - **Vertex AIGemini API** ---[billing required](https://firebase.google.com/docs/ai-logic/pricing?api=vertex#api-provider-pricing-plans)(requires the pay-as-you-go Blaze pricing plan)  
     The console's workflow will enable the required APIs in your project.

5. Continue in this migration guide to update the library and initialization in your app.

## **Step 3**: Update the library used in your app

Update your app's codebase to use theFirebase AI Logiclibrary.  

### Swift

1. In Xcode, with your app project open, update your Firebase package to v11.13.0 or later using one of the following options:

   - **Option 1** : Update all packages: Navigate to**File \> Packages \> Update to Latest Package Versions**.

   - **Option 2** : Update Firebase individually: Navigate to the Firebase package in the section called**Package Dependencies** . Right-click on the Firebase package, and then select**Update Package**.

2. Make sure that the Firebase package now shows v11.13.0 or later. If it doesn't, verify that your specified[Package Requirements](https://developer.apple.com/documentation/xcode/adding-package-dependencies-to-your-app#Decide-on-package-requirements)allow updating to v11.13.0 or later.

3. Select your app's target in the Project Editor, and then navigate to the**Frameworks, Libraries, and Embedded Content**section.

4. Add the new library: Select the**+** button, and then add**FirebaseAI**from the Firebase package.

5. After you've finished migrating your app (see the remaining sections in this guide), make sure to remove the old library:  
   Select**FirebaseVertexAI-Preview** , and then press the**---**button.

### Kotlin

1. In your**module (app-level) Gradle file** (usually`<project>/<app-module>/build.gradle.kts`or`<project>/<app-module>/build.gradle`), replace old dependencies (as applicable) with the following.

   Note that it might be easier to migrate your app's codebase (see the remaining sections in this guide) before deleting the old dependency.  

   ```kotlin
   // BEFORE
   dependencies {
     implementation("com.google.firebase:firebase-vertexai:16.0.0-betaXX")
   }


   // AFTER
   dependencies {
     // Import the BoM for the Firebase platform
     implementation(platform("com.google.firebase:firebase-bom:34.7.0"))

     // Add the dependency for the Firebase AI Logic library
     // When using the BoM, you don't specify versions in Firebase library dependencies
     implementation("com.google.firebase:firebase-ai")
   }
   ```
2. Sync your Android project with Gradle files.

Note that if you choose to not use theFirebase Android BoM, then just add the dependency for the`firebase-ai`library and accept the latest version that's suggested by Android Studio.

### Java

1. In your**module (app-level) Gradle file** (usually`<project>/<app-module>/build.gradle.kts`or`<project>/<app-module>/build.gradle`), replace old dependencies (as applicable) with the following.

   Note that it might be easier to migrate your app's codebase (see the remaining sections in this guide) before deleting the old dependency.  

   ```java
   // BEFORE
   dependencies {
     implementation("com.google.firebase:firebase-vertexai:16.0.0-betaXX")
   }


   // AFTER
   dependencies {
     // Import the BoM for the Firebase platform
     implementation(platform("com.google.firebase:firebase-bom:34.7.0"))

     // Add the dependency for the Firebase AI Logic library
     // When using the BoM, you don't specify versions in Firebase library dependencies
     implementation("com.google.firebase:firebase-ai")
   }
   ```
2. Sync your Android project with Gradle files.

Note that if you choose to not use theFirebase Android BoM, then just add the dependency for the`firebase-ai`library and accept the latest version that's suggested by Android Studio.

### Web

1. Get the latest version of the Firebase JS SDK for Web using npm:

   ```
   npm i firebase@latest
   ```

   OR  

   ```
   yarn add firebase@latest
   ```
2. Wherever you've imported the library, update your import statements to use`firebase/ai`instead.

   Note that it might be easier to migrate your app's codebase (see the remaining sections in this guide) before deleting the old imports.  

   ```javascript
   // BEFORE
   import { initializeApp } from "firebase/app";
   import { getVertexAI, getGenerativeModel } from "firebase/vertexai-preview";


   // AFTER
   import { initializeApp } from "firebase/app";
   import { getAI, getGenerativeModel } from "firebase/ai";
   ```

### Dart

1. Update to the use the`firebase_ai`package in your`pubspec.yaml`file by running the following command from your Flutter project directory:

   ```
   flutter pub add firebase_ai
   ```
2. Rebuild your Flutter project:

   ```
   flutter run
   ```
3. After you've finished migrating your app (see the remaining sections in this guide), make sure to delete the old package:

   <br />

   ```
   flutter pub remove firebase_vertexai
   ```

   <br />

### Unity

Support for Unity wasn't available from "Vertex AI in Firebase".

Learn how to[get started with theFirebase AI LogicSDK for Unity](https://firebase.google.com/docs/ai-logic/get-started).

## **Step 4**: Update the initialization in your app

<br />

|----------------------------------------------------------------------------------------------------------------------------------|
| *Click yourGemini APIprovider to view provider-specific content and code on this page.* Gemini Developer APIVertex AI Gemini API |

<br />

Update how you initialize the service for your chosen API provider and create a`GenerativeModel`instance.  

### Swift


    import FirebaseAILogic

    // Initialize the Gemini Developer API backend service
    let ai = FirebaseAI.firebaseAI(backend: .googleAI())

    // Create a `GenerativeModel` instance with a model that supports your use case
    let model = ai.generativeModel(modelName: "gemini-2.5-flash")

### Kotlin


    // Initialize the Gemini Developer API backend service
    // Create a `GenerativeModel` instance with a model that supports your use case
    val model = Firebase.ai(backend = GenerativeBackend.googleAI())
                            .generativeModel("gemini-2.5-flash")

### Java


    // Initialize the Gemini Developer API backend service
    // Create a `GenerativeModel` instance with a model that supports your use case
    GenerativeModel ai = FirebaseAI.getInstance(GenerativeBackend.googleAI())
            .generativeModel("gemini-2.5-flash");

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
    const model = getGenerativeModel(ai, { model: "gemini-2.5-flash" });

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
    FirebaseAI.googleAI().generativeModel(model: 'gemini-2.5-flash');

### Unity

Support for Unity wasn't available from "Vertex AI in Firebase".

Learn how to[get started with theFirebase AI LogicSDK for Unity](https://firebase.google.com/docs/ai-logic/get-started).

Note that**depending on the capability you're using, you might not always create a`GenerativeModel`instance**.

- To[access anImagenmodel](https://firebase.google.com/docs/ai-logic/generate-images-imagen), create an`ImagenModel`instance.

## **Step 5**: Update your code depending on features that you use

This step describes changes that may be required depending on which features you use.

- If you useCloud StorageURLs***and*** you swapped to use theGemini Developer APIin this migration, then you must update your multimodal requests to[include files as inline data](https://firebase.google.com/docs/ai-logic/generate-text?api=dev#base64)(or use YouTube URLs for videos).

- Several changes were introduced for the GA versions of the "Vertex AI in Firebase" SDKs. These same changes are required to use theFirebase AI LogicSDKs. Review the following lists for any changes that you might need to make in your code to accommodate taking up theFirebase AI LogicSDK.

### Required for all languages and platforms

- **Function calling**   
  If you implemented this feature before GA, then you'll need to make updates to how you define your schema. We recommend reviewing the updated[function calling guide](https://firebase.google.com/docs/ai-logic/function-calling)to learn how to write your function declarations.

- **Generating structured output (like JSON) using`responseSchema`**   
  If you implemented this feature before GA, then you'll need to make updates to how you define your schema. We recommend reviewing the new[structured output guide](https://firebase.google.com/docs/ai-logic/generate-structured-output)to learn how to write JSON schemas.

- **Timeout**

  - Changed the default timeout for requests to be 180 seconds.

### Required based on platform or language

### Swift

- **Enumerations**

  - Replaced most`enum`types with`struct`s with static variables. This change allows more flexibility for evolving the API in a backward-compatible way. When using`switch`statements, you must now include a`default:`case to cover unknown or unhandled values, including new values that are added to the SDK in the future.

  - Renamed the`BlockThreshold`enumeration to`HarmBlockThreshold`; this type is now a`struct`.

  - Removed`unknown`and`unspecified`cases from the following enumerations (now`struct`s):`HarmCategory`,`HarmBlockThreshold`,`HarmProbability`,`BlockReason`, and`FinishReason`.

  - Replaced the enumeration`ModelContent.Part`with a protocol named`Part`to allow new types to be added in a backward-compatible way. This change is described in greater detail in the**Content parts**section.

- **Content parts**

  - Removed the`ThrowingPartsRepresentable`protocol, and simplified the initializers for`ModelContent`to avoid occasional compiler errors. Images that don't encode properly will still throw errors when being used in`generateContent`.

  - Replaced the`ModelContent.Part`cases with the following`struct`types conforming to the`Part`protocol:

    - `.text`to`TextPart`
    - `.data`to`InlineDataPart`
    - `.fileData`to`FileDataPart`
    - `.functionCall`to`FunctionCallPart`
    - `.functionResponse`to`FunctionResponsePart`
- **Harm category**

  - Changed the`HarmCategory`to no longer be nested in the`SafetySetting`type. If you're referring to it as`SafetySetting.HarmCategory`, that can be replaced with`HarmCategory`.
- **Safety feedback**

  - Removed the`SafetyFeedback`type, since it wasn't used in any of the responses.
- **Citation metadata**

  - Renamed the`citationSources`property to`citations`in`CitationMetadata`.
- **Total billable characters**

  - Changed the`totalBillableCharacters`property in`CountTokensResponse`to be optional to reflect situations where no characters are sent.
- **Candidate response**

  - Renamed`CandidateResponse`to`Candidate`to match other platforms.
- **Generation configuration**

  - Changed the public properties of`GenerationConfig`to`internal`. They all remain configurable in the initializer.

### Kotlin

- **Enumerations**

  - Replaced`enum`classes and`sealed`classes with regular classes. This change allows more flexibility for evolving the API in a backward compatible way.

  - Renamed the`BlockThreshold`enumeration to`HarmBlockThreshold`.

  - Removed values from the following enumerations:`HarmBlockThreshold`,`HarmProbability`,`HarmSeverity`,`BlockReason`, and`FinishReason`.

- **Blob methods**

  - Renamed all methods that included`Blob`as part of their name to use`InlineData`instead.
- **Safety settings**

  - Changed the field`method`to be nullable.
- **Duration class**

  - Removed all usages of Kotlin's`Duration`class, and replaced it with`long`. This change provides better interoperability with Java.
- **Citation metadata**

  - Wrapped all the fields previously declared in`CitationMetadata`into a new class called`Citation`. Citations can be found in the list called`citations`in`CitationMetadata`. This change allows better alignment of types across platforms.
- **Count tokens**

  - Changed the field`totalBillableCharacters`to be nullable.
- **Total billable characters**

  - Changed the`totalBillableCharacters`property in`CountTokensResponse`to be optional to reflect situations where no characters are sent.
- **Instantiating a model**

  - Moved the`requestOptions`parameter to the end of the parameter list to align with other platforms.
- **Live API**

  - Removed`UNSPECIFIED`value for enum class`ResponseModality`. Instead use`null`.

  - Renamed`LiveGenerationConfig.setResponseModalities`to`LiveGenerationConfig.setResponseModality`.

  - Removed the`LiveContentResponse.Status`class, and instead have nested the status fields as properties of`LiveContentResponse`.

  - Removed the`LiveContentResponse`class, and instead have provided subclasses of`LiveServerMessage`that match the responses from the model.

  - Changed`LiveModelFutures.connect`to return`ListenableFuture<LiveSessionFutures>`instead of`ListenableFuture<LiveSession>`.

### Java

- **Enumerations**

  - Replaced`enum`classes and`sealed`classes with regular classes. This change allows more flexibility for evolving the API in a backward compatible way.

  - Renamed the`BlockThreshold`enumeration to`HarmBlockThreshold`.

  - Removed values from the following enumerations:`HarmBlockThreshold`,`HarmProbability`,`HarmSeverity`,`BlockReason`, and`FinishReason`.

- **Blob methods**

  - Renamed all methods that included`Blob`as part of their name to use`InlineData`instead.
- **Safety settings**

  - Changed the field`method`to be nullable.
- **Duration class**

  - Removed all usages of Kotlin's`Duration`class, and replaced it with`long`. This change provides better interoperability with Java.
- **Citation metadata**

  - Wrapped all the fields previously declared in`CitationMetadata`into a new class called`Citation`. Citations can be found in the list called`citations`in`CitationMetadata`. This change allows better alignment of types across platforms.
- **Count tokens**

  - Changed the field`totalBillableCharacters`to be nullable.
- **Total billable characters**

  - Changed the`totalBillableCharacters`property in`CountTokensResponse`to be optional to reflect situations where no characters are sent.
- **Instantiating a model**

  - Moved the`requestOptions`parameter to the end of the parameter list to align with other platforms.
- **Live API**

  - Removed`UNSPECIFIED`value for enum class`ResponseModality`. Instead use`null`.

  - Renamed`LiveGenerationConfig.setResponseModalities`to`LiveGenerationConfig.setResponseModality`.

  - Removed the`LiveContentResponse.Status`class, and instead have nested the status fields as properties of`LiveContentResponse`.

  - Removed the`LiveContentResponse`class, and instead have provided subclasses of`LiveServerMessage`that match the responses from the model.

  - Changed`LiveModelFutures.connect`to return`ListenableFuture<LiveSessionFutures>`instead of`ListenableFuture<LiveSession>`.

- Changed various Java builder methods to now correctly return the instance of their class, instead of`void`.

### Web

- **Enumerations**

  - Removed values from the following enumerations:`HarmCategory`,`BlockThreshold`,`HarmProbability`,`HarmSeverity`,`BlockReason`, and`FinishReason`.
- **Block reason**

  - Changed`blockReason`in`PromptFeedback`to be optional.

Changes required*only if you're starting to use theGemini Developer API* (instead of theVertex AIGemini API):

- **Safety settings**

  - Removed usages of the unsupported`SafetySetting.method`.
- **Inline data**

  - Removed usages of the unsupported`InlineDataPart.videoMetadata`.

### Dart

- **Enumerations**

  - Removed values from the following enumerations:`HarmCategory`,`HarmProbability`,`BlockReason`, and`FinishReason`.
- **Data part**

  - Renamed`DataPart`to`InlineDataPart`, and the`static``data`function to`inlineData`to align with other platforms.
- **Request options**

  - Removed`RequestOptions`since`timeout`wasn't functional. It will be re-added in the near future, but it will be moved to the`GenerativeModel`type to match other platforms.
- **Stop sequences**

  - Changed the`stopSequences`parameter in`GenerationConfig`to be optional and to default to`null`instead of an empty array.
- **Citations**

  - Renamed the`citationSources`property to`citations`in`CitationMetadata`. The`CitationSource`type was renamed to`Citation`to match other platforms.
- **Unnecessary public types, methods, and properties**

  - Removed the following types, methods, and properties which were unintentionally exposed:`defaultTimeout`,`CountTokensResponseFields`,`parseCountTokensResponse`,`parseEmbedContentResponse`,`parseGenerateContentResponse`,`parseContent`,`BatchEmbedContentsResponse`,`ContentEmbedding`,`EmbedContentRequest`, and`EmbedContentResponse`.
- **Count tokens**

  - Removed extra fields from the`countTokens`function that are no longer necessary. Only`contents`is needed.
- **Instantiating a model**

  - Moved the`systemInstruction`parameter to the end of the parameter list to align with other platforms.
- **Embedding functionality**

  - Removed unsupported embedding functionality (`embedContent`and`batchEmbedContents`) from the model.

### Unity

Support for Unity wasn't available from "Vertex AI in Firebase".

Learn how to[get started with theFirebase AI LogicSDK for Unity](https://firebase.google.com/docs/ai-logic/get-started).

## Possible errors related to migrating

As you're migrating to use the GA version ofFirebase AI Logic, you might encounter errors if you haven't completed all of the required changes as described in this migration guide.

### 403 Error:`Requests to this API firebasevertexai.googleapis.com ... are blocked.`

If you receive a 403 error that says`Requests to this API firebasevertexai.googleapis.com ... are blocked.`, it usually means that the Firebase API key in your Firebase configuration file or object doesn't have a required API in its allowlist for the product that you're trying to use.

Make sure that the Firebase API key used by your app has all the[required APIs included in the key's "API restrictions" allowlist](https://firebase.google.com/docs/projects/api-keys#faq-required-apis-for-restricted-firebase-api-key).**ForFirebase AI Logic, your Firebase API key needs to have at minimum theFirebase AI LogicAPI in its allowlist.** This API should have been automatically added to your API key's allowlist when you[enabled the required APIs in theFirebaseconsole](https://firebase.google.com/docs/ai-logic/migrate-to-ga#enable-required-apis).

You can view all your API keys in the[*APIs \& Services* \>*Credentials*](https://console.cloud.google.com/apis/credentials?project=_)panel in theGoogle Cloudconsole.
| **Note:** Firebase-related APIs use API keys only to*identify* the Firebase project or app,*not for authorization* to call the API (like some other APIs allow). Authorization for Firebase-related APIs is handled separately from the API key, either throughGoogle CloudIAM permissions,Firebase Security Rules, orFirebase App Check. Learn more about[Firebase API keys](https://firebase.google.com/docs/projects/api-keys).

<br />

[Give feedback about your experience withFirebase AI Logic](https://firebase.google.com/docs/ai-logic/feedback)

<br />