# Source: https://developers.webflow.com/browser/data-exports/destinations/redshift.mdx

***

title: Amazon Redshift
slug: data-exports/destinations/redshift
description: Configure Amazon Redshift as a destination for Data Exports
------------------------------------------------------------------------

This guide walks you through configuring Amazon Redshift as a destination for your Webflow Analyze and Optimize data export.

## Prerequisites

* If your Redshift security posture requires IP allowlisting, have the Webflow static IP: `34.69.83.207/32` available during the following steps. It will be required in Step 2.
* By default, Redshift authentication uses role-based access. You will need the trust policy prepopulated with Webflow's identifier to grant access.

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

<Note>
  **Network allowlisting**

  Webflow Static IP: `34.69.83.207/32`
</Note>

## Configuration steps

<Steps>
  ### Create a Limited User in Redshift

  1. Connect to Redshift using the SQL client.

  2. Execute the following query to create a user to write the data (replace `<password>` with a password of your choice).

     ```sql
     CREATE USER <username> PASSWORD '<password>';
     ```

     <Note>
       **Creating a user without a password.**

       Role-based authentication does not require a password. You may create the user using `CREATE USER <username> PASSWORD DISABLE;`.
     </Note>

  3. Grant user `create` and `temporary` privileges on the database. `create` allows the service to create new schemas and `temporary` allows the service to create temporary tables.

     ```sql
     GRANT CREATE, TEMPORARY ON DATABASE <database> TO <username>;
     ```

     <Note>
       **The schema will be created during the first sync**

       The schema name supplied as part of Step 4 will be created during the first connection. It does not need to be created manually in the destination ahead of time.
     </Note>

     <Warning>
       **If the `schema` already exists**

       By default, the service creates a new schema based on the destination configuration. If you prefer to create the schema yourself before connecting the destination, you must ensure that the writer user has the proper permissions on the schema, using `GRANT ALL ON schema <schema> TO <username>;`

       Once you've provided the `GRANT ALL` permission on the schema, you can safely remove the `CREATE` permission on the database (but you must retain the `TEMPORARY` permission on the database).
     </Warning>

  ### Allowlist connection

  1. In the Redshift console, click **Clusters**, and make a note of the **cluster** name.

  2. Select the cluster you would like to connect.

  3. In the **General information** pane, make note of the **Endpoint** details. You may need to use the **copy** icon to copy the full details to discover the full endpoint and port number.

     ![](https://storage.googleapis.com/prequel_docs/images/redshift-endpoint-details.png "redshift endpoint details.png")

  4. Click the **Properties** tab.

  5. Scroll down to the **Network and security settings** section.

  6. In the VPC security group field, select a security group to open it.

     ![](https://storage.googleapis.com/prequel_docs/images/redshift-vpc-security-groups.png "redshift vpc s groups.png")

  7. In the Security Groups window, click **Inbound rules**.

  8. Click **Edit inbound rules**.

  9. In the Edit the Inbound rules window, follow the steps below to create custom TCP rules for the static IP:
     a. Select **Custom TCP** in the drop-down menu.
     b. Enter your Redshift port number. (likely `5439`)
     c. Enter the **static IP**.
     d. Click **Add rule**.

     <Note>
       **Public accessibility and subnet requirements**

       For IP allowlisting from outside your VPC, the Redshift cluster must be set to **Publicly accessible** and deployed in a **public subnet** with a route to an Internet Gateway. For private Redshift clusters, SSH tunneling is supported. Contact support for instruction on configuring an SSH tunnel for your Redshift cluster.
     </Note>

  ### Create a staging bucket

  **Create staging bucket**

  1. Navigate to the S3 service page.
  2. Click Create bucket.
  3. Enter a **Bucket name** and modify any of the default settings as desired. Note: **Object Ownership** can be set to "**ACLs disabled**" and **Block Public Access settings for this bucket** can be set to "**Block all public access**" as recommended by AWS. Make note of the Bucket name and AWS Region.
  4. Click **Create bucket**.

  **Create policy**

  1. Navigate to the **IAM** service page, click on the **Policies** navigation tab, and click **Create policy**.

  2. Click the JSON tab, and paste the following policy, being sure to replace `BUCKET_NAME`  with the name of the bucket chosen above, and REGION\_NAME, ACCOUNT\_ID, CLUSTER\_NAME, USERNAME, and DATABASE\_NAME with the proper Redshift values.

     **Note**: the first bucket permission in the list applies to `BUCKET_NAME` whereas the second permission applies only to the bucket's contents — `BUCKET_NAME/*` — an important distinction.

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

     <Warning>
       **Credential character limitations**

       For user credentials containing special characters, please avoid using the following characters: `@`, `[`, `]`, `/`, `?`, `#`, `"`, `\\`, `+`, space, `&`, `:` as these characters can break connection string parsing.
     </Warning>

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

       Role-based authentication is the preferred authentication mode for Redshift based on AWS recommendations. However, HMAC Access Key ID & Secret Access Key is an alternative authentication method that can be used if preferred.

       1. Navigate to the **IAM** service page.
       2. Navigate to the **Users** navigation tab, and click **Add users**.
       3. Enter a **User name** for the service, for example, `transfer-service`, click **Next**. Under **Select AWS access type**, select the **Access key - Programmatic access** option. Click **Next: Permissions**.
       4. Click the **Attach existing policies directly** option, and search for the name of the policy created in the previous step. Select the policy, and click **Next: Tags**.
       5. Click **Next: Review** and click **Create user**.
       6. In the **Success** screen, record the **Access key ID** and the **Secret access key**.
     </Warning>

  ### Add your destination

  Use the following details to complete the connection setup: **username**, **host**, **database**, **cluster**, your chosen **schema**, **IAM role ARN**, and **staging bucket details**.

  * Instructions for [Analyze / Optimize for Webflow sites](https://help.webflow.com/hc/en-us/articles/49268191745171)
  * Instructions for [Optimize for non-Webflow sites](https://help-optimize.webflow.com/hc/en-us/articles/49270864953235)
</Steps>

## Permissions checklist

* Redshift database user exists and has `CREATE` and `TEMPORARY` on the database. If you pre-created the schema, ensure `GRANT ALL ON SCHEMA <schema> TO <username>`.
* IAM role trust policy allows the data transfer service to assume the role.
* IAM policy includes:
  * `redshift:GetClusterCredentials` on your target cluster (db user and db name resources).
  * S3 `ListBucket` on `arn:aws:s3:::BUCKET_NAME`.
  * S3 `GetObject`, `PutObject`, `DeleteObject` on `arn:aws:s3:::BUCKET_NAME/*`.
* Network allowlisting (if enforced) permits egress IP/CIDR for the Redshift port (typically `5439`).

## FAQs

<Accordion title="How is the Redshift connection secured?">
  We use role-based authentication with your AWS IAM Role. The data transfer service assumes your role to obtain short-lived database credentials and network access can be constrained by allowlisting the static egress IPs noted above.
</Accordion>

<Accordion title="Why is an S3 bucket required?">
  Redshift's high-throughput path loads data from S3 using `COPY`. We stage files briefly in your bucket to maximize throughput and reliability. Files are cleaned up after load.
</Accordion>

<Accordion title="What are the oaud vs sub IDs used for?">
  These are identity claims used in the IAM trust policy when federating from GCP to AWS. `sub` uniquely identifies our Google principal in federation. `oaud` is an additional claim used to bind role assumption to your organization.
</Accordion>

<Accordion title="Why am I getting authentication errors with Redshift?">
  Common causes:

  * Missing or incorrect permission on `redshift:GetClusterCredentials` (ensure it targets the correct cluster ARN and region/account).
  * Trust policy mismatch (the data transfer service's principal isn't permitted to assume your role).
  * Using a Serverless workgroup permission or `redshift-serverless:GetCredentials` instead of provisioned cluster + `redshift:GetClusterCredentials`.
  * Propagation delay: IAM changes can take a few minutes to apply. Retry after 5-10 minutes.
</Accordion>

<Accordion title="Do I need to pre-create the schema?">
  No. The schema provided in the destination configuration is created automatically on first sync. If you pre-create it, grant `ALL` on the schema to the writer user and you may remove the database-level `CREATE` permission (retain `TEMPORARY`).
</Accordion>
