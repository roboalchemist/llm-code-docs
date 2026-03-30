# Cargo.toml
[dependencies]
tauri-plugin-http = "2"
```

2. Use in JavaScript or Rust project:

<Tabs syncKey="lang">
<TabItem label="JavaScript">

```rust
fn main() {
    tauri::Builder::default()
        .plugin(tauri_plugin_http::init())
}
```

```json
// package.json
{
  "dependencies": {
    "@tauri-apps/plugin-http": "^2.0.0"
  }
}
```

```javascript
import { fetch } from '@tauri-apps/plugin-http';
const response = await fetch(
  'https://raw.githubusercontent.com/tauri-apps/tauri/dev/package.json'
);
```

</TabItem>
<TabItem label="Rust">

```rust
use tauri_plugin_http::reqwest;

tauri::Builder::default()
    .plugin(tauri_plugin_http::init())
    .setup(|app| {
        let response_data = tauri::async_runtime::block_on(async {
            let response = reqwest::get(
                "https://raw.githubusercontent.com/tauri-apps/tauri/dev/package.json",
            )
            .await
            .unwrap();
            response.text().await
        })?;
        Ok(())
    })
```

The HTTP plugin re-exports [reqwest](https://docs.rs/reqwest/latest/reqwest/) so you can check out their documentation for more information.

</TabItem>
</Tabs>

### Migrate to Notification Plugin

The Rust `tauri::api::notification` JavaScript `@tauri-apps/api/notification` APIs have been removed. Use the `@tauri-apps/plugin-notification` plugin instead:

1. Add to cargo dependencies:

```toml