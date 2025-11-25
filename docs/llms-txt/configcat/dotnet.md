# Source: https://configcat.com/docs/sdk-reference/openfeature/dotnet.md

# Source: https://configcat.com/docs/sdk-reference/dotnet.md

# Source: https://configcat.com/docs/sdk-reference/openfeature/dotnet.md

# Source: https://configcat.com/docs/sdk-reference/dotnet.md

# Source: https://configcat.com/docs/sdk-reference/openfeature/dotnet.md

# Source: https://configcat.com/docs/sdk-reference/dotnet.md

# Source: https://configcat.com/docs/sdk-reference/openfeature/dotnet.md

# OpenFeature Provider for .NET

[ConfigCat OpenFeature Provider for .NET on GitHub](https://github.com/open-feature/dotnet-sdk-contrib/tree/main/src/OpenFeature.Contrib.Providers.ConfigCat)

## Getting started[​](#getting-started "Direct link to Getting started")

### 1. Install the provider[​](#1-install-the-provider "Direct link to 1. Install the provider")

* Powershell / NuGet Package Manager Console
* .NET CLI
* Package Reference

```
Install-Package OpenFeature.Contrib.Providers.ConfigCat
```

```
dotnet add package OpenFeature.Contrib.Providers.ConfigCat
```

```
<PackageReference Include="OpenFeature.Contrib.Providers.ConfigCat" />
```

### 2. Initialize the provider[​](#2-initialize-the-provider "Direct link to 2. Initialize the provider")

The `ConfigCatProvider` constructor takes the SDK key and an optional callback that can be used to specify additional configuration options for the [ConfigCat .NET SDK](https://configcat.com/docs/docs/sdk-reference/dotnet/.md#creating-the-configcat-client):

```
using System;
using ConfigCat.Client;
using OpenFeature.Contrib.ConfigCat;

// Specify options for the ConfigCat SDK.
Action<ConfigCat.Client.Configuration.ConfigCatClientOptions> configureOptions = (options) =>
{
    options.PollingMode = PollingModes.AutoPoll(pollInterval: TimeSpan.FromSeconds(60));
    options.Logger = new ConsoleLogger(LogLevel.Warning);
    // ...
};

// Configure the provider.
await OpenFeature.Api.Instance.SetProviderAsync(new ConfigCatProvider("#YOUR-SDK-KEY#", configureOptions));

// Create a client.
var client = OpenFeature.Api.Instance.GetClient();
```

For more information about all the configuration options, see the [.NET SDK documentation](https://configcat.com/docs/docs/sdk-reference/dotnet/.md#creating-the-configcat-client).

### 3. Evaluate your feature flag[​](#3-evaluate-your-feature-flag "Direct link to 3. Evaluate your feature flag")

```
var isAwesomeFeatureEnabled = await client.GetBooleanValueAsync("isAwesomeFeatureEnabled", false);
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
await OpenFeature.Api.Instance.ShutdownAsync();
```

## Evaluation Context[​](#evaluation-context "Direct link to Evaluation Context")

An [evaluation context](https://openfeature.dev/docs/reference/concepts/evaluation-context) in the OpenFeature specification is a container for arbitrary contextual data that can be used as a basis for feature flag evaluation. The ConfigCat provider translates these evaluation contexts to ConfigCat [User Objects](https://configcat.com/docs/docs/sdk-reference/dotnet/.md#user-object).

The following table shows how the different context attributes are mapped to User Object attributes.

| Evaluation context | User Object  | Required |
| ------------------ | ------------ | -------- |
| `Id`/`Identifier`  | `Identifier` | ☑        |
| `Email`            | `Email`      |          |
| `Country`          | `Country`    |          |
| Any other          | `Custom`     |          |

To evaluate feature flags for a context, use the [OpenFeature Evaluation API](https://openfeature.dev/docs/reference/concepts/evaluation-api/):

```
var context = OpenFeature.Model.EvaluationContext.Builder()
    .Set("Id", "#SOME-USER-ID#")
    .Set("Email", "configcat@example.com")
    .Set("Country", "CountryID")
    .Set("Rating", 4.5)
    .Set("RegisteredAt", DateTime.Parse("2023-11-22 12:34:56 +00:00", System.Globalization.CultureInfo.InvariantCulture))
    .Build();

var isAwesomeFeatureEnabled = await client.GetBooleanValueAsync("isAwesomeFeatureEnabled", false, context);
```

## Look under the hood[​](#look-under-the-hood "Direct link to Look under the hood")

* [ConfigCat OpenFeature Provider's repository on GitHub](https://github.com/open-feature/dotnet-sdk-contrib/tree/main/src/OpenFeature.Contrib.Providers.ConfigCat)
* [ConfigCat OpenFeature Provider on nuget.org](https://www.nuget.org/packages/OpenFeature.Contrib.Providers.ConfigCat)
