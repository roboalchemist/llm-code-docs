# Cargo.toml
[dependencies]
tauri-plugin-os = "2"
```

2. Use in JavaScript or Rust project:

<Tabs syncKey="lang">
<TabItem label="JavaScript">

```rust
fn main() {
    tauri::Builder::default()
        .plugin(tauri_plugin_os::init())
}
```

```json
// package.json
{
  "dependencies": {
    "@tauri-apps/plugin-os": "^2.0.0"
  }
}
```

```javascript
import { arch } from '@tauri-apps/plugin-os';
const architecture = await arch();
```

</TabItem>
<TabItem label="Rust">

```rust
fn main() {
    tauri::Builder::default()
        .plugin(tauri_plugin_os::init())
        .setup(|app| {
            let os_arch = tauri_plugin_os::arch();
            Ok(())
        })
}
```

</TabItem>
</Tabs>

### Migrate to Process Plugin

The Rust `tauri::api::process` JavaScript `@tauri-apps/api/process` APIs have been removed. Use the `@tauri-apps/plugin-process` plugin instead:

1. Add to cargo dependencies:

```toml