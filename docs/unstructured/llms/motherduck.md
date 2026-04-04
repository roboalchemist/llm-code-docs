# Source: https://docs.unstructured.io/ui/destinations/motherduck.md

# Source: https://docs.unstructured.io/open-source/ingestion/destination-connectors/motherduck.md

# Source: https://docs.unstructured.io/api-reference/workflow/destinations/motherduck.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.unstructured.io/llms.txt
> Use this file to discover all available pages before exploring further.

# MotherDuck

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

Send processed data from Unstructured to MotherDuck.

The requirements are as follows.

<iframe width="560" height="315" src="https://www.youtube.com/embed/tj_0qmvPpJQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

* A [MotherDuck account](https://app.motherduck.com).

* A [MotherDuck access token](https://motherduck.com/docs/key-tasks/authenticating-and-connecting-to-motherduck/authenticating-to-motherduck/#creating-an-access-token) for the account.

* A database in the account.

  * [Create a database](https://motherduck.com/docs/sql-reference/motherduck-sql-reference/create-database/).
  * [List available databases](https://motherduck.com/docs/key-tasks/database-operations/basics-operations/#listing-databases).

  You can run commands to manage MotherDuck databases, schemas, tables, and more in the
  [MotherDuck UI](https://motherduck.com/docs/getting-started/motherduck-quick-tour/) or for example by connecting to MotherDuck with the
  [DuckDB CLI](https://motherduck.com/docs/key-tasks/authenticating-and-connecting-to-motherduck/connecting-to-motherduck/).

* A schema in the target database.

  * [Create a schema](https://duckdb.org/docs/sql/statements/create_schema.html).
  * You can list available schemas and their parent catalogs by running the following command in the MotherDuck UI or the DuckDB CLI:

    ```sql  theme={null}
    SELECT * FROM information_schema.schemata;
    ```

  The MotherDuck connector uses the default schema name of `main` if not otherwise specified.

* A table in the target schema.

  * [Create a table](https://duckdb.org/docs/sql/statements/create_table).
  * You can list available tables in a schema by running the following commands in the MotherDuck UI or the DuckDB CLI, replacing the target catalog and schema names:

    ```sql  theme={null}
    USE <catalog_name>.<schema_name>;
    SHOW TABLES;
    ```

  The MotherDuck connector uses the default table name of `elements` if not otherwise specified.

  For maximum compatibility, Unstructured recommends the following table schema:

  ```sql  theme={null}
  CREATE TABLE elements (
      id VARCHAR,
      element_id VARCHAR,
      text TEXT,
      embeddings FLOAT[],
      type VARCHAR,
      system VARCHAR,
      layout_width DECIMAL,
      layout_height DECIMAL,
      points TEXT,
      url TEXT,
      version VARCHAR,
      date_created INTEGER,
      date_modified INTEGER,
      date_processed DOUBLE,
      permissions_data TEXT,
      record_locator TEXT,
      category_depth INTEGER,
      parent_id VARCHAR,
      attached_filename VARCHAR,
      filetype VARCHAR,
      last_modified TIMESTAMP,
      file_directory VARCHAR,
      filename VARCHAR,
      languages VARCHAR[],
      page_number VARCHAR,
      links TEXT,
      page_name VARCHAR,
      link_urls VARCHAR[],
      link_texts VARCHAR[],
      sent_from VARCHAR[],
      sent_to VARCHAR[],
      subject VARCHAR,
      section VARCHAR,
      header_footer_type VARCHAR,
      emphasized_text_contents VARCHAR[],
      emphasized_text_tags VARCHAR[],
      text_as_html TEXT,
      regex_metadata TEXT,
      detection_class_prob DECIMAL,
      partitioner_type VARCHAR
  );
  ```

  You can list the schema of a table by running the following commands in the MotherDuck UI or the DuckDB CLI, replacing the target catalog, schema, and table names:

  ```sql  theme={null}
  USE <catalog_name>.<schema_name>;
  DESCRIBE TABLE <table_name>;
  ```

To create a MotherDuck destination connector, see the following examples.

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
                  type="motherduck",
                  config={
                      "database": "<database>",
                      "db_schema": "<db-schema>",
                      "table": "<table>",
                      "md_token": "<md-token>"
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
      "type": "motherduck",
      "config": {
          "database": "<database>",
          "db_schema": "<db-schema>",
          "table": "<table>",
          "md_token": "<md-token>"
      }
  }'
  ```
</CodeGroup>

Replace the preceding placeholders as follows:

* `<name>` (*required*): A unique name for this connector.
* `<database>` (*required*): The name of the target MotherDuck database.
* `<db-schema>` (*required*): The name of the target schema within the database.
* `<table>` The name of the target table within the schema. By default, this table is named `elements` if not otherwise specified.
* `<md-token>` (*required*): The access token value within the MotherDuck account that has the appropriate access to the target database, schema, and table.

## Learn more

* <Icon icon="blog" />  [Unstructured's New MotherDuck Integration](https://unstructured.io/blog/unstructured-s-new-motherduck-integration)
