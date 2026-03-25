# Source: https://posthog.com/docs/product-analytics/installation/go.md

# Source: https://posthog.com/docs/logs/installation/go.md

# Source: https://posthog.com/docs/feature-flags/installation/go.md

# Source: https://posthog.com/docs/experiments/installation/go.md

# Source: https://posthog.com/docs/error-tracking/installation/go.md

# Source: https://posthog.com/docs/endpoints/start-here/retrieve-data/go.md

# Source: https://posthog.com/docs/libraries/go.md

# Go - Docs

This library uses an internal queue to make calls fast and non-blocking. It also batches requests and flushes asynchronously, making it perfect to use in any part of your web app or other server-side application that needs performance.

## Installation

Terminal

PostHog AI

```bash
go get github.com/posthog/posthog-go
```

Go

PostHog AI

```go
package main
import (
    "os"
    "github.com/posthog/posthog-go"
)
func main() {
    client, _ := posthog.NewWithConfig(
        os.Getenv("POSTHOG_API_KEY"),
        posthog.Config{
            PersonalApiKey: "your personal API key", // Optional, but much more performant.  If this token is not supplied, then fetching feature flag values will be slower.
            Endpoint:       "https://us.i.posthog.com",
        },
    )
    defer client.Close()
    // run commands
}
```

## Identifying users

> **Identifying users is required.** Backend events need a `distinct_id` that matches the ID your frontend uses when calling `posthog.identify()`. Without this, backend events are orphaned — they can't be linked to frontend event captures, [session replays](/docs/session-replay.md), [LLM traces](/docs/ai-engineering.md), or [error tracking](/docs/error-tracking.md).
>
> See our guide on [identifying users](/docs/getting-started/identify-users.md) for how to set this up.

## Capturing events

You can send custom events using `capture`:

Go

PostHog AI

```go
client.Enqueue(posthog.Capture{
  DistinctId: "distinct_id_of_the_user",
  Event: "user_signed_up",
})
```

> **Tip:** We recommend using a `[object] [verb]` format for your event names, where `[object]` is the entity that the behavior relates to, and `[verb]` is the behavior itself. For example, `project created`, `user signed up`, or `invite sent`.

> **Tip:** You can define event schemas with typed properties and generate type-safe code using [schema management](/docs/product-analytics/schema-management.md).

### Setting event properties

Optionally, you can include additional information with the event by including a [properties](/docs/data/events.md#event-properties) object:

Go

PostHog AI

```go
client.Enqueue(posthog.Capture{
    DistinctId: "distinct_id_of_the_user",
    Event:      "user_signed_up",
    Properties: posthog.NewProperties().
      Set("login_type", "email").
      Set("is_free_trial", true),
  })
```

### Capturing pageviews

If you're aiming for a backend-only implementation of PostHog and won't be capturing events from your frontend, you can send `pageviews` from your backend like so:

Go

PostHog AI

```go
client.Enqueue(posthog.Capture{
  DistinctId: "distinct_id_of_the_user",
  Event:      "$pageview",
  Properties: posthog.NewProperties().
    Set("$current_url", "https://example.com"),
})
```

## Person profiles and properties

For backward compatibility, the Go SDK captures identified events by default. These create [person profiles](/docs/data/persons.md). To set [person properties](/docs/data/user-properties.md) in these profiles, include them when capturing an event:

Go

PostHog AI

```go
client.Enqueue(posthog.Capture{
    DistinctId: "distinct_id",
    Event:      "event_name",
    Properties: map[string]interface{}{
        "$set": map[string]interface{}{
            "name": "Max Hedgehog",
        },
        "$set_once": map[string]interface{}{
            "initial_url": "/blog",
        },
    },
})
```

For more details on the difference between `$set` and `$set_once`, see our [person properties docs](/docs/data/user-properties.md#what-is-the-difference-between-set-and-set_once).

To capture [anonymous events](/docs/data/anonymous-vs-identified-events.md) without person profiles, set the event's `$process_person_profile` property to `false`:

Go

PostHog AI

```go
client.Enqueue(posthog.Capture{
    DistinctId: "distinct_id",
    Event:      "event_name",
    Properties: map[string]interface{}{
        "$process_person_profile": false,
    },
})
```

## Alias

Sometimes, you want to assign multiple distinct IDs to a single user. This is helpful when your primary distinct ID is inaccessible. For example, if a distinct ID used on the frontend is not available in your backend.

In this case, you can use `alias` to assign another distinct ID to the same user.

Go

PostHog AI

```go
client.Enqueue(posthog.Alias{
  DistinctId: "distinct_id",
  Alias: "alias_id",
})
```

We strongly recommend reading our docs on [alias](/docs/data/identify.md#alias-assigning-multiple-distinct-ids-to-the-same-user) to best understand how to correctly use this method.

## Feature flags

PostHog's [feature flags](/docs/feature-flags.md) enable you to safely deploy and roll back new features as well as target specific users and groups with them.

There are 2 steps to implement feature flags in Go:

### Step 1: Evaluate the feature flag value

#### Boolean feature flags

Go

PostHog AI

```go
isMyFlagEnabled, err := client.IsFeatureEnabled(posthog.FeatureFlagPayload{
    Key:        "flag-key",
    DistinctId: "distinct_id_of_your_user",
})
if err != nil {
    // Handle error (e.g. capture error and fallback to default behavior)
}
if isMyFlagEnabled == true {
    // Do something differently for this user
}
```

#### Multivariate feature flags

Go

PostHog AI

```go
enabledVariant, err := client.GetFeatureFlag(posthog.FeatureFlagPayload{
    Key:        "flag-key",
    DistinctId: "distinct_id_of_your_user",
})
if err != nil {
    // Handle error (e.g. capture error and fallback to default behavior)
}
if enabledVariant == "variant-key" { // replace 'variant-key' with the key of your variant
    // Do something differently for this user
}
```

### Step 2: Include feature flag information when capturing events

If you want use your feature flag to breakdown or filter events in your [insights](/docs/product-analytics/insights.md), you'll need to include feature flag information in those events. This ensures that the feature flag value is attributed correctly to the event.

> **Note:** This step is only required for events captured using our server-side SDKs or [API](/docs/api.md).

There are two methods you can use to include feature flag information in your events:

#### Method 1: Include the `$feature/feature_flag_name` property

In the event properties, include `$feature/feature_flag_name: variant_key`:

Go

PostHog AI

```go
client.Enqueue(posthog.Capture{
  DistinctId: "distinct_id_of_your_user",
  Event:      "event_name",
  Properties: posthog.NewProperties().
    Set("$feature/feature-flag-key", "variant-key"), // replace feature-flag-key with your flag key. Replace 'variant-key' with the key of your variant
})
```

#### Method 2: Set `SendFeatureFlags` to `true`

The `Capture` struct has an optional field `SendFeatureFlags`, which is set to `false` by default. This parameter controls whether feature flag information is sent with the event.

#### Basic usage

Setting `SendFeatureFlags` to `true` will include feature flag information with the event:

Go

PostHog AI

```go
client.Enqueue(posthog.Capture{
  DistinctId: "distinct_id_of_your_user",
  Event:      "event_name",
  SendFeatureFlags: true,
})
```

## Advanced usage (v1.6.1+)

As of version 1.6.1, `SendFeatureFlags` can also accept a `SendFeatureFlagsOptions` struct for more granular control:

Go

PostHog AI

```go
client.Enqueue(posthog.Capture{
  DistinctId: "distinct_id_of_your_user",
  Event:      "event_name",
  SendFeatureFlags: posthog.SendFeatureFlagsOptions{
    OnlyEvaluateLocally: true,
    PersonProperties: map[string]interface{}{
      "plan": "premium",
    },
    GroupProperties: map[string]map[string]interface{}{
      "org": {
        "tier": "enterprise",
      },
    },
  },
})
```

#### Performance considerations

-   **With local evaluation**: When [local evaluation](/docs/feature-flags/local-evaluation.md) is configured, setting `SendFeatureFlags: true` will **not** make additional server requests. Instead, it uses the locally cached feature flags, and it provides an interface for including person and/or group properties needed to evaluate the flags in the context of the event, if required.

-   **Without local evaluation**: PostHog will make an additional request to fetch feature flag information before capturing the event, which adds delay.

#### Breaking change in v1.6.1

Prior to version 1.6.1, feature flags were automatically sent with events when using local evaluation, even when `SendFeatureFlags` was not explicitly set. This behavior has been **removed** in v1.6.1 to be more predictable and explicit.

If you were relying on this automatic behavior, you must now explicitly set `SendFeatureFlags: true` to continue sending feature flags with your events.

### Fetching all flags for a user

You can fetch all flag values for a single user by calling `GetAllFlags()`.

This is useful when you need to fetch multiple flag values and don't want to make multiple requests.

Go

PostHog AI

```go
featureVariants, err := client.GetAllFlags(posthog.FeatureFlagPayloadNoKey{
        DistinctId: "distinct_id_of_your_user",
})
```

### Sending `$feature_flag_called` events

Capturing `$feature_flag_called` events enable PostHog to know when a flag was accessed by a user and thus provide [analytics and insights](/docs/product-analytics/insights.md) on the flag. By default, we send a these event when:

1.  You call `GetFeatureFlag()` or `IsFeatureEnabled()`, AND
2.  It's a new user, or the value of the flag has changed.

> *Note:* Tracking whether it's a new user or if a flag value has changed happens in a local cache. This means that if you reinitialize the PostHog client, the cache resets as well – causing `$feature_flag_called` events to be sent again when calling `GetFeatureFlag` or `IsFeatureEnabled`. PostHog is built to handle this, and so duplicate `$feature_flag_called` events won't affect your analytics.

You can disable automatically capturing `$feature_flag_called` events. For example, when you don't need the analytics, or it's being called at such a high volume that sending events slows things down.

To disable it (pre v1.6.1), set the `SendFeatureFlagEvents` argument in your function call, like so:

Go

PostHog AI

```go
sendFeatureFlags := false
isMyFlagEnabled, err := client.IsFeatureEnabled(posthog.FeatureFlagPayload{
    Key:                    "flag-key",
    DistinctId:             "distinct_id_of_your_user",
    SendFeatureFlagEvents:  &sendFeatureFlags,
})
```

Versions after v1.6.1 have this feature disabled by default.

### Advanced: Overriding server properties

Sometimes, you may want to evaluate feature flags using [person properties](/docs/product-analytics/person-properties.md), [groups](/docs/product-analytics/group-analytics.md), or group properties that haven't been ingested yet, or were set incorrectly earlier.

You can provide properties to evaluate the flag with by using the `person properties`, `groups`, and `group properties` arguments. PostHog will then use these values to evaluate the flag, instead of any properties currently stored on your PostHog server.

For example:

Go

PostHog AI

```go
enabledVariant, err := client.GetFeatureFlag(
    FeatureFlagPayload{
        Key:        "flag-key",
        DistinctId: "distinct_id_of_the_user",
        Groups: posthog.NewGroups().
            Set("your_group_type", "your_group_id").
            Set("another_group_type", "your_group_id"),
        PersonProperties: posthog.NewProperties().
            Set("property_name", "value"),
        GroupProperties: map[string]map[string]interface{}{
            "your_group_type": {
                "group_property_name": "value",
            },
            "another_group_type": {
                "group_property_name": "value",
            },
        },
    },
)
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

You can configure the `FeatureFlagRequestTimeout` parameter when initializing your PostHog client to set a flag request timeout. This helps prevent your code from being blocked in the case when PostHog's servers are too slow to respond. By default, this is set at 3 seconds.

Go

PostHog AI

```go
client, _ := posthog.NewWithConfig(
   os.Getenv("<ph_project_token>"),
   posthog.Config{
      PersonalApiKey:            "your personal API key", // Optional, but much more performant.  If this token is not supplied, then fetching feature flag values will be slower.
      Endpoint:                  "https://us.i.posthog.com",
      FeatureFlagRequestTimeout: 3 // Time in seconds. Default is 3.
   },
)
```

### Error handling

When using the PostHog SDK, it's important to handle potential errors that may occur during feature flag operations. Here's an example of how to wrap PostHog SDK methods in an error handler:

Go

PostHog AI

```go
func handleFeatureFlag(client *posthog.Client, flagKey string, distinctId string) {
    flag, err := client.GetFeatureFlag(posthog.FeatureFlagPayload{
        Key:        flagKey,
        DistinctId: distinctId,
    })
    if err != nil {
        // Handle the error appropriately
        log.Printf("Error fetching feature flag: %v", err)
        return
    }
    // Use the flag value as needed
    fmt.Printf("Feature flag '%s' for user '%s': %s\n", flagKey, distinctId, flag)
}
```

### Local Evaluation

Evaluating feature flags requires making a request to PostHog for each flag. However, you can improve performance by evaluating flags locally. Instead of making a request for each flag, PostHog will periodically request and store feature flag definitions locally, enabling you to evaluate flags without making additional requests.

It is best practice to use local evaluation flags when possible, since this enables you to resolve flags faster and with fewer API calls.

For details on how to implement local evaluation, see our [local evaluation guide](/docs/feature-flags/local-evaluation.md).

## Experiments (A/B tests)

Since [experiments](/docs/experiments/manual.md) use feature flags, the code for running an experiment is very similar to the feature flags code:

Go

PostHog AI

```go
variant, err := client.GetFeatureFlag(posthog.FeatureFlagPayload{
    Key:        "experimentfeature-flag-name",
    DistinctId: "user_distinct_id",
})
if err != nil {
    // Handle error (e.g. capture error and fallback to default behavior)
}
if variant == "variant-name" {
    // Do something
}
```

It's also possible to [run experiments without using feature flags](/docs/experiments/running-experiments-without-feature-flags.md).

## Error tracking

You can capture exceptions and errors using the Go SDK. There are two approaches:

**Direct capture** using `NewDefaultException`, which automatically generates a stack trace:

Go

PostHog AI

```go
exception := posthog.NewDefaultException(
    time.Now(),
    "user_distinct_id",
    "DatabaseError",      // type - rendered as title in the UI
    "connection refused",  // value - rendered as description in the UI
)
client.Enqueue(exception)
```

**Automatic capture** using the `SlogCaptureHandler`, which wraps Go's `log/slog` and sends log records at warning level and above as exceptions:

Go

PostHog AI

```go
baseHandler := slog.NewTextHandler(os.Stdout, &slog.HandlerOptions{
    Level: slog.LevelInfo,
})
logger := slog.New(posthog.NewSlogCaptureHandler(baseHandler, client,
    posthog.WithDistinctIDFn(func(ctx context.Context, r slog.Record) string {
        return "user_distinct_id"
    }),
))
// Automatically captured as an exception in PostHog
logger.Warn("Something broke", "error", fmt.Errorf("connection refused"))
```

For the full setup guide, see the [Go error tracking installation docs](/docs/error-tracking/installation/go.md).

## Group analytics

Group analytics allows you to associate an event with a group (e.g. teams, organizations, etc.). Read the [Group Analytics](/docs/user-guides/group-analytics.md) guide for more information.

> **Note:** This is a paid feature and is not available on the open-source or free cloud plan. Learn more on the [pricing page](/pricing.md).

-   Send an event associated with a group

Go

PostHog AI

```go
client.Enqueue(posthog.Capture{
    DistinctId: "user_distinct_id",
    Event:      "some_event",
    Groups: posthog.NewGroups().
        Set("company", "company_id_in_your_db"),
})
```

-   Update properties on a group

Go

PostHog AI

```go
client.Enqueue(posthog.GroupIdentify{
    Type: "company",
    Key:  "company_id_in_your_db",
    Properties: posthog.NewProperties().
        Set("name", "Awesome Inc.").
        Set("employees", 11),
})
```

The `name` is a special property which is used in the PostHog UI for the name of the group. If you don't specify a `name` property, the group ID will be used instead.

## Thank you

This library is largely based on the `analytics-go` package.

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better