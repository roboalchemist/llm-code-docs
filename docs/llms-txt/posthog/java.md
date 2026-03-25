# Source: https://posthog.com/docs/product-analytics/installation/java.md

# Source: https://posthog.com/docs/logs/installation/java.md

# Source: https://posthog.com/docs/feature-flags/installation/java.md

# Source: https://posthog.com/docs/libraries/java.md

# Java - Docs

This is an optional library you can install if you're working with server-side Java applications. It uses an internal queue to make calls fast and non-blocking. It also batches requests and flushes asynchronously, making it perfect to use in any part of your web app or other server side application that needs performance.

## Installation

The best way to install the PostHog Java SDK is with a build system like Gradle or Maven. This ensures you can easily upgrade to the latest versions.

Look up the latest version of [`com.posthog.posthog-server`](https://central.sonatype.com/artifact/com.posthog/posthog-server).

#### Gradle

All you need to do is add the `posthog-server` module to your `build.gradle`:

build.gradle

PostHog AI

```kotlin
dependencies {
  implementation 'com.posthog:posthog-server:2.+'
}
```

#### Maven

All you need to do is add the `posthog-server` module to your `pom.xml`:

pom.xml

PostHog AI

```xml
<dependency>
  <groupId>com.posthog</groupId>
  <artifactId>posthog-server</artifactId>
  <version>LATEST</version>
</dependency>
```

#### Other

See [`com.posthog.posthog-server`](https://central.sonatype.com/artifact/com.posthog/posthog-server) in the Maven Central Repository. Clicking on the latest version shows you options for adding dependencies for other build systems.

### Setup

Java

PostHog AI

```java
import com.posthog.server.PostHog;
import com.posthog.server.PostHogConfig;
import com.posthog.server.PostHogInterface;
class Sample {
  private static final String POSTHOG_API_KEY = "<ph_project_token>";
  private static final String POSTHOG_HOST = "https://us.i.posthog.com";
  public static void main(String args[]) {
    PostHogConfig config = PostHogConfig
            .builder(POSTHOG_API_KEY)
            .host(POSTHOG_HOST)
            .build();
    PostHogInterface posthog = PostHog.with(config);
    posthog.flush(); // send any remaining events
    posthog.close(); // shut down the client
  }
}
```

## Integrating with Spring

To see how to integrate the PostHog SDK with Spring, check out this [sample project](https://github.com/PostHog/posthog-android/tree/main/posthog-samples/posthog-spring-sample).

## Debug mode

If you're not seeing the expected events being captured, or the feature flags being evaluated, you can enable debug mode to see what's happening.

To see detailed logging, set the debug configuration option to true.

Java

PostHog AI

```java
PostHogConfig config = PostHogConfig
          .builder(POSTHOG_API_KEY)
          .host(POSTHOG_HOST)
          .debug(true)
          .build();
```

## Identifying users

> **Identifying users is required.** Backend events need a `distinct_id` that matches the ID your frontend uses when calling `posthog.identify()`. Without this, backend events are orphaned — they can't be linked to frontend event captures, [session replays](/docs/session-replay.md), [LLM traces](/docs/ai-engineering.md), or [error tracking](/docs/error-tracking.md).
>
> See our guide on [identifying users](/docs/getting-started/identify-users.md) for how to set this up.

## Capturing events

You can send custom events using `capture`:

Java

PostHog AI

```java
posthog.capture("distinct_id_of_the_user", "user_signed_up");
```

> **Tip:** We recommend using a `[object] [verb]` format for your event names, where `[object]` is the entity that the behavior relates to, and `[verb]` is the behavior itself. For example, `project created`, `user signed up`, or `invite sent`.

### Setting event properties

Optionally, you can include additional information with the event by including a [properties](/docs/data/events.md#event-properties) object:

Java

PostHog AI

```java
posthog.capture(
    "distinct_id_of_the_user",
    "user_signed_up",
    PostHogCaptureOptions
        .builder()
        .property("login_type", "email")
        .property("is_free_trial", true)
        .build());
```

## Person profiles and properties

The Java SDK captures identified events by default. These create [person profiles](/docs/data/persons.md). To set [person properties](/docs/data/user-properties.md) in these profiles, include them when capturing an event:

Java

PostHog AI

```java
posthog.capture(
    "distinct_id_of_the_user",
    "event_name",
    PostHogCaptureOptions
        .builder()
        .userProperty("name", "Max Hedgehog")
        .userPropertySetOnce("initial_url", "/blog")
        .build()
);
```

For more details on the difference between `$set` and `$set_once`, see our [person properties docs](/docs/data/user-properties.md#what-is-the-difference-between-set-and-set_once).

To capture [anonymous events](/docs/data/anonymous-vs-identified-events.md) without person profiles, set the event's `$process_person_profile` property to `false`:

Java

PostHog AI

```java
posthog.capture(
    "distinct_id_of_the_user",
    "event_name",
    PostHogCaptureOptions
        .builder()
        .property("$process_person_profile", false)
        .build()
);
```

## Alias

Sometimes, you want to assign multiple distinct IDs to a single user. This is helpful when your primary distinct ID is inaccessible. For example, if a distinct ID used on the frontend is not available in your backend.

In this case, you can use `alias` to assign another distinct ID to the same user.

Java

PostHog AI

```java
posthog.alias("distinct_id", "alias_id");
```

We strongly recommend reading our docs on [alias](/docs/data/identify.md#alias-assigning-multiple-distinct-ids-to-the-same-user) to best understand how to correctly use this method.

## Group analytics

Group analytics allows you to associate an event with a group (e.g. teams, organizations, etc.). Read the [group analytics](/docs/product-analytics/group-analytics.md) guide for more information.

> **Note:** This is a paid feature and is not available on the open-source or free cloud plan. Learn more on our [pricing page](/pricing.md).

To create a group, use the `group` method. This associates a user with a group and optionally sets properties on the group:

Java

PostHog AI

```java
posthog.group(
    "user_distinct_id",
    "company",
    "company_id_in_your_db",
    Map.of(
        "name", "Acme Corporation",
        "industry", "Technology",
        "employee_count", 500
    )
);
```

You can also create a group without setting properties:

Java

PostHog AI

```java
posthog.group("user_distinct_id", "organization", "org_123");
```

To associate an event with a group, include the group information when capturing the event:

Java

PostHog AI

```java
posthog.capture(
    "user_distinct_id",
    "some_event",
    PostHogCaptureOptions
        .builder()
        .group("company", "company_id_in_your_db")
        .build()
);
```

## Feature flags

PostHog's [feature flags](/docs/feature-flags.md) enable you to safely deploy and roll back new features as well as target specific users and groups with them.

### Boolean feature flags

Java

PostHog AI

```java
boolean isEnabled = posthog.isFeatureEnabled("user_distinct_id", "use_optimized_query", false);
if (isEnabled) {
    // Do something differently for this user
}
```

### Multivariate feature flags

Java

PostHog AI

```java
Object flagValue = posthog.getFeatureFlag("user_distinct_id", "recommendation_algorithm", "control");
String algorithm = flagValue instanceof String ? (String) flagValue : "control";
switch (algorithm) {
    case "collaborative_filtering":
        useCollaborativeFiltering();
        break;
    case "neural_network":
        useNeuralNetwork();
        break;
    default:
        useControlAlgorithm();
}
```

### Feature flag payloads

Java

PostHog AI

```java
Object payload = posthog.getFeatureFlagPayload("user_distinct_id", "recommendation_algorithm");
if (payload instanceof Map) {
    Map<String, Object> config = (Map<String, Object>) payload;
    String modelVersion = config.get("model_version") instanceof String
        ? (String) config.get("model_version") : "v1.0";
    boolean enableFallback = config.get("enable_fallback") instanceof Boolean
        ? (Boolean) config.get("enable_fallback") : true;
}
```

### Sending `$feature_flag_called` events

Capturing `$feature_flag_called` events enable PostHog to know when a flag was accessed by a user and thus provide [analytics and insights](/docs/product-analytics/insights.md) on the flag. By default, we send these events when:

1.  You call `posthog.getFeatureFlag()` or `posthog.isFeatureEnabled()`, AND
2.  It's a new user, or the value of the flag has changed.

> *Note:* Tracking whether it's a new user or if a flag value has changed happens in a local cache. This means that if you reinitialize the PostHog client, the cache resets as well – causing `$feature_flag_called` events to be sent again when calling `getFeatureFlag` or `isFeatureEnabled`. PostHog is built to handle this, and so duplicate `$feature_flag_called` events won't affect your analytics.

You can control the automatic capture of `$feature_flag_called` events using the `sendFeatureFlagEvent` configuration option when initializing PostHog:

Java

PostHog AI

```java
PostHogConfig config = PostHogConfig
    .builder(POSTHOG_API_KEY)
    .host(POSTHOG_HOST)
    .sendFeatureFlagEvent(false)  // Disable automatic feature flag events
    .build();
```

### Local evaluation

Evaluating feature flags requires making a request to PostHog for each flag. However, you can improve performance by evaluating flags locally. Instead of making a request for each flag, PostHog will periodically request and store feature flag definitions locally, enabling you to evaluate flags without making additional requests.

It is best practice to use local evaluation flags when possible, since this enables you to resolve flags faster and with fewer API calls.

Local evaluation improves performance by fetching flag definitions once and evaluating them locally, rather than making API calls for each flag check.

#### Configuration

To enable local evaluation, you need:

1.  A **personal API key** (not your project token)
    -   Generate one at: PostHog → Settings → Account → [Personal API Keys](https://app.posthog.com/settings/user-api-keys)
2.  Enable `localEvaluation` in your config

Java

PostHog AI

```java
PostHogConfig config = PostHogConfig
    .builder(POSTHOG_API_KEY) // This is your project token
    .host(POSTHOG_HOST)
    .personalApiKey("phx_your_personal_api_key_here") // This is your personal API key, required for local evaluation
    .localEvaluation(true)
    .pollIntervalSeconds(30)  // Optional: customize the rate which flag definitions are polled (default: 30s)
    .build();
```

> **Note:** Setting the `personalApiKey` automatically enables `localEvaluation` unless explicitly set to `false`.

#### Usage with person and group properties

For local evaluation to work, you must provide person properties, groups, or group properties that are used in your flag's [release conditions](/docs/feature-flags/creating-feature-flags.md#release-conditions).

Use `PostHogFeatureFlagOptions` to provide these properties:

**Basic flag evaluation:**

Java

PostHog AI

```java
boolean isEnabled = posthog.isFeatureEnabled("distinct-id", "flag-key");
```

**With person properties:**

Java

PostHog AI

```java
PostHogFeatureFlagOptions options = PostHogFeatureFlagOptions
    .builder()
    .defaultValue(false)
    .personProperty("plan", "premium")
    .personProperty("email", "my-user@example.com")
    .build();
boolean isEnabled = posthog.isFeatureEnabled("distinct-id", "flag-key", options);
```

**With groups:**

Java

PostHog AI

```java
PostHogFeatureFlagOptions options = PostHogFeatureFlagOptions
    .builder()
    .defaultValue(false)
    .group("company", "company_id_in_your_db")
    .build();
boolean isEnabled = posthog.isFeatureEnabled("distinct-id", "flag-key", options);
```

**With group properties:**

Java

PostHog AI

```java
PostHogFeatureFlagOptions options = PostHogFeatureFlagOptions
    .builder()
    .defaultValue(false)
    .group("company", "company_id_in_your_db")
    .groupProperty("company", "industry", "technology")
    .groupProperty("company", "employees", 500)
    .build();
boolean isEnabled = posthog.isFeatureEnabled("distinct-id", "flag-key", options);
```

**Multivariate flags:**

Java

PostHog AI

```java
PostHogFeatureFlagOptions options = PostHogFeatureFlagOptions
    .builder()
    .defaultValue("control")
    .personProperty("plan", "premium")
    .group("company", "company_id_in_your_db")
    .groupProperty("company", "industry", "technology")
    .build();
Object flagValue = posthog.getFeatureFlag("distinct-id", "algorithm", options);
String algorithm = flagValue instanceof String ? (String) flagValue : "control";
switch (algorithm) {
    case "neural_network":
        useNeuralNetwork();
        break;
    case "collaborative_filtering":
        useCollaborativeFiltering();
        break;
    default:
        useControlAlgorithm();
}
```

#### Limitations

Local evaluation is **not possible** for flags that:

1.  Have **experience continuity** enabled (set when you check "persist flag across authentication steps")
2.  Are linked to an **early access feature**
3.  Depend on **static cohorts**

For these flags, PostHog automatically falls back to remote evaluation via the API.

For more details, see our [local evaluation guide](/docs/feature-flags/local-evaluation.md).

### Feature flag caching

To improve performance and reduce API calls, the Java SDK caches feature flag results in memory. You can configure the cache behavior when initializing PostHog:

Java

PostHog AI

```java
PostHogConfig config = PostHogConfig
    .builder(POSTHOG_API_KEY)
    .featureFlagCacheSize(1000)        // Maximum number of cached flag results (default: 1000)
    .featureFlagCacheMaxAgeMs(300000)  // Cache expiry in milliseconds (default: 300000 = 5 minutes)
    .build();
```

**Configuration options:**

-   `featureFlagCacheSize`: The maximum number of feature flag results to cache in memory (default: `1000`)
-   `featureFlagCacheMaxAgeMs`: The maximum age of a cached feature flag result in milliseconds (default: `300000` or 5 minutes)

Cached results are stored per distinct ID and flag key combination. When a cached result expires or the cache is full, the SDK will fetch fresh results from the PostHog API.

## Experiments (A/B tests)

Since [experiments](/docs/experiments/manual.md) use feature flags, the code for running an experiment is very similar to the feature flags code:

Java

PostHog AI

```java
Object flagValue = posthog.getFeatureFlag("user_distinct_id", "recommendation_algorithm", "control");
String variant = flagValue instanceof String ? (String) flagValue : "control";
if ("neural_network".equals(variant)) {
    // Do something differently for this user
}
```

It's also possible to [run experiments without using feature flags](/docs/experiments/running-experiments-without-feature-flags.md).

## GeoIP properties

The `posthog-server` library disregards the server IP, does not add the GeoIP properties, and does not use the values for feature flag evaluations.

## Serverless environments

By default, the library buffers events before sending them to the `/batch` endpoint for better performance. This can lead to lost events in serverless environments if the Java process is terminated by the platform before the buffer is fully flushed.

To avoid this, call `posthog.flush()` after processing every request. This allows `posthog.capture()` to remain asynchronous for better performance.

Java

PostHog AI

```java
posthog.flush();
```

## Shutdown

When you're done using PostHog, make sure to call `close()` to ensure all events are flushed before your application exits:

Java

PostHog AI

```java
posthog.close();
```

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better