# Source: https://docs.logrocket.com/docs/s3-prerequisites.md

# S3 Prerequisites

Configuring your AWS S3 destination.

## Prerequisites

* [ ] By default, S3 authentication uses role-based access. You will need the following trust policy to grant access to the data-syncing service:

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

## Step 1: Set up destination S3 bucket

### Create bucket

1. Navigate to the **S3** service page.
2. Click **Create bucket**.
3. Enter a **Bucket name** and modify any of the default settings as desired. Note: **Object Ownership** can be set to "ACLs disabled" and **Block Public Access settings for this bucket** can be set to "Block all public access" as recommended by AWS. Make note of the **Bucket name** and **AWS Region**.
4. Click **Create bucket**.

## Step 2: Create policy and IAM user

### Create policy

1. Navigate to the **IAM** service page.
2. Navigate to the **Policies** navigation tab, and click **Create policy**.
3. Click the **JSON** tab, and paste the following policy, being sure to replace `BUCKET_NAME` with the name of the bucket chosen in Step 1.

```json JSON policy
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:PutObject", "s3:DeleteObject"],
            "Resource": "arn:aws:s3:::BUCKET_NAME/*"
        }
    ]
}
```

> 📘
>
> By default, a connection test is performed against the destination during initial configuration and s3:DeleteObject is required to clean up test artifacts. Once the test has been performed successfully and the destination added, this action can be safely removed, as S3 destinations are append-only by default.

4. Click **Next: Tags**, click **Next: Review**.
5. Name the policy, add a description, and click **Create policy**.

### Create role

1. Navigate to the **IAM** service page.
2. Navigate to the **Roles** navigation tab, and click **Create role**.
3. Select **Custom trust policy** and paste the provided trust policy to allow AssumeRole access to the new role. Click **Next**.
4. Add the permissions policy created above, and click **Next**.
5. Enter a **Role name**, for example, `transfer-role`, and click **Create role**.
6. Once successfully created, search for the created role in the Roles list, click the role name, and make a note of the **ARN** value.

## Step 3: Gather the required setup information

For the data export setup, you will need:

* **S3 Bucket Name** and **Region**
* **role ARN**

Visit the [LogRocket Streaming Data Export settings page](https://app.logrocket.com/r/settings/streaming-data-export) to complete the setup.