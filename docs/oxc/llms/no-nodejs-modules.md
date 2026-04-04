# Source: https://oxc.rs/docs/guide/usage/linter/rules/import/no-nodejs-modules.md

---
url: /docs/guide/usage/linter/rules/import/no-nodejs-modules.md
---

### What it does

Forbid the use of Node.js builtin modules. Can be useful for client-side web projects that do not have access to those modules.

### Why is this bad?

Node.js builtins (e.g. `fs`, `path`, `crypto`) are not available in browsers, so importing them in client bundles causes runtime failures or forces bundlers to inject heavy polyfills/shims.
This increases bundle size, can leak server-only logic to the client, and may hide environment mismatches until production.

### Examples

Examples of **incorrect** code for this rule:

```js
import fs from "fs";
import path from "path";

var fs = require("fs");
var path = require("path");
```

Examples of **correct** code for this rule:

```js
import _ from "lodash";
import foo from "foo";
import foo from "./foo";

var _ = require("lodash");
var foo = require("foo");
var foo = require("./foo");

/* eslint import/no-nodejs-modules: ["error", {"allow": ["path"]}] */
import path from "path";
```

## Configuration

This rule accepts a configuration object with the following properties:

### allow

type: `string[]`

Array of names of allowed modules. Defaults to an empty array.

## How to use

To **enable** this rule using the config file or in the CLI, you can use:

::: code-group

```json [Config (.oxlintrc.json)]
{
  "plugins": ["import"],
  "rules": {
    "import/no-nodejs-modules": "error"
  }
}
```

```bash [CLI]
oxlint --deny import/no-nodejs-modules --import-plugin
```

:::

## References

* Rule Source
