# Source: https://docs.unstructured.io/ui/destinations/pinecone.md

# Source: https://docs.unstructured.io/open-source/ingestion/destination-connectors/pinecone.md

# Source: https://docs.unstructured.io/api-reference/workflow/destinations/pinecone.md

# Source: https://docs.unstructured.io/ui/destinations/pinecone.md

# Source: https://docs.unstructured.io/open-source/ingestion/destination-connectors/pinecone.md

# Source: https://docs.unstructured.io/api-reference/workflow/destinations/pinecone.md

# Source: https://docs.unstructured.io/ui/destinations/pinecone.md

# Source: https://docs.unstructured.io/open-source/ingestion/destination-connectors/pinecone.md

# Source: https://docs.unstructured.io/api-reference/workflow/destinations/pinecone.md

# Pinecone

<Note>
  If you're new to Unstructured, read this note first.

  Before you can create a destination connector, you must first sign in to your Unstructured account:

  * If you do not already have an Unstructured account, [sign up for free](https://unstructured.io/?modal=try-for-free).
    After you sign up, you are automatically signed in to your new Unstructured **Let's Go** account, at [https://platform.unstructured.io](https://platform.unstructured.io).
    To sign up for a **Business** account instead, [contact Unstructured Sales](https://unstructured.io/?modal=contact-sales), or [learn more](/api-reference/overview#pricing).
  * If you already have an Unstructured **Let's Go**, **Pay-As-You-Go**, or **Business SaaS** account and are not already signed in, sign in to your account at
    [https://platform.unstructured.io](https://platform.unstructured.io). For other types of **Business** accounts, see your Unstructured account administrator for sign-in instructions,
    or email Unstructured Support at [support@unstructured.io](mailto:support@unstructured.io).

  After you sign in, the [Unstructured user interface](/ui/overview) (UI) appears, which you use to get your Unstructured API key.

  1. After you sign in to your Unstructured **Let's Go**, **Pay-As-You-Go**, or **Business** account, click **API Keys** on the sidebar.<br />

     For a **Business** account, before you click **API Keys**, make sure you have selected the organizational workspace you want to create an API key
     for. Each API key works with one and only one organizational workspace. [Learn more](/ui/account/workspaces#create-an-api-key-for-a-workspace).

  2. Click **Generate API Key**.<br />

  3. Follow the on-screen instructions to finish generating the key.<br />

  4. Click the **Copy** icon next to your new key to add the key to your system's clipboard. If you lose this key, simply return and click the **Copy** icon again.<br />

  After you create the destination connector, add it along with a
  [source connector](/api-reference/workflow/sources/overview) to a [workflow](/api-reference/workflow/overview#workflows).
  Then run the worklow as a [job](/api-reference/workflow/overview#jobs). To learn how, try out the
  [hands-on Workflow Endpoint quickstart](/api-reference/workflow/overview#quickstart),
  go directly to the [quickstart notebook](https://colab.research.google.com/github/Unstructured-IO/notebooks/blob/main/notebooks/Unstructured_Platform_Workflow_Endpoint_Quickstart.ipynb),
  or watch the two 4-minute video tutorials for the [Unstructured Python SDK](/api-reference/workflow/overview#unstructured-python-sdk).

  You can also create destination connectors with the Unstructured user interface (UI).
  [Learn how](/ui/destinations/overview).

  If you need help, email Unstructured Support at [support@unstructured.io](mailto:support@unstructured.io).

  You are now ready to start creating a destination connector! Keep reading to learn how.
</Note>

Send processed data from Unstructured to Pinecone.

The requirements are as follows.

<iframe width="560" height="315" src="https://www.youtube.com/embed/Ydj74uBnJyA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

* A Pinecone account. [Get an account](https://app.pinecone.io/).

* A Pinecone API key in your Pinecone account. To create an API key, do the following:

  1. [Sign in to your Pinecone account and open the API keys page](https://app.pinecone.io/organizations/-/projects/-/keys).
  2. Click **+ API key**.
  3. For **API key name**, enter some descriptive name for the API key.
  4. Click **Create key**.
  5. Copy the generated API key to some secure location. You will not be able to access this API key again after you close the dialog.

* A Pinecone serverless index in your Pinecone account.

  Creating a serverless index on your own is optional.
  An index is not required to exist in advance.

  When you set up the connector, at runtime, the index behavior is as follows:

  For the [Unstructured UI](/ui/overview) and [Unstructured API](/api-reference/overview):

  * Your workflow must contain an embedder node, and the embedder node must specify the embedding model that Unstructured will use to generate the embeedings.
  * If an existing index name is specified,
    and the number of dimensions that Unstructured generates does not match the number of dimensions that is specified in the existing index's embedding settings, the run will fail.
    You must change the number of dimensions in your workflow's embedder node or your existing index's embedding settings to match, and try the run again.
  * If an index name is not specified, Unstructured creates a new index in your Pinecone account. The
    new index's name will be `u<short-workflow-id>-<short-embedding-model-name>-<number-of-dimensions>`.

  For [Unstructured Ingest](/open-source/ingestion/overview):

  * If an existing index name is specified, and Unstructured generates embeddings,
    but the number of dimensions that are generated does not match the existing index's embedding settings, the run will fail.
    You must change your Unstructured embedding settings or your existing index's embedding settings to match, and try the run again.
  * If an index name is not specified, Unstructured creates a new index in your Pinecone account. The new index's name will be `unstructuredautocreated`.

  <Note>
    If you create a new index or use an existing one, Unstructured recommends that all records in the target index have a field
    named `record_id` with a string data type.
    Unstructured can use this field to do intelligent document overwrites. Without this field, duplicate documents
    might be written to the index or, in some cases, the operation could fail altogether.
  </Note>

  To create a serverless index on your own, do the following:

  1. [Sign in to your Pinecone account and open the Create a new index page](https://app.pinecone.io/organizations/-/projects/-/create-index/serverless).

  2. For **Enter index name**, enter some descriptive name for the index.

  3. For **Configuration**, select the check box labelled **Custom settings**, or click the tile labelled **Manual configuration**.

     <Warning>
       Do not click any of the other tiles, such as **text-embedding-3-large**. Clicking any of these other tiles will cause Pinecone to generate embeddings instead of
       having Unstructured generate them. If Pinecone generates embeddings instead of Unstructured, this could cause any related Unstructured workflows to fail.
     </Warning>

  4. For **Vector type**, select **Dense**.

  5. For **Dimension**, enter the number of dimensions for the embeddings that Unstructured will generate.

     <Warning>
       The number of dimensions that you enter here must match the number of dimensions for the embedding model that you use in any related Unstructured workflows or ingestion pipelines. If these numbers do not
       match in both places, this could cause any related Unstructured workflows or ingestion pipelines to fail.
     </Warning>

  6. For **Metric**, select **cosine**.

  7. Leave **Capacity mode** set to **Serverless**.

  8. You can leave **Cloud provider** and **Region** set to their default values, or you can select a cloud provider and region that is closest to you, if available.

  9. Click **Create index**.

* Within a Pinecone serverless index, custom [namespaces](https://docs.pinecone.io/guides/index-data/indexing-overview#namespaces) are supported but are not required.

To create a Pinecone destination connector, see the following examples.

<CodeGroup>
  ```python Python SDK theme={null}
  import os

  from unstructured_client import UnstructuredClient
  from unstructured_client.models.operations import CreateDestinationRequest
  from unstructured_client.models.shared import CreateDestinationConnector

  with UnstructuredClient(api_key_auth=os.getenv("UNSTRUCTURED_API_KEY")) as client:
      response = client.destinations.create_destination(
          request=CreateDestinationRequest(
              create_destination_connector=CreateDestinationConnector(
                  name="<name>",
                  type="pinecone",
                  config={
                      "index_name": "<index-name>",
                      "namespace": "<namespace-name>",
                      "api_key": "<api-key>",
                      "batch_size": <batch-size>
                  }
              )
          )
      )

      print(response.destination_connector_information)
  ```

  ```bash curl theme={null}
  curl --request 'POST' --location \
  "$UNSTRUCTURED_API_URL/destinations" \
  --header 'accept: application/json' \
  --header "unstructured-api-key: $UNSTRUCTURED_API_KEY" \
  --header 'content-type: application/json' \
  --data \
  '{
      "name": "<name>",
      "type": "pinecone",
      "config": {
          "index_name" "<index-name>", 
          "namespace": "<namespace-name>",
          "api_key": "<api-key>",
          "batch_size" <batch-size>
      }
  }'
  ```
</CodeGroup>

Replace the preceding placeholders as follows:

* `<name>` (required) - A unique name for this connector.
* `<index-name>` - The name of the index in the Pinecone database. If no value is provided, see the beginning of this article for the behavior at run time.
* `<namespace-name>` - The name of any custom namespace in the Pinecone index to upsert data into. If no value is provided, the default namespace of `default` will be used.
* `<api-key>` (required) - The Pinecone API key.
* `<batch-size>` - The maximum number of records to transmit in a single batch. The default is `50` unless otherwise specified.
