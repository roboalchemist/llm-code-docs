# Source: https://firebase.google.com/docs/ai-logic/change-model-name-remotely.md.txt

The availability of generative AI models frequently changes --- new, better
models are released and older, less capable models are retired.

When you access generative AI models directly from a mobile or web app using
Firebase AI Logic, it's critical that you configure your app to accommodate
these frequent model changes. Not all of your users will update to the latest
version of your app to start using the model you need them to use.

[Firebase Remote Config](https://firebase.google.com/docs/remote-config) lets you update parameter
values in your app (like a model name) dynamically and remotely from the
Firebase console, without the need to release a new version of your app.

> [!CAUTION]
> We **strongly recommend implementing
> Firebase Remote Config into your app as early as possible**, even during development, so that you can update the model name remotely in every version of your app.

Note that changing a model name is a *critical* use case for using
Remote Config with Firebase AI Logic, but you can also
[use Remote Config to dynamically and even conditionally control parameters in your app](https://firebase.google.com/docs/ai-logic/solutions/remote-config),
like model generation configuration (maximum tokens, temperature, etc.),
safety settings, system instructions, and prompt data.

This guide describes how to implement Remote Config in your app,
specifically to control the model name used in your app.

### **Step 1** : Set the parameter value in the Firebase console

Create a Remote Config client template and configure a `model_name`
parameter and its value to fetch and use in the app.

1. Open your Firebase project in the Firebase console. Then, from the
   navigation menu, expand **Run** and select
   [**Remote Config**](https://console.firebase.google.com/project/_/config).

2. Ensure that **Client** is selected from the **Client/Server** selector
   at the top of the page.

3. Start a client template by clicking **Create Configuration**
   (or **Add parameter** if you've previously used client templates).

4. Define the `model_name` parameter:

   | Parameter name | Description | Type | Default value |
   |---|---|---|---|
   | `model_name` | Model name. See [available model names](https://firebase.google.com/docs/ai-logic/models#available-model-names). | String | `gemini-2.5-flash` |

5. After adding this parameter, click **Publish changes** . If this
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

3. Add the `_modelName` variable to
   your app so that you can use it later:

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

### **Step 3**: Set the in-app parameter value

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

5. In Xcode, right-click on your app and select **Add Files**

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

You can set the default value for the model name directly in your code:

    // Set default values for Remote Config parameters.
    remoteConfig.defaultConfig = {
      model_name: 'gemini-2.5-flash',
    };

### Dart

You can set the default value for the model name directly in your code:

    // Set default values for Remote Config parameters.
    remoteConfig.setDefaults(const {
      "model_name": "gemini-2.5-flash"
    });

### Unity

You can set the default value for the model name directly in your code:

    // Set default values for Remote Config parameters.
    await remoteConfig.SetDefaultsAsync(
      new System.Collections.Generic.Dictionary<string, object>() {
        { "model_name", "gemini-2.5-flash" }
      }
    );

### **Step 4**: Fetch and activate the value

After setting the default value for the model name, add the following to fetch
and activate values.

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

2. Locate the code where you specify the default value for the model name.
   Directly after that code block, add the following code to fetch and
   activate the config and assign the fetched value to the `modelName`
   constant.

       // Fetch and activate Remote Config.
       try {
         await fetchAndActivate(remoteConfig);
       } catch(err) {
         console.error('Remote Config fetch failed', err);
       }

       console.log('Remote Config fetched.');

       // Assign Remote Config values.
       const modelName = getValue(remoteConfig, 'model_name').asString();

> [!IMPORTANT]
> **Important:** Be sure to put any code that depends on these values *after* fetch and activate.

### Dart

    // Fetch and activate Remote Config.
    remoteConfig.fetchAndActivate();

    // Assign Remote Config values.
    String? _modelName = remoteConfig.getString("model_name");

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

### **Step 6** : Update the Gemini API requests to use the Remote Config value

|---|
| *Click your Gemini API provider to view provider-specific content and code on this page.* <button value="dev" default="">Gemini Developer API</button> <button value="vertex">Vertex AI Gemini API</button> |

Now that Remote Config is fully configured, update your code to replace
hard-coded values with values sourced from Remote Config.

> [!NOTE]
> **Note:** This example shows using Remote Config with a `GenerativeModel`, but it also works with an `ImagenModel` or `LiveModel`, as applicable.

### Swift

    import FirebaseAI

    // When creating a `GenerativeModel` instance, source the model name value from Remote Config
    let modelName = remoteConfig.configValue(forKey: "model_name").stringValue
    let model = FirebaseAI.firebaseAI(backend: .googleAI()).generativeModel(
      modelName: modelName
    )

    // ...

### Kotlin

    // When creating a `GenerativeModel` instance, source the model name value from Remote Config
    val model = Firebase.ai(backend = GenerativeBackend.googleAI()).generativeModel(
      modelName = remoteConfig.getString("model_name")
    )

    // ...

### Java

    // When creating a `GenerativeModel` instance, source the model name value from Remote Config
    GenerativeModel ai = FirebaseAI.getInstance(GenerativeBackend.googleAI())
        .generativeModel(
          /* modelName */ remoteConfig.getString("model_name"),
          /* generationConfig (optional) */ null,
          /* safetySettings (optional) */ null,
          /* requestOptions (optional) */ new RequestOptions(),
          /* tools (optional) */ null,
          /* toolsConfig (optional) */ null,
          /* systemInstruction (optional) */ null,
        );

    GenerativeModelFutures model = GenerativeModelFutures.from(ai);

    // ...

### Web

    // ...

    const ai = getAI(firebaseApp, { backend: new GoogleAIBackend() });

    // When creating a `GenerativeModel` instance, source the model name value from Remote Config
    const model = getGenerativeModel(ai, {
      model: modelName
    });

    // ...

### Dart

    // ...

    // When creating a `GenerativeModel` instance, source the model name value from Remote Config
    final model = FirebaseAI.googleAI().generativeModel(
      model: _modelName,
    );

    // ...

### Unity

    // ...

    var ai = FirebaseAI.GetInstance(FirebaseAI.Backend.GoogleAI());

    // When creating a `GenerativeModel` instance, source the model name value from Remote Config
    var modelName = remoteConfig.GetValue("model_name").StringValue;
    var model = ai.GetGenerativeModel(
      modelName: modelName
    );

    // ...

### **Step 7**: Run the app

Build and run the app and verify that it works. Make changes to your
configuration from the Remote Config page in the Firebase console,
publish the changes, and verify the result.

### Next steps

- Learn more about implementing other
  [use cases for Remote Config and Firebase AI Logic](https://firebase.google.com/docs/ai-logic/solutions/remote-config).

- For mobile apps and games:

  - Test different model settings with
    [Remote Config and A/B Testing](https://firebase.google.com/docs/ab-testing/abtest-config).

  - Gradually release model parameter changes using
    [Remote Config rollouts](https://firebase.google.com/docs/remote-config/rollouts) (iOS+ and Android only).

  - Use [Remote Config personalization](https://firebase.google.com/docs/remote-config/personalization)
    to use machine learning to determine the best settings for individual
    users (iOS+, Android, and Unity only).