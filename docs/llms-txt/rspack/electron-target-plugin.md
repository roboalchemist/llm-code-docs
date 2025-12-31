# Source: https://rspack.dev/plugins/webpack/electron-target-plugin.md

# ElectronTargetPlugin

This plugin is used to external the Electron built-in modules during bundling, and is used by [`externalsPresets.electron`](/config/externals.md#electron), [`externalsPresets.electronMain`](/config/externals.md#electronmain), [`externalsPresets.electronRenderer`](/config/externals.md#electronrenderer), and [`externalsPresets.electronPreload`](/config/externals.md#electronpreload) under the hood.

```js
new rspack.electron.ElectronTargetPlugin();
```
