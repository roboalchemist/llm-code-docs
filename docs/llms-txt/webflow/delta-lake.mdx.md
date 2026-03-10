# Source: https://developers.webflow.com/browser/data-exports/destinations/delta-lake.mdx

***

title: Delta Lake
slug: data-exports/destinations/delta-lake
description: Configure Delta Lake as a destination for Data Exports
-------------------------------------------------------------------

This guide walks you through configuring Delta Lake as a destination for your Webflow Analyze and Optimize data export.

Delta Lake can be set up on AWS S3, Google Cloud Storage, or Azure. Select your cloud provider below.

# Setting up AWS S3 Delta Lake

## Prerequisites

* By default, S3 authentication uses role-based access. You will need the trust policy prepopulated with Webflow's identifier to grant access.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "sts:AssumeRoleWithWebIdentity"
      ],
      "Principal": {
        "Federated": "accounts.google.com"
      },
      "Condition": {
        "StringEquals": {
          "accounts.google.com:oaud": "<some_organization_identifier>",
          "accounts.google.com:sub": "108000002380243782158"
        }
      }
    }
  ]
}
```

## Configuration steps

<Steps>
  ### Set up destination S3 bucket

  **Create bucket**

  1. Navigate to the **S3** service page.
  2. Click **Create bucket**.
  3. Enter a **Bucket name** and modify any of the default settings as desired. Note: **Object Ownership** can be set to "ACLs disabled" and **Block Public Access settings for this bucket** can be set to "Block all public access" as recommended by AWS. Make note of the **Bucket name** and **AWS Region**.
  4. Click **Create bucket**.

  ### Create policy and IAM role

  **Create policy**

  1. Navigate to the **IAM** service page.

  2. Navigate to the **Policies** navigation tab, and click **Create policy**.

  3. Click the **JSON** tab, and paste the following policy, being sure to replace `BUCKET_NAME` with the name of the bucket chosen in Step 1.

     ```json
     {
       "Version": "2012-10-17",
       "Statement": [
         {
           "Effect": "Allow",
           "Action": "s3:ListBucket",
           "Resource": "arn:aws:s3:::BUCKET_NAME"
         },
         {
           "Effect": "Allow",
           "Action": [
             "s3:GetObject",
             "s3:PutObject",
             "s3:DeleteObject"
           ],
           "Resource": "arn:aws:s3:::BUCKET_NAME/*"
         }
       ]
     }
     ```

  4. Click **Next: Tags**, click **Next: Review**.

  5. Name the policy, add a description, and click **Create policy**.

  **Create role**

  1. Navigate to the **IAM** service page.
  2. Navigate to the **Roles** navigation tab, and click **Create role**.
  3. Select **Custom trust policy** and paste the provided trust policy to allow AssumeRole access to the new role. Click **Next**.
  4. Add the permissions policy created above, and click **Next**.
  5. Enter a **Role name**, for example, `transfer-role`, and click **Create role**.
  6. Once successfully created, search for the created role in the Roles list, click the role name, and make a note of the **ARN** value.

     <Note>
       **Alternative authentication method: AWS User with HMAC Access Key ID & Secret Access Key**

       Role-based authentication is the preferred authentication mode for S3 based on AWS recommendations. However, HMAC Access Key ID & Secret Access Key is an alternative authentication method that can be used if preferred.

       1. Navigate to the **IAM** service page.
       2. Navigate to the **Users** navigation tab, and click **Add users**.
       3. Enter a **User name** for the service, for example, `transfer-service`, click **Next**. Under **Select AWS access type**, select the **Access key - Programmatic access** option. Click **Next: Permissions**.
       4. Click the **Attach existing policies directly** option, and search for the name of the policy created in the previous step. Select the policy, and click **Next: Tags**.
       5. Click **Next: Review** and click **Create user**.
       6. In the **Success** screen, record the **Access key ID** and the **Secret access key**.
     </Note>

  ### Add your destination

  Use the following details to complete the connection setup: **bucket name**, **bucket region**, and **role ARN**.

  * Instructions for [Analyze / Optimize for Webflow sites](https://help.webflow.com/hc/en-us/articles/49268470978963)
  * Instructions for [Optimize for non-Webflow sites](https://help-optimize.webflow.com/hc/en-us/articles/49271044687763)
</Steps>

# Setting up Google Cloud Delta Lake

## Prerequisites

* By default, GCS authentication uses role-based access. You will need the Webflow Data Sync Service Account email to grant access: `datasync-webflow@prql-prod.iam.gserviceaccount.com`.

## Configuration steps

<Steps>
  ### Create a service account

  1. In the GCP console, navigate to the **IAM & Admin** menu, click into the **Service Accounts** tab, and click **Create service account** at the top of the menu.
  2. In the first step, name the service account that will be used to transfer data into Cloud Storage and click **Create and Continue**. Click **Continue** in the following optional step without assigning any roles.
  3. In the **Grant users access to this service account** step, within the **Service account users role** field, enter the provided **Service account** (see prerequisite) and click **Done**.
  4. Once successfully created, search for the created service account in the service accounts list, click the **Service account** name to view the details, and make a note of the **email** (note: this is a different email the Webflow Data Sync Service Account).
  5. Select the permissions tab, find the provided principal name (**Service account** from the prerequisite), click the **Edit principal** button (pencil icon), click **Add another role**, select the **Service Account Token Creator** role, and click **Save**.

     ![](https://storage.googleapis.com/prequel_docs/images/gcp-grant-role.png)

     <Warning>
       **Alternative authentication method: Granting direct access to service account**

       Role-based authentication is the preferred authentication mode for GCS based on GCP recommendations. However, providing a service account key to directly log in to the created service account is an alternative authentication method that can be used if preferred.

       1. Back in the **Service accounts** menu, click the Actions dropdown next to the newly created service account and click **Manage keys**.

          ![](https://storage.googleapis.com/prequel_docs/images/gcp-manage-service-account-keys.png "manage sa keys.png")

       2. Click **Add key** and then **Create new key**.

          ![](https://storage.googleapis.com/prequel_docs/images/gcp-create-new-key.png "create new key sa.png")

       3. Select the **JSON** Key type and click **Create** and make note of the key that is generated.
     </Warning>

  ### Create destination GCS bucket

  1. Navigate to the **Cloud Storage** page.

  2. Click **Create**.

  3. Enter a **bucket name**, choose a **region**. **Note**: at the **Choose how to control access to objects** step, we recommend selecting **Enforce public access prevention on this bucket**.

     ![](https://storage.googleapis.com/prequel_docs/images/gcs-prevent-public-access.png)

  4. After choosing your preferences for the remaining steps, click **Create**.

  5. On the **Bucket details** page for the bucket you created, select the **Permissions** tab, and click **Grant access**.

  6. Grant access to the principal (Service Account) you created in **Step 1** (*Note: this is the service account you created, not the service account from the prerequisite*), and assign the Roles: **Storage Legacy Bucket Writer**, **Storage Legacy Bucket Reader**, **Storage Legacy Object Reader**. Click **Save**.

     ![](https://storage.googleapis.com/prequel_docs/images/gcp-storage-legacy-bucket-writer.png)

  ### Add your destination

  Use the following details to complete the connection setup: **bucket name**, your chosen **folder name** for the data, and your **Service account email**.

  * Instructions for [Analyze / Optimize for Webflow sites](https://help.webflow.com/hc/en-us/articles/49268470978963)
  * Instructions for [Optimize for non-Webflow sites](https://help-optimize.webflow.com/hc/en-us/articles/49271044687763)
</Steps>

# Setting up Azure Delta Lake

## Configuration steps

<Steps>
  ### Create Azure storage account

  1. In the Azure portal, navigate to the **Storage accounts** service and click **+ Create**.

  2. In the "Basics" tab of the "Create a storage account" form, fill in the required details.

  3. In the "Advanced" settings, under "Security" make sure **Enable storage account key access** is turned on. You may turn off (deselect) "Allow enabling public access on containers". Under "Data Lake Storage Gen2", select **Enable hierarchical namespace**.

     ![](https://storage.googleapis.com/prequel_docs/images/azure-settings-toggles.png "azure settings toggles.png")

  4. In the "Networking" settings, you may limit "Network access" to either **Enable public access from all networks** or **Enable public access from selected virtual networks and IP addresses**. If the latter is selected, be sure to add Webflow's static IP to the address range of the chosen virtual network. All other settings can use the default selections.

  5. In the "Data protection" settings, you must turn off **Enable soft delete for blobs**, **Enable soft delete for containers**, and **Enable soft delete for file shares**.

     ![](https://storage.googleapis.com/prequel_docs/images/azure-turn-off-settings.png "disable default soft delete settings.png")

  6. Once the remaining options have been configured to your preference, click **Create**.

  ### Create container and access token

  1. In the Azure portal, navigate to the **Storage accounts** service and click on the account that was created in the previous step.
  2. In the navigation pane, under "Data storage", click **Containers**. Click **+ Container**, choose a name for the container, and click **Create**.
  3. In the navigation pane, under "Security + networking", click **Access keys**.
  4. Make a note of the **Key** that is generated for either key1 or key2.

  ### Add your destination

  Use the following details to complete the connection setup: **storage account name**, **container name**, your chosen **folder name** for the data, and your **Access key**.

  * Instructions for [Analyze / Optimize for Webflow sites](https://help.webflow.com/hc/en-us/articles/49268470978963)
  * Instructions for [Optimize for non-Webflow sites](https://help-optimize.webflow.com/hc/en-us/articles/49271044687763)
</Steps>

# Understanding Delta Lake configuration options

<Warning>
  Changing these attributes on an existing destination table will not take effect until you perform a full refresh of the table.
</Warning>

## Protocol compatibility summary

The table below outlines the recommended settings for each feature to qualify for a given protocol minimum reader version. Adjust your configuration to match the protocol version required by your downstream readers.

| Protocol MinReader Version | Column Mapping Mode | Deletion Vectors         | Change Data Feed |
| -------------------------- | ------------------- | ------------------------ | ---------------- |
| 1                          | NONE                | Disabled (Copy-on-Write) | Disabled         |
| 2                          | NONE                | Disabled (Copy-on-Write) | Disabled         |
| 3                          | ID                  | Enabled (Merge-on-Read)  | Enabled          |

*For more details on protocol compatibility, please refer to the [Delta Feature Compatibility documentation](https://docs.delta.io/2.0.2/versioning.html).*

There are four key Delta Lake table properties that affect both performance and protocol compatibility. Adjust these settings carefully based on your performance needs and the protocol version supported by your readers.

### retention\_window\_days

**Purpose:** Sets the number of days for which historical data (e.g., previous table versions used for time travel or auditing) is retained.

**Recommendation:** Set this value according to your organization's internal data retention policies.

### column\_mapping\_mode

**Purpose:** Controls how columns are mapped between the underlying storage and the table schema. This setting is critical during schema evolution.

**Recommendation:** Set this to `ID` for robust, identifier-based mapping. Use a different setting (such as `NONE` or `NAME`) only if you need to support a lower protocol reader version.

### deletion\_vectors\_disabled

**Purpose:** Determines whether deletion vectors are used.

* **Deletion Vectors** enable the **merge-on-read** approach, where modifications (like deletes) are applied by marking rows as deleted without rewriting the underlying Parquet files.
* The traditional **copy-on-write** approach rewrites entire files for each change, which can be slower for small modifications.

**Recommendation:**

* **Enable deletion vectors** (i.e., set `deletion_vectors_disabled` to false) to leverage merge-on-read performance benefits.
* **Disable deletion vectors** if you must support a lower minimum reader version.

### change\_data\_feed\_disabled

**Purpose:** Controls whether the change data feed (CDF) is active. The CDF records row-level changes (inserts, updates, and deletes) for incremental processing, auditing, or real-time analytics.

**Recommendation:**

* **Keep change data feed enabled** (i.e., set `change_data_feed_disabled` to false) by default.
* **Disable change data feed** only if you need to support a lower minimum reader version.

## FAQs

<Accordion title="What is Delta Lake and why should I use it?">
  Delta Lake delivers warehouse-native capabilities such as upserts, time travel, and schema evolution—with the simplicity, scalability, and secure permissions model of an object storage bucket. It gives you the advanced transactional features and data consistency of a data warehouse while eliminating extra compute costs and provisioning required to write directly to a warehouse. This enables your warehouse to be isolated from data sharing, so you can receive data without exposing your internal resources.
</Accordion>

<Accordion title="Why do you need permissions to delete data?">
  Delta Lake uses vacuum operations to clean up obsolete data files and maintain transaction isolation. The writer must have delete permissions so that vacuuming can safely remove outdated files without compromising the consistency and isolation of ongoing transactions.
</Accordion>

<Accordion title="Can I send the data to a specific prefix in a bucket?">
  Yes, you can direct data to a specific prefix. However, we recommend using a completely isolated bucket to receive data. The Delta Lake destination requires permissions to list objects in the entire bucket, meaning all permissions cannot be scoped to a specific prefix. Isolating the destination to a dedicated bucket minimizes security risks and reduces the chance of malformed data mixing with other datasets.
</Accordion>

<Accordion title="Do I need to perform maintenance operations on the Delta Lake table?">
  No, the data writer is responsible for vacuuming and compacting data as needed. Data consumers should not run any non read queries on the table.
</Accordion>

<Accordion title="How do I know when a table has been updated?">
  To check for updates, you can query the table history. In Spark or Databricks SQL, run:

  ```sql
  DESCRIBE HISTORY table_name LIMIT 1;
  ```

  This command returns the most recent commit details. Additionally, most bucket providers offer the capability to trigger a webhook or lambda when objects are created. Configure the trigger to execute whenever a file is created in `s3://bucket-name/<configured_path>/<table_name>/_delta_log` to know when a table has been updated.
</Accordion>

<Accordion title="What is the difference between merge-on-read and copy-on-write in Delta Lake?">
  * **Merge-on-Read:** Uses deletion vectors to mark rows as deleted or modified without rewriting entire files. This approach speeds up incremental updates by applying changes during read time.
  * **Copy-on-Write:** Rewrites entire Parquet files upon any modification, which can be less efficient for small or frequent changes.
</Accordion>

# Mounting Delta Lake to analytics platforms

## Mounting AWS S3 Delta Lake to Athena

<Error>
  **Protocol MinReader Version:** Athena requires delta lake tables compatible with Protocol MinReader Version 1.
</Error>

1. In the AWS console, navigate to the Athena query editor.
2. Choose the same region as your configured bucket.
3. Execute the following SQL:

   ```sql
   CREATE EXTERNAL TABLE IF NOT EXISTS schema.table_name
      LOCATION 's3://bucket-name/<configured_path>/<table_name>'
      TBLPROPERTIES ('table_type' = DELTA);
   ```

## Mounting GCS Delta Lake to BigQuery

<Error>
  **Protocol MinReader Version:** BigQuery requires delta lake tables compatible with Protocol MinReader Version 3.
</Error>

1. In the Google Cloud console, navigate to the BigQuery Console.
2. Click the **+ Add Data** button at the top left of the console.
3. Select Google Cloud Storage as a Data Source.
4. Select **GCS: (Manual) BigLake External & External Tables: BigQuery** option.
5. Set the file format to **Delta**, then provide the path expression `'<bucket-name>/<configured_path>/<table_name>'`.
6. Choose a Dataset in the same region as the bucket and a table name.
7. Choose Table Type **External Table**.
8. Create your external table and query data to test.

<Info>
  **Schema Evolution:** The external table must be manually refreshed anytime new columns are added. Consult GCP documentation for instructions.
</Info>

## Mounting AWS S3 Delta Lake to ClickHouse

<Info>
  **Managed Credentials:** Clickhouse supports [managed credentials](https://clickhouse.com/docs/integrations/s3#managing-credentials) so that access key or role information does not need to be included in the `CREATE TABLE...` syntax.
</Info>

1. Open a Clickhouse SQL session.
2. Execute the following SQL:

   ```sql
   CREATE TABLE schema.table_name AS
   ENGINE = DeltaLake(
      's3://bucket-name/<configured_path>/<table_name>',
      '<AWS_ACCESS_ID>',
      '<AWS_SECRET_KEY>'
   );
   ```

## Mounting AWS S3 Delta Lake to DuckDB/MotherDuck

<Error>
  **Column Mapping:** DuckDB requires delta lake tables use column mapping mode `NONE`.
</Error>

<Info>
  **Secrets Manager:** DuckDB has a [secrets manager](https://duckdb.org/docs/stable/configuration/secrets_manager.html) which can be used in order for the access key or role information to not need to be included in the `CREATE TABLE...` syntax.
</Info>

1. Install the [DuckDB Delta extension](https://duckdb.org/docs/stable/extensions/delta.html).
2. Open a DuckDB SQL session.
3. Execute the following SQL:

   ```sql
   CREATE VIEW schema.table_name AS
   SELECT
      *
   FROM deltaLake(
      's3://bucket-name/<configured_path>/<table_name>',
      '<AWS_ACCESS_ID>',
      '<AWS_SECRET_KEY>'
   );
   ```

## Mounting S3 Delta Lake to Databricks (Unity)

1. Ensure your Databricks session has read access to the configured bucket.
2. Open a Databricks SQL session.
3. Execute the following SQL:

   ```sql
   CREATE VIEW schema.table_name AS
   SELECT
      *
   FROM delta.`s3a://bucket-name/metastore/<configured_path>/<table_name>`;
   ```

## Mounting S3 Delta Lake to Redshift

<Error>
  **Protocol MinReader Version:** Redshift requires delta lake tables compatible with Protocol MinReader Version 1.
</Error>

1. On the AWS Glue console, choose Crawlers in the navigation pane.
2. Choose Create crawler.
3. For Name, enter a name and choose "Next".
4. For Data source configuration, choose "Not yet".
5. For Data source, choose Add a data source.
6. For Data source, select Delta Lake.
7. For Include delta lake table paths, enter `s3://bucket-name/<configured_path>/<table_name>`.
8. Select Enable write manifest, then choose Add a Delta Lake data source. Choose Next.
9. For IAM role, either select an existing role or create one with permissions to Glue and the bucket.
10. For Target database, choose Add database, then Create a database page is shown.
11. For Name, enter a name, then choose Create database. Then come back to the previous page. For Target database, click the reload button, and select the created database.
12. For Frequency under Crawler schedule, choose double the frequency data is delivered. For example for data arriving on hourly minute frequency, choose 30 minutes.
13. Review your configuration, and choose Create crawler. You can trigger the crawler to run manually via the AWS Glue console, or through the SDK or AWS CLI using the StartCrawl API. You could also schedule a trigger via the AWS Glue console.
14. Wait for the crawler to complete.
15. Navigate to Redshift and inspect the awsdatacatalog to find the newly created table.

## Reading S3 Delta Lake with PySpark

<Info>
  **Broad Compatibility:** Spark can consume Delta Lake tables from S3, Google Cloud Storage, Azure Blob Storage, or other S3 compatible object stores. Delta Lake reads can be done in Java, Python, or Scala Spark.
</Info>

In your PySpark code, run the following to instantiate a dataframe backed by your delta table:

```python
df = spark.read.format("delta").load("s3://bucket-name/<configured_path>/<table_name>")
```

## Mounting S3 Delta Lake to Snowflake

<Error>
  **Protocol MinReader Version:** Snowflake requires delta lake tables compatible with Protocol MinReader Version 2.
</Error>

1. Open a Snowflake client.
2. Execute the following SQL, choose your frequency based on desired data freshness:

   ```sql
   CREATE OR REPLACE CATALOG INTEGRATION delta_catalog_name
     CATALOG_SOURCE = OBJECT_STORE
     TABLE_FORMAT = DELTA
     ENABLED = TRUE;

   CREATE OR REPLACE EXTERNAL VOLUME ext_volume_name
     STORAGE_LOCATIONS = (
       (
         NAME = 'some_name'
         STORAGE_PROVIDER = S3
         ...
       )
     )
     ALLOW_WRITES = FALSE;

   CREATE ICEBERG TABLE schema.table_name
     CATALOG = delta_catalog_name
     EXTERNAL_VOLUME = ext_volume_name
     BASE_LOCATION = '<configured_path>/<table_name>';

   CREATE OR REPLACE TASK task_name
     SCHEDULE = 'USING CRON 0/5 * * * * America/Los_Angeles' -- Runs every 5 minutes, change cron to match desired freshness
     ...
   AS
      ALTER ICEBERG TABLE schema.table_name REFRESH;
   ```

## Mounting Delta Lake to Microsoft Fabric & Microsoft OneLake

<Error>
  **Column Mapping:** Requires delta lake tables use column mapping mode `NONE`.
</Error>

1. Navigate to Microsoft Fabric.

2. Navigate to your lakehouse, if you do not have one, create one.

3. In your lakehouse, select the ellipses (…) next to Tables and then select "New shortcut".

   ![](https://learn.microsoft.com/en-us/fabric/onelake/media/onelake-shortcuts-adb-quickstart/new-table-shortcut.png)

4. In the New shortcut screen, select your bucket provider. Normally this will be Azure Data Lake Storage Gen2 tile.

5. Connect to your bucket and select the path of the delta lake table `'<configured_path>'/<table_name>'`.

   ![](https://learn.microsoft.com/en-us/fabric/onelake/media/onelake-shortcuts-adb-quickstart/connection-details.png)

6. After creating the shortcut, the shortcut should appear as a Delta table under Tables. It may appear as "Unidentified", this is a UI bug in Azure.

7. To confirm the table is correctly mounted, select "SQL Analytics endpoint" from the drop down to the left of the "share" button, in the top right of the console.

8. The shortcut should correctly appear as a Delta table under Tables.

9. (Optional) Click the "New semantic model" button at the top of the page to setup the mounted table for use in Microsoft products like PowerBI.

<Info>
  **Vector Support:** Azure Fabric and Microsoft OneLake do not support Delta Lake vector columns. These columns will be omitted from any table you mount.
</Info>
