# Source: https://firebase.google.com/docs/reference/js/remote-config.md.txt

# remote-config package

The Firebase Remote Config Web SDK. This SDK does not work in a Node.js environment.

## Functions

| Function | Description |
|---|---|
| **function(app, ...)** |   |
| [getRemoteConfig(app, options)](https://firebase.google.com/docs/reference/js/remote-config.md#getremoteconfig_61d368f) |   |
| **function(remoteConfig, ...)** |   |
| [activate(remoteConfig)](https://firebase.google.com/docs/reference/js/remote-config.md#activate_722a192) | Makes the last fetched config available to the getters. |
| [ensureInitialized(remoteConfig)](https://firebase.google.com/docs/reference/js/remote-config.md#ensureinitialized_722a192) | Ensures the last activated config are available to the getters. |
| [fetchAndActivate(remoteConfig)](https://firebase.google.com/docs/reference/js/remote-config.md#fetchandactivate_722a192) | Performs fetch and activate operations, as a convenience. |
| [fetchConfig(remoteConfig)](https://firebase.google.com/docs/reference/js/remote-config.md#fetchconfig_722a192) | Fetches and caches configuration from the Remote Config service. |
| [getAll(remoteConfig)](https://firebase.google.com/docs/reference/js/remote-config.md#getall_722a192) | Gets all config. |
| [getBoolean(remoteConfig, key)](https://firebase.google.com/docs/reference/js/remote-config.md#getboolean_476c09f) | Gets the value for the given key as a boolean.Convenience method for calling `remoteConfig.getValue(key).asBoolean()`. |
| [getNumber(remoteConfig, key)](https://firebase.google.com/docs/reference/js/remote-config.md#getnumber_476c09f) | Gets the value for the given key as a number.Convenience method for calling `remoteConfig.getValue(key).asNumber()`. |
| [getString(remoteConfig, key)](https://firebase.google.com/docs/reference/js/remote-config.md#getstring_476c09f) | Gets the value for the given key as a string. Convenience method for calling `remoteConfig.getValue(key).asString()`. |
| [getValue(remoteConfig, key)](https://firebase.google.com/docs/reference/js/remote-config.md#getvalue_476c09f) | Gets the [Value](https://firebase.google.com/docs/reference/js/remote-config.value.md#value_interface) for the given key. |
| [onConfigUpdate(remoteConfig, observer)](https://firebase.google.com/docs/reference/js/remote-config.md#onconfigupdate_8b13b26) | Starts listening for real-time config updates from the Remote Config backend and automatically fetches updates from the Remote Config backend when they are available. |
| [setCustomSignals(remoteConfig, customSignals)](https://firebase.google.com/docs/reference/js/remote-config.md#setcustomsignals_aeeb95e) | Sets the custom signals for the app instance. |
| [setLogLevel(remoteConfig, logLevel)](https://firebase.google.com/docs/reference/js/remote-config.md#setloglevel_039a45b) | Defines the log level to use. |
| **function()** |   |
| [isSupported()](https://firebase.google.com/docs/reference/js/remote-config.md#issupported) | This method provides two different checks:1. Check if IndexedDB exists in the browser environment. 2. Check if the current browser context allows IndexedDB `open()` calls. |

## Interfaces

| Interface | Description |
|---|---|
| [ConfigUpdate](https://firebase.google.com/docs/reference/js/remote-config.configupdate.md#configupdate_interface) | Contains information about which keys have been updated. |
| [ConfigUpdateObserver](https://firebase.google.com/docs/reference/js/remote-config.configupdateobserver.md#configupdateobserver_interface) | Observer interface for receiving real-time Remote Config update notifications.NOTE: Although an `complete` callback can be provided, it will never be called because the ConfigUpdate stream is never-ending. |
| [CustomSignals](https://firebase.google.com/docs/reference/js/remote-config.customsignals.md#customsignals_interface) | Defines the type for representing custom signals and their values. The values in CustomSignals must be one of the following types: - `string` - `number` - `null` |
| [FetchResponse](https://firebase.google.com/docs/reference/js/remote-config.fetchresponse.md#fetchresponse_interface) | Defines a successful response (200 or 304). Modeled after the native `Response` interface, but simplified for Remote Config's use case. |
| [FirebaseExperimentDescription](https://firebase.google.com/docs/reference/js/remote-config.firebaseexperimentdescription.md#firebaseexperimentdescription_interface) | Defines experiment and variant attached to a config parameter. |
| [FirebaseRemoteConfigObject](https://firebase.google.com/docs/reference/js/remote-config.firebaseremoteconfigobject.md#firebaseremoteconfigobject_interface) | Defines a self-descriptive reference for config key-value pairs. |
| [RemoteConfig](https://firebase.google.com/docs/reference/js/remote-config.remoteconfig.md#remoteconfig_interface) | The Firebase Remote Config service interface. |
| [RemoteConfigOptions](https://firebase.google.com/docs/reference/js/remote-config.remoteconfigoptions.md#remoteconfigoptions_interface) | Options for Remote Config initialization. |
| [RemoteConfigSettings](https://firebase.google.com/docs/reference/js/remote-config.remoteconfigsettings.md#remoteconfigsettings_interface) | Defines configuration options for the Remote Config SDK. |
| [Value](https://firebase.google.com/docs/reference/js/remote-config.value.md#value_interface) | Wraps a value with metadata and type-safe getters. |

## Type Aliases

| Type Alias | Description |
|---|---|
| [FetchStatus](https://firebase.google.com/docs/reference/js/remote-config.md#fetchstatus) | Summarizes the outcome of the last attempt to fetch config from the Firebase Remote Config server. - "no-fetch-yet" indicates the [RemoteConfig](https://firebase.google.com/docs/reference/js/remote-config.remoteconfig.md#remoteconfig_interface) instance has not yet attempted to fetch config, or that SDK initialization is incomplete. - "success" indicates the last attempt succeeded. - "failure" indicates the last attempt failed. - "throttle" indicates the last attempt was rate-limited. |
| [FetchType](https://firebase.google.com/docs/reference/js/remote-config.md#fetchtype) | Indicates the type of fetch request. - "BASE" indicates a standard fetch request. - "REALTIME" indicates a fetch request triggered by a real-time update. |
| [LogLevel](https://firebase.google.com/docs/reference/js/remote-config.md#loglevel) | Defines levels of Remote Config logging. |
| [Unsubscribe](https://firebase.google.com/docs/reference/js/remote-config.md#unsubscribe) | A function that unsubscribes from a real-time event stream. |
| [ValueSource](https://firebase.google.com/docs/reference/js/remote-config.md#valuesource) | Indicates the source of a value. - "static" indicates the value was defined by a static constant. - "default" indicates the value was defined by default config. - "remote" indicates the value was defined by fetched config. |

## function(app, ...)

### getRemoteConfig(app, options)

**Signature:**

    export declare function getRemoteConfig(app?: FirebaseApp, options?: RemoteConfigOptions): RemoteConfig;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| app | [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface) | The [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface) instance. |
| options | [RemoteConfigOptions](https://firebase.google.com/docs/reference/js/remote-config.remoteconfigoptions.md#remoteconfigoptions_interface) | Optional. The [RemoteConfigOptions](https://firebase.google.com/docs/reference/js/remote-config.remoteconfigoptions.md#remoteconfigoptions_interface) with which to instantiate the Remote Config instance. |

**Returns:**

[RemoteConfig](https://firebase.google.com/docs/reference/js/remote-config.remoteconfig.md#remoteconfig_interface)

A [RemoteConfig](https://firebase.google.com/docs/reference/js/remote-config.remoteconfig.md#remoteconfig_interface) instance.

## function(remoteConfig, ...)

### activate(remoteConfig)

Makes the last fetched config available to the getters.

**Signature:**

    export declare function activate(remoteConfig: RemoteConfig): Promise<boolean>;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| remoteConfig | [RemoteConfig](https://firebase.google.com/docs/reference/js/remote-config.remoteconfig.md#remoteconfig_interface) | The [RemoteConfig](https://firebase.google.com/docs/reference/js/remote-config.remoteconfig.md#remoteconfig_interface) instance. |

**Returns:**

Promise\<boolean\>

A `Promise` which resolves to true if the current call activated the fetched configs. If the fetched configs were already activated, the `Promise` will resolve to false.

### ensureInitialized(remoteConfig)

Ensures the last activated config are available to the getters.

**Signature:**

    export declare function ensureInitialized(remoteConfig: RemoteConfig): Promise<void>;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| remoteConfig | [RemoteConfig](https://firebase.google.com/docs/reference/js/remote-config.remoteconfig.md#remoteconfig_interface) | The [RemoteConfig](https://firebase.google.com/docs/reference/js/remote-config.remoteconfig.md#remoteconfig_interface) instance. |

**Returns:**

Promise\<void\>

A `Promise` that resolves when the last activated config is available to the getters.

### fetchAndActivate(remoteConfig)

Performs fetch and activate operations, as a convenience.

**Signature:**

    export declare function fetchAndActivate(remoteConfig: RemoteConfig): Promise<boolean>;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| remoteConfig | [RemoteConfig](https://firebase.google.com/docs/reference/js/remote-config.remoteconfig.md#remoteconfig_interface) | The [RemoteConfig](https://firebase.google.com/docs/reference/js/remote-config.remoteconfig.md#remoteconfig_interface) instance. |

**Returns:**

Promise\<boolean\>

A `Promise` which resolves to true if the current call activated the fetched configs. If the fetched configs were already activated, the `Promise` will resolve to false.

### fetchConfig(remoteConfig)

Fetches and caches configuration from the Remote Config service.

**Signature:**

    export declare function fetchConfig(remoteConfig: RemoteConfig): Promise<void>;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| remoteConfig | [RemoteConfig](https://firebase.google.com/docs/reference/js/remote-config.remoteconfig.md#remoteconfig_interface) | The [RemoteConfig](https://firebase.google.com/docs/reference/js/remote-config.remoteconfig.md#remoteconfig_interface) instance. |

**Returns:**

Promise\<void\>

### getAll(remoteConfig)

Gets all config.

**Signature:**

    export declare function getAll(remoteConfig: RemoteConfig): Record<string, Value>;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| remoteConfig | [RemoteConfig](https://firebase.google.com/docs/reference/js/remote-config.remoteconfig.md#remoteconfig_interface) | The [RemoteConfig](https://firebase.google.com/docs/reference/js/remote-config.remoteconfig.md#remoteconfig_interface) instance. |

**Returns:**

Record\<string, [Value](https://firebase.google.com/docs/reference/js/remote-config.value.md#value_interface)\>

All config.

### getBoolean(remoteConfig, key)

Gets the value for the given key as a boolean.

Convenience method for calling `remoteConfig.getValue(key).asBoolean()`.

**Signature:**

    export declare function getBoolean(remoteConfig: RemoteConfig, key: string): boolean;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| remoteConfig | [RemoteConfig](https://firebase.google.com/docs/reference/js/remote-config.remoteconfig.md#remoteconfig_interface) | The [RemoteConfig](https://firebase.google.com/docs/reference/js/remote-config.remoteconfig.md#remoteconfig_interface) instance. |
| key | string | The name of the parameter. |

**Returns:**

boolean

The value for the given key as a boolean.

### getNumber(remoteConfig, key)

Gets the value for the given key as a number.

Convenience method for calling `remoteConfig.getValue(key).asNumber()`.

**Signature:**

    export declare function getNumber(remoteConfig: RemoteConfig, key: string): number;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| remoteConfig | [RemoteConfig](https://firebase.google.com/docs/reference/js/remote-config.remoteconfig.md#remoteconfig_interface) | The [RemoteConfig](https://firebase.google.com/docs/reference/js/remote-config.remoteconfig.md#remoteconfig_interface) instance. |
| key | string | The name of the parameter. |

**Returns:**

number

The value for the given key as a number.

### getString(remoteConfig, key)

Gets the value for the given key as a string. Convenience method for calling `remoteConfig.getValue(key).asString()`.

**Signature:**

    export declare function getString(remoteConfig: RemoteConfig, key: string): string;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| remoteConfig | [RemoteConfig](https://firebase.google.com/docs/reference/js/remote-config.remoteconfig.md#remoteconfig_interface) | The [RemoteConfig](https://firebase.google.com/docs/reference/js/remote-config.remoteconfig.md#remoteconfig_interface) instance. |
| key | string | The name of the parameter. |

**Returns:**

string

The value for the given key as a string.

### getValue(remoteConfig, key)

Gets the [Value](https://firebase.google.com/docs/reference/js/remote-config.value.md#value_interface) for the given key.

**Signature:**

    export declare function getValue(remoteConfig: RemoteConfig, key: string): Value;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| remoteConfig | [RemoteConfig](https://firebase.google.com/docs/reference/js/remote-config.remoteconfig.md#remoteconfig_interface) | The [RemoteConfig](https://firebase.google.com/docs/reference/js/remote-config.remoteconfig.md#remoteconfig_interface) instance. |
| key | string | The name of the parameter. |

**Returns:**

[Value](https://firebase.google.com/docs/reference/js/remote-config.value.md#value_interface)

The value for the given key.

### onConfigUpdate(remoteConfig, observer)

Starts listening for real-time config updates from the Remote Config backend and automatically fetches updates from the Remote Config backend when they are available.

If a connection to the Remote Config backend is not already open, calling this method will open it. Multiple listeners can be added by calling this method again, but subsequent calls re-use the same connection to the backend.

**Signature:**

    export declare function onConfigUpdate(remoteConfig: RemoteConfig, observer: ConfigUpdateObserver): Unsubscribe;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| remoteConfig | [RemoteConfig](https://firebase.google.com/docs/reference/js/remote-config.remoteconfig.md#remoteconfig_interface) | The [RemoteConfig](https://firebase.google.com/docs/reference/js/remote-config.remoteconfig.md#remoteconfig_interface) instance. |
| observer | [ConfigUpdateObserver](https://firebase.google.com/docs/reference/js/remote-config.configupdateobserver.md#configupdateobserver_interface) | The [ConfigUpdateObserver](https://firebase.google.com/docs/reference/js/remote-config.configupdateobserver.md#configupdateobserver_interface) to be notified of config updates. |

**Returns:**

[Unsubscribe](https://firebase.google.com/docs/reference/js/remote-config.md#unsubscribe)

An [Unsubscribe](https://firebase.google.com/docs/reference/js/remote-config.md#unsubscribe) function to remove the listener.

### setCustomSignals(remoteConfig, customSignals)

Sets the custom signals for the app instance.

**Signature:**

    export declare function setCustomSignals(remoteConfig: RemoteConfig, customSignals: CustomSignals): Promise<void>;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| remoteConfig | [RemoteConfig](https://firebase.google.com/docs/reference/js/remote-config.remoteconfig.md#remoteconfig_interface) | The [RemoteConfig](https://firebase.google.com/docs/reference/js/remote-config.remoteconfig.md#remoteconfig_interface) instance. |
| customSignals | [CustomSignals](https://firebase.google.com/docs/reference/js/remote-config.customsignals.md#customsignals_interface) | Map (key, value) of the custom signals to be set for the app instance. If a key already exists, the value is overwritten. Setting the value of a custom signal to null unsets the signal. The signals will be persisted locally on the client. |

**Returns:**

Promise\<void\>

### setLogLevel(remoteConfig, logLevel)

Defines the log level to use.

**Signature:**

    export declare function setLogLevel(remoteConfig: RemoteConfig, logLevel: RemoteConfigLogLevel): void;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| remoteConfig | [RemoteConfig](https://firebase.google.com/docs/reference/js/remote-config.remoteconfig.md#remoteconfig_interface) | The [RemoteConfig](https://firebase.google.com/docs/reference/js/remote-config.remoteconfig.md#remoteconfig_interface) instance. |
| logLevel | [RemoteConfigLogLevel](https://firebase.google.com/docs/reference/js/remote-config.md#loglevel) | The log level to set. |

**Returns:**

void

## function()

### isSupported()

This method provides two different checks:

1. Check if IndexedDB exists in the browser environment. 2. Check if the current browser context allows IndexedDB `open()` calls.

**Signature:**

    export declare function isSupported(): Promise<boolean>;

**Returns:**

Promise\<boolean\>

A `Promise` which resolves to true if a [RemoteConfig](https://firebase.google.com/docs/reference/js/remote-config.remoteconfig.md#remoteconfig_interface) instance can be initialized in this environment, or false if it cannot.

## FetchStatus

Summarizes the outcome of the last attempt to fetch config from the Firebase Remote Config server.

- "no-fetch-yet" indicates the \[RemoteConfig\](./remote-config.remoteconfig.md#remoteconfig_interface) instance has not yet attempted to fetch config, or that SDK initialization is incomplete.
- "success" indicates the last attempt succeeded.
- "failure" indicates the last attempt failed.
- "throttle" indicates the last attempt was rate-limited.

**Signature:**

    export type FetchStatus = 'no-fetch-yet' | 'success' | 'failure' | 'throttle';

## FetchType

Indicates the type of fetch request.

- "BASE" indicates a standard fetch request.
- "REALTIME" indicates a fetch request triggered by a real-time update.

**Signature:**

    export type FetchType = 'BASE' | 'REALTIME';

## LogLevel

Defines levels of Remote Config logging.

**Signature:**

    export type LogLevel = 'debug' | 'error' | 'silent';

## Unsubscribe

A function that unsubscribes from a real-time event stream.

**Signature:**

    export type Unsubscribe = () => void;

## ValueSource

Indicates the source of a value.

- "static" indicates the value was defined by a static constant.
- "default" indicates the value was defined by default config.
- "remote" indicates the value was defined by fetched config.

**Signature:**

    export type ValueSource = 'static' | 'default' | 'remote';