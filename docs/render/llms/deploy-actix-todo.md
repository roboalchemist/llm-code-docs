# Source: https://render.com/docs/deploy-actix-todo.md

# Deploy an Actix Web App

You can deploy [Actix](https://actix.rs) [Rust](https://www.rust-lang.org) web apps on Render in just a few clicks.

The app in this guide is based on the official [todo](https://github.com/actix/examples/tree/master/basics/todo) example and available at https://actix-todo.onrender.com.

1. [Create](https://dashboard.render.com/new/database) a new PostgreSQL database on Render and copy the internal DB URL to use below.
2. Fork [render-examples/actix_todo](https://github.com/render-examples/actix_todo) on GitHub.
3. Create a new *Web Service* on Render, and give Render permission to access your new repo.
4. Set the service's *Language* field to `Rust` and use the following values during creation:

   ###### *Build Command*: `./build.sh`

   Here are the contents of the build script:

   ```bash
   #!/usr/bin/env bash
   cargo install sqlx-cli@^0.7 --no-default-features --features=postgres,rustls
   sqlx migrate run
   cargo build --release
   ```

   It's simply executing commands needed to build and deploy an Actix web app on each push to your repo. It also uses the [sqlx](https://github.com/launchbadge/sqlx) CLI to run migrations before each deploy.

   ###### *Start Command*: `cargo run --release`

   ###### Add the following environment variable under the _Advanced_ section:

   | Key            | Value                                                             |
   | -------------- | ----------------------------------------------------------------- |
   | `DATABASE_URL` | The *internal database URL* for the database you created above. |

That's it! Your web service will be live on your Render URL as soon as the build finishes.

Going forward, every push to your repo will automatically build your app and deploy it in production. If the build fails, Render will automatically stop the deploy process and the existing version of your app will keep running until the next successful deploy.

See [Specifying a Rust Toolchain](rust-toolchain) to customize the Rust toolchain for your app.