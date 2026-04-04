# Source: https://render.com/docs/deploy-rust-graphql.md

# Deploy a Rust GraphQL Server with Juniper

You can use Render to host a [Rust](https://www.rust-lang.org) GraphQL server built with [Juniper](https://graphql-rust.github.io/) in just a few clicks.

The app in this guide is based on the official [juniper_rocket](https://github.com/graphql-rust/juniper/tree/master/juniper_rocket) example
and uses [GraphQL Playground](https://github.com/prisma/graphql-playground/) and Juniper `master`.

1. Fork [render-examples/rust-graphql](https://github.com/render-examples/rust-graphql) on GitHub.

2. Create a new *Web Service* on Render, and give Render permission to access your new repo.

3. Use the following values during creation:

   |                   |                         |
   | ----------------- | ----------------------- |
   | *Language*      | `Rust`                  |
   | *Build Command* | `cargo build --release` |
   | *Start Command* | `cargo run --release`   |

That's it! Your web service will be live on your Render URL as soon as the build finishes.

Use the GraphQL query below to start exploring the schema!

```graphql
query {
  human(id: "1002") {
    id
    name
    friends {
      id
      name
    }
    appearsIn
  }
}
```

Going forward, every push to your repo will automatically build your app and deploy it in production. If the build fails, Render will automatically stop the deploy process and the existing version of your app will keep running until the next successful deploy.

See [Specifying a Rust Toolchain](rust-toolchain) to customize the Rust toolchain for your app.