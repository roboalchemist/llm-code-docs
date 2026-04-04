# Cargo.toml
[dependencies]
tauri-plugin-shell = "2"
```

2. Use in JavaScript or Rust project:

<Tabs syncKey="lang">
<TabItem label="JavaScript">

```rust
fn main() {
    tauri::Builder::default()
        .plugin(tauri_plugin_shell::init())
}
```

```json
// package.json
{
  "dependencies": {
    "@tauri-apps/plugin-shell": "^2.0.0"
  }
}
```

```javascript
import { Command, open } from '@tauri-apps/plugin-shell';
const output = await Command.create('echo', 'message').execute();

await open('https://github.com/tauri-apps/tauri');
```

</TabItem>
<TabItem label="Rust">

- Open an URL

```rust
use tauri_plugin_shell::ShellExt;

fn main() {
    tauri::Builder::default()
        .plugin(tauri_plugin_shell::init())
        .setup(|app| {
            app.shell().open("https://github.com/tauri-apps/tauri", None)?;
            Ok(())
        })
}
```

- Spawn a child process and retrieve the status code

```rust
use tauri_plugin_shell::ShellExt;

fn main() {
    tauri::Builder::default()
        .plugin(tauri_plugin_shell::init())
        .setup(|app| {
            let status = tauri::async_runtime::block_on(async move { app.shell().command("which").args(["ls"]).status().await.unwrap() });
            println!("`which` finished with status: {:?}", status.code());
            Ok(())
        })
}
```

- Spawn a child process and capture its output

```rust
use tauri_plugin_shell::ShellExt;

fn main() {
    tauri::Builder::default()
        .plugin(tauri_plugin_shell::init())
        .setup(|app| {
            let output = tauri::async_runtime::block_on(async move { app.shell().command("echo").args(["TAURI"]).output().await.unwrap() });
            assert!(output.status.success());
            assert_eq!(String::from_utf8(output.stdout).unwrap(), "TAURI");
            Ok(())
        })
}
```

- Spawn a child process and read its events asynchronously:

```rust
use tauri_plugin_shell::{ShellExt, process::CommandEvent};

fn main() {
    tauri::Builder::default()
        .plugin(tauri_plugin_shell::init())
        .setup(|app| {
            let handle = app.handle().clone();
            tauri::async_runtime::spawn(async move {
                let (mut rx, mut child) = handle.shell().command("cargo")
                    .args(["tauri", "dev"])
                    .spawn()
                    .expect("Failed to spawn cargo");

                let mut i = 0;
                while let Some(event) = rx.recv().await {
                    if let CommandEvent::Stdout(line) = event {
                        println!("got: {}", String::from_utf8(line).unwrap());
                       i += 1;
                       if i == 4 {
                           child.write("message from Rust\n".as_bytes()).unwrap();
                           i = 0;
                       }
                   }
                }
            });
            Ok(())
        })
}
```

</TabItem>
</Tabs>

### Migrate to Tray Icon Module

The Rust `SystemTray` APIs were renamed to `TrayIcon` for consistency. The new APIs can be found in the Rust `tray` module.

#### Use `tauri::tray::TrayIconBuilder`

Use `tauri::tray::TrayIconBuilder` instead of `tauri::SystemTray`:

```rust
let tray = tauri::tray::TrayIconBuilder::with_id("my-tray").build(app)?;
```

See [TrayIconBuilder](https://docs.rs/tauri/2.0.0/tauri/tray/struct.TrayIconBuilder.html) for more information.

#### Migrate to Menu

Use `tauri::menu::Menu` instead of `tauri::SystemTrayMenu`, `tauri::menu::Submenu` instead of `tauri::SystemTraySubmenu` and `tauri::menu::PredefinedMenuItem` instead of `tauri::SystemTrayMenuItem`.

#### Tray Events

`tauri::SystemTray::on_event` have been split into `tauri::tray::TrayIconBuilder::on_menu_event` and `tauri::tray::TrayIconBuilder::on_tray_icon_event`:

```rust
use tauri::{
    menu::{MenuBuilder, MenuItemBuilder},
    tray::{MouseButton, MouseButtonState, TrayIconBuilder, TrayIconEvent},
};

tauri::Builder::default()
    .setup(|app| {
        let toggle = MenuItemBuilder::with_id("toggle", "Toggle").build(app)?;
        let menu = MenuBuilder::new(app).items(&[&toggle]).build()?;
        let tray = TrayIconBuilder::new()
            .menu(&menu)
            .on_menu_event(move |app, event| match event.id().as_ref() {
                "toggle" => {
                    println!("toggle clicked");
                }
                _ => (),
            })
            .on_tray_icon_event(|tray, event| {
                if let TrayIconEvent::Click {
                        button: MouseButton::Left,
                        button_state: MouseButtonState::Up,
                        ..
                } = event
                {
                    let app = tray.app_handle();
                    if let Some(webview_window) = app.get_webview_window("main") {
                       let _ = webview_window.unminimize();
                       let _ = webview_window.show();
                       let _ = webview_window.set_focus();
                    }
                }
            })
            .build(app)?;

        Ok(())
    })
```

### Migrate to Updater Plugin

:::caution[Change of default behavior]

The built-in dialog with an automatic update check was removed, use the Rust and JS APIs to check for and install updates instead. Failing to do so will prevent your users from getting further updates!

:::

The Rust `tauri::updater` and JavaScript `@tauri-apps/api-updater` APIs have been removed. To set a custom updater target with the `@tauri-apps/plugin-updater`:

1. Add to cargo dependencies:

```toml
[dependencies]
tauri-plugin-updater = "2"
```

2. Use in JavaScript or Rust project:

<Tabs syncKey="lang">
<TabItem label="JavaScript">

```rust
fn main() {
    tauri::Builder::default()
        .plugin(tauri_plugin_updater::Builder::new().build())
}
```

```json
// package.json
{
  "dependencies": {
    "@tauri-apps/plugin-updater": "^2.0.0"
  }
}
```

```javascript
import { check } from '@tauri-apps/plugin-updater';
import { relaunch } from '@tauri-apps/plugin-process';

const update = await check();
if (update?.available) {
  console.log(`Update to ${update.version} available! Date: ${update.date}`);
  console.log(`Release notes: ${update.body}`);
  await update.downloadAndInstall();
  // requires the `process` plugin
  await relaunch();
}
```

</TabItem>
<TabItem label="Rust">

To check for updates:

```rust
use tauri_plugin_updater::UpdaterExt;

fn main() {
    tauri::Builder::default()
        .plugin(tauri_plugin_updater::Builder::new().build())
        .setup(|app| {
            let handle = app.handle();
            tauri::async_runtime::spawn(async move {
                let response = handle.updater().check().await;
            });
            Ok(())
        })
}
```

To set a custom updater target:

```rust
fn main() {
    let mut updater = tauri_plugin_updater::Builder::new();
    #[cfg(target_os = "macos")]
    {
        updater = updater.target("darwin-universal");
    }
    tauri::Builder::default()
        .plugin(updater.build())
}
```

</TabItem>
</Tabs>

### Migrate Path to Tauri Manager

The Rust `tauri::api::path` module functions and `tauri::PathResolver` have been moved to `tauri::Manager::path`:

```rust
use tauri::{path::BaseDirectory, Manager};

tauri::Builder::default()
    .setup(|app| {
        let home_dir_path = app.path().home_dir().expect("failed to get home dir");

        let path = app.path().resolve("path/to/something", BaseDirectory::Config)?;

        Ok(())
  })
```

### Migrate to new Window API

On the Rust side, `Window` was renamed to `WebviewWindow`, its builder `WindowBuilder` is now named `WebviewWindowBuilder` and `WindowUrl` is now named `WebviewUrl`.

Additionally, the `Manager::get_window` function was renamed to `get_webview_window` and
the window's `parent_window` API was renamed to `parent_raw` to support a high level window parent API.

On the JavaScript side, the `WebviewWindow` class is now exported in the `@tauri-apps/api/webviewWindow` path.

The `onMenuClicked` function was removed, you can intercept menu events when creating a menu in JavaScript instead.

### Migrate Embedded Additional Files (Resources)

On the JavaScript side, make sure you [Migrate to File System Plugin](#migrate-to-file-system-plugin).
Additionally, note the changes made to the v1 allowlist in [Migrate Permissions](#migrate-permissions).

On the Rust side, make sure you [Migrate Path to Tauri Manager](#migrate-path-to-tauri-manager).

### Migrate Embedded External Binaries (Sidecar)

In Tauri v1, the external binaries and their arguments were defined in the allowlist. In v2, use the new permissions system. Read [Migrate Permissions](#migrate-permissions) for more information.

On the JavaScript side, make sure you [Migrate to Shell Plugin](#migrate-to-shell-plugin).

On the Rust side, `tauri::api::process` API has been removed. Use `tauri_plugin_shell::ShellExt` and `tauri_plugin_shell::process::CommandEvent` APIs instead. Read the [Embedding External Binaries](/develop/sidecar/#running-it-from-rust) guide to see how.

The "process-command-api" features flag has been removed in v2. So running the external binaries does not require this feature to be defined in the Tauri config anymore.

### Migrate Permissions

The v1 allowlist have been rewritten to a completely new system for permissions that works for individual plugins and is much more configurable for multiwindow and remote URL support.
This new system works like an access control list (ACL) where you can allow or deny commands, allocate permissions to a specific set of windows and domains, and define access scopes.

To enable permissions for your app, you must create capability files inside the `src-tauri/capabilities` folder, and Tauri will automatically configure everything else for you.

The `migrate` CLI command automatically parses your v1 allowlist and generates the associated capability file.

To learn more about permissions and capabilities, see [the security documentation](/security/).