# Source: https://rolldown.rs/reference/Interface.MinimalPluginContext.md

---
url: /reference/Interface.MinimalPluginContext.md
---
# Interface: MinimalPluginContext

## Extended by

* [`PluginContext`](Interface.PluginContext.md)

## Properties

### meta

* **Type**: [`PluginContextMeta`](Interface.PluginContextMeta.md)

An object containing potentially useful metadata.

## Logging Methods

### debug()

* **Type**: (`log`) => `void`

Generate a `"debug"` level log.

[`code`](Interface.RolldownError.md#code) will be set to `"PLUGIN_LOG"` by Rolldown.
Make sure to add a distinctive [`pluginCode`](Interface.RolldownError.md#plugincode) to
those logs for easy filtering.

These logs are only processed if the [`logLevel`](/reference/InputOptions.logLevel) option is explicitly set to `"debug"`, otherwise it does nothing. Therefore, it is encouraged to add helpful debug logs to plugins as that can help spot issues while they will be efficiently muted by default.

::: tip Lazily Compute

If you need to do expensive computations to generate the log, make sure to use the function form so that these computations are only performed if the log is actually processed.

```js
function plugin() {
  return {
    name: 'test',
    transform(code, id) {
      this.debug(
        () => `transforming ${id},\n` + `module contains, ${code.split('\n').length} lines`,
      );
    },
  };
}
```

:::

#### Parameters

##### log

The log object or message.

The string argument is equivalent to passing an object with only the
[`message`](Interface.RolldownError.md#message) property.

`string` | [`RolldownLog`](Interface.RolldownLog.md) | () => `string` | [`RolldownLog`](Interface.RolldownLog.md)

#### Returns

`void`

***

### error()

* **Type**: (`e`) => `never`

Similar to [`this.warn`](#warn), except that it will also abort
the bundling process with an error.

If an Error instance is passed, it will be used as-is, otherwise a new Error
instance will be created with the given error message and all additional
provided properties.

In all hooks except the [`onLog`](Interface.Plugin.md#onlog) hook, the error will
be augmented with [`code: "PLUGIN_ERROR"`](Interface.RolldownError.md#code) and
[`plugin: plugin.name`](Interface.RolldownError.md#plugin) properties.
If a `code` property already exists and the code does not start with `PLUGIN_`,
it will be renamed to [`pluginCode`](Interface.RolldownError.md#plugincode).

#### Parameters

##### e

`string` | [`RolldownError`](Interface.RolldownError.md)

#### Returns

`never`

***

### info()

* **Type**: (`log`) => `void`

Generate a `"info"` level log.

[`code`](Interface.RolldownError.md#code) will be set to `"PLUGIN_LOG"` by Rolldown.
As these logs are displayed by default, use them for information that is not a warning
but makes sense to display to all users on every build.

If the [`logLevel`](/reference/InputOptions.logLevel) option is set to `"warn"` or `"silent"`, this method will do nothing.

#### Parameters

##### log

The log object or message.

The string argument is equivalent to passing an object with only the
[`message`](Interface.RolldownError.md#message) property.

`string` | [`RolldownLog`](Interface.RolldownLog.md) | () => `string` | [`RolldownLog`](Interface.RolldownLog.md)

#### Returns

`void`

***

### warn()

* **Type**: (`log`) => `void`

Generate a `"warn"` level log.

Just like internally generated warnings, these logs will be first passed to and
filtered by plugin [`onLog`](Interface.Plugin.md#onlog) hooks before they are forwarded
to custom [`onLog`](Interface.InputOptions.md#onlog) or
[`onwarn`](Interface.InputOptions.md#onwarn) handlers or printed to the console.

We encourage you to use objects with a [`pluginCode`](Interface.RolldownError.md#plugincode)
property as that will allow users to easily filter for those logs in an `onLog` handler.

If you need to add additional information, you can use the [`meta`](/reference/Interface.RolldownLog#meta) property. If the log contains a [`code`](/reference/Interface.RolldownLog#code) and does not yet have a [`pluginCode`](/reference/Interface.RolldownLog#plugincode) property, it will be renamed to [`pluginCode`](/reference/Interface.RolldownLog#plugincode) as plugin warnings always get a code of `PLUGIN_WARNING` added by Rolldown.

If the logLevel option is set to `"silent"`, this method will do nothing.

::: tip Lazily Compute

If you need to do expensive computations to generate the log, make sure to use the function form so that these computations are only performed if the log is actually processed.

:::

#### Parameters

##### log

The log object or message.

The string argument is equivalent to passing an object with only the
[`message`](Interface.RolldownError.md#message) property.

`string` | [`RolldownLog`](Interface.RolldownLog.md) | () => `string` | [`RolldownLog`](Interface.RolldownLog.md)

#### Returns

`void`
