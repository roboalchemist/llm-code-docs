# Cargo.toml
[dependencies]
tauri-plugin-fs = "2"
```

2. Use in JavaScript or Rust project:

<Tabs syncKey="lang">
<TabItem label="JavaScript">

```rust
fn main() {
    tauri::Builder::default()
        .plugin(tauri_plugin_fs::init())
}
```

```json
// package.json
{
  "dependencies": {
    "@tauri-apps/plugin-fs": "^2.0.0"
  }
}
```

```javascript
import { mkdir, BaseDirectory } from '@tauri-apps/plugin-fs';
await mkdir('db', { baseDir: BaseDirectory.AppLocalData });
```

Some functions and types have been renamed or removed:

- `Dir` enum alias removed, use `BaseDirectory`.
- `FileEntry`, `FsBinaryFileOption`, `FsDirOptions`, `FsOptions`, `FsTextFileOption` and `BinaryFileContents` interfaces and type aliases have been removed and replaced with new interfaces suited for each function.
- `createDir` renamed to `mkdir`.
- `readBinaryFile` renamed to `readFile`.
- `removeDir` removed and replaced with `remove`.
- `removeFile` removed and replaced with `remove`.
- `renameFile` removed and replaced with `rename`.
- `writeBinaryFile` renamed to `writeFile`.

</TabItem>
<TabItem label="Rust">

Use the Rust [`std::fs`](https://doc.rust-lang.org/std/fs/) functions.

</TabItem>
</Tabs>

### Migrate to Global Shortcut Plugin

The Rust `App::global_shortcut_manager` and `AppHandle::global_shortcut_manager` and JavaScript `@tauri-apps/api/global-shortcut` APIs have been removed. Use the `@tauri-apps/plugin-global-shortcut` plugin instead:

1. Add to cargo dependencies:

```toml