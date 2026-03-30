# Source: https://posthog.com/docs/feature-flags/remote-config.md

# Remote config - Docs

Boolean and multivariate flags are helpful for dynamic values that differ from user to user, but sometimes you need a simple way to pass configuration related to your application without having to make code changes or redeploy your app.

Remote config flags enable you to configure a simple flag that always returns the same payload wherever it is called. Remote config flags can also be stored as encrypted values and decrypted on the server side when requested. Encryption/decryption is handled automatically.

There are 3 steps to start using remote config flags:

## Step 1: Find your feature flags secure API key

The feature flags secure API key is a secret project specific token listed in the [Feature Flags tab of your project settings](https://us.posthog.com/settings/environment-feature-flags) in the "Feature Flags Secure API Key" section. It provides the SDKs with access to the feature flag definitions for your project so they can evaluate flags locally.

This key needs to be kept secret, and should not be used in the frontend or exposed to users.

> **Note:** Existing personal API keys will continue to work for local evaluation, but we recommend switching to the feature flags secure API key for local evaluation moving forward. We will be deprecating personal API keys for local evaluation in the future.

#### How to obtain a feature flags secure API key

1.  Go to the [Feature Flags tab of your project settings](https://us.posthog.com/settings/environment-feature-flags)

2.  The key should be displayed in the "Feature Flags Secure API Key" section.

3.  Copy the key and use it to initialize the PostHog client.

## Step 2: Initialize PostHog with your feature flags secure API key in options

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

> **Note:** By default, initializing PostHog with your feature flags secure API key enables local evaluation, but this can be disabled in `posthog-node` by setting `enableLocalEvaluation: false` in your config.

## Step 3: Use remote config flags

PostHog AI

### Node.js

```javascript
const config = posthog.getRemoteConfigPayload('landing-page-config')
// config is a JsonType
```

### Python

```python
config = posthog.get_remote_config_payload('landing-page-config')
# config is a JSON encoded string. It will need to be parsed as a JSON object.
```

### Go

```go
config, err := posthog.GetRemoteConfigPayload("landing-page-config")
// config is a JSON encoded string. It will need to be parsed as a JSON object.
```

### Ruby

```ruby
config = posthog.get_remote_config_payload('landing-page-config')
# config is a JSON encoded string. It will need to be parsed as a JSON object.
```

### C#

```csharp
var config = await posthog.GetRemoteConfigPayloadAsync("landing-page-config");
// config is a JsonDocument
```

You can think of remote config flags as multivariate flags with a single variant which is served for all flag requests. By default, enabled remote config flags roll out to 100% of all users.

> **Note**: Remote config flags are meant to always serve payloads and be called with the flag payload function in each SDK. If `getFeatureFlag` is called instead, the SDK simply returns `true`

## Related

-   [Feature flags vs configuration: Which should you choose?](/product-engineers/feature-flags-vs-configuration.md)

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better