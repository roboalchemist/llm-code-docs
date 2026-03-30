# Configuration Files

import CommandTabs from '@components/CommandTabs.astro';

Since Tauri is a toolkit for building applications there can be many files to configure project settings. Some common files that you may run across are `tauri.conf.json`, `package.json` and `Cargo.toml`. We briefly explain each on this page to help point you in the right direction for which files to modify.

## Tauri Config

The Tauri configuration is used to define the source of your Web app, describe your application's metadata, configure bundles, set plugin configurations, modify runtime behavior by configuring windows, tray icons, menus and more.

This file is used by the Tauri runtime and the Tauri CLI. You can define build settings (such as the [command run before `tauri build`][before-build-command] or [`tauri dev`][before-dev-command] kicks in), set the [name](/reference/config/#productname) and [version of your app](/reference/config/#version), [control the Tauri runtime][appconfig], and [configure plugins].

:::tip
You can find all of the options in the [configuration reference].
:::

### Supported Formats

The default Tauri config format is JSON. The JSON5 or TOML format can be enabled by adding the `config-json5` or `config-toml` feature flag (respectively) to the `tauri` and `tauri-build` dependencies in `Cargo.toml`.

```toml title=Cargo.toml
[build-dependencies]
tauri-build = { version = "2.0.0", features = [ "config-json5" ] }

[dependencies]
tauri = { version = "2.0.0", features = [  "config-json5" ] }
```

The structure and values are the same across all formats, however, the formatting should be consistent with the respective file's format:

```json5 title=tauri.conf.json or tauri.conf.json5
{
  build: {
    devUrl: 'http://localhost:3000',
    // start the dev server
    beforeDevCommand: 'npm run dev',
  },
  bundle: {
    active: true,
    icon: ['icons/app.png'],
  },
  app: {
    windows: [
      {
        title: 'MyApp',
      },
    ],
  },
  plugins: {
    updater: {
      pubkey: 'updater pub key',
      endpoints: ['https://my.app.updater/{{target}}/{{current_version}}'],
    },
  },
}
```

```toml title=Tauri.toml
[build]
dev-url = "http://localhost:3000"