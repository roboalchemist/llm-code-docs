# Source: https://firebase.google.com/docs/remote-config/web/get-started.md.txt

# Get started with Remote Config on Web

|---|---|
| **Select platform:** | [iOS+](https://firebase.google.com/docs/remote-config/ios/get-started) [Android](https://firebase.google.com/docs/remote-config/android/get-started) [Web](https://firebase.google.com/docs/remote-config/web/get-started) [Flutter](https://firebase.google.com/docs/remote-config/flutter/get-started) [Unity](https://firebase.google.com/docs/remote-config/unity/get-started) [C++](https://firebase.google.com/docs/remote-config/cpp/get-started) |

<br />

You can use Firebase Remote Config to define parameters in your app and
update their values in the cloud, allowing you to modify the appearance and
behavior of your app without distributing an app update. This guide walks you
through the steps to get started and provides some sample code, all of which is
available to clone or download from the
[firebase/quickstart-js](https://github.com/firebase/quickstart-js/tree/master)
GitHub repository.

## Step 1: Add and initialize the Remote Config SDK

> [!NOTE]
> **Note:** When installing the SDK, you have the option of adding the dependency for Analytics. Analytics is *required* for Remote Config's [conditional
> targeting of app instances](https://firebase.google.com/docs/remote-config/parameters#condition_rule_types) to user properties and audiences.

1. If you haven't already, [install the Firebase JS SDK and initialize Firebase](https://firebase.google.com/docs/web/setup#add-sdk-and-initialize).

2. Add the Remote Config JS SDK and initialize Remote Config:

### Web


> [!NOTE]
> [Learn more](https://firebase.google.com/docs/web/learn-more#modular-version) about the tree-shakeable modular web API and [upgrade](https://firebase.google.com/docs/web/modular-upgrade) from the namespaced API.

<br />

```
import { initializeApp } from "firebase/app";
import { getRemoteConfig } from "firebase/remote-config";

// TODO: Replace the following with your app's Firebase project configuration
// See: https://firebase.google.com/docs/web/learn-more#config-object
const firebaseConfig = {
  // ...
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);


// Initialize Remote Config and get a reference to the service
const remoteConfig = getRemoteConfig(app);
```

### Web


> [!NOTE]
> [Learn more](https://firebase.google.com/docs/web/learn-more#modular-version) about the tree-shakeable modular web API and [upgrade](https://firebase.google.com/docs/web/modular-upgrade) from the namespaced API.

<br />

```
import firebase from "firebase/compat/app";
import "firebase/compat/remote-config";

// TODO: Replace the following with your app's Firebase project configuration
// See: https://firebase.google.com/docs/web/learn-more#config-object
const firebaseConfig = {
  // ...
};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);


// Initialize Remote Config and get a reference to the service
const remoteConfig = firebase.remoteConfig();
```

This object is used to store in-app default parameter values, fetch updated
parameter values from the Remote Config backend, and control when fetched
values are made available to your app.

## Step 2: Set minimum fetch interval

During development, it's recommended to set a relatively low minimum fetch
interval. See [Throttling](https://firebase.google.com/docs/remote-config/web/get-started#throttling) for
more information.

### Web

```javascript
// The default and recommended production fetch interval for Remote Config is 12 hours
remoteConfig.settings.minimumFetchIntervalMillis = 3600000;
```

### Web

```javascript
remoteConfig.settings.minimumFetchIntervalMillis = 3600000;
```

## Step 3: Set in-app default parameter values

You can set in-app default parameter values in the Remote Config
object, so that your app behaves as intended before it connects to the
Remote Config backend, and so that default values are available if none are
set on the backend.

> [!IMPORTANT]
> **Important:** Don't store confidential data in Remote Config parameter keys or values. Remote Config data is encrypted in transit, but end users can access any default or fetched Remote Config parameter that is available to their client app instance.

### Web

```javascript
remoteConfig.defaultConfig = {
  "welcome_message": "Welcome"
};
```

### Web

```javascript
remoteConfig.defaultConfig = {
  "welcome_message": "Welcome"
};
```

If you have already configured Remote Config backend parameter values, you
can download a generated JSON file that includes all default values and include
it in your app bundle:

### REST

```
curl --compressed -D headers -H "Authorization: Bearer token" -X GET https://firebaseremoteconfig.googleapis.com/v1/projects/my-project-id/remoteConfig:downloadDefaults?format=JSON -o remote_config_defaults.json
```

You can generate a bearer token by running the following command using the
[Google Cloud CLI](https://cloud.google.com/sdk/docs/install) or [Cloud
Shell](https://cloud.google.com/shell/docs/run-gcloud-commands):

    gcloud auth print-access-token

This token is short-lived, so you may need to regenerate it if you get an
authentication error.

### Firebase console

1. In the [Parameters](https://console.firebase.google.com/project/_/config) tab, open the **Menu** , and select **Download default values**.
2. When prompted, enable **.json for web** , then click **Download file**.

The following examples show two different ways you could import and set default
values in your app. The first example uses `fetch`, which will make an HTTP
request to the defaults file included in your app bundle:

```
  const rcDefaultsFile = await fetch('remote_config_defaults.json');
  const rcDefaultsJson = await rcDefaultsFile.json();
  remoteConfig.defaultConfig = rcDefaultsJson;
  
```

The next example uses `require`, which compiles the values into your app at
build time:

```
  let rcDefaults = require('./remote_config_defaults.json');
  remoteConfig.defaultConfig = rcDefaults;
```

## Step 4: Get parameter values to use in your app

Now you can get parameter values from the Remote Config object. If you later
set values in the backend, fetch them, and then activate them, those values are
available to your app.To get these values, call the
[`getValue()`](https://firebase.google.com/docs/reference/js/remote-config#getvalue) method, providing the
parameter key as an argument.

### Web

```javascript
import { getValue } from "firebase/remote-config";

const val = getValue(remoteConfig, "welcome_messsage");
```

### Web

```javascript
const val = remoteConfig.getValue("welcome_messsage");
```

## Step 5: Set parameter values

Using the Firebase console or the [Remote Config backend
APIs](https://firebase.google.com/docs/remote-config/automate-rc), you can create new server-side default
values that override the in-app values according to your desired conditional
logic or user targeting. This section walks you through the Firebase console
steps to create these values.

1. In the [Firebase console](https://console.firebase.google.com/), open your project.
2. Select **Remote Config** from the menu to view the Remote Config dashboard.
3. Define parameters with the same names as the parameters that you defined in your app. For each parameter, you can set a default value (which will eventually override the in-app default value) and you can also set conditional values. To learn more, see [Remote Config Parameters and
   Conditions](https://firebase.google.com/docs/remote-config/web/parameters).
4. If using [custom signal
   conditions](https://firebase.google.com/docs/remote-config/parameters?template_type=client#custom_signal_conditions),
   define the attributes and their values. The following example shows how to
   define a custom signal condition.

   ```
     let customSignals = {
        "city": "Tokyo",
        "preferred_event_category": "sports"
     }

     setCustomSignals(config, customSignals);
   ```

## Step 6: Fetch and activate values

1. To fetch parameter values from the Remote Config backend, call the [`fetchConfig()`](https://firebase.google.com/docs/reference/js/remote-config#fetchconfig) method. Any values that you set on the backend are fetched and cached in the Remote Config object.
2. To make fetched parameter values available to your app, call the [`activate()`](https://firebase.google.com/docs/reference/js/remote-config#activate) method.

For cases where you want to fetch and activate values in one call, use
[`fetchAndActivate()`](https://firebase.google.com/docs/reference/js/remote-config#fetch-and-activate) as
shown in this example:

### Web

```javascript
import { fetchAndActivate } from "firebase/remote-config";

fetchAndActivate(remoteConfig)
  .then(() => {
    // ...
  })
  .catch((err) => {
    // ...
  });
```

### Web

```javascript
remoteConfig.fetchAndActivate()
  .then(() => {
    // ...
  })
  .catch((err) => {
    // ...
  });
```

Because these updated parameter values affect the behavior and appearance of
your app, you should activate the fetched values at a time that ensures a smooth
experience for your user, such as the next time that the user opens your app.
See [Remote Config loading strategies](https://firebase.google.com/docs/remote-config/loading) for more
information and examples.

## Step 7: Listen for updates in real time

After you fetch parameter values, you can use real-time Remote Config to
listen for updates from the Remote Config backend. Real-time
Remote Config signals to connected devices when updates are available and
automatically fetches the changes after you publish a new Remote Config
version.

> [!NOTE]
> **Important:** Real-time Remote Config also requires the
> Firebase Remote Config
> Realtime API, which should already be enabled for you. To verify, open the
> [Google Cloud console](https://console.developers.google.com/apis/api/firebaseremoteconfigrealtime.googleapis.com/overview),
> select your project, and open the **APIs and Services** page. The API should
> appear as enabled. If it's missing or not enabled, click **Enable APIs \&
> Services** , search for **Firebase Remote Config Realtime API**, and
> enable it.

1. In your app, use `onConfigUpdate` to start listening for updates and
   automatically fetch any new parameter values. Implement the `next` callback
   to activate the updated config.

   ```
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
   ```
2. The next time you publish a new version of your Remote Config, devices
   that are running your app and listening for changes will call the completion
   handler.

## Throttling

If an app fetches too many times in a short time period, fetch calls may be
throttled. In such cases, the SDK throws a `FETCH_THROTTLE` error. You are
recommended to catch this error and retry in exponential backoff mode, waiting
longer intervals between subsequent fetch requests.

During app development, you might want to refresh the cache very frequently
(many times per hour) to let you rapidly iterate as you develop and test your
app. To accommodate rapid iteration on a project with numerous developers, you
can temporarily add a property with a low minimum fetch interval
(`Settings.minimumFetchIntervalMillis`) in your app.

The default and recommended production fetch interval for Remote Config
is 12 hours, which means that configs won't be fetched from the backend more
than once in a 12 hour window, regardless of how many fetch calls are actually
made. Specifically, the minimum fetch interval is determined in the following
order:

1. The parameter in `Settings.minimumFetchIntervalMillis`.
2. The default value of 12 hours.

> [!CAUTION]
> Keep in mind that this setting should be used for development only, not for an app running in production. If you're just testing your app with a small 10-person development team, you are unlikely to hit the hourly service-side quota limits. But if you pushed your app out to thousands of test users with a very low minimum fetch interval, your app would probably hit this quota.