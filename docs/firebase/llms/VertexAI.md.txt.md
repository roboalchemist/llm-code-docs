# Source: https://firebase.google.com/docs/remote-config/solutions/vertexai.md.txt

When calling the Gemini API from your app using a
Firebase AI Logic SDK, your request contains a number of parameters that
control generative AI responses. These usually include the model name, the
model generation configuration (maximum tokens, temperature, etc.), safety
settings, system instructions, and prompt data.

> [!IMPORTANT]
> **Important:** We strongly recommend implementing Remote Config for [remotely changing the model name in your app](https://firebase.google.com/docs/ai-logic/change-model-name-remotely).

[Video](https://www.youtube.com/watch?v=8K9stpPhTYI)

In most cases, you'll want to change these on-demand or as needed for a number
of scenarios:

- Update your generative AI model without releasing a new app. You can upgrade to newer, stable model versions before earlier versions are retired, drop to lower-cost or higher performance models based on your users' needs and attributes, or conditionally deploy the latest and greatest models to specific user segments (like beta testers).
- Set the location where you access the model so that it's closer to your users.
- A/B test different system instructions and prompts, then slowly roll out the winning experiment values to your users.
- Use feature flags to quickly expose or hide generative AI features in your app.

[Firebase Remote Config](https://firebase.google.com/docs/remote-config) does all of this and
more, letting you update parameter values as needed and
*conditionally* for app instances that match characteristics you set in the
Firebase console, without releasing a new version of your app.

This solution guide provides specific recommended use cases and describes how to
add Remote Config to your generative AI app.

[Jump to code implementation](https://firebase.google.com/docs/remote-config/solutions/vertexai#add-firebase-remote-config)

## Why use Firebase Remote Config with your app?

Firebase Remote Config lets you dynamically adjust your app's behavior
without requiring app updates. This is especially powerful for apps that use
generative AI, where rapid iteration and fine-tuning are crucial.

### Essential use cases for Remote Config with generative AI apps

We recommend using Remote Config with Firebase AI Logic for the
following essential use cases:

- **Upgrade to the latest model version without an app update** :
  Use Remote Config parameters to change the model name as needed, so that
  you can upgrade to the latest version of your preferred Gemini
  model as soon as it's available.

  > [!IMPORTANT]
  > **Important:** We strongly recommend implementing Remote Config for [remotely changing the model name in your app](https://firebase.google.com/docs/ai-logic/change-model-name-remotely).

- **Update system instructions and safety settings without an app update** :
  Store system instructions and safety settings inside Remote Config
  parameters to ensure that you can change them on-demand if you discover
  issues after deployment.

- **Reduce risk and enforce AI safety** :
  Use
  [Remote Config rollouts](https://firebase.google.com/docs/remote-config/rollouts) to safely and gradually release
  generative AI changes to your iOS and Android users.

### Advanced and recommended use cases for Remote Config with generative AI apps

After instrumenting your app with Remote Config and Google Analytics,
you can explore advanced use cases:

- **Set location based on client location** :
  Use Remote Config conditions to
  [set the location where you access the model](https://firebase.google.com/docs/ai-logic/locations)
  based on the client's detected location.

- **Experiment with different models**:
  Quickly test and switch between various generative AI models, or even access
  different models for different user segments, to find the best fit for your
  specific use case.

- **Optimize model performance**:
  Fine-tune model parameters, such as system prompt, maximum output tokens,
  temperature, and other settings.

- **Use different system instructions, prompts, and model configuration
  based on client attributes** :
  When using
  [Remote Config with Google Analytics](https://firebase.google.com/docs/remote-config/config-analytics),
  you can create conditions based on client attributes or custom audiences and
  set different parameters based on these attributes.

  For example, if you're using generative AI to provide technical support
  in your app, you might want to set system instructions specific to the
  app platform to ensure accurate instructions are provided to your
  Android, iOS, and web platform users.
- **Personalize experiences for each user** :
  Use
  [Remote Config personalization](https://firebase.google.com/docs/remote-config/personalization) with your mobile
  apps and games to automatically determine the optimum generative AI settings
  for each user.

- **Control costs**:
  Remotely adjust which generative AI models are called, how frequently they
  are used, and dynamically configure maximum output token values based on
  user audience to reduce unnecessary costs.

- **Optimize app experience and results** :
  Use [A/B Testing with Remote Config](https://firebase.google.com/docs/ab-testing) with your
  mobile apps and games to test changes to generative AI parameters across
  different user segments to see how they affect key metrics like retention
  and revenue.

By instrumenting your generative AI app with Firebase Remote Config, you can
build flexible, safe, and cost-effective AI-powered applications while creating
delightful experiences for your users.

> [!IMPORTANT]
> **Important:** Don't store confidential data in Remote Config parameter keys or parameter values. Data is encrypted in transit, but end users can access any default or fetched Remote Config or Firebase AI Logic parameter that is available to their app instance.

## Add Firebase Remote Config to your app

In this solution guide, you'll use Firebase Remote Config to
dynamically update parameters in your app that use the
Firebase AI Logic SDK. You will learn how to:

- Fetch and activate parameters like model names and system instructions from Firebase Remote Config.
- Update your Gemini API calls to use the dynamically retrieved parameters, letting you switch between different models or modify system instructions without an app update.
- Control parameters remotely, adjusting model behavior and capabilities as needed.

### Prerequisites

This guide assumes that you're familiar with developing apps for your platform.

Before you begin, make sure that you do the following:

- Complete the
  [Firebase AI Logic getting started guide](https://firebase.google.com/docs/ai-logic/get-started),
  which describes how to set up your Firebase project,
  connect your app to Firebase, add the SDK, initialize the backend service
  for your chosen "Gemini API" provider, and create a model instance.

- Enable [Google Analytics](https://firebase.google.com/docs/analytics) in your Firebase project
  and add its SDK to your app (required for conditional targeting, like
  setting the location where you access the model based on the client device's
  location).

> [!TIP]
> **Tip:** If you don't have an app of your own, you can use the quickstart app for Firebase AI Logic: [iOS+](https://github.com/firebase/quickstart-ios/tree/main/firebaseai) \| [Android](https://github.com/firebase/quickstart-android/tree/master/firebase-ai) \| [Web](https://github.com/firebase/quickstart-js/tree/master/ai) \| [Flutter](https://github.com/firebase/flutterfire/tree/main/packages/firebase_ai/firebase_ai/example) \| [Unity](https://github.com/firebase/quickstart-unity/tree/master/firebaseai/testapp)

### **Step 1** : Set parameter values in the Firebase console

Create a Remote Config client template and configure parameters and
values to fetch and use in the app.

> [!IMPORTANT]
> **Important:** While Remote Config can optionally be used for all the parameters described in this guide, we **strongly recommend using Remote Config for
> (at minimum) remotely changing the model name in your app** . See the [streamlined guide](https://firebase.google.com/docs/ai-logic/change-model-name-remotely) for this use case.

1. Open your Firebase project in the Firebase console. Then, from the
   navigation menu, expand **Run** and select
   [**Remote Config**](https://console.firebase.google.com/project/_/config).

2. Ensure that **Client** is selected from the **Client/Server** selector
   at the top of the page.

3. Start a client template by clicking **Create Configuration**
   (or **Add parameter** if you've previously used client templates).

4. Define the parameters you want to control with Remote Config. For
   example:

   | Parameter name | Description | Type | Default value |
   |---|---|---|---|
   | `model_name` | Model name. See [available model names](https://firebase.google.com/docs/ai-logic/models#available-model-names). | String | `gemini-2.5-flash` |
   | `system_instructions` | [System instructions](https://firebase.google.com/docs/ai-logic/system-instructions) are like a "preamble" that you add before the model gets exposed to any further instructions from the end user to influence model behavior. | String | `You are a helpful assistant who knows everything there is to know about Firebase!` |
   | `prompt` | Default prompt to use with your generative AI feature. | String | `I am a developer who wants to know more about Firebase!` |
   | `vertex_location` | *Only applicable if using Vertex AI Gemini API.* Control the [location](https://firebase.google.com/docs/ai-logic/locations) to access the model. You can set conditions to configure this option based on client location detected by Google Analytics. | String | `global` |

   > [!TIP]
   > **Tip:** After you've created a Remote Config parameter, you can dynamically or conditionally control it or use it for [A/B Testing](https://firebase.google.com/docs/ab-testing) or [feature rollouts](https://firebase.google.com/docs/remote-config/rollouts). For more ideas, see [Advanced and recommended use cases for Remote Config with generative AI apps](https://firebase.google.com/docs/remote-config/solutions/vertexai#advanced-use).

5. When you've finished adding parameters, click **Publish changes** . If this
   is not a new Remote Config template, review the changes and click
   **Publish changes** again.

### **Step 2** : Add and initialize Remote Config in your app

Add the Remote Config library and set up Remote Config within your app.

### Swift

As part of
[Firebase AI Logic setup](https://firebase.google.com/docs/ai-logic/get-started#add-sdk),
you've already added the Firebase SDK to your app, but will also need to add
Remote Config.

1. In Xcode, with the project open, navigate to **File \> Add Package
   Dependencies**.

2. Select **firebase-ios-sdk** and then click **Add package**.

3. From the Project navigator, select your app \> **Targets** \> your app.

4. From the **General** tab, scroll to **Frameworks, Libraries, and
   Embedded Content**.

5. Click **+** and choose **FirebaseRemoteConfig** , then click **Add**.

6. Add the `FirebaseRemoteConfig` import to your code:

       import FirebaseRemoteConfig

7. Inside the appropriate class for your app, initialize Firebase and add
   Remote Config to your main application logic.

   Here, you'll include Remote Config and the
   [Remote Config real-time listener](https://firebase.google.com/docs/remote-config/ios/real-time)
   as imports so that the app can fetch new values in real-time, and add a
   minimum fetch interval:

       let remoteConfig = RemoteConfig.remoteConfig()
       let settings = RemoteConfigSettings()
       settings.minimumFetchInterval = 3600
       remoteConfig.configSettings = settings

   In the
   [quickstart app](https://github.com/firebase/quickstart-ios/tree/main/vertexai),
   this would be inside `VertexAISampleApp`, within the `AppDelegate` class.

   > [!NOTE]
   > **Note:** In this example, the default fetch interval is 3600 seconds, but we recommend that you set a relatively low minimum fetch interval inside your code during development.

### Kotlin

1. Add the Remote Config dependency to your module (app-level) Gradle
   file (usually `app/build.gradle.kts` or `app/build.gradle`):

       dependencies {
           implementation(platform("com.google.firebase:firebase-bom:34.10.0"))
           implementation("com.google.firebase:firebase-ai")
           implementation("com.google.firebase:firebase-config")
           // ... other dependencies
       }

2. Add Remote Config to your main application logic. Here, you'll
   initialize Remote Config and add a minimum fetch interval:

       val remoteConfig: FirebaseRemoteConfig = Firebase.remoteConfig
       val configSettings = remoteConfigSettings {
       minimumFetchIntervalInSeconds = 3600
       }
       remoteConfig.setConfigSettingsAsync(configSettings)

   > [!NOTE]
   > **Note:** In this example, the default fetch interval is 3600 seconds, but we recommend that you set a relatively low minimum fetch interval inside your code during development.

### Java

1. Add the Remote Config dependency to your module (app-level) Gradle
   file (usually `app/build.gradle.kts` or `app/build.gradle`):

       dependencies {
           implementation(platform("com.google.firebase:firebase-bom:34.10.0"))
           implementation("com.google.firebase:firebase-ai")
           implementation("com.google.firebase:firebase-config")
           // ... other dependencies
       }

2. Add Remote Config to your main application logic. Here, you'll
   initialize Remote Config and add a minimum fetch interval:

       FirebaseRemoteConfig mFirebaseRemoteConfig = FirebaseRemoteConfig.getInstance();
       FirebaseRemoteConfigSettings configSettings = new FirebaseRemoteConfigSettings.Builder()
           .setMinimumFetchIntervalInSeconds(3600)
           .build();
       mFirebaseRemoteConfig.setConfigSettingsAsync(configSettings);

   > [!NOTE]
   > **Note:** In this example, the default fetch interval is 3600 seconds, but we recommend that you set a relatively low minimum fetch interval inside your code during development.

### Web

1. Open your code in a text editor and import Remote Config:

       import { getRemoteConfig } from 'firebase/remote-config';

2. Inside your primary function and after the Firebase app is initialized
   for Firebase AI Logic SDK, initialize Remote Config:

         // Initialize Remote Config and get a reference to the service
         const remoteConfig = getRemoteConfig(app);

3. Set a minimum fetch interval:

       remoteConfig.settings.minimumFetchIntervalMillis = 3600000;

   > [!NOTE]
   > **Note:** In this example, the default fetch interval is 3600 seconds, but we recommend that you set a relatively low minimum fetch interval inside your code during development.

### Dart

1. From your Flutter project directory, install and add Remote Config
   using the following command:

       flutter pub add firebase_remote_config

2. Open `./lib/main.dart` and add the import after the other imports you
   added to support Firebase AI Logic:

       import 'package:firebase_vertexai/firebase_ai.dart';
       import 'package:firebase_core/firebase_core.dart';
       import 'package:firebase_remote_config/firebase_remote_config.dart';

3. Add `_modelName`, `_systemInstructions`, and `_prompt` variables to
   your app so that you can use them later:

       late final String _modelName;
       late final String _systemInstructions;
       late final String _prompt;

4. Get the Remote Config object instance and set the minimum fetch
   interval to allow for frequent refreshes. Make sure to add this after
   Firebase is initialized.

         final remoteConfig = FirebaseRemoteConfig.instance;
         await remoteConfig.setConfigSettings(RemoteConfigSettings(
           fetchTimeout: const Duration(seconds: 3600),
           minimumFetchInterval: const Duration(seconds: 3600),
         ));

   > [!NOTE]
   > **Note:** In this example, the default fetch interval is 3600 seconds, but we recommend that you set a relatively low minimum fetch interval inside your code during development.

### Unity

1. Add Remote Config to your Unity project, following these
   [instructions](https://firebase.google.com/docs/unity/setup#add-sdks).

2. Get the Remote Config object instance and set the minimum fetch
   interval to allow for frequent refreshes. Make sure to add this after
   Firebase is initialized.

       var remoteConfig = FirebaseRemoteConfig.DefaultInstance;
       const int MillisecondsPerSecond = 1000;
       await remoteConfig.SetConfigSettingsAsync(new ConfigSettings() {
         FetchTimeoutInMilliseconds = 3600 * MillisecondsPerSecond,
         MinimumFetchIntervalInMilliseconds = 3600 * MillisecondsPerSecond
       });

   > [!NOTE]
   > **Note:** In this example, the default fetch interval is 3600 seconds, but we recommend that you set a relatively low minimum fetch interval inside your code during development.

### **Step 3**: Set in-app parameter values

You should set in-app default parameter values in the Remote Config
object. This ensures that your app behaves as expected even if it cannot
fetch values from the Remote Config service.

### Swift

1. In the Firebase console, open Remote Config.

2. In the
   [**Parameters**](https://console.firebase.google.com/project/_/config)
   tab, open the **Menu** , and select **Download default values**.

3. When prompted, enable **.plist for iOS** , then click **Download file**.

4. Save the file in the your application directory.

   If using the sample app, save it within
   `FirebaseVertexAI/Sample/VertexAISample`.
5. In Xcode, right-click on your app and select **Add Files**

   If using the sample, right-click on **VertexAISample** and select
   **Add Files to "VertexAISample"**.
6. Select **remote_config_defaults.plist** , then click **Add**.

7. Update your app code to reference the defaults file:

       // Set default values for Remote Config parameters.
       remoteConfig.setDefaults(fromPlist: "remote_config_defaults")

### Kotlin

1. From the Firebase console, open Remote Config.

2. In the
   [**Parameters**](https://console.firebase.google.com/project/_/config)
   tab, open the **Menu** , and select **Download default values**.

3. When prompted, enable **.xml for Android** , then click **Download file**.

4. Save the file in your app's XML resources directory.

5. Update your main activity file to add the defaults after the
   `configSettings` you added previously:

       // Set default values for Remote Config parameters.
       remoteConfig.setDefaultsAsync(R.xml.remote_config_defaults)

### Java

1. In the Firebase console, open Remote Config.

2. In the
   [**Parameters**](https://console.firebase.google.com/project/_/config)
   tab, open the **Menu** , and select **Download default values**.

3. When prompted, enable **.xml for Android** , then click **Download file**.

4. Save the file in your app's XML resources directory.

5. Update your main activity file to add the defaults after the
   `configSettings` you added previously:

       // Set default values for Remote Config parameters.
       mFirebaseRemoteConfig.setDefaultsAsync(R.xml.remote_config_defaults);

### Web

You can set the default values directly in your code:

    // Set default values for Remote Config parameters.
    remoteConfig.defaultConfig = {
      model_name: 'gemini-2.5-flash',
      system_instructions:
        'You are a helpful assistant who knows everything there is to know about Firebase!',
      prompt: 'I am a developer who wants to know more about Firebase!',
      vertex_location: 'global',
    };

### Dart

You can set the default values directly in your code:

    // Set default values for Remote Config parameters.
    remoteConfig.setDefaults(const {
      "model_name": "gemini-2.5-flash",
      "system_instructions": "You are a helpful assistant who knows everything there is to know about Firebase!",
      "prompt": "I am a developer who wants to know more about Firebase!",
      "vertex_location": "global"
    });

### Unity

You can set the default values directly in your code:

    // Set default values for Remote Config parameters.
    await remoteConfig.SetDefaultsAsync(
      new System.Collections.Generic.Dictionary<string, object>() {
        { "model_name", "gemini-2.5-flash" },
        { "system_instructions", "You are a helpful assistant who knows everything there is to know about Firebase!" },
        { "prompt", "I am a developer who wants to know more about Firebase!" },
        { "vertex_location", "global" }
      }
    );

### **Step 4**: Fetch and activate values

After setting defaults, add the following to fetch and activate values.

### Swift

    // Fetch and activate Remote Config values
    remoteConfig.fetchAndActivate { status, error in
      if let error = error {
        print("Error fetching Remote Config: \(error.localizedDescription)")
      }
    }

This should update the Remote Config object whenever a new
Remote Config template is published.

> [!IMPORTANT]
> **Important:** Be sure to put any code that depends on these values *after* fetch and activate.

### Kotlin

    // Fetch and activate Remote Config values
    remoteConfig.fetchAndActivate()
          .addOnCompleteListener(this) { task ->
              if (task.isSuccessful) {
                  val updated = task.result
                  Log.d(TAG, "Remote Config values fetched and activated: $updated")
              } else {
                  Log.e(TAG, "Error fetching Remote Config", task.exception)
              }
          }

> [!IMPORTANT]
> **Important:** Be sure to put any code that depends on these values *after* fetch and activate.

### Java

      // Fetch and activate Remote Config values
      mFirebaseRemoteConfig.fetchAndActivate()
        .addOnCompleteListener(this, new OnCompleteListener<Boolean>() {
            @Override
            public void onComplete(@NonNull Task<Boolean> task) {
                if (task.isSuccessful()) {
                    boolean updated = task.getResult();
                    Log.d(TAG, "Config params updated: " + updated);
                } else {
                    Log.e(TAG, "Error fetching Remote Config", task.exception)
                }
              }
        });

> [!IMPORTANT]
> **Important:** Be sure to put any code that depends on these values *after* fetch and activate.

### Web

1. Add `getValue` and `fetchAndActivate` to your imports:

       import { getValue, fetchAndActivate } from 'firebase/remote-config';

2. Locate the code where you specify default Remote Config values.
   Directly after that code block, add the following code to fetch and
   activate the config and assign values to the `modelName`,
   `systemInstructions`, `prompt`, and `vertexLocation` constants.

       // Fetch and activate Remote Config.
       try {
         await fetchAndActivate(remoteConfig);
       } catch(err) {
         console.error('Remote Config fetch failed', err);
       }

       console.log('Remote Config fetched.');

       // Assign Remote Config values.
       const modelName = getValue(remoteConfig, 'model_name').asString();
       const systemInstructions = getValue(remoteConfig, 'system_instructions').asString();
       const prompt = getValue(remoteConfig, 'prompt').asString();
       const vertexLocation = getValue(remoteConfig, 'vertex_location').asString();

> [!IMPORTANT]
> **Important:** Be sure to put any code that depends on these values *after* fetch and activate.

### Dart

    // Fetch and activate Remote Config.
    remoteConfig.fetchAndActivate();

    // Assign Remote Config values.
    String? _modelName = remoteConfig.getString("model_name");
    String? _systemInstructions = remoteConfig.getString("system_instructions");
    String? _prompt = remoteConfig.getString("prompt");
    String? _vertexLocation = remoteConfig.getString("vertex_location");

> [!IMPORTANT]
> **Important:** Be sure to put any code that depends on these values *after* fetch and activate.

### Unity

    // Fetch and activate Remote Config values.
    await remoteConfig.FetchAndActivateAsync();

> [!IMPORTANT]
> **Important:** Be sure to put any code that depends on these values *after* fetch and activate.

### **Step 5** : Add a real-time Remote Config listener

Add a [real-time Remote Config listener](https://firebase.google.com/docs/remote-config/ios/real-time)
to your app to ensure that changes you make to the Remote Config template
are propagated to the client as soon as they're updated.

The following code updates the Remote Config object whenever a parameter
value changes.

### Swift

    // Add real-time Remote Config
    remoteConfig.addOnConfigUpdateListener { configUpdate, error in
      guard let configUpdate = configUpdate, error == nil else {
        print("Error listening for config updates: \(error?.localizedDescription ?? "No error available")")
        return
      }

      print("Updated keys: \(configUpdate.updatedKeys)")
      remoteConfig.activate { changed, error in
        guard error == nil else {
          print("Error activating config: \(error?.localizedDescription ?? "No error available")")
          return
        }
        print("Activated config successfully")
      }
    }

### Kotlin

Optionally, you can also configure an action inside the
`addOnCompleteListener` activation:

          // Add a real-time Remote Config listener
          remoteConfig.addOnConfigUpdateListener(object : ConfigUpdateListener {
              override fun onUpdate(configUpdate : ConfigUpdate) {
                  Log.d(ContentValues.TAG, "Updated keys: " + configUpdate.updatedKeys);
                  remoteConfig.activate().addOnCompleteListener {
                      // Optionally, add an action to perform on update here.
                  }
              }

              override fun onError(error : FirebaseRemoteConfigException) {
                  Log.w(ContentValues.TAG, "Config update error with code: " + error.code, error)
              }
          }

### Java

Optionally, you can also configure an action inside the
`addOnCompleteListener` activation:

      // Add a real-time Remote Config listener
      remoteConfig.addOnConfigUpdateListener(new ConfigUpdateListener() {
          @Override
          public void onUpdate(ConfigUpdate configUpdate) {
              Log.d(ContentValues.TAG, "Updated keys: " + configUpdate.getUpdatedKeys());
                    remoteConfig.activate().addOnCompleteListener(new OnCompleteListener<Boolean>() {
                      @Override
                      public void onComplete(@NonNull Task<Boolean> task) {
                          // Optionally, add an action to perform on update here.
                      }
                  });
              }

          @Override
          public void onError(FirebaseRemoteConfigException error) {
              Log.w(ContentValues.TAG, "Config update error with code: " + error.getCode(), error);
          }
      });

### Web

     // Add a real-time Remote Config listener
     onConfigUpdate(remoteConfig, {
       next: (configUpdate) => {
          console.log("Updated keys:", configUpdate.getUpdatedKeys());
          if (configUpdate.getUpdatedKeys().has("welcome_message")) {
             activate(remoteConfig).then(() => {
             showWelcomeMessage();
             });
          }
       },
       error: (error) => {
          console.log("Config update error:", error);
       },
       complete: () => {
          console.log("Listening stopped.");
       }
    });

### Dart

    // Add a real-time Remote Config listener
    remoteConfig.onConfigUpdated.listen((event) async {
      await remoteConfig.activate();
    });

### Unity

    // Add a real-time Remote Config listener to automatically update whenever
    // a new template is published.
    // Note: the parameters can be anonymous as they are unused.

    remoteConfig.OnConfigUpdateListener += (_, _) => {
      remoteConfig.ActivateAsync();
    };

### **Step 6** : Update the Gemini API requests to use Remote Config values

|---|
| *Click your Gemini API provider to view provider-specific content and code on this page.* <button value="dev" default="">Gemini Developer API</button> <button value="vertex">Vertex AI Gemini API</button> |

Now that Remote Config is fully configured, update your code to replace
hard-coded values with values sourced from Remote Config.

> [!NOTE]
> **Note:** This example shows using Remote Config with a `GenerativeModel`, but it also works with an `ImagenModel` or `LiveModel`, as applicable.

### Swift

    // Initialize the Gemini Developer API backend service
    // The Gemini Developer API doesn't support setting the location of a model
    let ai = FirebaseAI.firebaseAI(backend: .googleAI())

    // Create a `GenerativeModel` and add system instructions into its config
    // Both the model name and the system instructions will be sourced from Remote Config
    let modelName = remoteConfig.configValue(forKey: "model_name").stringValue
    let systemInstructions = remoteConfig.configValue(forKey: "system_instructions").stringValue

    let model = ai.generativeModel(
      modelName: modelName,
      systemInstruction: ModelContent(role: "system", parts: systemInstructions)
    )

    // Provide a prompt that contains text
    // The text in the prompt will be sourced from Remote Config
    let userPrompt = remoteConfig.configValue(forKey: "prompt").stringValue

    // To generate text output, call `generateContent` with the text input
    let response = try await model.generateContent(userPrompt)
    if let text = response.text {
      print(text)
    }

### Kotlin

    // Initialize the Gemini Developer API backend service
    // The Gemini Developer API doesn't support setting the location of a model
    val ai = Firebase.ai(backend = GenerativeBackend.googleAI())

    // Create a `GenerativeModel` and add system instructions into its config
    // Both the model name and the system instructions will be sourced from Remote Config
    val model = ai.generativeModel(
      modelName = remoteConfig.getString("model_name"),
      systemInstruction = content { text(remoteConfig.getString("system_instructions")) }
    )

    // To generate text output, call `generateContent` with the text input
    // The text in the prompt will be sourced from Remote Config
    val response = model.generateContent(remoteConfig.getString("prompt"))
    print(response.text)

### Java

    // Initialize the Gemini Developer API backend service
    // The Gemini Developer API doesn't support setting the location of a model
    FirebaseAI ai = FirebaseAI.getInstance(GenerativeBackend.googleAI());

    // Create a `GenerativeModel` and add system instructions into its config
    // Both the model name and the system instructions will be sourced from Remote Config
    GenerativeModel gm = ai.generativeModel(
            /* modelName */ remoteConfig.getString("model_name"),
            /* generationConfig (optional) */ null,
            /* safetySettings (optional) */ null,
            /* tools (optional) */ null,
            /* toolsConfig (optional) */ null,
            /* systemInstruction (optional) */ new Content.Builder().addText(
                    remoteConfig.getString("system_instructions")).build(),
            /* requestOptions (optional) */ new RequestOptions()
    );
    GenerativeModelFutures model = GenerativeModelFutures.from(gm);

    // Provide a prompt that contains text
    // The text in the prompt will be sourced from Remote Config
    Content userPrompt = new Content.Builder()
            .addText(remoteConfig.getString("prompt"))
            .build();

    // To generate text output, call `generateContent` with the text input
    ListenableFuture<GenerateContentResponse> response = model.generateContent(userPrompt);
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

### Web

    // Initialize FirebaseApp
    const firebaseApp = initializeApp(firebaseConfig);

    // Initialize the Gemini Developer API backend service
    // The Gemini Developer API doesn't support setting the location of a model
    const ai = getAI(firebaseApp, { backend: new GoogleAIBackend() });

    // Create a `GenerativeModel` and add system instructions into its config
    // Both the model name and the system instructions will be sourced from Remote Config
    const model = getGenerativeModel(ai, {
      model: modelName,
      systemInstruction: systemInstruction
    });

    // Wrap in an async function so you can use await
    async function run() {
      // Provide a prompt that contains text
      // The text in the prompt will be sourced from Remote Config
      const userPrompt = prompt;

      // To generate text output, call `generateContent` with the text input
      const result = await model.generateContent(userPrompt);

      const response = result.response;
      const text = response.text();
      console.log(text);
    }

### Dart

    // Initialize the Gemini Developer API backend service
    // The Gemini Developer API doesn't support setting the location of a model
    final ai = await FirebaseAI.googleAI();

    // Create a `GenerativeModel` and add system instructions into its config
    // Both the model name and the system instructions will be sourced from Remote Config
    final model =
          ai.generativeModel(
            model: _modelName,
            systemInstruction: Content.system(_systemInstructions),
          );

    // Provide a prompt that contains text
    // The text in the prompt will be sourced from Remote Config
    final _userPrompt = [Content.text(_prompt)];

    // To generate text output, call `generateContent` with the text input
    final response = await model.generateContent(_userPrompt);
    print(response.text);

### Unity

    // Initialize the Gemini Developer API backend service
    // The Gemini Developer API doesn't support setting the location of a model
    var ai = FirebaseAI.GetInstance(FirebaseAI.Backend.GoogleAI());

    // Create a `GenerativeModel` and add system instructions into its config
    // Both the model name and the system instructions will be sourced from Remote Config
    var modelName = remoteConfig.GetValue("model_name").StringValue;
    var systemInstructions = remoteConfig.GetValue("system_instructions").StringValue;

    var model = ai.GetGenerativeModel(
      modelName: modelName,
      systemInstruction: ModelContent.Text(systemInstructions)
    );

    // Provide a prompt that contains text
    // The text in the prompt will be sourced from Remote Config
    var userPrompt = remoteConfig.GetValue("prompt").StringValue;

    // To generate text output, call `GenerateContentAsync` with the text input
    var response = await model.GenerateContentAsync(userPrompt);
    UnityEngine.Debug.Log(response.Text ?? "No text in response.");

### **Step 7**: Run the app

Build and run the app and verify that it works. Make changes to your
configuration from the Remote Config page in the Firebase console,
publish the changes, and verify the result.

### Next steps

- Learn more about [Remote Config](https://firebase.google.com/docs/remote-config).

- Add [Google Analytics](https://firebase.google.com/docs/analytics/get-started)
  to your client code to enable targeting.

- For mobile apps and games:

  - Test different model settings with
    [Remote Config and A/B Testing](https://firebase.google.com/docs/ab-testing/abtest-config).

  - Gradually release model parameter changes using
    [Remote Config rollouts](https://firebase.google.com/docs/remote-config/rollouts) (iOS+ and Android only).

  - Use [Remote Config personalization](https://firebase.google.com/docs/remote-config/personalization)
    to use machine learning to determine the best settings for individual
    users (iOS+, Android, and Unity only).