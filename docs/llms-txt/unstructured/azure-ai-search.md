# Source: https://docs.unstructured.io/ui/destinations/azure-ai-search.md

# Source: https://docs.unstructured.io/open-source/ingestion/destination-connectors/azure-ai-search.md

# Source: https://docs.unstructured.io/api-reference/workflow/destinations/azure-ai-search.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.unstructured.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Azure AI Search

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

Send processed data from Unstructured to Azure AI Search.

The requirements are as follows.

The following video shows how to fulfill the minimum set of Azure AI Search requirements:

<iframe width="560" height="315" src="https://www.youtube.com/embed/6ZjU5OupWE8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

Here are some more details about these requirements:

* The endpoint and API key for Azure AI Search. [Create an endpoint and API key](https://learn.microsoft.com/azure/search/search-create-service-portal).
* The name of the index in Azure AI Search. [Create an index](https://learn.microsoft.com/rest/api/searchservice/create-index).

  <iframe width="560" height="315" src="https://www.youtube.com/embed/WY8h8Gtyo7o" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

  The Azure AI Search index that you use must have an index schema that is compatible with the schema of the documents
  that Unstructured produces for you. Unstructured cannot provide a schema that is guaranteed to work in all
  circumstances. This is because these schemas will vary based on your source files' types; how you
  want Unstructured to partition, chunk, and generate embeddings; any custom post-processing code that you run; and other factors.

  You can adapt the following index schema example for your own needs. Be sure to replace `<number-of-dimensions>`
  (in three locations in the following example) with the number of dimensions of the embedding model you are using:

  ```json  theme={null}
  {
    "name": "elements-index",
    "fields": [
      {
        "name": "id",
        "type": "Edm.String",
        "key": true
      },
      {
        "name": "record_id",
        "type": "Edm.String",
        "filterable": true
      },
      {
        "name": "element_id",
        "type": "Edm.String"
      },
      {
        "name": "text",
        "type": "Edm.String",
        "searchable": true
      },
      {
        "name": "type",
        "type": "Edm.String"
      },
      {
        "name": "metadata",
        "type": "Edm.ComplexType",
        "fields": [
          {
            "name": "orig_elements",
            "type": "Edm.String"
          },
          {
            "name": "category_depth",
            "type": "Edm.Int32"
          },
          {
            "name": "parent_id",
            "type": "Edm.String"
          },
          {
            "name": "attached_to_filename",
            "type": "Edm.String"
          },
          {
            "name": "filetype",
            "type": "Edm.String"
          },
          {
            "name": "last_modified",
            "type": "Edm.DateTimeOffset"
          },
          {
            "name": "is_continuation",
            "type": "Edm.Boolean"
          },
          {
            "name": "file_directory",
            "type": "Edm.String"
          },
          {
            "name": "filename",
            "type": "Edm.String"
          },
          {
            "name": "data_source",
            "type": "Edm.ComplexType",
            "fields": [
              {
                "name": "url",
                "type": "Edm.String"
              },
              {
                "name": "version",
                "type": "Edm.String"
              },
              {
                "name": "date_created",
                "type": "Edm.DateTimeOffset"
              },
              {
                "name": "date_modified",
                "type": "Edm.DateTimeOffset"
              },
              {
                "name": "date_processed",
                "type": "Edm.DateTimeOffset"
              },
              {
                "name": "permissions_data",
                "type": "Edm.String"
              },
              {
                "name": "record_locator",
                "type": "Edm.String"
              }
            ]
          },
          {
            "name": "coordinates",
            "type": "Edm.ComplexType",
            "fields": [
              {
                "name": "system",
                "type": "Edm.String"
              },
              {
                "name": "layout_width",
                "type": "Edm.Double"
              },
              {
                "name": "layout_height",
                "type": "Edm.Double"
              },
              {
                "name": "points",
                "type": "Edm.String"
              }
            ]
          },
          {
            "name": "languages",
            "type": "Collection(Edm.String)"
          },
          {
            "name": "page_number",
            "type": "Edm.String"
          },
          {
            "name": "links",
            "type": "Collection(Edm.String)"
          },
          {
            "name": "page_name",
            "type": "Edm.String"
          },
          {
            "name": "link_urls",
            "type": "Collection(Edm.String)"
          },
          {
            "name": "link_texts",
            "type": "Collection(Edm.String)"
          },
          {
            "name": "sent_from",
            "type": "Collection(Edm.String)"
          },
          {
            "name": "sent_to",
            "type": "Collection(Edm.String)"
          },
          {
            "name": "subject",
            "type": "Edm.String"
          },
          {
            "name": "section",
            "type": "Edm.String"
          },
          {
            "name": "header_footer_type",
            "type": "Edm.String"
          },
          {
            "name": "emphasized_text_contents",
            "type": "Collection(Edm.String)"
          },
          {
            "name": "emphasized_text_tags",
            "type": "Collection(Edm.String)"
          },
          {
            "name": "text_as_html",
            "type": "Edm.String"
          },
          {
            "name": "regex_metadata",
            "type": "Edm.String"
          },
          {
            "name": "detection_class_prob",
            "type": "Edm.Double"
          }
        ]
      },
      {
        "name": "embeddings",
        "type": "Collection(Edm.Single)",
        "dimensions": <number-of-dimensions>,
        "vectorSearchProfile": "embeddings-config-profile"
      }
    ],
    "vectorSearch": {
      "algorithms": [
        {
          "name": "hnsw-<number-of-dimensions>",
          "kind": "hnsw",
          "hnswParameters": {
            "m": 4,
            "efConstruction": 400,
            "efSearch": 500,
            "metric": "cosine"
          }
        }
      ],
      "profiles": [
        {
          "name": "embeddings-config-profile",
          "algorithm": "hnsw-<number-of-dimensions>"
        }
      ]
    },
    "semantic": {
      "configurations": [
        {
          "name": "default-semantic-config",
          "prioritizedFields": {
            "titleField": null,
            "prioritizedContentFields": [
              { "fieldName": "text" }
            ],
            "prioritizedKeywordsFields": []
          }
        }
      ]
    }
  }
  ```

  See also:

  * [Search indexes in Azure AI Search](https://learn.microsoft.com/azure/search/search-what-is-an-index)
  * [Schema of a search index](https://learn.microsoft.com/azure/search/search-what-is-an-index#schema-of-a-search-index)
  * [Example index schema](https://learn.microsoft.com/rest/api/searchservice/create-index#examples)
  * [Unstructured document elements and metadata](/api-reference/legacy-api/partition/document-elements)

To create an Azure AI Search destination connector, see the following examples.

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
                  type="azure_ai_search",
                  config={
                      "endpoint": "<endpoint>",
                      "index": "<index>",
                      "key": "<azure-ai-search-key>"
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
      "type": "azure_ai_search",
      "config": {
          "endpoint": "<endpoint>",
          "index": "<index>",
          "azure_ai_search_key": "<azure-ai-search-key>"
      }
  }'
  ```
</CodeGroup>

Replace the preceding placeholders as follows:

* `<name>` (required) - A unique name for this connector.
* `<endpoint>` (required) - The endpoint URL for Azure AI Search.
* `<index>` (required) - The name of the index for Azure AI Search.
* `<azure-ai-search-key>` (required) - The API key for Azure AI Search.
