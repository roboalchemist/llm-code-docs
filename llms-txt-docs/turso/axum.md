# Source: https://docs.turso.tech/sdk/rust/guides/axum.md

# Turso + Axum

> Set up Turso in your Axum project in minutes

<img src="https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/axum-banner.png?fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=e92d18a8f72196e94541553f254a77b3" alt="Axum banner" data-og-width="1133" width="1133" data-og-height="595" height="595" data-path="images/guides/axum-banner.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/axum-banner.png?w=280&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=bf97083ac7752958846a6a4024787f1c 280w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/axum-banner.png?w=560&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=48b6b7b19875da1dcdfd973969b16de1 560w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/axum-banner.png?w=840&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=eae74778559611606d2ec712b9872652 840w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/axum-banner.png?w=1100&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=07070e8cd61568e2038a786f8f01a42b 1100w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/axum-banner.png?w=1650&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=5574e47b4fe290f4191c4274bd0018ea 1650w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/axum-banner.png?w=2500&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=8fa6e56263a10312c22f9cbad07bb5de 2500w" />

## Prerequisites

Before you start, make sure you:

* [Install the Turso CLI](/cli/installation)
* [Sign up or login to Turso](/cli/authentication#signup)
* Have an Axum app — [learn more](https://github.com/tokio-rs/axum)

<Steps>
  <Step title="Retrieve database credentials">
    You will need an existing database to continue. If you don't have one, [create one](/quickstart).

    <Snippet file="retrieve-database-credentials.mdx" />

    <Info>You will want to store these as environment variables.</Info>
  </Step>

  <Step title="Add the libsql crate to the project">
    ```sh  theme={null}
    cargo add libsql
    ```

    <Note>
      Optionally, you can add a package such as [`dotenvy`](https://docs.rs/dotenvy/latest/dotenvy) to help you work with `.env` files:

      ```sh  theme={null}
      cargo add dotenvy
      ```
    </Note>
  </Step>

  <Step title="Execute SQL">
    ```rust  theme={null}
    use libsql::{Builder, Connection, Database, Result};

    #[tokio::main]
    async fn main() -> Result<()> {
        dotenv().ok();

        let db_url = std::env::var("TURSO_DATABASE_URL").expect("TURSO_DATABASE_URL must be set");
        let auth_token = std::env::var("TURSO_AUTH_TOKEN").expect("TURSO_AUTH_TOKEN must be set");

        let db = Builder::new_remote(db_url, auth_token)
            .build()
            .await?;

        let conn = db.connect()?;

        // Execute a query
        let mut rows = conn.query("SELECT * FROM users", ()).await?;

        while let Some(row) = rows.next().await? {
            let id: i64 = row.get(0)?;
            let name: String = row.get(1)?;
            println!("User: {} - {}", id, name);
        }

        Ok(())
    }
    ```
  </Step>

  <Step title="Use in an Axum handler">
    ```rust  theme={null}
    use axum::{
        extract::State,
        routing::get,
        Json, Router,
    };
    use libsql::{Builder, Connection, Database};
    use serde::Serialize;

    #[derive(Clone)]
    struct AppState {
        db: Database,
    }

    #[derive(Serialize)]
    struct User {
        id: i64,
        name: String,
    }

    async fn get_users(State(state): State<AppState>) -> Json<Vec<User>> {
        let conn = state.db.connect().unwrap();
        let mut rows = conn.query("SELECT id, name FROM users", ()).await.unwrap();

        let mut users = Vec::new();
        while let Some(row) = rows.next().await.unwrap() {
            users.push(User {
                id: row.get(0).unwrap(),
                name: row.get(1).unwrap(),
            });
        }

        Json(users)
    }

    #[tokio::main]
    async fn main() {
        let db_url = std::env::var("TURSO_DATABASE_URL").expect("TURSO_DATABASE_URL must be set");
        let auth_token = std::env::var("TURSO_AUTH_TOKEN").expect("TURSO_AUTH_TOKEN must be set");

        let db = Builder::new_remote(db_url, auth_token)
            .build()
            .await
            .unwrap();

        let app_state = AppState { db };

        let app = Router::new()
            .route("/users", get(get_users))
            .with_state(app_state);

        axum::Server::bind(&"0.0.0.0:3000".parse().unwrap())
            .serve(app.into_make_service())
            .await
            .unwrap();
    }
    ```

    This example creates a shared `Database` instance in the application state, which is then used in the handler to execute queries.
  </Step>
</Steps>
