# Source: https://docs.turso.tech/sdk/rust/guides/actix.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.turso.tech/llms.txt
> Use this file to discover all available pages before exploring further.

# Turso + Actix

> Set up Turso in your Actix project in minutes

<img src="https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/actix-banner.png?fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=4d06a48cc1186caa607491545546e600" alt="Actix banner" data-og-width="1133" width="1133" data-og-height="595" height="595" data-path="images/guides/actix-banner.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/actix-banner.png?w=280&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=8b3a1be0ff68b893ffb52e0d19c89684 280w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/actix-banner.png?w=560&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=7f97b18410c1f093093a1120bd0a884d 560w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/actix-banner.png?w=840&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=3e8b1f399ca826f962dfe82a5cf6b01c 840w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/actix-banner.png?w=1100&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=c1167e8b829243c9956d0bd672fd852f 1100w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/actix-banner.png?w=1650&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=6517991814a6de85ef7a9b7ca118f28f 1650w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/actix-banner.png?w=2500&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=4ebe1f254cea8d7c3423bb3d3224639f 2500w" />

## Prerequisites

Before you start, make sure you:

* [Install the Turso CLI](/cli/installation)
* [Sign up or login to Turso](/cli/authentication#signup)
* Have an Actix app — [learn more](https://actix.rs/docs/getting-started)

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
    #[tokio::main]
    #[actix_web::main]
    async fn main() -> std::io::Result<()> {
        HttpServer::new(|| App::new().route("/", web::get().to(index)).route("/items", web::get().to(get_items)))
            .bind(("127.0.0.1", 8080))?
            .run()
            .await
    }

    async fn get_items() -> Result<HttpResponse, Error> {
        dotenv().expect(".env file not found");

        let db_url = env::var("TURSO_DATABASE_URL").unwrap();
        let auth_token = env::var("TURSO_AUTH_TOKEN").unwrap();
        let db_file = env::var("LOCAL_DB").unwrap();

        let db = Builder::new_remote_replica(db_file, url, auth_token)
        .read_your_writes(true)
        .build()
        .await
        .unwrap();

        let conn = db.connect().unwrap();

        let mut results = conn.query("SELECT * FROM items", ()).await.unwrap();

        let mut items: Vec<T> = Vec::new();

        while let Some(row) = results.next().await.unwrap() {
            let item: Item = Item {
                task: row.get(0).unwrap(),
            };
            items.push(item);
        }

        Ok(HttpResponse::Ok().json(items))
    }
    ```
  </Step>
</Steps>

## Examples

<CardGroup cols={2}>
  <Card title="Turso + Actix Web Traffic Tracker" icon="github" href="https://github.com/tursodatabase/examples/tree/master/app-web-traffic-tracker-actix">
    See the full source code
  </Card>
</CardGroup>
