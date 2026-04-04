# Source: https://docs.unstructured.io/ui/sources/postgresql.md

# Source: https://docs.unstructured.io/ui/destinations/postgresql.md

# Source: https://docs.unstructured.io/open-source/ingestion/source-connectors/postgresql.md

# Source: https://docs.unstructured.io/open-source/ingestion/destination-connectors/postgresql.md

# Source: https://docs.unstructured.io/api-reference/workflow/sources/postgresql.md

# Source: https://docs.unstructured.io/api-reference/workflow/destinations/postgresql.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.unstructured.io/llms.txt
> Use this file to discover all available pages before exploring further.

# PostgreSQL

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

Send processed data from Unstructured to PostgreSQL.

The requirements are as follows.

* For the [Unstructured UI](/ui/overview) or the [Unstructured API](/api-reference/overview), local PostgreSQL installations are not supported.
* For [Unstructured Ingest](/open-source/ingestion/overview), local and non-local PostgreSQL installations are supported.

The following video shows how to set up [Amazon RDS for PostgreSQL](https://aws.amazon.com/rds/postgresql/):

<iframe width="560" height="315" src="https://www.youtube.com/embed/QuIlEimejDs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

The following video shows how to set up [Azure Database for PostgreSQL](https://azure.microsoft.com/products/postgresql):

<iframe width="560" height="315" src="https://www.youtube.com/embed/6lvtBUFI7eQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

* A PostgreSQL instance.

  * [Create an Amazon RDS for PostgreSQL instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.CreatingConnecting.PostgreSQL.html).
  * [Create an Azure Database for PostgreSQL server](https://learn.microsoft.com/en-us/azure/postgresql/flexible-server/how-to-deploy-on-azure-free-account).
  * [Install PostgreSQL locally](https://www.postgresql.org/docs/current/tutorial-install.html).

* The host name and port number for the instance.

  * For Amazon RDS for PostgreSQL, learn how to [get the host name and port number](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ConnectToPostgreSQLInstance.html#postgresql-endpoint).
  * For Azure Database for PostgreSQL, learn how to [get the host](https://learn.microsoft.com/azure/postgresql/flexible-server/quickstart-create-server#get-the-connection-information). The port number is `5432`.
  * For local PostgreSQL installations, these values are in the `postgresql.conf` file's `listen_addresses` and `port` settings. This file should be on the same machine as the instance. These values might also already be set as environment variables named `PGHOST` and `PGPORT` on the same machine as the instance.
  * For other installation types, see your PostgreSQL provider's documentation.

* Depending on your network security requirements, you might need to allow access to your instance only from specific IP addresses.

  To get Unstructured's IP address ranges, go to
  [https://assets.p6m.u10d.net/publicitems/ip-prefixes.json](https://assets.p6m.u10d.net/publicitems/ip-prefixes.json)
  and allow all of the `ip_prefix` fields' values that are listed.

  <Note>These IP address ranges are subject to change. You can always find the latest ones in the preceding file.</Note>

  To learn how to allow these IP address ranges, see your PostgreSQL provider's documentation, for example with
  [Amazon RDS for PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.RDSSecurityGroups.html) or
  [Azure Database for PostgreSQL](https://learn.microsoft.com/azure/postgresql/flexible-server/how-to-manage-firewall-portal#create-a-firewall-rule-after-server-is-created).

  <Note>
    For Amazon RDS for PostgreSQL, Amazon recommends that you set the instance's **Public access** setting to **No** by default, as this
    approach is more secure. This means that no
    resources can connect to the instance outside of the instance's associated Virtual Private Cloud (VPC) without extra configuration.
    [Learn more](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html#USER_VPC.Hiding).
    [Access an Amazon RDS instance in a VPC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.Scenarios.html).

    If you must enable public access, set the instance's **Public access** setting to **Yes**, and then adjust the instance's related
    security group to allow this access.
    [Learn how](https://repost.aws/en/questions/QUxemKa9u5TV6CmLiO-r5prg/lost-public-access-to-aws-rds-postgresql-instance).

    [Troubleshoot issues with connecting to Amazon RDS instances](https://repost.aws/knowledge-center/rds-connectivity-instance-subnet-vpc).
  </Note>

* A database in the instance.

  * For Amazon RDS for PostgreSQL and Azure Database for PostgreSQL, the default database name is `postgres` unless a custom database name was specified during the instance creation process.
  * For local PostgreSQL installations, learn how to [create a database](https://www.postgresql.org/docs/current/tutorial-createdb.html).
  * For other installation types, see your PostgreSQL provider's documentation.

* A table in the database. Learn how to [create a table](https://www.postgresql.org/docs/current/tutorial-table.html).

  For the destination connector, the table must have a defined schema before Unstructured can write to the table. The minimum viable
  schema for Unstructured contains only the fields `id`, `element_id`, `record_id`, `text`, (and `embeddings`, if you are using `pgvector` and generating vector embeddings), as follows.
  `type` is an optional field, but highly recommended.

  If you are using `pgvector` and generating vector embeddings, the number of dimensions (in this example, `1536`) must match the number of dimensions for the associated embedding model that you use in any related Unstructured workflows or ingestion pipelines.

  <CodeGroup>
    ```sql PostgreSQL theme={null}
    CREATE TABLE elements (
        id UUID PRIMARY KEY,
        element_id TEXT,
        record_id TEXT,
        text TEXT,
        type TEXT
    );
    ```

    ```sql PostgreSQL with pgvector theme={null}
    CREATE EXTENSION vector;

    CREATE TABLE elements (
        id UUID PRIMARY KEY,
        element_id TEXT,
        record_id TEXT,
        text TEXT,
        type TEXT,
        embeddings vector(1536)
    );
    ```
  </CodeGroup>

  For objects in the `metadata` field that Unstructured produces and that you want to store in PostgreSQL, you must create fields in your table's schema that
  follows Unstructured's `metadata` field naming convention. For example, if Unstructured produces a `metadata` field with the following
  child objects:

  ```json  theme={null}
  "metadata": {
    "is_extracted": "true",
    "coordinates": {
      "points": [
        [
          134.20055555555555,
          241.36027777777795
        ],
        [
          134.20055555555555,
          420.0269444444447
        ],
        [
          529.7005555555555,
          420.0269444444447
        ],
        [
          529.7005555555555,
          241.36027777777795
        ]
      ],
      "system": "PixelSpace",
      "layout_width": 1654,
      "layout_height": 2339
    },
    "filetype": "application/pdf",
    "languages": [
      "eng"
    ],
    "page_number": 1,
    "image_mime_type": "image/jpeg",
    "filename": "realestate.pdf",
    "data_source": {
      "url": "file:///home/etl/node/downloads/00000000-0000-0000-0000-000000000001/7458635f-realestate.pdf",
      "record_locator": {
        "protocol": "file",
        "remote_file_path": "file:///home/etl/node/downloads/00000000-0000-0000-0000-000000000001/7458635f-realestate.pdf"
      }
    }
  }
  ```

  You could create corresponding fields in your table's schema by using the following field names and data types:

  <CodeGroup>
    ```sql PostgreSQL theme={null}
    -- The fields "id", "element_id", "record_id", and "text" are required.
    -- "type" is an optional field, but highly recommended.
    -- All other "metadata" fields are optional.
    CREATE TABLE elements (
        id UUID PRIMARY KEY,
        element_id TEXT,
        record_id TEXT,
        text TEXT,
        type TEXT,
        is_extracted TEXT,
        points JSONB,
        system TEXT,
        layout_width INTEGER,
        layout_height INTEGER,
        filetype TEXT,
        languages TEXT[],
        page_number TEXT,
        image_mime_type TEXT,
        url TEXT,
        record_locator JSONB
    );
    ```

    ```sql PostgreSQL with pgvector  theme={null}
    -- The fields "id", "element_id", "record_id", and "text" are required.
    -- "embeddings" is required if you are generating vector embeddings.
    --   If you are generating embeddings, the number of dimensions in "embeddings" 
    --   must match the number of dimensions for the associated embedding model 
    --   that you use in any related Unstructured workflows or ingestion pipelines.
    -- "type" is an optional field, but highly recommended.
    -- All other "metadata" fields are optional.
    CREATE EXTENSION vector;

    CREATE TABLE elements (
        id UUID PRIMARY KEY,
        element_id TEXT,
        record_id TEXT,
        text TEXT,
        type TEXT,
        embeddings vector(1536),
        is_extracted TEXT,
        points JSONB,
        system TEXT,
        layout_width INTEGER,
        layout_height INTEGER,
        filetype TEXT,
        languages TEXT[],
        page_number TEXT,
        image_mime_type TEXT,
        url TEXT,
        record_locator JSONB
    );
    ```
  </CodeGroup>

  Unstructured cannot provide a schema that is guaranteed to work in all
  circumstances. This is because these schemas will vary based on your source files' types; how you
  want Unstructured to partition, chunk, and generate embeddings; any custom post-processing code that you run; and other factors.

  See also:

  * [CREATE TABLE](https://www.postgresql.org/docs/current/sql-createtable.html) for PostgreSQL
  * [CREATE TABLE](https://github.com/pgvector/pgvector) for PostrgreSQL with pgvector
  * [Unstructured document elements and metadata](/api-reference/legacy-api/partition/document-elements)

  The following video shows how to use the `psql` utility to connect to PostgreSQL, list databases, and list and create tables:

  <iframe width="560" height="315" src="https://www.youtube.com/embed/IKo-4QHdNF4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

* A user in the database, and a password for the user.

  * For Amazon RDS for PostgreSQL, learn how to [create a user](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.Roles.html).
  * For Azure Database for PostgreSQL, learn how to [create a user](https://learn.microsoft.com/azure/postgresql/flexible-server/how-to-create-users).
  * For local PostgreSQL installations, learn how to [create a user](https://www.postgresql.org/docs/current/sql-createuser.html).
  * For other installation types, see your PostgreSQL provider's documentation.

* Database access for the user.

  * For Amazon RDS for PostgreSQL, learn how to [control user access](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.Access.html).
  * For Azure Database for PostgreSQL, learn how to [control user access](https://www.postgresql.org/docs/current/sql-createuser.html).
  * For local PostgreSQL installations, learn how to [give database access to a user](https://www.postgresql.org/docs/current/sql-grant.html).
  * For other installation types, see your PostgreSQL provider's documentation.

To create a PostgreSQL destination connector, see the following examples.

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
                  type="postgres",
                  config={
                      "host": "<host>",
                      "database": "<database>",
                      "port": <port>
                      "username": "<username>",
                      "password": "<password>",
                      "table_name": "<table_name>",
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
      "type": "postgres",
      "config": {
          "host": "<host>",
          "database": "<database>",
          "port": "<port>",
          "username": "<username>",
          "password": "<password>",
          "table_name": "<table_name>",
          "batch_size": <batch-size>
      }
  }'
  ```
</CodeGroup>

Replace the preceding placeholders as follows:

* `<name>` (required) - A unique name for this connector.
* `<host>` (required) - The host name.
* `<database>` (required) - The name of the database.
* `<port>` (required) - The port number.
* `<username>` (required) - The username.
* `<password>` (required) - The user's password.
* `<table_name>` (required) - The name of the table in the database.
* `<batch-size>` - The maximum number of rows to transmit at a time. The default is `100` if not otherwise specified.
* `<id-column>` (required, source connector only) - The name of the ID column in the table.
* For `fields` (source connector only), set one or more `<field>` values, with each value representing the name of a column to process (including the specified `<id-column>` column). The default is all columns if not otherwise specified.

## Learn more

* <Icon icon="blog" />  [PostgreSQL Integration in the Unstructured Platform](https://unstructured.io/blog/postgresql-integration-in-the-unstructured-platform)
