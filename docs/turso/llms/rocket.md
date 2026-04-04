# Source: https://docs.turso.tech/sdk/rust/guides/rocket.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.turso.tech/llms.txt
> Use this file to discover all available pages before exploring further.

# Turso + Rocket

> Set up Turso in your Rocket project in minutes

<img src="https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/rocket-banner.png?fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=74dabf48dfb2a2ec82d5750672eab0e9" alt="Rocket banner" data-og-width="1133" width="1133" data-og-height="595" height="595" data-path="images/guides/rocket-banner.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/rocket-banner.png?w=280&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=79c495f110640528a720e6d12211e35f 280w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/rocket-banner.png?w=560&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=db1326a6701c4d0ea44385ac5326b9ff 560w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/rocket-banner.png?w=840&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=0bceb710baa09c0157d946ba8b117aa5 840w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/rocket-banner.png?w=1100&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=9b851ad8ba5c332c1593360c1cfbc15c 1100w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/rocket-banner.png?w=1650&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=9252aba70541fa4a8f4b9eb3c2945ec4 1650w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/rocket-banner.png?w=2500&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=5e72dd784c997c914335c463056a3329 2500w" />

## Prerequisites

Before you start, make sure you:

* [Install the Turso CLI](/cli/installation)
* [Sign up or login to Turso](/cli/authentication#signup)
* Have a Rocket app — [learn more](https://rocket.rs/v0.5/guide/getting-started/)

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
    #[get("/todos")]
    async fn get_todos() -> Json<Vec<Todo>> {
        dotenv().expect(".env file not found");

        let url = env::var("TURSO_DATABASE_URL").expect("TURSO_DATABASE_URL not found!");
        let token = env::var("TURSO_AUTH_TOKEN").expect("TURSO_AUTH_TOKEN not found!");

        let db = Database::open_remote(url, token).unwrap();
        let conn = db.connect().unwrap();

        let mut response = conn.query("select * from todos", ()).await.unwrap();

        let mut todos: Vec<Todo> = Vec::new();
        while let Some(row) = response.next().unwrap() {
            let todo: Todo = Todo {
                task: row.get(0).unwrap(),
            };
            todos.push(todo);
        }

        Json(todos)
    }

    #[launch]
    fn rocket() -> _ {
        dotenv().ok();
        rocket::build().mount("/", routes![get_todos])
    }
    ```
  </Step>
</Steps>

## Examples

<CardGroup cols={2}>
  <Card title="Turso + Rocket Todo List" icon="github" href="https://github.com/tursodatabase/examples/tree/master/app-todo-rocket">
    See the full source code
  </Card>
</CardGroup>
