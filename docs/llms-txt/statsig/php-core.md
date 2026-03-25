# Source: https://docs.statsig.com/server-core/php-core.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# PHP Server SDK

> Statsig's Next-gen PHP Server SDK built in our [Server Core](/server-core) framework

<Callout icon="github">
  <a href="https://github.com/statsig-io/statsig-server-core/tree/main/statsig-php" target="_blank" rel="noreferrer">PHP Core on Github</a>,
  <a href="https://packagist.org/packages/statsig/statsig-php-core" target="_blank" rel="noreferrer">Packagist Package</a>
</Callout>

<Tip>Migrating from the Legacy PHP SDK? See our [Migration Guide](/server-core/migration-guides/php).</Tip>

## Setup the SDK

<Steps>
  <Step title="Install the SDK">
    ## Installation

    ### 1. Install and Add as a Dependency

    You can install the new PHP Core SDK using composer:

    ```shell  theme={null}
    composer require statsig/statsig-php-core
    ```

    ### 2. PHP Configuration Requirements

    The PHP Core SDK uses the FFI extension to interface with the Rust core. You must enable FFI in your PHP configuration by setting `ffi.enable=true` in your php.ini file.

    For more information about this setting, see the [PHP manual for ffi.enable](https://www.php.net/manual/en/ffi.configuration.php#ini.ffi.enable).

    ### 3. Add Scripts & Cron Job

    Add post-install and post-update scripts in composer.json:

    ```json  theme={null}
    // composer.json
    {
      "name": "awesome-php-project",
      ...
      "scripts": {
        ...
        "post-install-cmd": [
          "cd vendor/statsig/statsig-php-core && php post-install.php"
        ],
        "post-update-cmd": [
          "cd vendor/statsig/statsig-php-core && php post-install.php"
        ]
      }
    }
    ```

    Next, you'll want to add a script to sync your Statsig configs and flush your events, see example files on Statsig's Github [here](https://github.com/daniel-statsig/statsig-php-core-slim-example/tree/main/bin).

    You'll also want to setup cron jobs to run these scripts periodically:

    ```shell  theme={null}
    */10 * * * * /usr/bin/php /var/www/example.com/bin/StatsigSyncConfig.php 1>> /dev/null 2>&1
    */1 * * * * /usr/bin/php /var/www/example.com/bin/StatsigFlushEvents.php 1>> /dev/null 2>&1
    ```

    Also, be sure to run the StatsigSyncConfig.php cron job at least once before proceeding.
  </Step>

  <Step title="Initialize the SDK">
    After installation, you will need to initialize the SDK using a [Server Secret Key from the Statsig console](https://console.statsig.com/api_keys).

    <Warning>
      Server Secret Keys should always be kept private. If you expose one, you can disable and recreate it in the Statsig console.
    </Warning>

    There is also an optional parameter named `options` that allows you to pass in a StatsigOptions to customize the SDK.

    You'll want to add your client secret key to the environment, by adding to a .env file, or directly on the command line:

    ```shell  theme={null}
    export STATSIG_SECRET_KEY=secret-123456789
    ```

    ```php  theme={null}
    // At the top of your file
    use Statsig\Statsig;
    use Statsig\StatsigOptions;
    use Statsig\StatsigLocalFileEventLoggingAdapter;
    use Statsig\StatsigLocalFileSpecsAdapter;

    //In the case of slim framework, in container builder definitions:

    Statsig::class => function (ContainerInterface $c) {
        $sdk_key = getenv("STATSIG_SECRET_KEY");

        $options = new StatsigOptions(
            null,
            null,
            new StatsigLocalFileSpecsAdapter($sdk_key, "/tmp"),
            new StatsigLocalFileEventLoggingAdapter($sdk_key, "/tmp")
        );

        $statsig = new Statsig($sdk_key, $options);
        $statsig->initialize();
        return $statsig;
    },
    ```

    <Callout type="warning">
      `StatsigLocalFile` Adapters rely on cron jobs and files. If you are seeing errors around file access, ensure your cron job has run at least one time before using Statsig.
      See [Add Scripts & Cron Job](#2-add-scripts--cron-job)
    </Callout>

    `initialize` will perform a network request. After `initialize` completes, virtually all SDK operations will be synchronous (See [Evaluating Feature Gates in the Statsig SDK](https://blog.statsig.com/evaluating-feature-gates-in-the-statsig-sdk-a6f8881a1ad8)). The SDK will fetch updates from Statsig in the background, independently of your API calls.
  </Step>
</Steps>

## Working with the SDK

### Checking a Feature Flag/Gate

Now that your SDK is initialized, let's fetch a [**Feature Gate**](/feature-flags/overview). Feature Gates can be used to create logic branches in code that can be rolled out to different users from the Statsig Console. Gates are always **CLOSED** or **OFF** (think `return false;`) by default.

From this point on, all APIs will require you to specify the user (see [Statsig user](#statsig-user)) associated with the request. For example, check a gate for a certain user like this:

```php  theme={null}
use Statsig\Statsig;
use Statsig\StatsigUserBuilder;

$user = StatsigUserBuilder::withUserID('my_user')->build();
$passed = $statsig->checkGate($user, 'my_gate');
```

### Reading a Dynamic Config

Feature Gates can be very useful for simple on/off switches, with optional but advanced user targeting. However, if you want to be send a different set of values (strings, numbers, and etc.) to your clients based on specific user attributes, e.g. country, [**Dynamic Configs**](/dynamic-config) can help you with that. The API is very similar to Feature Gates, but you get an entire json object you can configure on the server and you can fetch typed parameters from it. For example:

```php  theme={null}
$user = StatsigUserBuilder::withUserID('my_user')->build();
$config = $statsig->getDynamicConfig($user, 'my_config');
```

### Getting a Layer/Experiment

Then we have **Layers/Experiments**, which you can use to run A/B/n experiments. We offer two APIs, but often recommend the use of [layers](/layers), which make parameters reusable and let you run mutually exclusive experiments.

```php  theme={null}
$user = StatsigUserBuilder::withUserID('my_user')->build();
$xp = $statsig->getExperiment($user, 'an_experiment');
```

### Retrieving Feature Gate Metadata

In certain scenarios, you may need more information about a gate evaluation than just a boolean value. For additional metadata about the evaluation, use the Get Feature Gate API, which returns a FeatureGate object:

```php  theme={null}
$gate = $statsig->getFeatureGate($user, "example_gate");
```

### Parameter Stores

Sometimes you don't know whether you want a value to be a Feature Gate, Experiment, or Dynamic Config yet. If you want on-the-fly control of that outside of your deployment cycle, you can use Parameter Stores to define a parameter that can be changed into at any point in the Statsig console. Parameter Stores are optional, but parameterizing your application can prove very useful for future flexibility and can even allow non-technical Statsig users to turn parameters into experiments.

*Parameter stores are not yet available for this sdk. Need it now? Let us know in [Slack](https://statsig.com/slack).*

### Logging an Event

Now that you have a Feature Gate or an Experiment set up, you may want to track some custom events and see how your new features or different experiment groups affect these events. This is super easy with Statsig—simply call the Log Event API and specify the user and event name to log; you additionally provide some value and/or an object of metadata to be logged together with the event:

```php  theme={null}
$user = StatsigUserBuilder::withUserID('my_user')->build();
$statsig->logEvent($user, 'an_experiment');
```

### Sending Events to Log Explorer

You can forward logs to Logs Explorer for convenient analysis using the Forward Log Line Event API. This lets you include custom metadata and event values with each log.

Sending events to Log Explorer is not yet available for this sdk. Need it now? Let us know in [Slack](https://statsig.com/slack).

## Using Shared Instance

In some applications, you may want to create a single Statsig instance that can be accessed globally throughout your codebase. The shared instance functionality provides a singleton pattern for this purpose:

```php  theme={null}
use Statsig\Statsig;

// Initialize the shared instance
Statsig::initializeShared('your-server-secret-key', $options);

// Access the shared instance from anywhere in your code
$user = StatsigUserBuilder::withUserID('my_user')->build();
$gate = Statsig::shared()->checkGate($user, 'my_gate');

// Shutdown the shared instance when your application closes
Statsig::shared()->shutdown();
```

## Statsig User

The `StatsigUser` object represents a user in Statsig. You must provide a `userID` or at least one of the `customIDs` to identify the user.

When calling APIs that require a user, you should pass as much information as possible in order to take advantage of advanced gate and config conditions (like country or OS/browser level checks), and correctly measure impact of your experiments on your metrics/events. As explained [here](/sdks/user#why-is-an-id-always-required-for-server-sdks), at least one identifier (userID or customID) is required to provide a consistent experience for a given user.

Besides userID, we also have email, ip, userAgent, country, locale and appVersion as top-level fields on StatsigUser. In addition, you can pass any key-value pairs in an object/dictionary to the custom field and be able to create targeting based on them.

### Private Attributes

Private attributes are user attributes that are used for evaluation but are not forwarded to any integrations. They are useful for PII or sensitive data that you don't want to send to third-party services.

```php  theme={null}
use Statsig\StatsigUser;

$user = new StatsigUser([
    'userID' => 'a-user-id',
    'email' => 'user@example.com',
    'ip' => '192.168.1.1',
    'userAgent' => 'Mozilla/5.0...',
    'country' => 'US',
    'locale' => 'en_US',
    'appVersion' => '1.0.0',
    'custom' => [
        // Custom fields
        'plan' => 'premium',
        'age' => 25
    ],
    'customIDs' => [
        // Custom ID types
        'stableID' => 'stable-id-123'
    ],
    'privateAttributes' => [
        // Private attributes not forwarded to integrations
        'email' => 'private@example.com'
    ]
]);
```

## Private Attributes

You can define which attributes are considered "private" and should not be forwarded to any third-party integrations like the data connectors by setting the `privateAttributes` parameter in the `StatsigUser` constructor. The `privateAttributes` parameter is a key-value dictionary where keys are attribute names and values are the private values. Note that in the example user object above, for the key `"email"`, we have values for the top-level `email` field AND for the private attributes field with `"email"` as the key. These are distinct; you can have a value in the top-level `email` field that is not `private`, and a value in `private_attributes` that is `private`, or vice versa.

```php  theme={null}
$user = new StatsigUser([
    'userID' => 'a-user-id',
    'email' => 'non_private@example.com',
    'privateAttributes' => [
        'email' => 'private@example.com'
    ]
]);
```

## Statsig Options

You can pass in an optional parameter `options` in addition to `sdkKey` during initialization to customize the Statsig client. Here are the available options that you can configure.

<Accordion title="StatsigOptions">
  <ResponseField name="specs_url" type="string">
    Custom URL for fetching feature specifications.
  </ResponseField>

  <ResponseField name="log_event_url" type="string">
    Custom URL for logging events.
  </ResponseField>

  <ResponseField name="specs_adapter" type="StatsigSpecsAdapter">
    An adapter with custom storage behavior for config specs. For example, use `StatsigLocalFileSpecsAdapter` to store configs in the local filesystem.
  </ResponseField>

  <ResponseField name="event_logging_adapter" type="StatsigEventLoggingAdapter">
    An adapter with custom event logging behavior. For example, use `StatsigLocalFileEventLoggingAdapter` to store events in the local filesystem.
  </ResponseField>

  <ResponseField name="environment" type="string">
    Environment parameter for evaluation.
  </ResponseField>

  <ResponseField name="event_logging_flush_interval_ms" type="int">
    How often events are flushed to Statsig servers (in milliseconds).
  </ResponseField>

  <ResponseField name="event_logging_max_queue_size" type="Option<u32>">
    Maximum number of events to queue before forcing a flush.

    * Default is `2000`
    * event\_logging\_max\_queue\_size \* event\_logging\_max\_pending\_batch\_queue\_size is the upper limit on how many events are queued
    * See also `event_logging_max_pending_batch_queue_size`
  </ResponseField>

  <ResponseField name="event_logging_max_pending_batch_queue_size" type="Option<u32>">
    Maximum number of event batches to hold in buffer to retry.

    * Default is `100`.
    * event\_logging\_max\_queue\_size \* event\_logging\_max\_pending\_batch\_queue\_size is the upper limit on how many events are queued
    * eg: 2000 \* 100 means the SDK can process 200k event per second before events start getting dropped
    * See also `event_logging_max_queue_size`.
  </ResponseField>

  <ResponseField name="specs_sync_interval_ms" type="int">
    How often the SDK updates specifications from Statsig servers (in milliseconds).
  </ResponseField>

  <ResponseField name="output_log_level" type="string">
    Controls the verbosity of SDK logs.
  </ResponseField>

  <ResponseField name="disable_country_lookup" type="bool">
    Disables country lookup based on IP address. Set to `true` to improve performance if country-based targeting is not needed.
  </ResponseField>

  <ResponseField name="disable_user_agent_parsing" type="bool">
    Disables user agent parsing. Set to `true` to improve performance if device/browser-based targeting is not needed.
  </ResponseField>

  <ResponseField name="init_timeout_ms" type="int" default="3000">
    Maximum time in milliseconds to wait for SDK initialization to complete. If initialization takes longer than this timeout, the SDK will continue to operate but may return default values until initialization completes.
  </ResponseField>

  <ResponseField name="fallback_to_statsig_api" type="bool" default="false">
    When set to true, the SDK will fallback to using the Statsig API directly if custom adapters (like local file adapters) fail to load configurations.
  </ResponseField>

  <ResponseField name="enable_id_lists" type="bool">
    Enable/disable ID list functionality. **Required to be `true` when using segments with more than 1000 IDs.** See [ID List segments](/segments/add-id-list) for more details.
  </ResponseField>

  <ResponseField name="proxy_config" type="ProxyConfig">
    Configuration for connecting through a proxy server.
  </ResponseField>

  <Accordion title="ProxyConfig">
    <ResponseField name="proxyHost" type="string">
      The hostname or IP address of the proxy server (e.g., `"proxy.example.com"` or `"192.168.1.100"`).
    </ResponseField>

    <ResponseField name="proxyPort" type="int">
      The port number of the proxy server (e.g., `8080`, `3128`, `1080`).
    </ResponseField>

    <ResponseField name="proxyAuth" type="string">
      Authentication credentials for the proxy server in the format `"username:password"`. Only required if the proxy requires authentication.
    </ResponseField>

    <ResponseField name="proxyProtocol" type="string">
      The protocol to use for the proxy connection. Supported values: `"http"`, `"https"`, `"socks5"`.
    </ResponseField>
  </Accordion>

  ***

  ### Performance Recommendations

  If you are experiencing performance issues, particularly with long initialization times, you can disable user agent parsing and country lookup to improve performance:

  * Set `disable_user_agent_parsing: true` if you don't need device or browser-based targeting
  * Set `disable_country_lookup: true` if you don't need country-based targeting

  These optimizations were added in response to performance issues identified in [PR #1119](https://github.com/statsig-io/private-statsig-server-core/pull/1119).

  ***

  ### Example Usage

  ```php  theme={null}
  use Statsig\Statsig;
  use Statsig\StatsigOptions;
  use Statsig\ProxyConfig;
  use Statsig\StatsigLocalFileSpecsAdapter;
  use Statsig\StatsigLocalFileEventLoggingAdapter;

  // Create proxy configuration
  $proxyConfig = new ProxyConfig(
      proxyHost: "proxy.example.com",
      proxyPort: 8080,
      proxyAuth: "username:password",  // Optional, only if authentication is required
      proxyProtocol: "http"
  );

  // Initialize StatsigOptions with custom parameters
  $options = new StatsigOptions(
      specs_url: null,
      log_event_url: null,
      specs_adapter: new StatsigLocalFileSpecsAdapter($sdk_key, "/tmp"),
      event_logging_adapter: new StatsigLocalFileEventLoggingAdapter($sdk_key, "/tmp"),
      environment: "development",
      event_logging_flush_interval_ms: 60000,
      event_logging_max_queue_size: 1000,
      specs_sync_interval_ms: 600000,
      output_log_level: "INFO",
      disable_country_lookup: true, // For better performance
      wait_for_country_lookup_init: false,
      wait_for_user_agent_init: false,
      enable_id_lists: false,
      disable_network: false,
      id_lists_url: null,
      id_lists_sync_interval_ms: null,
      disable_all_logging: false,
      init_timeout_ms: 3000,
      fallback_to_statsig_api: false,
      use_third_party_ua_parser: null,
      persistent_storage: null,
      proxy_config: $proxyConfig  // Add proxy configuration
  );

  // Pass the options object into Statsig constructor
  $statsig = new Statsig($sdk_key, $options);
  $statsig->initialize();
  ```

  <Callout type="warning">
    When using `StatsigLocalFile` Adapters, ensure your cron job has run at least one time before using Statsig.
    See [Add Scripts & Cron Job](#2-add-scripts--cron-job)
  </Callout>
</Accordion>

## Custom Adapters

### SpecsAdapterBase - Custom Configuration Sources

The `SpecsAdapterBase` allows you to fetch Statsig configurations from custom sources instead of (or in addition to) Statsig's servers. This is useful when you want to:

* Store configurations in your own database or cache (e.g., Redis, Memcached)
* Implement custom caching strategies
* Use Statsig in environments with restricted network access
* Reduce latency by serving configs from a local source

#### Implementation

To create a custom specs adapter, extend the `SpecsAdapterBase` class and implement the required methods:

```php  theme={null}
<?php

use Statsig\SpecsAdapterBase;
use Statsig\SpecsUpdateListener;

class RedisSpecsAdapter extends SpecsAdapterBase
{
    private $redis;
    private $listener;

    public function __construct($redis)
    {
        parent::__construct();
        $this->redis = $redis;
    }

    public function setup(SpecsUpdateListener $listener): void
    {
        $this->listener = $listener;
    }

    public function start(): void
    {
        // Fetch initial specs when SDK starts
        $this->refreshSpecsFromRedis();
        
        // Optionally, trigger a background job or set up a timer
        $this->refreshSpecsFromRedis();
    }

    private function fetchSpecsFromRedis()
    {
        try {
            $specs = $this->redis->get('statsig_config_specs');
            return $specs ?: null;
        } catch (Exception $e) {
            error_log("Failed to fetch specs from Redis: " . $e->getMessage());
            return null;
        }
    }

    private function refreshSpecsFromRedis()
    {
        $specs = $this->fetchSpecsFromRedis();
        if ($specs && $this->listener) {
            $timestamp = intval(microtime(true) * 1000);
            $this->listener->didReceiveSpecsUpdate($specs, "Redis", $timestamp);
        }
    }
}
```

#### Usage

```php  theme={null}
use Statsig\Statsig;
use Statsig\StatsigOptions;

$redis = new Redis();
$redis->connect('127.0.0.1', 6379);
$specsAdapter = new RedisSpecsAdapter($redis);

$options = new StatsigOptions(
    specs_adapter: $specsAdapter
);

$statsig = new Statsig('your-server-secret-key', $options);
$statsig->initialize();
```

#### Key Methods

* **`setup(SpecsUpdateListener $listener)`**: Called during initialization to provide the listener for spec updates
* **`start()`**: Called when the SDK starts. Fetch and provide initial configuration specs
* **`shutdown()`**: Called when the SDK shuts down. Clean up resources
* **`scheduleBackgroundSync()`**: Called to schedule periodic updates of configuration specs

The `SpecsUpdateListener` provides:

* **`didReceiveSpecsUpdate(string $specs, string $source, int $timestamp)`**: Notify the SDK of new specs
* **`getCurrentSpecsInfo()`**: Get information about current specs

***

### EventLoggingAdapterBase - Custom Event Destinations

The `EventLoggingAdapterBase` allows you to send events to custom destinations instead of or in addition to Statsig's servers. This is useful when you want to:

* Send events to your existing analytics platform
* Store events in a database for custom analysis
* Forward events to multiple destinations
* Implement custom batching or retry logic

#### Implementation

To create a custom event logging adapter, extend the `EventLoggingAdapterBase` class and implement the required methods:

```php  theme={null}
<?php

use Statsig\EventLoggingAdapterBase;
use Statsig\LogEventRequest;

class AnalyticsEventAdapter extends EventLoggingAdapterBase
{
    private $analyticsClient;
    private $isStarted = false;

    public function __construct($analyticsClient)
    {
        parent::__construct();
        $this->analyticsClient = $analyticsClient;
    }

    public function start(): void
    {
        $this->isStarted = true;
        // Initialize analytics client connection if needed
        $this->analyticsClient->connect();
    }

    public function logEvents(LogEventRequest $request): bool
    {
        if (!$this->isStarted) {
            return false;
        }

        try {
            $events = $request->payload->events;
            $metadata = $request->payload->statsig_metadata;

            foreach ($events as $event) {
                // Transform Statsig event to analytics platform format
                $analyticsEvent = [
                    'event_name' => $event['eventName'],
                    'user_id' => $event['user']['userID'] ?? null,
                    'timestamp' => $event['time'],
                    'properties' => array_merge(
                        $event['metadata'] ?? [],
                        ['statsig_metadata' => $metadata]
                    )
                ];

                // Send to analytics platform
                $this->analyticsClient->track($analyticsEvent);
            }

            return true;
        } catch (Exception $e) {
            error_log("Failed to log events to analytics platform: " . $e->getMessage());
            return false;
        }
    }

    public function shutdown(): void
    {
        $this->isStarted = false;
        // Clean up analytics client connection
        $this->analyticsClient->disconnect();
    }
}
```

#### Usage

```php  theme={null}
use Statsig\Statsig;
use Statsig\StatsigOptions;

$analyticsClient = new MyAnalyticsClient('api-key');
$eventAdapter = new AnalyticsEventAdapter($analyticsClient);

$options = new StatsigOptions(
    event_logging_adapter: $eventAdapter
);

$statsig = new Statsig('your-server-secret-key', $options);
$statsig->initialize();

// Events will now be sent to your custom analytics platform
$statsig->logEvent($user, 'button_clicked', ['button_id' => 'signup']);
```

#### Key Methods

* **`start()`**: Called when the SDK starts. Initialize connections or resources
* **`logEvents(LogEventRequest $request): bool`**: Process and send events. Return true on success, false on failure
* **`shutdown()`**: Called when the SDK shuts down. Clean up resources

The `LogEventRequest` contains:

* **`event_count`**: Number of events in the request
* **`retries`**: Number of retry attempts for this request
* **`payload`**: `LogEventPayload` with events and metadata

The `LogEventPayload` contains:

* **`events`**: Array of event objects with user data, event names, and metadata
* **`statsig_metadata`**: SDK metadata including version and environment information

## Shutting Statsig Down

Because we batch and periodically flush events, some events may not have been sent when your app/server shuts down. To make sure all logged events are properly flushed, you should call `shutdown()` before your app/server shuts down:

```php  theme={null}
// Method signature
public function shutdown(): void

// example usage
try {
    $statsig->shutdown();
    echo "Statsig instance has been successfully shutdown.\n";
} catch (Exception $e) {
    error_log($e->getMessage());
}
```

Alternatively, if you are operating in a serverless environment/cloud function, you may wish to leave Statsig running in case your function is recycled but flush the logs to Statsig servers. Or, if you need an async method to wait for logs to post before resolving, you can use:

```php  theme={null}
// Method signature
public function flushEvents(): void

// example usage
try {
    $statsig->flushEvents();
    echo "All events have been successfully flushed.\n";
} catch (Exception $e) {
    echo "Failed to flush events: " . $e->getMessage() . "\n";
}
```

## Persistent Storage

The Persistent Storage interface allows you to implement custom storage for user-specific configurations. This enables you to persist user assignments across sessions, ensuring consistent experiment groups even when the user returns later. This is particularly useful for client-side A/B testing where you want to ensure users always see the same variant.

## Persistent Storage

The Persistent Storage interface allows you to implement custom storage for experiment assignments. This ensures consistent user experiences across sessions by persisting experiment assignments. For more information on persistent assignments, see the [Persistent Assignment](/client/concepts/persistent_assignment) documentation.

<Note>Not supported at this time.</Note>

## Data Store

The Data Store interface allows you to implement custom storage for Statsig configurations. This enables advanced caching strategies and integration with your preferred storage systems.

## Data Store

The Data Store interface allows you to implement custom storage for Statsig configurations. This enables advanced caching strategies and integration with your preferred storage systems.

<Note>Not supported at this time.</Note>

## Custom Output Logger

The Output Logger interface allows you to customize how the SDK logs messages. This enables integration with your own logging system and control over log verbosity.

## Custom Output Logger

The Output Logger interface allows you to customize how the SDK logs messages. This enables integration with your own logging system and control over log verbosity.

<Note>Not supported at this time.</Note>

## Observability Client

The Observability Client interface allows you to monitor the health of the SDK by integrating with your own observability systems. This enables tracking metrics, errors, and performance data. For more information on the metrics emitted by Statsig SDKs, see the [Monitoring documentation](/sdk_monitoring).

## Observability Client

The Observability Client interface allows you to monitor the health of the SDK by integrating with your own observability systems. This enables tracking metrics, errors, and performance data. For more information on the metrics emitted by Statsig SDKs, see the [Monitoring](/infrastructure/monitoring) documentation.

<Note>Not supported at this time.</Note>

## Notes on Beta Version

The PHP SDK expects an adapter to be provided for both logging and saving config specs, given the stateless nature of PHP. In [our example](https://github.com/daniel-statsig/statsig-php-core-slim-example), we've provided simple file-based adapters. More mature implementations may choose a different, and more performant caching approach. If you need help setting this up, reach out to us in [Slack](https://statsig.com/slack).

## FAQ

<AccordionGroup>
  <Accordion title="How do I run experiments for logged out users?">
    See the guide on [device level experiments](/guides/device-level-experiment)
  </Accordion>
</AccordionGroup>


Built with [Mintlify](https://mintlify.com).