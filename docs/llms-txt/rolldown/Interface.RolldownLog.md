# Source: https://rolldown.rs/reference/Interface.RolldownLog.md

---
url: /reference/Interface.RolldownLog.md
---
# Interface: RolldownLog

## Extended by

* [`RolldownError`](Interface.RolldownError.md)

## Properties

### binding?

* **Type**: `string`
* **Optional**

***

### cause?

* **Type**: `unknown`
* **Optional**

***

### code?

* **Type**: `string`
* **Optional**

The log code for this log object.

#### Example

```ts
'PLUGIN_ERROR'
```

***

### exporter?

* **Type**: `string`
* **Optional**

***

### frame?

* **Type**: `string`
* **Optional**

***

### hook?

* **Type**: `string`
* **Optional**

***

### id?

* **Type**: `string`
* **Optional**

***

### ids?

* **Type**: `string`\[]
* **Optional**

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

***

### message

* **Type**: `string`

The message for this log object.

#### Example

```ts
'The "transform" hook used by the output plugin "rolldown-plugin-foo" is a build time hook and will not be run for that plugin. Either this plugin cannot be used as an output plugin, or it should have an option to configure it as an output plugin.'
```

***

### meta?

* **Type**: `any`
* **Optional**

***

### names?

* **Type**: `string`\[]
* **Optional**

***

### plugin?

* **Type**: `string`
* **Optional**

***

### pluginCode?

* **Type**: `unknown`
* **Optional**

***

### pos?

* **Type**: `number`
* **Optional**

***

### reexporter?

* **Type**: `string`
* **Optional**

***

### stack?

* **Type**: `string`
* **Optional**

***

### url?

* **Type**: `string`
* **Optional**
