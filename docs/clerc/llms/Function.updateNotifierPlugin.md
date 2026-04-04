# Source: https://clerc.so1ve.dev/reference/api/plugin-update-notifier/Function.updateNotifierPlugin.md

# Source: https://clerc.so1ve.dev/reference/api/clerc/Function.updateNotifierPlugin.md

---

url: /reference/api/clerc/Function.updateNotifierPlugin.md
---

# Function: updateNotifierPlugin()

```ts twoslash
// @include: imports
function updateNotifierPlugin(__namedParameters): Plugin;
```

Defined in: [packages/plugin-update-notifier/src/index.ts:35](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-update-notifier/src/index.ts#L35)

Plugin to check for CLI updates using update-notifier.

## Parameters

`__namedParameters`

[`UpdateNotifierPluginOptions`](Interface.UpdateNotifierPluginOptions.md)

## Returns

[`Plugin`](Interface.Plugin.md)

## Example

```ts twoslash
// @include: imports
import { Clerc } from "@clerc/core";
import { updateNotifierPlugin } from "@clerc/plugin-update-notifier";
import pkg from "./package.json";

Clerc.create().use(updateNotifierPlugin({ pkg })).parse();
```
