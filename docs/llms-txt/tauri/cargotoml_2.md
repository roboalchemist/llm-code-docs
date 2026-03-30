# Cargo.toml
[dependencies]
tauri-plugin-dialog = "2"
```

2. Use in JavaScript or Rust project:

<Tabs syncKey="lang">
<TabItem label="JavaScript">

```rust
fn main() {
    tauri::Builder::default()
        .plugin(tauri_plugin_dialog::init())
}
```

```json
// package.json
{
  "dependencies": {
    "@tauri-apps/plugin-dialog": "^2.0.0"
  }
}
```

```javascript
import { save } from '@tauri-apps/plugin-dialog';
const filePath = await save({
  filters: [
    {
      name: 'Image',
      extensions: ['png', 'jpeg'],
    },
  ],
});
```

</TabItem>
<TabItem label="Rust">

```rust
use tauri_plugin_dialog::DialogExt;
tauri::Builder::default()
    .plugin(tauri_plugin_dialog::init())
    .setup(|app| {
        app.dialog().file().pick_file(|file_path| {
            // do something with the optional file path here
            // the file path is `None` if the user closed the dialog
        });

        app.dialog().message("Tauri is Awesome!").show();
        Ok(())
     })
```

</TabItem>
</Tabs>

### Migrate to File System Plugin

The Rust `App::get_cli_matches` JavaScript `@tauri-apps/api/fs` APIs have been removed. Use the [`std::fs`](https://doc.rust-lang.org/std/fs/) for Rust and `@tauri-apps/plugin-fs` plugin for JavaScript instead:

1. Add to cargo dependencies:

```toml