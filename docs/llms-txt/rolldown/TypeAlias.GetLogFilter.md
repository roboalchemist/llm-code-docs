# Source: https://rolldown.rs/reference/TypeAlias.GetLogFilter.md

---
url: /reference/TypeAlias.GetLogFilter.md
---
# Type Alias: GetLogFilter()

* **Exported from**: `rolldown/getLogFilter`
* **Type**: (`filters`) => (`log`) => `boolean`

## Parameters

### filters

`string`\[]

A list of log filters to apply

## Returns

A function that tests whether a log should be output

* **Type**: (`log`: [`RolldownLog`](Interface.RolldownLog.md)) => `boolean`

### Parameters

#### log

[`RolldownLog`](Interface.RolldownLog.md)

### Returns

`boolean`
