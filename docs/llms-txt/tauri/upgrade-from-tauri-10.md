# Upgrade from Tauri 1.0

import { Tabs, TabItem } from '@astrojs/starlight/components';
import CommandTabs from '@components/CommandTabs.astro';

This guide walks you through upgrading your Tauri 1.0 application to Tauri 2.0.

## Preparing for Mobile

The mobile interface of Tauri requires your project to output a shared library. If you are targeting mobile for your existing application, you must change your crate to produce that kind of artifact along with the desktop executable.

1. Change the Cargo manifest to produce the library. Append the following block:

```toml
// src-tauri/Cargo.toml
[lib]
name = "app_lib"
crate-type = ["staticlib", "cdylib", "rlib"]
```

2. Rename `src-tauri/src/main.rs` to `src-tauri/src/lib.rs`. This file will be shared by both desktop and mobile targets.

3. Rename the `main` function header in `lib.rs` to the following:

```rust
// src-tauri/src/lib.rs
#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    // your code here
}
```

The `tauri::mobile_entry_point` macro prepares your function to be executed on mobile.

4. Recreate the `main.rs` file calling the shared run function:

```rust
// src-tauri/src/main.rs
#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]

fn main() {
  app_lib::run();
}
```

## Automated Migration

:::danger

This command is not a substitude for this guide! Please read the _whole_ page regardless of whether you chose to use the command.

:::

The Tauri v2 CLI includes a `migrate` command that automates most of the process and helps you finish the migration:

<CommandTabs
  npm="npm install @tauri-apps/cli@latest
    npm run tauri migrate"
  yarn="yarn upgrade @tauri-apps/cli@latest
    yarn tauri migrate"
  pnpm="pnpm update @tauri-apps/cli@latest
    pnpm tauri migrate"
  cargo='cargo install tauri-cli --version "^2.0.0" --locked
    cargo tauri migrate'
/>

Learn more about the `migrate` command in the [Command Line Interface reference](/reference/cli/#migrate)

## Summary of Changes

Below is a summary of the changes from Tauri 1.0 to Tauri 2.0:

### Tauri Configuration

- `package > productName` and `package > version` moved to top-level object.
- the binary name is no longer renamed to match `productName` automatically, so you must add a `mainBinaryName` string to the top-level object matching `productName`.
- `package` removed.
- `tauri` key renamed to `app`.
- `tauri > allowlist` removed. Refer to [Migrate Permissions](#migrate-permissions).
- `tauri > allowlist > protocol > assetScope` moved to `app > security > assetProtocol > scope`.
- `tauri > cli` moved to `plugins > cli`.
- `tauri > windows > fileDropEnabled` renamed to `app > windows > dragDropEnabled`.
- `tauri > updater > active` removed.
- `tauri > updater > dialog` removed.
- `tauri > updater` moved to `plugins > updater`.
- `bundle > createUpdaterArtifacts` added, must be set when using the app updater.
  - set it to `v1Compatible` when upgrading from v1 apps that were already distributed. See the [updater guide](/plugin/updater/) for more information.
- `tauri > systemTray` renamed to `app > trayIcon`.
- `tauri > pattern` moved to `app > security > pattern`.
- `tauri > bundle` moved top-level.
- `tauri > bundle > identifier` moved to top-level object.
- `tauri > bundle > dmg` moved to `bundle > macOS > dmg`
- `tauri > bundle > deb` moved to `bundle > linux > deb`
- `tauri > bundle > appimage` moved to `bundle > linux > appimage`
- `tauri > bundle > macOS > license` removed, use `bundle > licenseFile` instead.
- `tauri > bundle > windows > wix > license` removed, use `bundle > licenseFile` instead.
- `tauri > bundle > windows > nsis > license` removed, use `bundle > licenseFile` instead.
- `tauri > bundle > windows > webviewFixedRuntimePath` removed, use `bundle > windows > webviewInstallMode` instead.
- `build > withGlobalTauri` moved to `app > withGlobalTauri`.
- `build > distDir` renamed to `frontendDist`.
- `build > devPath` renamed to `devUrl`.

[Tauri 2.0 Configuration API reference](/reference/config/)

### New Cargo Features

- linux-protocol-body: Enables custom protocol request body parsing, allowing the IPC to use it. Requires webkit2gtk 2.40.

### Removed Cargo Features

- reqwest-client: reqwest is now the only supported client.
- reqwest-native-tls-vendored: use `native-tls-vendored` instead.
- process-command-api: use the `shell` plugin instead (see instructions in the following section).
- shell-open-api: use the `shell` plugin instead (see instructions in the following section).
- windows7-compat: moved to the `notification` plugin.
- updater: Updater is now a plugin.
- linux-protocol-headers: Now enabled by default since we upgraded our minimum webkit2gtk version.
- system-tray: renamed to `tray-icon`.

### Rust Crate Changes

- `api` module removed. Each API module can be found in a Tauri plugin.
- `api::dialog` module removed. Use `tauri-plugin-dialog` instead. [Migration](#migrate-to-dialog-plugin)
- `api::file` module removed. Use Rust's [`std::fs`](https://doc.rust-lang.org/std/fs/) instead.
- `api::http` module removed. Use `tauri-plugin-http` instead. [Migration](#migrate-to-http-plugin)
- `api::ip` module rewritten and moved to `tauri::ipc`. Check out the new APIs, specially `tauri::ipc::Channel`.
- `api::path` module functions and `tauri::PathResolved` moved to `tauri::Manager::path`. [Migration](#migrate-path-to-tauri-manager)
- `api::process::Command`, `tauri::api::shell` and `tauri::Manager::shell_scope` APIs removed. Use `tauri-plugin-shell` instead. [Migration](#migrate-to-shell-plugin)
- `api::process::current_binary` and `tauri::api::process::restart` moved to `tauri::process`.
- `api::version` module has been removed. Use the [semver crate](https://docs.rs/semver/latest/semver/) instead.
- `App::clipboard_manager` and `AppHandle::clipboard_manager` removed. Use `tauri-plugin-clipboard` instead. [Migration](#migrate-to-clipboard-plugin)
- `App::get_cli_matches` removed. Use `tauri-plugin-cli` instead. [Migration](#migrate-to-cli-plugin)
- `App::global_shortcut_manager` and `AppHandle::global_shortcut_manager` removed. Use `tauri-plugin-global-shortcut` instead. [Migration](#migrate-to-global-shortcut-plugin)
- `Manager::fs_scope` removed. The file system scope can be accessed via `tauri_plugin_fs::FsExt`.
- `Plugin::PluginApi` now receives a plugin configuration as a second argument.
- `Plugin::setup_with_config` removed. Use the updated `tauri::Plugin::PluginApi` instead.
- `scope::ipc::RemoteDomainAccessScope::enable_tauri_api` and `scope::ipc::RemoteDomainAccessScope::enables_tauri_api` removed. Enable each core plugin individually via `scope::ipc::RemoteDomainAccessScope::add_plugin` instead.
- `scope::IpcScope` removed, use `scope::ipc::Scope` instead.
- `scope::FsScope`, `scope::GlobPattern` and `scope::FsScopeEvent` removed, use `scope::fs::Scope`, `scope::fs::Pattern` and `scope::fs::Event` respectively.
- `updater` module removed. Use `tauri-plugin-updater` instead. [Migration](#migrate-to-updater-plugin)
- `Env.args` field has been removed, use `Env.args_os` field instead.
- `Menu`, `MenuEvent`, `CustomMenuItem`, `Submenu`, `WindowMenuEvent`, `MenuItem` and `Builder::on_menu_event` APIs removed. [Migration](#migrate-to-menu)
- `SystemTray`, `SystemTrayHandle`, `SystemTrayMenu`, `SystemTrayMenuItemHandle`, `SystemTraySubmenu`, `MenuEntry` and `SystemTrayMenuItem` APIs removed. [Migration](#migrate-to-tray-icon-module)

### JavaScript API Changes

The `@tauri-apps/api` package no longer provides non-core modules. Only the previous `tauri` (now `core`), `path`, `event` and `window` modules are exported. All others have been moved to plugins.

- `@tauri-apps/api/tauri` module renamed to `@tauri-apps/api/core`. [Migration](#migrate-to-core-module)
- `@tauri-apps/api/cli` module removed. Use `@tauri-apps/plugin-cli` instead. [Migration](#migrate-to-cli-plugin)
- `@tauri-apps/api/clipboard` module removed. Use `@tauri-apps/plugin-clipboard` instead. [Migration](#migrate-to-clipboard-plugin)
- `@tauri-apps/api/dialog` module removed. Use `@tauri-apps/plugin-dialog` instead. [Migration](#migrate-to-dialog-plugin)
- `@tauri-apps/api/fs` module removed. Use `@tauri-apps/plugin-fs` instead. [Migration](#migrate-to-file-system-plugin)
- `@tauri-apps/api/global-shortcut` module removed. Use `@tauri-apps/plugin-global-shortcut` instead. [Migration](#migrate-to-global-shortcut-plugin)
- `@tauri-apps/api/http` module removed. Use `@tauri-apps/plugin-http` instead. [Migration](#migrate-to-http-plugin)
- `@tauri-apps/api/os` module removed. Use `@tauri-apps/plugin-os` instead. [Migration](#migrate-to-os-plugin)
- `@tauri-apps/api/notification` module removed. Use `@tauri-apps/plugin-notification` instead. [Migration](#migrate-to-notification-plugin)
- `@tauri-apps/api/process` module removed. Use `@tauri-apps/plugin-process` instead. [Migration](#migrate-to-process-plugin)
- `@tauri-apps/api/shell` module removed. Use `@tauri-apps/plugin-shell` instead. [Migration](#migrate-to-shell-plugin)
- `@tauri-apps/api/updater` module removed. Use `@tauri-apps/plugin-updater` instead [Migration](#migrate-to-updater-plugin)
- `@tauri-apps/api/window` module renamed to `@tauri-apps/api/webviewWindow`. [Migration](#migrate-to-new-window-api)

The v1 plugins are now published as `@tauri-apps/plugin-<plugin-name>`. Previously they were available from git as `tauri-plugin-<plugin-name>-api`.

### Environment Variables Changes

Most of the environment variables read and written by the Tauri CLI were renamed for consistency and prevention of mistakes:

- `TAURI_PRIVATE_KEY` -> `TAURI_SIGNING_PRIVATE_KEY`
- `TAURI_KEY_PASSWORD` -> `TAURI_SIGNING_PRIVATE_KEY_PASSWORD`
- `TAURI_SKIP_DEVSERVER_CHECK` -> `TAURI_CLI_NO_DEV_SERVER_WAIT`
- `TAURI_DEV_SERVER_PORT` -> `TAURI_CLI_PORT`
- `TAURI_PATH_DEPTH` -> `TAURI_CLI_CONFIG_DEPTH`
- `TAURI_FIPS_COMPLIANT` -> `TAURI_BUNDLER_WIX_FIPS_COMPLIANT`
- `TAURI_DEV_WATCHER_IGNORE_FILE` -> `TAURI_CLI_WATCHER_IGNORE_FILENAME`
- `TAURI_TRAY` -> `TAURI_LINUX_AYATANA_APPINDICATOR`
- `TAURI_APPLE_DEVELOPMENT_TEAM` -> `APPLE_DEVELOPMENT_TEAM`
- `TAURI_PLATFORM` -> `TAURI_ENV_PLATFORM`
- `TAURI_ARCH` -> `TAURI_ENV_ARCH`
- `TAURI_FAMILY` -> `TAURI_ENV_FAMILY`
- `TAURI_PLATFORM_VERSION` -> `TAURI_ENV_PLATFORM_VERSION`
- `TAURI_PLATFORM_TYPE` -> `TAURI_ENV_PLATFORM_TYPE`
- `TAURI_DEBUG` -> `TAURI_ENV_DEBUG`

### Event System

The event system was redesigned to be easier to use. Instead of relying on the source of the event, it now has a simpler implementation that relies on event targets.

- The `emit` function now emits the event to all event listeners.
- Added a new `emit_to`/`emitTo` function to trigger an event to a specific target.
- `emit_filter` now filters based on [`EventTarget`](https://docs.rs/tauri/2.0.0/tauri/event/enum.EventTarget.html) instead of a window.
- Renamed `listen_global` to `listen_any`. It now listens to all events regardless of their filters and targets.
- JavaScript: `event.listen()` behaves similar to `listen_any`. It now listens to all events regardless of their filters and targets, unless a target is set in the `Options`.
- JavaScript: `WebviewWindow.listen` etc. only listen to events emitted to the respective `EventTarget`.

### Multiwebview support

Tauri v2 introduces multiwebview support currently behind an `unstable` feature flag.
In order to support it, we renamed the Rust `Window` type to `WebviewWindow` and the Manager `get_window` function to `get_webview_window`.

The `WebviewWindow` JS API type is now re-exported from `@tauri-apps/api/webviewWindow` instead of `@tauri-apps/api/window`.

### New origin URL on Windows

On Windows the frontend files in production apps are now hosted on `http://tauri.localhost` instead of `https://tauri.localhost`. Because of this IndexedDB, LocalStorage and Cookies will be reset unless `dangerousUseHttpScheme` was used in v1. To prevent this you can set `app > windows > useHttpsScheme` to `true` or use `WebviewWindowBuilder::use_https_scheme` to keep using the `https` scheme.

## Detailed Migration Steps

Common scenarios you may encounter when migrating your Tauri 1.0 app to Tauri 2.0.

### Migrate to Core Module

The `@tauri-apps/api/tauri` module was renamed to `@tauri-apps/api/core`.
Simply rename the module import:

```diff
- import { invoke } from "@tauri-apps/api/tauri"
+ import { invoke } from "@tauri-apps/api/core"
```

### Migrate to CLI Plugin

The Rust `App::get_cli_matches` JavaScript `@tauri-apps/api/cli` APIs have been removed. Use the `@tauri-apps/plugin-cli` plugin instead:

1. Add to cargo dependencies:

```toml