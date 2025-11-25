# Source: https://docs.unstructured.io/ui/sources/azure-blob-storage.md

# Source: https://docs.unstructured.io/api-reference/workflow/sources/azure-blob-storage.md

# Azure

<Note>
  If you're new to Unstructured, read this note first.

  Before you can create a source connector, you must first sign in to your Unstructured account:

  * If you do not already have an Unstructured account, [sign up for free](https://unstructured.io/?modal=try-for-free).
    After you sign up, you are automatically signed in to your new Unstructured **Let's Go** account, at [https://platform.unstructured.io](https://platform.unstructured.io).
    To sign up for a **Business** account instead, [contact Unstructured Sales](https://unstructured.io/?modal=contact-sales), or [learn more](/api-reference/overview#pricing).
  * If you already have an Unstructured **Let's Go**, **Pay-As-You-Go**, or **Business SaaS** account and are not already signed in, sign in to your account at
    [https://platform.unstructured.io](https://platform.unstructured.io). For other types of **Business** accounts, see your Unstructured account administrator for sign-in instructions,
    or email Unstructured Support at [support@unstructured.io](mailto:support@unstructured.io).

  After you sign in, the [Unstructured user interface](/ui/overview) (UI) appears, which you use to get your Unstructured API key, as follows:

  1. After you sign in to your Unstructured **Let's Go**, **Pay-As-You-Go**, or **Business** account, click **API Keys** on the sidebar.<br />

     For a **Business** account, before you click **API Keys**, make sure you have selected the organizational workspace you want to create an API key
     for. Each API key works with one and only one organizational workspace. [Learn more](/ui/account/workspaces#create-an-api-key-for-a-workspace).

  2. Click **Generate API Key**.<br />

  3. Follow the on-screen instructions to finish generating the key.<br />

  4. Click the **Copy** icon next to your new key to add the key to your system's clipboard. If you lose this key, simply return and click the **Copy** icon again.<br />

  After you create the source connector, add it along with a
  [destination connector](/api-reference/workflow/destinations/overview) to a [workflow](/api-reference/workflow/overview#workflows).
  Then run the worklow as a [job](/api-reference/workflow/overview#jobs). To learn how, try out the
  [hands-on Workflow Endpoint quickstart](/api-reference/workflow/overview#quickstart),
  go directly to the [quickstart notebook](https://colab.research.google.com/github/Unstructured-IO/notebooks/blob/main/notebooks/Unstructured_Platform_Workflow_Endpoint_Quickstart.ipynb),
  or watch the two 4-minute video tutorials for the [Unstructured Python SDK](/api-reference/workflow/overview#unstructured-python-sdk).

  You can also create source connectors with the Unstructured user interface (UI).
  [Learn how](/ui/sources/overview).

  If you need help, email Unstructured Support at [support@unstructured.io](mailto:support@unstructured.io).

  You are now ready to start creating a source connector! Keep reading to learn how.
</Note>

Ingest your files into Unstructured from Azure Blob Storage.

The requirements are as follows.

The following video shows how to fulfill the minimum set of Azure Storage account requirements:

<iframe width="560" height="315" src="https://www.youtube.com/embed/Vl3KCphlh9Y" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

<Note>
  If you are generating an SAS token as shown in the preceding video, be sure to set the following permissions:

  * **Read** and **List** for reading from the container only.
  * **Write** and **List** for writing to the container only.
  * **Read**, **Write**, and **List** for both reading from and writing to the container.
</Note>

Here are some more details about these requirements:

* An Azure account. To create one, [learn how](https://azure.microsoft.com/pricing/purchase-options/azure-account).

  <iframe width="560" height="315" src="https://www.youtube.com/embed/2bQ6WiJ1ncA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

* An Azure Storage account, and a container within that account. [Create a storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create). [Create a container](https://learn.microsoft.com/azure/storage/blobs/blob-containers-portal).

  <iframe width="560" height="315" src="https://www.youtube.com/embed/AhuNgBafmUo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

  <iframe width="560" height="315" src="https://www.youtube.com/embed/xmndjYnGvcs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

* The Azure Storage remote URL, using the format `az://<container-name>/<path/to/file/or/folder/in/container/as/needed>`

  For example, if your container is named `my-container`, and there is a folder in the container named `my-folder`, the
  Azure Storage remote URL would be `az://my-container/my-folder/`.

* An SAS token (recommended), access key, or connection string for the Azure Storage account.  [Create an SAS token (recommended)](https://learn.microsoft.com/azure/ai-services/translator/document-translation/how-to-guides/create-sas-tokens). [Get an access key](https://learn.microsoft.com/azure/storage/common/storage-account-keys-manage#view-account-access-keys). [Get a connection string](https://learn.microsoft.com/azure/storage/common/storage-configure-connection-string#configure-a-connection-string-for-an-azure-storage-account).

  Create an SAS token (recommended):

  <iframe width="560" height="315" src="https://www.youtube.com/embed/X6cmJ2IbVzo?start=240&end=370" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

  Get an access key or connection string:

  <iframe width="560" height="315" src="https://www.youtube.com/embed/muMmcwVfFqs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

To create an Azure Blob Storage source connector, see the following examples.

<CodeGroup>
  ```python Python SDK theme={null}
  import os

  from unstructured_client import UnstructuredClient
  from unstructured_client.models.operations import CreateSourceRequest
  from unstructured_client.models.shared import CreateSourceConnector

  with UnstructuredClient(api_key_auth=os.getenv("UNSTRUCTURED_API_KEY")) as client:
      response = client.sources.create_source(
          request=CreateSourceRequest(
              create_source_connector=CreateSourceConnector(
                  name="<name>",
                  type="azure",
                  config={
                      "remote_url": "az://<container-name>/<path/to/file/or/folder>",
                      "recursive": <True|False>,

                      # For anonymous authentication, omit the following auth keys.
                      
                      # For SAS token authentication:
                      # "account_name": "<account-name>",
                      # "sas_token": "<sas-token>",

                      # For account key authentication:
                      # "account_name": "<account-name>",
                      # "account_key": "<account-key>",

                      # For connection string authentication:
                      # "connection_string": "<connection-string>"
                  }
              )
          )
      )

      print(response.source_connector_information)
  ```

  ```bash curl theme={null}
  curl --request 'POST' --location \
  "$UNSTRUCTURED_API_URL/sources" \
  --header 'accept: application/json' \
  --header "unstructured-api-key: $UNSTRUCTURED_API_KEY" \
  --header 'content-type: application/json' \
  --data \
  '{
      "name": "<name>",
      "type": "azure",
      "config": {
          "remote_url": "az://<container-name>/<path/to/file/or/folder>",
          "recursive": <true|false>,
      
          # For anonymous authentication, do not set any of the 
          # following fields.

          # For SAS token authentication:
          "account_name": "<account-name>",
          "sas_token": "<sas-token>"

          # For account key authentication:
          "account_name": "<account-name>",
          "account_key": "<account-key>"

          # For connection string authentication:
          "connection_string": "<connection-string>"
      }
  }'
  ```
</CodeGroup>

Replace the preceding placeholders as follows:

* `<name>` (*required*) - A unique name for this connector.

* `az://<container-name>/<path/to/file/or/folder>`  (*required*) - The Azure Storage remote URL, with the format `az://<container-name>/<path/to/file/or/folder/in/container/as/needed>`

  For example, if your container is named `my-container`, and there is a folder in the container named `my-folder`, the
  Azure Storage remote URL would be `az://my-container/my-folder/`.

* `<account-name>`  (*required* for SAS token authentication and account key authentication) - The Azure Storage account name.

* `<sas-token>` - For SAS token authentication, the SAS token for the Azure Storage account (*required*).

* `<account-key>` - For account key authentication, the key for the Azure Storage account (*required*).

* `<connection-string>` - For connection string authentication, the connection string for the Azure Storage account (*required*).

* For `recursive` (source connector only), set to `true` to recursively access files from subfolders within the container. The default is `false` if not otherwise specified.
