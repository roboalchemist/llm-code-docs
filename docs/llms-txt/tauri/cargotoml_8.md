# Cargo.toml
[dependencies]
tauri-plugin-process = "2"
```

2. Use in JavaScript or Rust project:

<Tabs syncKey="lang">
<TabItem label="JavaScript">

```rust
fn main() {
    tauri::Builder::default()
        .plugin(tauri_plugin_process::init())
}
```

```json
// package.json
{
  "dependencies": {
    "@tauri-apps/plugin-process": "^2.0.0"
  }
}
```

```javascript
import { exit, relaunch } from '@tauri-apps/plugin-process';
await exit(0);
await relaunch();
```

</TabItem>
<TabItem label="Rust">

```rust
fn main() {
    tauri::Builder::default()
        .plugin(tauri_plugin_process::init())
        .setup(|app| {
            // exit the app with a status code
            app.handle().exit(1);
            // restart the app
            app.handle().restart();
            Ok(())
        })
}
```

</TabItem>
</Tabs>

### Migrate to Shell Plugin

The Rust `tauri::api::shell` JavaScript `@tauri-apps/api/shell` APIs have been removed. Use the `@tauri-apps/plugin-shell` plugin instead:

1. Add to cargo dependencies:

```toml