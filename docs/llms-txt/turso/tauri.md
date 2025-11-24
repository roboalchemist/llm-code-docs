# Source: https://docs.turso.tech/sdk/rust/guides/tauri.md

# Tauri + Turso

> Set up Turso in your Tauri project in minutes

<img src="https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/tauri-banner.png?fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=92bdd8d06ba15875c3c553650796b77d" alt="Tauri banner" data-og-width="1133" width="1133" data-og-height="595" height="595" data-path="images/guides/tauri-banner.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/tauri-banner.png?w=280&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=0a7bad4818f5aa4c4abff5814f24a531 280w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/tauri-banner.png?w=560&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=95abd25b2f34c5e3c4aa66bdf96e7c2f 560w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/tauri-banner.png?w=840&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=b57c63cf21ba58ef19000163344a7902 840w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/tauri-banner.png?w=1100&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=6e04691ec86f779bf627348676652415 1100w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/tauri-banner.png?w=1650&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=5be3ffcb6e0e77a221f72d65f06f4113 1650w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/tauri-banner.png?w=2500&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=828d2c7045e3a39c13e3563913fbdbf5 2500w" />

## Prerequisites

Before you start, make sure you:

* [Install the Turso CLI](/cli/installation)
* [Sign up or login to Turso](/cli/authentication#signup)
* Have a Tauri app — [learn more](https://tauri.app/v1/guides/getting-started/setup)

<Steps>
  <Step title="Add the following crates to the Tauri project's dependencies">
    ```toml src-tauri/Cargo.toml theme={null}
    [dependencies]
    serde_json = "1.0"
    serde = { version = "1.0", features = ["derive"] }
    reqwest = { version = "0.11.22", features = ["json", "blocking"] }
    dotenvy = "0.15.7"
    tokio = { version = "1", features = ["full"] }
    libsql = { git = "https://github.com/tursodatabase/libsql" }
    tracing-subscriber = "0.3"
    tracing = "0.1.40"

    [patch.crates-io]
    sqlite3-parser = { git = "https://github.com/LucioFranco/lemon-rs" }
    ```
  </Step>

  <Step title="Fetch Rust dependencies inside the `src-tauri` directory.">
    ```bash  theme={null}
    cargo fetch
    ```
  </Step>

  <Step title="Configure database credentials">
    Get the database URL.

    ```bash  theme={null}
    turso db show --url <database-name>
    ```

    Get the database authentication token.

    ```bash  theme={null}
    turso db tokens create <database-name>
    ```

    Assign acquired credentials to the environment variables inside `src-tauri/.env`.

    ```bash src-tauri/.env theme={null}
    TURSO_SYNC_URL="..."
    TURSO_AUTH_TOKEN="..."
    DB_PATH=./my-data.db # embedded replica
    ```
  </Step>

  <Step title="Execute SQL">
    ```rust src-tauri/src/main.rs theme={null}
    use dotenvy::dotenv;
    use libsql::{params, Database};
    use serde::{Deserialize, Serialize};
    use std::env;

    use tracing::info;

    #[derive(Serialize, Debug)]
    struct Error {
        msg: String,
    }

    type Result<T> = std::result::Result<T, Error>;

    impl<T> From<T> for Error
    where
        T: std::error::Error,
    {
        fn from(value: T) -> Self {
            Self {
                msg: value.to_string(),
            }
        }
    }

    #[derive(Deserialize, Serialize, Debug)]
    pub struct Item {
        id: String,
        foo: String,
        bar: String,
    }

    #[tauri::command]
    async fn get_all_items() -> Result<Vec<Item>> {
        dotenv().expect(".env file not found");

        let db_path = env::var("DB_PATH").unwrap();
        let sync_url = env::var("TURSO_SYNC_URL").unwrap();
        let auth_token = env::var("TURSO_AUTH_TOKEN").unwrap();

        let db = Database::open_with_remote_sync(db_path, sync_url, auth_token).await?;

        let conn = db.connect()?;

        let mut results = conn
            .query("SELECT * FROM table_name", ())
            .await?;

        let mut items: Vec<Item> = Vec::new();
        while let Some(row) = results.next()? {
            let note: Item = Item {
                id: row.get(0)?,
                foo: row.get(1)?,
                bar: row.get(2)?,
            };
            items.push(item);
        }

        Ok(items)
    }

    fn main() {
        tracing_subscriber::fmt::init();

        tauri::Builder::default()
            .invoke_handler(tauri::generate_handler![
                get_all_items,
            ])
            .run(tauri::generate_context!())
            .expect("error while running tauri application");
    }
    ```
  </Step>
</Steps>

## Examples

<CardGroup cols={2}>
  <Card title="Personal Notes App" icon="github" href="https://github.com/tursodatabase/examples/tree/master/app-turso-notes">
    See the full source code
  </Card>
</CardGroup>
