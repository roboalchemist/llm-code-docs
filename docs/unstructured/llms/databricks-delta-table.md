# Source: https://docs.unstructured.io/ui/destinations/databricks-delta-table.md

# Source: https://docs.unstructured.io/open-source/ingestion/destination-connectors/databricks-delta-table.md

# Source: https://docs.unstructured.io/api-reference/workflow/destinations/databricks-delta-table.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.unstructured.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Delta Tables in Databricks

<Tip>
  This article covers connecting Unstructured to Delta Tables in Databricks.

  For information about connecting Unstructured to Delta Tables in Amazon S3 instead, see
  [Delta Tables in Amazon S3](/api-reference/workflow/destinations/delta-table).

  For information about connecting Unstructured to Databricks Volumes instead, see
  [Databricks Volumes](/api-reference/workflow/destinations/databricks-volumes).
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
  the notebook [Dropbox-To-Pinecone Connector API Quickstart for Unstructured](https://colab.research.google.com/github/Unstructured-IO/notebooks/blob/main/notebooks/Dropbox_To_Pinecone_Connector_Quickstart.ipynb),
  or watch the two 4-minute video tutorials for the [Unstructured Python SDK](/api-reference/workflow/overview#unstructured-python-sdk).

  You can also create destination connectors with the Unstructured user interface (UI).
  [Learn how](/ui/destinations/overview).

  If you need help, email Unstructured Support at [support@unstructured.io](mailto:support@unstructured.io).

  You are now ready to start creating a destination connector! Keep reading to learn how.
</Note>

Send processed data from Unstructured to a Delta Table in Databricks.

The requirements are as follows.

* A Databricks account on [AWS](https://docs.databricks.com/getting-started/free-trial.html),
  [Azure](https://learn.microsoft.com/azure/databricks/getting-started/), or
  [GCP](https://docs.gcp.databricks.com/getting-started/index.html).

* A workspace within the Datbricks account for [AWS](https://docs.databricks.com/admin/workspace/index.html),
  [Azure](https://learn.microsoft.com/azure/databricks/admin/workspace/), or
  [GCP](https://docs.gcp.databricks.com/admin/workspace/index.html).

* One of the following compute resources within the workspace:

  * A SQL warehouse for [AWS](https://docs.databricks.com/compute/sql-warehouse/create.html),
    [Azure](https://learn.microsoft.com/azure/databricks/compute/sql-warehouse/create), or
    [GCP](https://docs.gcp.databricks.com/compute/sql-warehouse/create.html).

    The following video shows how to create a SQL warehouse if you do not already have one available, get its **Server Hostname** and **HTTP Path** values, and set permissions for someone other than the warehouse's owner to use it:

    <iframe width="560" height="315" src="https://www.youtube.com/embed/N-Aw9-U3_fE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

  * An all-purpose cluster for [AWS](https://docs.databricks.com/compute/use-compute.html),
    [Azure](https://learn.microsoft.com/azure/databricks/compute/use-compute), or
    [GCP](https://docs.gcp.databricks.com/compute/use-compute.html).

    The following video shows how to create an all-purpose cluster if you do not already have one available, get its **Server Hostname** and **HTTP Path** values, and set permissions for someone other than the cluster's owner to use it:

    <iframe width="560" height="315" src="https://www.youtube.com/embed/apgibaelVY0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

* The SQL warehouse's or cluster's **Server Hostname** and **HTTP Path** values for [AWS](https://docs.databricks.com/integrations/compute-details.html),
  [Azure](https://learn.microsoft.com/azure/databricks/integrations/compute-details), or
  [GCP](https://docs.gcp.databricks.com/integrations/compute-details.html).

* Unity Catalog enabled in the workspace for [AWS](https://docs.databricks.com/data-governance/unity-catalog/get-started.html),
  [Azure](https://learn.microsoft.com/azure/databricks/data-governance/unity-catalog/get-started), or
  [GCP](https://docs.gcp.databricks.com/data-governance/unity-catalog/get-started.html).

* Within Unity Catalog:

  * A catalog
    for [AWS](https://docs.databricks.com/catalogs/create-catalog.html),
    [Azure](https://learn.microsoft.com/azure/databricks/catalogs/create-catalog), or
    [GCP](https://docs.gcp.databricks.com/catalogs/create-catalog.html).
  * A schema (formerly known as a database)
    for [AWS](https://docs.databricks.com/schemas/create-schema.html),
    [Azure](https://learn.microsoft.com/azure/databricks/schemas/create-schema), or
    [GCP](https://docs.gcp.databricks.com/schemas/create-schema.html)
    within that catalog,
  * A table
    for [AWS](https://docs.databricks.com/tables/managed.html),
    [Azure](https://learn.microsoft.com/azure/databricks/tables/managed), or
    [GCP](https://docs.gcp.databricks.com/tables/managed.html)
    within that schema (formerly known as a database).

    You can have the connector attempt to create a table for you automatically at run time. To do this, in the connector settings as described later in this article,
    do one of the following:

    * Specify the name of the table that you want the connector to attempt to create within the specified catalog and schema (formerly known as a database).
    * Leave the table name blank. The connector will attempt to create a table within the specified catalog and schema (formerly known as a database).
      For the [Unstructured UI](/ui/overview) and [Unstructured API](/api-reference/overview), the table is named `u<short-workflow-id>`.
      For the [Unstructured Ingest CLI and Ingest Python library](/open-source/ingestion/overview), the table is named `unstructuredautocreated`.

    The connector will attempt to create the table on behalf of the related Databricks workspace user or Databricks managed service principal that is referenced in the connector settings, as described later in these requirements.
    If successful, the table's owner is set as the related Databricks workspace user or Databricks managed service principal. The owner will have all Unity Catalog
    privileges on the table by default. No other Databricks workspace users or Databricks managed service principals will have any privileges on the table by default.

    <Warning>
      If the table's parent schema (formerly known as a database) is not owned by the same Databricks workspace user or Databricks managed service principal that is
      referenced in the connector settings, then you should grant the new table's owner the `CREATE TABLE` privilege on that parent schema (formerly known as a database)
      before the connector attempts to create the table. Otherwise, table creation could fail.
    </Warning>

    <Note>
      Using dashes (`-`) in the names of catalogs, schemas (formerly known as databases), and tables might cause isolated issues with the connector. It is
      recommended to use underscores (`_`) instead of dashes in the names of catalogs, schemas, and tables.
    </Note>

  The following video shows how to create a catalog, schema (formerly known as a database), and a table in Unity Catalog if you do not already have them available, and set privileges for someone other than their owner to use them:

  <iframe width="560" height="315" src="https://www.youtube.com/embed/ffNnq-6bpd4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

  If you want to use an existing table or create one yourself beforehand, this table must contain at minimum the following column names and their data types:

  ```text  theme={null}
  CREATE TABLE IF NOT EXISTS <catalog_name>.<schema_name>.<table_name> (
      id STRING NOT NULL PRIMARY KEY,
      record_id STRING NOT NULL,
      element_id STRING NOT NULL,
      text STRING,
      embeddings ARRAY<FLOAT>,
      type STRING,
      metadata VARIANT
  );
  ```

  <Info>
    In Databricks, a table's *schema* is different than a *schema* (formerly known as a database) in a catalog-schema object relationship in Unity Catalog.
  </Info>

* Within Unity Catalog, a volume
  for [AWS](https://docs.databricks.com/volumes/utility-commands.html),
  [Azure](https://learn.microsoft.com/azure/databricks/volumes/utility-commands),
  or [GCP](https://docs.gcp.databricks.com/volumes/utility-commands.html). The volume can be in the same
  schema (formerly known as a database) as the table, or the volume and table can be in separate schemas. In either case, both of these
  schemas must share the same parent catalog.

  <Note>
    Using dashes (`-`) in the names of volumes might cause isolated issues with the connector. It is
    recommended to use underscores (`_`) instead of dashes in the names of volumes.
  </Note>

  The following video shows how to create a catalog, schema (formerly known as a database), and a volume in Unity Catalog if you do not already have them available, and set privileges for someone other than their owner to use them:

  <iframe width="560" height="315" src="https://www.youtube.com/embed/yF9DJphhQQc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

* For Databricks managed service principal authentication (using Databricks OAuth M2M) to the workspace:

  * A Databricks managed service principal.
    This service principal must have the appropriate access permissions to the catalog, schema (formerly known as a database), table, volume, and cluster or SQL warehouse.
  * The service principal's **UUID** (or **Client ID** or **Application ID**) value.
  * The OAuth **Secret** value for the service principal.

  To get this information, see Steps 1-3 of the instructions for [AWS](https://docs.databricks.com/dev-tools/auth/oauth-m2m.html),
  [Azure](https://learn.microsoft.com/azure/databricks/dev-tools/auth/oauth-m2m), or
  [GCP](https://docs.gcp.databricks.com/dev-tools/auth/oauth-m2m.html).

  <Note>
    For Azure Databricks, this connector only supports Databricks managed service principals for authentication.
    Microsoft Entra ID managed service principals are not supported.
  </Note>

  The following video shows how to create a Databricks managed service principal if you do not already have one available:

  <iframe width="560" height="315" src="https://www.youtube.com/embed/wBmqv5DaA1E" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

* For Databricks personal access token authentication to the workspace, the
  Databricks personal access token value for
  [AWS](https://docs.databricks.com/dev-tools/auth/pat.html#databricks-personal-access-tokens-for-workspace-users),
  [Azure](https://learn.microsoft.com/azure/databricks/dev-tools/auth/pat#azure-databricks-personal-access-tokens-for-workspace-users), or
  [GCP](https://docs.gcp.databricks.com/dev-tools/auth/pat.html#databricks-personal-access-tokens-for-workspace-users).
  This token must be for the workspace user who
  has the appropriate access permissions to the catalog, schema (formerly known as a database), table, volume, and cluster or SQL warehouse,

  The following video shows how to create a Databricks personal access token if you do not already have one available:

  <iframe width="560" height="315" src="https://www.youtube.com/embed/OzEU2miAS6I" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

* The Databricks workspace user or Databricks managed service principal must have the following *minimum* set of permissions and privileges to write to an
  existing volume or table in Unity Catalog. If the owner of these is that Databricks workspace user or Databricks managed service principal, then
  they will have all necessary permissions and privileges by default. If the owner is someone else, then the following permissions and privileges must be
  explicitly granted to them before using the connector:

  * To use an all-purpose cluster for access, `Can Restart` permission on that cluster. Learn how to check and set cluster permissions for
    [AWS](https://docs.databricks.com/compute/clusters-manage.html#compute-permissions),
    [Azure](https://learn.microsoft.com/azure/databricks/compute/clusters-manage#cluster-level-permissions), or
    [GCP](https://docs.gcp.databricks.com/compute/clusters-manage.html#compute-permissions).

  * To use a SQL warehouse for access, `Can use` permission on that SQL warehouse. Learn how to check and set SQL warehouse permissions for
    [AWS](https://docs.databricks.com/compute/sql-warehouse/create.html#manage-a-sql-warehouse),
    [Azure](https://learn.microsoft.com/azure/databricks/compute/sql-warehouse/create#manage), or
    [GCP](https://docs.gcp.databricks.com/compute/sql-warehouse/create.html#manage-a-sql-warehouse).

  * To access a Unity Catalog volume, the following privileges:

    * `USE CATALOG` on the volume's parent catalog in Unity Catalog.
    * `USE SCHEMA` on the volume's parent schema (formerly known as a database) in Unity Catalog.
    * `READ VOLUME` and `WRITE VOLUME` on the volume.

    Learn how to check and set Unity Catalog privileges for
    [AWS](https://docs.databricks.com/data-governance/unity-catalog/manage-privileges/index.html#show-grant-and-revoke-privileges),
    [Azure](https://learn.microsoft.com/azure/databricks/data-governance/unity-catalog/manage-privileges/#grant), or
    [GCP](https://docs.gcp.databricks.com/data-governance/unity-catalog/manage-privileges/index.html#show-grant-and-revoke-privileges).

  * To access a Unity Catalog table, the following privileges:

    * `USE CATALOG` on the table's parent catalog in Unity Catalog.
    * `USE SCHEMA` on the table's parent schema (formerly known as a database) in Unity Catalog.
    * To create a new table, `CREATE TABLE` on the table's parent schema (formerly known as a database) in Unity Catalog.
    * If the table already exists, `MODIFY` and `SELECT` on the table.

    Learn how to check and set Unity Catalog privileges for
    [AWS](https://docs.databricks.com/data-governance/unity-catalog/manage-privileges/index.html#show-grant-and-revoke-privileges),
    [Azure](https://learn.microsoft.com/azure/databricks/data-governance/unity-catalog/manage-privileges/#grant), or
    [GCP](https://docs.gcp.databricks.com/data-governance/unity-catalog/manage-privileges/index.html#show-grant-and-revoke-privileges).

To create a Delta Tables in Databricks destination connector, see the following examples.

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
                  type="databricks_volume_delta_tables",
                  config={
                      "server_hostname": "<server-hostname>",
                      "http_path": "<http-path>",
                      "token": "<token>",
                      "client_id": "<client-id>",
                      "client_secret": "<client-secret>",
                      "volume": "<volume>",
                      "catalog": "<catalog>",
                      "volume_path": "<volume_path>",
                      "schema": "<schema>",
                      "database": "<database>",
                      "table_name": "<table_name>"
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
      "type": "databricks_volume_delta_tables",
      "config": {
          "server_hostname": "<server-hostname>",
          "http_path": "<http-path>",
          "token": "<token>",
          "client_id": "<client-id>",
          "client_secret": "<client-secret>",
          "volume": "<volume>",
          "catalog": "<catalog>",
          "volume_path": "<volume_path>",
          "schema": "<schema>",
          "database": "<database>",
          "table_name": "<table_name>"
      }
  }'
  ```
</CodeGroup>

Replace the preceding placeholders as follows:

* `<name>` (*required*) - A unique name for this connector.

* `<server-hostname>` (*required*): The target Databricks cluster's or SQL warehouse's **Server Hostname** value.

* `<http-path>` (*required*): The cluster's or SQL warehouse's **HTTP Path** value.

* `<token>` (*required* for PAT authentication): For Databricks personal access token (PAT) authentication, the target Databricks user's PAT value.

* `<client-id>` and `<client-secret>` (*required* for OAuth authentication): For Databricks OAuth machine-to-machine (M2M) authentication, the Databricks managed service principal's **UUID** (or **Client ID** or **Application ID**) and OAuth **Secret** (client secret) values.

* `<catalog>` (*required*): The name of the catalog in Unity Catalog for the target volume and table in the Databricks workspace.

* `<database>`: The name of the schema (formerly known as a database) in Unity Catalog for the target table. The default is `default` if not otherwise specified.

  If the target table and volume are in the same schema (formerly known as a database), then `<database>` and `<schema>` will have the same values.

* `<table_name>`: The name of the target table in Unity Catalog.

  * If a table name is specified, but a table with that name does not exist within the specified schema (formerly known as a database), the connector attempts to create a table with that name within that schema.
  * If no table name is specified, the connector attempts to create a table named `u<short-workflow-id>` within the specified schema (formerly known as a database).

  See the beginning of this article for additional technical requirements before having the connector attempt to create a table.

* `<schema>`: The name of the schema  (formerly known as a database) in Unity Catalog for the target volume. The default is `default` if not otherwise specified.

  If the target volume and table are in the same schema (formerly known as a database), then `<schema>` and `<database>` will have the same values.

* `<volume>` (*required*): The name of the target volume in Unity Catalog.

* `<volume_path>`: Any target folder path inside of the volume to use instead of the volume's root. If not otherwise specified, processing occurs at the volume's root.

<Note>
  Using dashes (`-`) in the names of catalogs, schemas (formerly known as databases), tables, and volumes might cause isolated issues with the connector. It is
  recommended to use underscores (`_`) instead of dashes in the names of catalogs, schemas, tables, and volumes.
</Note>

## Learn more

* <Icon icon="blog" />  [Integration Highlight: Databricks Delta Tables](https://unstructured.io/blog/integration-highlight-databricks-delta-tables)
