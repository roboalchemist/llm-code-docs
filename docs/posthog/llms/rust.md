# Source: https://posthog.com/docs/product-analytics/installation/rust.md

# Source: https://posthog.com/docs/feature-flags/installation/rust.md

# Source: https://posthog.com/docs/experiments/installation/rust.md

# Source: https://posthog.com/docs/libraries/rust.md

# Rust - Docs

## Installation

Install the `posthog-rs` crate by adding it to your `Cargo.toml`.

Cargo.toml

PostHog AI

```toml
[dependencies]
posthog-rs = "0.3.5"
```

Next, set up the client with your PostHog project key.

Rust

PostHog AI

```rust
let client = posthog_rs::client(env!("<ph_project_token>"));
```

### Blocking client

Our Rust SDK supports both blocking and async clients. The async client is the default and is recommended for most use cases.

If you need to use a synchronous client instead – like we do in our [CLI](https://github.com/PostHog/posthog/tree/master/cli) –, you can opt into it by disabling the asynchronous feature on your `Cargo.toml` file.

toml

PostHog AI

```toml
[dependencies]
posthog-rs = { version = "0.3.5", default-features = false }
```

In blocking mode, calls to `capture` and related methods will block until the PostHog event capture API returns – generally this is on the order of tens of milliseconds, but you may want to `thread::spawn` a background thread when you send an event.

## Identifying users

> **Identifying users is required.** Backend events need a `distinct_id` that matches the ID your frontend uses when calling `posthog.identify()`. Without this, backend events are orphaned — they can't be linked to frontend event captures, [session replays](/docs/session-replay.md), [LLM traces](/docs/ai-engineering.md), or [error tracking](/docs/error-tracking.md).
>
> See our guide on [identifying users](/docs/getting-started/identify-users.md) for how to set this up.

## Capturing events

You can send custom events using `capture`:

Rust

PostHog AI

```rust
let mut event = Event::new("user_signed_up", "distinct_id_of_the_user");
client.capture(event).unwrap();
```

> **Tip:** We recommend using a `[object] [verb]` format for your event names, where `[object]` is the entity that the behavior relates to, and `[verb]` is the behavior itself. For example, `project created`, `user signed up`, or `invite sent`.

### Setting event properties

Optionally, you can include additional information with the event by including a [properties](/docs/data/events.md#event-properties) object:

Rust

PostHog AI

```rust
let mut event = Event::new("user_signed_up", "distinct_id_of_the_user");
event.insert_prop("login_type", "email").unwrap();
event.insert_prop("is_free_trial", true).unwrap();
client.capture(event).unwrap();
```

### Batching events

To capture multiple events at once, use `batch()`:

Rust

PostHog AI

```rust
let event1 = posthog_rs::Event::new("event 1", "distinct_id_of_user_A");
let event2 = posthog_rs::Event::new("event 2", "distinct_id_of_user_B");
client.capture_batch(vec![event1, event2]).unwrap();
```

## Feature flags

PostHog's [feature flags](/docs/feature-flags.md) enable you to safely deploy and roll back new features as well as target specific users and groups with them.

### Boolean feature flags

Rust

PostHog AI

```rust
let is_enabled = client.is_feature_enabled(
    "flag-key".to_string(),
    "distinct_id_of_your_user".to_string(),
    None, None, None
).await.unwrap();
if is_enabled {
    // Do something differently for this user
}
```

### Multivariate feature flags

Rust

PostHog AI

```rust
use posthog_rs::FlagValue;
match client.get_feature_flag(
    "flag-key".to_string(),
    "distinct_id_of_your_user".to_string(),
    None, None, None
).await.unwrap() {
    Some(FlagValue::String(variant)) => {
        if variant == "variant-key" {
            // Do something for this variant
        }
    }
    Some(FlagValue::Boolean(enabled)) => {
        // Handle boolean flag
    }
    None => {
        // Flag not found or disabled
    }
}
```

### Fetching all flags

Rust

PostHog AI

```rust
let (flags, payloads) = client.get_feature_flags(
    "distinct_id_of_your_user".to_string(),
    None, None, None
).await.unwrap();
for (key, value) in flags {
    println!("Flag {}: {:?}", key, value);
}
```

### Feature flag payloads

Rust

PostHog AI

```rust
let payload = client.get_feature_flag_payload(
    "flag-key".to_string(),
    "distinct_id_of_your_user".to_string()
).await.unwrap();
if let Some(data) = payload {
    println!("Payload: {}", data);
}
```

### With person properties

Rust

PostHog AI

```rust
use std::collections::HashMap;
use serde_json::json;
let mut person_props = HashMap::new();
person_props.insert("plan".to_string(), json!("enterprise"));
person_props.insert("country".to_string(), json!("US"));
let flag = client.get_feature_flag(
    "premium-feature".to_string(),
    "distinct_id_of_your_user".to_string(),
    None,
    Some(person_props),
    None
).await.unwrap();
```

### With groups

For B2B applications with group-based flags:

Rust

PostHog AI

```rust
use std::collections::HashMap;
use serde_json::json;
let mut groups = HashMap::new();
groups.insert("company".to_string(), "company-123".to_string());
let mut group_props = HashMap::new();
let mut company_props = HashMap::new();
company_props.insert("size".to_string(), json!(500));
group_props.insert("company".to_string(), company_props);
let flag = client.get_feature_flag(
    "b2b-feature".to_string(),
    "distinct_id_of_your_user".to_string(),
    Some(groups),
    None,
    Some(group_props)
).await.unwrap();
```

## Local evaluation

For improved performance, you can evaluate feature flags locally by enabling local evaluation. This caches flag definitions and evaluates them without making API requests for each flag check.

To enable local evaluation, you need a [personal API key](/docs/api.md#how-to-obtain-a-personal-api-key) and to configure the client:

Rust

PostHog AI

```rust
use posthog_rs::ClientOptionsBuilder;
let options = ClientOptionsBuilder::default()
    .api_key("your-project-api-key")
    .personal_api_key("your-personal-api-key")
    .enable_local_evaluation(true)
    .poll_interval_seconds(30) // Optional, defaults to 30
    .build()
    .unwrap();
let client = posthog_rs::client(options).await;
```

When local evaluation is enabled, flag definitions are fetched on initialization and periodically refreshed in the background. Flag evaluation then happens locally without network requests, providing 100-1000x faster performance.

> **Note:** Local evaluation requires providing any person properties, groups, or group properties needed to evaluate the flag's release conditions, since PostHog can't fetch these automatically without a server request.

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better