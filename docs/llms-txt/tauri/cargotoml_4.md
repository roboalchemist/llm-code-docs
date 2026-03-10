# Cargo.toml
[dependencies]
[target."cfg(not(any(target_os = \"android\", target_os = \"ios\")))".dependencies]
tauri-plugin-global-shortcut = "2"
```

2. Use in JavaScript or Rust project:

<Tabs syncKey="lang">
<TabItem label="JavaScript">

```rust
fn main() {
    tauri::Builder::default()
        .plugin(tauri_plugin_global_shortcut::Builder::default().build())
}
```

```json
// package.json
{
  "dependencies": {
    "@tauri-apps/plugin-global-shortcut": "^2.0.0"
  }
}
```

```javascript
import { register } from '@tauri-apps/plugin-global-shortcut';
await register('CommandOrControl+Shift+C', () => {
  console.log('Shortcut triggered');
});
```

</TabItem>
<TabItem label="Rust">

```rust
use tauri_plugin_global_shortcut::GlobalShortcutExt;

tauri::Builder::default()
    .plugin(
        tauri_plugin_global_shortcut::Builder::new().with_handler(|app, shortcut| {
            println!("Shortcut triggered: {:?}", shortcut);
        })
        .build(),
    )
    .setup(|app| {
        // register a global shortcut
        // on macOS, the Cmd key is used
        // on Windows and Linux, the Ctrl key is used
        app.global_shortcut().register("CmdOrCtrl+Y")?;
        Ok(())
    })
```

</TabItem>
</Tabs>

### Migrate to HTTP Plugin

The Rust `tauri::api::http` JavaScript `@tauri-apps/api/http` APIs have been removed. Use the `@tauri-apps/plugin-http` plugin instead:

1. Add to cargo dependencies:

```toml