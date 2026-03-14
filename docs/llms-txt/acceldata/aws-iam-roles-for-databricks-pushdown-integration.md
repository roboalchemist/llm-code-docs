# Source: https://docs.acceldata.io/documentation/aws-iam-roles-for-databricks-pushdown-integration.md

# AWS IAM Roles for Databricks Pushdown Integration

To enable **Good/Bad record publishing** for Databricks data sources using the **Pushdown engine**, your Databricks workspace must have access to the external storage location (such as an **S3 bucket**) where the records will be written.

This guide explains how to create and configure the necessary **IAM roles** and **S3 permissions** for AWS-based Databricks workspaces.

## Prerequisites

Before starting, ensure that:

- You have an **AWS account** with permissions to create **S3 buckets** and **IAM roles**.
- You know the **AWS account ID** associated with your Databricks workspace.
- The Databricks workspace has **Unity Catalog enabled** (for managing external locations and credentials).

## Step 1. Create an S3 Bucket for Good/Bad Records

1. Log in to the **AWS Management Console**.
2. Go to **S3** -&gt; **Create bucket**.
3. Enter a name for your bucket such as `databricks-good-bad-data.`
4. Ensure the **region** matches the one where your **Databricks cluster** runs.
5. Click **Create bucket**.

This bucket will store the _Good_ and _Bad_ data records generated during Data Quality policy execution.

## Step 2. Create an IAM Role for S3 Bucket Access

1. In the **AWS Console**, go to **IAM** -&gt; **Roles** -&gt; **Create role**.
2. Choose **Custom trust policy** and paste the following JSON in the Custom Trust Policy editor:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": [
          "arn:aws:iam::414351767826:role/unity-catalog-prod-UCMasterRole-14S5ZJVKOTYTL"
        ]
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": {
          "sts:ExternalId": "0000"
        }
      }
    }
  ]
}
```



3. Click **Next**, skip the **Permissions Policy** section for now, and **create the role**.
4. Enter a meaningful name, for example: `databricks-unity-catalog-good-bad-role`.

## Step 3. Grant S3 Permissions to the IAM Role

1. Open the newly created IAM role.
2. Go to **Permissions** tab.
3. Paste the following JSON policy, replacing placeholders as needed:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": [
        "s3:GetObject",
        "s3:PutObject",
        "s3:DeleteObject",
        "s3:ListBucket",
        "s3:GetBucketLocation",
        "s3:GetLifecycleConfiguration",
        "s3:PutLifecycleConfiguration"
      ],
      "Resource": [
        "arn:aws:s3:::<DATABRICKS-GOOD-BAD-BUCKET-NAME>/*",
        "arn:aws:s3:::<DATABRICKS-GOOD-BAD-BUCKET-NAME>"
      ],
      "Effect": "Allow"
    },
    {
      "Action": "sts:AssumeRole",
      "Resource": "arn:aws:iam::<YOUR-AWS-ACCOUNT-ID>:role/<UNITY-CATALOG-IAM-ROLE-NAME>",
      "Effect": "Allow"
    }
  ]
}
```



4. Save the policy and verify it appears under role’s permissions.

## Step 4. Create Storage Credentials in Databricks

In the Databricks SQL editor or Notebook, create **storage credentials** linked to the IAM role.

### Option A — Using SQL Editor

```sql
CREATE STORAGE CREDENTIAL <UNIQUE-CREDENTIAL-NAME>
WITH STORAGE ROLE 'AwsIamRole:arn:aws:iam::<YOUR-AWS-ACCOUNT-ID>:role/<UNITY-CATALOG-IAM-ROLE-NAME>';
```



If this fails with the following syntax error, use the Databricks **Notebook** approach:

```none
[PARSE_SYNTAX_ERROR] Syntax error at or near 'STORAGE'. SQLSTATE: 42601
```



### Option B — Using Databricks Notebook (Python)

```none
from databricks.sdk import WorkspaceClient
from databricks.sdk.service.catalog import AwsIamRole

w = WorkspaceClient()
w.storage_credentials.create(
    name="<UNIQUE-CREDENTIAL-NAME>",
    aws_iam_role=AwsIamRole(
        role_arn="arn:aws:iam::<YOUR-AWS-ACCOUNT-ID>:role/<UNITY-CATALOG-IAM-ROLE-NAME>"
    )
)
```



After successful creation, copy the **External ID** displayed in the “Storage Credential Created” dialog.

You will use this External ID in the next step to update the IAM trust policy.

## Step 5. Create an External Location in Databricks

Once the storage credential is created, register your S3 bucket as an **External Location**.

Run the following SQL in Databricks:

```sql
CREATE EXTERNAL LOCATION <UNIQUE-LOCATION-NAME>
URL 's3://<DATABRICKS-GOOD-BAD-BUCKET-NAME>/exports/warehouse/'
WITH (STORAGE CREDENTIAL <UNIQUE-CREDENTIAL-NAME>);
```



If your data source uses a **Personal Access Token (PAT)**, grant the necessary privileges:

```sql
GRANT READ FILES, WRITE FILES
ON EXTERNAL LOCATION <UNIQUE-LOCATION-NAME>
TO `<DATABRICKS-USER>`;
```



## Step 6. Update the IAM Trust Relationship Policy

Back in AWS, edit the **trust relationship** for your IAM role to include the **Databricks storage credential’s external ID** and allow self-assumption.

1. Go to **IAM** -&gt; **Roles** -&gt; **&lt; UNITY-CATALOG-IAM-ROLE-NAME&gt;** -&gt; **Trust Relationships -&gt;** **Edit**.
2. Replace the trust policy with the following JSON:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::414351767826:role/unity-catalog-prod-UCMasterRole-14S5ZJVKOTYTL"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": {
          "sts:ExternalId": "<STORAGE-CREDENTIAL-EXTERNAL-ID>"
        }
      }
    },
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::<YOUR-AWS-ACCOUNT-ID>:root"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": {
          "AWS:PrincipalArn": "arn:aws:iam::<YOUR-AWS-ACCOUNT-ID>:role/<UNITY-CATALOG-IAM-ROLE-NAME>",
          "sts:ExternalId": "<STORAGE-CREDENTIAL-EXTERNAL-ID>"
        }
      }
    }
  ]
}
```



Alternative (Optional)
If you prefer a simpler version, the following trust relationship will also work:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": [
          "arn:aws:iam::414351767826:role/unity-catalog-prod-UCMasterRole-14S5ZJVKOTYTL",
          "arn:aws:iam::<YOUR-AWS-ACCOUNT-ID>:role/<THIS-ROLE-NAME>"
        ]
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": {
          "sts:ExternalId": "<STORAGE-CREDENTIAL-EXTERNAL-ID>"
        }
      }
    }
  ]
}
```



Save the trust policy.

## Step 7: Validate the Configuration

Use Databricks SQL to test the setup by running a simple write and read operations on your external storage (S3).

```sql
-- Write to S3
INSERT OVERWRITE DIRECTORY 's3://<DATABRICKS-GOOD-BAD-BUCKET-NAME>/exports/warehouse/test_write/'
USING PARQUET
SELECT * FROM <DATABASE>.<TABLE> LIMIT 10;

-- Read back
SELECT * FROM PARQUET.`s3://<DATABRICKS-GOOD-BAD-BUCKET-NAME>/exports/warehouse/test_write/` LIMIT 10;
```



If both queries execute successfully, your IAM role and external storage configuration are complete.

## Notes and Limitations

- Only **Parquet** format is supported for Good/Bad record export.
- Ensure the IAM role and bucket are created in the **same AWS region** as your Databricks workspace.
- ADOC does not manage lifecycle or retention of exported data.
- External storage must remain accessible to Databricks clusters.

## Next Step

Return to  [Databricks Integration for Data Reliability](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/databricks-integration-for-data-reliability) and complete the configuration to publish **Good/Bad Records Using Pushdown Engine.**