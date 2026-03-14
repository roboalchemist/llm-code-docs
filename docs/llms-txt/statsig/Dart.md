# Source: https://docs.statsig.com/client/Dart.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Dart Client SDK

> Statsig's SDK for Experimentation and Feature Flags in Dart & Flutter applications.

<Callout icon="github">
  Source code: <a href="https://github.com/statsig-io/dart-sdk" target="_blank" rel="noreferrer">statsig-io/dart-sdk</a>
</Callout>

## Set Up the SDK

<Steps>
  <Step title="Install the SDK">
    With Dart:

    ```bash  theme={null}
    dart pub add statsig
    ```

    With Flutter:

    ```bash  theme={null}
    flutter pub add statsig
    ```

    <Note>
      If you are using **Flutter**, be sure to add Statsig as part of the [app lifecycle](#flutter-lifecycle-hooks) to avoid losing events.
    </Note>
  </Step>

  <Step title="Initialize the SDK">
    Next, initialize the SDK with a client SDK key from the ["API Keys" tab on the Statsig console](https://console.statsig.com/api_keys). These keys are safe to embed in a client application.

    Along with the key, pass in a [User Object](#statsig-user) with the attributes you'd like to target later on in a gate or experiment.

    ```dart  theme={null}
    import 'package:statsig/statsig.dart';

    await Statsig.initialize('client-sdk-key', StatsigUser(userId: "a-user-id"));
    ```
  </Step>
</Steps>

## Use the SDK

### Checking a Feature Flag/Gate

Now that your SDK is initialized, let's check a [**Feature Gate**](/feature-flags/overview). Feature Gates can be used to create logic branches in code that can be rolled out to different users from the Statsig Console. Gates are always **CLOSED** or **OFF** (think `return false;`) by default.

```dart  theme={null}
if (Statsig.checkGate("new_homepage_design")) {
  // Gate is on, show new home page
} else {
  // Gate is off, show old home page
}
```

### Reading a Dynamic Config

Feature Gates can be very useful for simple on/off switches, with optional but advanced user targeting. However, if you want to be able send a different set of values (strings, numbers, and etc.) to your clients based on specific user attributes, e.g. country, **Dynamic Configs** can help you with that. The API is very similar to Feature Gates, but you get an entire json object you can configure on the server and you can fetch typed parameters from it. For example:

```dart  theme={null}
var config = Statsig.getConfig("awesome_product_details");

// The 2nd parameter is the default value to be used in case the given parameter name does not exist on
// the Dynamic Config object. This can happen when there is a typo, or when the user is offline and the
// value has not been cached on the client.
var itemName = config.get("product_name", "Awesome Product v1");
var price = config.get("price", 10.0);
var shouldDiscount = config.get("discount", false);
```

### Getting a Layer/Experiment

Then we have **Layers/Experiments**, which you can use to run A/B/n experiments. We offer two APIs, but we recommend the use of [layers](/layers) to enable quicker iterations with parameter reuse.

```dart  theme={null}
// Values via getLayer

var layer = Statsig.getLayer("user_promo_experiments");
var promoTitle = layer.getString("title", "Welcome to Statsig!");
var discount = layer.getDouble("discount", 0.1);

// or, via getExperiment

var titleExperiment = Statsig.getExperiment("new_user_promo_title");
var priceExperiment = Statsig.getExperiment("new_user_promo_price");

var promoTitle = titleExperiment.get("title", "Welcome to Statsig!");
var discount = priceExperiment.get("discount", 0.1);
```

### Logging an Event

Now that you have a Feature Gate or an Experiment set up, you may want to track some custom events and see how your new features or different experiment groups affect these events. This is super easy with Statsig - simply call the Log Event API for the event, and you can additionally provide some value and/or an object of metadata to be logged together with the event:

```dart  theme={null}
// Provide a doubleValue argument for number values
Statsig.logEvent("purchase", doubleValue: 2.99, metadata: {"item_name": "remove_ads"});

// or provide a stringValue argument for string values
Statsig.logEvent("login", stringValue: "a.user@mail.com");
```

## Parameter Stores

Parameter Stores hold a set of parameters for your mobile app. These parameters can be remapped on-the-fly from a static value to a Statsig entity (Feature Gates, Experiments, and Layers), so you can decouple your code from the configuration in Statsig. Read more about Param Stores [here](/client/concepts/parameter-stores).

```dart  theme={null}
var homepageStore = Statsig.getParameterStore("homepage");

var title = homepageStore.get("title", "Welcome");
var shouldShowUpsell = homepageStore.get("upsell_upgrade_now", false);
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

```dart  theme={null}
await Statsig.updateUser(StatsigUser("a_new_user"));
```

### Private Attributes

Have sensitive user PII data that should not be logged? No problem, we have a solution for it! On the StatsigUser object we also have a field called `privateAttributes`, which is a simple object/dictionary that you can use to set private user attributes. Any attribute set in `privateAttributes` will only be used for evaluation/targeting, and removed from any logs before they are sent to Statsig server.

For example, if you have feature gates that should only pass for users with emails ending in "@statsig.com", but do not want to log your users' email addresses to Statsig, you can simply add the key-value pair `{ email: "my_user@statsig.com" }` to `privateAttributes` on the user and that's it!

## Statsig Options

<ResponseField name="initTimeout" type="int" default="3">
  Used to decide how long (in seconds) the Statsig client waits for the initial network request to respond before calling the completion block. The Statsig client will return either cached values (if any) or default values if checkGate/getConfig/getExperiment is called before the initial network request completes.

  If you always want to wait for the latest values fetched from Statsig server, you should set this to 0 so we do not timeout the network request.
</ResponseField>

<ResponseField name="api" type="string" default="https://statsigapi.net/v1/">
  The endpoint to use for all SDK network requests. You should not override this (unless you have another API that implements the Statsig API endpoints).
</ResponseField>

<ResponseField name="environment" type="string" default="">
  The environment tier to evaluate rules for the current user. Default empty, which is the same as "production." On non-production tiers, events will not make it in to downstream pulse results.
</ResponseField>

## Lifecycle & Advanced Usage

## Shutting Statsig Down

In order to save users' data and battery usage, as well as prevent logged events from being dropped, we keep event logs in client cache and flush periodically.
Because of this, some events may not have been sent when your app shuts down.

To make sure all logged events are properly flushed or saved locally, you should tell Statsig to shutdown when your app is closing:

```dart  theme={null}
await Statsig.shutdown();
```

## Flutter Lifecycle Hooks

Due to the nature of mobile development, apps can be closed by the operating system when they are no longer in the foreground. To be sure that all events are logged before an app is closed by the operating system, we recommend adding Statsig to the app lifecycle events. This way we can flush all pending events when an app state change is detected.

Something like the following:

```dart  theme={null}
// An example App Lifecycle Observer
class StatsigLifecycleObserver extends WidgetsBindingObserver {
  @override
  void didChangeAppLifecycleState(AppLifecycleState state) async {
    switch (state) {
      case AppLifecycleState.resumed:
        await Statsig.initialize('client-sdk-key');
        break;
      case AppLifecycleState.paused:
        await Statsig.shutdown();
        break;
    }
  }
}

```

Then in your app code, add this observer to the WidgetsBinding instance.

```dart  theme={null}
@override
void initState() {
  super.initState();
  WidgetsBinding.instance.addObserver(StatsigLifecycleObserver());
}
```

## FAQs

### How do I run experiments for logged out users?

See the guide on [device level experiments](/client/concepts/persistent_assignment).


Built with [Mintlify](https://mintlify.com).