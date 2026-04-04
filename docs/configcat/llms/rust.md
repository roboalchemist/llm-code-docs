# Source: https://configcat.com/docs/sdk-reference/rust.md

# Source: https://configcat.com/docs/sdk-reference/openfeature/rust.md

# OpenFeature Provider for Rust

Copy page

[![Build Status](https://github.com/configcat/openfeature-rust/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/configcat/openfeature-rust/actions/workflows/ci.yml) [![crates.io](https://img.shields.io/crates/v/configcat-openfeature-provider.svg?logo=rust)](https://crates.io/crates/configcat-openfeature-provider) [![docs.rs](https://img.shields.io/badge/docs.rs-configcat_openfeature_provider-66c2a5?logo=docs.rs)](https://docs.rs/configcat-openfeature-provider)

[ConfigCat OpenFeature Provider for Rust on GitHub](https://github.com/configcat/openfeature-rust)

## Getting started[​](#getting-started "Direct link to Getting started")

### 1. Install the provider[​](#1-install-the-provider "Direct link to 1. Install the provider")

Run the following Cargo command in your project directory:

```shell
cargo add configcat-openfeature-provider

```

Or add the following to your `Cargo.toml`:

```toml
[dependencies]
configcat-openfeature-provider = "0.1"

```

### 2. Initialize the provider[​](#2-initialize-the-provider "Direct link to 2. Initialize the provider")

The `ConfigCatProvider` needs a pre-configured [ConfigCat Rust SDK](https://configcat.com/docs/sdk-reference/rust.md#creating-the-configcat-client) client:

```rust
use std::time::Duration;
use configcat::{Client, PollingMode};
use open_feature::OpenFeature;
use configcat_openfeature_provider::ConfigCatProvider;

#[tokio::main]
async fn main() {
    // Acquire an OpenFeature API instance.
    let mut api = OpenFeature::singleton_mut().await;

    // Configure the ConfigCat SDK.
    let configcat_client = Client::builder("<YOUR-CONFIGCAT-SDK-KEY>")
        .polling_mode(PollingMode::AutoPoll(Duration::from_secs(60)))
        .build()
        .unwrap();

    // Configure the provider.
    api.set_provider(ConfigCatProvider::new(configcat_client)).await;

    // Create a client.
    let client = api.create_client();
}

```

For more information about all the configuration options, see the [Rust SDK documentation](https://configcat.com/docs/sdk-reference/rust.md#creating-the-configcat-client).

### 3. Evaluate your feature flag[​](#3-evaluate-your-feature-flag "Direct link to 3. Evaluate your feature flag")

```rust
let is_awesome_feature_enabled = client
    .get_bool_value("isAwesomeFeatureEnabled", None, None)
    .await
    .unwrap_or(false);

if is_awesome_feature_enabled {
    do_the_new_thing();
} else {
    do_the_old_thing();
}

```

## Evaluation Context[​](#evaluation-context "Direct link to Evaluation Context")

An [evaluation context](https://openfeature.dev/docs/reference/concepts/evaluation-context) in the OpenFeature specification is a container for arbitrary contextual data that can be used as a basis for feature flag evaluation. The ConfigCat provider translates these evaluation contexts to ConfigCat [User Objects](https://configcat.com/docs/sdk-reference/rust.md#user-object).

The following table shows how the different context attributes are mapped to User Object attributes.

| Evaluation context | User Object  | Required |
| ------------------ | ------------ | -------- |
| `targeting_key`    | `identifier` | ☑        |
| `Email`            | `email`      |          |
| `Country`          | `country`    |          |
| Any other          | `custom`     |          |

To evaluate feature flags for a context, use the [OpenFeature Evaluation API](https://openfeature.dev/docs/reference/concepts/evaluation-api/):

```rust
let context = EvaluationContext::default()
    .with_targeting_key("#SOME-USER-ID#")
    .with_custom_field("Email", "configcat@example.com")
    .with_custom_field("Country", "CountryID")
    .with_custom_field("Rating", 4.5)
    .with_custom_field("Roles", ["Role1", "Role2"]);

let is_awesome_feature_enabled = client
    .get_bool_value("isAwesomeFeatureEnabled", Some(&context), None)
    .await
    .unwrap_or(false);

```

## Look under the hood[​](#look-under-the-hood "Direct link to Look under the hood")

* [Sample Rust App](https://github.com/configcat/openfeature-rust/tree/main/examples)
* [ConfigCat OpenFeature Provider's repository on GitHub](https://github.com/configcat/openfeature-rust)
* [ConfigCat OpenFeature Provider on crates.io](https://crates.io/crates/configcat-openfeature-provider)
* [ConfigCat OpenFeature Provider on docs.rs](https://docs.rs/configcat-openfeature-provider/latest/configcat_openfeature_provider)
