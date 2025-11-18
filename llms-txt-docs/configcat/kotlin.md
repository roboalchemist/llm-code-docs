# Source: https://configcat.com/docs/sdk-reference/openfeature/kotlin.md

# OpenFeature Provider for Kotlin

[![CI](https://github.com/configcat/openfeature-kotlin/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/configcat/openfeature-kotlin/actions/workflows/ci.yml) [![Maven Central](https://img.shields.io/maven-central/v/com.configcat/configcat-openfeature-provider?label=maven%20central)](https://central.sonatype.com/artifact/com.configcat/configcat-openfeature-provider)

[ConfigCat OpenFeature Provider for Kotlin on GitHub](https://github.com/configcat/openfeature-kotlin)

## Getting started[​](#getting-started "Direct link to Getting started")

### 1. Install the provider[​](#1-install-the-provider "Direct link to 1. Install the provider")

```
dependencies {
    implementation("com.configcat:configcat-openfeature-provider:$providerVersion")
}
```

### 2. Initialize the provider[​](#2-initialize-the-provider "Direct link to 2. Initialize the provider")

The `ConfigCatProvider` function takes the SDK key and an optional `ConfigCatOptions` argument containing the additional configuration options for the [ConfigCat Kotlin SDK](https://configcat.com/docs/docs/sdk-reference/kotlin/.md#setting-up-the-configcat-client):

```
import com.configcat.*
import dev.openfeature.kotlin.sdk.*

coroutineScope.launch(Dispatchers.IO) {
    // Configure the provider.
    val provider = ConfigCatProvider("<YOUR-CONFIGCAT-SDK-KEY>") {
        pollingMode = autoPoll { pollingInterval = 60.seconds }
    }

    // Configure the OpenFeature API with the ConfigCat provider.
    OpenFeatureAPI.setProviderAndWait(provider)

    // Create a client.
    val client = OpenFeatureAPI.getClient()
}
```

For more information about all the configuration options, see the [Kotlin SDK documentation](https://configcat.com/docs/docs/sdk-reference/kotlin/.md#setting-up-the-configcat-client).

### 3. Evaluate your feature flag[​](#3-evaluate-your-feature-flag "Direct link to 3. Evaluate your feature flag")

```
val isAwesomeFeatureEnabled = client.getBooleanValue("isAwesomeFeatureEnabled", false)
if (isAwesomeFeatureEnabled) {
    doTheNewThing()
} else {
    doTheOldThing()
}
```

## Evaluation Context[​](#evaluation-context "Direct link to Evaluation Context")

An [evaluation context](https://openfeature.dev/docs/reference/concepts/evaluation-context) in the OpenFeature specification is a container for arbitrary contextual data that can be used as a basis for feature flag evaluation. The ConfigCat provider translates these evaluation contexts to ConfigCat [User Objects](https://configcat.com/docs/docs/sdk-reference/kotlin/.md#user-object).

The following table shows how the different context attributes are mapped to User Object attributes.

| Evaluation context | User Object  | Required |
| ------------------ | ------------ | -------- |
| `targetingKey`     | `identifier` | ☑        |
| `Email`            | `email`      |          |
| `Country`          | `country`    |          |
| Any other          | `custom`     |          |

To evaluate feature flags for a context, use the `setEvaluationContext()` method on the `OpenFeatureAPI` to set the context for the provider:

```
val context = ImmutableContext(
    targetingKey = "#SOME-USER-ID#",
    attributes = mapOf(
        "Email" to Value.String("configcat@example.com"),
        "Country" to Value.String("CountryID"),
        "Rating" to Value.Double(4.5),
        "RegisteredAt" to Value.Instant(kotlin.time.Instant.parse("2025-05-30T10:15:30.00Z")),
        "Roles" to Value.List(listOf(Value.String("Role1"), Value.String("Role2")))
    ),
)
OpenFeatureAPI.setEvaluationContext(context)
```

## Look under the hood[​](#look-under-the-hood "Direct link to Look under the hood")

* [Sample Android APP](https://github.com/configcat/openfeature-kotlin/tree/main/samples/android)
* [ConfigCat OpenFeature Provider's repository on GitHub](https://github.com/configcat/openfeature-kotlin)
* [ConfigCat OpenFeature Provider on Maven Central](https://central.sonatype.com/artifact/com.configcat/configcat-openfeature-provider)
