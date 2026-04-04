# Source: https://posthog.com/docs/product-analytics/installation/php.md

# Source: https://posthog.com/docs/feature-flags/installation/php.md

# Source: https://posthog.com/docs/experiments/installation/php.md

# Source: https://posthog.com/docs/libraries/php.md

# PHP - Docs

This is an optional library you can install if you're working with PHP. It uses an internal queue to batch requests, flushes at the end of the request, and optionally does so in an async manner.

## Installation

Add the following to `composer.json`:

JSON

PostHog AI

```json
{
    "require": {
        "posthog/posthog-php": "3.0.*"
    }
}
```

And then install the dependencies with the command:

Terminal

PostHog AI

```bash
composer install
```

In your app, set your project token before making any calls.

PHP

PostHog AI

```php
PostHog\PostHog::init("<ph_project_token>",
  ['host' => 'https://us.i.posthog.com']
);
```

> **Note:** As a rule of thumb, we do not recommend having API keys or tokens in plaintext. Setting it as an environment variable is best.

You can find your project token and instance address in the [project settings](https://app.posthog.com/project/settings) page in PostHog.

## Identifying users

> **Identifying users is required.** Backend events need a `distinct_id` that matches the ID your frontend uses when calling `posthog.identify()`. Without this, backend events are orphaned — they can't be linked to frontend event captures, [session replays](/docs/session-replay.md), [LLM traces](/docs/ai-engineering.md), or [error tracking](/docs/error-tracking.md).
>
> See our guide on [identifying users](/docs/getting-started/identify-users.md) for how to set this up.

## Capturing events

You can send custom events using `capture`:

PHP

PostHog AI

```php
PostHog::capture([
  'distinctId' => 'distinct_id_of_the_user',
  'event' => 'user_signed_up'
]);
```

> **Tip:** We recommend using a `[object] [verb]` format for your event names, where `[object]` is the entity that the behavior relates to, and `[verb]` is the behavior itself. For example, `project created`, `user signed up`, or `invite sent`.

### Setting event properties

Optionally, you can include additional information with the event by including a [properties](/docs/data/events.md#event-properties) object:

PHP

PostHog AI

```php
PostHog::capture([
  'distinctId' => 'distinct_id_of_the_user',
  'event' => 'user_signed_up',
  'properties' => [
    'login_type' => 'email',
    'is_free_trial' => 'true'
  ]
]);
```

### Sending page views

If you're aiming for a backend-only implementation of PostHog and won't be capturing events from your frontend, you can send `pageviews` from your backend like so:

PHP

PostHog AI

```php
PostHog::capture([
  'distinctId' => 'distinct_id_of_the_user',
  'event' => '$pageview',
  'properties' => [
    '$current_url' => 'https://example.com'
  ]
]);
```

## Person profiles and properties

The PHP SDK captures identified events by default. These create [person profiles](/docs/data/persons.md). To set [person properties](/docs/data/user-properties.md) in these profiles, include them when capturing an event:

PHP

PostHog AI

```php
PostHog::capture([
    'distinctId' => 'distinct_id',
    'event' => 'event_name',
    'properties' => [
        '$set' => [
            'name' => 'Max Hedgehog'
        ],
        '$set_once' => [
            'initial_url' => '/blog'
        ]
    ]
]);
```

For more details on the difference between `$set` and `$set_once`, see our [person properties docs](/docs/data/user-properties.md#what-is-the-difference-between-set-and-set_once).

To capture [anonymous events](/docs/data/anonymous-vs-identified-events.md) without person profiles, set the event's `$process_person_profile` property to `false`:

PHP

PostHog AI

```php
PostHog::capture([
    'distinctId' => 'distinct_id',
    'event' => 'event_name',
    'properties' => [
        '$process_person_profile' => false
    ]
]);
```

## Alias

Sometimes, you want to assign multiple distinct IDs to a single user. This is helpful when your primary distinct ID is inaccessible. For example, if a distinct ID used on the frontend is not available in your backend.

In this case, you can use `alias` to assign another distinct ID to the same user.

PHP

PostHog AI

```php
PostHog::alias([
  'distinctId' => 'distinct_id',
  'alias' => 'alias_id'
]);
```

We strongly recommend reading our docs on [alias](/docs/data/identify.md#alias-assigning-multiple-distinct-ids-to-the-same-user) to best understand how to correctly use this method.

## Feature flags

PostHog's [feature flags](/docs/feature-flags.md) enable you to safely deploy and roll back new features as well as target specific users and groups with them.

There are 2 steps to implement feature flags in PHP:

### Step 1: Evaluate the feature flag value

#### Boolean feature flags

PHP

PostHog AI

```php
$isMyFlagEnabledForUser = PostHog::isFeatureEnabled('flag-key', 'distinct_id_of_your_user')
if ($isMyFlagEnabledForUser) {
    // Do something differently for this user
}
```

#### Multivariate feature flags

PHP

PostHog AI

```php
$enabledVariant = PostHog::getFeatureFlag('flag-key', 'distinct_id_of_your_user')
if ($enabledVariant === 'variant-key') { # replace 'variant-key' with the key of your variant
    # Do something differently for this user
}
```

### Step 2: Include feature flag information when capturing events

If you want use your feature flag to breakdown or filter events in your [insights](/docs/product-analytics/insights.md), you'll need to include feature flag information in those events. This ensures that the feature flag value is attributed correctly to the event.

> **Note:** This step is only required for events captured using our server-side SDKs or [API](/docs/api.md).

There are two methods you can use to include feature flag information in your events:

#### Method 1: Include the `$feature/feature_flag_name` property

In the event properties, include `$feature/feature_flag_name: variant_key`:

PHP

PostHog AI

```php
PostHog::capture([
  'distinctId' => 'distinct_id_of_your_user',
  'event' => 'event_name',
  'properties' => [
    '$feature/feature-flag-key' => 'variant-key' // replace feature-flag-key with your flag key. Replace 'variant-key' with the key of your variant
  ]
]);
```

#### Method 2: Set `send_feature_flags` to `true`

The `capture()` method has an optional argument `send_feature_flags`, which is set to `false` by default. By setting this to `true`, feature flag information will automatically be sent with the event.

Note that by doing this, PostHog will make an additional request to fetch feature flag information before capturing the event. So this method is only recommended if you don't mind the extra API call and delay.

PHP

PostHog AI

```php
PostHog::capture([
  'distinctId' => 'distinct_id_of_your_user',
  'event' => 'event_name',
  'send_feature_flags' => true
]);
```

### Fetching all flags for a user

You can fetch all flag values for a single user by calling `getAllFlags()`.

This is useful when you need to fetch multiple flag values and don't want to make multiple requests.

PHP

PostHog AI

```php
PostHog::getAllFlags('distinct_id_of_your_user')
```

### Sending `$feature_flag_called` events

Capturing `$feature_flag_called` events enable PostHog to know when a flag was accessed by a user and thus provide [analytics and insights](/docs/product-analytics/insights.md) on the flag. By default, we send a these event when:

1.  You call `getFeatureFlag()` or `isFeatureEnabled()`, AND
2.  It's a new user, or the value of the flag has changed.

> *Note:* Tracking whether it's a new user or if a flag value has changed happens in a local cache. This means that if you reinitialize the PostHog client, the cache resets as well – causing `$feature_flag_called` events to be sent again when calling `getFeatureFlag` or `isFeatureEnabled`. PostHog is built to handle this, and so duplicate `$feature_flag_called` events won't affect your analytics.

You can disable automatically capturing `$feature_flag_called` events. For example, when you don't need the analytics, or it's being called at such a high volume that sending events slows things down.

To disable it, set the `sendFeatureFlagEvents` argument in your function call, like so:

PHP

PostHog AI

```php
$isMyFlagEnabledForUser = PostHog::isFeatureEnabled(
    key: 'flag-key',
    distinctId: 'distinct_id_of_your_user',
    sendFeatureFlagEvents: false
)
```

### Advanced: Overriding server properties

Sometimes, you may want to evaluate feature flags using [person properties](/docs/product-analytics/person-properties.md), [groups](/docs/product-analytics/group-analytics.md), or group properties that haven't been ingested yet, or were set incorrectly earlier.

You can provide properties to evaluate the flag with by using the `person properties`, `groups`, and `group properties` arguments. PostHog will then use these values to evaluate the flag, instead of any properties currently stored on your PostHog server.

For example:

PHP

PostHog AI

```php
PostHog::getFeatureFlag(
    'flag-key',
    'distinct_id_of_the_user',
    [
        'your_group_type' => 'your_group_id',
        'another_group_type' => 'your_group_id'
    ], // groups
    ['property_name' => 'value'], // person properties
    [
        'your_group_type' => ['group_property_name' => 'value'],
        'another_group_type' => ['group_property_name' => 'value']
    ], // group properties
    false, // onlyEvaluateLocally, Optional. Defaults to false.
    true // sendFeatureFlagEvents
);
```

### Overriding GeoIP properties

By default, a user's GeoIP properties are set using the IP address they use to capture events on the frontend. You may want to override the these properties when evaluating feature flags. A common reason to do this is when you're not using PostHog on your frontend, so the user has no GeoIP properties.

You can override GeoIP properties by including them in the `person_properties` parameter when evaluating feature flags. This is useful when you're evaluating flags on your backend and want to use the client's location instead of your server's location.

The following GeoIP properties can be overridden:

-   `$geoip_country_code`
-   `$geoip_country_name`
-   `$geoip_city_name`
-   `$geoip_city_confidence`
-   `$geoip_continent_code`
-   `$geoip_continent_name`
-   `$geoip_latitude`
-   `$geoip_longitude`
-   `$geoip_postal_code`
-   `$geoip_subdivision_1_code`
-   `$geoip_subdivision_1_name`
-   `$geoip_subdivision_2_code`
-   `$geoip_subdivision_2_name`
-   `$geoip_subdivision_3_code`
-   `$geoip_subdivision_3_name`
-   `$geoip_time_zone`

Simply include any of these properties in the `person_properties` parameter alongside your other person properties when calling feature flags.

### Request timeout

You can configure the `feature_flag_request_timeout_ms` parameter when initializing your PostHog client to set a flag request timeout. This helps prevent your code from being blocked in the case when PostHog's servers are too slow to respond. By default, this is set at 3 seconds.

PHP

PostHog AI

```php
PostHog::init("<ph_project_token>",
  [
    'host' => 'https://us.i.posthog.com',
    'feature_flag_request_timeout_ms' => 3000 // Time in milliseconds. Default is 3000 (3 seconds).
  ]
);
```

### Error handling

When using the PostHog SDK, it's important to handle potential errors that may occur during feature flag operations. Here's an example of how to wrap PostHog SDK methods in an error handler:

PHP

PostHog AI

```php
function handleFeatureFlag($client, $flagKey, $distinctId) {
    try {
        $isEnabled = $client->isFeatureEnabled($flagKey, $distinctId);
        echo "Feature flag '$flagKey' for user '$distinctId' is " . ($isEnabled ? 'enabled' : 'disabled') . "\n";
        return $isEnabled;
    } catch (Exception $e) {
        echo "Error fetching feature flag '$flagKey': " . $e->getMessage() . "\n";
        // Optionally, you can return a default value or throw the error
        // return false; // Default to disabled
        throw $e;
    }
}
// Usage example
try {
    $flagEnabled = handleFeatureFlag($client, 'new-feature', 'user-123');
    if ($flagEnabled) {
        // Implement new feature logic
    } else {
        // Implement old feature logic
    }
} catch (Exception $e) {
    // Handle the error at a higher level
    echo 'Feature flag check failed, using default behavior';
    // Implement fallback logic
}
```

### Local Evaluation

Evaluating feature flags requires making a request to PostHog for each flag. However, you can improve performance by evaluating flags locally. Instead of making a request for each flag, PostHog will periodically request and store feature flag definitions locally, enabling you to evaluate flags without making additional requests.

It is best practice to use local evaluation flags when possible, since this enables you to resolve flags faster and with fewer API calls.

For details on how to implement local evaluation, see our [local evaluation guide](/docs/feature-flags/local-evaluation.md).

### Experiments (A/B tests)

Since [experiments](/docs/experiments/manual.md) use feature flags, the code for running an experiment is very similar to the feature flags code:

PHP

PostHog AI

```php
$variant = PostHog::getFeatureFlag('experiment-feature-flag-key', 'user_distinct_id')
if ($variant === 'variant-name') {
    // Do something differently for this user
}
```

It's also possible to [run experiments without using feature flags](/docs/experiments/running-experiments-without-feature-flags.md).

### Group analytics

Group analytics allows you to associate an event with a group (e.g. teams, organizations, etc.). This feature requires a posthog-php version of `2.1.0` or above. Read the [Group Analytics](/docs/user-guides/group-analytics.md) guide for more information.

> **Note:** This is a paid feature and is not available on the open-source or free cloud plan. Learn more on the [pricing page](/pricing.md).

-   Capture an event and associate it with a group

PHP

PostHog AI

```php
PostHog::capture([
    'distinctId' => 'user_distinct_id',
    'event' => 'some_event',
    '$groups' => ['company' => 'company_id_in_your_db']
]);
```

-   Update properties on a group

PHP

PostHog AI

```php
PostHog::groupIdentify([
    'groupType' => 'company',
    'groupKey' => 'company_id_in_your_db',
    'properties' => ['name' => 'Awesome Inc.', 'employees' => 11]
]);
```

The `name` is a special property which is used in the PostHog UI for the name of the group. If you don't specify a `name` property, the group ID will be used instead.

## Config options

When calling `PostHog::init`, there are various configuration options you can set apart from the host. Pass them into your client initialisation like so:

PHP

PostHog AI

```php
PostHog::init(
    '<ph_project_token>',
    [
        'host' => 'https://us.i.posthog.com',
        'debug' => true,
        'ssl' => false,
        // all options go here
    ],
);
```

All possible options below:

| Attribute | Description |
| --- | --- |
| hostType: StringDefault: app.posthog.com | URL of your PostHog instance. |
| sslType: BooleanDefault: true | Whether to use SSL for API requests or not |
| timeoutType: IntegerDefault: 10000 | Request timeout in milliseconds |
| verify_batch_events_requestType: BooleanDefault: true | Whether to verify successful delivery of batch events (true, synchronous) or fire and forget (false, asynchronous) with the lib_curl consumer |
| feature_flag_request_timeout_msType: IntegerDefault: 3000 | Request timeout for feature flags in milliseconds |
| maximum_backoff_durationType: IntegerDefault: 10000 | Request retry backoff. Retries will stop after this duration is hit |
| consumerType: StringDefault: lib_curl | One of socket, file, lib_curl, and fork_curl. Determines what transport option to use for analytics capture. [More details here](https://github.com/PostHog/posthog-php/blob/master/lib/Consumer/File.php) |
| debugType: BooleanDefault: false | Output debug logs or not |

## Debug mode

PHP

PostHog AI

```php
PostHog::init(
    '<ph_project_token>',
    [
        'host' => 'https://us.i.posthog.com',
        'debug' => true,
    ],
);
```

## Thank you

This library is largely based on the `analytics-php` package.

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better