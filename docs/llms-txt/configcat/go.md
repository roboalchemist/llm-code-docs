# Source: https://configcat.com/docs/sdk-reference/openfeature/go.md

# Source: https://configcat.com/docs/sdk-reference/go.md

# Source: https://configcat.com/docs/sdk-reference/openfeature/go.md

# Source: https://configcat.com/docs/sdk-reference/go.md

# Source: https://configcat.com/docs/sdk-reference/openfeature/go.md

# Source: https://configcat.com/docs/sdk-reference/go.md

# Source: https://configcat.com/docs/sdk-reference/openfeature/go.md

# OpenFeature Provider for Go

[ConfigCat OpenFeature Provider for Go on GitHub](https://github.com/open-feature/go-sdk-contrib/tree/main/providers/configcat)

## Getting started[​](#getting-started "Direct link to Getting started")

### 1. Install the provider[​](#1-install-the-provider "Direct link to 1. Install the provider")

```
go get github.com/open-feature/go-sdk-contrib/providers/configcat
```

### 2. Initialize the provider[​](#2-initialize-the-provider "Direct link to 2. Initialize the provider")

The ConfigCat Provider needs a pre-configured [ConfigCat Go SDK](https://configcat.com/docs/docs/sdk-reference/go/.md#creating-the-configcat-client) client:

```
import (
    "time"

    configcat "github.com/configcat/go-sdk/v9"
    configcatprovider "github.com/open-feature/go-sdk-contrib/providers/configcat/pkg"

    "github.com/open-feature/go-sdk/openfeature"
)

func main() {
    // Configure the ConfigCat SDK.
    configcatClient := configcat.NewCustomClient(configcat.Config{SDKKey: "#YOUR-SDK-KEY#",
        PollingMode:  configcat.AutoPoll,
        PollInterval: time.Second * 60})

    // Configure the provider.
    _ = openfeature.SetProviderAndWait(configcatprovider.NewProvider(configcatClient))

    // Create a client.
    client := openfeature.NewClient("app")
}
```

For more information about all the configuration options, see the [Go SDK documentation](https://configcat.com/docs/docs/sdk-reference/go/.md#creating-the-configcat-client).

### 3. Evaluate your feature flag[​](#3-evaluate-your-feature-flag "Direct link to 3. Evaluate your feature flag")

```
isAwesomeFeatureEnabled, err := client.BooleanValue(
    context.Background(), "isAwesomeFeatureEnabled", false, openfeature.EvaluationContext{},
)

if err == nil && isAwesomeFeatureEnabled {
    doTheNewThing()
} else {
    doTheOldThing()
}
```

## Evaluation Context[​](#evaluation-context "Direct link to Evaluation Context")

An [evaluation context](https://openfeature.dev/docs/reference/concepts/evaluation-context) in the OpenFeature specification is a container for arbitrary contextual data that can be used as a basis for feature flag evaluation. The ConfigCat provider translates these evaluation contexts to ConfigCat [User Objects](https://configcat.com/docs/docs/sdk-reference/go/.md#user-object).

The following table shows how the different context attributes are mapped to User Object attributes.

| Evaluation context         | User Object  | Required |
| -------------------------- | ------------ | -------- |
| `openfeature.TargetingKey` | `Identifier` | ☑        |
| `configcat.EmailKey`       | `Email`      |          |
| `configcat.CountryKey`     | `Country`    |          |
| Any other                  | `Custom`     |          |

To evaluate feature flags for a context, use the [OpenFeature Evaluation API](https://openfeature.dev/docs/reference/concepts/evaluation-api/):

```
registeredAt, _ := time.Parse(time.DateTime, "2023-11-22 12:34:56")
context := openfeature.NewEvaluationContext("#SOME-USER-ID#", map[string]any{
    configcat.EmailKey: "configcat@example.com",
    configcat.CountryKey: "CountryID",
    "Rating": 4.5,
    "RegisteredAt": registeredAt,
    "Roles": []string{"Role1","Role2"},
})

isAwesomeFeatureEnabled, err := client.BooleanValue(
    context.Background(), "isAwesomeFeatureEnabled", false, context,
)
```

## Look under the hood[​](#look-under-the-hood "Direct link to Look under the hood")

* [ConfigCat OpenFeature Provider's repository on GitHub](https://github.com/open-feature/go-sdk-contrib/tree/main/providers/configcat)
