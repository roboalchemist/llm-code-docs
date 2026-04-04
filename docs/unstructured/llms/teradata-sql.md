# Source: https://docs.unstructured.io/ui/sources/teradata-sql.md

# Source: https://docs.unstructured.io/ui/destinations/teradata-sql.md

# Source: https://docs.unstructured.io/open-source/ingestion/source-connectors/teradata-sql.md

# Source: https://docs.unstructured.io/open-source/ingestion/destination-connectors/teradata-sql.md

# Source: https://docs.unstructured.io/api-reference/workflow/sources/teradata-sql.md

# Source: https://docs.unstructured.io/api-reference/workflow/destinations/teradata-sql.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.unstructured.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Teradata

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

Send processed data from Unstructured to Teradata.

The requirements are as follows.

* A Teradata Vantage system that can be accessed by its host name or IP address.

  For example, a Teradata Vantage system in Teradata ClearScape Analytics Experience includes:

  * A Teradata ClearScape Analytics Experience account.
  * An environment in the account.
  * A Teradata Vantage database in the environment.
  * The name and password for a Teradata user who has the appropriate access to the database.

  [Learn how to create these in Teradata ClearScape Analytics Experience](https://developers.teradata.com/quickstarts/get-access-to-vantage/clearscape-analytics-experience/getting-started-with-csae/).

* The system's corresponding host name or IP address.

  For example, you can get these values from Teradata ClearScape Analytics Experience as follows:

  1. Sign in to your Teradata ClearScape Analytics Experience account.<br />
  2. On the sidebar, under **Environments**, click the name of the database's corresponding environment.<br />
  3. Under **Connection details for Vantage database**, use the **Host** value.<br />

* The name of the target database in the system. To get a list of available databases in the system, you can run a Teradata SQL query such as the following:

  ```sql  theme={null}
  SELECT DatabaseName 
  FROM DBC.DatabasesV 
  ORDER BY DatabaseName;
  ```

* The name of the target table in the database. To get a list of available tables in a database, you can run a Teradata SQL query such as the following, replacing `<database-name>` with the name of the target database:

  ```sql  theme={null}
  SELECT TableName
  FROM DBC.TablesV
  WHERE DatabaseName = '<database-name>' AND TableKind = 'T'
  ORDER BY TableName;
  ```

  When Unstructured writes rows to a table, the table's columns must have a schema that is compatible with Unstructured.
  Unstructured cannot provide a schema that is guaranteed to work for everyone in all circumstances.
  This is because these schemas will vary based on
  your source files' types; how you want Unstructured to partition, chunk, and generate embeddings;
  any custom post-processing code that you run; and other factors.

  In any case, note the following about table schemas:

  * The following columns are always required by Unstructured: `record_id` and `element_id`.
  * The following columns are optional for Unstructured, but highly recommended: `text` and `type`.
  * The rest of the columns are optional and typically will be output by Unstructured as part of the `metadata` field.
  * If Unstructured is generating vector embeddings, the `embeddings` column is also required.

    <Warning>
      The destination connector outputs Unstructured-generated [embeddings](/ui/embedding) that are not directly compatible
      with Teradata Enterprise Vector Store. To use embeddings with Teradata Enterprise Vector Store, Unstructured
      recommends that you choose from among the following options:

      * Define a column in your target table named `embeddings` that is of type `VARCHAR(64000)`, to store the
        Unstructured-generated embeddings. After Unstructured adds its embeddings to your `embeddings` column,
        choose from among Teradata's options to convert the `embeddings` column's `VARCHAR` values to the
        Teradata [VECTOR Data Type](https://docs.teradata.com/r/Enterprise_IntelliFlex_VMware/Teradata-Vector-Store-User-Guide/Vector-Store-Components-and-Features/VECTOR-Data-Type)
        yourself.
      * Omit any columns named `embedding`, `message`, or `num_tokens` from your target table. Then choose from
        among Teradata's options (such as [AI\_TextEmbeddings](https://docs.teradata.com/r/Enterprise_IntelliFlex_VMware/Teradata-Vector-Store-User-Guide/Vector-Store-Components-and-Features/In-Database-Analytic-Functions-for-Vector-Store))
        to have Teradata generate the embeddings for you, instead of having Unstructured generate them.
    </Warning>

  Here is an example table schema that is compatible with Unstructured. It includes all of the required and recommended columns, as
  well as a few additional columns that are typically output by Unstructured as part of the `metadata` field. Be sure to replace
  `<database-name>` with the name of the target database and `<table-name>` with the name of the target table (by Unstructured convention,
  the table name is typically `elements`, but this is not a requirement).

  ```sql  theme={null}
  CREATE SET TABLE "<database-name>"."<table-name>" (
    "id" VARCHAR(64) NOT NULL,
    PRIMARY KEY ("id"),
    "record_id" VARCHAR(64),
    "element_id" VARCHAR(64),
    "text" VARCHAR(32000) CHARACTER SET UNICODE,
    "type" VARCHAR(50),
    "embeddings" VARCHAR(64000), -- Add this column only if Unstructured is generating vector embeddings.
    "last_modified" VARCHAR(50),
    "languages" VARCHAR(200),
    "file_directory" VARCHAR(500),
    "filename" VARCHAR(255),
    "filetype" VARCHAR(50),
    "record_locator" VARCHAR(1000),
    "date_created" VARCHAR(50),
    "date_modified" VARCHAR(50),
    "date_processed" VARCHAR(50),
    "permissions_data" VARCHAR(1000),
    "filesize_bytes" INTEGER,
    "parent_id" VARCHAR(64)
  )
  ```

* For the source connector, the name of the primary key column in the table (for example, a column named `id`, typically defined as `"id" VARCHAR(64) NOT NULL, PRIMARY KEY ("id")`).

* For the source connector, the names of any specific columns to fetch from the table. By default, all columns are fetched unless otherwise specified.

* For the destination connector, the name of the column in the table that uniquely identifies each record for Unstructured to perform any necessary record updates. By default convention, Unstructured expects this field to be named `record_id`.

* The name of the Teradata user who has the appropriate access to the target database.

  For example, you can get this from Teradata ClearScape Analytics Experience as follows:

  1. Sign in to your Teradata ClearScape Analytics account.<br />
  2. On the sidebar, under **Environments**, click the name of the database's corresponding environment.<br />
  3. Under **Connection details for Vantage database**, use the **Username** value.<br />

  The Teradata SQL command to get a list of available users is as follows:

  ```sql  theme={null}
  SELECT UserName 
  FROM DBC.UsersV 
  ORDER BY UserName;
  ```

* The password for the user, which was set up when the user was created.

  If the user has forgotten their password, the Teradata SQL command to change a user's password is as follows, replacing `<user-name>` with the name of the user and `<new-password>` with the new password:

  ```sql  theme={null}
  MODIFY USER <user-name> SET PASSWORD = '<new-password>';
  ```

  To change a user's password, you must be an administrator (such as the `DBC` user or another user with `DROP USER` privileges).

To create a Teradata destination connector, see the following examples.

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
                  type="teradata",
                  config={
                      "host": "<host>",
                      "database": "<database>",
                      "table_name": "<table-name>",
                      "batch_size": <batch-size>,
                      "record_id_key": "<record-id-key>",
                      "username": "<username>",
                      "password": "<password>"
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
      "type": "teradata",
      "config": {
          "host": "<host>",
          "database": "<database>",
          "table_name": "<table-name>",
          "batch_size": <batch-size>,
          "record_id_key": "<record-id-key>",
          "username": "<username>",
          "password": "<password>"
      }
  }'
  ```
</CodeGroup>

Replace the preceding placeholders as follows:

* `<name>` (*required*) - A unique name for this connector.
* `<host>` (*required*): The hostname or IP address associated with the target Teradata Vantage database.
* `<database>`: The name of the target database. By default, the default database name is used if not otherwise specified. To get the name of the default database, you can run the Teradata SQL command `SELECT DATABASE;`.
* `<table-name>` (*required*): The name of the target table in the database.
* `<batch-size>`: The maximum number of rows per batch. The default is `100` if not otherwise specified.
* `<id-column>` (*required*, source connector only): The name of the primary key column that Teradata uses to uniquely identify each record in the table.
* `<record-id-key>` (destination connector only): The name of the column that Unstructured uses to uniquely identify each record in the table for record update purposes. The default is `record_id` if not otherwise specified.
* `<column-name>` (source connector only): The name of a column to fetch from the table. By default, all columns are fetched unless otherwise specified.
* `<username>` (*required*): The name of the user who has the appropriate access to the database.
* `<password>` (*required*): The password for the user.
