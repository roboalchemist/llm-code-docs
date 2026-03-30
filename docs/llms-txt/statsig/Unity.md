# Source: https://docs.statsig.com/client/Unity.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Unity SDK

> Statsig's SDK for Experimentation and Feature Flags in Unity applications.

<Callout icon="github">
  Source code: <a href="https://github.com/statsig-io/unity-sdk" target="_blank" rel="noreferrer">statsig-io/unity-sdk</a>
</Callout>

## Setup the SDK

<Steps>
  <Step title="Install the SDK">
    The project is on [GitHub](https://github.com/statsig-io/unity-sdk). You can add the package to your Unity project via "Package Manager" -> "add package from Git URL" -> enter [https://github.com/statsig-io/unity-sdk.git](https://github.com/statsig-io/unity-sdk.git) (be sure to include the `.git` part in the URL)
  </Step>

  <Step title="Initialize the SDK">
    Next, initialize the SDK with a client SDK key from the ["API Keys" tab on the Statsig console](https://console.statsig.com/api_keys). These keys are safe to embed in a client application.

    Along with the key, pass in a [User Object](#statsig-user) with the attributes you'd like to target later on in a gate or experiment.

    It is important to **make sure API calls to `Statsig` are made from the main thread** to ensure everything functions correctly. Operations that take longer like network requests are made asynchronously so they will not block the main thread.

    ```csharp  theme={null}
    using StatsigUnity;

    await Statsig.Initialize(
        "client-sdk-key",
        new StatsigUser { UserID = "some_user_id", Email = "user@email.com" },
        new StatsigOptions // optional parameters to customize your Statsig client, see "Statsig Options" section below to see details on available options
        {
            EnvironmentTier = EnvironmentTier.Development,
            InitializeTimeoutMs = 5000,
        }
    );
    ```
  </Step>
</Steps>

## Use the SDK

### Checking a Feature Flag/Gate

Now that your SDK is initialized, let's check a [**Feature Gate**](/feature-flags/overview). Feature Gates can be used to create logic branches in code that can be rolled out to different users from the Statsig Console. Gates are always **CLOSED** or **OFF** (think `return false;`) by default.

```csharp  theme={null}
if (Statsig.CheckGate("show_new_loading_screen"))
{
  // Gate is on, show new loading screen
}
else
{
  // Gate is off, show old loading screen
}
```

### Reading a Dynamic Config

Feature Gates can be very useful for simple on/off switches, with optional but advanced user targeting. However, if you want to be able send a different set of values (strings, numbers, and etc.) to your clients based on specific user attributes, e.g. country, **Dynamic Configs** can help you with that. The API is very similar to Feature Gates, but you get an entire json object you can configure on the server and you can fetch typed parameters from it. For example:

```csharp  theme={null}
var config = Statsig.GetConfig("awesome_product_details");

// The 2nd parameter is the default value to be used in case the given parameter name does not exist on
// the Dynamic Config object. This can happen when there is a typo, or when the user is offline and the
// value has not been cached on the client.
string itemName = config.Get<string>("product_name", "Awesome Product v1");
double price = config.Get<double>("price", 10.0);
bool shouldDiscount = config.Get<bool>("discount", false);
```

### Getting a Layer/Experiment

Then we have **Layers/Experiments**, which you can use to run A/B/n experiments. We offer two APIs, but we recommend the use of [layers](/layers) to enable quicker iterations with parameter reuse.

```csharp  theme={null}
// Values via getLayer

var layer = Statsig.GetLayer("user_promo_experiments");
var promoTitle = layer.Get("title", "Welcome to Statsig!");
var discount = layer.Get("discount", 0.1);

// or, via getExperiment

var titleExperiment = Statsig.GetExperiment("new_user_promo_title");
var priceExperiment = Statsig.GetExperiment("new_user_promo_price");

var promoTitle = titleExperiment.Get("title", "Welcome to Statsig!");
var discount = priceExperiment.Get("discount", 0.1);

...

double price = msrp * (1 - discount);
```

### Logging an Event

Now that you have a Feature Gate or an Experiment set up, you may want to track some custom events and see how your new features or different experiment groups affect these events. This is super easy with Statsig - simply call the Log Event API for the event, and you can additionally provide some value and/or an object of metadata to be logged together with the event:

```csharp  theme={null}
Statsig.LogEvent(
  "purchase",
  "new_player_pack",
  new Dictionary<string, string>() {
    { "price", "9.99" }
  }
);
```

## Statsig User

You need to provide a StatsigUser object to check/get your configurations. You should pass as much
information as possible in order to take advantage of advanced gate and config conditions.

Most of the time, the `userID` field is needed in order to provide a consistent experience for a given
user (see [logged-out experiments](/guides/first-device-level-experiment) to understand how to correctly run experiments for logged-out
users).

Besides `userID`, we also have `email`, `ip`, `userAgent`, `country`, `locale` and `appVersion` as top-level fields on
StatsigUser. In addition, you can pass any key-value pairs in an object/dictionary to the `custom` field and be able to
create targeting based on them.

Once the user logs in or has an update/changed, make sure to call `updateUser`
with the updated `userID` and/or any other updated user attributes:

```csharp  theme={null}
// if you want to update the existing user, or change to a different user, call UpdateUser.
// The API makes a network request to fetch values for the new user.

await Statsig.UpdateUser(
    new StatsigUser { UserID = "new_user_id", Email = "new_user@email.com" },
);
```

### Private Attributes

Have sensitive user PII data that should not be logged? No problem, we have a solution for it! On the StatsigUser object we also have a field called `privateAttributes`, which is a simple object/dictionary that you can use to set private user attributes. Any attribute set in `privateAttributes` will only be used for evaluation/targeting, and removed from any logs before they are sent to Statsig server.

For example, if you have feature gates that should only pass for users with emails ending in "@statsig.com", but do not want to log your users' email addresses to Statsig, you can simply add the key-value pair `{ email: "my_user@statsig.com" }` to `privateAttributes` on the user and that's it!

## Statsig Options

`Initialize()` takes an optional parameter `options` in addition to `clientKey` and `user` that you can provide to customize the Statsig client.

<ResponseField name="EnvironmentTier" type="EnvironmentTier" default="null">
  Set the environment tier for the user. Values: `Production | Development | Staging`.
  Users with `null` or `Production` tier are included in Pulse metrics by default.
</ResponseField>

<ResponseField name="InitializeTimeoutMs" type="int" default="5000">
  Maximum milliseconds `Statsig.Initialize()` will wait before proceeding with cached/default values.
</ResponseField>

<ResponseField name="LoggingIntervalMs" type="int" default="60000">
  Interval for periodically flushing logging events to the Statsig backend.
</ResponseField>

<ResponseField name="LoggingBufferMaxSize" type="int" default="100">
  Maximum number of events the logger batches before flushing.
</ResponseField>

## Shutting Statsig Down

In order to save users' data and battery usage, as well as prevent logged events from being dropped, we keep event logs in client cache and flush periodically.
Because of this, some events may not have been sent when your app shuts down.

To make sure all logged events are properly flushed or saved locally, you should tell Statsig to shutdown when your app is closing:

```csharp  theme={null}
// This function is async, and you can choose to await for it so that we make sure all the
// events that are yet to be flushed get flushed
await Statsig.Shutdown();
```

## FAQs

#### How do I run experiments for logged out users?

See the guide on [device level experiments](/guides/first-device-level-experiment)


Built with [Mintlify](https://mintlify.com).