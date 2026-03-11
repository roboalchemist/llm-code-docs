# Source: https://rolldown.rs/reference/Interface.RolldownError.md

---
url: /reference/Interface.RolldownError.md
---
# Interface: RolldownError

## Extends

* [`RolldownLog`](Interface.RolldownLog.md)

## Properties

### binding?

* **Type**: `string`
* **Optional**

#### Inherited from

[`RolldownLog`](Interface.RolldownLog.md).[`binding`](Interface.RolldownLog.md#binding)

***

### cause?

* **Type**: `unknown`
* **Optional**

#### Inherited from

[`RolldownLog`](Interface.RolldownLog.md).[`cause`](Interface.RolldownLog.md#cause)

***

### code?

* **Type**: `string`
* **Optional**

The log code for this log object.

#### Example

```ts
'PLUGIN_ERROR'
```

#### Inherited from

[`RolldownLog`](Interface.RolldownLog.md).[`code`](Interface.RolldownLog.md#code)

***

### exporter?

* **Type**: `string`
* **Optional**

#### Inherited from

[`RolldownLog`](Interface.RolldownLog.md).[`exporter`](Interface.RolldownLog.md#exporter)

***

### frame?

* **Type**: `string`
* **Optional**

#### Inherited from

[`RolldownLog`](Interface.RolldownLog.md).[`frame`](Interface.RolldownLog.md#frame)

***

### hook?

* **Type**: `string`
* **Optional**

#### Inherited from

[`RolldownLog`](Interface.RolldownLog.md).[`hook`](Interface.RolldownLog.md#hook)

***

### id?

* **Type**: `string`
* **Optional**

#### Inherited from

[`RolldownLog`](Interface.RolldownLog.md).[`id`](Interface.RolldownLog.md#id)

***

### ids?

* **Type**: `string`\[]
* **Optional**

#### Inherited from

[`RolldownLog`](Interface.RolldownLog.md).[`ids`](Interface.RolldownLog.md#ids)

***

### loc?

* **Type**: object with the properties below
* **Optional**

#### column

* **Type**: `number`

#### file?

* **Type**: `string`
* **Optional**

#### line

* **Type**: `number`

#### Inherited from

[`RolldownLog`](Interface.RolldownLog.md).[`loc`](Interface.RolldownLog.md#loc)

***

### message

* **Type**: `string`

The message for this log object.

#### Example

```ts
'The "transform" hook used by the output plugin "rolldown-plugin-foo" is a build time hook and will not be run for that plugin. Either this plugin cannot be used as an output plugin, or it should have an option to configure it as an output plugin.'
```

#### Inherited from

[`RolldownLog`](Interface.RolldownLog.md).[`message`](Interface.RolldownLog.md#message)

***

### meta?

* **Type**: `any`
* **Optional**

#### Inherited from

[`RolldownLog`](Interface.RolldownLog.md).[`meta`](Interface.RolldownLog.md#meta)

***

### name?

* **Type**: `string`
* **Optional**

***

### names?

* **Type**: `string`\[]
* **Optional**

#### Inherited from

[`RolldownLog`](Interface.RolldownLog.md).[`names`](Interface.RolldownLog.md#names)

***

### plugin?

* **Type**: `string`
* **Optional**

#### Inherited from

[`RolldownLog`](Interface.RolldownLog.md).[`plugin`](Interface.RolldownLog.md#plugin)

***

### pluginCode?

* **Type**: `unknown`
* **Optional**

#### Inherited from

[`RolldownLog`](Interface.RolldownLog.md).[`pluginCode`](Interface.RolldownLog.md#plugincode)

***

### pos?

* **Type**: `number`
* **Optional**

#### Inherited from

[`RolldownLog`](Interface.RolldownLog.md).[`pos`](Interface.RolldownLog.md#pos)

***

### reexporter?

* **Type**: `string`
* **Optional**

#### Inherited from

[`RolldownLog`](Interface.RolldownLog.md).[`reexporter`](Interface.RolldownLog.md#reexporter)

***

### stack?

* **Type**: `string`
* **Optional**

#### Overrides

[`RolldownLog`](Interface.RolldownLog.md).[`stack`](Interface.RolldownLog.md#stack)

***

### url?

* **Type**: `string`
* **Optional**

#### Inherited from

[`RolldownLog`](Interface.RolldownLog.md).[`url`](Interface.RolldownLog.md#url)

***

### watchFiles?

* **Type**: `string`\[]
* **Optional**
