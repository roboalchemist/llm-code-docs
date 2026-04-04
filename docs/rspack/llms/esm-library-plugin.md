# Source: https://rspack.dev/plugins/rspack/esm-library-plugin.md

# EsmLibraryPlugin

[Added in v1.5.6](https://github.com/web-infra-dev/rspack/releases/tag/v1.5.6)[Removed in v2.0.0](/en/misc/planning/future)Rspack only
:::tip
Since v2.0, this plugin has already bean the implementation for library with type ["modern-module"](/config/output.md#type-modern-module), you should use config instead of using plugin directly.

🚧 This plugin is still work-in-progress, config may change at anytime.
:::

Rspack provides experimental `EsmLibraryPlugin` plugin, provides statically analyzable, cleaner output for ESM library, and also supports code splitting.

```js title="rspack.config.mjs"
import { rspack } from '@rspack/core';

export default {
  plugins: [new rspack.experiments.EsmLibraryPlugin()],
  optimization: {
    runtimeChunk: true, // recommended to enable runtime chunk, otherwise consumers need to import runtime code from entry
  },
};
```

## Known limits

- Execution order of modules is not 100% guaranteed, so avoid relying on side effects of execution orders.
- Currently does not support context module and ModuleFederation, but this will be improved in the future.
