# Source: https://docs.unstructured.io/ui/destinations/delta-table.md

# Source: https://docs.unstructured.io/open-source/ingestion/source-connectors/delta-table.md

# Source: https://docs.unstructured.io/open-source/ingestion/destination-connectors/delta-table.md

# Source: https://docs.unstructured.io/api-reference/workflow/destinations/delta-table.md

# Source: https://docs.unstructured.io/ui/destinations/delta-table.md

# Source: https://docs.unstructured.io/open-source/ingestion/source-connectors/delta-table.md

# Source: https://docs.unstructured.io/open-source/ingestion/destination-connectors/delta-table.md

# Source: https://docs.unstructured.io/api-reference/workflow/destinations/delta-table.md

# Source: https://docs.unstructured.io/ui/destinations/delta-table.md

# Source: https://docs.unstructured.io/open-source/ingestion/source-connectors/delta-table.md

# Source: https://docs.unstructured.io/open-source/ingestion/destination-connectors/delta-table.md

# Source: https://docs.unstructured.io/api-reference/workflow/destinations/delta-table.md

# Delta Tables in Amazon S3

<Tip>
  This article covers connecting Unstructured to Delta Tables in Amazon S3. For information about
  connecting Unstructured to Delta Tables in Databricks instead, see
  [Delta Tables in Databricks](/api-reference/workflow/destinations/databricks-delta-table).
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

Send processed data from Unstructured to a Delta Table, stored in Amazon S3.

The requirements are as follows.

The following video shows how to fulfill the minimum set of Amazon S3 requirements to store Delta Tables:

<iframe width="560" height="315" src="https://www.youtube.com/embed/_W4565dcUGI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

<Warning>
  If you are experiencing S3 connector or workflow failures after adding a new S3 bucket or updating an existing S3 bucket,
  it could be due to S3 latency issues. You might need to wait up to a few hours before any related S3 connectors
  and workflows begin working without failures.

  Various Amazon S3 operations such as propagating DNS records for new buckets, updating bucket access policies and
  permissions, reusing bucket names after deletion, and using AWS Regions that are not geographically closer
  to your users or applications, can take a few minutes to hours to fully propagate across the Amazon network.
</Warning>

The preceding video does not show how to create an AWS account.

For more information about requirements, see the following:

* An AWS account. [Create an AWS account](https://aws.amazon.com/free).

  <iframe width="560" height="315" src="https://www.youtube.com/embed/lIdh92JmWtg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

* An S3 bucket. You can create an S3 bucket by using the S3 console, following the steps [in the S3 documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html) or in the following video.
  Additional approaches that use AWS CloudFormation or the AWS CLI are in the how-to sections later on this page.

  <iframe width="560" height="315" src="https://www.youtube.com/embed/e6w9LwZJFIA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

* For authenticated bucket write access or both, you should first
  [block all public access to the bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/configuring-block-public-access-bucket.html).

  After blocking all public access to the bucket, for read access, the authenticated AWS IAM user must have at minimum the permissions of `s3:ListBucket` and `s3:GetObject` for that bucket.
  For write access, the authenticated AWS IAM user must have at minimum the permission of `s3:PutObject` for that bucket. To grant permissions,
  attach the appropriate bucket policy to the bucket. See the policy examples later on this page, and [learn about bucket policies for S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-policy-language-overview.html). These permissions remain in effect until the bucket policy is removed from the bucket.
  To apply a bucket policy by using the S3 console, follow the steps [in the S3 documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/add-bucket-policy.html) or in the following video.
  Additional approaches that use AWS CloudFormation or the AWS CLI are in the how-to sections later on this page.

  <iframe width="560" height="315" src="https://www.youtube.com/embed/y4SfQoJpipo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

* Provide an AWS access key and secret access key for the authenticated AWS IAM user in the account.
  Create an AWS access key and secret access key by following the steps [in the IAM documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_CreateAccessKey) or in the following video.

  <iframe width="560" height="315" src="https://www.youtube.com/embed/MoFTaGJE65Q" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

* If the target files are in the root of the bucket, provide the path to the bucket, formatted as `protocol://bucket/` (for example, `s3://my-bucket/`).
  If the target files are in a folder, the path to the target folder in the S3 bucket, formatted as `protocol://bucket/path/to/folder/` (for example, `s3://my-bucket/my-folder/`).

* If the target files are in a folder, make sure the authenticated AWS IAM user has
  authenticated access to the folder as well. [See examples of authenticated folder access](https://docs.aws.amazon.com/AmazonS3/latest/userguide/example-bucket-policies.html#example-bucket-policies-folders).

## Add an access policy to an existing bucket

To use the Amazon S3 console to add an access policy that allows all authenticated AWS IAM users in the
corresponding AWS account to read and write to an existing S3 bucket, do the following.

<Info>Your organization might have stricter bucket policy requirements. Check with your AWS account
administrator if you are unsure.</Info>

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/).

2. Open the [Amazon S3 Console](https://console.aws.amazon.com/s3/home).

3. Browse to the existing bucket and open it.

4. Click the **Permissions** tab.

5. In the **Bucket policy** area, click **Edit**.

6. In the **Policy** text area, copy the following JSON-formatted policy.
   To change the following policy to restrict it to a specific user in the AWS account, change `root` to that
   specific username.

   In this policy, replace the following:

   * Replace `<my-account-id>` with your AWS account ID.
   * Replace `<my-bucket-name>` in two places with the name of your bucket.

   ```json  theme={null}
   {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Sid": "AllowAuthenticatedUsersInAccountReadWrite",
               "Effect": "Allow",
               "Principal": {
                   "AWS": "arn:aws:iam::<my-account-id>:root"
               },
               "Action": [
                   "s3:GetObject",
                   "s3:PutObject",
                   "s3:ListBucket",
                   "s3:DeleteObject"
               ],
               "Resource": [
                   "arn:aws:s3:::<my-bucket-name>",
                   "arn:aws:s3:::<my-bucket-name>/*"
               ],
               "Condition": {
                   "StringEquals": {
                       "aws:PrincipalType": "IAMUser"
                   }
               }
           }
       ]
   }
   ```

7. Click **Save changes**.

## Create a bucket with AWS CloudFormation

To use the AWS CloudFormation console to create an Amazon S3 bucket that allows all authenticated AWS IAM users
in the corresponding AWS account to read and write to the bucket, do the following.

<Info>Your organization might have stricter bucket policy requirements. Check with your AWS account
administrator if you are unsure.</Info>

1. Save the following YAML to a file on your local machine, for example `create-s3-bucket.yaml`. To change
   the following bucket policy to restrict it to a specific user in the AWS account, change `root` to that
   specific username.

   ```yaml  theme={null}
   AWSTemplateFormatVersion: '2010-09-09'
   Description: 'CloudFormation template to create an S3 bucket with specific permissions for account users.'

   Parameters:
     BucketName:
       Type: String
       Description: 'Name of the S3 bucket to create'

   Resources:
     MyS3Bucket:
       Type: 'AWS::S3::Bucket'
       Properties:
         BucketName: !Ref BucketName
         PublicAccessBlockConfiguration:
           BlockPublicAcls: true
           BlockPublicPolicy: false
           IgnorePublicAcls: true
           RestrictPublicBuckets: true

     BucketPolicy:
       Type: 'AWS::S3::BucketPolicy'
       Properties:
         Bucket: !Ref MyS3Bucket
         PolicyDocument:
           Version: '2012-10-17'
           Statement:
             - Sid: AllowAllAuthenticatedUsersInAccount
               Effect: Allow
               Principal:
                 AWS: !Sub 'arn:aws:iam::${AWS::AccountId}:root'
               Action:
                 - 's3:GetObject'
                 - 's3:PutObject'
                 - 's3:ListBucket'
                 - 's3:DeleteObject'
               Resource:
                 - !Sub 'arn:aws:s3:::${BucketName}'
                 - !Sub 'arn:aws:s3:::${BucketName}/*'

   Outputs:
     BucketName:
       Description: 'Name of the created S3 bucket'
       Value: !Ref MyS3Bucket
   ```

2. Sign in to the [AWS Management Console](https://console.aws.amazon.com/).

3. Open the [AWS CloudFormation Console](https://console.aws.amazon.com/cloudformation/home).

4. Click **Create stack > With new resources (standard)**.

5. On the **Create stack** page, with **Choose an existing template** already selected, select **Upload a template file**.

6. Click **Choose file**, and browse to and select the YAML file from your local machine.

7. Click **Next**.

8. Enter a unique **Stack name** and **BucketName**.

9. Click **Next** two times.

10. Click **Submit**.

11. Wait until the **Status** changes to **CREATE\_COMPLETE**.

12. After the bucket is created, you can delete the YAML file, if you want.

## Create a bucket with the AWS CLI

To use the AWS CLI to create an Amazon S3 bucket that allows all authenticated AWS IAM users in the
corresponding AWS account to read and write to the bucket, do the following.

<Info>Your organization might have stricter bucket policy requirements. Check with your AWS account
administrator if you are unsure.</Info>

1. [Install the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).

2. [Set up the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-quickstart.html).

3. Copy the following script to a file on your local machine, for example a file named `create-s3-bucket.sh`.
   To change the following bucket policy to restrict it to a specific user in the AWS account, change `root` to that
   specific username.

   In this script, replace the following:

   * Replace `<my-account-id>` with your AWS account ID.
   * Replace `<my-unique-bucket-name>` with the name of your bucket.
   * Replace `<us-east-1>` with your AWS Region.

   ```bash  theme={null}
   #!/bin/bash

   # Set variables for the AWS account ID, Amazon S3 bucket name, and AWS Region.
   ACCOUNT_ID="<my-account-id>"
   BUCKET_NAME="<my-unique-bucket-name>"
   REGION="<us-east-1>"

   # Temporary filename for the bucket policy.
   # Do not change this variable.
   POLICY_FILE="bucket_policy.json"

   # Create the bucket.
   aws s3api create-bucket --bucket $BUCKET_NAME --region $REGION

   # Wait for the bucket to exist.
   echo "Waiting for bucket '$BUCKET_NAME' to be fully created..."
   aws s3api wait bucket-exists --bucket $BUCKET_NAME

   # Check if the wait command was successful.
   if [ $? -eq 0 ]; then
       echo "The bucket '$BUCKET_NAME' has been fully created."
   else
       echo "Error: Timed out waiting for bucket '$BUCKET_NAME' to be created."
       exit 1
   fi

   # Remove the "block public policy" bucket access setting.
   aws s3api put-public-access-block \
       --bucket $BUCKET_NAME \
       --public-access-block-configuration \
       '{"BlockPublicPolicy": false, "IgnorePublicAcls": false, "BlockPublicAcls": false, "RestrictPublicBuckets": false}'

   # Check if the operation was successful.
   if [ $? -eq 0 ]; then
       echo "The block public policy access setting was removed from '$BUCKET_NAME'."
   else
       echo "Error: Failed to remove the block public policy access setting from '$BUCKET_NAME'."
       exit 1
   fi

   # Create the bucket policy.
   cat << EOF > $POLICY_FILE
   {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Sid": "AllowAuthenticatedUsersInAccountReadWrite",
               "Effect": "Allow",
               "Principal": {
                   "AWS": "arn:aws:iam::$ACCOUNT_ID:root"
               },
               "Action": [
                   "s3:GetObject",
                   "s3:PutObject",
                   "s3:ListBucket",
                   "s3:DeleteObject"
               ],
               "Resource": [
                   "arn:aws:s3:::$BUCKET_NAME",
                   "arn:aws:s3:::$BUCKET_NAME/*"
               ],
               "Condition": {
                   "StringEquals": {
                       "aws:PrincipalType": "IAMUser"
                   }
               }
           }
       ]
   }
   EOF

   # Apply the bucket policy.
   aws s3api put-bucket-policy --bucket $BUCKET_NAME --policy file://$POLICY_FILE

   # Check if the policy application was successful.
   if [ $? -eq 0 ]; then
       echo "The bucket policy was applied to '$BUCKET_NAME'."
   else
       echo "Error: Failed to apply the bucket policy to '$BUCKET_NAME'."
       exit 1
   fi

   # Verify the applied policy.
   echo "Verifying the applied policy:"
   aws s3api get-bucket-policy --bucket $BUCKET_NAME --query Policy --output text

   # Remove the temporary bucket policy file.
   rm $POLICY_FILE
   ```

4. Run the script, for example:

   ```bash  theme={null}
   sh create-s3-bucket.sh
   ```

5. After the bucket is created, you can delete the script file, if you want.

## Delta table output format

A Delta table consists of Parquet files that contain data and a transaction log that stores metadata about the transactions.
[Learn more](https://delta-io.github.io/delta-rs/how-delta-lake-works/architecture-of-delta-table/).

The Delta Tables in Amazon S3 destination connector generates the following output within the specified path to the S3 bucket (or the specified folder within the bucket):

* Initially, one Parquet (`.parquet`) file per file in the source location. For example, for a file in the source location named `my-file.pdf`, an associated
  file with the extension `.parquet` is generated. Various kinds of file transactions can result in additional Parquet files being generated. These Parquet filenames are automatically generated by the Delta Lake engine and are not meant to be manually modified.
* A folder named `_delta_log` that contains metadata and change history about the `.parquet` files. As Parquet files are added to, changed, or removed from
  the specified bucket or folder path, the `_delta_log` folder is updated with any related metadata and change history details.

Together, this set of Parquet files and their associated `_delta_log` folder (and its contents) describe a single, versioned Delta table. Because of this, Unstructured recommends the following usage best practices:

* In the source location, each set of source files that is to be considered as a unit for change management purposes should be controlled by a unique, dedicated
  Delta Tables in S3 destination connector. This connector should reference a unique, dedicated output folder within the bucket. Having
  multiple workflows refer to different sets of source files, yet all share the same Delta table, could results in data loss or table corruption.
* Avoid directly modifying, adding, or deleting Parquet data files or the `_delta_log` folder within a Delta table's directory. This can lead to data loss or table corruption.
* If you need to copy or move a Delta table to a different location,
  you must move or copy its entire set of Parquet files and its associated `_delta_log` folder (and its contents) together as a unit.
  Note that the copied or moved Delta table will
  no longer be controlled by the original Delta Tables in S3 destination connector.

## Create the destination connector

To create a Delta Tables in Amazon S3 destination connector, see the following examples.

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
                  type="delta_table",
                  config={
                      "aws_region": "<aws-region>",
                      "table_uri": "<table-uri>",
                      "aws_access_key_id": "<aws-access-key-id>",
                      "aws_secret_access_key": "<aws-secret-access-key>"
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
      "type": "delta_table",
      "name": "<name>",
      "config": {
          "aws_region": "<aws-region>",
          "table_uri": "<table-uri>",
          "aws_access_key_id": "<aws-access-key-id>",
          "aws_secret_access_key": "<aws-secret-access-key>"
      }
  }'
  ```
</CodeGroup>

Replace the preceding placeholders as follows:

* `<name>` (*required*) - A unique name for this connector.
* `<aws-region>` (*required*) - The AWS Region identifier (for example, `us-east-1`) for the Amazon S3 bucket you want to store the Delta Table in.
* `<table-uri>` (*required*) - The URI of the Amazon S3 bucket you want to store the Delta Table in. This typically takes the format `s3://my-bucket/my-folder`.
* `<aws-access-key-id>` (*required*) - The AWS access key ID for the AWS IAM principal (such as an IAM user) that has the appropriate access to the S3 bucket.
* `<aws-secret-access-key>` (*required*) - The AWS secret access key for the corresponding AWS access key ID.
