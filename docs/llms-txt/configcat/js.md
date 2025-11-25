# Source: https://configcat.com/docs/sdk-reference/openfeature/js.md

# Source: https://configcat.com/docs/sdk-reference/js.md

# Source: https://configcat.com/docs/sdk-reference/openfeature/js.md

# Source: https://configcat.com/docs/sdk-reference/js.md

# Source: https://configcat.com/docs/sdk-reference/openfeature/js.md

# Source: https://configcat.com/docs/sdk-reference/js.md

# Source: https://configcat.com/docs/sdk-reference/openfeature/js.md

# OpenFeature Provider for JavaScript

[ConfigCat OpenFeature Provider for JavaScript on GitHub](https://github.com/open-feature/js-sdk-contrib/tree/main/libs/providers/config-cat-web)

## Getting started[​](#getting-started "Direct link to Getting started")

### 1. Install the provider[​](#1-install-the-provider "Direct link to 1. Install the provider")

```
npm i @openfeature/config-cat-web-provider
```

### 2. Initialize the provider[​](#2-initialize-the-provider "Direct link to 2. Initialize the provider")

The `ConfigCatWebProvider.create()` function takes the SDK key and an optional `options` argument containing additional configuration options for the [ConfigCat Browser (JavaScript) SDK](https://configcat.com/docs/docs/sdk-reference/js/browser/.md#creating-the-configcat-client):

```
import { OpenFeature } from "@openfeature/web-sdk";
import { ConfigCatWebProvider } from '@openfeature/config-cat-web-provider';
import { createConsoleLogger, LogLevel } from "@configcat/sdk";

// Build options for the ConfigCat SDK.
const options = {
  logger: createConsoleLogger(LogLevel.Info),
  setupHooks: (hooks) => hooks.on('clientReady', () => console.log('Client is ready!')),
  // ...
}

// Configure the provider.
await OpenFeature.setProviderAndWait(ConfigCatWebProvider.create('#YOUR-SDK-KEY#', options));

// Create a client.
const client = OpenFeature.getClient();
```

For more information about all the configuration options, see the [Browser (JavaScript) SDK documentation](https://configcat.com/docs/docs/sdk-reference/js/browser/.md#creating-the-configcat-client).

### 3. Evaluate your feature flag[​](#3-evaluate-your-feature-flag "Direct link to 3. Evaluate your feature flag")

```
const isAwesomeFeatureEnabled = client.getBooleanValue('isAwesomeFeatureEnabled', false);
if (isAwesomeFeatureEnabled) {
  doTheNewThing();
} else {
  doTheOldThing();
}
```

### 4. Cleaning up[​](#4-cleaning-up "Direct link to 4. Cleaning up")

On application shutdown, clean up the OpenFeature provider and the underlying ConfigCat client.

```
await OpenFeature.clearProviders();
```

## Evaluation Context[​](#evaluation-context "Direct link to Evaluation Context")

An [evaluation context](https://openfeature.dev/docs/reference/concepts/evaluation-context) in the OpenFeature specification is a container for arbitrary contextual data that can be used as a basis for feature flag evaluation. The ConfigCat provider translates these evaluation contexts to ConfigCat [User Objects](https://configcat.com/docs/docs/sdk-reference/js/browser/.md#user-object).

The following table shows how the different context attributes are mapped to User Object attributes.

| Evaluation context | User Object  | Required |
| ------------------ | ------------ | -------- |
| `targetingKey`     | `identifier` | ☑        |
| `email`            | `email`      |          |
| `country`          | `country`    |          |
| Any other          | `custom`     |          |

To evaluate feature flags for a context, use the [OpenFeature Evaluation API](https://openfeature.dev/docs/reference/concepts/evaluation-api/):

```
await OpenFeature.setContext({
  targetingKey: '#SOME-USER-ID#',
  email: 'configcat@example.com',
  country: 'CountryID',
});

const isAwesomeFeatureEnabled = client.getBooleanValue('isAwesomeFeatureEnabled', false);
```

## Look under the hood[​](#look-under-the-hood "Direct link to Look under the hood")

* [ConfigCat OpenFeature Provider's repository on GitHub](https://github.com/open-feature/js-sdk-contrib/tree/main/libs/providers/config-cat-web)
* [ConfigCat OpenFeature Provider in NPM](https://www.npmjs.com/package/@openfeature/config-cat-web-provider)
