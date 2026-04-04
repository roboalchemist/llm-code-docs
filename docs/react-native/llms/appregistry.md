# Source: https://reactnative.dev/docs/appregistry.md

# AppRegistry

### Project with Native Code Required

If you are using the managed Expo workflow there is only ever one entry component registered with `AppRegistry` and it is handled automatically (or through [registerRootComponent](https://docs.expo.dev/versions/latest/sdk/register-root-component/)). You do not need to use this API.

`AppRegistry` is the JS entry point to running all React Native apps. App root components should register themselves with `AppRegistry.registerComponent`, then the native system can load the bundle for the app and then actually run the app when it's ready by invoking `AppRegistry.runApplication`.

tsx

```
import {Text, AppRegistry} from 'react-native';

const App = () => (
  <View>
    <Text>App1</Text>
  </View>
);

AppRegistry.registerComponent('Appname', () => App);
```

To "stop" an application when a view should be destroyed, call `AppRegistry.unmountApplicationComponentAtRootTag` with the tag that was passed into `runApplication`. These should always be used as a pair.

`AppRegistry` should be required early in the `require` sequence to make sure the JS execution environment is setup before other modules are required.

***

# Reference

## Methods[​](#methods "Direct link to Methods")

### `getAppKeys()`[​](#getappkeys "Direct link to getappkeys")

tsx

```
static getAppKeys(): string[];
```

Returns an array of strings.

***

### `getRegistry()`[​](#getregistry "Direct link to getregistry")

tsx

```
static getRegistry(): {sections: string[]; runnables: Runnable[]};
```

Returns a [Registry](/docs/appregistry.md#registry) object.

***

### `getRunnable()`[​](#getrunnable "Direct link to getrunnable")

tsx

```
static getRunnable(appKey: string): : Runnable | undefined;
```

Returns a [Runnable](/docs/appregistry.md#runnable) object.

**Parameters:**

| Name           | Type   |
| -------------- | ------ |
| appKeyRequired | string |

***

### `getSectionKeys()`[​](#getsectionkeys "Direct link to getsectionkeys")

tsx

```
static getSectionKeys(): string[];
```

Returns an array of strings.

***

### `getSections()`[​](#getsections "Direct link to getsections")

tsx

```
static getSections(): Record<string, Runnable>;
```

Returns a [Runnables](/docs/appregistry.md#runnables) object.

***

### `registerCancellableHeadlessTask()`[​](#registercancellableheadlesstask "Direct link to registercancellableheadlesstask")

tsx

```
static registerCancellableHeadlessTask(
  taskKey: string,
  taskProvider: TaskProvider,
  taskCancelProvider: TaskCancelProvider,
);
```

Register a headless task which can be cancelled. A headless task is a bit of code that runs without a UI.

**Parameters:**

| Name                             | Type                                                          | Description                                                                                                                                                                                                                         |
| -------------------------------- | ------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| taskKey<br />Required            | string                                                        | The native id for this task instance that was used when startHeadlessTask was called.                                                                                                                                               |
| taskProvider<br />Required       | [TaskProvider](/docs/appregistry.md#taskprovider)             | A promise returning function that takes some data passed from the native side as the only argument. When the promise is resolved or rejected the native side is notified of this event and it may decide to destroy the JS context. |
| taskCancelProvider<br />Required | [TaskCancelProvider](/docs/appregistry.md#taskcancelprovider) | a void returning function that takes no arguments; when a cancellation is requested, the function being executed by taskProvider should wrap up and return ASAP.                                                                    |

***

### `registerComponent()`[​](#registercomponent "Direct link to registercomponent")

tsx

```
static registerComponent(
  appKey: string,
  getComponentFunc: ComponentProvider,
  section?: boolean,
): string;
```

**Parameters:**

| Name                      | Type              |
| ------------------------- | ----------------- |
| appKeyRequired            | string            |
| componentProviderRequired | ComponentProvider |
| section                   | boolean           |

***

### `registerConfig()`[​](#registerconfig "Direct link to registerconfig")

tsx

```
static registerConfig(config: AppConfig[]);
```

**Parameters:**

| Name           | Type                                           |
| -------------- | ---------------------------------------------- |
| configRequired | [AppConfig](/docs/appregistry.md#appconfig)\[] |

***

### `registerHeadlessTask()`[​](#registerheadlesstask "Direct link to registerheadlesstask")

tsx

```
static registerHeadlessTask(
  taskKey: string,
  taskProvider: TaskProvider,
);
```

Register a headless task. A headless task is a bit of code that runs without a UI.

This is a way to run tasks in JavaScript while your app is in the background. It can be used, for example, to sync fresh data, handle push notifications, or play music.

**Parameters:**

| Name                 | Type                                              | Description                                                                                                                                                                                                                         |
| -------------------- | ------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| taskKeyRequired      | string                                            | The native id for this task instance that was used when startHeadlessTask was called.                                                                                                                                               |
| taskProviderRequired | [TaskProvider](/docs/appregistry.md#taskprovider) | A promise returning function that takes some data passed from the native side as the only argument. When the promise is resolved or rejected the native side is notified of this event and it may decide to destroy the JS context. |

***

### `registerRunnable()`[​](#registerrunnable "Direct link to registerrunnable")

tsx

```
static registerRunnable(appKey: string, func: Runnable): string;
```

**Parameters:**

| Name           | Type     |
| -------------- | -------- |
| appKeyRequired | string   |
| runRequired    | function |

***

### `registerSection()`[​](#registersection "Direct link to registersection")

tsx

```
static registerSection(
  appKey: string,
  component: ComponentProvider,
);
```

**Parameters:**

| Name              | Type              |
| ----------------- | ----------------- |
| appKeyRequired    | string            |
| componentRequired | ComponentProvider |

***

### `runApplication()`[​](#runapplication "Direct link to runapplication")

tsx

```
static runApplication(appKey: string, appParameters: any): void;
```

Loads the JavaScript bundle and runs the app.

**Parameters:**

| Name                  | Type   |
| --------------------- | ------ |
| appKeyRequired        | string |
| appParametersRequired | any    |

***

### `setComponentProviderInstrumentationHook()`[​](#setcomponentproviderinstrumentationhook "Direct link to setcomponentproviderinstrumentationhook")

tsx

```
static setComponentProviderInstrumentationHook(
  hook: ComponentProviderInstrumentationHook,
);
```

**Parameters:**

| Name         | Type     |
| ------------ | -------- |
| hookRequired | function |

A valid `hook` function accepts the following as arguments:

| Name                            | Type               |
| ------------------------------- | ------------------ |
| componentRequired               | ComponentProvider  |
| scopedPerformanceLoggerRequired | IPerformanceLogger |

The function must also return a React Component.

***

### `setWrapperComponentProvider()`[​](#setwrappercomponentprovider "Direct link to setwrappercomponentprovider")

tsx

```
static setWrapperComponentProvider(
  provider: WrapperComponentProvider,
);
```

**Parameters:**

| Name             | Type              |
| ---------------- | ----------------- |
| providerRequired | ComponentProvider |

***

### `startHeadlessTask()`[​](#startheadlesstask "Direct link to startheadlesstask")

tsx

```
static startHeadlessTask(
  taskId: number,
  taskKey: string,
  data: any,
);
```

Only called from native code. Starts a headless task.

**Parameters:**

| Name            | Type   | Description                                                          |
| --------------- | ------ | -------------------------------------------------------------------- |
| taskIdRequired  | number | The native id for this task instance to keep track of its execution. |
| taskKeyRequired | string | The key for the task to start.                                       |
| dataRequired    | any    | The data to pass to the task.                                        |

***

### `unmountApplicationComponentAtRootTag()`[​](#unmountapplicationcomponentatroottag "Direct link to unmountapplicationcomponentatroottag")

tsx

```
static unmountApplicationComponentAtRootTag(rootTag: number);
```

Stops an application when a view should be destroyed.

**Parameters:**

| Name            | Type   |
| --------------- | ------ |
| rootTagRequired | number |

## Type Definitions[​](#type-definitions "Direct link to Type Definitions")

### AppConfig[​](#appconfig "Direct link to AppConfig")

Application configuration for the `registerConfig` method.

| Type   |
| ------ |
| object |

**Properties:**

| Name           | Type              |
| -------------- | ----------------- |
| appKeyRequired | string            |
| component      | ComponentProvider |
| run            | function          |
| section        | boolean           |

note

Every config is expected to set either `component` or `run` function.

### Registry[​](#registry "Direct link to Registry")

| Type   |
| ------ |
| object |

**Properties:**

| Name      | Type                                                |
| --------- | --------------------------------------------------- |
| runnables | array of [Runnables](/docs/appregistry.md#runnable) |
| sections  | array of strings                                    |

### Runnable[​](#runnable "Direct link to Runnable")

| Type   |
| ------ |
| object |

**Properties:**

| Name      | Type              |
| --------- | ----------------- |
| component | ComponentProvider |
| run       | function          |

### Runnables[​](#runnables "Direct link to Runnables")

An object with key of `appKey` and value of type of [`Runnable`](/docs/appregistry.md#runnable).

| Type   |
| ------ |
| object |

### Task[​](#task "Direct link to Task")

A `Task` is a function that accepts any data as argument and returns a Promise that resolves to `undefined`.

| Type     |
| -------- |
| function |

### TaskCanceller[​](#taskcanceller "Direct link to TaskCanceller")

A `TaskCanceller` is a function that accepts no argument and returns void.

| Type     |
| -------- |
| function |

### TaskCancelProvider[​](#taskcancelprovider "Direct link to TaskCancelProvider")

A valid `TaskCancelProvider` is a function that returns a [`TaskCanceller`](/docs/appregistry.md#taskcanceller).

| Type     |
| -------- |
| function |

### TaskProvider[​](#taskprovider "Direct link to TaskProvider")

A valid `TaskProvider` is a function that returns a [`Task`](/docs/appregistry.md#task).

| Type     |
| -------- |
| function |
