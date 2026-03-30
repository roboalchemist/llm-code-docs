# Source: https://render.com/docs/deploy-rocket-rust.md

# Deploy a Rust Web App with Rocket

You can use Render to host a [Rust](https://www.rust-lang.org) web application built with [Rocket](https://rocket.rs/) in just a few clicks.

The app in this guide is based on Rocket's [Hello](https://github.com/rwf2/Rocket/tree/master/examples/hello) example.

1. Fork [render-examples/rocket-rust-hello-world](https://github.com/render-examples/rocket-rust-hello-world) on GitHub.
2. Create a new *Web Service* on Render, and give Render permission to access your new repo.
3. Use the following values during creation:

   |                   |                         |
   | ----------------- | ----------------------- |
   | *Language*      | `Rust`                  |
   | *Build Command* | `cargo build --release` |
   | *Start Command* | `cargo run --release`   |

That's it! Your web service will be live on your Render URL as soon as the build finishes.

Going forward, every push to your repo will automatically build your app and deploy it in production. If the build fails, Render will automatically stop the deploy process and the existing version of your app will keep running until the next successful deploy.