# Source: https://firebase.google.com/docs/ai-logic/migrate-from-google-ai-client-sdks.md.txt

> [!NOTE]
> **This guide helps you migrate from the
> Google AI client SDKs to the
> Firebase AI Logic client SDKs** .  
> These client SDKs are available in Swift for Apple platforms, Kotlin and Java for Android, JavaScript for Web, Dart for Flutter, and Unity.
>
> If you're using a GA or Preview (or beta) version of a
> "Vertex AI in Firebase" SDK, then go to the guide for
> [migrating from the GA
> version of the SDK](https://firebase.google.com/docs/ai-logic/migrate-to-latest-sdk) or
> [migrating from the preview
> version of the SDK](https://firebase.google.com/docs/ai-logic/migrate-from-preview).

<br />

[Go directly to migration instructions](https://firebase.google.com/docs/ai-logic/migrate-from-google-ai-client-sdks#migration-instructions)

## Why migrate to use the Firebase AI Logic SDKs?

You might have tried out an alternative set of mobile or web client SDKs that
gave you access to the Gemini Developer API.

Those client SDKs were not integrated into the robust Firebase ecosystem that
offers critical services for mobile and web apps. They are now deprecated in
favor of the Firebase AI Logic client SDKs, which can give you
access to the Gemini Developer API.

#### Security features for mobile and web apps

For mobile and web apps, security is critical and requires special
considerations because your code -- including calls to the Gemini API -- is
running in an unprotected environment. You can use Firebase App Check to
protect APIs from abuse by unauthorized clients.

When you
[use Firebase App Check with Firebase AI Logic](https://firebase.google.com/docs/ai-logic/app-check),
you never add your Gemini API key for the Gemini Developer API
directly into your mobile or web app's codebase. Instead, the
Gemini API key stays on the server, unexposed to malicious actors.

#### Ecosystem built for mobile and web apps

Firebase is Google's platform for developing mobile and web apps. Using
Firebase AI Logic means that your apps are in an ecosystem that's focused on
the needs of full-stack apps and developers. For example:

- Dynamically set run-time configurations or swap out values in
  your app (like a model name and version) without releasing a new app version
  using [Firebase Remote Config](https://firebase.google.com/docs/ai-logic/solutions/remote-config).

- Use Cloud Storage for Firebase to include large files in your multimodal
  requests (if you use the Vertex AI Gemini API). The
  Cloud Storage client SDKs help you handle file uploads and downloads (even in
  poor network conditions) and offer more security for your end-users' data.
  Learn more in our
  [solution guide about using Cloud Storage for Firebase](https://firebase.google.com/docs/ai-logic/solutions/cloud-storage).

- Manage structured data using database SDKs built for mobile and web apps
  (like [Cloud Firestore](https://firebase.google.com/docs/firestore)).

## Migrate to the Firebase AI Logic SDKs

Overview of steps to migrate to the Firebase AI Logic SDKs:

- **Step 1**: Set up a new or existing Firebase project and connect your app to
  Firebase.

- **Step 2** : Add the Firebase AI Logic SDKs to your app.

- **Step 3**: Update your imports and initialization in your app.

- **Step 4**: Update your code depending on the features that you use.

### **Step 1**: Set up a Firebase project and connect your app

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

     If you'd like, you can add Firebase to the project that was created behind
     the scenes when you created a Gemini API key in
     Google AI Studio.

   Complete the remaining steps of the on-screen workflow to create a Firebase
   project. Note that when prompted, you do ***not*** need to set up
   Google Analytics to use the Firebase AI Logic SDKs.

   <br />

   <br />

2. In the Firebase console, go to the [**Firebase AI Logic** page](https://console.firebase.google.com/project/_/ailogic).

3. Click **Get started** to launch a guided workflow that helps you set up the
   [required APIs](https://firebase.google.com/docs/ai-logic/faq-and-troubleshooting#required-apis)
   and resources for your project.

4. Select the **Gemini Developer API**. You can always set up and use
   the other API provider later, if you'd like.

   The console will enable the required APIs and create a new, dedicated
   Gemini API key in your project.  

   *Do **not** add this new Gemini API key into your app's codebase.*
   [Learn more.](https://firebase.google.com/docs/ai-logic/faq-and-troubleshooting#add-gemini-api-key-to-codebase)
5. If prompted in the console's workflow, follow the on-screen instructions to
   register your app and connect it to Firebase.

6. Continue in this migration guide to update the library and initialization in
   your app.

### **Step 2** : Add the Firebase AI Logic SDK to your app

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

Support for Unity wasn't available from the
Google AI client SDKs.

Learn how to
[get started with the Firebase AI Logic SDK for Unity](https://firebase.google.com/docs/ai-logic/get-started).

#### Remove the old SDK from your app

After you've finished migrating your app (see the remaining sections in this
guide), make sure to delete the old library.

### Swift

Remove the old library:

1. In Xcode, with your app project open, navigate to the
   **Packages Dependencies** pane.

2. Select the `generative-ai-swift` package from the list of package
   dependencies.

3. Click the **`-`** button from the bottom of the list and click **Remove**
   to confirm.

### Kotlin

    dependencies {
        implementation("com.google.ai.client.generativeai:generativeai:VERSION")
    }

### Java

    dependencies {
        implementation("com.google.ai.client.generativeai:generativeai:VERSION")
    }

### Web

    // BEFORE
    import { initializeApp } from "firebase/app";
    import { GoogleGenerativeAI } from "@google/generative-ai";

### Dart

Delete the old package:  

`flutter pub remove google_generative_ai`

### Unity

Support for Unity wasn't available from
Google AI client SDKs.

Learn how to
[get started with the Firebase AI Logic SDK for Unity](https://firebase.google.com/docs/ai-logic/get-started).

### **Step 3**: Update your imports and initialization in your app

Update your imports and how you initialize the Gemini Developer API
backend service and create a `GenerativeModel` instance.

> [!CAUTION]
> When using the Firebase AI Logic client SDKs with the Gemini Developer API, **you do *not* add your
> Gemini API key into your app's codebase** . [Learn more.](https://firebase.google.com/docs/ai-logic/faq-and-troubleshooting#add-gemini-api-key-to-codebase) Also, make sure to remove from your app your old Gemini API key and any mechanisms or files that you used to store that key.
>
> As soon as you start seriously developing your app,
> **it's critical that you
> [integrate with Firebase App Check](https://firebase.google.com/docs/ai-logic/app-check)**
> so that only requests from your actual app and verified devices are passed
> through to the backend.

### Swift

```swift
// BEFORE
import GoogleGenerativeAI

let model = GenerativeModel(name: "MODEL_NAME", apiKey: APIKey.default)

// AFTER
import FirebaseAILogic

// Initialize the Gemini Developer API backend service
let ai = FirebaseAI.firebaseAI(backend: .googleAI())

// Create a `GenerativeModel` instance with a model that supports your use case
let model = ai.generativeModel(modelName: "gemini-3-flash-preview")
```

### Kotlin

```kotlin
// BEFORE
import com.google.ai.client.generativeai.Chat
import com.google.ai.client.generativeai.type.Content
import com.google.ai.client.generativeai.java.GenerativeModuleFutures

...

val generativeModel = GenerativeModel(modelName = "MODEL_NAME",
  // Access your API key as a Build Configuration variable
  apiKey = BuildConfig.apiKey
)

// AFTER
import com.google.firebase.Firebase
import com.google.firebase.ai.ai
import com.google.firebase.ai.type.GenerativeBackend

...

// Initialize the Gemini Developer API backend service
// Create a `GenerativeModel` instance with a model that supports your use case
val model = Firebase.ai(backend = GenerativeBackend.googleAI())
                        .generativeModel("gemini-3-flash-preview")
```

### Java

```java
// BEFORE
import com.google.ai.client.generativeai.Chat;
import com.google.ai.client.generativeai.type.Content;
import com.google.ai.client.generativeai.java.GenerativeModuleFutures;

...

GenerativeModel gm = new GenerativeModel("MODEL_NAME",
  // Access your API key as a Build Configuration variable
  BuildConfig.apiKey
);

GenerativeModelFutures model = GenerativeModelFutures.from(gm);

// AFTER
import com.google.firebase.ai.FirebaseAI;
import com.google.firebase.ai.GenerativeModel;
import com.google.firebase.ai.java.GenerativeModelFutures;
import com.google.firebase.ai.type.GenerativeBackend;

...

// Initialize the Gemini Developer API backend service
// Create a `GenerativeModel` instance with a model that supports your use case
GenerativeModel ai = FirebaseAI.getInstance(GenerativeBackend.googleAI())
        .generativeModel("gemini-3-flash-preview");

// Use the GenerativeModelFutures Java compatibility layer which offers
// support for ListenableFuture and Publisher APIs
GenerativeModelFutures model = GenerativeModelFutures.from(ai);
```

### Web

```javascript
// BEFORE
import { GoogleGenerativeAI } from "@google/generative-ai";

// Fetch your API_KEY and access your API
const API_KEY = "...";
const genAI = new GoogleGenerativeAI(API_KEY);

...

const model = genAI.getGenerativeModel({ model: "MODEL_NAME"});

// AFTER
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
```

### Dart

```dart
// BEFORE
import 'package:google_generative_ai/google_generative_ai.dart';

final apiKey = Platform.environment['API_KEY'];
if (apiKey == null) {
print('No \$API_KEY environment variable');
exit(1);
}

final model = GenerativeModel(model: 'MODEL_NAME', apiKey: apiKey);

// AFTER
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
```

### Unity

Support for Unity wasn't available from
Google AI client SDKs.

Learn how to
[get started with the Firebase AI Logic SDK for Unity](https://firebase.google.com/docs/ai-logic/get-started).

Note that **depending on the capability you're using, you might not always
create a `GenerativeModel` instance**.

- To [access an Imagen model](https://firebase.google.com/docs/ai-logic/generate-images-imagen), create an `ImagenModel` instance.

### **Step 4**: Update code depending on the features that you use

This step describes changes that may be required depending on which features you
use.

- The Firebase AI Logic client SDKs don't support
  code execution. If you use this feature, make sure to accommodate this in
  your app.

- Review the following lists for any changes that you might need to make in your
  code to accommodate migrating to the
  Firebase AI Logic client SDKs.

#### Required for all languages and platforms

- **Function calling**   

  If you implemented this feature, then you'll need to make updates to
  how you define your schema. We recommend reviewing the updated
  [function calling guide](https://firebase.google.com/docs/ai-logic/function-calling) to learn how to
  write your function declarations.

- **Generating structured output (like JSON) using `responseSchema`**   

  If you implemented this feature, then you'll need to make updates to
  how you define your schema. We recommend reviewing the new
  [structured output guide](https://firebase.google.com/docs/ai-logic/generate-structured-output) to learn
  how to write JSON schemas.

- **Timeout**

  - Changed the default timeout for requests to be 180 seconds.

#### Required based on platform or language

### Swift

- **Enumerations**

  - Replaced most `enum` types with `struct`s with static variables. This
    change allows more flexibility for evolving the API in a
    backward-compatible way. When using `switch` statements, you must now
    include a `default:` case to cover unknown or unhandled values,
    including new values that are added to the SDK in the future.

  - Renamed the `BlockThreshold` enumeration to `HarmBlockThreshold`; this
    type is now a `struct`.

  - Removed `unknown` and `unspecified` cases from the following
    enumerations (now `struct`s): `HarmCategory`, `HarmBlockThreshold`,
    `HarmProbability`, `BlockReason`, and `FinishReason`.

  - Replaced the enumeration `ModelContent.Part` with a protocol named
    `Part` to allow new types to be added in a backward-compatible way. This
    change is described in greater detail in the **Content parts** section.

- **Content parts**

  - Removed the `ThrowingPartsRepresentable` protocol, and simplified
    the initializers for `ModelContent` to avoid occasional compiler errors.
    Images that don't encode properly will still throw errors when being
    used in `generateContent`.

  - Replaced the `ModelContent.Part` cases with the following `struct` types
    conforming to the `Part` protocol:

    - `.text` to `TextPart`
    - `.data` to `InlineDataPart`
    - `.fileData` to `FileDataPart`
    - `.functionCall` to `FunctionCallPart`
    - `.functionResponse` to `FunctionResponsePart`
- **Harm category**

  - Changed the `HarmCategory` to no longer be nested in the `SafetySetting` type. If you're referring to it as `SafetySetting.HarmCategory`, that can be replaced with `HarmCategory`.
- **Safety feedback**

  - Removed the `SafetyFeedback` type, since it wasn't used in any of the responses.
- **Citation metadata**

  - Renamed the `citationSources` property to `citations` in `CitationMetadata`.
- **Total billable characters**

  - Changed the `totalBillableCharacters` property in `CountTokensResponse` to be optional to reflect situations where no characters are sent.
- **Candidate response**

  - Renamed `CandidateResponse` to `Candidate` to match other platforms.
- **Generation configuration**

  - Changed the public properties of `GenerationConfig` to `internal`. They all remain configurable in the initializer.

### Kotlin

- **Enumerations**

  - Replaced `enum` classes and `sealed` classes with regular classes. This
    change allows more flexibility for evolving the API in a backward
    compatible way.

  - Renamed the `BlockThreshold` enumeration to `HarmBlockThreshold`.

  - Removed values from the following enumerations: `HarmBlockThreshold`,
    `HarmProbability`, `HarmSeverity`, `BlockReason`, and `FinishReason`.

- **Blob methods**

  - Renamed all methods that included `Blob` as part of their name to use `InlineData` instead.
- **Safety settings**

  - Changed the field `method` to be nullable.
- **Duration class**

  - Removed all usages of Kotlin's `Duration` class, and replaced it with `long`. This change provides better interoperability with Java.
- **Citation metadata**

  - Wrapped all the fields previously declared in `CitationMetadata` into a new class called `Citation`. Citations can be found in the list called `citations` in `CitationMetadata`. This change allows better alignment of types across platforms.
- **Count tokens**

  - Changed the field `totalBillableCharacters` to be nullable.
- **Total billable characters**

  - Changed the `totalBillableCharacters` property in `CountTokensResponse` to be optional to reflect situations where no characters are sent.
- **Instantiating a model**

  - Moved the `requestOptions` parameter to the end of the parameter list to align with other platforms.

### Java

- **Enumerations**

  - Replaced `enum` classes and `sealed` classes with regular classes. This
    change allows more flexibility for evolving the API in a backward
    compatible way.

  - Renamed the `BlockThreshold` enumeration to `HarmBlockThreshold`.

  - Removed values from the following enumerations: `HarmBlockThreshold`,
    `HarmProbability`, `HarmSeverity`, `BlockReason`, and `FinishReason`.

- **Blob methods**

  - Renamed all methods that included `Blob` as part of their name to use `InlineData` instead.
- **Safety settings**

  - Changed the field `method` to be nullable.
- **Duration class**

  - Removed all usages of Kotlin's `Duration` class, and replaced it with `long`. This change provides better interoperability with Java.
- **Citation metadata**

  - Wrapped all the fields previously declared in `CitationMetadata` into a new class called `Citation`. Citations can be found in the list called `citations` in `CitationMetadata`. This change allows better alignment of types across platforms.
- **Count tokens**

  - Changed the field `totalBillableCharacters` to be nullable.
- **Total billable characters**

  - Changed the `totalBillableCharacters` property in `CountTokensResponse` to be optional to reflect situations where no characters are sent.
- **Instantiating a model**

  - Moved the `requestOptions` parameter to the end of the parameter list to align with other platforms.

### Web

Note that the Google AI client SDK for JavaScript has had many
changes since the time that the
Firebase AI Logic client SDKs branched from it. The
following list are some potential changes that you might need to consider as
you migrate to the
Firebase AI Logic client SDKs.

- **Enumerations**

  - Removed values from the following enumerations: `HarmCategory`, `BlockThreshold`, `HarmProbability`, `HarmSeverity`, `BlockReason`, and `FinishReason`.
- **Block reason**

  - Changed `blockReason` in `PromptFeedback` to be optional.
- **Search Grounding**

  - Removed all usages of this feature, since it's not yet supported in the Firebase AI Logic SDKs.
- **Errors**

  - Removed all usages of `GoogleGenerativeAIError`, and optionally move to `AIError`.

### Dart

- **Enumerations**

  - Removed values from the following enumerations: `HarmCategory`, `HarmProbability`, `BlockReason`, and `FinishReason`.
- **Data part**

  - Renamed `DataPart` to `InlineDataPart`, and the `static` `data` function to `inlineData` to align with other platforms.
- **Request options**

  - Removed `RequestOptions` since `timeout` wasn't functional. It will be re-added in the near future, but it will be moved to the `GenerativeModel` type to match other platforms.
- **Stop sequences**

  - Changed the `stopSequences` parameter in `GenerationConfig` to be optional and to default to `null` instead of an empty array.
- **Citations**

  - Renamed the `citationSources` property to `citations` in `CitationMetadata`. The `CitationSource` type was renamed to `Citation` to match other platforms.
- **Unnecessary public types, methods, and properties**

  - Removed the following types, methods, and properties which were unintentionally exposed: `defaultTimeout`, `CountTokensResponseFields`, `parseCountTokensResponse`, `parseEmbedContentResponse`, `parseGenerateContentResponse`, `parseContent`, `BatchEmbedContentsResponse`, `ContentEmbedding`, `EmbedContentRequest`, and `EmbedContentResponse`.
- **Count tokens**

  - Removed extra fields from the `countTokens` function that are no longer necessary. Only `contents` is needed.
- **Instantiating a model**

  - Moved the `systemInstruction` parameter to the end of the parameter list to align with other platforms.
- **Embedding functionality**

  - Removed unsupported embedding functionality (`embedContent` and `batchEmbedContents`) from the model.

### Unity

Support for Unity wasn't available from
Google AI client SDKs.

Learn how to
[get started with the Firebase AI Logic SDK for Unity](https://firebase.google.com/docs/ai-logic/get-started).

<br />

[Give feedback
about your experience with Firebase AI Logic](https://firebase.google.com/docs/ai-logic/feedback)

<br />