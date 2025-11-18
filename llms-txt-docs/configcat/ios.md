# Source: https://configcat.com/docs/sdk-reference/ios.md

# Swift (iOS) SDK Reference

[![Star on GitHub](https://img.shields.io/github/stars/configcat/swift-sdk.svg?style=social)](https://github.com/configcat/swift-sdk/stargazers) [![Build Status](https://github.com/configcat/swift-sdk/actions/workflows/swift-ci.yml/badge.svg?branch=master)](https://github.com/configcat/swift-sdk/actions/workflows/swift-ci.yml) [![CocoaPods](https://img.shields.io/cocoapods/v/ConfigCat.svg)](https://cocoapods.org/pods/ConfigCat) [![Supported Platforms](https://img.shields.io/cocoapods/p/ConfigCat.svg?style=flat)](https://configcat.com/docs/sdk-reference/ios) [![Coverage Status](https://img.shields.io/sonar/coverage/configcat_swift-sdk?logo=SonarCloud\&server=https%3A%2F%2Fsonarcloud.io)](https://sonarcloud.io/project/overview?id=configcat_swift-sdk) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=configcat_swift-sdk\&metric=alert_status)](https://sonarcloud.io/dashboard?id=configcat_swift-sdk)

[ConfigCat Swift SDK on GitHub](https://github.com/configcat/swift-sdk)

## Getting Started[​](#getting-started "Direct link to Getting Started")

### 1. Add the ConfigCat SDK to your project[​](#1-add-the-configcat-sdk-to-your-project "Direct link to 1. Add the ConfigCat SDK to your project")

* CocoaPods
* Carthage
* Swift Package Manager

Podfile

```
target '<YOUR TARGET>' do
pod 'ConfigCat'
end
```

Then, run the following command to install your dependencies:

```
pod install
```

Cartfile

```
github "configcat/swift-sdk"
```

Then, run the carthage update command and then follow the Carthage integration steps to link the framework with your project.

Add the SDK to your `Package.swift`.

Package.swift

```
dependencies: [
    .package(
        url: "https://github.com/configcat/swift-sdk",
        from: "11.0.1"
    )
]
```

### 2. Import the ConfigCat SDK[​](#2-import-the-configcat-sdk "Direct link to 2. Import the ConfigCat SDK")

* Swift
* Objective-C

```
import ConfigCat
```

```
@import ConfigCat;
```

### 3. Create the *ConfigCat* client with your *SDK Key*[​](#3-create-the-configcat-client-with-your-sdk-key "Direct link to 3-create-the-configcat-client-with-your-sdk-key")

* Swift
* Objective-C

```
let client = ConfigCatClient.get(sdkKey: "#YOUR-SDK-KEY#")
```

```
ConfigCatClient* client = [ConfigCatClient getWithSdkKey:@"#YOUR-SDK-KEY#"
                                                 options:NULL];
```

### 4. Get your setting value[​](#4-get-your-setting-value "Direct link to 4. Get your setting value")

* Swift
* Objective-C

```
client.getValue(for: "isMyAwesomeFeatureEnabled", defaultValue: false) { isMyAwesomeFeatureEnabled in
    if isMyAwesomeFeatureEnabled {
        doTheNewThing()
    } else {
        doTheOldThing()
    }
}

// Or with async/await
let isMyAwesomeFeatureEnabled = await client.getValue(for: "isMyAwesomeFeatureEnabled", defaultValue: false)
if isMyAwesomeFeatureEnabled {
    doTheNewThing()
} else {
    doTheOldThing()
}
```

```
[client getBoolValueFor:@"isMyAwesomeFeatureEnabled"
           defaultValue:false
                   user:NULL
             completion:^(BOOL isMyAwesomeFeatureEnabled) {
    if (isMyAwesomeFeatureEnabled) {
        // do the new thing
    } else {
        // do the old thing
    }
}];
```

The *ConfigCat SDK* also offers a synchronous API for feature flag evaluation. Read more [here](#snapshots-and-non-blocking-synchronous-feature-flag-evaluation).

### 5. Close ConfigCat client​[​](#5-close-configcat-client "Direct link to 5. Close ConfigCat client​")

You can safely shut down all clients at once or individually and release all associated resources on application exit.

* Swift
* Objective-C

```
ConfigCatClient.closeAll() // closes all clients

client.close() // closes the specific client
```

```
[ConfigCatClient closeAll]; // closes all clients

[client close]; // closes the specific client
```

## Supported platform versions[​](#supported-platform-versions "Direct link to Supported platform versions")

The following device platform versions are supported:

| Platform | Version  |
| -------- | -------- |
| iOS      | >= 12.0  |
| watchOS  | >= 4.0   |
| tvOS     | >= 12.0  |
| macOS    | >= 10.13 |
| visionOS | >= 1.0   |

## Creating the *ConfigCat Client*[​](#creating-the-configcat-client "Direct link to creating-the-configcat-client")

*ConfigCat Client* is responsible for:

* managing the communication between your application and ConfigCat servers.
* caching your setting values and feature flags.
* serving values quickly in a failsafe way.

`ConfigCatClient.get(sdkKey: <sdkKey>)` returns a client with default options.

### Customizing the *ConfigCat Client*[​](#customizing-the-configcat-client "Direct link to customizing-the-configcat-client")

To customize the SDK's behavior, you can pass an additional `(ConfigCatOptions) -> ()` parameter to the `get()` static factory method where the `ConfigCatOptions` class is used to set up the *ConfigCat Client*.

* Swift
* Objective-C

```
let client = ConfigCatClient.get(sdkKey: "#YOUR-SDK-KEY#") { options in
    options.pollingMode = PollingModes.manualPoll()
    options.logLevel = .info
}
```

```
ConfigCatClient* client = [ConfigCatClient getWithSdkKey:@"#YOUR-SDK-KEY#"
                                            configurator:^(ConfigCatOptions* options) {
    options.pollingMode = [PollingModes manualPoll];
    options.logLevel = LogLevelInfo;
}];
```

These are the available options on the `ConfigCatOptions` class:

| Arguments              | Type                      | Description                                                                                                                                                                                                                                                                                                                         |
| ---------------------- | ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `dataGovernance`       | `DataGovernance`          | Optional, defaults to `global`. Describes the location of your feature flag and setting data within the ConfigCat CDN. This parameter needs to be in sync with your Data Governance preferences. [More about Data Governance](https://configcat.com/docs/docs/advanced/data-governance/.md). Available options: `global`, `euOnly`. |
| `configCache`          | `ConfigCache?`            | Optional, sets a custom cache implementation for the client. [More about cache](#custom-cache).                                                                                                                                                                                                                                     |
| `pollingMode`          | `PollingMode`             | Optional, sets the polling mode for the client. [More about polling modes](#polling-modes).                                                                                                                                                                                                                                         |
| `sessionConfiguration` | `URLSessionConfiguration` | Optional, sets a custom `URLSessionConfiguration` used by the HTTP calls.                                                                                                                                                                                                                                                           |
| `baseUrl`              | `String`                  | Optional, sets the CDN base url (forward proxy, dedicated subscription) from where the sdk will download the config JSON.                                                                                                                                                                                                           |
| `flagOverrides`        | `OverrideDataSource?`     | Optional, sets the local feature flag & setting overrides. [More about feature flag overrides](#flag-overrides).                                                                                                                                                                                                                    |
| `logLevel`             | `LogLevel`                | Optional, sets the internal log level. [More about logging.](#logging).                                                                                                                                                                                                                                                             |
| `defaultUser`          | `ConfigCatUser?`          | Optional, sets the default user. [More about default user](#default-user).                                                                                                                                                                                                                                                          |
| `logger`               | `ConfigCatLogger`         | Optional, sets the logger implementation used by the SDK. [More about logging](#logging)                                                                                                                                                                                                                                            |
| `offline`              | `Bool`                    | Optional, defaults to `false`. Indicates whether the SDK should be initialized in offline mode. [More about offline mode](#online--offline-mode).                                                                                                                                                                                   |
| `hooks`                | `Hooks`                   | Optional, used to subscribe events that the SDK sends in specific scenarios. [More about hooks](#hooks).                                                                                                                                                                                                                            |

caution

We strongly recommend you to use the `ConfigCatClient` as a Singleton object in your application. The `ConfigCatClient.get(sdkKey: <sdkKey>)` static factory method constructs singleton client instances for your SDK keys. These clients can be closed all at once with the `ConfigCatClient.closeAll()` method or individually with `client.close()`.

## Anatomy of `getValue()`[​](#anatomy-of-getvalue "Direct link to anatomy-of-getvalue")

| Parameters     | Description                                                                                                                                             |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `key`          | **REQUIRED.** Setting-specific key. Set on *ConfigCat Dashboard* for each setting.                                                                      |
| `defaultValue` | **REQUIRED.** This value will be returned in case of an error.                                                                                          |
| `user`         | Optional, *User Object*. Essential when using Targeting. [Read more about Targeting.](https://configcat.com/docs/docs/targeting/targeting-overview/.md) |
| `completion`   | **REQUIRED.** Callback function to call, when the result is ready.                                                                                      |

* Swift
* Objective-C

```
client.getValue(
    for: "keyOfMySetting", // Setting Key
    defaultValue: false, // Default value
    user: ConfigCatUser(identifier: "#UNIQUE-USER-IDENTIFIER#") // Optional User Object
) { isMyAwesomeFeatureEnabled in
    if isMyAwesomeFeatureEnabled {
        doTheNewThing()
    } else {
        doTheOldThing()
    }
}

// Or with async/await
let isMyAwesomeFeatureEnabled = await client.getValue(
    for: "keyOfMySetting", // Setting Key
    defaultValue: false, // Default value
    user: ConfigCatUser(identifier: "#UNIQUE-USER-IDENTIFIER#") // Optional User Object

if isMyAwesomeFeatureEnabled {
    doTheNewThing()
} else {
    doTheOldThing()
}
```

```
ConfigCatUser* user = [[ConfigCatUser alloc]initWithIdentifier:@"#UNIQUE-USER-IDENTIFIER#"
                                                         email:NULL country:NULL custom:NULL];

[client getBoolValueFor:@"keyOfMySetting" // Setting Key
           defaultValue:false // Default value
                   user:user // Optional User Object
             completion:^(BOOL isMyAwesomeFeatureEnabled) {
    if (isMyAwesomeFeatureEnabled) {
        // do the new thing
    } else {
        // do the old thing
    }
}];
```

caution

*The following is only related to the SDK's generic-typed API which's only accessible from Swift.*

It is important to provide an argument for the `defaultValue` parameter, specifically for the `Value` generic type parameter, that matches the type of the feature flag or setting you are evaluating. Please refer to the following table for the corresponding types.

### Setting type mapping[​](#setting-type-mapping "Direct link to Setting type mapping")

| Setting Kind   | Type parameter `Value` |
| -------------- | ---------------------- |
| On/Off Toggle  | `Bool` / `Bool?`       |
| Text           | `String` / `String?`   |
| Whole Number   | `Int` / `Int?`         |
| Decimal Number | `Double` / `Double?`   |

In addition to the types mentioned above, you also have the option to provide `Any` or `Any?` for the type parameter (or to use the `getAnyValue` method) regardless of the setting kind.

If you provide any other type for the type parameter, or if you specify an allowed type but it mismatches the setting kind, an error message will be logged and `defaultValue` will be returned.

When relying on type inference, be mindful of potential type mismatch issues, especially with number types. For example, `await client.getValue(for: "keyOfMyDecimalSetting", defaultValue: 0)` will return `defaultValue` (`0`) instead of the actual value of the decimal setting because the compiler infers the type as `Int` instead of `Double`.

To correctly evaluate a decimal setting, you should use:

```
let value = await client.getValue(for: "keyOfMyDecimalSetting", defaultValue: 0.0);
```

## Anatomy of `getValueDetails()`[​](#anatomy-of-getvaluedetails "Direct link to anatomy-of-getvaluedetails")

`getValueDetails()` is similar to `getValue()` but instead of returning the evaluated value only, it gives more detailed information about the evaluation result.

| Parameters     | Description                                                                                                                                             |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `key`          | **REQUIRED.** Setting-specific key. Set on *ConfigCat Dashboard* for each setting.                                                                      |
| `defaultValue` | **REQUIRED.** This value will be returned in case of an error.                                                                                          |
| `user`         | Optional, *User Object*. Essential when using Targeting. [Read more about Targeting.](https://configcat.com/docs/docs/targeting/targeting-overview/.md) |

* Swift
* Objective-C

```
client.getValueDetails(
    for: "keyOfMySetting", // Setting Key
    defaultValue: false, // Default value
    user: ConfigCatUser(identifier: "#UNIQUE-USER-IDENTIFIER#") // Optional User Object
) { details in
    // Use the details result
}

// Or with async/await
let details = await client.getValueDetails(
    for: "keyOfMySetting", // Setting Key
    defaultValue: false, // Default value
    user: ConfigCatUser(identifier: "#UNIQUE-USER-IDENTIFIER#") // Optional User Object
```

```
ConfigCatUser* user = [[ConfigCatUser alloc]initWithIdentifier:@"#UNIQUE-USER-IDENTIFIER#"
                                                         email:NULL country:NULL custom:NULL];

[client getBoolValueDetailsFor:@"keyOfMySetting" // Setting Key
                  defaultValue:false // Default value
                          user:user // Optional User Object
                    completion:^(BoolEvaluationDetails* details) {
    // Use the details result
}];
```

caution

*The following is only related to the SDK's generic-typed API which's only accessible from Swift.*

It is important to provide an argument for the `defaultValue` parameter, specifically for the `Value` generic type parameter, that matches the type of the feature flag or setting you are evaluating. Please refer to [this table](#setting-type-mapping) for the corresponding types.

The details result contains the following information:

| Field                     | Type                                 | Description                                                                                                |
| ------------------------- | ------------------------------------ | ---------------------------------------------------------------------------------------------------------- |
| `value`                   | `Bool` / `String` / `Int` / `Double` | The evaluated value of the feature flag or setting.                                                        |
| `key`                     | `String`                             | The key of the evaluated feature flag or setting.                                                          |
| `isDefaultValue`          | `Bool`                               | True when the default value passed to `getValueDetails()` is returned due to an error.                     |
| `error`                   | `String?`                            | In case of an error, this property contains the error message.                                             |
| `user`                    | `ConfigCatUser?`                     | The User Object that was used for evaluation.                                                              |
| `matchedPercentageOption` | `PercentageOption?`                  | The Percentage Option (if any) that was used to select the evaluated value.                                |
| `matchedTargetingRule`    | `TargetingRule?`                     | The Targeting Rule (if any) that matched during the evaluation and was used to return the evaluated value. |
| `fetchTime`               | `Date`                               | The last download time of the current config.                                                              |

## User Object[​](#user-object "Direct link to User Object")

The [User Object](https://configcat.com/docs/docs/targeting/user-object/.md) is essential if you'd like to use ConfigCat's [Targeting](https://configcat.com/docs/docs/targeting/targeting-overview/.md) feature.

* Swift
* Objective-C

```
let user = ConfigCatUser(identifier: "#UNIQUE-USER-IDENTIFIER#")
```

```
ConfigCatUser* user = [[ConfigCatUser alloc]initWithIdentifier:@"#UNIQUE-USER-IDENTIFIER#"
                                                         email:NULL
                                                       country:NULL
                                                        custom:NULL];
```

* Swift
* Objective-C

```
let user = ConfigCatUser(identifier: "john@example.com")
```

```
ConfigCatUser* user = [[ConfigCatUser alloc]initWithIdentifier:@"john@example.com"
                                                         email:NULL
                                                       country:NULL
                                                        custom:NULL];
```

| Arguments    | Description                                                                                                                     |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------- |
| `identifier` | **REQUIRED.** Unique identifier of a user in your application. Can be any value, even an email address.                         |
| `email`      | Optional parameter for easier Targeting Rule definitions.                                                                       |
| `country`    | Optional parameter for easier Targeting Rule definitions.                                                                       |
| `custom`     | Optional dictionary for custom attributes of a user for advanced Targeting Rule definitions. e.g. User role, Subscription type. |

* Swift
* Objective-C

```
let user = ConfigCatUser(identifier: "#UNIQUE-USER-IDENTIFIER#",
    email: "john@example.com",
    country: "United Kingdom",
    custom: ["SubscriptionType":"Pro", "UserRole":"Admin"])
```

```
ConfigCatUser* user = [[ConfigCatUser alloc]initWithIdentifier:@"#UNIQUE-USER-IDENTIFIER#"
                                                         email:@"john@example.com"
                                                       country:@"United Kingdom"
                                                        custom:@{@"SubscriptionType": @"Pro", @"UserRole": @"Admin"}];
```

The `custom` map also allows attribute values other than `String` values:

* Swift
* Objective-C

```
let dateFormatter = DateFormatter()
dateFormatter.dateFormat = "yyyy-MM-dd'T'HH:mm:ss.SSSZ"
let registeredAt = dateFormatter.date(from:"2023-03-31T23:59:59.999Z")!

let user = ConfigCatUser(identifier: "#UNIQUE-USER-IDENTIFIER#",
    email: "john@example.com",
    country: "United Kingdom",
    custom: ["Rating":4.5, "RegisteredAt":registeredAt, "Roles": ["Role1", "Role2"]])
```

```
NSDateFormatter *dateFormatter = [[NSDateFormatter alloc] init];
[dateFormatter setDateFormat:@"yyyy-MM-dd'T'HH:mm:ss.SSSZ"];
NSDate *registeredAt = [dateFormatter dateFromString: @"2023-03-31T23:59:59.999Z"];

ConfigCatUser* user = [[ConfigCatUser alloc]initWithIdentifier:@"#UNIQUE-USER-IDENTIFIER#"
                                                         email:@"john@example.com"
                                                       country:@"United Kingdom"
                                                        custom:@{@"Rating": @4.5, 
                                                                 @"RegisteredAt": registeredAt,
                                                                 @"Roles":@[@"Role1", @"Role2"]}];
```

### User Object Attribute Types[​](#user-object-attribute-types "Direct link to User Object Attribute Types")

All comparators support `String` values as User Object attribute (in some cases they need to be provided in a specific format though, see below), but some of them also support other types of values. It depends on the comparator how the values will be handled. The following rules apply:

**Text-based comparators** (EQUALS, IS ONE OF, etc.)

* accept `String` values,
* all other values are automatically converted to `String` (a warning will be logged but evaluation will continue as normal).

**SemVer-based comparators** (IS ONE OF, <, >=, etc.)

* accept `String` values containing a properly formatted, valid semver value,
* all other values are considered invalid (a warning will be logged and the currently evaluated targeting rule will be skipped).

**Number-based comparators** (=, <, >=, etc.)

* accept `Int`, `UInt`, `Double`, or `Float` values,
* accept `String` values containing a properly formatted, valid `Double` value,
* all other values are considered invalid (a warning will be logged and the currently evaluated targeting rule will be skipped).

**Date time-based comparators** (BEFORE / AFTER)

* accept `Date` values, which are automatically converted to a second-based Unix timestamp,
* accept `Int`, `UInt`, `Double`, or `Float` values representing a second-based Unix timestamp,
* accept `String` values containing a properly formatted, valid `Double` value,
* all other values are considered invalid (a warning will be logged and the currently evaluated targeting rule will be skipped).

**String array-based comparators** (ARRAY CONTAINS ANY OF / ARRAY NOT CONTAINS ANY OF)

* accept arrays of `String`,
* accept `String` values containing a valid JSON string which can be deserialized to an array of `String`,
* all other values are considered invalid (a warning will be logged and the currently evaluated targeting rule will be skipped).

### Default user[​](#default-user "Direct link to Default user")

There's an option to set a default User Object that will be used at feature flag and setting evaluation. It can be useful when your application has a single user only, or rarely switches users.

You can set the default User Object either on SDK initialization:

* Swift
* Objective-C

```
let client = ConfigCatClient.get(sdkKey: "#YOUR-SDK-KEY#") { options in
    options.defaultUser = ConfigCatUser(identifier: "john@example.com")
}
```

```
ConfigCatClient* client = [ConfigCatClient getWithSdkKey:@"#YOUR-SDK-KEY#"
                                            configurator:^(ConfigCatOptions* options) {

    options.defaultUser = [[ConfigCatUser alloc]initWithIdentifier:@"john@example.com"
                                                             email:NULL
                                                           country:NULL
                                                            custom:NULL];
}];
```

or with the `setDefaultUser()` method of the ConfigCat client.

* Swift
* Objective-C

```
client.setDefaultUser(user: ConfigCatUser(identifier: "john@example.com"))
```

```
[client setDefaultUserWithUser:[[ConfigCatUser alloc]initWithIdentifier:@"john@example.com"
                                                                  email:NULL
                                                                country:NULL
                                                                 custom:NULL]];
```

Whenever the `getValue()`, `getValueDetails()`, `getAllValues()`, or `getAllVariationIds()` methods are called without an explicit `user` parameter, the SDK will automatically use the default user as a User Object.

* Swift
* Objective-C

```
let user = ConfigCatUser(identifier: "john@example.com")
client.setDefaultUser(user)

// The default user will be used at the evaluation process.
let value = await client.getValue(for: "keyOfMySetting", defaultValue: false)
```

```
ConfigCatUser* user = [[ConfigCatUser alloc]initWithIdentifier:@"john@example.com"
                                                         email:NULL
                                                       country:NULL
                                                        custom:NULL];

[client setDefaultUserWithUser:user];

// The default user will be used at the evaluation process.
[client getBoolValueFor:@"keyOfMySetting"
           defaultValue:false 
                   user:NULL 
             completion:^(BOOL value) {
    // You can use the evaluation's result here.
}];
```

When the `user` parameter is specified on the requesting method, it takes precedence over the default user.

* Swift
* Objective-C

```
et user = ConfigCatUser(identifier: "john@example.com")
client.setDefaultUser(user)

let otherUser = ConfigCatUser(identifier: "brian@example.com")

// otherUser will be used at the evaluation process.
let value = await client.getValue(for: 'keyOfMySetting', defaultValue: false, user: otherUser)
```

```
ConfigCatUser* user = [[ConfigCatUser alloc]initWithIdentifier:@"john@example.com"
                                                         email:NULL
                                                       country:NULL
                                                        custom:NULL];

[client setDefaultUserWithUser:user];

ConfigCatUser* otherUser = [[ConfigCatUser alloc]initWithIdentifier:@"brian@example.com"
                                                              email:NULL
                                                            country:NULL
                                                             custom:NULL];

// otherUser will be used at the evaluation process.
[client getBoolValueFor:@"keyOfMySetting"
           defaultValue:false 
                   user:otherUser 
             completion:^(BOOL value) {
    // You can use the evaluation's result here.
}];
```

For deleting the default user, you can do the following:

* Swift
* Objective-C

```
client.clearDefaultUser()
```

```
[client clearDefaultUser];
```

## `getAllKeys()`[​](#getallkeys "Direct link to getallkeys")

You can get the keys for all available feature flags and settings by calling the `getAllKeys()` method of the `ConfigCatClient`.

* Swift
* Objective-C

```
let client = ConfigCatClient.get(sdkKey: "#YOUR-SDK-KEY#")

// Completion callback
client.getAllKeys() { keys in
    // use keys
}

// Async/await
let keys = await client.getAllKeys()
```

```
ConfigCatClient* client = [ConfigCatClient getWithSdkKey:@"#YOUR-SDK-KEY#" options:NULL];

[client getAllKeysWithCompletion:^(NSArray<NSString*>* keys) {
    // use keys
}];
```

## `getAllValues()`[​](#getallvalues "Direct link to getallvalues")

Evaluates and returns the values of all feature flags and settings. Passing a [User Object](#user-object) is optional.

| Parameters | Description                                                                                                                                             |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `user`     | Optional, *User Object*. Essential when using Targeting. [Read more about Targeting.](https://configcat.com/docs/docs/targeting/targeting-overview/.md) |

* Swift
* Objective-C

```
let client = ConfigCatClient.get(sdkKey: "#YOUR-SDK-KEY#")
let user = ConfigCatUser(identifier: "#UNIQUE-USER-IDENTIFIER#")

// Completion callback
client.getAllValues(
    user:  user// Optional User Object
) { allValues in
    // use allValues
}

// Async/await
let allValues = await client.getAllValues(
    user: user // Optional User Object
)
```

```
ConfigCatClient* client = [ConfigCatClient getWithSdkKey:@"#YOUR-SDK-KEY#" options:NULL];

ConfigCatUser* user = [[ConfigCatUser alloc]initWithIdentifier:@"#UNIQUE-USER-IDENTIFIER#"
                                                         email:NULL
                                                       country:NULL
                                                        custom:NULL];

[client getAllValuesWithUser:user completion:^(NSDictionary<NSString*,id>* values) {
    // use values
}];
```

## Polling Modes[​](#polling-modes "Direct link to Polling Modes")

The *ConfigCat SDK* supports 3 different polling strategies to fetch feature flags and settings from the ConfigCat CDN. Once the latest data is downloaded, it is stored in the cache, then calls to `getValue()` use the cached data to evaluate feature flags and settings. With the following polling modes, you can customize the SDK to best fit to your application's lifecycle.<br />[More about polling modes.](https://configcat.com/docs/docs/advanced/caching/.md)

### Auto polling (default)[​](#auto-polling-default "Direct link to Auto polling (default)")

The *ConfigCat SDK* downloads the latest config data from the ConfigCat CDN automatically every 60 seconds and stores it in the cache.

Use the the `autoPollIntervalInSeconds` option parameter of the `PollingModes.autoPoll()` to change the polling interval.

* Swift
* Objective-C

```
let client = ConfigCatClient.get(sdkKey: "#YOUR-SDK-KEY#") { options in
    options.pollingMode = PollingModes.autoPoll(autoPollIntervalInSeconds: 120 /* polling interval in seconds */)
}
```

```
ConfigCatClient* client = [ConfigCatClient getWithSdkKey:@"#YOUR-SDK-KEY#"
                                            configurator:^(ConfigCatOptions* options) {

    options.pollingMode = [PollingModes autoPollWithAutoPollIntervalInSeconds:120 maxInitWaitTimeInSeconds:5];
}];
```

Available options:

| Option Parameter            | Description                                                                                          | Default |
| --------------------------- | ---------------------------------------------------------------------------------------------------- | ------- |
| `autoPollIntervalInSeconds` | Polling interval.                                                                                    | 60      |
| `maxInitWaitTimeInSeconds`  | Maximum waiting time between the client initialization and the first config acquisition in secconds. | 5       |

### Lazy loading[​](#lazy-loading "Direct link to Lazy loading")

When calling `getValue()`, the *ConfigCat SDK* downloads the latest config data from the ConfigCat CDN only if it is not already present in the cache, or if the cache has expired. In this case `getValue()` will return the setting value after the cache is updated.

Use the `cacheRefreshIntervalInSeconds` option parameter of the `PollingModes.lazyLoad()` to set cache lifetime.

* Swift
* Objective-C

```
let client = ConfigCatClient.get(sdkKey: "#YOUR-SDK-KEY#") { options in
    options.pollingMode = PollingModes.lazyLoad(cacheRefreshIntervalInSeconds: 120 /* the cache will expire in 120 seconds */)
}
```

```
ConfigCatClient* client = [ConfigCatClient getWithSdkKey:@"#YOUR-SDK-KEY#"
                                            configurator:^(ConfigCatOptions* options) {

    options.pollingMode = [PollingModes lazyLoadWithCacheRefreshIntervalInSeconds:120];
}];
```

Available options:

| Option Parameter                | Description | Default |
| ------------------------------- | ----------- | ------- |
| `cacheRefreshIntervalInSeconds` | Cache TTL.  | 60      |

### Manual polling[​](#manual-polling "Direct link to Manual polling")

Manual polling gives you full control over when the config data is downloaded from the ConfigCat CDN. The *ConfigCat SDK* will not download it automatically. Calling `refresh()` is your application's responsibility.

* Swift
* Objective-C

```
let client = ConfigCatClient.get(sdkKey: "#YOUR-SDK-KEY#") { options in
    options.pollingMode = PollingModes.manualPoll()
}

// Completion callback
client.forceRefresh() { _ in
    // The client uses the latest config JSON
}

// Async/await
await client.forceRefresh()
```

```
ConfigCatClient* client = [ConfigCatClient getWithSdkKey:@"#YOUR-SDK-KEY#"
                                            configurator:^(ConfigCatOptions* options) {

    options.pollingMode = [PollingModes manualPoll];
}];

[client forceRefreshWithCompletion:^(RefreshResult* result) {
    // The client uses the latest config JSON
}];
```

> `getValue()` returns `defaultValue` if the cache is empty. Call `refresh()` to update the cache.

## Hooks[​](#hooks "Direct link to Hooks")

The SDK provides several hooks (events), by means of which you can get notified of its actions. You can subscribe to the following events emitted by the *ConfigCat* client:

* `onReady(ClientCacheState)`: This event is emitted when the client reaches the ready state, i.e. completes initialization.

  * If Lazy Loading or Manual Polling is used, it's considered ready right after the initial sync with the external cache (if any) completes.

  * If Auto Polling is used, the ready state is reached as soon as

    <!-- -->

    * the initial sync with the external cache yields up-to-date config data,
    * otherwise, if the client is online (i.e. HTTP requests are allowed), the first config fetch operation completes (regardless of success or failure),
    * or the time specified via Auto Polling's `maxInitWaitTimeInSeconds` option has passed.

  Reaching the ready state usually means the client is ready to evaluate feature flags and settings. However, please note that this is not guaranteed. In case of initialization failure or timeout, the internal cache may be empty or expired even after the ready state is reported. You can verify this by checking the `ClientCacheState` argument.

* `onConfigChanged((Config, ConfigCatClientSnapshot))`: This event is emitted first when the client's internal cache gets populated. Afterwards, it is emitted again each time the internally cached config is updated to a newer version, either as a result of synchronization with the external cache, or as a result of fetching a newer version from the ConfigCat CDN.

* `onFlagEvaluated(EvaluationDetails)`: This event is emitted each time the client evaluates a feature flag or setting. The event provides the same evaluation details that you would get from [`getValueDetails()`](#anatomy-of-getvaluedetails).

* `onError(String)`: This event is emitted when an error occurs within the client.

You can subscribe to these events either on SDK initialization:

* Swift
* Objective-C

```
let client = ConfigCatClient.get(sdkKey: "#YOUR-SDK-KEY#") { options in
    options.hooks.addOnFlagEvaluated { details in
        /* handle the event */
    }
}
```

```
ConfigCatClient* client = [ConfigCatClient getWithSdkKey:@"#YOUR-SDK-KEY#"
                                            configurator:^(ConfigCatOptions* options) {

    [options.hooks addOnFlagEvaluatedWithHandler:^(EvaluationDetails* details) {
        /* handle the event */
    }];
}];
```

or with the `hooks` property of the ConfigCat client:

* Swift
* Objective-C

```
client.hooks.addOnFlagEvaluated { details in
    /* handle the event */
}
```

```
[client.hooks addOnFlagEvaluatedWithHandler:^(EvaluationDetails* details) {
    /* handle the event */
}];
```

## Snapshots and non-blocking synchronous feature flag evaluation[​](#snapshots-and-non-blocking-synchronous-feature-flag-evaluation "Direct link to Snapshots and non-blocking synchronous feature flag evaluation")

The *ConfigCat* client doesn't directly provide synchronous methods for evaluating feature flags and settings because such synchronous methods could block the executing thread for longer periods of time (e.g. when downloading config data from the ConfigCat CDN servers), which could lead to an unresponsive application.

However, there can be circumstances where synchronous evaluation is preferable, thus, since `v10.0.0`, the Swift SDK provides a way to synchronously evaluate feature flags and settings as a non-blocking operation, via *snapshots*.

* Swift
* Objective-C

Using the `snapshot()` method, you can capture the current state of the *ConfigCat* client (including the latest downloaded config data) and use the resulting snapshot object to synchronously evaluate feature flags and settings based on the captured state:

```
let client = ConfigCatClient.get(sdkKey: "#YOUR-SDK-KEY#") { options in
    options.pollingMode = PollingModes.autoPoll()
}

// Wait for the client to initialize.
await client.waitForReady()

let snapshot = client.snapshot()

let user = ConfigCatUser(identifier: "#UNIQUE-USER-IDENTIFIER#")
for key in snapshot.getAllKeys() {
    let value: Any? = snapshot.getValue(for: key, defaultValue: nil, user: user)
    print("\(key): \(String(describing: value))")
}
```

Subscribing to the `onReady` hook gives you a snapshot of the captured initialized state of the *ConfigCat* client (including the latest downloaded config data) that you can use to synchronously evaluate feature flags and settings:

```
ConfigCatClient* client = [ConfigCatClient getWithSdkKey:@"#YOUR-SDK-KEY#" configurator:^(ConfigCatOptions* options) {
    [options.hooks addOnReadyWithSnapshotHandler:^(ConfigCatClientSnapshot* snapshot) {
        ConfigCatUser* user = [[ConfigCatUser alloc]initWithIdentifier:@"#UNIQUE-USER-IDENTIFIER#"
                                                                 email:NULL
                                                               country:NULL
                                                                custom:NULL];
                
        for (NSString* key in [snapshot getAllKeys]) {
            id def = NULL;
            id value = [snapshot getAnyValueFor:key defaultValue:def user:user];
            NSLog(@"%@: %@", key, value);
        }
    }];
}];
```

Creating a snapshot is a cheap operation. This is possible because snapshots capture the client's internal (in-memory) cache. No attempt is made to refresh the internal cache, even if it's empty or expired.

caution

Please note that creating and using a snapshot

* won't trigger a sync with the external cache when working with [shared caching](https://configcat.com/docs/docs/advanced/caching/.md#shared-cache),
* won't fetch the latest config data from the ConfigCat CDN when the internally cached config data is empty or expired.

For the above reasons, it's recommended to use snapshots in conjunction with the Auto Polling mode, where the SDK automatically updates the internal cache in the background. (For other polling modes, you'll need to manually initiate a cache refresh by calling `forceRefresh`.)

Because of this behavior, it's important to make sure that the client has completed initialization and populated its internal cache before creating snapshots. Otherwise the snapshot's evaluation methods won't have the data to do actual evaluation, but will just return the default value you pass to them. Which behavior is usually not what you want in your application.

In Auto Polling mode, you can use the `waitForReady` method to wait for the latest config data to become available locally. This is an asynchronous operation, which completes as soon as the client reaches the ready state, i.e. completes initialization (or the time specified via the `maxInitWaitTimeInSeconds` option passes).

(Please note that this doesn't apply to other polling modes. In those cases, the client doesn't contact the ConfigCat CDN during initialization, so the ready state is reached as soon as the first sync with the external cache completes.)

Typically, you call `waitForReady` and wait for its completion only once, in the initialization phase of your application. (In Objective-C, `waitForReady` is not available. As an alternative, you can subscribe to the `onReady` hook and wait for the first event.)

caution

Reaching the ready state usually means the client is ready to evaluate feature flags and settings. However, please note that this is not guaranteed. In case of initialization failure or timeout, the internal cache may be empty or expired even after the ready state is reported. You can verify this by checking the return value.

* Swift
* Objective-C

```
let clientCacheState = await client.waitForReady()
if (clientCacheState == .noFlagData) {
    // Handle initialization failure (see below).
}
```

```
ConfigCatClient* client = [ConfigCatClient getWithSdkKey:@"#YOUR-SDK-KEY#" configurator:^(ConfigCatOptions* options) {
    [options.hooks addOnReadyWithSnapshotHandler:^(ConfigCatClientSnapshot* snapshot) {
        if ([snapshot cacheState] == ClientCacheStateNoFlagData) {
            // Handle initialization failure (see below).        
        }
    }];
}];
```

You have the following options to handle unsuccessful initialization:

* If it's acceptable for your application to start up and use the default values passed to the evaluation methods, you may log some warning (or skip the check altogether as the client will log warnings anyway), and let the application continue.
* Otherwise, you need to either terminate the application or continue waiting. The latter is an option because the client might be able to obtain the config data later, in the case of a transient problem like some temporary network issue. However, the *ConfigCat SDK* doesn't provide out-of-the-box support for this case currently. You can implement this logic by subscribing to the `onConfigChanged` hook and waiting for the first event.

## Online / Offline mode[​](#online--offline-mode "Direct link to Online / Offline mode")

In cases when you'd want to prevent the SDK from making HTTP calls, you can put it in offline mode:

* Swift
* Objective-C

```
client.setOffline()
```

```
[client setOffline];
```

In offline mode, the SDK won't initiate HTTP requests and will work only from its cache.

To put the SDK back in online mode, you can do the following:

* Swift
* Objective-C

```
client.setOnline()
```

```
[client setOnline];
```

> With `client.isOffline` you can check whether the SDK is in offline mode.

## Flag Overrides[​](#flag-overrides "Direct link to Flag Overrides")

With flag overrides you can overwrite the feature flags & settings downloaded from the ConfigCat CDN with local values. Moreover, you can specify how the overrides should apply over the downloaded values. The following 3 behaviours are supported:

* **Local only** (`OverrideBehaviour.localOnly`): When evaluating values, the SDK will not use feature flags & settings from the ConfigCat CDN, but it will use all feature flags & settings that are loaded from local-override sources.

* **Local over remote** (`OverrideBehaviour.localOverRemote`): When evaluating values, the SDK will use all feature flags & settings that are downloaded from the ConfigCat CDN, plus all feature flags & settings that are loaded from local-override sources. If a feature flag or a setting is defined both in the downloaded and the local-override source then the local-override version will take precedence.

* **Remote over local** (`OverrideBehaviour.remoteOverLocal`): When evaluating values, the SDK will use all feature flags & settings that are downloaded from the ConfigCat CDN, plus all feature flags & settings that are loaded from local-override sources. If a feature flag or a setting is defined both in the downloaded and the local-override source then the downloaded version will take precedence.

You can set up the SDK to load your feature flag & setting overrides from a `[String: Any]` dictionary.

* Swift
* Objective-C

```
let dictionary:[String: Any] = [
    "enabledFeature": true,
    "disabledFeature": false,
    "intSetting": 5,
    "doubleSetting": 3.14,
    "stringSetting": "test"
]

let client = ConfigCatClient.get(sdkKey: "#YOUR-SDK-KEY#") { options in
    options.flagOverrides = LocalDictionaryDataSource(source: dictionary, behaviour: .localOnly)
}
```

```
NSDictionary<NSString*,id>* dictionary = @{
    @"enabledFeature": @true,
    @"disabledFeature": @false,
    @"intSetting": @5,
    @"doubleSetting": @3.14,
    @"stringSetting": @"test"
};

ConfigCatClient* client = [ConfigCatClient getWithSdkKey:@"#YOUR-SDK-KEY#"
                                            configurator:^(ConfigCatOptions* options) {

    options.flagOverrides = [[LocalDictionaryDataSource alloc]initWithSource:dictionary
                                                                   behaviour:OverrideBehaviourLocalOnly];
}];
```

## Cache[​](#cache "Direct link to Cache")

The SDK uses `UserDefaults` as the default cache to store the downloaded `config JSON`.

If you want to turn off the default behavior, you can set the SDK's cache to `nil` or to your own cache implementation.

* Swift
* Objective-C

```
let client = ConfigCatClient.get(sdkKey: "#YOUR-SDK-KEY#") { options in
    options.configCache = nil
}
```

```
ConfigCatClient* client = [ConfigCatClient getWithSdkKey:@"#YOUR-SDK-KEY#"
                                            configurator:^(ConfigCatOptions* options) {

    options.configCache = NULL;
}];
```

### Custom cache[​](#custom-cache "Direct link to Custom cache")

You have the option to inject your custom cache implementation into the client. All you have to do is to conform the `ConfigCache` protocol:

* Swift
* Objective-C

```
@import ConfigCat

public class MyCustomCache: ConfigCache {
    public func read(key: String) throws -> String {
        // here you have to return with the cached value
    }

    public func write(key: String, value: String) throws {
        // here you have to store the new value in the cache
    }
}
```

MyCustomCache.h

```
@import Foundation;
@import ConfigCat;

@interface MyCustomCache: NSObject <ConfigCache>

@end
```

MyCustomCache.m

```
#import "MyCustomCache.h"

@implementation MyCustomCache

- (NSString *)readFor:(NSString *)key error:(NSError * __autoreleasing *)error {
    // here you have to return with the cached value
}

- (BOOL)writeFor:(NSString *)key value:(NSString *)value error:(NSError * __autoreleasing *)error {
    // here you have to store the new value in the cache
}

@end
```

Then you can use your custom cache implementation at the SDK's initialization:

* Swift
* Objective-C

```
let client = ConfigCatClient.get(sdkKey: "#YOUR-SDK-KEY#") { options in
    options.configCache = MyCustomCache()
}
```

```
ConfigCatClient* client = [ConfigCatClient getWithSdkKey:@"#YOUR-SDK-KEY#"
                                            configurator:^(ConfigCatOptions* options) {

    options.configCache = [MyCustomCache alloc];
}];
```

info

The Swift SDK supports *shared caching*. You can read more about this feature and the required minimum SDK versions [here](https://configcat.com/docs/docs/advanced/caching/.md#shared-cache).

## Force refresh[​](#force-refresh "Direct link to Force refresh")

Call the `forceRefresh()` method on the client to download the latest config JSON and update the cache.

## Using ConfigCat behind a proxy[​](#using-configcat-behind-a-proxy "Direct link to Using ConfigCat behind a proxy")

Provide your own network credentials (username/password), and proxy server settings (proxy server/port) by adding a *ProxyDictionary* to the ConfigCat's `URLSessionConfiguration`.

* Swift
* Objective-C

```
let proxyHost = "127.0.0.1"
let proxyPort = 8080
let proxyUser = "user"
let proxyPassword = "password"

let sessionConfiguration = URLSessionConfiguration.default
sessionConfiguration.connectionProxyDictionary = [
    kCFNetworkProxiesHTTPEnable: true,
    kCFNetworkProxiesHTTPProxy: proxyHost,
    kCFNetworkProxiesHTTPPort: proxyPort,
    kCFNetworkProxiesHTTPSEnable: true,
    kCFNetworkProxiesHTTPSProxy: proxyHost,
    kCFNetworkProxiesHTTPSPort: proxyPort,
    kCFProxyUsernameKey: proxyUser, // Optional
    kCFProxyPasswordKey: proxyPassword // Optional
]

let client = ConfigCatClient.get(sdkKey: "#YOUR-SDK-KEY#") { options in
    options.sessionConfiguration = sessionConfiguration
}
```

```
NSString* proxyHost = @"127.0.0.1";
NSNumber* proxyPort = @8080;
NSString* proxyUser = @"user";
NSString* proxyPassword = @"password";

NSURLSessionConfiguration* sessionConfiguration = [NSURLSessionConfiguration defaultSessionConfiguration];
sessionConfiguration.connectionProxyDictionary = @{
    (NSString *)kCFNetworkProxiesHTTPEnable: @true,
    (NSString *)kCFNetworkProxiesHTTPProxy: proxyHost,
    (NSString *)kCFNetworkProxiesHTTPPort: proxyPort,
    (NSString *)kCFNetworkProxiesHTTPSEnable: @true,
    (NSString *)kCFNetworkProxiesHTTPSProxy: proxyHost,
    (NSString *)kCFNetworkProxiesHTTPSPort: proxyPort,
    (NSString *)kCFProxyUsernameKey: proxyUser, // Optional
    (NSString *)kCFProxyPasswordKey: proxyPassword // Optional
};

ConfigCatClient* client = [ConfigCatClient getWithSdkKey:@"#YOUR-SDK-KEY#"
                                            configurator:^(ConfigCatOptions* options) {

    options.sessionConfiguration = sessionConfiguration;
}];
```

## Changing the default HTTP timeout[​](#changing-the-default-http-timeout "Direct link to Changing the default HTTP timeout")

Set the maximum wait time for a ConfigCat HTTP response by changing the *timeoutIntervalForRequest* of the ConfigCat's `URLSessionConfiguration`. The default *timeoutIntervalForRequest* is 60 seconds.

* Swift
* Objective-C

```
let sessionConfiguration = URLSessionConfiguration.default
sessionConfiguration.timeoutIntervalForRequest = 10 // Timeout in seconds

let client = ConfigCatClient.get(sdkKey: "#YOUR-SDK-KEY#") { options in
    options.sessionConfiguration = sessionConfiguration
}
```

```
NSURLSessionConfiguration* sessionConfiguration = [NSURLSessionConfiguration defaultSessionConfiguration];
sessionConfiguration.timeoutIntervalForRequest = 10; // Timeout in seconds

ConfigCatClient* client = [ConfigCatClient getWithSdkKey:@"#YOUR-SDK-KEY#"
                                            configurator:^(ConfigCatOptions* options) {

    options.sessionConfiguration = sessionConfiguration;
}];
```

## Logging[​](#logging "Direct link to Logging")

The default logger used by the SDK is using the *Unified Logging System*. For more information about *Unified Logging* please visit [Apple's developer page](https://developer.apple.com/documentation/os/logging) or check [Session 721 - Unified Logging and Activity Tracing](https://developer.apple.com/videos/play/wwdc2016/721) from WWDC 2016.

You can override the default logger with your custom implementation via the `logger` client option. The custom implementation must conform the `ConfigCatLogger` protocol.

* Swift
* Objective-C

```
@import ConfigCat

class MyCustomLogger: ConfigCatLogger {
    func debug(message: String) {
        // write the debug logs
    }
    
    func info(message: String) {
        // write the info logs
    }
    
    func warning(message: String) {
        // write the warning logs
    }
    
    func error(message: String) {
        // write the error logs
    }
}
```

MyCustomLogger.h

```
@import Foundation;
@import ConfigCat;

@interface MyCustomLogger: NSObject <ConfigCatLogger>

@end
```

MyCustomLogger.m

```
#import "MyCustomLogger.h"

@implementation MyCustomLogger

- (void)debugWithMessage:(NSString * _Nonnull)message { 
    // write the debug logs
}

- (void)infoWithMessage:(NSString * _Nonnull)message { 
    // write the info logs
}

- (void)warningWithMessage:(NSString * _Nonnull)message { 
    // write the warning logs
}

- (void)errorWithMessage:(NSString * _Nonnull)message { 
    // write the error logs
}

@end
```

Then you can use your custom logger implementation at the SDK's initialization:

* Swift
* Objective-C

```
let client = ConfigCatClient.get(sdkKey: "#YOUR-SDK-KEY#") { options in
    options.logger = MyCustomLogger()
}
```

```
ConfigCatClient* client = [ConfigCatClient getWithSdkKey:@"#YOUR-SDK-KEY#"
                                            configurator:^(ConfigCatOptions* options) {

    options.logger = [MyCustomLogger alloc];
}];
```

### Log level[​](#log-level "Direct link to Log level")

You can change the verbosity of the logs by setting the `logLevel` option.

* Swift
* Objective-C

```
let client = ConfigCatClient.get(sdkKey: "#YOUR-SDK-KEY#") { options in
    options.logLevel = .info
}
```

```
ConfigCatClient* client = [ConfigCatClient getWithSdkKey:@"#YOUR-SDK-KEY#"
                                            configurator:^(ConfigCatOptions* options) {

    options.logLevel = ConfigCatLogLevelInfo;
}];
```

Available log levels:

* Swift
* Objective-C

| Level      | Description                                                                             |
| ---------- | --------------------------------------------------------------------------------------- |
| `.nolog`   | Turn the ConfigCat logging off.                                                         |
| `.error`   | Only error level events are logged.                                                     |
| `.warning` | Default. Errors and Warnings are logged.                                                |
| `.info`    | Errors, Warnings and feature flag evaluation is logged.                                 |
| `.debug`   | All of the above plus debug info is logged. Debug logs can be different for other SDKs. |

| Level                      | Description                                                                             |
| -------------------------- | --------------------------------------------------------------------------------------- |
| `ConfigCatLogLevelNolog`   | Turn the ConfigCat logging off.                                                         |
| `ConfigCatLogLevelError`   | Only error level events are logged.                                                     |
| `ConfigCatLogLevelWarning` | Default. Errors and Warnings are logged.                                                |
| `ConfigCatLogLevelInfo`    | Errors, Warnings and feature flag evaluation is logged.                                 |
| `ConfigCatLogLevelDebug`   | All of the above plus debug info is logged. Debug logs can be different for other SDKs. |

Info level logging helps to inspect the feature flag evaluation process.<br /><!-- -->Example log entries:

```
[5000] Evaluating 'isPOCFeatureEnabled' for User '{"Identifier":"<SOME USERID>","version":"1.0.0","Email":"configcat@example.com","Country":"CountryID"}'
  Evaluating targeting rules and applying the first match if any:
  - IF User.Email CONTAINS ANY OF ['@something.com'] THEN 'false' => no match
  - IF User.Email CONTAINS ANY OF ['@example.com'] THEN 'true' => MATCH, applying rule
  Returning 'true'.
```

## Sensitive information handling[​](#sensitive-information-handling "Direct link to Sensitive information handling")

The frontend/mobile SDKs are running in your users' browsers/devices. The SDK is downloading a [config JSON](https://configcat.com/docs/docs/requests/.md) file from ConfigCat's CDN servers. The URL path for this config JSON file contains your SDK key, so the SDK key and the content of your config JSON file (feature flag keys, feature flag values, Targeting Rules, % rules) can be visible to your users. In ConfigCat, all SDK keys are read-only. They only allow downloading your config JSON files, but nobody can make any changes with them in your ConfigCat account.

If you do not want to expose the SDK key or the content of the config JSON file, we recommend using the SDK in your backend components only. You can always create a backend endpoint using the ConfigCat SDK that can evaluate feature flags for a specific user, and call that backend endpoint from your frontend/mobile applications.

Also, we recommend using [confidential targeting comparators](https://configcat.com/docs/docs/targeting/targeting-rule/user-condition/.md#confidential-text-comparators) in the Targeting Rules of those feature flags that are used in the frontend/mobile SDKs.

## Sample App[​](#sample-app "Direct link to Sample App")

Check out our Sample Application how they use the ConfigCat SDK

* [iOS with auto polling and change listener](https://github.com/configcat/swift-sdk/tree/master/samples/ios)
