# Cargo.toml
[dependencies]
tauri-plugin-cli = "2"
```

2. Use in JavaScript or Rust project:

<Tabs syncKey="lang">
<TabItem label="JavaScript">

```rust
fn main() {
    tauri::Builder::default()
        .plugin(tauri_plugin_cli::init())
}
```

```json
// package.json
{
  "dependencies": {
    "@tauri-apps/plugin-cli": "^2.0.0"
  }
}
```

```javascript
import { getMatches } from '@tauri-apps/plugin-cli';
const matches = await getMatches();
```

</TabItem>
<TabItem label="Rust">

```rust
fn main() {
    use tauri_plugin_cli::CliExt;
    tauri::Builder::default()
        .plugin(tauri_plugin_cli::init())
        .setup(|app| {
            let cli_matches = app.cli().matches()?;
            Ok(())
        })
}
```

</TabItem>
</Tabs>

### Migrate to Clipboard Plugin

The Rust `App::clipboard_manager` and `AppHandle::clipboard_manager` and JavaScript `@tauri-apps/api/clipboard` APIs have been removed. Use the `@tauri-apps/plugin-clipboard-manager` plugin instead:

```toml
[dependencies]
tauri-plugin-clipboard-manager = "2"
```

<Tabs syncKey="lang">
<TabItem label="JavaScript">

```rust
fn main() {
    tauri::Builder::default()
        .plugin(tauri_plugin_clipboard_manager::init())
}
```

```json
// package.json
{
  "dependencies": {
    "@tauri-apps/plugin-clipboard-manager": "^2.0.0"
  }
}
```

```javascript
import { writeText, readText } from '@tauri-apps/plugin-clipboard-manager';
await writeText('Tauri is awesome!');
assert(await readText(), 'Tauri is awesome!');
```

</TabItem>
<TabItem label="Rust">

```rust
use tauri_plugin_clipboard::{ClipboardExt, ClipKind};
tauri::Builder::default()
    .plugin(tauri_plugin_clipboard::init())
    .setup(|app| {
        app.clipboard().write(ClipKind::PlainText {
            label: None,
            text: "Tauri is awesome!".into(),
        })?;
        Ok(())
    })
```

</TabItem>
</Tabs>

### Migrate to Dialog Plugin

The Rust `tauri::api::dialog` JavaScript `@tauri-apps/api/dialog` APIs have been removed. Use the `@tauri-apps/plugin-dialog` plugin instead:

1. Add to cargo dependencies:

```toml