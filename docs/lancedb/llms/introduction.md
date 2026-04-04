# Source: https://docs.lancedb.com/api-reference/introduction.md

# Introduction

> API reference for LanceDB Cloud with Python, JavaScript, and Rust SDK examples.

## Introduction

**LanceDB Cloud REST API** allows you to interact with your remote table using standard HTTP requests.

<Tip>[LanceDB Quickstart](https://lancedb.com/documentation/quickstart/) will get you up and running in 5 minutes!</Tip>

Our [documentation site](https://lancedb.com/documentation/) covers SDK examples in Python, Typescript and Rust.

## Authentication

All HTTP requests to LanceDB APIs must contain an <u>x-api-key</u> header that specifies a valid API key and
must be encoded as JSON or Arrow RPC.

### Get the API Key

1. Go to [LanceDB Cloud](https://accounts.lancedb.com/sign-up) and complete the onboarding.

![create](https://mintlify.s3.us-west-1.amazonaws.com/lancedb-bcbb4faf/assets/create.png)

2. Let's call this particular **Project** `embedding`.
3. Save the API key and the project instance name: `embedding-yhs6bg`.

This is how the Project looks in the LanceDB Cloud Dashboard:
![projects](https://mintlify.s3.us-west-1.amazonaws.com/lancedb-bcbb4faf/assets/projects.png)

4. In your terminal, check the existence of the remote **Project**. Specify the remote LanceDB **Project** `db` and `region`.

```shell
curl -X GET "https://{db}.{region}.api.lancedb.com/v1/tables" \
   -H "Content-Type: application/json" \
   -H "x-api-key: LANCEDB_API_KEY"
```

5. Now, create a **Table** to store data. Let's call it `words`.

```shell
curl -X POST "https://embedding-yhs6bg.us-east-1.api.lancedb.com/v1/tables/words" \
   -H "Content-Type: application/vnd.apache.arrow.stream" \
   -H "x-api-key: LANCEDB_API_KEY"
```

* the `db` is `embedding-yhs6bg`
* the `region` is `us-east-1`
* the name of the table is `words`.

6. Now check that the **Table has** been created:

```shell
curl -X GET "https://embedding-yhs6bg.us-east-1.api.lancedb.com/v1/tables" \
   -H "Content-Type: application/json" \
   -H "x-api-key: LANCEDB_API_KEY"
```

You can always check from the LanceDB Cloud Dashboard:

![words](https://mintlify.s3.us-west-1.amazonaws.com/lancedb-bcbb4faf/assets/words.png)

That's it - you're connected! Now, you can start adding data and querying it.
The best way to start is to try the [LanceDB Quickstart](https://lancedb.com/documentation/quickstart/) or read the [documentation site](https://lancedb.com/documentation/).


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.lancedb.com/llms.txt