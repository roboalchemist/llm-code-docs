# Source: https://posthog.com/docs/feature-flags/local-evaluation.md

# Server-side local evaluation - Docs

> **Note:** Local evaluation is only available in the [Node](/docs/libraries/node.md), [Ruby](/docs/libraries/ruby.md), [Go](/docs/libraries/go.md), [Python](/docs/libraries/python.md), [C#/.NET](/docs/libraries/dotnet.md), [PHP](/docs/libraries/php.md), [Java](/docs/libraries/java.md), and [Rust](/docs/libraries/rust.md) SDKs.

> **Note:** In edge/lambda environments and stateless PHP applications, local evaluation with the default in-memory cache causes performance issues and inflated costs due to per-request initialization. For these environments, use an [external cache provider](/docs/feature-flags/local-evaluation/distributed-environments.md) to share flag definitions across requests, or use regular flag evaluation instead.

Evaluating feature flags requires making a request to PostHog for each flag. However, you can improve performance by evaluating flags locally. Instead of making a request for each flag, PostHog will periodically request and store feature flag definitions locally, enabling you to evaluate flags without making additional requests.

It is best practice to use local evaluation flags when possible, since this enables you to resolve flags faster and with fewer API calls.

## How local evaluation works

To understand local evaluation, it helps to see how **remote evaluation** (the default) works first.

With remote evaluation, your server sends a request to PostHog's `/flags` API every time you check a flag. PostHog looks up all the data it needs — flag definitions, person properties, group properties, and cohort memberships — from its own database, evaluates the flag, and returns the result:

sequenceDiagram participant App as Your app participant SDK as PostHog SDK participant PH as PostHog App->>SDK: flag key + user ID SDK->>PH: POST /flags Note right of PH: Resolves using stored flag definitions,<br/>person properties, group properties,<br/>and cohort memberships PH-->>SDK: true / false / variant SDK-->>App: true / false / variant

Every flag check is a network round trip. PostHog already has all the data it needs, so you just pass the flag key and a user ID.

With local evaluation, the SDK periodically fetches **flag definitions** from PostHog's `/api/feature_flag/local_evaluation` endpoint in the background. When you check a flag, **you provide the properties** and the SDK evaluates locally — no round trip:

sequenceDiagram participant App as Your app participant SDK as PostHog SDK participant PH as PostHog Note over SDK,PH: Background (every 30s) SDK->>PH: GET /local\_evaluation PH-->>SDK: Flag definitions Note over App,SDK: At evaluation time App->>SDK: flag key + person properties + group properties Note right of SDK: Evaluates locally using<br/>cached flag definitions +<br/>properties you provided SDK-->>App: true / false / variant

Notice that PostHog is not involved at evaluation time. The tradeoff: **you are responsible for providing every property the flag's release conditions depend on**. If you forget to pass a property, the SDK can't evaluate the flag locally and will either fall back to a remote request or return `undefined` (depending on your configuration).

Local evaluation is also more cost-effective: with remote evaluation, every flag check is a billable request, whereas local evaluation only bills for the periodic request to fetch flag definitions (counted as 10 flag requests each). For high-traffic services, this can significantly reduce your flag usage costs.

There are 3 steps to enable local evaluation:

## Step 1: Find your feature flags secure API key

The feature flags secure API key is a secret project specific token listed in the [Feature Flags tab of your project settings](https://us.posthog.com/settings/environment-feature-flags) in the "Feature Flags Secure API Key" section. It provides the SDKs with access to the feature flag definitions for your project so they can evaluate flags locally.

This key needs to be kept secret, and should not be used in the frontend or exposed to users.

> **Note:** Existing personal API keys will continue to work for local evaluation, but we recommend switching to the feature flags secure API key for local evaluation moving forward. We will be deprecating personal API keys for local evaluation in the future.

#### How to obtain a feature flags secure API key

1.  Go to the [Feature Flags tab of your project settings](https://us.posthog.com/settings/environment-feature-flags)

2.  The key should be displayed in the "Feature Flags Secure API Key" section.

3.  Copy the key and use it to initialize the PostHog client.

## Step 2: Initialize PostHog with your feature flags secure API key

When you initialize PostHog with your feature flags secure API key, PostHog will use the key to automatically fetch feature flag definitions. These definitions are then used to evaluate feature flags locally.

By default, PostHog fetches these definitions every 30 seconds (or 5 minutes in the Go SDK). However, you can change this frequency by specifying a different value in the polling interval argument.

> **Note:** For billing purposes, we count the request to fetch the feature flag definitions as being equivalent to `10 flags` requests.
>
> This is because one of these requests can compute feature flags for hundreds or thousands of users. It ensures local evaluation is priced fairly while remaining the most cost-effective option (by far!).

PostHog AI

### Node.js

```javascript
const client = new PostHog(
    '<ph_project_token>',
    {
        host: 'https://us.i.posthog.com',
        personalApiKey: 'your feature flags secure API key from step 1',
        featureFlagsPollingInterval: 30000 // Optional. Measured in milliseconds. Defaults to 30000 (30 seconds)
    }
)
```

### Ruby

```ruby
posthog = PostHog::Client.new({
  api_key: "<ph_project_token>",
  host: "https://us.i.posthog.com",
  personal_api_key: 'your feature flags secure API key from step 1',
  feature_flags_polling_interval: 30 # Optional. Measured in seconds. Defaults to 30.
})
```

### Go

```go
package main
import (
    "os"
    "time"
    "github.com/posthog/posthog-go"
)
func main() {
    client, _ := posthog.NewWithConfig(
        os.Getenv("POSTHOG_API_KEY"),
        posthog.Config{
            Endpoint:       "https://us.i.posthog.com",
            PersonalApiKey: "your feature flags secure API key", // Optional, but much more performant. If this token is not supplied, then fetching feature flag values will be slower.
            DefaultFeatureFlagsPollingInterval: time.Minute * 5 // time.Duration // Optional. Defaults to 5 minutes.
            // NextFeatureFlagsPollingTick: func() time.Duration {} // Optional. Use this to sync polling intervals between instances. For an example see: https://github.com/PostHog/posthog-go/pull/36#issuecomment-1991734125
        },
    )
    defer client.Close()
    // run commands
}
```

### PHP

```php
PostHog::init("<ph_project_token>",
  ['host' => 'https://us.i.posthog.com'],
  null, // or custom http client
 'your feature flags secure API key from step 1'
);
// NOTE: PHP currently doesn't support a poller, so you'll need to reload flags as and when needed, or re-initialize the posthog client
```

### Python

```python
from posthog import Posthog
posthog = Posthog('<ph_project_token>',
    host='https://us.i.posthog.com',
    poll_interval=30, # Optional. Measured in seconds. Defaults to 30.
    personal_api_key='your feature flags secure API key from step 1'
)
```

### C#

```csharp
// Note: We don't recommend passing these in directly.
// Instead, rely on the config system and set the personal
// api key in a secrets manager.
var client = new PostHogClient(
    new PostHogOptions {
        ProjectApiKey = "<ph_project_token>",
        PersonalApiKey = "your feature flags secure API key from step 1"
    });
```

### Java

```java
import com.posthog.server.PostHog;
import com.posthog.server.PostHogConfig;
import com.posthog.server.PostHogInterface;
PostHogConfig config = PostHogConfig.builder("<ph_project_token>")
    .host("https://us.i.posthog.com")
    .personalApiKey("your feature flags secure API key from step 1")
    .pollIntervalSeconds(30)  // Optional. Measured in seconds. Defaults to 30.
    .build();
PostHogInterface posthog = PostHog.with(config);
```

### Rust

```rust
use posthog_rs::ClientOptionsBuilder;
let options = ClientOptionsBuilder::default()
    .api_key("<ph_project_token>")
    .personal_api_key("your feature flags secure API key from step 1")
    .enable_local_evaluation(true)
    .poll_interval_seconds(30) // Optional. Measured in seconds. Defaults to 30.
    .build()
    .unwrap();
let client = posthog_rs::client(options).await;
```

## Step 3: Evaluate your feature flag

To evaluate the feature flag, call any of the flag related methods, like `getFeatureFlag` or `getAllFlags`, as you normally would. The only difference is that you must provide any `person properties`, `groups` or `group properties` used to evaluate the [release conditions](/docs/feature-flags/creating-feature-flags.md#release-conditions) of the flag.

Then, by default, PostHog attempts to evaluate the flag locally using definitions it loads on initialization and at the `poll interval`. If this fails, PostHog then makes a server request to fetch the flag value.

You can disable this behavior by setting `onlyEvaluateLocally` to `true`. In this case, PostHog will **only** attempt to evaluate the flag locally, and return `undefined` / `None` / `nil` if it was unable to.

PostHog AI

### Node.js

```javascript
await client.getFeatureFlag(
    'flag-key',
    'distinct_id_of_the_user',
    {
        // include any person properties, groups, or group properties required to evaluate the flag
        personProperties: {
            'property_name': 'value'
        },
        groups: {
            "your_group_type": "your_group_id",
            "another_group_type": "another_group_id",
        },
        groupProperties: {
            'your_group_type': {
                'group_property_name': 'value'
            },
            'another_group_type': {
                'group_property_name': 'another value'
            }
        },
        onlyEvaluateLocally: false, // Optional. Defaults to false. Set to true if you don't want PostHog to make a server request if it can't evaluate locally
    }
)
```

### Ruby

```ruby
posthog.get_feature_flag(
    'flag-key',
    'distinct_id_of_the_user',
    # Include any person properties, groups, or group properties required to evaluate the flag
    person_properties: {
        'property_name': 'value'
    },
    groups: {
        'your_group_type': 'your_group_id',
        'another_group_type': 'another_group_id',
    },
    group_properties: {
        'your_group_type': {
            'group_property_name': 'value'
        }
        'another_group_type': {
            'group_property_name': 'another value'
        }
    },
    only_evaluate_locally: False # Optional. Defaults to False. Set to True if you don't want PostHog to make a server request if it can't evaluate locally
)
```

### Go

```go
enabledVariant, err := client.GetFeatureFlag(
    FeatureFlagPayload{
        Key:        "flag-key",
        DistinctId: "distinct_id_of_the_user",
        // Include any person properties, groups, or group properties required to evaluate the flag
        Groups: posthog.NewGroups().
            Set("your_group_type", "your_group_id").
            Set("another_group_type", "another_group_id"),
        PersonProperties: posthog.NewProperties().
            Set("property_name", "value"),
        GroupProperties: map[string]map[string]interface{}{
            "your_group_type": {
                "group_property_name": "value",
            },
            "another_group_type": {
                "group_property_name": "another value",
            },
        },
        OnlyEvaluateLocally: false, // Optional. Defaults to false. Set to true if you don't want PostHog to make a server request if it can't evaluate locally
    },
)
```

### Python

```python
posthog.get_feature_flag(
    'flag-key',
    'distinct_id_of_the_user',
    # Include any person properties, groups, or group properties required to evaluate the flag
    person_properties={'property_name': 'value'},
    groups={
        'your_group_type': 'your_group_id',
        'another_group_type': 'another_group_id'
    },
    group_properties={
        'your_group_type': {'group_property_name': 'value'},
        'another_group_type': {'group_property_name': 'another value'}
    },
    only_evaluate_locally=False # Optional. Defaults to False. Set to True if you don't want PostHog to make a server request if it can't evaluate locally
)
```

### PHP

```php
PostHog::getFeatureFlag(
    'flag-key',
    'distinct_id_of_the_user',
    // Include any person properties, groups, or group properties required to evaluate the flag
    [
        'your_group_type' => 'your_group_id',
        'another_group_type' => 'another_group_id'
    ], // groups
    ['property_name' => 'value'], // person properties
    [
        'your_group_type' => ['group_property_name' => 'value'],
        'another_group_type' => ['group_property_name' => 'another value']
    ], // group properties
    false, // only_evaluate_locally, Optional. Defaults to false. Set to true if you don't want PostHog to make a server request if it can't evaluate locally
    true // sendFeatureFlagEvents
);
```

### C#

```csharp
await posthog.GetFeatureFlagAsync(
    "flag-key",
    "distinct_id_of_the_user",
    options: new FeatureFlagOptions
    {
        PersonProperties = new()
        {
            ["property_name"] = "value"
        },
        Groups = new()
        {
            new Group("your_group_type", "your_group_id")
            {
                ["group_property_name"] = "value"
            },
            new Group("another_group_type", "another_group_id")
            {
                ["group_property_name"] = "another value"
            }
        }
    }
);
```

### Java

```java
posthog.getFeatureFlag(
    "distinct_id_of_the_user",
    "flag-key",
    PostHogFeatureFlagOptions
        .builder()
        .personProperty("property_name", "value")
        .group("your_group_type", "your_group_id")
        .group("another_group_type", "another_group_id")
        .groupProperty("your_group_type", "group_property_name", "value")
        .groupProperty("another_group_type", "group_property_name", "another value")
        .build());
```

### Rust

```rust
use std::collections::HashMap;
use serde_json::json;
// Include any person properties, groups, or group properties required to evaluate the flag
let mut groups = HashMap::new();
groups.insert("your_group_type".to_string(), "your_group_id".to_string());
groups.insert("another_group_type".to_string(), "another_group_id".to_string());
let mut person_props = HashMap::new();
person_props.insert("property_name".to_string(), json!("value"));
let mut group_props = HashMap::new();
let mut your_group_props = HashMap::new();
your_group_props.insert("group_property_name".to_string(), json!("value"));
group_props.insert("your_group_type".to_string(), your_group_props);
let mut another_group_props = HashMap::new();
another_group_props.insert("group_property_name".to_string(), json!("another value"));
group_props.insert("another_group_type".to_string(), another_group_props);
let flag = client.get_feature_flag(
    "flag-key".to_string(),
    "distinct_id_of_the_user".to_string(),
    Some(groups),
    Some(person_props),
    Some(group_props),
).await.unwrap();
```

## Reloading flags

As mentioned in [step 2](#step-2-initialize-posthog-with-your-feature-flags-secure-api-key), PostHog periodically fetches feature flag definitions. However, you can also force a reload by calling `reloadFeatureFlags()`:

PostHog AI

### Node.js

```javascript
await client.reloadFeatureFlags()
```

### Ruby

```ruby
posthog.reload_feature_flags()
```

### Go

```go
client.ReloadFeatureFlags()
```

### Python

```python
posthog.load_feature_flags()
```

### PHP

```php
PostHog::loadFlags()
```

### Java

```java
posthog.reloadFeatureFlags()
```

### Rust

```rust
// The Rust SDK automatically reloads flags in the background
// at the interval specified by poll_interval_seconds (default: 30).
// Manual reload is not currently supported.
```

## Restriction on local evaluation

### General restrictions

Local evaluation is not possible for flags that:

1.  Have experience continuity enabled, which is set when you check ['persist flag across authentication steps'](/docs/feature-flags/creating-feature-flags.md#persisting-feature-flags-across-authentication-steps) on your feature flag.
2.  Are linked to an [early access feature](/docs/feature-flags/early-access-feature-management.md)
3.  Depend on [static cohorts](/docs/data/cohorts.md#static-cohorts)
4.  Use the `is_not_set` property operator, since local evaluation can only check properties you provide — it can't determine whether a property is absent on a person.

### Dynamic cohort restrictions

> **Note:** This restriction **does not apply** to our [Go](/docs/libraries/go.md) SDK, [Rust](/docs/libraries/rust.md) SDK, v2.6.0 and above of our [Node](/docs/libraries/node.md) SDK, and to v2.4.0 and above of our [Python](/docs/libraries/python.md) SDK.

To enable local evaluation of feature flags that depend on [dynamic cohorts](/docs/data/cohorts.md#dynamic-cohorts), we translate the cohort definition into person properties.

However, there are a few constraints, and cohorts cannot be evaluated locally if:

1.  There is a variant override on the condition with the cohort.
2.  They have non-person properties.
3.  There's more than one cohort in the feature flag definition.
4.  The cohort in the feature flag is in the same group as another condition.
5.  The cohort has nested AND-OR filters. Only simple cohorts that have a top level OR group, and inner level ANDs will be evaluated locally.

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better