# Source: https://rolldown.rs/reference/Function.defineConfig.md

---
url: /reference/Function.defineConfig.md
---
# Function: defineConfig()

## Call Signature

* **Type**: (`config`: [`RolldownOptions`](Interface.RolldownOptions.md)) => [`RolldownOptions`](Interface.RolldownOptions.md)

A helper to define a rolldown configuration with type hints.

### Parameters

#### config

[`RolldownOptions`](Interface.RolldownOptions.md)

### Returns

[`RolldownOptions`](Interface.RolldownOptions.md)

### Example

```js [rolldown.config.js]
import { defineConfig } from 'rolldown';

export default defineConfig({
  input: 'src/main.js',
  output: {
    file: 'bundle.js',
  },
});
```

## Call Signature

* **Type**: (`config`: [`RolldownOptions`](Interface.RolldownOptions.md)\[]) => [`RolldownOptions`](Interface.RolldownOptions.md)\[]

A helper to define a rolldown configuration with type hints.

### Parameters

#### config

[`RolldownOptions`](Interface.RolldownOptions.md)\[]

### Returns

[`RolldownOptions`](Interface.RolldownOptions.md)\[]

### Example

```js [rolldown.config.js]
import { defineConfig } from 'rolldown';

export default defineConfig({
  input: 'src/main.js',
  output: {
    file: 'bundle.js',
  },
});
```

## Call Signature

* **Type**: (`config`: [`RolldownOptionsFunction`](TypeAlias.RolldownOptionsFunction.md)) => [`RolldownOptionsFunction`](TypeAlias.RolldownOptionsFunction.md)

A helper to define a rolldown configuration with type hints.

### Parameters

#### config

[`RolldownOptionsFunction`](TypeAlias.RolldownOptionsFunction.md)

### Returns

[`RolldownOptionsFunction`](TypeAlias.RolldownOptionsFunction.md)

### Example

```js [rolldown.config.js]
import { defineConfig } from 'rolldown';

export default defineConfig({
  input: 'src/main.js',
  output: {
    file: 'bundle.js',
  },
});
```

## Call Signature

* **Type**: (`config`: [`ConfigExport`](TypeAlias.ConfigExport.md)) => [`ConfigExport`](TypeAlias.ConfigExport.md)

A helper to define a rolldown configuration with type hints.

### Parameters

#### config

[`ConfigExport`](TypeAlias.ConfigExport.md)

### Returns

[`ConfigExport`](TypeAlias.ConfigExport.md)

### Example

```js [rolldown.config.js]
import { defineConfig } from 'rolldown';

export default defineConfig({
  input: 'src/main.js',
  output: {
    file: 'bundle.js',
  },
});
```
