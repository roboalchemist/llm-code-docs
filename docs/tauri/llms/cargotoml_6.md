# Cargo.toml
[dependencies]
tauri-plugin-notification = "2"
```

2. Use in JavaScript or Rust project:

<Tabs syncKey="lang">
<TabItem label="JavaScript">

```rust
fn main() {
    tauri::Builder::default()
        .plugin(tauri_plugin_notification::init())
}
```

```json
// package.json
{
  "dependencies": {
    "@tauri-apps/plugin-notification": "^2.0.0"
  }
}
```

```javascript
import { sendNotification } from '@tauri-apps/plugin-notification';
sendNotification('Tauri is awesome!');
```

</TabItem>
<TabItem label="Rust">

```rust
use tauri_plugin_notification::NotificationExt;
use tauri::plugin::PermissionState;

fn main() {
    tauri::Builder::default()
        .plugin(tauri_plugin_notification::init())
        .setup(|app| {
            if app.notification().permission_state()? == PermissionState::Unknown {
                app.notification().request_permission()?;
            }
            if app.notification().permission_state()? == PermissionState::Granted {
                app.notification()
                    .builder()
                    .body("Tauri is awesome!")
                    .show()?;
            }
            Ok(())
        })
}
```

</TabItem>
</Tabs>

### Migrate to Menu Module

The Rust `Menu` APIs were moved to the `tauri::menu` module and refactored to use the [muda crate](https://github.com/tauri-apps/muda).

#### Use `tauri::menu::MenuBuilder`

Use `tauri::menu::MenuBuilder` instead of `tauri::Menu`. Note that its constructor takes a Manager instance (one of `App`, `AppHandle` or `WebviewWindow`) as an argument:

```rust
use tauri::menu::MenuBuilder;

tauri::Builder::default()
    .setup(|app| {
        let menu = MenuBuilder::new(app)
            .copy()
            .paste()
            .separator()
            .undo()
            .redo()
            .text("open-url", "Open URL")
            .check("toggle", "Toggle")
            .icon("show-app", "Show App", app.default_window_icon().cloned().unwrap())
            .build()?;
        app.set_menu(menu);
        Ok(())
    })
```

#### Use `tauri::menu::PredefinedMenuItem`

Use `tauri::menu::PredefinedMenuItem` instead of `tauri::MenuItem`:

```rust
use tauri::menu::{MenuBuilder, PredefinedMenuItem};

tauri::Builder::default()
    .setup(|app| {
        let menu = MenuBuilder::new(app).item(&PredefinedMenuItem::copy(app)?).build()?;
        Ok(())
    })
```

:::tip
The menu builder has dedicated methods to add each predefined menu item so you can call `.copy()` instead of `.item(&PredefinedMenuItem::copy(app, None)?)`.
:::

#### Use `tauri::menu::MenuItemBuilder`

Use `tauri::menu::MenuItemBuilder` instead of `tauri::CustomMenuItem`:

```rust
use tauri::menu::MenuItemBuilder;

tauri::Builder::default()
    .setup(|app| {
        let toggle = MenuItemBuilder::new("Toggle").accelerator("Ctrl+Shift+T").build(app)?;
        Ok(())
    })
```

#### Use `tauri::menu::SubmenuBuilder`

Use `tauri::menu::SubmenuBuilder` instead of `tauri::Submenu`:

```rust
use tauri::menu::{MenuBuilder, SubmenuBuilder};

tauri::Builder::default()
    .setup(|app| {
        let submenu = SubmenuBuilder::new(app, "Sub")
            .text("Tauri")
            .separator()
            .check("Is Awesome")
            .build()?;
        let menu = MenuBuilder::new(app).item(&submenu).build()?;
        Ok(())
    })
```

`tauri::Builder::menu` now takes a closure because the menu needs a Manager instance to be built. See [the documentation](https://docs.rs/tauri/2.0.0/tauri/struct.Builder.html#method.menu) for more information.

#### Menu Events

The Rust `tauri::Builder::on_menu_event` API was removed. Use `tauri::App::on_menu_event` or `tauri::AppHandle::on_menu_event` instead:

```rust
use tauri::menu::{CheckMenuItemBuilder, MenuBuilder, MenuItemBuilder};

tauri::Builder::default()
    .setup(|app| {
        let toggle = MenuItemBuilder::with_id("toggle", "Toggle").build(app)?;
        let check = CheckMenuItemBuilder::new("Mark").build(app)?;
        let menu = MenuBuilder::new(app).items(&[&toggle, &check]).build()?;

        app.set_menu(menu)?;

        app.on_menu_event(move |app, event| {
            if event.id() == check.id() {
                println!("`check` triggered, do something! is checked? {}", check.is_checked().unwrap());
            } else if event.id() == "toggle" {
                println!("toggle triggered!");
            }
        });
        Ok(())
    })
```

Note that there are two ways to check which menu item was selected: move the item to the event handler closure and compare IDs, or define a custom ID for the item through the `with_id` constructor and use that ID string to compare.

:::tip
Menu items can be shared across menus, and the menu event is bound to a menu item instead of a menu or window.
If you don't want all listeners to be triggered when a menu item is selected, do not share menu items and use dedicated instances instead, that you could move into `tauri::WebviewWindow/WebviewWindowBuilder::on_menu_event` closure.
:::

### Migrate to OS Plugin

The Rust `tauri::api::os` JavaScript `@tauri-apps/api/os` APIs have been removed. Use the `@tauri-apps/plugin-os` plugin instead:

1. Add to cargo dependencies:

```toml