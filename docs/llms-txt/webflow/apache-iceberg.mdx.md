# Source: https://developers.webflow.com/browser/data-exports/destinations/apache-iceberg.mdx

***

title: Apache Iceberg
slug: data-exports/destinations/apache-iceberg
description: Configure Apache Iceberg as a destination for Data Exports
-----------------------------------------------------------------------

This guide walks you through configuring Apache Iceberg as a destination for your Webflow Analyze and Optimize data export.

Apache Iceberg requires a central catalog to manage table metadata and provide atomic transactions. We support several catalog options, each with its own setup guide below:

* **[AWS Glue Catalog](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-format-iceberg.html)**
* **[AWS S3 Tables Catalog](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-integrating-open-source.html)**
* **[Iceberg REST Catalog](https://iceberg.apache.org/rest-catalog-spec/)** (including R2 Data Catalog and Tabular)

# Setting up with AWS Glue Catalog

<Note>
  **How this works**

  * The **Glue catalog** stores Iceberg table metadata and the pointer to each table's location.
  * The **destination S3 bucket** stores your Iceberg data, metadata files, and is used during staging.
</Note>

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

  3. Click the **JSON** tab, and paste the following policy, being sure to replace `BUCKET_NAME`, `ACCOUNT_ID`, and `SCHEMA` with your specific values.

     <Note>
       **Why are these permissions necessary?**

       * The listed **Glue permissions** are needed to manage catalog metadata and handle table operations, including cleaning up temporary tables during syncs.
       * The listed **S3 permissions** are needed to upload data files, list bucket contents, read Iceberg metadata, and manage files during compaction.
       * Note: The `glue:CreateDatabase` permission is required if the database does not yet exist. If you wish to use an existing Glue database, you can remove this action and provide us with the name of your pre-existing database.
     </Note>

     ```json
     {
         "Version": "2012-10-17",
         "Statement": [
             {
                 "Sid": "AllowGlueAccessToDestinationDatabaseAndTables",
                 "Effect": "Allow",
                 "Action": [
                     "glue:GetDatabases",
                     "glue:GetDatabase",
                     "glue:GetTables",
                     "glue:GetTable",
                     "glue:GetPartitions",
                     "glue:CreateTable",
                     "glue:CreateDatabase",
                     "glue:UpdateTable",
                     "glue:DeleteTable"
                 ],
                 "Resource": [
                     "arn:aws:glue:*:ACCOUNT_ID:catalog",
                     "arn:aws:glue:*:ACCOUNT_ID:database/SCHEMA",
                     "arn:aws:glue:*:ACCOUNT_ID:database/default",
                     "arn:aws:glue:*:ACCOUNT_ID:table/SCHEMA/*"
                 ]
             },
             {
                 "Sid": "AllowS3AccessToBucket",
                 "Effect": "Allow",
                 "Action": [
                     "s3:PutObject",
                     "s3:ListBucket",
                     "s3:GetBucketLocation",
                     "s3:GetObject",
                     "s3:DeleteObject"
                 ],
                 "Resource": [
                     "arn:aws:s3:::BUCKET_NAME",
                     "arn:aws:s3:::BUCKET_NAME/*"
                 ]
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

  ### Add your destination

  Use the following details to complete the connection setup: **bucket name**, **bucket region**, **role ARN**, and **Glue database name**.

  * Instructions for [Analyze / Optimize for Webflow sites](https://help.webflow.com/hc/en-us/articles/49268499539603)
  * Instructions for [Optimize for non-Webflow sites](https://help-optimize.webflow.com/hc/en-us/articles/49271128719507)
</Steps>

# Setting up with AWS S3 Tables Catalog

<Note>
  **How this works**

  * The **S3 Tables bucket** stores your Iceberg data and metadata.
  * A separate **staging S3 bucket** is required for staging data.
</Note>

## Prerequisites

* S3 Tables authentication uses role-based access. You will need the trust policy prepopulated with Webflow's identifier to grant access.
* The IAM role must also have a trust relationship with itself to function correctly with the S3 Tables API. Your final trust policy should include two principals: our service and the role itself. Be sure to replace `YOUR_ACCOUNT_ID` and `YOUR_ROLE_NAME` with the appropriate identifiers.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": { "AWS": "arn:aws:iam::YOUR_ACCOUNT_ID:role/YOUR_ROLE_NAME" },
      "Action": "sts:AssumeRole"
    },
    {
      "Effect": "Allow",
      "Action": ["sts:AssumeRoleWithWebIdentity"],
      "Principal": { "Federated": "accounts.google.com" },
      "Condition": {
        "StringEquals": {
          "accounts.google.com:oaud": "<some_oaud_identifier>",
          "accounts.google.com:sub": "108000002380243782158"
        }
      }
    }
  ]
}
```

## Configuration steps

<Steps>
  ### Set up S3 Tables bucket

  1. Navigate to the **S3** service page.
  2. In the left navigation, click **Table buckets**.
  3. Click **Create bucket**.
  4. Enter a **Bucket name** and choose the same **AWS Region** you plan to use for your destination S3 bucket. This bucket will be used as your **S3 Tables bucket**.
  5. Click **Create bucket**.

  ### Set up staging S3 bucket

  1. Navigate to the **S3** service page.
  2. Click **Create bucket**.
  3. Enter a **Bucket name** and modify any of the default settings as desired. Note: **Object Ownership** can be set to "ACLs disabled" and **Block Public Access settings for this bucket** can be set to "Block all public access" as recommended by AWS. Make note of the **Bucket name** and **AWS Region**.
  4. Click **Create bucket**.

  ### Create policy and IAM role

  **Create policy**

  1. Navigate to the **IAM** service page.

  2. Navigate to the **Policies** navigation tab, and click **Create policy**.

  3. Click the **JSON** tab, and paste the following policy, replacing `ACCOUNT_ID`, `REGION`, `S3_TABLES_BUCKET_NAME`, and `S3_STAGING_BUCKET_NAME` with the appropriate values.

     <Note>
       **Why are these permissions necessary?**

       * The listed **S3 Table data permissions** are needed to read/write Iceberg data files and manage metadata locations in your S3 Tables bucket.
       * The listed **S3 Table management permissions** are needed to create/manage tables and namespaces (including cleaning up temporary tables during syncs) in your S3 Tables bucket.
       * The listed **S3 permissions** are needed to write data files to your staging S3 bucket, list bucket contents, and clean up staged or test files.
       * The permissions to create and manage namespaces (`s3tables:CreateNamespace`, etc.) are required if the namespace does not already exist. If you wish to use an existing namespace, you can remove these actions.
     </Note>

     ```json
     {
         "Version": "2012-10-17",
         "Statement": [
             {
                 "Sid": "AllowS3TableDataActions",
                 "Effect": "Allow",
                 "Action": [
                     "s3tables:GetTable",
                     "s3tables:DeleteTable",
                     "s3tables:GetTableData",
                     "s3tables:PutTableData",
                     "s3tables:GetTableMetadataLocation",
                     "s3tables:UpdateTableMetadataLocation"
                 ],
                 "Resource": "arn:aws:s3tables:REGION:ACCOUNT_ID:bucket/S3_TABLES_BUCKET_NAME/table/*"
             },
             {
                 "Sid": "AllowS3TableManagementAndNamespaceActions",
                 "Effect": "Allow",
                 "Action": [
                     "s3tables:GetTableBucket",
                     "s3tables:CreateTable",
                     "s3tables:ListTables",
                     "s3tables:CreateNamespace",
                     "s3tables:GetNamespace",
                     "s3tables:ListNamespaces",
                     "s3tables:DeleteNamespace"
                 ],
                 "Resource": "arn:aws:s3tables:REGION:ACCOUNT_ID:bucket/S3_TABLES_BUCKET_NAME"
             },
             {
                 "Sid": "AllowS3AccessToDestinationBucket",
                 "Effect": "Allow",
                 "Action": [
                     "s3:PutObject",
                     "s3:ListBucket",
                     "s3:GetBucketLocation",
                     "s3:GetObject",
                     "s3:DeleteObject"
                 ],
                 "Resource": [
                     "arn:aws:s3:::S3_STAGING_BUCKET_NAME",
                     "arn:aws:s3:::S3_STAGING_BUCKET_NAME/*"
                 ]
             }
         ]
     }
     ```

  4. Click **Next: Tags**, click **Next: Review**.

  5. Name the policy, and click **Create policy**.

  **Create role**

  1. Navigate to the **IAM** service page.
  2. Navigate to the **Roles** navigation tab, and click **Create role**.
  3. Select **Custom trust policy**. Leave the default placeholder trust policy as-is for now (do not paste the final trust policy yet), and click **Next**. The policy must be self-assuming, which is not allowed until the role is created, so it must be updated after the role is created.
  4. Add the permissions policy created above, and click **Next**.
  5. Enter a **Role name** and click **Create role**.
  6. Once successfully created, search for the created role in the Roles list and click the role name.
  7. In the role detail view, navigate to the **Trust relationships** tab, click **Edit trust policy**, and replace the default trust policy with the trust policy JSON in the **Prerequisites** section above. Click **Update policy** to save.

     <Note>
       **AWS IAM propagation delay**

       After updating the trust policy, AWS IAM changes can take **5-10 minutes or longer** to propagate. Please wait for the propagation to complete before testing the connection.
     </Note>

  ### Add your destination

  Use the following details to complete the connection setup: **S3 Tables bucket ARN**, **destination S3 bucket name**, **destination S3 bucket region**, **role ARN**, and chosen **namespace**.

  * Instructions for [Analyze / Optimize for Webflow sites](https://help.webflow.com/hc/en-us/articles/49268499539603)
  * Instructions for [Optimize for non-Webflow sites](https://help-optimize.webflow.com/hc/en-us/articles/49271128719507)
</Steps>

# Setting up with Iceberg REST Catalog

The Iceberg REST catalog is an open standard for interacting with an Iceberg catalog over HTTP. Below are instructions for two popular implementations.

<Note>
  **Note on credentials**

  We connect to REST catalogs as a standard client using the credentials you provide. We do not support credential vendoring (issuing temporary credentials) for downstream access.
</Note>

## R2 Data Catalog (Cloudflare)

<Info>
  **Zero egress fees**

  Cloudflare R2 charges no egress fees, making it a cost-effective option if you plan to query your Iceberg data from external locations or other cloud providers.
</Info>

<Steps>
  ### Create R2 bucket and API token

  1. Log in to your Cloudflare dashboard.
  2. Follow the [Cloudflare documentation to create an R2 bucket](https://developers.cloudflare.com/r2/buckets/create-buckets/). Make a note of the **Bucket Name** and your **R2 Account ID**.
  3. Follow the [Cloudflare documentation to create an R2 API token](https://developers.cloudflare.com/r2/api/tokens/) with **Admin Read & Write** permissions. Make a note of the generated **Access Key ID** and **Secret Access Key**.

  ### Add your destination

  Use the following details to complete the connection setup:

  * **Catalog URI**: `https://api.cloudflare.com/client/v4/accounts/YOUR_R2_ACCOUNT_ID/r2/catalog`
  * **API Token** (as the credential)
  * **Bucket Name** and **Region**
  * **R2 Access Key ID** and **R2 Secret Access Key**

  <Note>
    **R2 catalog path requirement**

    If you customize the folder or path used for the R2 Data Catalog, it must start with `__r2_data_catalog`. The R2 API does not validate this upfront, so an incorrect prefix will result in runtime failures when creating or querying tables.
  </Note>

  * Instructions for [Analyze / Optimize for Webflow sites](https://help.webflow.com/hc/en-us/articles/49268499539603)
  * Instructions for [Optimize for non-Webflow sites](https://help-optimize.webflow.com/hc/en-us/articles/49271128719507)
</Steps>

## Tabular

<Steps>
  ### Create a Tabular credential

  1. Log in to your Tabular organization's dashboard.
  2. Navigate to the credentials section and create a new credential with permissions to create tables and write data.
  3. Make a note of the generated **Client ID** and **Client Secret**.

  ### Add your destination

  Use the following details to complete the connection setup:

  * **Catalog URI**: `https://api.tabular.io/ws`

  * **Client ID**

  * **Client Secret**

  * Instructions for [Analyze / Optimize for Webflow sites](https://help.webflow.com/hc/en-us/articles/49268499539603)

  * Instructions for [Optimize for non-Webflow sites](https://help-optimize.webflow.com/hc/en-us/articles/49271128719507)
</Steps>

# Understanding Iceberg configuration options

<Warning>
  Changing these attributes on an existing destination table will not take effect until you perform a full refresh of the table.
</Warning>

## Managing staged data

**Purpose:**
During each transfer, batches are first written to a staging prefix in your object storage bucket before they are committed into the final Iceberg table. This prefix is always named `_write_ahead_staging` (for example: `your_folder/_write_ahead_staging/<table_name>/<transfer_id>` or `_write_ahead_staging/<table_name>/<transfer_id>` if no folder/schema is configured).

**Recommendation:**
We recommend configuring an object storage lifecycle policy to automatically delete objects under the `_write_ahead_staging` prefix after **30 days**. This provides a safety net for any orphaned staged files that are not cleaned up due to failed or interrupted runs.

## retention\_window\_days

**Purpose:**
Sets the number of days for which historical data (e.g., previous table snapshots used for time travel or auditing) is retained.

**Recommendation:**
Set this value according to your organization's internal data retention policies.

## FAQs

<Accordion title="How is data transferred into my Iceberg tables?">
  We first stage batch files into an object storage bucket, then use your chosen catalog to atomically commit them into the final Iceberg table. For Glue and REST catalogs, the same S3 bucket is used for both staging and permanent table data, with different prefixes. For S3 Tables, batches are staged into your **staging S3 bucket**, then the finalized Iceberg data and metadata is written to the managed **S3 Tables bucket**.
</Accordion>

<Accordion title="Should I use AWS Glue or AWS S3 Tables?">
  There are tradeoffs to consider when choosing between Glue and S3 Tables:

  * **Glue Catalog**: Glue stores the table metadata, and your S3 bucket stores both staged files and the final Iceberg data under different prefixes. We run snapshot expiry and compaction and you control the S3 layout. This is a good fit if you already use Glue as your central catalog or want to keep data in a single S3 bucket you manage directly.

  * **S3 Tables Catalog**: The S3 Tables bucket is a fully managed table bucket where AWS stores the finalized Iceberg data and metadata. We write batches to a separate **staging S3 bucket**, and the catalog writes the final data into the S3 Tables bucket and handles maintenance on your behalf. This is a good fit if you prefer automatic maintenance and plan to query through engines that natively support S3 Tables.
</Accordion>

<Accordion title="What is Apache Iceberg and why should I use it?">
  Apache Iceberg is an open table format designed for analytic datasets on object stores. It delivers warehouse-native capabilities such as ACID transactions, time travel, and schema evolution with the simplicity, scalability, and secure permissions model of an object storage bucket. By using a central catalog, Iceberg provides reliable transactions and enables multiple engines to work concurrently on the same data. This enables your warehouse to be isolated from data sharing, so you can receive data without exposing your internal resources.
</Accordion>

<Accordion title="Why do you need permissions to delete data?">
  Iceberg performs background maintenance operations to manage the table's health and performance. These include expiring old snapshots and compacting small data files. The writer must have delete permissions to safely remove obsolete files without compromising data integrity.
</Accordion>

<Accordion title="Can I send the data to a specific prefix in a bucket?">
  Yes, you can direct data to a specific prefix (warehouse path). However, we recommend using a completely isolated bucket to receive data. This minimizes security risks and reduces the chance of accidental interference with other datasets.
</Accordion>

<Accordion title="Do I need to perform maintenance operations on the Iceberg table?">
  No, the data writer is responsible for expiring snapshots and compacting data as needed. Data consumers should not run any non-read queries on the table, except managed catalogs like R2 and S3 Tables, which automatically run compaction and snapshot expiration.

  <Error>
    You should treat the destination tables as read-only. Executing write or delete operations manually may corrupt the table state and break data synchronization.
  </Error>
</Accordion>

<Accordion title="How do I know when a table has been updated?">
  You can query the table's metadata to see the history of snapshots. Each snapshot represents a version of the table. For example, in Spark SQL, you can run:

  ```sql
  SELECT snapshot_id, committed_at FROM my_glue_catalog.my_db.my_table.snapshots ORDER BY committed_at DESC LIMIT 1;
  ```

  This command returns the most recent snapshot details. Additionally, most bucket providers offer the capability to trigger a webhook or lambda when objects are created, which can be configured to monitor the table's metadata directory for new manifest lists.

  <Note>
    We write a `version-hint.txt` file to the metadata directory. This allows tools like PyIceberg and DuckDB to read the table directly from S3 without needing to connect to the catalog service, by pointing them to the table's root location.
  </Note>
</Accordion>

<Accordion title="Are there any limitations on data sizes?">
  We do not enforce size limits, including JSON fields. Downstream query engines may have their own limits (e.g., Amazon Redshift's `SUPER` and `VARCHAR` sizes). Ensure your data fits within your query engine's constraints to avoid query failures.
</Accordion>

<Accordion title="Can I mount my Iceberg data to BigQuery?">
  Coming soon! Contact us if you'd like to be notified when this feature is available.
</Accordion>

# Mounting/Reading an Iceberg table

You can mount/read an Iceberg table into your data warehouse of choice. Below are the supported catalog types and links to the corresponding vendor documentation:

* **ClickHouse**
  * [Glue catalog](https://clickhouse.com/docs/use-cases/data-lake/glue-catalog)
  * [S3 Tables catalog](https://clickhouse.com/docs/engines/table-engines/integrations/iceberg)
  * [REST catalog](https://clickhouse.com/docs/use-cases/data-lake/rest-catalog)
* **DuckDB / MotherDuck**
  * [Glue catalog](https://duckdb.org/docs/stable/core_extensions/iceberg/amazon_sagemaker_lakehouse)
  * [S3 Tables catalog](https://duckdb.org/2025/03/14/preview-amazon-s3-tables)
  * [REST catalog](https://duckdb.org/docs/stable/core_extensions/iceberg/iceberg_rest_catalogs)
* **Spark**
  * [Glue catalog](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-format-iceberg.html#aws-glue-programming-etl-format-iceberg-read-spark)
  * [S3 Tables catalog](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-integrating-open-source.html)
  * [REST catalog](https://iceberg.apache.org/docs/latest/spark-configuration/#rest-catalog)
* **Athena / Redshift**
  * [Glue catalog](https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg.html)
  * [S3 Tables catalog](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-integrating-open-source.html)
* **Snowflake**
  * [REST catalog](https://docs.snowflake.com/en/user-guide/tables-iceberg-externally-managed-writes)
