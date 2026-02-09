# Source: https://configcat.com/docs/sdk-reference/openfeature/swift.md

# OpenFeature Provider for Swift

Copy page

[![CI](https://github.com/configcat/openfeature-swift/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/configcat/openfeature-swift/actions/workflows/ci.yml)

[ConfigCat OpenFeature Provider for Swift on GitHub](https://github.com/configcat/openfeature-swift)

## Getting started[​](#getting-started "Direct link to Getting started")

### 1. Install the provider[​](#1-install-the-provider "Direct link to 1. Install the provider")

#### Swift Package Manager[​](#swift-package-manager "Direct link to Swift Package Manager")

If you manage dependencies through SPM, in the dependencies section of Package.swift add:

```swift
.package(url: "https://github.com/configcat/openfeature-swift", from: "0.1.0")

```

and in the target dependencies section add:

```swift
.product(name: "ConfigCat", package: "openfeature-swift"),

```

#### Xcode Dependencies[​](#xcode-dependencies "Direct link to Xcode Dependencies")

* Open the dependencies dialog from `File` > `Add Package Dependencies...`
* Search for `https://github.com/configcat/openfeature-swift` and click `Add Package`.

### 2. Initialize the provider[​](#2-initialize-the-provider "Direct link to 2. Initialize the provider")

The initializer of `ConfigCatProvider` takes the SDK key and an optional `ConfigCatOptions` argument containing the additional configuration options for the [ConfigCat Swift SDK](https://configcat.com/docs/sdk-reference/ios.md#creating-the-configcat-client):

```swift
import ConfigCatOpenFeature
import ConfigCat
import OpenFeature

Task {
    // Configure the provider.
    let provider = ConfigCatProvider(sdkKey: "<YOUR-CONFIGCAT-SDK-KEY>") { opts in
        opts.pollingMode = PollingModes.autoPoll()
    }

    // Configure the OpenFeature API with the ConfigCat provider.
    await OpenFeatureAPI.shared.setProviderAndWait(provider: provider)

    // Create a client.
    let client = OpenFeatureAPI.shared.getClient()
}

```

For more information about all the configuration options, see the [Swift SDK documentation](https://configcat.com/docs/sdk-reference/ios.md#creating-the-configcat-client).

### 3. Evaluate your feature flag[​](#3-evaluate-your-feature-flag "Direct link to 3. Evaluate your feature flag")

```swift
let isAwesomeFeatureEnabled = client.getBooleanValue(key: "isAwesomeFeatureEnabled", defaultValue: false)
if isAwesomeFeatureEnabled {
    doTheNewThing()
} else {
    doTheOldThing()
}

```

## Evaluation Context[​](#evaluation-context "Direct link to Evaluation Context")

An [evaluation context](https://openfeature.dev/docs/reference/concepts/evaluation-context) in the OpenFeature specification is a container for arbitrary contextual data that can be used as a basis for feature flag evaluation. The ConfigCat provider translates these evaluation contexts to ConfigCat [User Objects](https://configcat.com/docs/sdk-reference/ios.md#user-object).

The following table shows how the different context attributes are mapped to User Object attributes.

| Evaluation context | User Object  | Required |
| ------------------ | ------------ | -------- |
| `targetingKey`     | `identifier` | ☑        |
| `Email`            | `email`      |          |
| `Country`          | `country`    |          |
| Any other          | `custom`     |          |

To evaluate feature flags for a context, use the `setEvaluationContext()` method on `OpenFeatureAPI.shared` to set the context for the provider:

```swift
let context = MutableContext(targetingKey: "#SOME-USER-ID#", structure: MutableStructure(attributes: [
    "Email": Value.string("configcat@example.com"),
    "Country": Value.string("CountryID"),
    "Rating": Value.double(4.5),
    "Roles": Value.list([Value.string("Role1"), Value.string("Role2")])
]))
OpenFeatureAPI.shared.setEvaluationContext(evaluationContext: context)

```

## Look under the hood[​](#look-under-the-hood "Direct link to Look under the hood")

* [Sample iOS APP](https://github.com/configcat/openfeature-swift/tree/main/samples/ios)
* [ConfigCat OpenFeature Provider's repository on GitHub](https://github.com/configcat/openfeature-swift)
