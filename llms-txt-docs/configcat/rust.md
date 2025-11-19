# Source: https://configcat.com/docs/sdk-reference/rust.md

# Source: https://configcat.com/docs/sdk-reference/openfeature/rust.md

# Source: https://configcat.com/docs/sdk-reference/rust.md

# Rust SDK Reference

[![Star on GitHub](https://img.shields.io/github/stars/configcat/rust-sdk.svg?style=social)](https://github.com/configcat/rust-sdk/stargazers) [![Build Status](https://github.com/configcat/rust-sdk/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/configcat/rust-sdk/actions/workflows/ci.yml) [![crates.io](https://img.shields.io/crates/v/configcat.svg?logo=rust)](https://crates.io/crates/configcat) [![docs.rs](https://img.shields.io/badge/docs.rs-configcat-66c2a5?logo=docs.rs)](https://docs.rs/configcat)

[ConfigCat Rust SDK on GitHub](https://github.com/configcat/rust-sdk)

## Getting started[​](#getting-started "Direct link to Getting started")

### 1. Install the package[​](#1-install-the-package "Direct link to 1. Install the package")

Run the following Cargo command in your project directory:

```
cargo add configcat
```

Or add the following to your `Cargo.toml`:

```
[dependencies]
configcat = "0.1"
```

### 2. Import the `configcat` module to your application[​](#2-import-the-configcat-module-to-your-application "Direct link to 2-import-the-configcat-module-to-your-application")

```
use configcat::*;
```

### 3. Create the *ConfigCat* client with your *SDK Key*[​](#3-create-the-configcat-client-with-your-sdk-key "Direct link to 3-create-the-configcat-client-with-your-sdk-key")

```
use configcat::*;

#[tokio::main]
async fn main() {
    let client = Client::new("#YOUR-SDK-KEY#").unwrap();
}
```

### 4. Get your setting value[​](#4-get-your-setting-value "Direct link to 4. Get your setting value")

```
use configcat::*;

#[tokio::main]
async fn main() {
    let client = Client::new("#YOUR-SDK-KEY#").unwrap();

    let is_awesome_feature_enabled = client.get_value("isAwesomeFeatureEnabled", false, None).await;
    
    if is_awesome_feature_enabled {
        do_the_new_thing();
    } else {
        do_the_old_thing();
    }
}
```

## Creating the *ConfigCat Client*[​](#creating-the-configcat-client "Direct link to creating-the-configcat-client")

*ConfigCat Client* is responsible for:

* managing the communication between your application and ConfigCat servers.
* caching your setting values and feature flags.
* serving values quickly in a failsafe way.

`Client::new(<sdk_key>)` returns a client with default options.

| Arguments | Description                                                                               |
| --------- | ----------------------------------------------------------------------------------------- |
| `sdk_key` | SDK Key to access your feature flags and settings. Get it from the *ConfigCat Dashboard*. |

### Custom client options[​](#custom-client-options "Direct link to Custom client options")

`Client::builder(<sdk_key>)` returns a builder used to construct a customized client.

```
use std::time::Duration;
use configcat::{Client, PollingMode, DataGovernance};

let builder = Client::builder("#YOUR-SDK-KEY#")
    .polling_mode(PollingMode::AutoPoll(Duration::from_secs(60)))
    .data_governance(DataGovernance::EU);

let client = builder.build().unwrap();
```

Available options:

| Option                                                     | Description                                                                                                                                                                                                                                                                                                               |
| ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `data_governance(DataGovernance)`                          | Defaults to `Global`. Describes the location of your feature flag and setting data within the ConfigCat CDN. This parameter needs to be in sync with your Data Governance preferences. [More about Data Governance](https://configcat.com/docs/docs/advanced/data-governance/.md). Available options: `Global`, `EuOnly`. |
| `base_url(&str)`                                           | Sets the CDN base url (forward proxy, dedicated subscription) from where the sdk will download the configurations.                                                                                                                                                                                                        |
| `cache(Box<dyn ConfigCache>)`                              | Sets a custom cache implementation for the client. [See below](#cache).                                                                                                                                                                                                                                                   |
| `http_timeout(Duration)`                                   | Sets the maximum wait time for a HTTP response. [More about the HTTP timeout](#http-timeout)                                                                                                                                                                                                                              |
| `polling_mode(PollingMode)`                                | Defaults to `AutoPoll`. Sets the polling mode for the client. [More about polling modes](#polling-modes).                                                                                                                                                                                                                 |
| `overrides(Box<dyn OverrideDataSource>, OverrideBehavior)` | Sets the local feature flag & setting overrides. [More about feature flag overrides](#flag-overrides).                                                                                                                                                                                                                    |
| `default_user(User)`                                       | Sets the default user. [More about default user](#default-user).                                                                                                                                                                                                                                                          |
| `offline(bool)`                                            | Defaults to `false`. Indicates whether the SDK should be initialized in offline mode. [More about offline mode](#online--offline-mode).                                                                                                                                                                                   |

caution

We strongly recommend you to use the *ConfigCat Client* as a Singleton object in your application. If you want to use multiple SDK Keys in the same application, create only one *ConfigCat Client* per SDK Key.

## Anatomy of `get_value()`[​](#anatomy-of-get_value "Direct link to anatomy-of-get_value")

| Parameters | Description                                                                                                                                             |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `key`      | **REQUIRED.** Setting-specific key. Set on *ConfigCat Dashboard* for each setting.                                                                      |
| `default`  | **REQUIRED.** This value will be returned in case of an error.                                                                                          |
| `user`     | Optional, *User Object*. Essential when using Targeting. [Read more about Targeting.](https://configcat.com/docs/docs/targeting/targeting-overview/.md) |

```
let is_awesome_feature_enabled = client.get_value(
    "isAwesomeFeatureEnabled", // Setting Key
    false, // Default value
    Some(User::new("#UNIQUE-USER-IDENTIFIER#")) // Optional User Object
).await;
```

caution

It is important to provide an argument for the `default` parameter, specifically for the `T` generic type parameter, that matches the type of the feature flag or setting you are evaluating. Please refer to the following table for the corresponding types.

### Setting type mapping[​](#setting-type-mapping "Direct link to Setting type mapping")

| Setting Kind   | Type parameter `T` |
| -------------- | ------------------ |
| On/Off Toggle  | `bool`             |
| Text           | `String`           |
| Whole Number   | `i64`              |
| Decimal Number | `f64`              |

If you specify an allowed type but it mismatches the setting kind, an error message will be logged and `default` will be returned.

When relying on type inference and not explicitly specifying the type parameter, be mindful of potential type mismatch issues, especially with number types. For example, `client.get_value("keyOfMyDecimalSetting", 0, None).await` will return `default` (`0`) instead of the actual value of the decimal setting because the compiler infers the type as `i64` instead of `f64`, that is, the call is equivalent to `client.get_value::<i64>("keyOfMyDecimalSetting", 0, None).await`, which is a type mismatch.

To correctly evaluate a decimal setting, you should use:

```
let value = client.get_value("keyOfMyDecimalSetting", 0.0, None).await;
// -or-
let value = client.get_value("keyOfMyDecimalSetting", 0_f64, None).await;
```

## Anatomy of `get_value_details()`[​](#anatomy-of-get_value_details "Direct link to anatomy-of-get_value_details")

`get_value_details()` is similar to `get_value()` but instead of returning the evaluated value only, it provides more detailed information about the evaluation result.

| Parameters | Description                                                                                                                                             |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `key`      | **REQUIRED.** Setting-specific key. Set on *ConfigCat Dashboard* for each setting.                                                                      |
| `default`  | **REQUIRED.** This value will be returned in case of an error.                                                                                          |
| `user`     | Optional, *User Object*. Essential when using Targeting. [Read more about Targeting.](https://configcat.com/docs/docs/targeting/targeting-overview/.md) |

```
let user = User::new("#UNIQUE-USER-IDENTIFIER#"); // Optional User Object
let details = client.get_value_details("keyOfMyFeatureFlag", false, Some(user)).await;
```

caution

It is important to provide an argument for the `default` parameter, specifically for the `T` generic type parameter, that matches the type of the feature flag or setting you are evaluating. Please refer to [this table](#setting-type-mapping) for the corresponding types.

The `details` result contains the following information:

| Field                       | Type                              | Description                                                                                                |
| --------------------------- | --------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `key`                       | `String`                          | The key of the evaluated feature flag or setting.                                                          |
| `value`                     | `bool` / `String` / `i64` / `f64` | The evaluated value of the feature flag or setting.                                                        |
| `user`                      | `Option<User>`                    | The User Object used for the evaluation.                                                                   |
| `is_default_value`          | `bool`                            | True when the default value passed to `GetValueDetailsAsync()` is returned due to an error.                |
| `error`                     | `Option<ClientError>`             | In case of an error, this field contains the related error structure.                                      |
| `matched_targeting_rule`    | `Option<Arc<TargetingRule>>`      | The Targeting Rule (if any) that matched during the evaluation and was used to return the evaluated value. |
| `matched_percentage_option` | `Option<Arc<PercentageOption>>`   | The Percentage Option (if any) that was used to select the evaluated value.                                |
| `fetch_time`                | `Option<DateTime<Utc>>`           | The last download time (UTC) of the current config.                                                        |

## User Object[​](#user-object "Direct link to User Object")

The [User Object](https://configcat.com/docs/docs/targeting/user-object/.md) is essential if you'd like to use ConfigCat's [Targeting](https://configcat.com/docs/docs/targeting/targeting-overview/.md) feature.

```
let user = User::new("#UNIQUE-USER-IDENTIFIER#");
```

```
let user = User::new("john@example.com");
```

| Option                          | Description                                                                                                      |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `new(<identifier>)`             | **REQUIRED.** Unique identifier of a user in your application. Can be any `string` value, even an email address. |
| `email(&str)`                   | Optional email address for easier Targeting Rule definitions.                                                    |
| `country(&str)`                 | Optional country for easier Targeting Rule definitions.                                                          |
| `custom(&str, Into<UserValue>)` | Optional custom attribute of a user for advanced Targeting Rule definitions. E.g. User role, Subscription type.  |

```
let user = new User("#UNIQUE-USER-IDENTIFIER#")
    .email("john@example.com")
    .country("United Kingdom")
    .custom("SubscriptionType", "Pro")
    .custom("UserRole", "Admin");
```

The `custom()` method allows attribute values other than `String`:

```
let user = new User("#UNIQUE-USER-IDENTIFIER#")
    .custom("Rating", 4.5)
    .custom("RegisteredAt", DateTime::from_str("2023-06-14T15:27:15.8440000Z").unwrap())
    .custom("Roles", ["Role1", "Role2"]);
```

### User Object Attribute Types[​](#user-object-attribute-types "Direct link to User Object Attribute Types")

All comparators support `String` values as User Object attribute (in some cases they need to be provided in a specific format though, see below), but some of them also support other types of values. It depends on the comparator how the values will be handled. The following rules apply:

**Text-based comparators** (`EQUALS`, `IS ONE OF`, etc.)

* accept `String` values,
* all other values are automatically converted to `String` (a warning will be logged but evaluation will continue as normal).

**SemVer-based comparators** (`IS ONE OF`, `<`, `>=`, etc.)

* accept `String` values containing a properly formatted, valid semver value,
* all other values are considered invalid (a warning will be logged and the currently evaluated targeting rule will be skipped).

**Number-based comparators** (`=`, `<`, `>=`, etc.)

* accept `Int`, `UInt`, or `Float` values,
* accept `String` values containing a properly formatted, valid `Float` value,
* all other values are considered invalid (a warning will be logged and the currently evaluated targeting rule will be skipped).

**Date time-based comparators** (`BEFORE` / `AFTER`)

* accept `DateTime` values, which are automatically converted to a second-based Unix timestamp,
* accept `Int`, `UInt`, or `Float` values representing a second-based Unix timestamp,
* accept `String` values containing a properly formatted, valid `Float` value,
* all other values are considered invalid (a warning will be logged and the currently evaluated targeting rule will be skipped).

**String array-based comparators** (`ARRAY CONTAINS ANY OF` / `ARRAY NOT CONTAINS ANY OF`)

* accept `Vec` of `String`s,
* accept `String` values containing a valid JSON string which can be deserialized to an array of `String`,
* all other values are considered invalid (a warning will be logged and the currently evaluated targeting rule will be skipped).

### Default user[​](#default-user "Direct link to Default user")

It's possible to set a default User Object that will be used on feature flag and setting evaluation. It can be useful when your application has a single user only or rarely switches users.

You can set the default User Object either on SDK initialization:

```
let client = Client::builder("#YOUR-SDK-KEY#")
    .default_user(User::new("john@example.com"))
    .build()
    .unwrap();
```

...or using the `set_default_user()` method of the `configcat::Client`:

```
client.set_default_user(User::new("john@example.com"));
```

Whenever the evaluation methods like `get_value()`, `get_value_details()`, etc. are called without an explicit `user` parameter, the SDK will automatically use the default user as a User Object.

```
let client = Client::builder("#YOUR-SDK-KEY#")
    .default_user(User::new("john@example.com"))
    .build()
    .unwrap();

// The default user will be used in the evaluation process.
let value = client.get_value("keyOfMyFeatureFlag", false, None).await;
```

When a `user` parameter is passed to the evaluation methods, it takes precedence over the default user.

```
let client = Client::builder("#YOUR-SDK-KEY#")
    .default_user(User::new("john@example.com"))
    .build()
    .unwrap();

let other_user = User::new("brian@example.com");

// other_user will be used in the evaluation process.
let value = client.get_value("keyOfMyFeatureFlag", false, Some(other_user)).await;
```

You can also remove the default user by doing the following:

```
client.clear_default_user();
```

## Polling Modes[​](#polling-modes "Direct link to Polling Modes")

The *ConfigCat SDK* supports 3 different polling strategies to fetch feature flags and settings from the ConfigCat CDN. Once the latest data is downloaded, it is stored in the cache, then calls to `get_value()` use the cached data to evaluate feature flags and settings. With the following polling modes, you can customize the SDK to best fit to your application's lifecycle. [More about polling modes & caching](https://configcat.com/docs/docs/advanced/caching/.md).

When no polling mode is specified upon SDK initialization, `AutoPoll` will be selected with a `60s` poll interval.

### Auto polling (default)[​](#auto-polling-default "Direct link to Auto polling (default)")

The *ConfigCat SDK* downloads the latest config data from the ConfigCat CDN automatically and stores it in the cache. The `Duration` parameter specifies how frequent the config JSON downloads will happen.

```
let client = Client::builder("#YOUR-SDK-KEY#")
    .polling_mode(PollingMode::AutoPoll(Duration::from_secs(60)))
    .build()
    .unwrap();
```

### Lazy loading[​](#lazy-loading "Direct link to Lazy loading")

When calling `get_value()`, the *ConfigCat SDK* downloads the latest config data from the ConfigCat CDN only if it is not already present in the cache, or if the cache has expired. In this case `get_value()` will return the setting value after the cache is updated. The `Duration` parameter specifies after how much time the cache is considered stale.

```
let client = Client::builder("#YOUR-SDK-KEY#")
    .polling_mode(PollingMode::LazyLoad(Duration::from_secs(60)))
    .build()
    .unwrap();
```

### Manual polling[​](#manual-polling "Direct link to Manual polling")

Manual polling gives you full control over when the config data is downloaded from the ConfigCat CDN. The *ConfigCat SDK* will not download it automatically. Calling `refresh()` is your application's responsibility.

```
let client = Client::builder("#YOUR-SDK-KEY#")
    .polling_mode(PollingMode::Manual)
    .build()
    .unwrap();

_ = client.refresh().await;
```

> `get_value()` returns `default` if the cache is empty. Call `refresh()` to update the cache.

## Online / Offline mode[​](#online--offline-mode "Direct link to Online / Offline mode")

In cases where you want to prevent the SDK from making HTTP calls, you can switch it to offline mode:

```
client.offline();
```

In offline mode, the SDK won't initiate HTTP requests and will work only from its cache.

To switch the SDK back to online mode, do the following:

```
client.online();
```

Using the `client.is_offline()` method, you can check whether the SDK is in offline mode.

## Flag Overrides[​](#flag-overrides "Direct link to Flag Overrides")

With flag overrides you can overwrite the feature flags & settings downloaded from the ConfigCat CDN with local values. Moreover, you can specify how the overrides should apply over the downloaded values. The following 3 behaviours are supported:

* **Local only** (`OverrideBehavior::LocalOnly`): When evaluating values, the SDK will not use feature flags & settings from the ConfigCat CDN, but it will use all feature flags & settings that are loaded from local-override sources.

* **Local over remote** (`OverrideBehavior::LocalOverRemote`): When evaluating values, the SDK will use all feature flags & settings that are downloaded from the ConfigCat CDN, plus all feature flags & settings that are loaded from local-override sources. If a feature flag or a setting is defined both in the downloaded and the local-override source then the local-override version will take precedence.

* **Remote over local** (`OverrideBehavior::RemoteOverLocal`): When evaluating values, the SDK will use all feature flags & settings that are downloaded from the ConfigCat CDN, plus all feature flags & settings that are loaded from local-override sources. If a feature flag or a setting is defined both in the downloaded and the local-override source then the downloaded version will take precedence.

You can load your feature flag & setting overrides from a file or from a simple `HashMap<String, configcat::Value>`.

### JSON File[​](#json-file "Direct link to JSON File")

The SDK can load your feature flag & setting overrides from a file.

#### File[​](#file "Direct link to File")

```
use configcat::{Client, FileDataSource, OverrideBehavior};

let file_ds = FileDataSource::new("path/to/local_flags.json").unwrap();

let client = Client::builder("localhost")
    .overrides(Box::new(file_ds), OverrideBehavior::LocalOnly)
    .build()
    .unwrap();
```

#### JSON File Structure[​](#json-file-structure "Direct link to JSON File Structure")

The SDK supports 2 types of JSON structures to describe feature flags & settings.

##### 1. Simple (key-value) structure[​](#1-simple-key-value-structure "Direct link to 1. Simple (key-value) structure")

```
{
  "flags": {
    "enabledFeature": true,
    "disabledFeature": false,
    "intSetting": 5,
    "doubleSetting": 3.14,
    "stringSetting": "test"
  }
}
```

##### 2. Complex (full-featured) structure[​](#2-complex-full-featured-structure "Direct link to 2. Complex (full-featured) structure")

This is the same format that the SDK downloads from the ConfigCat CDN. It allows the usage of all features that are available on the ConfigCat Dashboard.

You can download your current config JSON from ConfigCat's CDN and use it as a baseline.

A convenient way to get the config JSON for a specific SDK Key is to install the [ConfigCat CLI](https://github.com/configcat/cli) tool and execute the following command:

```
configcat config-json get -f v6 -p {YOUR-SDK-KEY} > config.json
```

(Depending on your [Data Governance](https://configcat.com/docs/docs/advanced/data-governance/.md) settings, you may need to add the `--eu` switch.)

Alternatively, you can download the config JSON manually, based on your [Data Governance](https://configcat.com/docs/docs/advanced/data-governance/.md) settings:

* GLOBAL: `https://cdn-global.configcat.com/configuration-files/{YOUR-SDK-KEY}/config_v6.json`
* EU: `https://cdn-eu.configcat.com/configuration-files/{YOUR-SDK-KEY}/config_v6.json`

```
{
  "p": {
    // hash salt, required only when confidential text comparator(s) are used
    "s": "80xCU/SlDz1lCiWFaxIBjyJeJecWjq46T4eu6GtozkM="
  },
  "s": [ // array of segments
    {
      "n": "Beta Users", // segment name
      "r": [ // array of User Conditions (there is a logical AND relation between the elements)
        {
          "a": "Email", // comparison attribute
          "c": 0, // comparator (see below)
          "l": [ // comparison value (see below)
            "john@example.com", "jane@example.com"
          ]
        }
      ]
    }
  ],
  "f": { // key-value map of feature flags & settings
    "isFeatureEnabled": { // key of a particular flag / setting
      "t": 0, // setting type, possible values:
              // 0 -> on/off setting (feature flag)
              // 1 -> text setting
              // 2 -> whole number setting
              // 3 -> decimal number setting
      "r": [ // array of Targeting Rules (there is a logical OR relation between the elements)
        {
          "c": [ // array of conditions (there is a logical AND relation between the elements)
            {
              "u": { // User Condition
                "a": "Email", // comparison attribute
                "c": 2, // comparator, possible values and required comparison value types:
                        // 0  -> IS ONE OF (cleartext) + string array comparison value ("l")
                        // 1  -> IS NOT ONE OF (cleartext) + string array comparison value ("l")
                        // 2  -> CONTAINS ANY OF (cleartext) + string array comparison value ("l")
                        // 3  -> NOT CONTAINS ANY OF (cleartext) + string array comparison value ("l")
                        // 4  -> IS ONE OF (semver) + semver string array comparison value ("l")
                        // 5  -> IS NOT ONE OF (semver) + semver string array comparison value ("l")
                        // 6  -> < (semver) + semver string comparison value ("s")
                        // 7  -> <= (semver + semver string comparison value ("s")
                        // 8  -> > (semver) + semver string comparison value ("s")
                        // 9  -> >= (semver + semver string comparison value ("s")
                        // 10 -> = (number) + number comparison value ("d")
                        // 11 -> <> (number + number comparison value ("d")
                        // 12 -> < (number) + number comparison value ("d")
                        // 13 -> <= (number + number comparison value ("d")
                        // 14 -> > (number) + number comparison value ("d")
                        // 15 -> >= (number) + number comparison value ("d")
                        // 16 -> IS ONE OF (hashed) + string array comparison value ("l")
                        // 17 -> IS NOT ONE OF (hashed) + string array comparison value ("l")
                        // 18 -> BEFORE (UTC datetime) + second-based Unix timestamp number comparison value ("d")
                        // 19 -> AFTER (UTC datetime) + second-based Unix timestamp number comparison value ("d")
                        // 20 -> EQUALS (hashed) + string comparison value ("s")
                        // 21 -> NOT EQUALS (hashed) + string comparison value ("s")
                        // 22 -> STARTS WITH ANY OF (hashed) + string array comparison value ("l")
                        // 23 -> NOT STARTS WITH ANY OF (hashed) + string array comparison value ("l")
                        // 24 -> ENDS WITH ANY OF (hashed) + string array comparison value ("l")
                        // 25 -> NOT ENDS WITH ANY OF (hashed) + string array comparison value ("l")
                        // 26 -> ARRAY CONTAINS ANY OF (hashed) + string array comparison value ("l")
                        // 27 -> ARRAY NOT CONTAINS ANY OF (hashed) + string array comparison value ("l")
                        // 28 -> EQUALS (cleartext) + string comparison value ("s")
                        // 29 -> NOT EQUALS (cleartext) + string comparison value ("s")
                        // 30 -> STARTS WITH ANY OF (cleartext) + string array comparison value ("l")
                        // 31 -> NOT STARTS WITH ANY OF (cleartext) + string array comparison value ("l")
                        // 32 -> ENDS WITH ANY OF (cleartext) + string array comparison value ("l")
                        // 33 -> NOT ENDS WITH ANY OF (cleartext + string array comparison value ("l")
                        // 34 -> ARRAY CONTAINS ANY OF (cleartext) + string array comparison value ("l")
                        // 35 -> ARRAY NOT CONTAINS ANY OF (cleartext) + string array comparison value ("l")
                "l": [ // comparison value - depending on the comparator, another type of value may need
                       // to be specified (see above):
                       // "s": string
                       // "d": number
                  "@example.com"
                ]
              }
            },
            {
              "p": { // Flag Condition (Prerequisite)
                "f": "mainIntFlag", // key of prerequisite flag
                "c": 0, // comparator, possible values: 0 -> EQUALS, 1 -> NOT EQUALS
                "v": { // comparison value (value's type must match the prerequisite flag's type)
                  "i": 42
                }
              }
            },
            {
              "s": { // Segment Condition
                "s": 0, // segment index, a valid index into the top-level segment array ("s")
                "c": 1 // comparator, possible values: 0 -> IS IN SEGMENT, 1 -> IS NOT IN SEGMENT
              }
            }
          ],
          "s": { // alternatively, an array of Percentage Options ("p", see below) can also be specified
            "v": { // the value served when the rule is selected during evaluation
              "b": true
            },
            "i": "bcfb84a7"
          }
        }
      ],
      "p": [ // array of Percentage Options
        {
          "p": 10, // % value
          "v": { // the value served when the Percentage Option is selected during evaluation
            "b": true
          },
          "i": "bcfb84a7"
        },
        {
          "p": 90,
          "v": {
            "b": false
          },
          "i": "bddac6ae"
        }
      ],
      "v": { // fallback value, served when none of the Targeting Rules match,
             // no Percentage Options are defined or evaluation of these is not possible
        "b": false // depending on the setting type, another type of value may need to be specified:
                   // text setting -> "s": string
                   // whole number setting -> "i": number
                   // decimal number setting -> "d": number
      },
      "i": "430bded3" // variation id (for analytical purposes)
    }
  }
}
```

For a more comprehensive specification of the config JSON v6 format, you may refer to [this JSON schema document](https://github.com/configcat/config-json/blob/main/V6/config.schema.json).

### Map[​](#map "Direct link to Map")

You can set up the SDK to load your feature flag & setting overrides from a `HashMap<String, configcat::Value>`.

```
use configcat::{Client, MapDataSource, OverrideBehavior, Value};

let map: MapDataSource = [
    ("enabledFeature", Value::Bool(true)),
    ("disabledFeature", Value::Bool(false)),
    ("intSetting", Value::Int(5)),
    ("doubleSetting", Value::Float(1.2)),
    ("stringSetting", Value::String("test".to_owned())),
].into();

let client = Client::builder("localhost")
    .overrides(Box::new(map), OverrideBehavior::LocalOnly)
    .build()
    .unwrap();
```

## `get_all_keys()`[​](#get_all_keys "Direct link to get_all_keys")

You can get the keys for all available feature flags and settings by calling the `get_all_keys()` method.

```
let client = Client::new("#YOUR-SDK-KEY#").unwrap();
let keys = client.get_all_keys().await;
```

## `get_all_values()`[​](#get_all_values "Direct link to get_all_values")

Evaluates and returns the values of all feature flags and settings. Passing a [User Object](#user-object) is optional.

```
let client = Client::new("#YOUR-SDK-KEY#").unwrap();
let values = await client.get_all_values(None).await;

// invoke with User Object
let user = User::new("#UNIQUE-USER-IDENTIFIER#");
let values_with_user = await client.get_all_values(Some(user)).await;
```

## `get_all_value_details()`[​](#get_all_value_details "Direct link to get_all_value_details")

Evaluates and returns the values along with evaluation details of all feature flags and settings. Passing a [User Object](#user-object) is optional.

```
let client = Client::new("#YOUR-SDK-KEY#").unwrap();
let details = await client.get_all_value_details(None).await;

// invoke with User Object
let user = User::new("#UNIQUE-USER-IDENTIFIER#");
let details_with_user = await client.get_all_value_details(Some(user)).await;
```

## Cache[​](#cache "Direct link to Cache")

The *ConfigCat SDK* stores the downloaded config data in a local cache to minimize network traffic and enhance client performance. If you prefer to use your own cache solution, such as an external or distributed cache in your system, you can implement the [`ConfigCache`](https://github.com/configcat/rust-sdk/blob/main/src/cache.rs) trait and call the `cache()` method of the `ClientBuilder` with your implementation. This allows you to seamlessly integrate ConfigCat with your existing caching infrastructure.

```
struct CustomCache {}

impl ConfigCache for CustomCache {
    fn read(&self, key: &str) -> Option<String> {
        // here you have to return with the cached value
    }

    fn write(&self, key: &str, value: &str) {
        // here you have to store the new value in the cache
    }
}
```

Then use your custom cache implementation:

```
let client = Client::builder("#YOUR-SDK-KEY#")
    .cache(Box::new(CustomCache{}))
    .build()
    .unwrap();
```

## HTTP Proxy[​](#http-proxy "Direct link to HTTP Proxy")

The SDK uses the [`reqwest`](https://docs.rs/reqwest) crate for HTTP communication. This crate supports [HTTP proxies](https://docs.rs/reqwest/#proxies) via the `HTTP_PROXY` / `HTTPS_PROXY` environment variables.

## HTTP Timeout[​](#http-timeout "Direct link to HTTP Timeout")

You can set the maximum wait time for a ConfigCat HTTP response.

```
let client = Client::builder("#YOUR-SDK-KEY#")
    .http_timeout(Duration::from_secs(60));
    .build()
    .unwrap();
```

The default timeout is `30` seconds.

## Logging[​](#logging "Direct link to Logging")

The SDK uses the [`log`](https://docs.rs/log) crate for logging, so you can use any package that implements the `log::Log` trait.

`Info` level logging helps to inspect how a feature flag was evaluated:

```
INFO [5000] Evaluating 'isPOCFeatureEnabled' for User '{"Identifier":"<SOME USERID>","Email":"configcat@example.com","Country":"US","SubscriptionType":"Pro","Role":"Admin","version":"1.0.0"}'
  Evaluating targeting rules and applying the first match if any:
  - IF User.Email CONTAINS ANY OF ['@something.com'] THEN 'false' => no match
  - IF User.Email CONTAINS ANY OF ['@example.com'] THEN 'true' => MATCH, applying rule
  Returning 'true'.
```

As an example, [this](https://github.com/configcat/rust-sdk/blob/main/examples/print_eval.rs) sample app defines a [minimal `log::Log` implementation](https://github.com/configcat/rust-sdk/blob/main/examples/print_eval.rs#L36) that uses `println!()` to show log messages on the console.

## Sample Applications[​](#sample-applications "Direct link to Sample Applications")

Check out our Sample Applications how they use the *ConfigCat SDK*:

* [Sample App](https://github.com/configcat/rust-sdk/blob/main/examples/print_eval.rs)

## Look under the hood[​](#look-under-the-hood "Direct link to Look under the hood")

* [ConfigCat Rust SDK on GitHub](https://github.com/configcat/rust-sdk)
* [ConfigCat Rust SDK on crates.io](https://crates.io/crates/configcat)
* [ConfigCat Rust SDK on docs.rs](https://docs.rs/configcat)
