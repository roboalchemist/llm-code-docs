# Serverless Semantic Search

Andre Bogus

·

July 12, 2023

![Serverless Semantic Search](https://qdrant.tech/articles_data/serverless/preview/title.jpg)

Do you want to insert a semantic search function into your website or online app? Now you can do so - without spending any money! In this example, you will learn how to create a free prototype search engine for your own non-commercial purposes.

## [Anchor](https://qdrant.tech/articles/serverless/\#ingredients) Ingredients

- A [Rust](https://rust-lang.org/) toolchain
- [cargo lambda](https://cargo-lambda.info/) (install via package manager, [download](https://github.com/cargo-lambda/cargo-lambda/releases) binary or `cargo install cargo-lambda`)
- The [AWS CLI](https://aws.amazon.com/cli)
- Qdrant instance ( [free tier](https://cloud.qdrant.io/) available)
- An embedding provider service of your choice (see our [Embeddings docs](https://qdrant.tech/documentation/embeddings/). You may be able to get credits from [AI Grant](https://aigrant.org/), also Cohere has a [rate-limited non-commercial free tier](https://cohere.com/pricing))
- AWS Lambda account (12-month free tier available)

## [Anchor](https://qdrant.tech/articles/serverless/\#what-youre-going-to-build) What you’re going to build

You’ll combine the embedding provider and the Qdrant instance to a neat semantic search, calling both services from a small Lambda function.

![lambda integration diagram](https://qdrant.tech/articles_data/serverless/lambda_integration.png)

Now lets look at how to work with each ingredient before connecting them.

## [Anchor](https://qdrant.tech/articles/serverless/\#rust-and-cargo-lambda) Rust and cargo-lambda

You want your function to be quick, lean and safe, so using Rust is a no-brainer. To compile Rust code for use within Lambda functions, the `cargo-lambda` subcommand has been built. `cargo-lambda` can put your Rust code in a zip file that AWS Lambda can then deploy on a no-frills `provided.al2` runtime.

To interface with AWS Lambda, you will need a Rust project with the following dependencies in your `Cargo.toml`:

```toml
[dependencies]
tokio = { version = "1", features = ["macros"] }
lambda_http = { version = "0.8", default-features = false, features = ["apigw_http"] }
lambda_runtime = "0.8"

```

This gives you an interface consisting of an entry point to start the Lambda runtime and a way to register your handler for HTTP calls. Put the following snippet into `src/helloworld.rs`:

```rust
use lambda_http::{run, service_fn, Body, Error, Request, RequestExt, Response};

/// This is your callback function for responding to requests at your URL
async fn function_handler(_req: Request) -> Result<Response<Body>, Error> {
    Response::from_text("Hello, Lambda!")
}

#[tokio::main]
async fn main() {
    run(service_fn(function_handler)).await
}

```

You can also use a closure to bind other arguments to your function handler (the `service_fn` call then becomes `service_fn(|req| function_handler(req, ...))`). Also if you want to extract parameters from the request, you can do so using the [Request](https://docs.rs/lambda_http/latest/lambda_http/type.Request.html) methods (e.g. `query_string_parameters` or `query_string_parameters_ref`).

Add the following to your `Cargo.toml` to define the binary:

```toml
[[bin]]
name = "helloworld"
path = "src/helloworld.rs"

```

On the AWS side, you need to setup a Lambda and IAM role to use with your function.

![create lambda web page](https://qdrant.tech/articles_data/serverless/create_lambda.png)

Choose your function name, select “Provide your own bootstrap on Amazon Linux 2”. As architecture, use `arm64`. You will also activate a function URL. Here it is up to you if you want to protect it via IAM or leave it open, but be aware that open end points can be accessed by anyone, potentially costing money if there is too much traffic.

By default, this will also create a basic role. To look up the role, you can go into the Function overview:

![function overview](https://qdrant.tech/articles_data/serverless/lambda_overview.png)

Click on the “Info” link near the “▸ Function overview” heading, and select the “Permissions” tab on the left.

You will find the “Role name” directly under _Execution role_. Note it down for later.

![function overview](https://qdrant.tech/articles_data/serverless/lambda_role.png)

To test that your “Hello, Lambda” service works, you can compile and upload the function:

```bash
$ export LAMBDA_FUNCTION_NAME=hello
$ export LAMBDA_ROLE=<role name from lambda web ui>
$ export LAMBDA_REGION=us-east-1
$ cargo lambda build --release --arm --bin helloworld --output-format zip
  Downloaded libc v0.2.137