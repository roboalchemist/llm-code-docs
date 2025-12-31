# Source: https://configcat.com/docs/sdk-reference/community/vue.md

# ConfigCat SDK for Vue.js

caution

As this is a community-maintained package, ConfigCat can't guarantee its stability, and safety and can't provide official customer support.

[ConfigCat SDK for Vue.js on GitHub](https://github.com/codedbychavez/configcat-vue)

## Getting Started[​](#getting-started "Direct link to Getting Started")

### 1. Install the package[​](#1-install-the-package "Direct link to 1. Install the package")

*via [npm](https://www.npmjs.com/package/configcat-vue)*

```
npm i configcat-vue
```

### 2. Import and use the `ConfigCatPlugin` with your SDK Key[​](#2-import-and-use-the-configcatplugin-with-your-sdk-key "Direct link to 2-import-and-use-the-configcatplugin-with-your-sdk-key")

In **main.ts**:

```
import { ConfigCatPlugin } from "configcat-vue";
```

```
app.use(ConfigCatPlugin, {
  sdkKey: "YOUR-CONFIGCAT-SDK-KEY-GOES-HERE", // sdkKey is required
});
```

### 3. Get your setting value[​](#3-get-your-setting-value "Direct link to 3. Get your setting value")

This SDK includes a `FeatureWrapper` component. It enables users to control the visibility of specific parts within their Vue.js application (such as components or HTML elements) when the feature flag is enabled.

In any `.vue` component file:

```
<script setup lang="ts">

import { FeatureWrapper } from "configcat-vue";

</script>
```

Pass the feature flag key as a prop:

```
<template>
  <div class="my-app">
    <FeatureWrapper featureKey="YOUR-FEATURE-KEY-GOES-HERE">
      <!-- This is displayed when the feature flag is turned on --> 
      <TheNewFeature />
    </FeatureWrapper>
  </div>
</template>
```

Optionally, the `FeatureWrapper` component also provides an `#else` and `#loading` template. Components or HTML elements can be included within these templates that would display when the feature flag is **turned off** or **loading** respectively.

```
<FeatureWrapper
  featureKey="YOUR-FEATURE-KEY-GOES-HERE"
>
  <TheNewFeature />
  <template #else>
    <!-- Displayed when the feature flag is turned off -->
    <div class="feature-not-available-wrapper">
      <p>Sorry, this feature is not available. Your feature flag is off.</p>
    </div>
  </template>
  <template #loading>
    <!-- Display while the feature flag is loading -->
    <div class="loading-wrapper">
      <p>Loading...</p>
    </div>
  </template>
</FeatureWrapper>
```

## Advanced Usage[​](#advanced-usage "Direct link to Advanced Usage")

### Specifying a polling mode[​](#specifying-a-polling-mode "Direct link to Specifying a polling mode")

Polling modes are used to control how often ConfigCat's SDK client downloads the values of feature flags from ConfigCat's servers. The default polling mode is `AutoPoll`. Auto Polling fetches the latest feature flag values every 60 seconds by default. To change this, Specify a polling mode and set the polling interval (in seconds) via the `pollingIntervalInSeconds` property.

Import:

```
import { PollingMode } from "configcat-vue";
```

Add `pollingMode` to the `ConfigCatPlugin` options and set the polling interval via the `clientOptions` property:

```
app.use(ConfigCatPlugin, {
    sdkKey: "YOUR-CONFIGCAT-SDKKEY-GOES-HERE",
    pollingMode: PollingMode.AutoPoll, // Optional. Default is AutoPoll
    clientOptions: {
        pollIntervalSeconds: 5 // Optional. Specify the polling interval in seconds. The default is 60 seconds.
    }
});
```

`pollingMode` can be set to: `PollingMode.AutoPoll`, `PollingMode.ManualPoll` and `PollingMode.LazyLoad`

> See documentation [here](https://configcat.com/docs/docs/advanced/caching/.md).

### Using the plugin with a logger[​](#using-the-plugin-with-a-logger "Direct link to Using the plugin with a logger")

You may want to log the actions of the underlying ConfigCat SDK client. To do this, specify a logger in `clientOptions`:

> See documentation [here](https://configcat.com/docs/docs/sdk-reference/js/browser/.md#logging).

Add `createConsoleLogger`, and `LoggerLevel` to your import:

```
import { createConsoleLogger, LogLevel } from "configcat-vue"; 
```

Create the logger with a specified log level:

> See documentation [here](https://configcat.com/docs/docs/sdk-reference/js/browser/.md#setting-log-levels).

Use the logger in `clientOptions`:

```
app.use(ConfigCatPlugin, {
  sdkKey: "YOUR-CONFIGCAT-SDK-KEY-GOES-HERE", // // sdkKey is required
  clientOptions: { // clientOptions is optional
    // ...
    logger: createConsoleLogger(LogLevel.Info),
  }
});
```

#### Available log levels[​](#available-log-levels "Direct link to Available log levels")

| Level | Description                                             |
| ----- | ------------------------------------------------------- |
| Off   | Nothing gets logged.                                    |
| Error | Only error level events are logged.                     |
| Warn  | Default. Errors and Warnings are logged.                |
| Info  | Errors, Warnings and feature flag evaluation is logged. |
| Debug | All of the above plus debug info is logged.             |

### Specifying a User Object[​](#specifying-a-user-object "Direct link to Specifying a User Object")

The [User Object](https://configcat.com/docs/docs/targeting/user-object/.md) stores attributes of a user in your application. It works hand in hand with ConfigCat's [Targeting](https://configcat.com/docs/docs/targeting/targeting-overview/.md) rules for targeting specific users with feature flags. A User Object can be passed as a prop to the `FeatureWrapper` component.

> See documentation [here](https://configcat.com/docs/docs/targeting/user-object/.md).

Define the User Object:

```
<script setup lang="ts">
import { ref } from 'vue';
import { User } from 'configcat-vue';

// Define the User Object
const user = { identifier: 'john@example.com' };
const userObject = ref<User>(user)

</script>
```

Pass it to the `FeatureWrapper` component:

```
<template>
  <div class="my-app">
    <FeatureWrapper featureKey="YOUR-FEATURE-KEY-GOES-HERE" :userObject="userObject">
      <TheNewFeature />
    </FeatureWrapper>
  </div>
</template>
```

### Listening to flag changes emitted from the FeatureWrapper component[​](#listening-to-flag-changes-emitted-from-the-featurewrapper-component "Direct link to Listening to flag changes emitted from the FeatureWrapper component")

When a feature flag is toggled ON or OFF in the [ConfigCat Dashboard](https://app.configcat.com) the `FeatureWrapper` component emits the updated feature flag value. How quickly the updated value is emitted depends on the polling interval set in the `clientOptions` property of the `ConfigCatPlugin`.

Listen and handle changes using `@flag-value-changed`:

```
<template>
  <div class="my-app">
    <FeatureWrapper featureKey="YOUR-FEATURE-KEY-GOES-HERE" @flag-value-changed="handleFlagValueChange">
      <TheNewFeature />
    </FeatureWrapper>
  </div>
</template>
```

```
<script setup lang="ts">
// Handle to the flag value changes
const handleFlagValueChange = (flagValue: boolean) => {
  console.log('Flag value changed to: ', flagValue);
}
</script>
```

### Using the underlying ConfigCat client[​](#using-the-underlying-configcat-client "Direct link to Using the underlying ConfigCat client")

This plugin exposes (provides) the underlying ConfigCat client. By injecting the provided client instance, you can use all the features it offers.

> See documentation [here](https://configcat.com/docs/docs/sdk-reference/js/browser/.md).

One of the ways it can be used is by subscribing to events emitted by the ConfigCat client.

Inject the ConfigCat client into your component:

```
<script setup lang="ts">
import { inject, onBeforeMount } from 'vue';
import { FeatureWrapper } from "configcat-vue";

// Import the ConfigCat client interface
import type { IConfigCatClient } from 'configcat-vue';

// Inject the ConfigCat client
const configCatClient = inject<IConfigCatClient>('configCatClient');

onBeforeMount(() => {
  // Subscribe to the events using the .on method of the ConfigCat SDK client
  configCatClient?.on('flagEvaluated', () => {
    console.log('Flag evaluated');
  });
});
</script>
```

## Sample Application[​](#sample-application "Direct link to Sample Application")

* [Sample Vue.js App](https://github.com/codedbychavez/configcat-vue-sample)

## Look under the hood[​](#look-under-the-hood "Direct link to Look under the hood")

* [ConfigCat Vue.js SDK on GitHub](https://github.com/codedbychavez/configcat-vue)
* [ConfigCat Vue.js SDK on NPM](https://www.npmjs.com/package/configcat-vue)
