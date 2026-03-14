# Source: https://docs.logrocket.com/docs/redshift-prerequisites.md

# Redshift Prerequisites

Configuring your Redshift destination.

## Prerequisites

* [ ] If your Redshift security posture requires IP whitelisting, have our data syncing service's static IP (`34.171.168.215/32`) available during the following steps. It will be required in Step 2.
* [ ] By default, Redshift authentication uses role-based access. You will need the following trust policy to grant access to the data-syncing service:

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

## Step 1: Create a Limited User in Redshift

1. Connect to Redshift using the SQL client.
2. Execute the following query to create a user to write the data (replace `<password>` with a password of your choice).

```sql
CREATE USER <username> PASSWORD '<password>';
```

> 📘 Creating a user without a password
>
> Role based auth does not require a password. You may create the user using `CREATE USER <username> PASSWORD DISABLE;`.

3. Grant user `create` and `temporary` privileges on the database. `create` allows the service to create new schemas and `temporary` allows the service to create temporary tables.

```sql
GRANT CREATE, TEMPORARY ON DATABASE <database> TO <username>;
```

> 📘 The schema will be created during the first sync
>
> The schema name supplied as part of Step 4 will be created during the first connection. It does not need to be created manually in the destination ahead of time.

## Step 2: Whitelist connection

1. In the Redshift console, click **Clusters**.
2. Select the cluster you would like to connect.
3. In the **General information** pane, make note of the **Endpoint** details. You may need to use the **copy** icon to copy the full details to discover the full endpoint and port number.

![](https://storage.googleapis.com/prequel_docs/images/redshift-endpoint-details.png "redshift endpoint details.png")

4. Click the **Properties** tab.
5. Scroll down to the **Network and security settings** section.
6. In the VPC security group field, select a security group to open it.

![](https://storage.googleapis.com/prequel_docs/images/redshift-vpc-security-groups.png "redshift vpc s groups.png")

7. In the Security Groups window, click **Inbound rules**.
8. Click **Edit inbound rules**.
9. In the Edit the Inbound rules window, follow the steps below to create custom TCP rules for the static IP:\
   a. Select **Custom TCP** in the drop-down menu.\
   b. Enter your Redshift port number. (likely `5439`)\
   c. Enter the **static IP**: `34.171.168.215/32`.\
   d. Click **Add rule**.

## Step 3: Create a staging bucket

### Create staging bucket

1. Navigate to the S3 service page.
2. Click Create bucket.
3. Enter a **Bucket name** and modify any of the default settings as desired. Note: **Object Ownership** can be set to "**ACLs disabled**" and **Block Public Access settings for this bucket** can be set to "**Block all public access**" as recommended by AWS. Make note of the Bucket name and AWS Region.
4. Click **Create bucket**.

### Create policy

5. Navigate to the **IAM** service page, click on the **Policies** navigation tab, and click **Create policy**.
6. Click the JSON tab, and paste the following policy, being sure to replace `BUCKET_NAME`  with the name of the bucket chosen above, and REGION\_NAME, ACCOUNT\_ID, CLUSTER\_NAME, USERNAME, and DATABASE\_NAME with the proper Redshift values.
   1. **Note**: the first bucket permission in the list applies to BUCKET\_NAME whereas the second permission applies only to the bucket's contents — BUCKET\_NAME/\* — an important distinction.

```json JSON policy
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
                "s3:PutObject",
                "s3:GetObject",
              	"s3:DeleteObject"
            ],
            "Resource": "arn:aws:s3:::BUCKET_NAME/*"
        },
        {
            "Effect": "Allow",
            "Action": "redshift:GetClusterCredentials",
            "Resource": [
                "arn:aws:redshift:REGION_NAME:ACCOUNT_ID:dbuser:CLUSTER_NAME/USERNAME",
                "arn:aws:redshift:REGION_NAME:ACCOUNT_ID:dbname:CLUSTER_NAME/DATABASE_NAME"
            ]
        }
    ]
}
```

5. Click through to the **Review** step, choose a **name** for the policy, for example, `transfer-service-policy` (this will be referenced in the next step), add a description, and click **Create policy**.

### Create role

1. Navigate to the **IAM** service page.
2. Navigate to the **Roles** navigation tab, and click **Create role**.
3. Select **Custom trust policy** and paste the provided trust policy (from the prerequisite) to allow AssumeRole access to this role. Click **Next**.
4. Add the permissions policy created above, and click **Next**.
5. Enter a **Role name**, for example, `transfer-role`, and click **Create role**.
6. Once successfully created, search for the created role in the Roles list, click the role name, and make a note of the **ARN** value.

## Step 4: Gather the required setup information

For the data export setup, you will need:

* **host name**
* **database name**
* **schema**
* **IAM role ARN**
* **staging bucket details**

Visit the [LogRocket Streaming Data Export settings page](https://app.logrocket.com/r/settings/streaming-data-export) to complete the setup.