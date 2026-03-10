# [..] output omitted for brevity
    Finished release [optimized] target(s) in 1m 27s
$ # Delete the old empty definition
$ aws lambda delete-function-url-config --region $LAMBDA_REGION --function-name $LAMBDA_FUNCTION_NAME
$ aws lambda delete-function --region $LAMBDA_REGION --function-name $LAMBDA_FUNCTION_NAME
$ # Upload the function
$ aws lambda create-function --function-name $LAMBDA_FUNCTION_NAME \
    --handler bootstrap \
    --architectures arm64 \
    --zip-file fileb://./target/lambda/helloworld/bootstrap.zip \
    --runtime provided.al2 \
    --region $LAMBDA_REGION \
    --role $LAMBDA_ROLE \
    --tracing-config Mode=Active
$ # Add the function URL
$ aws lambda add-permission \
    --function-name $LAMBDA_FUNCTION_NAME \
    --action lambda:InvokeFunctionUrl \
    --principal "*" \
    --function-url-auth-type "NONE" \
    --region $LAMBDA_REGION \
    --statement-id url
$ # Here for simplicity unauthenticated URL access. Beware!
$ aws lambda create-function-url-config \
    --function-name $LAMBDA_FUNCTION_NAME \
    --region $LAMBDA_REGION \
    --cors "AllowOrigins=*,AllowMethods=*,AllowHeaders=*" \
    --auth-type NONE

```

Now you can go to your _Function Overview_ and click on the Function URL. You should see something like this:

```text
Hello, Lambda!

```

Bearer ! You have set up a Lambda function in Rust. On to the next ingredient:

## [Anchor](https://qdrant.tech/articles/serverless/\#embedding) Embedding

Most providers supply a simple https GET or POST interface you can use with an API key, which you have to supply in an authentication header. If you are using this for non-commercial purposes, the rate limited trial key from Cohere is just a few clicks away. Go to [their welcome page](https://dashboard.cohere.ai/welcome/register), register and you’ll be able to get to the dashboard, which has an “API keys” menu entry which will bring you to the following page:
[cohere dashboard](https://qdrant.tech/articles_data/serverless/cohere-dashboard.png)

From there you can click on the ⎘ symbol next to your API key to copy it to the clipboard. _Don’t put your API key in the code!_ Instead read it from an env variable you can set in the lambda environment. This avoids accidentally putting your key into a public repo. Now all you need to get embeddings is a bit of code. First you need to extend your dependencies with `reqwest` and also add `anyhow` for easier error handling:

```toml
anyhow = "1.0"
reqwest =  { version = "0.11.18", default-features = false, features = ["json", "rustls-tls"] }
serde = "1.0"

```

Now given the API key from above, you can make a call to get the embedding vectors:

```rust
use anyhow::Result;
use serde::Deserialize;
use reqwest::Client;

#[derive(Deserialize)]
struct CohereResponse { outputs: Vec<Vec<f32>> }

pub async fn embed(client: &Client, text: &str, api_key: &str) -> Result<Vec<Vec<f32>>> {
    let CohereResponse { outputs } = client
        .post("https://api.cohere.ai/embed")
        .header("Authorization", &format!("Bearer {api_key}"))
        .header("Content-Type", "application/json")
        .header("Cohere-Version", "2021-11-08")
        .body(format!("{{\"text\":[\"{text}\"],\"model\":\"small\"}}"))
        .send()
        .await?
        .json()
        .await?;
    Ok(outputs)
}

```

Note that this may return multiple vectors if the text overflows the input dimensions.
Cohere’s `small` model has 1024 output dimensions.

Other providers have similar interfaces. Consult our [Embeddings docs](https://qdrant.tech/documentation/embeddings/) for further information. See how little code it took to get the embedding?

While you’re at it, it’s a good idea to write a small test to check if embedding works and the vectors are of the expected size:

```rust
#[tokio::test]
async fn check_embedding() {
    // ignore this test if API_KEY isn't set
    let Ok(api_key) = &std::env::var("API_KEY") else { return; }
    let embedding = crate::embed("What is semantic search?", api_key).unwrap()[0];
    // Cohere's `small` model has 1024 output dimensions.
    assert_eq!(1024, embedding.len());
}

```

Run this while setting the `API_KEY` environment variable to check if the embedding works.

## [Anchor](https://qdrant.tech/articles/serverless/\#qdrant-search) Qdrant search

Now that you have embeddings, it’s time to put them into your Qdrant. You could of course use `curl` or `python` to set up your collection and upload the points, but as you already have Rust including some code to obtain the embeddings, you can stay in Rust, adding `qdrant-client` to the mix.

```rust
use anyhow::Result;
use qdrant_client::prelude::*;
use qdrant_client::qdrant::{VectorsConfig, VectorParams};
use qdrant_client::qdrant::vectors_config::Config;
use std::collections::HashMap;

fn setup<'i>(
    embed_client: &reqwest::Client,
    embed_api_key: &str,
    qdrant_url: &str,
    api_key: Option<&str>,
    collection_name: &str,
    data: impl Iterator<Item = (&'i str, HashMap<String, Value>)>,
) -> Result<()> {
    let mut config = QdrantClientConfig::from_url(qdrant_url);
    config.api_key = api_key;
    let client = QdrantClient::new(Some(config))?;

    // create the collections
    if !client.has_collection(collection_name).await? {
        client
            .create_collection(&CreateCollection {
                collection_name: collection_name.into(),
                vectors_config: Some(VectorsConfig {
                    config: Some(Config::Params(VectorParams {
                        size: 1024, // output dimensions from above
                        distance: Distance::Cosine as i32,
                        ..Default::default()
                    })),
                }),
                ..Default::default()
            })
            .await?;
    }
    let mut id_counter = 0_u64;
    let points = data.map(|(text, payload)| {
        let id = std::mem::replace(&mut id_counter, *id_counter + 1);
        let vectors = Some(embed(embed_client, text, embed_api_key).unwrap());
        PointStruct { id, vectors, payload }
    }).collect();
    client.upsert_points(collection_name, points, None).await?;
    Ok(())
}

```

Depending on whether you want to efficiently filter the data, you can also add some indexes. I’m leaving this out for brevity. Also this does not implement chunking (splitting the data to upsert in multiple requests, which avoids timeout errors).

Add a suitable `main` method and you can run this code to insert the points (or just use the binary from the example). Be sure to include the port in the `qdrant_url`.

Now that you have the points inserted, you can search them by embedding:

```rust
use anyhow::Result;
use qdrant_client::prelude::*;
pub async fn search(
    text: &str,
    collection_name: String,
    client: &Client,
    api_key: &str,
    qdrant: &QdrantClient,
) -> Result<Vec<ScoredPoint>> {
    Ok(qdrant.search_points(&SearchPoints {
        collection_name,
        limit: 5, // use what fits your use case here
        with_payload: Some(true.into()),
        vector: embed(client, text, api_key)?,
        ..Default::default()
    }).await?.result)
}

```

You can also filter by adding a `filter: ...` field to the `SearchPoints`, and you will likely want to process the result further, but the example code already does that, so feel free to start from there in case you need this functionality.

## [Anchor](https://qdrant.tech/articles/serverless/\#putting-it-all-together) Putting it all together

Now that you have all the parts, it’s time to join them up. Now copying and wiring up the snippets above is left as an exercise to the reader.

You’ll want to extend the `main` method a bit to connect with the Client once at the start, also get API keys from the environment so you don’t need to compile them into the code. To do that, you can get them with `std::env::var(_)` from the rust code and set the environment from the AWS console.

```bash
$ export QDRANT_URI=<qour Qdrant instance URI including port>
$ export QDRANT_API_KEY=<your Qdrant API key>
$ export COHERE_API_KEY=<your Cohere API key>
$ export COLLECTION_NAME=site-cohere
$ aws lambda update-function-configuration \
    --function-name $LAMBDA_FUNCTION_NAME \
    --environment "Variables={QDRANT_URI=$QDRANT_URI,\
        QDRANT_API_KEY=$QDRANT_API_KEY,COHERE_API_KEY=${COHERE_API_KEY},\
        COLLECTION_NAME=${COLLECTION_NAME}"`

```

In any event, you will arrive at one command line program to insert your data and one Lambda function. The former can just be `cargo run` to set up the collection. For the latter, you can again call `cargo lambda` and the AWS console:

```bash
$ export LAMBDA_FUNCTION_NAME=search
$ export LAMBDA_REGION=us-east-1
$ cargo lambda build --release --arm --output-format zip
  Downloaded libc v0.2.137