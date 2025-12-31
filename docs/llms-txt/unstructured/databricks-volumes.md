# Source: https://docs.unstructured.io/ui/sources/databricks-volumes.md

# Source: https://docs.unstructured.io/ui/destinations/databricks-volumes.md

# Source: https://docs.unstructured.io/open-source/ingestion/source-connectors/databricks-volumes.md

# Source: https://docs.unstructured.io/open-source/ingestion/destination-connectors/databricks-volumes.md

# Source: https://docs.unstructured.io/api-reference/workflow/sources/databricks-volumes.md

# Source: https://docs.unstructured.io/api-reference/workflow/destinations/databricks-volumes.md

# Source: https://docs.unstructured.io/ui/sources/databricks-volumes.md

# Source: https://docs.unstructured.io/ui/destinations/databricks-volumes.md

# Source: https://docs.unstructured.io/open-source/ingestion/source-connectors/databricks-volumes.md

# Source: https://docs.unstructured.io/open-source/ingestion/destination-connectors/databricks-volumes.md

# Source: https://docs.unstructured.io/api-reference/workflow/sources/databricks-volumes.md

# Source: https://docs.unstructured.io/api-reference/workflow/destinations/databricks-volumes.md

# Source: https://docs.unstructured.io/ui/sources/databricks-volumes.md

# Source: https://docs.unstructured.io/ui/destinations/databricks-volumes.md

# Source: https://docs.unstructured.io/open-source/ingestion/source-connectors/databricks-volumes.md

# Source: https://docs.unstructured.io/open-source/ingestion/destination-connectors/databricks-volumes.md

# Source: https://docs.unstructured.io/api-reference/workflow/sources/databricks-volumes.md

# Source: https://docs.unstructured.io/api-reference/workflow/destinations/databricks-volumes.md

# Source: https://docs.unstructured.io/api-reference/workflow/sources/databricks-volumes.md

# Source: https://docs.unstructured.io/api-reference/workflow/destinations/databricks-volumes.md

# Databricks Volumes

<Tip>
  This article covers connecting Unstructured to Databricks Volumes.

  For information about connecting Unstructured to Delta Tables in Databricks instead, see
  [Delta Tables in Databricks](/api-reference/workflow/destinations/databricks-delta-table).
</Tip>

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

Send processed data from Unstructured to Databricks Volumes.

The requirements are as follows.

* A Databricks account on [AWS](https://docs.databricks.com/getting-started/free-trial.html),
  [Azure](https://learn.microsoft.com/azure/databricks/getting-started/), or
  [GCP](https://docs.gcp.databricks.com/getting-started/index.html).

* A workspace within the Databricks account for [AWS](https://docs.databricks.com/admin/workspace/index.html),
  [Azure](https://learn.microsoft.com/azure/databricks/admin/workspace/), or
  [GCP](https://docs.gcp.databricks.com/admin/workspace/index.html).

* The workspace's URL. Get the workspace URL for
  [AWS](https://docs.databricks.com/workspace/workspace-details.html#workspace-instance-names-urls-and-ids),
  [Azure](https://learn.microsoft.com/azure/databricks/workspace/workspace-details#workspace-instance-names-urls-and-ids),
  or [GCP](https://docs.gcp.databricks.com/workspace/workspace-details.html#workspace-instance-names-urls-and-ids).

  Examples:

  * AWS: `https://<workspace-id>.cloud.databricks.com`
  * Azure: `https://adb-<workspace-id>.<random-number>.azuredatabricks.net`
  * GCP: `https://<workspace-id>.<random-number>.gcp.databricks.com`

  <Note>
    Do not add a trailing slash (`/`) to the workspace URL.
  </Note>

* The Databricks authentication details. For more information, see the documentation for
  [AWS](https://docs.databricks.com/dev-tools/auth/index.html),
  [Azure](https://learn.microsoft.com/azure/databricks/dev-tools/auth/),
  or [GCP](https://docs.gcp.databricks.com/dev-tools/auth/index.html).

  For the [Unstructured UI](/ui/overview) or the [Unstructured API](/api-reference/overview), the following Databricks authentication types are supported:

  * Databricks OAuth machine-to-machine (M2M) authentication for\
    [AWS](https://docs.databricks.com/dev-tools/auth/oauth-m2m.html),
    [Azure](https://learn.microsoft.com/azure/databricks/dev-tools/auth/oauth-m2m), or
    [GCP](https://docs.gcp.databricks.com/dev-tools/auth/oauth-m2m.html).

    You will need the the **Client ID** (or **UUID** or **Application** ID) and OAuth **Secret** (client secret) values for the corresponding service principal.
    Note that for Azure, only Databricks managed service principals are supported. Microsoft Entra ID managed service principals are not supported.

    The following video shows how to create a Databricks managed service principal:

    <iframe width="560" height="315" src="https://www.youtube.com/embed/wBmqv5DaA1E" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

  * Databricks personal access token authentication for
    [AWS](https://docs.databricks.com/dev-tools/auth/pat.html),
    [Azure](https://learn.microsoft.com/azure/databricks/dev-tools/auth/pat), or
    [GCP](https://docs.gcp.databricks.com/dev-tools/auth/pat.html).

    You will need the personal access token's value.

    The following video shows how to create a Databricks personal access token:

    <iframe width="560" height="315" src="https://www.youtube.com/embed/OzEU2miAS6I" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

  For [Unstructured Ingest](/open-source/ingestion/overview), the following Databricks authentication types are supported:

  * For Databricks personal access token authentication for
    [AWS](https://docs.databricks.com/dev-tools/auth/pat.html),
    [Azure](https://learn.microsoft.com/azure/databricks/dev-tools/auth/pat), or
    [GCP](https://docs.gcp.databricks.com/dev-tools/auth/pat.html): The personal access token's value.

    The following video shows how to create a Databricks personal access token:

    <iframe width="560" height="315" src="https://www.youtube.com/embed/OzEU2miAS6I" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

  * For username and password (basic) authentication ([AWS](https://docs.databricks.com/archive/dev-tools/basic.html) only): The user's name and password values.

  * For OAuth machine-to-machine (M2M) authentication ([AWS](https://docs.databricks.com/dev-tools/auth/oauth-m2m.html),
    [Azure](https://learn.microsoft.com/azure/databricks/dev-tools/auth/oauth-m2m), and
    [GCP](https://docs.gcp.databricks.com/dev-tools/auth/oauth-m2m.html)): The client ID and OAuth secret values for the corresponding service principal.

  * For OAuth user-to-machine (U2M) authentication ([AWS](https://docs.databricks.com/dev-tools/auth/oauth-u2m.html),
    [Azure](https://learn.microsoft.com/azure/databricks/dev-tools/auth/oauth-u2m), and
    [GCP](https://docs.gcp.databricks.com/dev-tools/auth/oauth-u2m.html)): No additional values.

  * For Azure managed identities (formerly Managed Service Identities (MSI) authentication) ([Azure](https://learn.microsoft.com/azure/databricks/dev-tools/auth/azure-mi) only): The client ID value for the corresponding managed identity.

  * For Microsoft Entra ID service principal authentication ([Azure](https://learn.microsoft.com/azure/databricks/dev-tools/auth/azure-sp) only): The tenant ID, client ID, and client secret values for the corresponding service principal.

  * For Azure CLI authentication ([Azure](https://learn.microsoft.com/azure/databricks/dev-tools/auth/azure-cli) only): No additional values.

  * For Microsoft Entra ID user authentication ([Azure](https://learn.microsoft.com/azure/databricks/dev-tools/user-aad-token) only): The Entra ID token for the corresponding Entra ID user.

  * For Google Cloud Platform credentials authentication ([GCP](https://docs.gcp.databricks.com/dev-tools/auth/gcp-creds.html) only): The local path to the corresponding Google Cloud service account's credentials file.

  * For Google Cloud Platform ID authentication ([GCP](https://docs.gcp.databricks.com/dev-tools/auth/gcp-id.html) only): The Google Cloud service account's email address.

* The name of the parent catalog in Unity Catalog for
  [AWS](https://docs.databricks.com/catalogs/create-catalog.html),
  [Azure](https://learn.microsoft.com/azure/databricks/catalogs/create-catalog), or
  [GCP](https://docs.gcp.databricks.com/catalogs/create-catalog.html) for the volume.

* The name of the parent schema (formerly known as a database) in Unity Catalog for
  [AWS](https://docs.databricks.com/schemas/create-schema.html),
  [Azure](https://learn.microsoft.com/azure/databricks/schemas/create-schema), or
  [GCP](https://docs.gcp.databricks.com/schemas/create-schema.html) for the volume.

* The name of the volume in Unity Catalog for [AWS](https://docs.databricks.com/tables/managed.html),
  [Azure](https://learn.microsoft.com/azure/databricks/tables/managed), or
  [GCP](https://docs.gcp.databricks.com/tables/managed.html), and optionally any path in that volume that you want to access directly, beginning with the volume's root.

* The Databricks workspace user or service principal must have the following *minimum* set of privileges to read from or write to the
  existing volume in Unity Catalog:

  * `USE CATALOG` on the volume's parent catalog in Unity Catalog.
  * `USE SCHEMA` on the volume's parent schema (formerly known as a database) in Unity Catalog.
  * `READ VOLUME` and `WRITE VOLUME` on the volume.

  The following videos shows how to create and set privileges for a catalog, schema (formerly known as a database), and volume in Unity Catalog.

  <iframe width="560" height="315" src="https://www.youtube.com/embed/yF9DJphhQQc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

  Learn more about how to check and set Unity Catalog privileges for
  [AWS](https://docs.databricks.com/data-governance/unity-catalog/manage-privileges/index.html#show-grant-and-revoke-privileges),
  [Azure](https://learn.microsoft.com/azure/databricks/data-governance/unity-catalog/manage-privileges/#grant), or
  [GCP](https://docs.gcp.databricks.com/data-governance/unity-catalog/manage-privileges/index.html#show-grant-and-revoke-privileges).

To create a Databricks Volumes destination connector, see the following examples.

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
                  type="databricks_volumes",
                  config={
                      "host": "<host>",
                      "catalog": "<catalog>",
                      "schema": "<schema>",
                      "volume": "<volume>",
                      "volume_path": "<volume_path>",

                      # For Databricks OAuth machine-to-machine (M2M) authentication:
                      "client_secret": "<client-secret>",
                      "client_id": "<client-id>"

                      # For Databricks personal access token authentication:
                      "token": "<token>"
                  }
              )
          )
      )

      print(response.destination_connector_information)
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
      "type": "databricks_volumes",
      "config": {
          "host": "<host>",
          "catalog": "<catalog>",
          "schema": "<schema>",
          "volume": "<volume>",
          "volume_path": "<volume_path>",

          # For Databricks OAuth machine-to-machine (M2M) authentication:
          "client_secret": "<client-secret>",
          "client_id": "<client-id>"

          # For Databricks personal access token authentication:
          "token": "<token>"
      }
  }'
  ```
</CodeGroup>

Replace the preceding placeholders as follows:

* `<name>` (*required*) - A unique name for this connector.

* `<host>` (*required*) - The Databricks workspace host URL.

  <Note>
    Do not add a trailing slash (`/`) to the workspace host URL.
  </Note>

* `<client-id>` (*required*) - For Databricks OAuth machine-to-machine (M2M) authentication,
  the **Client ID** (or **UUID** or **Application ID**) value for the Databricks managed service principal that has the appropriate privileges to the volume.

* `<client-secret>` (*required*) - For Databricks OAuth M2M authentication,
  the associated OAuth **Secret** value for the Databricks managed service principal that has the appropriate privileges to the volume.

* `<token>` (*required*) - For Databricks personal access token authentication, the personal access token's value.

* `<catalog>` (*required*) - The name of the catalog to use.

* `<schema>` - The name of the associated schema. If not specified, `default` is used.

* `<volume>` (*required*) - The name of the associated volume.

* `<volume_path>` - Any optional path to access within the volume.
