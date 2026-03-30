# Source: https://docs.logrocket.com/docs/aws-athena-prerequisites.md

# AWS Athena Prerequisites

Configuring your AWS Athena destination.

## Prerequisites

* [ ] By default, Athena authentication uses role-based access. You will need the following trust policy to grant access to the data-syncing service:

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
          "accounts.google.com:sub": "109570679157784085515"
        }
      }
    }
  ]
}
```

## Step 1: Create a destination bucket, service policy, and user

### Create Athena target bucket

Follow these steps to create a bucket to be used for staging data before transferring to a destination.

1. Navigate to the **S3** service page.
2. Click **Create bucket**.
3. Enter a **Bucket name**, select an **AWS Region**, and modify any of the default settings as desired. Note: **Object Ownership** can be set to "**ACLs disabled**" and **Block Public Access settings for this bucket** can be set to "**Block all public access**" as recommended by AWS. Make note of the Bucket name and AWS Region.
4. Click **Create bucket**.

### Create Athena access policy

1. Navigate to the **IAM** service page, click on the **Policies** navigation tab, and click **Create policy**.
2. Click the JSON tab, and paste the following policy, being sure to replace `BUCKET` and `SCHEMA` with the name of the buckets and database/schema/folder where Athena should write the data. `BUCKET` should refer to the bucket created in the previous step. Note: the `SCHEMA` used below does not need to be created ahead of time. If it does not exist, it will be created automatically before transferring data.

```json JSON policy
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowAthenaAccess",
            "Effect": "Allow",
            "Action": "athena:*",
            "Resource": "*"
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
                "arn:aws:glue:*:239674069128:catalog",
                "arn:aws:glue:*:239674069128:database/SCHEMA",
                "arn:aws:glue:*:239674069128:database/default",
                "arn:aws:glue:*:239674069128:table/SCHEMA/*"
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
                "arn:aws:s3:::BUCKET",
                "arn:aws:s3:::BUCKET/*"
            ]
        }
    ]
}
```

> Athena vs. S3 permissions
>
> Because Athena uses S3 as the underlying storage layer, the Resource access requested in the policy is scoped down via resource-specific permissions in the S3 actions.
>
> Schema vs. Database
>
> During destination onboarding, you will be asked to provide both a "schema" and a "database". Though those are mostly synonymous in Athena, they are used for two different purposes here:
>
> * `schema` should be the name of the folder in S3 under which the final data will be written.
> * `database` should be the name of the folder in S3 in which the Athena query results are written (i.e., the automatically generated `athena_output/` data).

3. Click through to the **Review** step, choose a **name** for the policy, for example, `transfer-service-policy` (this will be referenced in the next step), add a description, and click **Create policy**.

### Create role

1. Navigate to the **IAM** service page.
2. Navigate to the **Roles** navigation tab, and click **Create role**.
3. Select **Custom trust policy** and paste the provided trust policy (from the prerequisite) to allow AssumeRole access to this role. Click **Next**.
4. Add the permissions policy created above, and click **Next**.
5. Enter a **Role name**, for example, `transfer-role`, and click **Create role**.
6. Once successfully created, search for the created role in the Roles list, click the role name, and make a note of the **ARN** value.

## Step 2: Gather the required setup information

1. For the data export setup you will need:
   * **database** and **schema**
   * **workgroup**
   * **bucket name**
   * **bucket region**
   * **IAM Role ARN**

Visit the [LogRocket Streaming Data Export settings page](https://app.logrocket.com/r/settings/streaming-data-export) to complete the setup.