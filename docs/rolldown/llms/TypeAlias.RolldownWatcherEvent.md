# Source: https://rolldown.rs/reference/TypeAlias.RolldownWatcherEvent.md

---
url: /reference/TypeAlias.RolldownWatcherEvent.md
---
# Type Alias: RolldownWatcherEvent

* **Type**: { `code`: `"START"`; } | { `code`: `"BUNDLE_START"`; } | { `code`: `"BUNDLE_END"`; `duration`: `number`; `output`: readonly `string`\[]; `result`: `RolldownWatchBuild`; } | { `code`: `"END"`; } | { `code`: `"ERROR"`; `error`: `Error`; `result`: `RolldownWatchBuild`; }

- `START`: the watcher is (re)starting
- `BUNDLE_START`: building an individual bundle
- `BUNDLE_END`: finished building a bundle
  * `duration`: the build duration in milliseconds
  * `output`: an array of the [`file`](Interface.OutputOptions.md#file) or [`dir`](Interface.OutputOptions.md#dir) option values of the generated outputs
  * `result`: the bundle object that can be used to generate additional outputs. This is especially important when the watch.skipWrite option is used. You should call `event.result.close()` once you are done generating outputs, or if you do not generate outputs. This will allow plugins to clean up resources via the `closeBundle` hook.
- `END`: finished building all bundles
- `ERROR`: encountered an error while bundling
  * `error`: the error that was thrown
  * `result`: the bundle object
