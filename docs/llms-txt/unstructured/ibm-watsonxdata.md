# Source: https://docs.unstructured.io/ui/destinations/ibm-watsonxdata.md

# Source: https://docs.unstructured.io/open-source/ingestion/destination-connectors/ibm-watsonxdata.md

# Source: https://docs.unstructured.io/api-reference/workflow/destinations/ibm-watsonxdata.md

# Source: https://docs.unstructured.io/ui/destinations/ibm-watsonxdata.md

# Source: https://docs.unstructured.io/open-source/ingestion/destination-connectors/ibm-watsonxdata.md

# Source: https://docs.unstructured.io/api-reference/workflow/destinations/ibm-watsonxdata.md

# Source: https://docs.unstructured.io/ui/destinations/ibm-watsonxdata.md

# Source: https://docs.unstructured.io/open-source/ingestion/destination-connectors/ibm-watsonxdata.md

# Source: https://docs.unstructured.io/api-reference/workflow/destinations/ibm-watsonxdata.md

# IBM watsonx.data

<Tip>
  The IBM watsonx.data destination connector relies on an Apache Iceberg-based catalog within the watsonx.data data store instance.
  Apache Iceberg is suitable for managed data storage and cataloging, but not for embedding storage or semantic similarity
  queries. For embedding storage and semantic similarity queries, Unstructured recommends that you use the following destination connectors
  instead:

  * [Astra DB](/api-reference/workflow/destinations/astradb)
  * [Milvus](/api-reference/workflow/destinations/milvus) on IBM watsonx.data
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

Send processed data from Unstructured to IBM watsonx.data.

The requirements are as follows.

* An [IBM Cloud account](https://cloud.ibm.com/login). [Create an IBM Cloud account](https://cloud.ibm.com/registration) if you do not already have one.

* An API key for the IBM Cloud account. If you do not have one already, create one as follows:

  <iframe width="560" height="315" src="https://www.youtube.com/embed/AsV8Edq_Lko" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

  1. [Log in to your IBM Cloud account](https://cloud.ibm.com/login).
  2. In the top navigation bar, click **Manage** and then, under **Security and access**, click **Access (IAM)**.
  3. On the sidebar, under **Manage identities**, click **API keys**.
  4. With the **View** list showing **My IBM Cloud API keys**, click **Create**.
  5. Enter some **Name** and an optional **Description** for the API key.
  6. Leave **Leaked action** set to **Disable the leaked key** and **Session management** set to **No**.
  7. Click **Create**.
  8. Click **Copy** or **Download** to copy or save the API key to a secure location. You won't be able to access this API key from this screen again.

* An IBM Cloud Object Storage (COS) instance in the account, and a bucket within that instance. If you do not have them already,
  create them as follows:

  <iframe width="560" height="315" src="https://www.youtube.com/embed/C_7q1EM8w20" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

  1. [Log in to your IBM Cloud account](https://cloud.ibm.com/login).
  2. On the sidebar, click the **Resource list** icon. If the sidebar is not visible, click the **Navigation Menu** icon to the far left of the
     top navigation bar.
  3. Click **Create resource**.
  4. With **IBM Cloud catalog** selected, search for and select **Object Storage**.
  5. Complete the on-screen instructions to finish creating the COS instance.
  6. With the COS instance's settings page shown, on the **Buckets** tab, click **Create bucket**.
  7. Complete the on-screen instructions to finish creating the bucket.

* The name, region, and public endpoint for the target bucket within the target Cloud Object Storage (COS) instance. To get these:

  1. [Log in to your IBM Cloud account](https://cloud.ibm.com/login).
  2. On the sidebar, click the **Resource list** icon. If the sidebar is not visible, click the **Navigation Menu** icon to the far left of the
     top navigation bar.
  3. In the list of resources, expand **Storage**, and then click the target COS instance.
  4. On the **Buckets** tab, click the target bucket.
  5. On the **Configuration** tab, note the following:

     * Under **Bucket details**, note the **Bucket name**. This is the bucket's name.
     * Under **Bucket details** section, note the value inside of the parentheses inside **Location**, for example `us-east`. This is the bucket's region.
     * Under **Endpoints**, note the value of **Public**, for example `s3.us-east.cloud-object-storage.appdomain.cloud`. (Ignore the values of
       **Private** and **Direct**). This is the bucket's public endpoint.

* An HMAC access key ID and secret access key for the target Cloud Object Storage (COS) instance. If you do not have them already,
  get or create them as follows:

  1. [Log in to your IBM Cloud account](https://cloud.ibm.com/login).

  2. On the sidebar, click the **Resource list** icon. If the sidebar is not visible, click the **Navigation Menu** icon to the far left of the
     top navigation bar.

  3. In the list of resources, expand **Storage**, and then click the target COS instance.

  4. On the **Service credentials** tab, if there is a credential that you want to use in the list, expand the credential, and copy the following values to a secure location:

     * `access_key_id` under `cos_hmac_keys`, which represents the HMAC access key ID.
     * `secret_access_key` under `cos_hmac_keys`, which represents the HMAC secret access key.

     After you have copied the preceding values, you have completed this procedure.

  5. If there is not a credential that you want to use, or there are no credentials at all, click **New Credential**.

  6. Enter some **Name** for the credential.

  7. For **Role**, select at least **Writer**, leave **Select Service ID** set to **Auto Generated**,
     switch on **Include HMAC Credential**, and then click **Add**.

  8. In the list of credentials, expand the credential, and copy the following values to a secure location:

     * `access_key_id` under `cos_hmac_keys`, which represents the HMAC access key ID.
     * `secret_access_key` under `cos_hmac_keys`, which represents the HMAC secret access key.

* An IBM watsonx.data data store instance in the IBM Cloud account. If you do not have one already, create one as follows:

  <iframe width="560" height="315" src="https://www.youtube.com/embed/oU21hQ9TUnU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

  1. [Log in to your IBM Cloud account](https://cloud.ibm.com/login).
  2. On the sidebar, click the **Resource list** icon. If the sidebar is not visible, click the **Navigation Menu** icon to the far left of the
     top navigation bar.
  3. Click **Create resource**.
  4. With **IBM Cloud catalog** selected, search for and select **watsonx.data**.
  5. Complete the on-screen instructions to finish creating the watsonx.data data store instance.

* An Apache Iceberg-based catalog within the watsonx.data data store instance. If you do not have one already, create one as follows:

  1. [Log in to your IBM Cloud account](https://cloud.ibm.com/login).

  2. On the sidebar, click the **Resource list** icon. If the sidebar is not visible, click the **Navigation Menu** icon to the far left of the
     top navigation bar.

  3. In the list of resources, expand **Databases**, and then click the target watsonx.data data store instance.

  4. Click **Open web console**.

  5. If prompted, log in to the web console.

  6. On the sidebar, click **Infrastructure manager**. If the sidebar is not visible, click the **Global navigation** icon to the far left of the
     top navigation bar.

  7. Click **Add component**.

  8. Under **Storage**, click **IBM Cloud Object Storage**, and then click **Next**.

  9. Complete the on-screen instructions to finish creating the Iceberg catalog. This includes providing the following settings:

     If you select **Discover COS instance**, you must provide the following settings:

     * The name of the target COS instance.
     * The name of the target storage object (such as the target bucket) within the COS instance.
     * Some display name for the component.
     * After you provide this information, do the following:

       a. Check the box labelled **Associate Catalog**.<br />
       b. For **Catalog type**, select **Apache Iceberg**.<br />
       c. Enter some **Catalog name**.<br />
       d. Click **Associate**.<br />

     If you select **Register my own**, you must provide the following settings:

     * Some display name for the component.
     * The name of the target bucket within the target Cloud Object Storage (COS) instance that you noted earlier.
     * The region for the target bucket, which you noted earlier.
     * The public endpoint for the target bucket, which you noted earlier. For this screen only, be sure to prefix the public endpoint with `https://`.
     * The HMAC access key ID for the target COS instance, which you noted earlier.
     * The HMAC secret access key for the target COS instance, which you noted earlier.
     * After you provide this information, do the following:

       a. Check the box labelled **Associate Catalog**.<br />
       b. For **Catalog type**, select **Apache Iceberg**.<br />
       c. Enter some **Catalog name**.<br />
       d. Click **Associate**.<br />

  10. On the sidebar, click **Infrastructure manager**. Make sure the catalog is associated with the appropriate engines. If it is not, rest your mouse
      on an unassociated target engine, click the **Manage associations** icon, check the box next to the target catalog's name, and then
      click **Save and restart engine**.

      To create an engine if one is not already shown, click **Add component**, and follow the on-screen to add an appropriate engine from the list of available **Engines**
      (for example, an **IBM Presto** engine).

* The catalog name and metastore REST endpoint for the target Iceberg catalog. To get this:

  1. [Log in to your IBM Cloud account](https://cloud.ibm.com/login).
  2. On the sidebar, click the **Resource list** icon. If the sidebar is not visible, click the **Navigation Menu** icon to the far left of the
     top navigation bar.
  3. In the list of resources, expand **Databases**, and then click the target watsonx.data data store instance.
  4. Click **Open web console**.
  5. If prompted, log in to the web console.
  6. On the sidebar, click **Infrastructure manager**. If the sidebar is not visible, click the **Global navigation** icon to the far left of the
     top navigation bar.
  7. In the **Catalogs** section, click the target Iceberg catalog.
  8. On the **Details** tab, note the value of **Name** representing the catalog name, and **Metastore REST endpoint** representing the metastore REST endpoint. (Ignore the **Metastore Thrift endpoint** value.)

* A namespace (also known as a schema) and a table in the target catalog. If you do not have these already, create them as follows:

  1. [Log in to your IBM Cloud account](https://cloud.ibm.com/login).
  2. On the sidebar, click the **Resource list** icon. If the sidebar is not visible, click the **Navigation Menu** icon to the far left of the
     top navigation bar.
  3. In the list of resources, expand **Databases**, and then click the target watsonx.data data store instance.
  4. Click **Open web console**.
  5. If prompted, log in to the web console.
  6. On the sidebar, click **Data manager**. If the sidebar is not visible, click the **Global navigation** icon to the far left of the
     top navigation bar.
  7. On the **Browse data** tab, under **Catalogs associated**, click the target catalog.
  8. Click the ellipses, and then click **Create schema**.
  9. Enter some **Name** for the schema, and then click **Create**.
  10. On the sidebar, click **Query workspace**.
  11. In the SQL editor, enter and run a table creation statement such as the following one that uses
      [Presto SQL](https://prestodb.io/docs/current/connector/iceberg.html) syntax, replacing `<catalog-name>` with the name of the target
      catalog and `<schema-name>` with the name of the target schema:

      ```sql  theme={null}
      CREATE TABLE <catalog-name>.<schema-name>.elements (
         "type" varchar,
         "element_id" varchar,
         "text" varchar,
         "file_directory" varchar,
         "filename" varchar,
         "languages" array(varchar),
         "last_modified" double,
         "page_number" varchar,
         "filetype" varchar,
         "url" varchar,
         "version" varchar,
         "record_locator" varchar,
         "date_created" double,
         "date_modified" double,
         "date_processed" double,
         "filesize_bytes" bigint,
         "points" varchar,
         "system" varchar,
         "layout_width" double,
         "layout_height" double,
         "id" varchar,
         "record_id" varchar,
         "parent_id" varchar
      )
      WITH (
         delete_mode = 'copy-on-write',
         format = 'PARQUET',
         format_version = '2'
      )
      ```

      Incoming elements that do not have matching column
      names will be dropped upon record insertion. For example, if the incoming data has an element named `sent_from` and there is no
      column named `sent_from` in the table, the `sent_from` element will be dropped upon record insertion. You should modify the preceding
      sample table creation statement to add columns for any additional elements that you want to be included upon record
      insertion.

      To increase query performance, Iceberg uses [hidden partitioning](https://iceberg.apache.org/docs/latest/partitioning/) to
      group similar rows together when writing. You can also
      [explicitly define partitions](https://prestodb.io/docs/current/connector/iceberg.html#create-table) as part of the
      preceding `CREATE TABLE` statement.

* The name of the target namespace (also known as a schema) within the target catalog, and name of the target table within that schema. To get these:

  1. [Log in to your IBM Cloud account](https://cloud.ibm.com/login).
  2. On the sidebar, click the **Resource list** icon. If the sidebar is not visible, click the **Navigation Menu** icon to the far left of the
     top navigation bar.
  3. In the list of resources, expand **Databases**, and then click the target watsonx.data data store instance.
  4. Click **Open web console**.
  5. If prompted, log in to the web console.
  6. On the sidebar, click **Data manager**. If the sidebar is not visible, click the **Global navigation** icon to the far left of the
     top navigation bar.
  7. On the **Browse data** tab, expand the name of the target catalog, and note the names of the target schema and target table.

* The name of the column in the target table that uniquely identifies each of the records in the table.

* To improve performance, the target table should be set to regularly remove old metadata files. To do this, run the following Python script.
  (You cannot use the preceding `CREATE TABLE` statement, or other SQL statements such as `ALTER TABLE`, to set this behavior.) To get the
  values for the specified environment variables, see the preceding instructions.

  ```python  theme={null}
  # Improves performance by setting the target table to regularly remove 
  # old metadata files. 
  #
  # First, install the following dependencies into your Python virtual 
  # environment:
  # 
  # pip install requests pyiceberg pyarrow
  #
  # Then, set the following environment variables:
  #
  # IBM_IAM_API_KEY - An API key value for the target IBM Cloud account.
  # IBM_ICEBERG_CATALOG_METASTORE_REST_ENDPOINT - The metastore REST endpoint 
  #     value for the target Apache Iceberg catalog in the target IBM watsonx.data 
  #     data store instance.
  # IBM_COS_BUCKET_PUBLIC_ENDPOINT - The target IBM Cloud Object Storage (COS) 
  #     instance’s endpoint value.
  # IBM_COS_ACCESS_KEY - An HMAC access key ID for the target COS instance.
  # IBM_COS_SECRET_ACCESS_KEY - The associated HMAC secret access key ID for the 
  #     target HMAC access key.
  # IBM_COS_BUCKET_REGION - The target COS instance’s region short ID.
  # IBM_ICEBERG_CATALOG - The name of the target Iceberg catalog.
  # IBM_ICEBERG_SCHEMA - The name of the target namespace (also known as a schema) 
  #     in the target catalog.
  # IBM_ICEBERG_TABLE - The name of the target table in the target schema.
  #
  # To get these values, see the Unstructured documentation for the 
  #     IBM watsonx.data connector.

  import os
  import requests
  from pyiceberg.catalog import load_catalog

  def main():
     # Get a bearer token for the target IBM Cloud account.   
     bearer_token = requests.post(
        url="https://iam.cloud.ibm.com/identity/token",
        headers={
              "Content-Type": "application/x-www-form-urlencoded",
              "Accept": "application/json"
        },
        data={
              "grant_type": "urn:ibm:params:oauth:grant-type:apikey", 
              "apikey": os.getenv("IBM_IAM_API_KEY")
        }
     ).json().get("access_token")

     # Connect to the target Iceberg catalog.
     catalog = load_catalog(
        os.getenv("IBM_ICEBERG_CATALOG"),
        **{
              "type": "rest",
              "uri": f"https://{os.getenv("IBM_ICEBERG_CATALOG_METASTORE_REST_ENDPOINT")}/mds/iceberg",
              "token": bearer_token,
              "warehouse": os.getenv("IBM_ICEBERG_CATALOG"),
              "s3.endpoint": os.getenv("IBM_COS_BUCKET_PUBLIC_ENDPOINT"),
              "s3.access-key-id": os.getenv("IBM_COS_ACCESS_KEY"),
              "s3.secret-access-key": os.getenv("IBM_COS_SECRET_ACCESS_KEY"),
              "s3.region": os.getenv("IBM_COS_BUCKET_REGION")
        },
     )
              
     # Load the target table.
     table = catalog.load_table(f"{os.getenv("IBM_ICEBERG_SCHEMA")}.{os.getenv("IBM_ICEBERG_TABLE")}")

     # Set the target table's properties to remove old metadata files.
     with table.transaction() as transaction:
        transaction.set_properties(
              {
                 "commit.manifest.min-count-to-merge": 10,
                 "commit.manifest-merge.enabled": True,
                 "write.metadata.previous-versions-max": 10,
                 "write.metadata.delete-after-commit.enabled": True,
              }
        )

     # Confirm that the target table's properties were set as expected.
     print(table.metadata.properties)

  if __name__ == "__main__":
     main()
  ```

To create an IBM watsonx.data destination connector, see the following examples.

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
                  type="ibm_watsonx_s3",
                  config={
                      "iceberg_endpoint": "<iceberg-endpoint>",
                      "object_storage_endpoint": "<object-storage-endpoint>",
                      "object_storage_region": "<object-storage-region>",
                      "iam_api_key": "<iam-api-key>",
                      "access_key_id": "<access-key-id>",
                      "secret_access_key": "<secret-access-key>",
                      "catalog": "<catalog>",
                      "namespace": "<namespace>",
                      "table": "<table>",
                      "max_retries": <max-retries>,
                      "max_retries_connection": <max-retries-connection>,
                      "record_id_key": "<record-id-key>"
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
      "type": "ibm_watsonx_s3",
      "config": {
          "iceberg_endpoint": "<iceberg-endpoint>",
          "object_storage_endpoint": "<object-storage-endpoint>",
          "object_storage_region": "<object-storage-region>",
          "iam_api_key": "<iam-api-key>",
          "access_key_id": "<access-key-id>",
          "secret_access_key": "<secret-access-key>",
          "catalog": "<catalog>",
          "namespace": "<namespace>",
          "table": "<table>",
          "max_retries": <max-retries>,
          "max_retries_connection": <max-retries-connection>,
          "record_id_key": "<record-id-key>"
      }
  }'
  ```
</CodeGroup>

Replace the preceding placeholders as follows:

* `<name>` (*required*) - A unique name for this connector.
* `<iceberg-endpoint>` (*required*): The metastore REST endpoint for the target Apache Iceberg-based catalog within the IBM watsonx.data data store instance. Do not include `https://` in this value.
* `<object-storage-endpoint>` (*required*): The public endpoint for the target bucket within the IBM Cloud Object Storage (COS) instance that is associated with the catalog. Do not include `https://` in this value.
* `<object-storage-region>` (*required*): The region short ID (such as us-east) for the bucket.
* `<iam-api-key>` (*required*): A valid API key value for the IBM Cloud account.
* `<access-key-id>` (*required*): A valid hash-based message authentication code (HMAC) access key ID for the COS instance.
* `<secret-access-key>` (*required*): The HMAC secret access key for the access key ID.
* `<catalog>` (*required*): The name of the target Apache Iceberg-based catalog within the IBM watsonx.data data store instance.
* `<namespace>` (*required*): The name of the target namespace (also known as a schema) within the catalog.
* `<table>` (*required*): The name of the target table within the namespace (schema).
* `<max-retries>`: The maximum number of retries for the upload process. Typically, an optimal setting is `150`. The default is `50`. If specified, it must be a number between `2` and `500`, inclusive.
* `<max-retries-connection>`: The maximum number of retries when connecting to the catalog. Typically, an optimal setting is `15`. The default is `10`. If specified, it must be a number between `2` and `100`, inclusive.
* `<record-id-key>`: The name of the column that uniquely identifies each record in the target table. The default is `record_id`.

## Learn more

* <Icon icon="blog" />  [Unstructured + IBM watsonx.data: A New OEM Partnership Powering the Future of Enterprise AI](https://unstructured.io/blog/unstructured-ibm-watsonx-data-a-new-oem-partnership-powering-the-future-of-enterprise-ai)
