# Source: https://docs.unstructured.io/ui/destinations/astradb.md

# Source: https://docs.unstructured.io/open-source/ingestion/source-connectors/astradb.md

# Source: https://docs.unstructured.io/open-source/ingestion/destination-connectors/astradb.md

# Source: https://docs.unstructured.io/api-reference/workflow/destinations/astradb.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.unstructured.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Astra DB

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
  the notebook [Dropbox-To-Pinecone Connector API Quickstart for Unstructured](https://colab.research.google.com/github/Unstructured-IO/notebooks/blob/main/notebooks/Dropbox_To_Pinecone_Connector_Quickstart.ipynb),
  or watch the two 4-minute video tutorials for the [Unstructured Python SDK](/api-reference/workflow/overview#unstructured-python-sdk).

  You can also create destination connectors with the Unstructured user interface (UI).
  [Learn how](/ui/destinations/overview).

  If you need help, email Unstructured Support at [support@unstructured.io](mailto:support@unstructured.io).

  You are now ready to start creating a destination connector! Keep reading to learn how.
</Note>

Send processed data from Unstructured to Astra DB.

The requirements are as follows.

<iframe width="560" height="315" src="https://www.youtube.com/embed/PMs1iwL52aM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

* An IBM Cloud account or DataStax account.

  * For an IBM Cloud account, [sign up](https://cloud.ibm.com/registration) for an IBMid, and then [sign in](https://accounts.datastax.com/session-service/v1/login) to DataStax with your IBMid.
  * For a DataStax account, [sign up](https://astra.datastax.com/signup) for a DataStax account, and then [sign in](https://accounts.datastax.com/session-service/v1/login) to DataStax with your DataStax account.

* An Astra DB database in the DataStax account. To create a database:

  a. After you sign in to DataStax, click **Create database**.<br />
  b. Click the **Serverless (vector)** tile, if it is not already selected.<br />
  c. For **Database name**, enter some unique name for the database.<br />
  d. Select a **Provider** and a **Region**, and then click **Create database**.<br />

  [Learn more](https://docs.datastax.com/en/astra-db-classic/databases/manage-create.html).

* An application token for the database. To create an application token:

  a. After you sign in to DataStax, in the list of databases, click the name of the target database.<br />
  b. On the **Overview** tab, under **Database Details**, in the **Application Tokens** tile, click **Generate Token**.<br />
  c. Enter some **Token description** and select and **Expiration** time period, and then click **Generate token**.<br />
  d. Save the application token that is displayed to a secure location, and then click **Close**.<br />

  [Learn more](https://docs.datastax.com/en/astra-db-serverless/administration/manage-application-tokens.html).

* A keyspace in the database. To create a keyspace:

  a. After you sign in to DataStax, in the list of databases, click the name of the target database.<br />
  b. On the **Data Explorer** tab, in the **Keyspace** list, select **Create keyspace**.<br />
  c. Enter some **Keyspace name**, and then click **Add keyspace**.<br />

  [Learn more](https://docs.datastax.com/en/astra-db-serverless/databases/manage-keyspaces.html#keyspaces).

* A collection in the keyspace.

  For the [Unstructured UI](/ui/overview) and [Unstructured API](/api-reference/overview):

  * An existing collection is not required. At runtime, the collection behavior is as follows:

    * If an existing collection name is specified, and Unstructured generates embeddings,
      but the number of dimensions that are generated does not match the existing collection's embedding settings, the run will fail.
      You must change your Unstructured embedding settings or your existing collection's embedding settings to match, and try the run again.
    * If a collection name is not specified, Unstructured creates a new collection in your keyspace. If Unstructured generates embeddings,
      the new collection's name will be `u<short-workflow-id>_<short-embedding-model-name>_<number-of-dimensions>`.
      If Unstructured does not generate embeddings, the new collection's name will be `u<short-workflow-id`.

  For [Unstructured Ingest](/open-source/ingestion/overview):

  * For the source connector only, an existing collection is required.
  * For the destination connector only, an existing collection is not required. At runtime, the collection behavior is as follows:

    * If an existing collection name is specified, and Unstructured generates embeddings,
      but the number of dimensions that are generated does not match the existing collection's embedding settings, the run will fail.
      You must change your Unstructured embedding settings or your existing collection's embedding settings to match, and try the run again.
    * If a collection name is not specified, Unstructured creates a new collection in your keyspace. The new collection's name will be `unstructuredautocreated`.

  To create a collection yourself:

  a. After you sign in to DataStax, in the list of databases, click the name of the target database.<br />
  b. On the **Data Explorer** tab, in the **Keyspace** list, select the name of the target keyspace.<br />
  c. In the **Collections** list, select **Create collection**.<br />
  d. Enter some **Collection name**.<br />
  e. Turn on **Vector-enabled collection**, if it is not already turned on.<br />
  f. Choose a mode for **Embedding generation method**. See [Astra DB generated embeddings](#astra-db-generated-embeddings).<br />
  g. If you chose **Bring my own**, enter the number of dimensions for the embedding model that you plan to use.<br />
  h. For **Similarity metric**, select **Cosine**.<br />
  i. Click **Create collection**.<br />

  [Learn more](https://docs.datastax.com/en/astra-db-serverless/databases/manage-collections.html#create-collection).

To create an Astra DB destination connector, see the following examples.

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
                  type="astradb",
                  config={
                      "token": "<token>",
                      "api_endpoint": "<api-endpoint>",
                      "collection_name": "<collection-name>",
                      "keyspace": "<keyspace>",
                      "batch_size": <batch-size>,
                      "flatten_metadata": <True|False>,
                      "binary_encode_vectors": <True|False>,
                      "enable_lexical_search": <True|False>,
                      "astra_generated_embeddings": <True|False>
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
      "type": "astradb",
      "config": {
          "token": "<token>",
          "api_endpoint": "<api-endpoint>",
          "collection_name": "<collection-name>",
          "keyspace": "<keyspace>",
          "batch_size": <batch-size>,
          "flatten_metadata": "<true|false>",
          "binary_encode_vectors": "<true|false>",
          "enable_lexical_search": "<true|false>",
          "astra_generated_embeddings": "<true|false>"
      }
  }'
  ```
</CodeGroup>

Replace the preceding placeholders as follows:

* `<name>` (*required*) - A unique name for this connector.
* `<token>` (*required*) - The application token for the database.
* `<api-endpoint>` (*required*) - The database's associated API endpoint.
* `<collection-name>` - The name of the collection in the keyspace. If no value is provided, see the beginning of this article for the behavior at run time.
* `<keyspace>` - The name of the keyspace in the collection. The default is `default_keyspace` if not otherwise specified.
* `<batch-size>` - The maximum number of records to send per batch. The default is `20` if not otherwise specified.
* `flatten_metadata` - Set to `true` to flatten the metadata into each record. Specifically, when flattened, the metadata key values are brought to the top level of the element, and the `metadata` key itself is removed. By default, the metadata is not flattened (`false`).
* `binary_encode_vectors` - Set to `false` to upload vectors as a list of numbers. By default, vectors are binary encoded before sending (`true`). This is more efficient, but it makes it harder to view and work with vectors in the UI.
* `enable_lexical_search` - Set to `true` to enable lexical and hybrid search. See [Lexical search](#lexical-search).
* `astra_generated_embeddings` - Set to `true` to use an Astra vectorize integration for embeddings. See [Astra DB generated embeddings](#astra-db-generated-embeddings).

## Lexical search

When **Enable Lexical Search** is enabled, document text will be inserted into the `$lexical` field for lexical and hybrid search capabilities.

<Note>
  Your collection must be configured for lexical search, and your database must be in one of the supported AWS regions. For more information, see [Find data with lexicographical matching](https://docs.datastax.com/en/astra-db-serverless/databases/lexical-search.html) in the Astra DB documentation. Otherwise, you will encounter the following error when running a job:

  ` The Collection <keyspace>.<collection> does not have Lexical feature enabled. (LEXICAL_NOT_ENABLED_FOR_COLLECTION) [with 0 inserted ids])`
</Note>

## Astra DB generated embeddings

When **Astra DB Generated Embeddings** is enabled:

* Your document text will be inserted into the `$vectorize` field.
* Astra DB will automatically populate the `$vector` field with embeddings.
* Your workflow **must not** include an embedder node.
* You **must** have an embedding provider configured for your collection.

When **Astra DB Generated Embeddings** is disabled (the default):

* Unstructured will insert embeddings directly into the `$vector` field
* Your workflow **must** include an embedder node.

For more information, see [Auto-generate embeddings with vectorize](https://docs.datastax.com/en/astra-db-serverless/databases/embedding-generation.html) in the Astra DB documentation.

### Troubleshooting

You might encounter the following errors when running a job that uses this connector:

**Error**:

`Unable to vectorize data, embedding service not configured for the collection : <collection> (EMBEDDING_SERVICE_NOT_CONFIGURED) [with 0 inserted ids])`

You've enabled **Astra DB Generated Embeddings**, but your collection does not have an embedding provider. Either disable **Astra DB Generated Embeddings** in your connector settings, or recreate your collection with an embedding provider.

**Error**:

`Cannot use Unstructured embeddings and Astra-generated embeddings simultaneously. Please disable Astra generated embeddings or remove the Unstructured embedder.`

**or**:

`No vectors provided. Please enable an Unstructured embedding provider or configure Astra to generate embeddings.`

You must choose either Unstructured or Astra DB embeddings. Configuring neither, or both, is unsupported.
