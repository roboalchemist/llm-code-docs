# Source: https://docs.datafold.com/integrations/databases/amazon-s3.md

# Amazon S3

**Steps to complete:**

1. [Create a user with access to S3](/integrations/databases/google-cloud-storage#create-a-service-account)
2. [Assign the user to the S3 bucket](/integrations/databases/google-cloud-storage#service-account-access-and-permissions)
3. [Create an access key for the user](/integrations/databases/google-cloud-storage#generate-a-service-account-key)
4. [Configure your data connection in Datafold](/integrations/databases/google-cloud-storage#configure-in-datafold)

## Create a user with access to S3

To connect your Amazon S3 bucket, you will need to create a user for Datafold to use.

* Navigate to the [AWS Console](https://console.aws.amazon.com/).
* Click on the search bar in the top header, then find **IAM** service and click on it.
* Click on the **Users** item of the Access Management section.
* Click on the **Create user** button.
* Create a user named `Datafold`.
* Assign the user to the `AmazonS3FullAccess` policy.
* When done, keep ARN of the user handy as you'll need it in the next step.

## Assign the user to the S3 bucket

* Go to S3 panel and select the bucket.
* Click on the **Permissions** tab.
* Click on **Edit** next to the **Bucket Policy**.
* Add the following policy:
  ```json  theme={null}
  {
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Allow",
        "Principal": {
          "AWS": "arn:aws:iam:::user/Datafold" // Replace with your user's ARN
        },
        "Action": [
          "s3:GetObject",
          "s3:PutObject" // Optional: Only needed if you're planning to use this data connection as a destination for materialized diff results.
        ],
        "Resource": [
          "arn:aws:s3:::your-bucket-name/*", // Replace with your bucket's ARN
          "arn:aws:s3:::your-bucket-name" // Replace with your bucket's ARN
        ]
      }
    ]
  }
  ```

<Note>
  The Datafold user requires the following roles and permissions:

  * **s3:GetObject** for read access.
  * **s3:PutObject** for write access if you're planning to use this data connection as a destination for materialized diff results.
</Note>

## Create an access key for the user

Next, go back to the **IAM** page to generate a key for Datafold.

* Click on the **Users** page.
* Click on the **Datafold** user.
* Click on the **Security Credentials** tab.
* Click on **Create access key** and select **Create new access key**.
* Select **JSON** and click **Create**.

## Configure in Datafold

| Field Name                                                | Description                                                                                                                           |
| --------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| Connection name                                           | A name given to the data connection within Datafold                                                                                   |
| Bucket Name                                               | The name of the bucket you want to connect to.                                                                                        |
| Bucket region                                             | The region of the bucket you want to connect to.                                                                                      |
| Key ID                                                    | The key file generated in the [Create an access key for the user](#create-an-access-key-for-the-user) step                            |
| Secret Access Key                                         | The secret access key generated in the [Create an access key for the user](#create-an-access-key-for-the-user) step                   |
| Directory for writing diff results                        | Optional. The directory in the bucket where diff results will be written. Service account should have write access to this directory. |
| Default maximum number of rows to include in diff results | Optional. The maximum number of rows that a file with materialized results will contain.                                              |

Click **Create**. Your data connection is ready!
