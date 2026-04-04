# Source: https://firebase.google.com/docs/remote-config/cpp/get-started.md.txt

|---|---|
| **Select platform:** | [iOS+](https://firebase.google.com/docs/remote-config/ios/get-started) [Android](https://firebase.google.com/docs/remote-config/android/get-started) [Web](https://firebase.google.com/docs/remote-config/web/get-started) [Flutter](https://firebase.google.com/docs/remote-config/flutter/get-started) [Unity](https://firebase.google.com/docs/remote-config/unity/get-started) [C++](https://firebase.google.com/docs/remote-config/cpp/get-started) |

<br />

You can use Firebase Remote Config to define parameters in your app and
update their values in the cloud, allowing you to modify the appearance and
behavior of your app without distributing an app update.

The Remote Config library is used to store in-app default parameter values,
fetch updated parameter values from the Remote Config backend, and
control when fetched values are made available to your app. To learn more,
see [Remote Config loading strategies](https://firebase.google.com/docs/remote-config/loading).

## Step 1: Add Firebase to your app

Before you can use
[Remote Config](https://firebase.google.com/docs/reference/unity/namespace/firebase/remote-config),
you need to:

- Register your C++ project and configure it to use Firebase.

  If your C++ project already uses Firebase, then it's already registered and
  configured for Firebase.
- Add the [Firebase C++ SDK](https://firebase.google.com/download/cpp) to your C++ project.

> [!NOTE]
> **Find detailed instructions for these initial
> setup tasks in
> [Add Firebase to your C++
> project](https://firebase.google.com/docs/cpp/setup#note-select-platform).**

Note that adding Firebase to your C++ project involves tasks both in the
[Firebase console](https://console.firebase.google.com/) and in your open C++ project (for example, you download
Firebase config files from the console, then move them into your C++ project).

## Step 2: Add Remote Config to your app

### Android

After you've added Firebase to your app:

1. Create a Firebase App, passing in the JNI environment and Activity:

   ```c++
   app = ::firebase::App::Create(::firebase::AppOptions(), jni_env, activity);
   ```

   <br />

2. Initialize the Remote Config library, as shown:

   ```c++
   ::firebase::remote_config::Initialize(app);
   ```

   <br />

### iOS+

After you've added Firebase to your app:

1. Create a Firebase App:

   ```c++
   app = ::firebase::App::Create(::firebase::AppOptions());
   ```

   <br />

2. Initialize the Remote Config library, as shown:

   ```c++
   ::firebase::remote_config::Initialize(app);
   ```

   <br />

## Step 3: Set in-app default parameter values

You can set in-app default parameter values in the Remote Config
object, so that your app behaves as intended before it connects to the
Remote Config backend, and so that default values are available if none are
set on the backend.

> [!IMPORTANT]
> **Important:** Don't store confidential data in Remote Config parameter keys or values. Remote Config data is encrypted in transit, but end users can access any default or fetched Remote Config parameter that is available to their client app instance.

1. Define a set of parameter names, and default parameter values using a
   [`ConfigKeyValue*`](https://firebase.google.com/docs/reference/cpp/struct/firebase/remote-config/config-key-value)
   object or a
   [`ConfigKeyValueVariant*`](https://firebase.google.com/docs/reference/cpp/struct/firebase/remote-config/config-key-value-variant)
   object with the size of the array.

   If you have already configured Remote Config backend parameter
   values, you can download a file that contains these key-value pairs and use
   it to construct your `map` object. For more information, see
   [Download
   Remote Config template defaults](https://firebase.google.com/docs/remote-config/templates#download_template_defaults).
2. Add these values to the Remote Config object using
   [`SetDefaults()`](https://firebase.google.com/docs/reference/cpp/namespace/firebase/remote-config#setdefaults).

## Step 4: Get parameter values to use in your app

Now you can get parameter values from the Remote Config object. If you set
values in the Remote Config backend, fetched them, and then activated them,
those values are available to your app. Otherwise, you get the in-app parameter
values configured using
[`SetDefaults()`](https://firebase.google.com/docs/reference/cpp/namespace/firebase/remote-config#setdefaults).

To get these values, call any of the following methods that map to the data type
expected by your app, providing the parameter key as an argument:

- [`GetBoolean()`](https://firebase.google.com/docs/reference/cpp/namespace/firebase/remote-config#getboolean)
- [`GetData()`](https://firebase.google.com/docs/reference/cpp/namespace/firebase/remote-config#getdata)
- [`GetDouble()`](https://firebase.google.com/docs/reference/cpp/namespace/firebase/remote-config#getdouble)
- [`GetLong()`](https://firebase.google.com/docs/reference/cpp/namespace/firebase/remote-config#getlong)
- [`GetString()`](https://firebase.google.com/docs/reference/cpp/namespace/firebase/remote-config#getstring)

## Step 5: Set parameter values

1. In the [Firebase console](https://console.firebase.google.com/), open your project.
2. Select **Remote Config** from the menu to view the Remote Config dashboard.
3. Define parameters with the same names as the parameters that you defined in your app. For each parameter, you can set a default value (which will eventually override the in-app default value) and conditional values. To learn more, see [Remote Config parameters and conditions](https://firebase.google.com/docs/remote-config/cpp/parameters).

## Step 6: Fetch and activate values

1. To fetch parameter values from the Remote Config backend, call the [`Fetch()`](https://firebase.google.com/docs/reference/cpp/namespace/firebase/remote-config#fetch) method. Any values that you set on the backend are fetched and cached in the Remote Config object.
2. To make fetched parameter values available to your app, call the [`ActivateFetched()`](https://firebase.google.com/docs/reference/cpp/namespace/firebase/remote-config#activatefetched)

## Step 7: Listen for updates in real time

After you fetch parameter values, you can use real-time Remote Config to
listen for updates from the Remote Config backend. Real-time
Remote Config signals to connected devices when updates are available and
automatically fetches the changes after you publish a new Remote Config
version.

Real-time updates are supported by the Firebase C++ SDK
v11.0.0+ and higher for Android and Apple platforms.

> [!NOTE]
> **Important:** Real-time Remote Config also requires the
> Firebase Remote Config
> Realtime API, which should already be enabled for you. To verify, open the
> [Google Cloud console](https://console.developers.google.com/apis/api/firebaseremoteconfigrealtime.googleapis.com/overview),
> select your project, and open the **APIs and Services** page. The API
> should appear as enabled. If it's missing or not enabled, click **Enable
> APIs \& Services** , search for **Firebase Remote Config Realtime
> API**, and enable it.

1. In your app, call `AddOnConfigUpdateListener` to start listening for updates and automatically fetch any new or updated parameter values. The following example listens for updates and, when `Activate` is called, uses the newly fetched values to display an updated welcome message.

```c++
remote_config->AddOnConfigUpdateListener(
    [](firebase::remote_config::ConfigUpdate&& config_update,
       firebase::remote_config::RemoteConfigError remote_config_error) {
      if (remote_config_error != firebase::remote_config::kRemoteConfigErrorNone) {
        printf("Error listening for config updates: %d", remote_config_error);
      }
      // Search the `updated_keys` set for the key "welcome_message."
      // `updated_keys` represents the keys that have changed since the last
      // fetch.
      if (std::find(config_update.updated_keys.begin(),
                    config_update.updated_keys.end(),
                    "welcome_message") != config_update.updated_keys.end()) {
        remote_config->Activate().OnCompletion(
            [&](const firebase::Future& completed_future,
               void* user_data) {
              // The key "welcome_message" was found within `updated_keys` and
              // can be activated.
              if (completed_future.error() == 0) {
                DisplayWelcomeMessage();
              } else {
                printf("Error activating config: %d", completed_future.error());
              }
            },
            nullptr);
      }
    });
```

The next time you publish a new version of your Remote Config, devices
that are running your app and listening for changes will call the config
update listener.