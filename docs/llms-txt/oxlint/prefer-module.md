# Source: https://oxc.rs/docs/guide/usage/linter/rules/unicorn/prefer-module.md

---
url: /docs/guide/usage/linter/rules/unicorn/prefer-module.md
---

### What it does

Prefer JavaScript modules (ESM) over CommonJS.

### Why is this bad?

CommonJS globals and patterns (`require`, `module`, `exports`, `__filename`, `__dirname`)
make code harder to migrate and can block ESM-only features.

### Examples

Examples of **incorrect** code for this rule:

```js
"use strict";
const foo = require("foo");
module.exports = foo;
```

Examples of **correct** code for this rule:

```js
import foo from "foo";
export default foo;
```

## How to use

To **enable** this rule using the config file or in the CLI, you can use:

::: code-group

```json [Config (.oxlintrc.json)]
{
  "rules": {
    "unicorn/prefer-module": "error"
  }
}
```

```bash [CLI]
oxlint --deny unicorn/prefer-module
```

:::

## References

* Rule Source
