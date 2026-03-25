# Source: https://clerc.so1ve.dev/official-plugins/plugin-update-notifier.md

# Source: https://clerc.so1ve.dev/reference/api/plugin-update-notifier.md

---

url: /reference/api/plugin-update-notifier.md
---

# @clerc/plugin-update-notifier

## Interfaces

[UpdateNotifierPluginOptions](Interface.UpdateNotifierPluginOptions.md)

‐

## Functions

[updateNotifierPlugin](Function.updateNotifierPlugin.md)

Plugin to check for CLI updates using update-notifier.

**Example**

```ts twoslash
// @include: imports
import { Clerc } from "@clerc/core";
import { updateNotifierPlugin } from "@clerc/plugin-update-notifier";
import pkg from "./package.json";

Clerc.create().use(updateNotifierPlugin({ pkg })).parse();
```
