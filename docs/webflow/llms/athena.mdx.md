# Source: https://developers.webflow.com/browser/data-exports/destinations/athena.mdx

***

title: Amazon Athena
slug: data-exports/destinations/athena
description: Configure Amazon Athena as a destination for Data Exports
----------------------------------------------------------------------

This guide walks you through configuring Amazon Athena as a destination for your Webflow Analyze and Optimize data export.

## Prerequisites

* By default, Athena authentication uses role-based access. You will need the trust policy prepopulated with Webflow's identifier to grant access.

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
  ### Create a destination bucket, service policy, and role

  **Create Athena target bucket**

  Follow these steps to create a bucket to be used for staging data before transferring to a destination.

  1. Navigate to the **S3** service page.
  2. Click **Create bucket**.
  3. Enter a **Bucket name**, select an **AWS Region**, and modify any of the default settings as desired. Note: **Object Ownership** can be set to "**ACLs disabled**" and **Block Public Access settings for this bucket** can be set to "**Block all public access**" as recommended by AWS. Make note of the Bucket name and AWS Region.
  4. Click **Create bucket**.

  **Create Athena access policy**

  1. Navigate to the **IAM** service page, click on the **Policies** navigation tab, and click **Create policy**.

  2. Click the JSON tab, and paste the following policy, being sure to replace `ACCOUNT_ID`, `WORKGROUP`, `BUCKET_NAME` and `SCHEMA` with the your account information.

     * `WORKGROUP` should be `primary` unless otherwise specified during connection configuration.
     * `BUCKET` should refer to the bucket created in the previous step.
     * `SCHEMA` used below does not need to be created ahead of time. If it does not exist, it will be created automatically before transferring data.

     ```json
     {
         "Version": "2012-10-17",
         "Statement": [
             {
                 "Sid": "AllowAthenaAccess",
                 "Effect": "Allow",
                 "Action": [
                     "athena:GetQueryResults",
                     "athena:StartQueryExecution",
                     "athena:StopQueryExecution",
                     "athena:StartSession",
                     "athena:GetDatabase",
                     "athena:GetDataCatalog",
                     "athena:GetWorkGroup",
                     "athena:GetTableMetadata",
                     "athena:GetQueryExecution"
                 ],
                 "Resource": [
                     "arn:aws:athena:*:ACCOUNT_ID:workgroup/WORKGROUP"
                 ]
             },
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

     <Note>
       **Athena vs. S3 permissions**

       Because Athena uses S3 as the underlying storage layer, the Resource access requested in the policy is scoped down via resource-specific permissions in the S3 actions.
     </Note>

  3. Click through to the **Review** step, choose a **name** for the policy, for example, `transfer-service-policy` (this will be referenced in the next step), add a description, and click **Create policy**.

  **Create role**

  1. Navigate to the **IAM** service page.
  2. Navigate to the **Roles** navigation tab, and click **Create role**.
  3. Select **Custom trust policy** and paste the provided trust policy (from the prerequisite) to allow AssumeRole access to this role. Click **Next**.
  4. Add the permissions policy created above, and click **Next**.
  5. Enter a **Role name**, for example, `transfer-role`, and click **Create role**.
  6. Once successfully created, search for the created role in the Roles list, click the role name, and make a note of the **ARN** value.

     <Warning>
       **Alternative authentication method: AWS User with HMAC Access Key ID & Secret Access Key**

       Role-based authentication is the preferred authentication mode for Athena based on AWS recommendations. However, HMAC Access Key ID & Secret Access Key is an alternative authentication method that can be used if preferred.

       1. Navigate to the **IAM** service page.
       2. Navigate to the **Users** navigation tab, and click **Add users**.
       3. Enter a **User name** for the service, for example, `transfer-service`, click **Next**. Under **Select AWS access type**, select the **Access key - Programmatic access** option. Click **Next: Permissions**.
       4. Click the **Attach existing policies directly** option, and search for the name of the policy created in the previous step. Select the policy, and click **Next: Tags**.
       5. Click **Next: Review** and click **Create user**.
       6. In the **Success** screen, record the **Access key ID** and the **Secret access key**.
     </Warning>

  ### Add your destination

  Use the following details to complete the connection setup: **database**, **schema**, **workgroup**, **bucket name**, **bucket region**, and **IAM Role ARN**.

  * Instructions for [Analyze / Optimize for Webflow sites](https://help.webflow.com/hc/en-us/articles/49362201385235)
  * Instructions for [Optimize for non-Webflow sites](https://help-optimize.webflow.com/hc/en-us/articles/49362246174227)

  ### Data management

  Follow these guidelines to manage your new Athena tables effectively:

  **Optimize Iceberg queries**

  To optimize the performance of your Iceberg tables, use the `OPTIMIZE` command. This command reorganizes the data in a way that improves query efficiency. Execute the following query periodically:

  ```sql
  OPTIMIZE iceberg_table REWRITE DATA;
  ```

  **Set vacuum properties**

  Iceberg tables can accumulate snapshots over time, which can affect performance. To manage this, set the maximum age for snapshots that the vacuum process should retain:

  ```sql
  ALTER TABLE iceberg_table SET TBLPROPERTIES (
    'vacuum_max_snapshot_age_seconds'='259200');
  ```

  The default setting is `432000` seconds, we recommend only updating this if you notice degrading performance.

  **Perform time travel queries**

  Iceberg supports accessing historical data snapshots using time travel queries. This feature allows you to query the table as it appeared at a previous point in time, which is useful for audits and rollbacks:

  ```sql
  SELECT * FROM iceberg_table FOR TIMESTAMP AS OF timestamp;
  ```

  Replace `timestamp` with the specific UNIX timestamp of the snapshot you wish to query.
</Steps>
