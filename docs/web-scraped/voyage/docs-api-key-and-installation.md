# Source: https://docs.voyageai.com/docs/api-key-and-installation

## GET STARTED 

- [[[Introduction]]](/docs/introduction)
- [[[API Key and Python Client]]](/docs/api-key-and-installation)
- [[[Quickstart Tutorial]]](/docs/quickstart-tutorial)

## CAPABILITIES 

- [[[Text Embeddings]]](/docs/embeddings)
- [[[Contextualized Chunk Embeddings]]](/docs/contextualized-chunk-embeddings)
- [[[Multimodal Embeddings]]](/docs/multimodal-embeddings)
- [[[Rerankers]]](/docs/reranker)

## GUIDES 

- [[[Tokenization]]](/docs/tokenization)
- [[[Flexible Dimensions and Quantization]]](/docs/flexible-dimensions-and-quantization)
- [[[Batch Inference]]](/docs/batch-inference)
- [[[Error Codes]]](/docs/error-codes)
- [[[Rate Limits]]](/docs/rate-limits)
- [[[Pricing]]](/docs/pricing)
- [[[Organizations and Projects]]](/docs/organizations-and-projects)
- [[[Service Level Objectives]]](/docs/service-level-objectives)

## DEPLOYMENT ON VPC 

- [[AWS Marketplace Model Package]]
  - [[[MongoDB Voyage AI Models in AWS]]](/docs/aws-marketplace-mongodb-voyage)
  - [[[Voyage AI Models in AWS]]](/docs/aws-marketplace-voyage)
- [[Azure Marketplace Managed Application]]
  - [[[MongoDB Voyage AI Models in Azure]]](/docs/azure-marketplace-mongodb-voyage)
  - [[[Voyage AI Models in Azure]]](/docs/azure-marketplace-voyage)

## ACCESS VIA DATA PLATFORMS 

- [[[Snowflake]]](/docs/snowflake)

## Community 

- [[[Integrations]]](/docs/integrations-and-other-libraries)
- [[[Community SDKs]]](/docs/community-sdks)

## HELP 

- [[[FAQ]]](/docs/faq)
- [[[Contact Email]]](/docs/contact-email)
- [[[Discord]]](/docs/discord)

Powered by [](https://readme.com?ref_src=hub&project=voyage-ai)

# API Key and Python Client

##  

Authentication with API Keys

[](#authentication-with-api-keys)

Voyage AI utilizes API keys to monitor usage and manage permissions. To obtain your key, please sign in with your Voyage AI account and click the \"Create new secret key\" button in the [**API keys**](https://dashboard.voyageai.com/organization/api-keys) section of the Voyage [dashboard](https://dashboard.voyageai.com/organization/api-keys). We recommend setting the API key as an environment variable. For example, in MacOS or Linux, type the following command in the terminal, replacing `<your secret key>` with your actual API key:

Shell

    export VOYAGE_API_KEY="<your secret key>"

You can verify the setup by typing `echo $VOYAGE_API_KEY` in the terminal. It should display your API key.

Your API key is supposed to be secret \-- please avoid sharing it or exposing it in browsers or apps. Please store your API key securely for future use.

##  

Install Voyage Python Package

[](#install-voyage-python-package)

You can interact with the API through HTTP requests from any language. For Python users, we offer an official package which can be installed via `pip` :

Shell

    pip install -U voyageai

We recommend using the `-U` or `--upgrade` option to ensure you are installing the latest version of the package. This helps you access the most recent features and bug fixes.

After installation, you can test it by running:

Shell

    python -c "import voyageai"

The installation is successful if this command runs without any errors.

##  

`voyageai.Client`

[](#voyageaiclient)

The Python package offers the `voyageai.Client` class as the interface to invoke Voyage\'s API. You can create a client object and use it to access the predictions by our models.

[`class voyageai.Client`](https://github.com/voyage-ai/voyageai-python/blob/main/voyageai/client.py)

**Parameters**

- **api_key** (str, optional, defaults to
  `None`) - Voyage API key. If
  `None`, the client will search for the API key in the following order:
  - `voyageai.api_key_path`, path to the file containing the key;
  - environment variable
    `VOYAGE_API_KEY_PATH`, which can be set to the path to the file containing the key;
  - `voyageai.api_key`, an attribute of the
    `voyageai` module, which can be used to store the key;
  - environment variable
    `VOYAGE_API_KEY`.
- **max_retries** (int, defaults to 0) - Maximum number of retries for each API request in case of rate limit errors or temporary server unavailability. The client employs a wait-and-retry strategy to handle such errors, and will raise an exception upon reaching the maximum retry limit. By default, the client does not retry.
- **timeout** (int, optional, defaults to
  `None`) - Maximum time in seconds to wait for a response from the API before aborting the request. If the specified timeout is exceeded, the request is terminated and a timeout exception is raised. By default, no timeout constraint is enforced.

**Example**

Python

    import voyageai

    vo = voyageai.Client()
    # This will automatically use the environment variable VOYAGE_API_KEY.
    # Alternatively, you can use vo = voyageai.Client(api_key="<your secret key>")

    result = vo.embed(["hello world"], model="voyage-3.5")

##  

Asynchronous Requests

[](#asynchronous-requests)

The following client-side code serves as a reference for handling high-concurrency and/or asynchronous (non-blocking) requests.

Python

    import asyncio
    import os

    import aiohttp

    async def main():
        # Number of concurrent workers (coroutines) to run in parallel
        # Each worker will make requests independently
        concurrency = 10

        async def sending_coroutine(t: int, session: aiohttp.ClientSession) -> None:
            """
            Worker coroutine that makes multiple sequential API requests.

            Args:
                t: Worker ID number for tracking/debugging
                session: Shared aiohttp session for connection pooling

            Each worker makes 100 requests sequentially, sharing the same
            session across all requests to reuse TCP connections.
            """
            # Each worker makes 100 requests
            for i in range(100):
                # Use async context manager to ensure response is properly closed
                async with session.post(
                    # Update for your endpoint, model, and input data
                    # "a " * 1000 creates a ~1000-token string to test larger payloads
                    f"https://api.voyageai.com/v1/embeddings",
                    headers="},
                    json=
                ) as response:
                    assert response.status == 200, (
                        f"Response status code : "
                    )
                    # Log progress showing which worker and which iteration
                    print(f"Processed request  in thread ")

        # Create a single session to be shared across all workers
        # This enables connection pooling and reduces overhead
        async with aiohttp.ClientSession() as session:
            # asyncio.gather runs all coroutines concurrently
            # The * operator unpacks the list comprehension into separate arguments
            # Creates 10 workers (t=0 through t=9), each sharing the same session
            await asyncio.gather(
                *[sending_coroutine(t, session) for t in range(concurrency)],
            )

    if __name__ == "__main__":
        # Entry point: starts the async event loop and runs main()
        # asyncio.run() handles event loop creation, execution, and cleanup
        asyncio.run(main())

Updated 22 days ago

------------------------------------------------------------------------

[[]](/docs/introduction)

Introduction

[](/docs/quickstart-tutorial)

Quickstart Tutorial

[]

- [Table of Contents](#)
- - [Authentication with API Keys](#authentication-with-api-keys)
  - [Install Voyage Python Package](#install-voyage-python-package)
  - [voyageai.Client](#voyageaiclient)
  - [Asynchronous Requests](#asynchronous-requests)