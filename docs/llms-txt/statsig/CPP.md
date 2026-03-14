# Source: https://docs.statsig.com/client/CPP.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# C++ Client SDK

> Statsig's SDK for Experimentation and Feature Flags in C++ applications.

<Callout icon="github">
  Source code: <a href="https://github.com/statsig-io/cpp-client-sdk" target="_blank" rel="noreferrer">statsig-io/cpp-client-sdk</a>
</Callout>

## Set Up the SDK

<Steps>
  <Step title="Install the SDK">
    <Tabs>
      <Tab title="Downloaded From GitHub">
        ```cpp  theme={null}
        add_subdirectory(path/to/downloaded/statsig_sdk)
        target_link_libraries(${PROJECT_NAME} StatsigClientSDK)
        ```
      </Tab>

      <Tab title="FetchContent">
        ```cpp  theme={null}
        include(FetchContent)

        FetchContent_Declare(statsig
          GIT_REPOSITORY    https://github.com/statsig-io/cpp-client-sdk.git
          GIT_TAG           main
        )
        FetchContent_MakeAvailable(statsig)

        target_link_libraries(${PROJECT_NAME} StatsigClientSDK)
        ```
      </Tab>
    </Tabs>
  </Step>

  <Step title="Initialize the SDK">
    Next, initialize the SDK with a client SDK key from the ["API Keys" tab on the Statsig console](https://console.statsig.com/api_keys). These keys are safe to embed in a client application.

    Along with the key, pass in a [User Object](#statsig-user) with the attributes you'd like to target later on in a gate or experiment.

    ```cpp  theme={null}
    #include <statsig/statsig.h>

    using namespace statsig;

    StatsigUser user;
    user.user_id = "a-user";
    user.custom_ids = {
        {"employeeID", "an-employee"}
    };

    // Create your own instance
    StatsigClient client;

    // Initialize synchronously using cached values from the previous session
    client.InitializeSync("client-{YOUR_CLIENT_SDK_KEY}", user);

    // or, Initialize asynchronously from network
    client.InitializeAsync(
        "client-{YOUR_CLIENT_SDK_KEY}",
        [](StatsigResultCode result) {
            // completion callback
        },
        user
    );
    ```

    **Synchronous** initialization will leverage cache (if available), returning immediately.
    Data for subsequent sessions will then be fetched in the background.

    **Asynchronous** initialization, on the other hand provides a callback, allowing you to wait for the most
    current data to be fetched.

    For convenience, there is also a singleton instance that can be accessed via `StatsigClient::Shared()`.

    ```cpp  theme={null}
    // Initialize synchronously using cached values from the previous session
    StatsigClient::Shared().InitializeSync("client-{YOUR_CLIENT_SDK_KEY}", user);

    // or, Initialize asynchronously from network
    StatsigClient::Shared().InitializeAsync(
        "client-{YOUR_CLIENT_SDK_KEY}",
        [](StatsigResultCode result) {
            // completion callback
        },
        user
    );
    ```

    **Optional** - Configuration via StatsigOptions

    It is possible to adjust certain aspects of how the SDK works via a [StatsigOptions](#statsig-options) struct.
    Just pass in a StatsigOptions struct during initialization.

    ```cpp  theme={null}
    StatsigOptions options;
    options.environment = StatsigEnvironment{"staging"};

    client.InitializeSync(..., options);

    // or

    client.InitializeAsync(..., options);
    ```
  </Step>
</Steps>

## Use the SDK

### Checking a Feature Flag/Gate

Now that your SDK is initialized, let's check a [**Feature Gate**](/feature-flags/overview). Feature Gates can be used to create logic branches in code that can be rolled out to different users from the Statsig Console. Gates are always **CLOSED** or **OFF** (think `return false;`) by default.

```cpp  theme={null}
if (client.CheckGate("a_gate")) {
  // show new feature
}

// or, use the shared instance

if (StatsigClient::Shared().CheckGate("a_gate")) {
  // show new feature
}
```

### Reading a Dynamic Config

Feature Gates can be very useful for simple on/off switches, with optional but advanced user targeting. However, if you want to be able send a different set of values (strings, numbers, and etc.) to your clients based on specific user attributes, e.g. country, **Dynamic Configs** can help you with that. The API is very similar to Feature Gates, but you get an entire json object you can configure on the server and you can fetch typed parameters from it. For example:

```cpp  theme={null}
DynamicConfig config = client.GetDynamicConfig("a_config");

// or, use the shared instance

DynamicConfig config = StatsigClient::Shared().GetDynamicConfig("a_config");

// then access the params
std::cout << config.GetValue()["a_string_param"] << std::endl;
```

<Info>
  DynamicConfig.GetValue returns JsonObj which is an unordered map of string to `nlohmann/json`. See [https://github.com/nlohmann/json](https://github.com/nlohmann/json)
</Info>

### Getting a Layer/Experiment

Then we have **Layers/Experiments**, which you can use to run A/B/n experiments. We offer two APIs, but we recommend the use of [layers](/layers) to enable quicker iterations with parameter reuse.

```cpp  theme={null}
// Values via getLayer

Layer layer = StatsigClient::Shared().GetLayer("name");
std::string promoTitle = layer.GetValue("title").get<std::string>();
double discount = layer.GetValue("discount").get<double>();

// or, via getExperiment

Experiment titleExperiment = StatsigClient::Shared().GetExperiment("new_user_promo_title");
Experiment priceExperiment = StatsigClient::Shared().GetExperiment("new_user_promo_price");

std::string promoTitle = titleExperiment.GetValue()["title"].get<std::string>();
double discount = priceExperiment.GetValue()["discount"].get<double>();
```

<Info>
  Layer.GetValue and Experiment.GetValue return JsonObj which are unordered maps of string to `nlohmann/json`. See [https://github.com/nlohmann/json](https://github.com/nlohmann/json)
</Info>

### Logging an Event

Now that you have a Feature Gate or an Experiment set up, you may want to track some custom events and see how your new features or different experiment groups affect these events. This is super easy with Statsig - simply call the Log Event API for the event, and you can additionally provide some value and/or an object of metadata to be logged together with the event:

```cpp  theme={null}
std::unordered_map<std::string, std::string> metadata{
    { "price", "9.99" },
    { "item_name", "some_great_product" }
};

StatsigEvent event("add_to_cart", "SKU_12345", metadata);
StatsigClient::Shared().LogEvent(event);

// Then, at some point later, you need to "flush" the events
StatsigClient::Shared().Flush();
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

```cpp  theme={null}
StatsigUser user;
user.user_id = "a-user";
user.email = "developer@statsig.com";
user.custom_ids = {
    {"employeeID", "an-employee"}
};
```

### Private Attributes

Have sensitive user PII data that should not be logged? No problem, we have a solution for it! On the StatsigUser object we also have a field called `privateAttributes`, which is a simple object/dictionary that you can use to set private user attributes. Any attribute set in `privateAttributes` will only be used for evaluation/targeting, and removed from any logs before they are sent to Statsig server.

For example, if you have feature gates that should only pass for users with emails ending in "@statsig.com", but do not want to log your users' email addresses to Statsig, you can simply add the key-value pair `{ email: "my_user@statsig.com" }` to `privateAttributes` on the user and that's it!

### Updating Users

At some point, your user might need to change. To make Statsig aware of this new user, you will need to make a call to an UpdateUser function.

```cpp  theme={null}
client.UpdateUserSync(user);

// or, use the shared instance

StatsigClient::Shared().UpdateUserSync(user);
```

If you want to ensure you have the latest values for an update (Say you are transition from logged out to logged in). You can use the Asynchronous update function.

```cpp  theme={null}
{client or StatsigClient::Shared()}.UpdateUserAsync(
    user,
    [](StatsigResultCode result) {
        if (result == StatsigResultCode::Ok) {
          // do something now that the latest values have been fetched
        } else {
          // error state
        }
    }
);
```

Asynchronous vs Synchronous behaviors are the same as the Initialize functions.

## Statsig Options

`StatsigClient::Initialize`, in addition to `sdk_key` and `user`, takes an optional parameter `options` that you can provide to customize the StatsigClient. Here are the current options and we are always adding more to the list:

<ResponseField name="api" type="std::string" default="https://statsigapi.net">
  The API to use for all SDK network requests. You should not need to override this unless you have another API that implements the Statsig API endpoints.
</ResponseField>

<ResponseField name="providers" type="EvaluationsDataProvider" default="LocalFileCache then Network">
  Array of EvaluationsDataProvider, used to customize the initialization and update behavior.
</ResponseField>

## Lifecycle & Advanced Usage

## Shutting Statsig Down

In order to save users' data and battery usage, as well as prevent logged events from being dropped, we keep event logs in client cache and flush periodically.
Because of this, some events may not have been sent when your app shuts down.

To make sure all logged events are properly flushed or saved locally, you should tell Statsig to shutdown when your app is closing:

```cpp  theme={null}
client.Shutdown();

// or, use the shared instance

StatsigClient::Shared().Shutdown();
```

#### How do I run experiments for logged out users?​

See the guide on [device level experiments](/guides/first-device-level-experiment)


Built with [Mintlify](https://mintlify.com).