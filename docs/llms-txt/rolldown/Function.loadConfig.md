# Source: https://rolldown.rs/reference/Function.loadConfig.md

---
url: /reference/Function.loadConfig.md
---
# Function: loadConfig()

* **Exported from**: `rolldown/config`
* **Type**: (`configPath`: `string`) => `Promise`<[`ConfigExport`](TypeAlias.ConfigExport.md)>

Load config from a file in a way that Rolldown does.

## Parameters

### configPath

`string`

The path to the config file. If empty, it will look for `rolldown.config` with supported extensions in the current working directory.

## Returns

`Promise`<[`ConfigExport`](TypeAlias.ConfigExport.md)>

The loaded config export
