# Source: https://docs.statsig.com/server/cpp.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# C++ Server SDK

> Statsig's Server SDK for C++ applications

<Card title="GitHub Repository" icon="github" href="https://github.com/statsig-io/cpp-server-sdk">
  View the C++ SDK source code and releases
</Card>

## Setup the SDK

<Steps>
  <Step title="Install the SDK">
    If you are using CMake, add the following to a `.cmake` file

    ```cmake  theme={null}
    FetchContent_Declare(statsig
            GIT_REPOSITORY    https://github.com/statsig-io/cpp-server-sdk.git
            GIT_TAG           v0.1.0
    )

    FetchContent_MakeAvailable(statsig)
    ```

    And include the following in your `CMakeLists.txt` file

    ```cmake  theme={null}
    cmake_minimum_required(VERSION 3.11)

    include(FetchContent)
    include(${CMAKE_CURRENT_SOURCE_DIR}/cmake/statsig.cmake)
    ```

    Check out the latest versions on [https://github.com/statsig-io/cpp-server-sdk/releases/latest](https://github.com/statsig-io/cpp-server-sdk/releases/latest)
  </Step>

  <Step title="Initialize the SDK">
    After installation, you will need to initialize the SDK using a [Server Secret Key from the Statsig console](https://console.statsig.com/api_keys).

    <Warning>
      Do NOT embed your Server Secret Key in client-side applications, or expose it in any external-facing documents. However, if you accidentally expose it, you can create a new one in the Statsig console.
    </Warning>

    ```cpp  theme={null}
    #include <statsig.h>

    statsig::initialize('server-secret-key');

    // Or, if you want to initialize with certain options
    statsig::Options options;
    options.localMode = true
    statsig::initialize('server-secret-key', options)
    ```

    `initialize` will perform a network request. After `initialize` completes, virtually all SDK operations will be synchronous (See [Evaluating Feature Gates in the Statsig SDK](https://blog.statsig.com/evaluating-feature-gates-in-the-statsig-sdk-a6f8881a1ad8)). The SDK will fetch updates from Statsig in the background, independently of your API calls.
  </Step>
</Steps>

## Working with the SDK

## Checking a Feature Flag/Gate

Now that your SDK is initialized, let's fetch a [**Feature Gate**](/feature-flags/overview). Feature Gates can be used to create logic branches in code that can be rolled out to different users from the Statsig Console. Gates are always **CLOSED** or **OFF** (think `return false;`) by default.

From this point on, all APIs will require you to specify the user (see [Statsig user](#statsig-user)) associated with the request. For example, check a gate for a certain user like this:

```cpp  theme={null}
statsig::User user;
user.userID = "some_user_id"
if (statsig::checkGate(user, 'use_new_feature'))
{
  // Gate is on, enable new feature
}
else {
  // Gate is off
}
```

## Reading a Dynamic Config

Feature Gates can be very useful for simple on/off switches, with optional but advanced user targeting. However, if you want to be able send a different set of values (strings, numbers, and etc.) to your clients based on specific user attributes, e.g. country, [**Dynamic Configs**](/dynamic-config) can help you with that. The API is very similar to Feature Gates, but you get an entire json object you can configure on the server and you can fetch typed parameters from it.

```cpp  theme={null}
statsig::DynamicConfig config = statsig::get_config(user, 'awesome_product_details')

auto item_name = config.value['product_name'];
auto price = config.value['price'];
auto shouldDiscount = config.value['discount'];
```

## Getting a Layer/Experiment

Then we have **Layers/Experiments**, which you can use to run A/B/n experiments. We offer two APIs, but we recommend the use of [layers](/layers) to enable quicker iterations with parameter reuse.

```cpp  theme={null}
// Values via getLayer

statsig::Layer layer = statsig::getLayer(user, "user_promo_experiments")
auto title = layer.get("title", "Welcome to Statsig!")
auto discount = layer.get("discount")

// or, via getExperiment

statsig::DynamicConfig title_exp = statsig::getExperiment(user, "new_user_promo_title")
statsig::DynamicConfig price_exp = statsig::getExperiment(user, "new_user_promo_price")

title = title_exp.value["title"]
discount = price_exp.value["discount"]

...

price = msrp * (1 - discount)


```

## Logging an Event

Now that you have a Feature Gate or an Experiment set up, you may want to track some custom events and see how your new features or different experiment groups affect these events. This is super easy with Statsig - simply call the Log Event API and specify the user and event name to log; you additionally provide some value and/or an object of metadata to be logged together with the event:

```cpp  theme={null}
statsig::logEvent(user, 'add_to_cart')
```

Learn more about identifying users, group analytics, and best practices for logging events in the [logging events guide](/guides/logging-events).

## Statsig User

When calling APIs that require a user, you should pass as much information as possible in order to take advantage of advanced gate and config conditions (like country or OS/browser level checks), and correctly measure impact of your experiments on your metrics/events. As explained [here](/sdks/user#why-is-an-id-always-required-for-server-sdks), at least one identifier (userID or customID) is required to provide a consistent experience for a given user.

Besides `userID`, we also have `email`, `ip`, `userAgent`, `country`, `locale` and `appVersion` as top-level fields on StatsigUser. In addition, you can pass any key-value pairs in an object/dictionary to the `custom` field and be able to create targeting based on them.

Note that while typing is lenient on the `StatsigUser` object to allow you to pass in numbers, strings, arrays, objects, and potentially even enums or classes, the evaluation operators will only be able to operate on primitive types - mostly strings and numbers. While we attempt to smartly cast custom field types to match the operator, we cannot guarantee evaluation results for other types. For example, setting an array as a custom field will only ever be compared as a string - there is no operator to match a value in that array.

### Private Attributes

Have sensitive user PII data that should not be logged? No problem, we have a solution for it! On the StatsigUser object we also have a field called `privateAttributes`, which is a simple object/dictionary that you can use to set private user attributes. Any attribute set in `privateAttributes` will only be used for evaluation/targeting, and removed from any logs before they are sent to Statsig server.

For example, if you have feature gates that should only pass for users with emails ending in "@statsig.com", but do not want to log your users' email addresses to Statsig, you can simply add the key-value pair `{ email: "my_user@statsig.com" }` to `privateAttributes` on the user and that's it!

## Statsig Options

`initialize()` takes an optional parameter `options` in addition to the secret key that you can provide to customize the Statsig client. Here are the current options and we are always adding more to the list:

You can specify optional parameters with `options` when initializing.

* **api** string, default `"https://statsigapi.net/v1"`
  * The base url to use for network requests from the SDK
* **rulesetsSyncIntervalMs**: int, default `10000`
  * The interval to poll for changes to your gate and config definition changes
* **loggingIntervalMs**: int, default `60000`
  * The default interval to flush logs to Statsig servers
* **loggingMaxBufferSize**: int, default `1000`, can be set lower but anything over 1000 will be dropped on the server
  * The maximum number of events to batch before flushing logs to the server
* **localMode**: bool, default `false`
  * Restricts the SDK to not issue any network requests and only respond with default values (or local overrides)

<Info>
  ID Lists are currently not supported in the C++ server SDK
</Info>

## Shutdown

To gracefully shutdown the SDK and ensure all events are flushed:

```cpp  theme={null}
statsig::shutdown()
```

## Local Overrides

You can override the values returned by the SDK for testing purposes. This can be useful for local development when you want to test specific scenarios.

```cpp  theme={null}
// Adding gate overrides
statsig::overrideGate("a_gate_name", true)

// Adding config overrides
std::unordered_map<std::string, JSON::any> overrideValue = {
    {"overridden key", "overridden field"},
};
statsig::overrideConfig("a_config_name", overrideValue)
```

## FAQ

#### How do I run experiments for logged out users?

See the guide on [device level experiments](/guides/first-device-level-experiment)

## Reference

### User

```cpp  theme={null}
struct User
{
  std::string userID;
  std::string email;
  std::string ipAddress;
  std::string userAgent;
  std::string country;
  std::string locale;
  std::string appVersion;
  std::unordered_map<std::string, JSON::any> custom;
  std::unordered_map<std::string, JSON::any> privateAttribute;
  std::unordered_map<std::string, std::string> statsigEnvironment;
  std::unordered_map<std::string, std::string> customIDs;
};
inline bool operator==(User const &a, User const &b)
{
  return a.userID == b.userID &&
          a.email == b.email &&
          a.ipAddress == b.ipAddress &&
          a.userAgent == b.userAgent &&
          a.country == b.country &&
          a.locale == b.locale &&
          a.appVersion == b.appVersion &&
          a.custom == b.custom &&
          a.privateAttribute == b.privateAttribute &&
          a.statsigEnvironment == b.statsigEnvironment &&
          a.customIDs == b.customIDs;
};
```

### Options

```cpp  theme={null}
struct Options
{
  std::string api;
  bool localMode;
  int rulesetsSyncIntervalMs;
  int loggingIntervalMs;
  int loggingMaxBufferSize;
  Options() : api("https://statsigapi.net"),
              localMode(false),
              rulesetsSyncIntervalMs(10 * 1000),
              loggingIntervalMs(60 * 1000),
              loggingMaxBufferSize(1000){};
};
```


Built with [Mintlify](https://mintlify.com).