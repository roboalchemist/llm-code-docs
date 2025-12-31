# Source: https://configcat.com/docs/sdk-reference/python.md

# Source: https://configcat.com/docs/sdk-reference/openfeature/python.md

# Source: https://configcat.com/docs/sdk-reference/python.md

# Source: https://configcat.com/docs/sdk-reference/openfeature/python.md

# Source: https://configcat.com/docs/sdk-reference/python.md

# Source: https://configcat.com/docs/sdk-reference/openfeature/python.md

# Source: https://configcat.com/docs/sdk-reference/python.md

# Source: https://configcat.com/docs/sdk-reference/openfeature/python.md

# Source: https://configcat.com/docs/sdk-reference/python.md

# Source: https://configcat.com/docs/sdk-reference/openfeature/python.md

# Source: https://configcat.com/docs/sdk-reference/python.md

# Python SDK Reference

[![Star on GitHub](https://img.shields.io/github/stars/configcat/python-sdk.svg?style=social)](https://github.com/configcat/python-sdk/stargazers) [![Python CI](https://github.com/configcat/python-sdk/actions/workflows/python-ci.yml/badge.svg?branch=master)](https://github.com/configcat/python-sdk/actions/workflows/python-ci.yml) [![codecov](https://codecov.io/gh/ConfigCat/python-sdk/branch/master/graph/badge.svg)](https://codecov.io/gh/ConfigCat/python-sdk) [![PyPI](https://img.shields.io/pypi/v/configcat-client.svg)](https://pypi.python.org/pypi/configcat-client) [![PyPI](https://img.shields.io/pypi/pyversions/configcat-client.svg)](https://pypi.python.org/pypi/configcat-client) [![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=configcat_python-sdk\&metric=vulnerabilities)](https://sonarcloud.io/dashboard?id=configcat_python-sdk)

[ConfigCat Python SDK on GitHub](https://github.com/configcat/python-sdk)

## Getting started[​](#getting-started "Direct link to Getting started")

### 1. Install *ConfigCat SDK*[​](#1-install-configcat-sdk "Direct link to 1-install-configcat-sdk")

```
pip install configcat-client
```

### 2. Import the package[​](#2-import-the-package "Direct link to 2. Import the package")

```
import configcatclient
```

### 3. Create the *ConfigCat* client with your *SDK Key*[​](#3-create-the-configcat-client-with-your-sdk-key "Direct link to 3-create-the-configcat-client-with-your-sdk-key")

```
client = configcatclient.get('#YOUR-SDK-KEY#')
```

### 4. Get your setting value[​](#4-get-your-setting-value "Direct link to 4. Get your setting value")

```
is_my_awesome_feature_enabled = client.get_value('isMyAwesomeFeatureEnabled', False)
if is_my_awesome_feature_enabled:
    do_the_new_thing()
else:
    do_the_old_thing()
```

### 5. Stop *ConfigCat* client[​](#5-stop-configcat-client "Direct link to 5-stop-configcat-client")

You can safely shut down all clients at once or individually and release all associated resources on application exit.

```
configcatclient.close_all() # closes all clients

client.close() # closes a specific client
```

## Creating the *ConfigCat Client*[​](#creating-the-configcat-client "Direct link to creating-the-configcat-client")

*ConfigCat Client* is responsible for:

* managing the communication between your application and ConfigCat servers.
* caching your setting values and feature flags.
* serving values quickly in a failsafe way.

`configcatclient.get('#YOUR-SDK-KEY#')` returns a client with default options.

| Client options            | Description                                                                                                                                                                                                                                                                                         | Default                  |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ |
| `base_url`                | *Obsolete*, sets the CDN base url (forward proxy, dedicated subscription) from where the sdk will download the config JSON.                                                                                                                                                                         | None                     |
| `polling_mode`            | Sets the polling mode for the client. [More about polling modes](#polling-modes).                                                                                                                                                                                                                   | PollingMode.auto\_poll() |
| `config_cache`            | Sets a custom config cache implementation for the client. [More about cache](#custom-cache).                                                                                                                                                                                                        | None                     |
| `proxies`                 | Sets custom proxies for the client. [More about proxy](#using-configcat-behind-a-proxy).                                                                                                                                                                                                            | None                     |
| `proxy_auth`              | Sets proxy authentication for the custom proxies. [More about proxy](#using-configcat-behind-a-proxy).                                                                                                                                                                                              | None                     |
| `connect_timeout_seconds` | The number of seconds to wait for the server to make the initial connection (i.e. completing the TCP connection handshake).                                                                                                                                                                         | 10                       |
| `read_timeout_seconds`    | The number of seconds to wait for the server to respond before giving up.                                                                                                                                                                                                                           | 30                       |
| `flag_overrides`          | Local feature flag & setting overrides. [More about feature flag overrides](#flag-overrides)                                                                                                                                                                                                        | None                     |
| `data_governance`         | Describes the location of your feature flag and setting data within the ConfigCat CDN. This parameter needs to be in sync with your Data Governance preferences. [More about Data Governance](https://configcat.com/docs/docs/advanced/data-governance/.md). Available options: `Global`, `EuOnly`. | `Global`                 |
| `default_user`            | Sets the default user. [More about default user](#default-user).                                                                                                                                                                                                                                    | None                     |
| `hooks`                   | Used to subscribe events that the SDK sends in specific scenarios. [More about hooks](#hooks).                                                                                                                                                                                                      | None                     |
| `offline`                 | Indicates whether the SDK should be initialized in offline mode. [More about offline mode](#online--offline-mode).                                                                                                                                                                                  | False                    |

```
client = configcatclient.get('#YOUR-SDK-KEY#',
    ConfigCatOptions(
        polling_mode=PollingMode.auto_poll()
    )
)
```

caution

We strongly recommend you to use the *ConfigCat Client* as a Singleton object in your application. The `configcatclient.get()` static factory method constructs singleton client instances for your SDK keys. These clients can be closed all at once with the `configcatclient.close_all()` method or individually with `client.close()`.

## Anatomy of `get_value()`[​](#anatomy-of-get_value "Direct link to anatomy-of-get_value")

| Parameters      | Description                                                                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `key`           | **REQUIRED.** Setting-specific key. Set on *ConfigCat Dashboard* for each setting.                                                                      |
| `default_value` | **REQUIRED.** This value will be returned in case of an error.                                                                                          |
| `user`          | Optional, *User Object*. Essential when using Targeting. [Read more about Targeting.](https://configcat.com/docs/docs/targeting/targeting-overview/.md) |

```
value = client.get_value(
    'keyOfMySetting', # Setting Key
    False, # Default value
    User('#UNIQUE-USER-IDENTIFIER#') # Optional User Object
)
```

## Anatomy of `get_value_details()`[​](#anatomy-of-getvaluedetails "Direct link to anatomy-of-getvaluedetails")

`get_value_details()` is similar to `get_value()` but instead of returning the evaluated value only, it gives an *EvaluationDetails* object with more detailed information about the evaluation result.

| Parameters     | Description                                                                                                                                             |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `key`          | **REQUIRED.** Setting-specific key. Set on *ConfigCat Dashboard* for each setting.                                                                      |
| `defaultValue` | **REQUIRED.** This value will be returned in case of an error.                                                                                          |
| `user`         | Optional, *User Object*. Essential when using Targeting. [Read more about Targeting.](https://configcat.com/docs/docs/targeting/targeting-overview/.md) |

```
details = client.get_value_details(
    'keyOfMySetting', # Setting Key
    False, # Default value
    User('#UNIQUE-USER-IDENTIFIER#') # Optional User Object
)
```

The details result contains the following information:

| Property                    | Description                                                                                                |
| --------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `value`                     | The evaluated value of the feature flag or setting.                                                        |
| `key`                       | The key of the evaluated feature flag or setting.                                                          |
| `is_default_value`          | True when the default value passed to `get_value_details()` is returned due to an error.                   |
| `error`                     | In case of an error, this property contains the error message.                                             |
| `user`                      | The User Object that was used for evaluation.                                                              |
| `matched_targeting_rule`    | The Targeting Rule (if any) that matched during the evaluation and was used to return the evaluated value. |
| `matched_percentage_option` | The Percentage Option (if any) that was used to select the evaluated value.                                |
| `fetch_time`                | The last download time (UTC *datetime*) of the current config.                                             |

## User Object[​](#user-object "Direct link to User Object")

The [User Object](https://configcat.com/docs/docs/targeting/user-object/.md) is essential if you'd like to use ConfigCat's [Targeting](https://configcat.com/docs/docs/targeting/targeting-overview/.md) feature.

```
user_object = User('#UNIQUE-USER-IDENTIFIER#')
```

```
user_object = User('john@example.com')
```

### Customized User Object creation[​](#customized-user-object-creation "Direct link to Customized User Object creation")

| Parameters   | Description                                                                                                                       |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------- |
| `identifier` | **REQUIRED.** Unique identifier of a user in your application. Can be any `string` value, even an email address.                  |
| `email`      | Optional parameter for easier Targeting Rule definitions.                                                                         |
| `country`    | Optional parameter for easier Targeting Rule definitions.                                                                         |
| `custom`     | Optional `dictionary` for custom attributes of a user for advanced Targeting Rule definitions. E.g. User role, Subscription type. |

```
user_object = User(
  '#UNIQUE-USER-IDENTIFIER#',
  'john@example',
  'United Kingdom',
  { SubscriptionType: 'Pro', UserRole: 'Admin' }
)
```

The `custom` dictionary also allows attribute values other than `string` values:

```
user_object = User(
    '#UNIQUE-USER-IDENTIFIER#',
    custom={
        'Rating': 4.5,
        'RegisteredAt': datetime.fromisoformat('2023-11-22 12:34:56 +00:00'),
        'Roles': [ 'Role1', 'Role2' ]
    }
)
```

### User Object Attribute Types[​](#user-object-attribute-types "Direct link to User Object Attribute Types")

All comparators support `string` values as User Object attribute (in some cases they need to be provided in a specific format though, see below), but some of them also support other types of values. It depends on the comparator how the values will be handled. The following rules apply:

**Text-based comparators** (EQUALS, IS\_ONE\_OF, etc.)

* accept `string` values,
* all other values are automatically converted to `string` (a warning will be logged but evaluation will continue as normal).

**SemVer-based comparators** (IS\_ONE\_OF\_SEMVER, LESS\_THAN\_SEMVER, GREATER\_THAN\_SEMVER, etc.)

* accept `string` values containing a properly formatted, valid semver value,
* all other values are considered invalid (a warning will be logged and the currently evaluated Targeting Rule will be skipped).

**Number-based comparators** (EQUALS\_NUMBER, LESS\_THAN\_NUMBER, GREATER\_THAN\_OR\_EQUAL\_NUMBER, etc.)

* accept `float` values and all other numeric values which can safely be converted to `float`,
* accept `string` values containing a properly formatted, valid `float` value,
* all other values are considered invalid (a warning will be logged and the currently evaluated Targeting Rule will be skipped).

**Date time-based comparators** (BEFORE\_DATETIME / AFTER\_DATETIME)

* accept `datetime` values, which are automatically converted to a second-based Unix timestamp (`datetime` values with naive timezone are considered to be in UTC),
* accept `float` values representing a second-based Unix timestamp and all other numeric values which can safely be converted to `float`,
* accept `string` values containing a properly formatted, valid `float` value,
* all other values are considered invalid (a warning will be logged and the currently evaluated Targeting Rule will be skipped).

**String array-based comparators** (ARRAY\_CONTAINS\_ANY\_OF / ARRAY\_NOT\_CONTAINS\_ANY\_OF)

* accept arrays of `string`,
* accept `string` values containing a valid JSON string which can be deserialized to an array of `string`,
* all other values are considered invalid (a warning will be logged and the currently evaluated Targeting Rule will be skipped).

### Default user[​](#default-user "Direct link to Default user")

There's an option to set a default User Object that will be used at feature flag and setting evaluation. It can be useful when your application has a single user only, or rarely switches users.

You can set the default User Object either on SDK initialization:

```
client = configcatclient.get('#YOUR-SDK-KEY#',
    ConfigCatOptions(
        default_user=User('john@example.com')
    )
)
```

or with the `set_default_user()` method of the ConfigCat client.

```
client.set_default_user(User('john@example.com'))
```

Whenever the `get_value()`, `get_value_details()`, `get_variation_id()`, `get_all_variation_ids()`, or `get_all_values()` methods are called without an explicit `user` parameter, the SDK will automatically use the default user as a User Object.

```
client = configcatclient.get('#YOUR-SDK-KEY#',
    ConfigCatOptions(
        default_user=User('john@example.com')
    )
)
# The default user will be used at the evaluation process.
value = client.get_value('keyOfMySetting', False)
```

When the `user` parameter is specified on the requesting method, it takes precedence over the default user.

```
client = configcatclient.get('#YOUR-SDK-KEY#',
    ConfigCatOptions(
        default_user=User('john@example.com')
    )
)
other_user = User('brian@example.com')
# otherUser will be used at the evaluation process.
value = client.get_value('keyOfMySetting', False, other_user)
```

For deleting the default user, you can do the following:

```
client.clear_default_user()
```

## Polling Modes[​](#polling-modes "Direct link to Polling Modes")

The *ConfigCat SDK* supports 3 different polling strategies to fetch feature flags and settings from the ConfigCat CDN. Once the latest data is downloaded, it is stored in the cache, then calls to `get_value()` use the cached data to evaluate feature flags and settings. With the following polling modes, you can customize the SDK to best fit to your application's lifecycle.<br />[More about polling modes.](https://configcat.com/docs/docs/advanced/caching/.md)

### Auto polling (default)[​](#auto-polling-default "Direct link to Auto polling (default)")

The *ConfigCat SDK* downloads the latest config data from the ConfigCat CDN automatically every 60 seconds and stores it in the cache.

Use the `poll_interval_seconds` option parameter of the `PollingMode.auto_poll()` to change the polling interval.

```
client = configcatclient.get('#YOUR-SDK-KEY#',
    ConfigCatOptions(
        polling_mode=PollingMode.auto_poll(poll_interval_seconds=95)
    )
)
```

Available options:

| Option Parameter             | Description                                                                                         | Default |
| ---------------------------- | --------------------------------------------------------------------------------------------------- | ------- |
| `poll_interval_seconds`      | Polling interval.                                                                                   | 60      |
| `max_init_wait_time_seconds` | Maximum waiting time between the client initialization and the first config acquisition in seconds. | 5       |

caution

Auto polling mode utilizes its polling job in a `threading.Thread` object. If you are running your application behind an uWSGI web server, the auto polling mode may not work as expected because the uWSGI web server disables Python's threading by default. Please [enable threading](https://uwsgi-docs.readthedocs.io/en/latest/Options.html#enable-threads) or switch to another polling mode in this case.

### Lazy loading[​](#lazy-loading "Direct link to Lazy loading")

When calling `get_value()`, the *ConfigCat SDK* downloads the latest config data from the ConfigCat CDN only if it is not already present in the cache, or if the cache has expired. In this case `get_value()` will return the setting value after the cache is updated.

Use `cache_refresh_interval_seconds` option parameter to set cache lifetime.

```
client = configcatclient.get('#YOUR-SDK-KEY#',
    ConfigCatOptions(
        polling_mode=PollingMode.lazy_load(cache_refresh_interval_seconds=600)
    )
)
```

Available options:

| Option Parameter                 | Description | Default |
| -------------------------------- | ----------- | ------- |
| `cache_refresh_interval_seconds` | Cache TTL.  | 60      |

### Manual polling[​](#manual-polling "Direct link to Manual polling")

Manual polling gives you full control over when the config data is downloaded from the ConfigCat CDN. The *ConfigCat SDK* will not download it automatically. Calling `force_refresh()` is your application's responsibility.

```
client = configcatclient.get('#YOUR-SDK-KEY#',
    ConfigCatOptions(
        polling_mode=PollingMode.manual_poll()
    )
)
client.force_refresh()
```

> `get_value()` returns `default_value` if the cache is empty. Call `force_refresh()` to update the cache.

```
client = configcatclient.get('#YOUR-SDK-KEY#',
    ConfigCatOptions(
        polling_mode=PollingMode.manual_poll()
    )
)
value = client.get_value('key', 'my default value') # Returns "my default value"
client.force_refresh()
value = client.get_value('key', 'my default value') # Returns "value from server"
```

## Hooks[​](#hooks "Direct link to Hooks")

The SDK provides several hooks (events), by means of which you can get notified of its actions. You can subscribe to the following events emitted by the *ConfigCat* client:

* `on_client_ready()`: This event is emitted when the client reaches the ready state, i.e. completes initialization.

  * If Lazy Loading or Manual Polling is used, it's considered ready right after instantiation.

  * If Auto Polling is used, the ready state is reached as soon as

    <!-- -->

    * the initial sync with the external cache yields up-to-date config data,
    * otherwise, if the client is online (i.e. HTTP requests are allowed), the first config fetch operation completes (regardless of success or failure),
    * or the time specified via Auto Polling's `max_init_wait_time_seconds` option has passed.

  Reaching the ready state usually means the client is ready to evaluate feature flags and settings. However, please note that this is not guaranteed. In case of initialization failure or timeout, the internal cache may be empty or expired even after the ready state is reported. Alternatively, in Auto Polling mode, you can wait for the first `onConfigChanged` event to be notified when the internal cache is actually populated with config data.

* `on_config_changed(config: dict)`: This event is emitted first when the client's internal cache gets populated. Afterwards, it is emitted again each time the internally cached config is updated to a newer version, either as a result of synchronization with the external cache, or as a result of fetching a newer version from the ConfigCat CDN.

* `on_flag_evaluated(evaluation_details: EvaluationDetails)`: This event is emitted each time the client evaluates a feature flag or setting. The event provides the same evaluation details that you would get from [`get_value_details()`](#anatomy-of-getvaluedetails).

* `on_error(error: str)`: This event is emitted when an error occurs within the client.

You can subscribe to these events either on SDK initialization:

```
def on_flag_evaluated(evaluation_details):
    # handle the event
    pass

client = configcatclient.get('#YOUR-SDK-KEY#',
    ConfigCatOptions(
        hooks=Hooks(on_flag_evaluated=on_flag_evaluated)
    )
)
```

or with the `get_hooks()` method of the ConfigCat client:

```
client.get_hooks().add_on_flag_evaluated(on_flag_evaluated)
```

## Online / Offline mode[​](#online--offline-mode "Direct link to Online / Offline mode")

In cases when you'd want to prevent the SDK from making HTTP calls, you can put it in offline mode:

```
client.set_offline()
```

In offline mode, the SDK won't initiate HTTP requests and will work only from its cache.

To put the SDK back in online mode, you can do the following:

```
client.set_online()
```

> With `client.is_offline()` you can check whether the SDK is in offline mode.

## Flag Overrides[​](#flag-overrides "Direct link to Flag Overrides")

With flag overrides you can overwrite the feature flags & settings downloaded from the ConfigCat CDN with local values. Moreover, you can specify how the overrides should apply over the downloaded values. The following 3 behaviours are supported:

* **Local only** (`OverrideBehaviour.LocalOnly`): When evaluating values, the SDK will not use feature flags & settings from the ConfigCat CDN, but it will use all feature flags & settings that are loaded from local-override sources.

* **Local over remote** (`OverrideBehaviour.LocalOverRemote`): When evaluating values, the SDK will use all feature flags & settings that are downloaded from the ConfigCat CDN, plus all feature flags & settings that are loaded from local-override sources. If a feature flag or a setting is defined both in the downloaded and the local-override source then the local-override version will take precedence.

* **Remote over local** (`OverrideBehaviour.RemoteOverLocal`): When evaluating values, the SDK will use all feature flags & settings that are downloaded from the ConfigCat CDN, plus all feature flags & settings that are loaded from local-override sources. If a feature flag or a setting is defined both in the downloaded and the local-override source then the downloaded version will take precedence.

You can set up the SDK to load your feature flag & setting overrides from a file or a dictionary.

### JSON File[​](#json-file "Direct link to JSON File")

The SDK can load your feature flag & setting overrides from a file.

#### File[​](#file "Direct link to File")

```
client = configcatclient.get('#YOUR-SDK-KEY#',
    ConfigCatOptions(
        flag_overrides=LocalFileFlagOverrides(
            file_path='path/to/the/local_flags.json',  # path to the file
            override_behaviour=OverrideBehaviour.LocalOnly
        )
    )
)
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

### Dictionary[​](#dictionary "Direct link to Dictionary")

You can set up the SDK to load your feature flag & setting overrides from a dictionary.

```
dictionary = {
    'enabledFeature': True,
    'disabledFeature': False,
    'intSetting': 5,
    'doubleSetting': 3.14,
    'stringSetting': 'test'
}

client = configcatclient.get('#YOUR-SDK-KEY#',
    ConfigCatOptions(
        flag_overrides=LocalDictionaryFlagOverrides(source=dictionary, override_behaviour=OverrideBehaviour.LocalOnly)
    )
)
```

## Logging[​](#logging "Direct link to Logging")

The *ConfigCat SDK* uses Python's built-in [logging library](https://docs.python.org/3/library/logging.html).

With the `logging.basicConfig()` method, you can set up the logging system. The following example shows how to set the default root logger to write logs to the standard output with `INFO` log level.

```
import logging
logging.basicConfig(level=logging.INFO)
```

The *ConfigCat SDK* specifies an internal logger called `'configcat'`. The following example shows how to set the *Log Level* on the internal *ConfigCat* logger.

```
logger = logging.getLogger('configcat')
logger.setLevel(logging.INFO)
```

Available log levels:

| Level | Description                                                                             |
| ----- | --------------------------------------------------------------------------------------- |
| ERROR | Only error level events are logged.                                                     |
| WARN  | Default. Errors and Warnings are logged.                                                |
| INFO  | Errors, Warnings and feature flag evaluation is logged.                                 |
| DEBUG | All of the above plus debug info is logged. Debug logs can be different for other SDKs. |

Info level logging helps to inspect the feature flag evaluation process:

```
INFO:configcat:[5000] Evaluating 'isPOCFeatureEnabled' for User '{"Identifier":"<SOME USERID>","Email":"configcat@example.com","Country":"US","SubscriptionType":"Pro","Role":"Admin","version":"1.0.0"}'
  Evaluating targeting rules and applying the first match if any:
  - IF User.Email CONTAINS ANY OF ['@something.com'] THEN 'False' => no match
  - IF User.Email CONTAINS ANY OF ['@example.com'] THEN 'True' => MATCH, applying rule
  Returning 'True'.
```

## `get_all_keys()`[​](#get_all_keys "Direct link to get_all_keys")

You can get the keys for all available feature flags and settings by calling the `get_all_keys()` method.

```
client = configcatclient.get('#YOUR-SDK-KEY#')
keys = client.get_all_keys()
```

## `get_all_values()`[​](#get_all_values "Direct link to get_all_values")

Evaluates and returns the values of all feature flags and settings. Passing a [User Object](#user-object) is optional.

| Parameters | Description                                                                                                                                             |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `user`     | Optional, *User Object*. Essential when using Targeting. [Read more about Targeting.](https://configcat.com/docs/docs/targeting/targeting-overview/.md) |

```
client = configcatclient.get('#YOUR-SDK-KEY#')
all_values = client.get_all_values(User('#UNIQUE-USER-IDENTIFIER#'))  # Optional User Object
```

## `get_all_value_details()`[​](#get_all_value_details "Direct link to get_all_value_details")

Evaluates and returns the detailed values of all feature flags and settings. Passing a [User Object](#user-object) is optional.

```
client = configcatclient.get('#YOUR-SDK-KEY#')
all_value_details = client.get_all_value_details(User('#UNIQUE-USER-IDENTIFIER#'))  # Optional User Object
```

## Custom cache[​](#custom-cache "Direct link to Custom cache")

The *ConfigCat SDK* stores the downloaded config data in a local cache to minimize network traffic and enhance client performance. If you prefer to use your own cache solution, such as an external or distributed cache in your system, you can implement the [`ConfigCache`](https://github.com/configcat/python-sdk/blob/master/configcatclient/interfaces.py) interface and set the `config_cache` parameter in the options passed to `configcatclient.get`. This allows you to seamlessly integrate ConfigCat with your existing caching infrastructure.

```
from configcatclient.interfaces import ConfigCache

class InMemoryConfigCache(ConfigCache):
    def __init__(self):
        self._value = {}

    def get(self, key):
        # you should return the cached value
        return self._value.get(key)

    def set(self, key, value):
        # you should cache the new value
        self._value[key] = value
```

Then use your custom cache implementation:

```
client = configcatclient.get('#YOUR-SDK-KEY#',
    ConfigCatOptions(
        config_cache=InMemoryConfigCache()
    )
)
```

info

The Python SDK supports *shared caching*. You can read more about this feature and the required minimum SDK versions [here](https://configcat.com/docs/docs/advanced/caching/.md#shared-cache).

## Using ConfigCat behind a proxy[​](#using-configcat-behind-a-proxy "Direct link to Using ConfigCat behind a proxy")

Provide your own network credentials (username/password), and proxy server settings (proxy server/port) by passing the proxy details to the creator method.

```
proxies = {'https': '127.0.0.1:8080'}
proxy_auth = HTTPProxyAuth('user', 'password')
client = configcatclient.get('#YOUR-SDK-KEY#',
    ConfigCatOptions(
        proxies=proxies,
        proxy_auth=proxy_auth
    )
)
```

## Sample Applications[​](#sample-applications "Direct link to Sample Applications")

* [Sample Console App](https://github.com/configcat/python-sdk/tree/master/samples/consolesample)
* [Django Web App](https://github.com/configcat/python-sdk/tree/master/samples/webappsample)

## Guides[​](#guides "Direct link to Guides")

See [this](https://configcat.com/blog/2022/08/12/how-to-use-feature-flag-with-flask/) guide on how to use ConfigCat's Python SDK in a Flask application.

## Look under the hood[​](#look-under-the-hood "Direct link to Look under the hood")

* [ConfigCat's Python SDK on GitHub](https://github.com/configcat/python-sdk)
* [ConfigCat's Python SDK in PyPI](https://pypi.org/project/configcat-client/)
