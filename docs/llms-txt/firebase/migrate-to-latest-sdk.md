# Source: https://firebase.google.com/docs/ai-logic/migrate-to-latest-sdk.md.txt

<br />

| **This guide helps you migrate from the GA versions of the "Vertex AI in Firebase" SDKs to theFirebase AI Logicclient SDKs** .  
| These client SDKs are available in Swift for Apple platforms, Kotlin and Java for Android, JavaScript for Web, Dart for Flutter, and Unity.
|
| If you're using a Preview version of a "Vertex AI in Firebase" SDK (you'll see "beta" or "preview" in the version or the package/library name), then go to the guide for[migrating from the preview version of the SDK](https://firebase.google.com/docs/ai-logic/migrate-from-preview).

<br />

Firebase AI Logicand its client SDKs were formerly called "Vertex AI in Firebase". To better reflect our expanded services and features (for example, we now support theGemini Developer API!),**we renamed and repackaged our services intoFirebase AI Logic**.

To securely access Google's generative AI models directly from your mobile or web apps,**you can now choose a "Gemini API" provider --- either the long-availableVertex AIGemini APIor now theGemini Developer API** . This means that you now have the option to use theGemini Developer API, which provides a**no-cost tier**with reasonable rate limits and quotas.

#### Overview of steps to migrate to theFirebase AI LogicSDKs

- **Step 1** : Choose the best "Gemini API" provider for your app and use cases.

- **Step 2** : Set up your Firebase project so that you can use theGemini Developer API.  
  *Only applicable if you're swapping to use theGemini Developer APIinstead of theVertex AIGemini API.*

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
| If your Firebase project stays on the Blaze pricing plan, then you'll be using one of the "paid tiers" for theGemini Developer API.

- **If you want to keep using theVertex AIGemini API** :  
  Skip the next step and jump straight to[updating the library in your app](https://firebase.google.com/docs/ai-logic/migrate-to-latest-sdk?api=vertex#update-library-and-initialization), and then the rest of this guide.

- **If you want to swap to theGemini Developer API** :  
  Continue to the next step to[set up your Firebase project to use that API](https://firebase.google.com/docs/ai-logic/migrate-to-latest-sdk#set-up-firebase), and then the rest of this guide.

## **Step 2** : Set up your Firebase project so that you can use theGemini Developer API

*This step is only required if you want to swap to using theGemini Developer APIwith theFirebase AI Logicclient SDKs. However, if you want to keep using theVertex AIGemini API, skip to the next step.*

Note that it's OK to have both of the "Gemini API" providers enabled in your project at the same time.

1. In theFirebaseconsole, go to the[**Firebase AI Logic**page](https://console.firebase.google.com/project/_/ailogic).

2. Go to the**Settings** tab, and select**Gemini Developer API**.

3. Enable theGemini Developer API.

   The console will make sure the required APIs are enabled and generate aGeminiAPI key in your Firebase project.  
   *Do**not** add thisGeminiAPI key into your app's codebase.* [Learn more.](https://firebase.google.com/docs/ai-logic/faq-and-troubleshooting#add-gemini-api-key-to-codebase)
4. Continue in this migration guide to update the library and initialization in your app.

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
   Select**FirebaseVertexAI** , and then press the**---**button.

### Kotlin

1. In your**module (app-level) Gradle file** (usually`<project>/<app-module>/build.gradle.kts`or`<project>/<app-module>/build.gradle`), replace old dependencies (as applicable) with the following.

   Note that it might be easier to migrate your app's codebase (see the remaining sections in this guide) before deleting the old dependency.  

   ```kotlin
   // BEFORE
   dependencies {
     implementation(platform("com.google.firebase:firebase-bom:33.x.y"))
     implementation("com.google.firebase:firebase-vertexai")
     // OR if not using the BoM
     implementation("com.google.firebase:firebase-vertexai:16.x.y")
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
     implementation(platform("com.google.firebase:firebase-bom:33.x.y"))
     implementation("com.google.firebase:firebase-vertexai")
     // OR if not using the BoM
     implementation("com.google.firebase:firebase-vertexai:16.x.y")
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
   import { getVertexAI, getGenerativeModel } from "firebase/vertexai";


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

- If you useCloud StorageURLs***and*** you swapped to use theGemini Developer APIin this migration, then you need to update your multimodal requests to[include files as inline data](https://firebase.google.com/docs/ai-logic/generate-text?api=dev#base64)(or use YouTube URLs for videos).

- Review the following lists for any changes that you might need to make in your code to accommodate taking up theFirebase AI LogicSDK.

### Swift

No additional changes.

### Kotlin

- **Live API**

  - Removed`UNSPECIFIED`value for enum class`ResponseModality`. Instead use`null`.

### Java

- **Live API**

  - Removed`UNSPECIFIED`value for enum class`ResponseModality`. Instead use`null`.
- Changed various Java builder methods to now correctly return the instance of their class, instead of void.

### Web

Changes required*only if you're starting to use theGemini Developer API* (instead of theVertex AIGemini API):

- **Safety settings**

  - Removed usages of the unsupported`SafetySetting.method`.
- **Inline data**

  - Removed usages of the unsupported`InlineDataPart.videoMetadata`.

### Dart

No additional changes.

### Unity

Support for Unity wasn't available from "Vertex AI in Firebase".

Learn how to[get started with theFirebase AI LogicSDK for Unity](https://firebase.google.com/docs/ai-logic/get-started).

<br />

[Give feedback about your experience withFirebase AI Logic](https://firebase.google.com/docs/ai-logic/feedback)

<br />