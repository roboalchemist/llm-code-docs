# Source: https://configcat.com/docs/sdk-reference/openfeature/java.md

# Source: https://configcat.com/docs/sdk-reference/java.md

# Source: https://configcat.com/docs/sdk-reference/openfeature/java.md

# Source: https://configcat.com/docs/sdk-reference/java.md

# Source: https://configcat.com/docs/sdk-reference/openfeature/java.md

# Source: https://configcat.com/docs/sdk-reference/java.md

# Source: https://configcat.com/docs/sdk-reference/openfeature/java.md

# Source: https://configcat.com/docs/sdk-reference/java.md

# Source: https://configcat.com/docs/sdk-reference/openfeature/java.md

# Source: https://configcat.com/docs/sdk-reference/java.md

# Source: https://configcat.com/docs/sdk-reference/openfeature/java.md

# OpenFeature Provider for Java

[ConfigCat OpenFeature Provider for Java on GitHub](https://github.com/open-feature/java-sdk-contrib/tree/main/providers/configcat)

## Getting started[​](#getting-started "Direct link to Getting started")

### 1. Install the provider[​](#1-install-the-provider "Direct link to 1. Install the provider")

* Gradle
* Maven

build.gradle

```
dependencies {
    implementation 'dev.openfeature.contrib.providers:configcat:0.1.+'
    implementation 'dev.openfeature:sdk:1.+'
}
```

pom.xml

```
<dependency>
    <groupId>dev.openfeature.contrib.providers</groupId>
    <artifactId>configcat</artifactId>
    <version>[0.1,)</version>
</dependency>
<dependency>
    <groupId>dev.openfeature</groupId>
    <artifactId>sdk</artifactId>
    <version>[1.0,)</version>
</dependency>
```

### 2. Initialize the provider[​](#2-initialize-the-provider "Direct link to 2. Initialize the provider")

The `ConfigCatProvider` constructor takes a `ConfigCatProviderConfig` argument containing the configuration options for the [ConfigCat Java SDK](https://configcat.com/docs/docs/sdk-reference/java/.md#creating-the-configcat-client):

```
// Build options for the ConfigCat SDK.
ConfigCatProviderConfig configCatProviderConfig = ConfigCatProviderConfig.builder()
        .sdkKey("#YOUR-SDK-KEY#")
        .options(options -> {
            options.pollingMode(PollingModes.autoPoll());
            options.logLevel(LogLevel.WARNING);
            // ...
        })
        .build();

// Configure the provider.
OpenFeatureAPI.getInstance().setProviderAndWait(new ConfigCatProvider(configCatProviderConfig));

// Create a client.
Client client = OpenFeatureAPI.getInstance().getClient();
```

For more information about all the configuration options, see the [Java SDK documentation](https://configcat.com/docs/docs/sdk-reference/java/.md#creating-the-configcat-client).

### 3. Evaluate your feature flag[​](#3-evaluate-your-feature-flag "Direct link to 3. Evaluate your feature flag")

```
boolean isAwesomeFeatureEnabled = client.getBooleanValue("isAwesomeFeatureEnabled", false);
if (isAwesomeFeatureEnabled)
{
    doTheNewThing();
}
else
{
    doTheOldThing();
}
```

### 4. Cleaning up[​](#4-cleaning-up "Direct link to 4. Cleaning up")

On application shutdown, clean up the OpenFeature provider and the underlying ConfigCat client.

```
OpenFeatureAPI.getInstance().shutdown();
```

## Evaluation Context[​](#evaluation-context "Direct link to Evaluation Context")

An [evaluation context](https://openfeature.dev/docs/reference/concepts/evaluation-context) in the OpenFeature specification is a container for arbitrary contextual data that can be used as a basis for feature flag evaluation. The ConfigCat provider translates these evaluation contexts to ConfigCat [User Objects](https://configcat.com/docs/docs/sdk-reference/java/.md#user-object).

The following table shows how the different context attributes are mapped to User Object attributes.

| Evaluation context | User Object  | Required |
| ------------------ | ------------ | -------- |
| `TargetingKey`     | `identifier` | ☑        |
| `Email`            | `email`      |          |
| `Country`          | `country`    |          |
| Any other          | `custom`     |          |

To evaluate feature flags for a context, use the [OpenFeature Evaluation API](https://openfeature.dev/docs/reference/concepts/evaluation-api/):

```
MutableContext context = new MutableContext();
context.setTargetingKey("#SOME-USER-ID#");
context.add("Email", "configcat@example.com");
context.add("Country", "CountryID");
context.add("Rating", 4.5);

boolean isAwesomeFeatureEnabled = client.getBooleanValue("isAwesomeFeatureEnabled", false, context);
```

## Look under the hood[​](#look-under-the-hood "Direct link to Look under the hood")

* [ConfigCat OpenFeature Provider's repository on GitHub](https://github.com/open-feature/java-sdk-contrib/tree/main/providers/configcat)
* [ConfigCat OpenFeature Provider on Maven Central](https://search.maven.org/artifact/dev.openfeature.contrib.providers/configcat)
