# Source: https://firebase.google.com/docs/remote-config/unity/get-started.md.txt

|---|---|
| **Select platform:** | [iOS+](https://firebase.google.com/docs/remote-config/ios/get-started) [Android](https://firebase.google.com/docs/remote-config/android/get-started) [Web](https://firebase.google.com/docs/remote-config/web/get-started) [Flutter](https://firebase.google.com/docs/remote-config/flutter/get-started) [Unity](https://firebase.google.com/docs/remote-config/unity/get-started) [C++](https://firebase.google.com/docs/remote-config/cpp/get-started) |

<br />

You can use Firebase Remote Config to define parameters in your app and
update their values in the cloud, allowing you to modify the appearance and
behavior of your app without distributing an app update.

The Remote Config library is used to store in-app default parameter values,
fetch updated parameter values from the Remote Config backend, and control
when fetched values are made available to your app. To learn more, see [Remote
Config loading strategies](https://firebase.google.com/docs/remote-config/loading).

This guide walks you through the steps to get started and provides some sample
code, all of which is available to clone or download from the
[firebase/quickstart-unity](https://github.com/firebase/quickstart-unity/tree/master) GitHub repository.

## Step 1: Add Remote Config to your app

Before you can use
[Remote Config](https://firebase.google.com/docs/reference/unity/namespace/firebase/remote-config),
you need to:

- Register your Unity project and configure it to use Firebase.

  - If your Unity project already uses Firebase, then it's already
    registered and configured for Firebase.

  - If you don't have a Unity project, you can download a
    [sample app](https://github.com/google/mechahamster).

- Add the [Firebase Unity SDK](https://firebase.google.com/download/unity) (specifically, `FirebaseRemoteConfig.unitypackage`) to
  your Unity project.

> [!NOTE]
> **Find detailed instructions for these initial
> setup tasks in
> [Add Firebase to your Unity project](https://firebase.google.com/docs/unity/setup#prerequisites).**

Note that adding Firebase to your Unity project involves tasks both in the
[Firebase console](https://console.firebase.google.com/) and in your open Unity project
(for example, you download Firebase config files from the console, then move
them into your Unity project).

## Step 2: Set in-app default parameter values

You can set in-app default parameter values in the Remote Config
object, so that your app behaves as intended before it connects to the
Remote Config backend, and so that default values are available if none are
set in the backend.

> [!IMPORTANT]
> **Important:** Don't store confidential data in Remote Config parameter keys or values. Remote Config data is encrypted in transit, but end users can access any default or fetched Remote Config parameter that is available to their client app instance.

To do this, create a string dictionary, and populate it with key-value pairs
representing the defaults you want to add. If you have already configured
Remote Config backend parameter values, you can download a file that
contains these key-value pairs and use it to construct your string dictionary.
For more information, see
[Download
Remote Config template defaults](https://firebase.google.com/docs/remote-config/templates#download_template_defaults).

(Non-string properties will be converted to the property's type when
`SetDefaultsAsync()` is called).

```c#
System.Collections.Generic.Dictionary<string, object> defaults =
  new System.Collections.Generic.Dictionary<string, object>();

// These are the values that are used if we haven't fetched data from the
// server
// yet, or if we ask for values that the server doesn't have:
defaults.Add("config_test_string", "default local string");
defaults.Add("config_test_int", 1);
defaults.Add("config_test_float", 1.0);
defaults.Add("config_test_bool", false);

Firebase.RemoteConfig.FirebaseRemoteConfig.DefaultInstance.SetDefaultsAsync(defaults)
  .ContinueWithOnMainThread(task => {
```

## Step 3: Get parameter values to use in your app

Now you can get parameter values from the Remote Config object. If you set
values in the Remote Config backend, fetched them, and then activated them,
those values are available to your app. Otherwise, you get the in-app parameter
values configured using
[`SetDefaultsAsync()`](https://firebase.google.com/docs/reference/unity/class/firebase/remote-config/firebase-remote-config#setdefaultsasync).

To get these values, use
[`GetValue()`](https://firebase.google.com/docs/reference/unity/class/firebase/remote-config/firebase-remote-config#getvalue),
providing the parameter key as an argument. This returns a
[`ConfigValue`](https://firebase.google.com/docs/reference/unity/struct/firebase/remote-config/config-value),
which has properties to convert the value into various base types.

## Step 4: Set parameter values

1. In the [Firebase console](https://console.firebase.google.com/), open your project.
2. Select **Remote Config** from the menu to view the Remote Config dashboard.
3. Define parameters with the same names as the parameters that you defined in your app. For each parameter, you can set a default value (which will eventually override the in-app default value) and conditional values. To learn more, see [Remote Config parameters and conditions](https://firebase.google.com/docs/remote-config/unity/parameters).

## Step 5: Fetch and activate values (as needed)

To fetch parameter values from the Remote Config backend, call the
[`FetchAsync()`](https://firebase.google.com/docs/reference/unity/class/firebase/remote-config/firebase-remote-config#fetchasync_1)
method. Any values that you set on the backend are fetched and cached in the
Remote Config object.

```c#
// Start a fetch request.
// FetchAsync only fetches new data if the current data is older than the provided
// timespan.  Otherwise it assumes the data is "recent enough", and does nothing.
// By default the timespan is 12 hours, and for production apps, this is a good
// number. For this example though, it's set to a timespan of zero, so that
// changes in the console will always show up immediately.
public Task FetchDataAsync() {
  DebugLog("Fetching data...");
  System.Threading.Tasks.Task fetchTask =
  Firebase.RemoteConfig.FirebaseRemoteConfig.DefaultInstance.FetchAsync(
      TimeSpan.Zero);
  return fetchTask.ContinueWithOnMainThread(FetchComplete);
}
```

In the previous code, `FetchComplete` is a method whose signature matches the
parameters of one of the
[overloads](https://firebase.google.com/docs/reference/unity/class/firebase/extensions/task-extension)
of `ContinueWithOnMainThread()`.

In the sample code that follows, the `FetchComplete` method is passed the
previous task (`fetchTask`), which allows `FetchComplete` to determine whether
it finished. The code uses
[`Info.LastFetchStatus`](https://firebase.google.com/docs/reference/unity/class/firebase/remote-config/config-info#lastfetchstatus)
to then determine whether the finish was *also* successful. If so,
Remote Config parameter values are then activated using `ActivateAsync()`.

    private void FetchComplete(Task fetchTask) {
      if (!fetchTask.IsCompleted) {
        Debug.LogError("Retrieval hasn't finished.");
        return;
      }

      var remoteConfig = FirebaseRemoteConfig.DefaultInstance;
      var info = remoteConfig.Info;
      if(info.LastFetchStatus != LastFetchStatus.Success) {
        Debug.LogError($"{nameof(FetchComplete)} was unsuccessful\n{nameof(info.LastFetchStatus)}: {info.LastFetchStatus}");
        return;
      }

      // Fetch successful. Parameter values must be activated to use.
      remoteConfig.ActivateAsync()
        .ContinueWithOnMainThread(
          task => {
            Debug.Log($"Remote data loaded and ready for use. Last fetch time {info.FetchTime}.");
        });
    }

Values fetched using
[`FetchAsync()`](https://firebase.google.com/docs/reference/unity/class/firebase/remote-config/firebase-remote-config#fetchasync_1)
are cached locally when the fetch completes, but are not made available until
[`ActivateAsync()`](https://firebase.google.com/docs/reference/unity/class/firebase/remote-config/firebase-remote-config#activateasync)
is invoked. This lets you ensure that the new values are not applied
mid-calculation, or at other times that might cause problems or strange
behavior.

## Step 6: Listen for updates in real time

After you fetch parameter values, you can use real-time Remote Config to
listen for updates from the Remote Config backend. Real-time
Remote Config signals to connected devices when updates are available and
automatically fetches the changes after you publish a new Remote Config
version.

Real-time updates are supported by the Firebase Unity SDK v11.0.0+ and higher for
Android and Apple platforms.

> [!NOTE]
> **Important:** Real-time Remote Config also requires the
> Firebase Remote Config
> Realtime API, which should already be enabled for you. To verify, open the
> [Google Cloud console](https://console.developers.google.com/apis/api/firebaseremoteconfigrealtime.googleapis.com/overview),
> select your project, and open the **APIs and Services** page. The API
> should appear as enabled. If it's missing or not enabled, click
> **Enable APIs \& Services** , search for
> **Firebase Remote Config Realtime API**, and then enable it.

1. In your app, add an `OnConfigUpdateListener` to start listening for updates and automatically fetch any new or updated parameter values. Then, create a `ConfigUpdateListenerEventHandler` to process update events. The following example listens for updates and uses the newly fetched values to display an updated welcome message.

```c#
// Invoke the listener.
void Start()
{
  Firebase.RemoteConfig.FirebaseRemoteConfig.DefaultInstance.OnConfigUpdateListener
    += ConfigUpdateListenerEventHandler;
}

// Handle real-time Remote Config events.
void ConfigUpdateListenerEventHandler(
   object sender, Firebase.RemoteConfig.ConfigUpdateEventArgs args) {
  if (args.Error != Firebase.RemoteConfig.RemoteConfigError.None) {
    Debug.Log(String.Format("Error occurred while listening: {0}", args.Error));
    return;
  }

  Debug.Log("Updated keys: " + string.Join(", ", args.UpdatedKeys));
  // Activate all fetched values and then display a welcome message.
  remoteConfig.ActivateAsync().ContinueWithOnMainThread(
    task => {
        DisplayWelcomeMessage();
    });
}

// Stop the listener.
void OnDestroy() {
    Firebase.RemoteConfig.FirebaseRemoteConfig.DefaultInstance.OnConfigUpdateListener
      -= ConfigUpdateListenerEventHandler;
}
```

The next time you publish a new version of your Remote Config, devices that
are running your app and listening for changes will call the completion handler.