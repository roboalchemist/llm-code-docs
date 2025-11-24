# Source: https://configcat.com/docs/sdk-reference/js/bun.md

# Bun SDK

<!-- -->

<!-- -->

<!-- -->

<!-- -->

<!-- -->

<!-- -->

[![Star on GitHub](https://img.shields.io/github/stars/configcat/js-unified-sdk.svg?style=social)](https://github.com/configcat/js-unified-sdk/stargazers) [![JS SDK CI](https://github.com/configcat/js-unified-sdk/actions/workflows/js-sdk-ci.yml/badge.svg?branch=master)](https://github.com/configcat/js-unified-sdk/actions/workflows/js-sdk-ci.yml) [![SonarCloud Coverage](https://img.shields.io/sonar/coverage/configcat_js-unified-sdk?logo=SonarCloud\&server=https%3A%2F%2Fsonarcloud.io)](https://sonarcloud.io/project/overview?id=configcat_js-unified-sdk) [![Known Vulnerabilities](https://snyk.io/test/github/configcat/js-unified-sdk/badge.svg?targetFile=package.json)](https://snyk.io/test/github/configcat/js-unified-sdk?targetFile=package.json) [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=configcat_js-sdk\&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=configcat_js-sdk) [![JSDELIVR](https://data.jsdelivr.com/v1/package/npm/@configcat/sdk/badge)](https://data.jsdelivr.com/v1/package/npm/@configcat/sdk/badge)

<!-- -->

<!-- -->

<!-- -->

[ConfigCat SDK for JavaScript on GitHub](https://github.com/configcat/js-unified-sdk)

## Getting started[​](#getting-started "Direct link to Getting started")

### 1. Install and import package[​](#1-install-and-import-package "Direct link to 1. Install and import package")

<!-- -->

<!-- -->

<!-- -->

First install the [NPM package](https://npmjs.com/package/@configcat/sdk):

```
npm i @configcat/sdk
```

Then import it into your application:

```
import * as configcat from "@configcat/sdk/bun";
```

### 2. Create the *ConfigCat* client with your SDK Key[​](#2-create-the-configcat-client-with-your-sdk-key "Direct link to 2-create-the-configcat-client-with-your-sdk-key")

```
const configCatClient = configcat.getClient('#YOUR-SDK-KEY#');
```

<!-- -->

### 3. Get your setting value[​](#3-get-your-setting-value "Direct link to 3. Get your setting value")

The async/await way:

```
const value = await configCatClient.getValueAsync(
  'isMyAwesomeFeatureEnabled',
  false,
);

if (value) {
  do_the_new_thing();
} else {
  do_the_old_thing();
}
```

<!-- -->

<!-- -->

The Promise way:

```
configCatClient
  .getValueAsync('isMyAwesomeFeatureEnabled', false)
  .then((value) => {
    if (value) {
      do_the_new_thing();
    } else {
      do_the_old_thing();
    }
  });
```

The *ConfigCat SDK* also offers a synchronous API for feature flag evaluation. Read more [here](#snapshots-and-synchronous-feature-flag-evaluation).

### 4. Dispose the *ConfigCat* client[​](#4-dispose-the-configcat-client "Direct link to 4-dispose-the-configcat-client")

You can safely dispose all clients at once or individually and release all associated resources on application exit.

```
configcat.disposeAllClients(); // disposes all clients
// -or-
configCatClient.dispose(); // disposes a specific client
```

<!-- -->

## Creating the *ConfigCat* Client[​](#creating-the-configcat-client "Direct link to creating-the-configcat-client")

*ConfigCat Client* is responsible for:

* managing the communication between your application and ConfigCat servers.
* caching your setting values and feature flags.
* serving values quickly in a failsafe way.

`configcat.getClient('<sdkKey>')` returns a client with default options.

The `getClient` function has optional parameters, which can be used to adjust the behavior of the client.

| Parameters    | Description                                                                                                                    | Default                |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------ | ---------------------- |
| `sdkKey`      | **REQUIRED.** SDK Key to access your feature flags and settings. Get it from *ConfigCat Dashboard*.                            | -                      |
| `pollingMode` | Optional. The polling mode to use to fetch the config data from the ConfigCat CDN. [More about polling modes](#polling-modes). | `PollingMode.AutoPoll` |
| `options`     | Optional. The options object. See the table below.                                                                             | -                      |

The available options depends on the chosen polling mode. However, there are some common options which can be set in the case of every polling mode:

<!-- -->

<!-- -->

<!-- -->

| Option Parameter   | Description                                                                                                                                                                                                                                                                                                                       | Default                                                                                                                      |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `configFetcher`    | Custom [`IConfigCatConfigFetcher`](https://github.com/configcat/js-unified-sdk/blob/master/src/ConfigFetcher.ts) instance for downloading a config.                                                                                                                                                                               | [`NodeHttpConfigFetcher`](https://github.com/configcat/js-unified-sdk/blob/master/src/node/NodeHttpConfigFetcher.ts)         |
| `cache`            | Custom [`IConfigCatCache`](https://github.com/configcat/js-unified-sdk/blob/master/src/ConfigCatCache.ts) implementation for caching the downloaded config.                                                                                                                                                                       | [`InMemoryConfigCache`](https://github.com/configcat/js-unified-sdk/blob/master/src/ConfigCatCache.ts)                       |
| `logger`           | Custom [`IConfigCatLogger`](https://github.com/configcat/js-unified-sdk/blob/master/src/ConfigCatLogger.ts) implementation for tracing.                                                                                                                                                                                           | [`ConfigCatConsoleLogger`](https://github.com/configcat/js-unified-sdk/blob/master/src/ConfigCatLogger.ts) (with WARN level) |
| `logFilter`        | Sets a custom log filter. [More about log filtering](#log-filtering).                                                                                                                                                                                                                                                             | `undefined` (none)                                                                                                           |
| `baseUrl`          | Sets the CDN base url (forward proxy, dedicated subscription) from where the SDK will download the config JSON.                                                                                                                                                                                                                   |                                                                                                                              |
| `httpAgent`        | The [`http.Agent`](https://nodejs.org/api/http.html#class-httpagent) instance to use for non-secure HTTP communication. Can be used to route `http://...` requests made by the SDK through an HTTP, HTTPS or SOCKS proxy (see also [this section](#using-configcat-behind-a-proxy)).                                              |                                                                                                                              |
| `httpsAgent`       | The [`https.Agent`](https://nodejs.org/api/https.html#class-httpsagent) instance to use for secure HTTP communication. Can be used to route `https://...` requests made by the SDK through an HTTP, HTTPS or SOCKS proxy (see also [this section](#using-configcat-behind-a-proxy)).                                              |                                                                                                                              |
| `requestTimeoutMs` | The amount of milliseconds the SDK waits for a response from the ConfigCat servers before returning values from the cache.                                                                                                                                                                                                        | 30000                                                                                                                        |
| `flagOverrides`    | Local feature flag & setting overrides. [More about feature flag overrides](#flag-overrides).                                                                                                                                                                                                                                     |                                                                                                                              |
| `dataGovernance`   | Describes the location of your feature flag and setting data within the ConfigCat CDN. This parameter needs to be in sync with your Data Governance preferences. [More about Data Governance](https://configcat.com/docs/docs/advanced/data-governance/.md). Available options: `DataGovernance.Global`, `DataGovernance.EuOnly`. | `DataGovernance.Global`                                                                                                      |
| `defaultUser`      | Sets the default user. [More about default user](#default-user).                                                                                                                                                                                                                                                                  | `undefined` (none)                                                                                                           |
| `offline`          | Determines whether the client should be initialized to offline mode. [More about offline mode](#online--offline-mode).                                                                                                                                                                                                            | `false`                                                                                                                      |

Options also include a property named `setupHook`, which you can use to subscribe to the hooks (events) at the time of initialization. [More about hooks](#hooks).

For example:

```
const configCatClient = configcat.getClient(
  '#YOUR-SDK-KEY#',
  configcat.PollingMode.AutoPoll,
  {
    setupHooks: (hooks) => hooks.on('clientReady', function() {
      const keys = this.configCatClient.snapshot().getAllKeys();
      console.log(`Client is ready! Number of available feature flags: ${keys.length}`);
    }),
  },
);
```

info

You can acquire singleton client instances for your SDK keys using the `configcat.getClient(sdkKey: "<sdkKey>")` factory function. (However, please keep in mind that subsequent calls to `getClient()` with the *same SDK Key* return a *shared* client instance, which was set up by the first call.)

You can close all open clients at once using the `configcat.disposeAllClients()` function or do it individually using the `configCatClient.dispose()` method.

## Anatomy of `getValueAsync()`[​](#anatomy-of-getvalueasync "Direct link to anatomy-of-getvalueasync")

Returns a Promise with the value.

| Parameters     | Description                                                                                                                                             |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `key`          | **REQUIRED.** The key of a specific setting or feature flag. Set on *ConfigCat Dashboard* for each setting.                                             |
| `defaultValue` | **REQUIRED.** This value will be returned in case of an error.                                                                                          |
| `user`         | Optional, *User Object*. Essential when using Targeting. [Read more about Targeting.](https://configcat.com/docs/docs/targeting/targeting-overview/.md) |

```
const value = await configCatClient.getValueAsync(
  'keyOfMyFeatureFlag', // Setting Key
  false, // Default value
  { identifier: '#UNIQUE-USER-IDENTIFIER#' }, // Optional User Object
);
```

or

```
configCatClient
  .getValueAsync(
    'keyOfMyFeatureFlag', // Setting Key
    false, // Default value
    { identifier: '#UNIQUE-USER-IDENTIFIER#' }, // Optional User Object
  )
  .then((value) => {
    console.log(value);
  });
```

caution

It is important to provide an argument for the `defaultValue` parameter that matches the type of the feature flag or setting you are evaluating. Please refer to the following table for the corresponding types.

### Setting type mapping[​](#setting-type-mapping "Direct link to Setting type mapping")

| Setting Kind   | `typeof defaultValue` |
| -------------- | --------------------- |
| On/Off Toggle  | `boolean`             |
| Text           | `string`              |
| Whole Number   | `number`              |
| Decimal Number | `number`              |

In addition to the types mentioned above, you also have the option to provide `null` or `undefined` for the `defaultValue` parameter regardless of the setting kind. However, if you do so, the return type of the `getValue` method will be

* `boolean | string | number | null` when `defaultValue` is `null` or
* `boolean | string | number | undefined` when `defaultValue` is `undefined`.

This is because in these cases the exact return type cannot be determined at compile-time as the TypeScript compiler has no information about the setting type.

It's important to note that providing any other type for the `defaultValue` parameter will result in a `TypeError`.

If you specify an allowed type but it mismatches the setting kind, an error message will be logged and `defaultValue` will be returned.

## Anatomy of `getValueDetailsAsync()`[​](#anatomy-of-getvaluedetailsasync "Direct link to anatomy-of-getvaluedetailsasync")

`getValueDetailsAsync()` is similar to `getValueAsync()` but instead of returning the evaluated value only, it provides more detailed information about the evaluation result.

| Parameters     | Description                                                                                                                                             |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `key`          | **REQUIRED.** The key of a specific setting or feature flag. Set on *ConfigCat Dashboard* for each setting.                                             |
| `defaultValue` | **REQUIRED.** This value will be returned in case of an error.                                                                                          |
| `user`         | Optional, *User Object*. Essential when using Targeting. [Read more about Targeting.](https://configcat.com/docs/docs/targeting/targeting-overview/.md) |

```
const details = await configCatClient.getValueDetailsAsync(
  'keyOfMyFeatureFlag', // Setting Key
  false, // Default value
  { identifier: '#UNIQUE-USER-IDENTIFIER#' }, // Optional User Object
);
```

or

```
configCatClient
  .getValueDetailsAsync(
    'keyOfMyFeatureFlag', // Setting Key
    false, // Default value
    { identifier: '#UNIQUE-USER-IDENTIFIER#' }, // Optional User Object
  )
  .then((details) => {
    console.log(details);
  });
```

caution

It is important to provide an argument for the `defaultValue` parameter that matches the type of the feature flag or setting you are evaluating. Please refer to [this table](#setting-type-mapping) for the corresponding types.

The `details` result contains the following information:

| Field                     | Type                            | Description                                                                                                |
| ------------------------- | ------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `key`                     | `string`                        | The key of the evaluated feature flag or setting.                                                          |
| `value`                   | `boolean` / `string` / `number` | The evaluated value of the feature flag or setting.                                                        |
| `user`                    | `User`                          | The User Object used for the evaluation.                                                                   |
| `isDefaultValue`          | `boolean`                       | True when the default value passed to `getValueDetailsAsync()` is returned due to an error.                |
| `errorCode`               | `EvaluationErrorCode`           | In case of an error, this property contains a code that identifies the reason for the error.               |
| `errorMessage`            | `string`                        | In case of an error, this property contains the error message.                                             |
| `errorException`          | `any`                           | In case of an error, this property contains the related exception object (if any).                         |
| `matchedTargetingRule`    | `TargetingRule`                 | The Targeting Rule (if any) that matched during the evaluation and was used to return the evaluated value. |
| `matchedPercentageOption` | `PercentageOption`              | The Percentage Option (if any) that was used to select the evaluated value.                                |
| `fetchTime`               | `Date`                          | The last download time (UTC) of the current config.                                                        |

## User Object[​](#user-object "Direct link to User Object")

The [User Object](https://configcat.com/docs/docs/targeting/user-object/.md) is essential if you'd like to use ConfigCat's [Targeting](https://configcat.com/docs/docs/targeting/targeting-overview/.md) feature.

For simple targeting:

```
const userObject = { identifier: '#UNIQUE-USER-IDENTIFIER#' };
```

```
const userObject = { identifier: 'john@example.com' };
```

| Parameters   | Description                                                                                                                     |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------- |
| `identifier` | **REQUIRED.** Unique identifier of a user in your application. Can be any `string` value, even an email address.                |
| `email`      | Optional parameter for easier Targeting Rule definitions.                                                                       |
| `country`    | Optional parameter for easier Targeting Rule definitions.                                                                       |
| `custom`     | Optional dictionary for custom attributes of a user for advanced Targeting Rule definitions. E.g. User role, Subscription type. |

For advanced targeting:

```
const userObject = {
  identifier: '#UNIQUE-USER-IDENTIFIER#',
  email: 'john@example.com',
  country: 'United Kingdom',
  custom: {
    SubscriptionType: 'Pro',
    UserRole: 'Admin',
  },
};
```

The `custom` dictionary also allows attribute values other than `string` values:

```
const userObject = { identifier: '#UNIQUE-USER-IDENTIFIER#' };
userObject.custom = {
  Rating: 4.5,
  RegisteredAt: new Date('2023-11-22T12:34:56.000Z'),
  Roles: ['Role1', 'Role2'],
};
```

### User Object Attribute Types[​](#user-object-attribute-types "Direct link to User Object Attribute Types")

All comparators support `string` values as User Object attribute (in some cases they need to be provided in a specific format though, see below), but some of them also support other types of values. It depends on the comparator how the values will be handled. The following rules apply:

**Text-based comparators** (EQUALS, IS ONE OF, etc.)

* accept `string` values,
* all other values are automatically converted to `string` (a warning will be logged but evaluation will continue as normal).

**SemVer-based comparators** (IS ONE OF, <, >=, etc.)

* accept `string` values containing a properly formatted, valid semver value,
* all other values are considered invalid (a warning will be logged and the currently evaluated Targeting Rule will be skipped).

**Number-based comparators** (=, <, >=, etc.)

* accept `number` values,
* accept `string` values containing a properly formatted, valid `number` value,
* all other values are considered invalid (a warning will be logged and the currently evaluated Targeting Rule will be skipped).

**Date time-based comparators** (BEFORE / AFTER)

* accept `Date` values, which are automatically converted to a second-based Unix timestamp,
* accept `number` values representing a second-based Unix timestamp,
* accept `string` values containing a properly formatted, valid `number` value,
* all other values are considered invalid (a warning will be logged and the currently evaluated Targeting Rule will be skipped).

**String array-based comparators** (ARRAY CONTAINS ANY OF / ARRAY NOT CONTAINS ANY OF)

* accept arrays of `string`,
* accept `string` values containing a valid JSON string which can be deserialized to an array of `string`,
* all other values are considered invalid (a warning will be logged and the currently evaluated Targeting Rule will be skipped).

### Default user[​](#default-user "Direct link to Default user")

It's possible to set a default User Object that will be used on feature flag and setting evaluation. It can be useful when your application has a single user only or rarely switches users.

You can set the default User Object either on SDK initialization:

```
const configCatClient = configcat.getClient(
  '#YOUR-SDK-KEY#',
  configcat.PollingMode.AutoPoll,
  {
    defaultUser: { identifier: 'john@example.com' },
  },
);
```

...or using the `setDefaultUser()` method of the `configCatClient` object:

```
configCatClient.setDefaultUser({ identifier: 'john@example.com' });
```

Whenever the evaluation methods like `getValueAsync()`, `getValueDetailsAsync()`, etc. are called without an explicit `user` parameter, the SDK will automatically use the default user as a User Object.

```
const user = { identifier: 'john@example.com' };
configCatClient.setDefaultUser(user);

// The default user will be used in the evaluation process.
const value = await configCatClient.getValueAsync('keyOfMyFeatureFlag', false);
```

When a `user` parameter is passed to the evaluation methods, it takes precedence over the default user.

```
const user = { identifier: 'john@example.com' };
configCatClient.setDefaultUser(user);

const otherUser = { identifier: 'brian@example.com' };

// otherUser will be used in the evaluation process.
const value = await configCatClient.getValueAsync(
  'keyOfMyFeatureFlag',
  false,
  otherUser,
);
```

You can also remove the default user by doing the following:

```
configCatClient.clearDefaultUser();
```

## Polling Modes[​](#polling-modes "Direct link to Polling Modes")

The *ConfigCat SDK* supports 3 different polling strategies to fetch feature flags and settings from the ConfigCat CDN. Once the latest data is downloaded, it is stored in the cache, then calls to `getValueAsync()` use the cached data to evaluate feature flags and settings. With the following polling modes, you can customize the SDK to best fit to your application's lifecycle. [More about polling modes.](https://configcat.com/docs/docs/advanced/caching/.md)

### Auto polling (default)[​](#auto-polling-default "Direct link to Auto polling (default)")

The *ConfigCat SDK* downloads the latest config data from the ConfigCat CDN automatically every 60 seconds and stores it in the cache.

Use the `pollIntervalSeconds` option parameter to change the polling interval.

```
const configCatClient = configcat.getClient(
  '#YOUR-SDK-KEY#',
  configcat.PollingMode.AutoPoll,
  {
    pollIntervalSeconds: 95,
  },
);
```

Available options (in addition to the [common ones](#creating-the-configcat-client)):

| Option Parameter         | Description                                                                                         | Default |
| ------------------------ | --------------------------------------------------------------------------------------------------- | ------- |
| `pollIntervalSeconds`    | Polling interval in seconds.                                                                        | 60s     |
| `maxInitWaitTimeSeconds` | Maximum waiting time between the client initialization and the first config acquisition in seconds. | 5s      |

### Lazy loading[​](#lazy-loading "Direct link to Lazy loading")

When calling `getValueAsync()`, the *ConfigCat SDK* downloads the latest config data from the ConfigCat CDN only if it is not already present in the cache, or if the cache has expired. In this case `getValueAsync()` will return the setting value after the cache is updated.

Use `cacheTimeToLiveSeconds` option parameter to set cache lifetime.

```
const configCatClient = configcat.getClient(
  '#YOUR-SDK-KEY#',
  configcat.PollingMode.LazyLoad,
  {
    cacheTimeToLiveSeconds: 600,
  },
);
```

Available options (in addition to the [common ones](#creating-the-configcat-client)):

| Option Parameter         | Description           | Default |
| ------------------------ | --------------------- | ------- |
| `cacheTimeToLiveSeconds` | Cache TTL in seconds. | 60s     |

### Manual polling[​](#manual-polling "Direct link to Manual polling")

Manual polling gives you full control over when the config data is downloaded from the ConfigCat CDN. The *ConfigCat SDK* will not download it automatically. Calling `forceRefreshAsync()` is your application's responsibility.

```
const configCatClient = configcat.getClient(
  '#YOUR-SDK-KEY#',
  configcat.PollingMode.ManualPoll,
);

await configCatClient.forceRefreshAsync();
const value = await configCatClient.getValueAsync(
  'keyOfMyTextSetting',
  'my default value',
);
console.log(value);
```

> `getValueAsync()` returns `defaultValue` if the cache is empty. Call `forceRefreshAsync()` to update the cache.

```
const configCatClient = configcat.getClient(
  '#YOUR-SDK-KEY#',
  configcat.PollingMode.ManualPoll,
);

const value = await configCatClient.getValueAsync(
  'keyOfMyTextSetting',
  'my default value',
);
console.log(value); // console: "my default value"

await configCatClient.forceRefreshAsync();
value = await configCatClient.getValueAsync(
  'keyOfMyTextSetting',
  'my default value',
);
console.log(value);
```

## Hooks[​](#hooks "Direct link to Hooks")

The SDK provides several hooks (events), by means of which you can get notified of its actions. You can subscribe to the following events emitted by the *ConfigCat* client:

* `clientReady: [cacheState: ClientCacheState]`: This event is emitted when the client reaches the ready state, i.e. completes initialization.

  * If Lazy Loading or Manual Polling is used, it's considered ready right after the initial sync with the external cache (if any) completes.

  * If Auto Polling is used, the ready state is reached as soon as

    <!-- -->

    * the initial sync with the external cache yields up-to-date config data,
    * otherwise, if the client is online (i.e. HTTP requests are allowed), the first config fetch operation completes (regardless of success or failure),
    * or the time specified via Auto Polling's `maxInitWaitTimeSeconds` option has passed.

  Reaching the ready state usually means the client is ready to evaluate feature flags and settings. However, please note that this is not guaranteed. In case of initialization failure or timeout, the internal cache may be empty or expired even after the ready state is reported. You can verify this by checking the `cacheState` argument.

* `configFetched: [result: RefreshResult, isInitiatedByUser: boolean]`: This event is emitted each time the client attempts to refresh the cached config by fetching the latest version from the ConfigCat CDN. It is emitted not only when `ForceRefreshAsync` is called but also when the refresh is initiated by the client automatically. Thus, this event allows you to observe potential network issues that occur under the hood.

* `configChanged: [newConfig: IConfig]`: This event is emitted first when the client's internal cache gets populated. Afterwards, it is emitted again each time the internally cached config is updated to a newer version, either as a result of synchronization with the external cache, or as a result of fetching a newer version from the ConfigCat CDN.

* `flagEvaluated: [evaluationDetails: IEvaluationDetails]`: This event is emitted each time the client evaluates a feature flag or setting. The event provides the same evaluation details that you would get from [`getValueDetailsAsync()`](#anatomy-of-getvaluedetailsasync).

* `clientError: [message: string, exception?: any]`: This event is emitted when an error occurs within the client.

You can subscribe to these events either on initialization:

```
const configCatClient = configcat.getClient(
  '#YOUR-SDK-KEY#',
  configcat.PollingMode.ManualPoll,
  {
    setupHooks: (hooks) =>
      hooks.on('flagEvaluated', function() {
        /* handle the event */
      }),
  },
);
```

...or directly on the `ConfigCatClient` instance:

```
configCatClient.on('flagEvaluated', function() {
  /* handle the event */
});
```

caution

Some events (e.g. `clientReady`, `configChanged` and `clientError`) may be emitted before `getClient` returns. This means you may miss them unless you subscribe on initialization.

However, even if you do, there's another gotcha: it's not safe to use the outer `configCatClient` variable in your event handler because it may not yet be assigned when the handler is called. Instead, you can safely access the client instance via `this.configCatClient` - provided that the event handler is a normal function, not an arrow function.

## Snapshots and synchronous feature flag evaluation[​](#snapshots-and-synchronous-feature-flag-evaluation "Direct link to Snapshots and synchronous feature flag evaluation")

On JavaScript platforms, the *ConfigCat* client provides only asynchronous methods for evaluating feature flags and settings because these operations may involve network communication (e.g. downloading config data from the ConfigCat CDN servers), which is necessarily an asynchronous operation in JavaScript.

However, there can be circumstances where synchronous evaluation is preferable, thus, since v8.1.0, the JavaScript SDK provides a way to synchronously evaluate feature flags and settings via *snapshots*.

Using the `snapshot()` method, you can capture the current state of the *ConfigCat* client (including the latest downloaded config data) and use the resulting snapshot object to synchronously evaluate feature flags and settings based on the captured state:

```
const configCatClient = configcat.getClient(
  '#YOUR-SDK-KEY#',
  configcat.PollingMode.AutoPoll,
);

// Wait for the client to initialize.
await configCatClient.waitForReady();

const snapshot = configCatClient.snapshot();

const user = { identifier: '#UNIQUE-USER-IDENTIFIER#' };
for (const key of snapshot.getAllKeys()) {
  const value = snapshot.getValue(key, null, user);
  console.log(`${key}: ${value}`);
}
```

Creating a snapshot is a cheap operation. This is possible because snapshots capture the client's internal (in-memory) cache. No attempt is made to refresh the internal cache, even if it's empty or expired.

caution

Please note that creating and using a snapshot

* won't trigger a sync with the external cache when working with [shared caching](https://configcat.com/docs/docs/advanced/caching/.md#shared-cache),
* won't fetch the latest config data from the ConfigCat CDN when the internally cached config data is empty or expired.

For the above reasons, it's recommended to use snapshots in conjunction with the Auto Polling mode, where the SDK automatically updates the internal cache in the background. (For other polling modes, you'll need to manually initiate a cache refresh by calling `forceRefreshAsync`.)

Because of this behavior, it's important to make sure that the client has completed initialization and populated its internal cache before creating snapshots. Otherwise the snapshot's evaluation methods won't have the data to do actual evaluation, but will just return the default value you pass to them. Which behavior is usually not what you want in your application.

In Auto Polling mode, you can use the `waitForReady` method to wait for the latest config data to become available locally. This is an asynchronous operation, which completes as soon as the client reaches the ready state, i.e. completes initialization (or the time specified via the `maxInitWaitTimeSeconds` option passes).

(Please note that this doesn't apply to other polling modes. In those cases, the client doesn't contact the ConfigCat CDN during initialization, so the ready state is reached as soon as the first sync with the external cache completes.)

Typically, you call `waitForReady` and wait for its completion only once, in the initialization phase of your application.

caution

Reaching the ready state usually means the client is ready to evaluate feature flags and settings. However, please note that this is not guaranteed. In case of initialization failure or timeout, the internal cache may be empty or expired even after the ready state is reported. You can verify this by checking the return value.

```
const clientCacheState = await configCatClient.waitForReady();
if (clientCacheState === configcat.ClientCacheState.NoFlagData) {
  // Handle initialization failure (see below).
  console.warn('ConfigCat client failed to obtain the config data during initialization.');
}
```

You have the following options to handle unsuccessful initialization:

* If it's acceptable for your application to start up and use the default values passed to the evaluation methods, you may log some warning (or skip the check altogether as the client will log warnings anyway), and let the application continue.
* Otherwise, you need to either terminate the application or continue waiting. The latter is an option because the client might be able to obtain the config data later, in the case of a transient problem like some temporary network issue. However, the *ConfigCat SDK* doesn't provide out-of-the-box support for this case currently. You can implement this logic by subscribing to the `configChanged` hook and waiting for the first event.

## Online / Offline mode[​](#online--offline-mode "Direct link to Online / Offline mode")

In cases where you want to prevent the SDK from making HTTP calls, you can switch it to offline mode:

```
configCatClient.setOffline();
```

In offline mode, the SDK won't initiate HTTP requests and will work only from its cache.

To switch the SDK back to online mode, do the following:

```
configCatClient.setOnline();
```

Using the `configCatClient.isOffline` property you can check whether the SDK is in offline mode.

## Flag Overrides[​](#flag-overrides "Direct link to Flag Overrides")

With flag overrides you can overwrite the feature flags & settings downloaded from the ConfigCat CDN with local values. Moreover, you can specify how the overrides should apply over the downloaded values. The following 3 behaviours are supported:

* **Local only** (`OverrideBehaviour.LocalOnly`): When evaluating values, the SDK will not use feature flags & settings from the ConfigCat CDN, but it will use all feature flags & settings that are loaded from local-override sources.

* **Local over remote** (`OverrideBehaviour.LocalOverRemote`): When evaluating values, the SDK will use all feature flags & settings that are downloaded from the ConfigCat CDN, plus all feature flags & settings that are loaded from local-override sources. If a feature flag or a setting is defined both in the downloaded and the local-override source then the local-override version will take precedence.

* **Remote over local** (`OverrideBehaviour.RemoteOverLocal`): When evaluating values, the SDK will use all feature flags & settings that are downloaded from the ConfigCat CDN, plus all feature flags & settings that are loaded from local-override sources. If a feature flag or a setting is defined both in the downloaded and the local-override source then the downloaded version will take precedence.

You can set up the SDK to load your feature flag & setting overrides from a `{ [key: string]: boolean | string | number }` object<!-- --> or from a custom flag override data source.

### Map[​](#map "Direct link to Map")

You can specify simple feature flag & setting overrides using a `{ [key: string]: boolean | string | number }` map.

```
const configCatClient = configcat.getClient(
  '#YOUR-SDK-KEY#',
  configcat.PollingMode.AutoPoll,
  {
    flagOverrides: configcat.createFlagOverridesFromMap(
      {
        enabledFeature: true,
        disabledFeature: false,
        intSetting: 5,
        doubleSetting: 3.14,
        stringSetting: 'test',
      },
      configcat.OverrideBehaviour.LocalOnly,
    ),
  },
);
```

<!-- -->

### Custom data source implementation[​](#custom-data-source-implementation "Direct link to Custom data source implementation")

You can create a custom flag override data source by implementing `IOverrideDataSource`.

The SDK provides the `createSettingFromValue` function to create `Setting` objects from simple `boolean`, `string` and `number` values. In case you need complex (full-featured) flag overrides, you can use the `deserializeConfig` function to obtain `Setting` objects from a config JSON conforming to the [config JSON v6 format](https://github.com/configcat/config-json/blob/main/V6/config.schema.json).

```
class MyCustomOverrideDataSource implements IOverrideDataSource {
  private settings: Record<string, Setting>;

  constructor(configJson: string) {
    this.settings = deserializeConfig(configJson).f ?? {};
  }

  getOverrides(): Record<string, Setting> {
    return this.settings;
  }
}
```

or

```
function MyCustomOverrideDataSource(configJson) {
  this.settings = deserializeConfig(configJson).f ?? {};
}

MyCustomOverrideDataSource.prototype.getOverrides = function () {
  return this.settings;
};
```

then

```
// Set the `MyCustomOverrideDataSource` implementation on client creation.
const configCatClient = configcat.getClient(
  '#YOUR-SDK-KEY#',
  configcat.PollingMode.AutoPoll,
  {
    flagOverrides: {
      dataSource: new MyCustomOverrideDataSource('{ "f": { ... } }'),
      behaviour: configcat.OverrideBehaviour.LocalOnly,
    }
  },
);
```

## Logging[​](#logging "Direct link to Logging")

### Setting log levels[​](#setting-log-levels "Direct link to Setting log levels")

```
const configCatClient = configcat.getClient(
  '#YOUR-SDK-KEY#',
  configcat.PollingMode.AutoPoll,
  {
    logger: configcat.createConsoleLogger(configcat.LogLevel.Info), // Setting log level to Info
  },
);
```

Available log levels:

| Level | Description                                             |
| ----- | ------------------------------------------------------- |
| Off   | Nothing gets logged.                                    |
| Error | Only error level events are logged.                     |
| Warn  | Default. Errors and Warnings are logged.                |
| Info  | Errors, Warnings and feature flag evaluation is logged. |
| Debug | All of the above plus debug info is logged.             |

Info level logging helps to inspect the feature flag evaluation process:

```
ConfigCat - INFO - [5000] Evaluating 'isPOCFeatureEnabled' for User '{"Identifier":"#SOME-USER-ID#","Email":"configcat@example.com"}'
  Evaluating targeting rules and applying the first match if any:
  - IF User.Email CONTAINS ANY OF ['@something.com'] THEN 'false' => no match
  - IF User.Email CONTAINS ANY OF ['@example.com'] THEN 'true' => MATCH, applying rule
  Returning 'true'.
```

### Custom logger implementation[​](#custom-logger-implementation "Direct link to Custom logger implementation")

The SDK provides a simple logger implementation that logs to [the debugging console](https://developer.mozilla.org/en-US/docs/Web/API/console) (`configcat.createConsoleLogger(...)`) but it also allows you to inject any custom implementation of `IConfigCatLogger`.

```
class MyCustomLogger implements IConfigCatLogger {
  /**
   * Writes an event into the log.
   * @param level Event severity level.
   * @param eventId Event identifier.
   * @param message Message.
   * @param exception The exception object related to the message (if any).
   */
  log(
    level: LogLevel,
    eventId: LogEventId,
    message: LogMessage,
    exception?: any,
  ): void {
    // insert your custom log logic
  }
}
```

or

```
function MyCustomLogger() {}

MyCustomLogger.prototype.log = function (level, eventId, message, exception) {
  // insert your custom log logic
};
```

then

```
// Set the `MyCustomLogger` implementation on client creation.
const configCatClient = configcat.getClient(
  '#YOUR-SDK-KEY#',
  configcat.PollingMode.AutoPoll,
  {
    logger: new MyCustomLogger(),
  },
);
```

### Log Filtering[​](#log-filtering "Direct link to Log Filtering")

You can define a custom log filter by providing a callback function via the `logFilter` option. The callback will be called by the *ConfigCat SDK* each time a log event occurs (and the event passes the minimum log level specified by the `IConfigCatLogger.level` property). That is, the callback allows you to filter log events by `level`, `eventId`, `message` or `exception`. The formatted message string can be obtained via `message.toString()`. If the callback function returns `true`, the event will be logged, otherwise it will be skipped.

```
// Filter out events with id 1001 from the log.
const logFilter = (level, eventId, message, exception) => eventId != 1001;

const configCatClient = configcat.getClient(
  "#YOUR-SDK-KEY#",
  configcat.PollingMode.AutoPoll,
  {
    logFilter: logFilter
  }
);
```

caution

Please make sure that your log filter logic doesn't perform heavy computation. A complex or incorrectly implemented log filter can degrade the performance of the SDK.

## `getAllKeysAsync()`[​](#getallkeysasync "Direct link to getallkeysasync")

You can get the keys for all available feature flags and settings by calling the `getAllKeysAsync()` method.

```
const configCatClient = configcat.getClient('#YOUR-SDK-KEY#');

const keys = await configCatClient.getAllKeysAsync();
console.log(keys);
```

## `getAllValuesAsync()`[​](#getallvaluesasync "Direct link to getallvaluesasync")

Evaluates and returns the values of all feature flags and settings. Passing a [User Object](#user-object) is optional.

```
const configCatClient = configcat.getClient('#YOUR-SDK-KEY#');

let settingValues = await configCatClient.getAllValuesAsync();
settingValues.forEach((i) =>
  console.log(i.settingKey + ' -> ' + i.settingValue),
);

// invoke with User Object
const userObject = { identifier: 'john@example.com' };

settingValues = await configCatClient.getAllValuesAsync(userObject);
settingValues.forEach((i) =>
  console.log(i.settingKey + ' -> ' + i.settingValue),
);
```

## `getAllValueDetailsAsync()`[​](#getallvaluedetailsasync "Direct link to getallvaluedetailsasync")

Evaluates and returns the values along with evaluation details of all feature flags and settings. Passing a [User Object](#user-object) is optional.

```
const configCatClient = configcat.getClient('#YOUR-SDK-KEY#');

let settingValues = await configCatClient.getAllValueDetailsAsync();
settingValues.forEach((details) => console.log(details));

// invoke with User Object
const userObject = { identifier: 'john@example.com' };

settingValues = await configCatClient.getAllValueDetailsAsync(userObject);
settingValues.forEach((details) => console.log(details));
```

## Using custom cache implementation[​](#using-custom-cache-implementation "Direct link to Using custom cache implementation")

The *ConfigCat SDK* stores the downloaded config data in a local cache to minimize network traffic and enhance client performance. If you prefer to use your own cache solution, such as an external or distributed cache in your system, you can implement the [`IConfigCatCache`](https://github.com/configcat/js-unified-sdk/blob/master/src/ConfigCatCache.ts) interface and set the `cache` property in the options passed to `getClient`. This allows you to seamlessly integrate ConfigCat with your existing caching infrastructure.

```
class MyCustomCache implements IConfigCatCache {
  set(key: string, value: string): Promise<void> | void {
    // insert your cache write logic here
  }

  get(
    key: string,
  ): Promise<string | null | undefined> | string | null | undefined {
    // insert your cache read logic here
  }
}
```

or

```
function MyCustomCache() {}

MyCustomCache.prototype.set = function (key, value) {
  // insert your cache write logic here
};
MyCustomCache.prototype.get = function (key) {
  // insert your cache read logic here
};
```

then

```
// Set the `MyCustomCache` implementation on client creation.
const configCatClient = configcat.getClient(
  '#YOUR-SDK-KEY#',
  configcat.PollingMode.AutoPoll,
  {
    cache: new MyCustomCache(),
  },
);
```

info

The JavaScript SDK supports *shared caching*. You can read more about this feature and the required minimum SDK versions [here](https://configcat.com/docs/docs/advanced/caching/.md#shared-cache).

## Using ConfigCat behind a proxy[​](#using-configcat-behind-a-proxy "Direct link to Using ConfigCat behind a proxy")

It is possible to set up the SDK to route HTTP requests through a HTTP, HTTPS or SOCKS proxy.

```
npm i https-proxy-agent
```

```
import { HttpsProxyAgent } from 'https-proxy-agent';

const configCatClient = configcat.getClient(
  '#YOUR-SDK-KEY#',
  configcat.PollingMode.AutoPoll,
  {
    httpsAgent: new HttpsProxyAgent("http://192.168.1.1:8080"),
  },
);
```

info

By default, you need to specify the `httpsAgent` option because the SDK always uses HTTPS to access the ConfigCat CDN. However, if you set the `baseUrl` to a `http://...` URL, you will need to install `http-proxy-agent` and set the `httpAgent` option instead.

## Sensitive information handling[​](#sensitive-information-handling "Direct link to Sensitive information handling")

The frontend/mobile SDKs are running in your users' browsers/devices. The SDK is downloading a [config JSON](https://configcat.com/docs/docs/requests/.md) file from ConfigCat's CDN servers. The URL path for this config JSON file contains your SDK key, so the SDK key and the content of your config JSON file (feature flag keys, feature flag values, Targeting Rules, % rules) can be visible to your users. In ConfigCat, all SDK keys are read-only. They only allow downloading your config JSON files, but nobody can make any changes with them in your ConfigCat account.

If you do not want to expose the SDK key or the content of the config JSON file, we recommend using the SDK in your backend components only. You can always create a backend endpoint using the *ConfigCat SDK* that can evaluate feature flags for a specific user, and call that backend endpoint from your frontend/mobile applications.

Also, we recommend using [confidential targeting comparators](https://configcat.com/docs/docs/targeting/targeting-rule/user-condition/.md#confidential-text-comparators) in the Targeting Rules of those feature flags that are used in the frontend/mobile SDKs.

## Platform compatibility[​](#platform-compatibility "Direct link to Platform compatibility")

<!-- -->

The SDK should be compatible with newer versions of Bun.

The SDK is [tested](https://github.com/configcat/js-unified-sdk/blob/master/.github/workflows/js-sdk-ci.yml) against the following <!-- -->runtimes<!-- -->:

* Bun (v1.1.0, latest stable) on Windows / Ubuntu / macOS

The SDK is compatible with TypeScript v4.0.2 or newer. Earlier versions may work but those are not tested, thus, not supported officially.

These tests are running on each pull request, before each deploy, and on a daily basis.

You can view a sample run [here](https://github.com/configcat/js-unified-sdk/actions/runs/11745259578).

<!-- -->

## Sample Applications[​](#sample-applications "Direct link to Sample Applications")

<!-- -->

<!-- -->

<!-- -->

* [Sample Bun console application](https://github.com/configcat/js-unified-sdk/tree/master/samples/bun-console)

<!-- -->

<!-- -->

<!-- -->

## Look under the hood[​](#look-under-the-hood "Direct link to Look under the hood")

* [ConfigCat SDK for JavaScript on GitHub](https://github.com/configcat/js-unified-sdk)
* [ConfigCat SDK for JavaScript in NPM](https://www.npmjs.com/package/@configcat/sdk)
