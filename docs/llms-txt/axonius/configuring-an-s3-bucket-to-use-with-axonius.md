# Source: https://docs.axonius.com/docs/configuring-an-s3-bucket-to-use-with-axonius.md

# Configuring an S3 Bucket to use with Axonius

To save files on AWS S3 buckets you must first create an S3 bucket. This section outlines the basic steps to configure an AWS S3 bucket to be used by the Axonius system for the purposes of backups, data synchronization and EC action support. This is not intended to be an exhaustive process for configuring the bucket or for setting security controls on the bucket. Refer to [AWS Buckets overview](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingBucket.html#access-bucket-intro.) for more extensive information.

## Creating a Bucket in S3

1. Login to the AWS Console.

   <Image alt="console Logon.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/console%20Logon(1).png" />

2. Open the AWS Management Console and go to the S3 service.

   <Image align="center" alt="S3-2-.png" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/S3-2-(1).png" />

3. Click **Create Bucket**.

   <Image align="center" alt="CreateBucket.png" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CreateBucket.png" />

4. Supply a name for the bucket. Note that S3 bucket names must be unique across AWS.

5. Select the appropriate AWS Region.

   <Image alt="BucketNAme.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/BucketNAme(1).png" />

6. Configure the appropriate settings in the Bucket Creation page.

   <Image align="center" alt="Bucket2.png" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Bucket2(1).png" />

7. Click **Create Bucket** to complete the bucket creation process.

8. Gather the S3 bucket ARN:
   a.  Locate the bucket you just created in the S3 Bucket Listing page.
   b. Click  the bucket.
   c. Click the **Properties** tab.
   d.  Copy the S3 bucket Amazon resource name (ARN) for use later in this process.

   <Image align="center" alt="ARN\(4\)" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ARN(4).png" />

9. Continue the setup in the IAM section.

## Setting the IAM Policy for the S3 Bucket

There are two flows in this process. The flow to use will be determined by the presence or absence of an existing Axonius IAM policy. If no IAM policy exists in AWS to support Axonius, follow the instructions in 'No Existing IAM Policy.' In most cases, an IAM policy will already exist to support the system's operation. If this is the case, follow the instructions in 'IAM Policy Exists'.

### No Existing IAM Policy

* At the top of the AWS S3 Administration page, type IAM (or choose IAM from the Services dropdown menu) to go to the IAM administration page.
* Click on the link for Policies on the left side of the window.
* Click **Create policy** at the top of the page to create a dedicated Axonius Adapter policy.
* On the **Create Policy** page, do the following:
  a.   Click the **JSON** tab.
  b. Copy and paste the policy presented below into the window that opens.

```json
{
  "Version": "2012-10-17",
 "Statement": [
    {
     "Action": [
        "s3:GetObject",
        "s3:ListBucket",
        "s3:PutObject",
        "s3:PutObjectTagging",
        "s3:DeleteObject"
    ],
     "Effect": "Allow",
     "Resource": "["Enter_S3_Bucket_ARN_Here", "Enter_S3_Bucket_ARN_Here/*"]",
     "Sid": "AxoniusS3BucketAccess"
   }
 ]
}
```

c. In the policy, locate the "Resource" element.\
d. Replace `["Enter_S3_Bucket_ARN_Here", "Enter_S3_Bucket_ARN_Here/*"]` with the S3 bucket ARN you captured in the S3 section above.\
e. Click the "Next: Tags" button to continue.\
f. Add tags, if needed.\
g. Click the "Next: Review" button to continue.\
h. Give the policy a name.\
i. Click the "Create policy" button.

### IAM Policy Exists

1. If you have an existing Axonius Adapter policy, locate it and click  it to open the Policy Summary page.
2. Click **{} JSON** to display the existing policy as JSON.
3. Click **Edit policy**.
4. Add a new section to the policy as follows:

```json
    {
      "Action": [
        "s3:GetObject",
        "s3:ListBucket",
        "s3:PutObject",
        "s3:PutObjectTagging",
        "s3:DeleteObject"
      ],
      "Effect": "Allow",
      "Resource": "["Enter_S3_Bucket_ARN_Here", "Enter_S3_Bucket_ARN_Here/*"]",
      "Sid": "AxoniusS3BucketAccess"
    },
}
```

5. In the policy, locate the "Resource" element.
6. Replace `["Enter_S3_Bucket_ARN_Here", "Enter_S3_Bucket_ARN_Here/*"]` with the S3 bucket ARN you captured above in the S3 section.
7. Click **Review policy**.
8. Click **Save changes**.

## IAM User/Role

Similar to the IAM Policy section, there are two flows in this process. If Axonius is already running in AWS, then use the "IAM User/Role Exists" flow. If Axonius isn't running in AWS, complete [IAM User/Role Does Not Exist](/docs/amazon-web-services-aws#iam-userrole-does-not-exist).

### IAM User/Role Does Not Exist

Refer to the [Axonius documentation](/docs/connecting-aws-adapter-using-iam-user) to configure the user/role.

### IAM User/Role Exists

#### **IAM User**

1. Login to the AWS Console, if you are not already logged in.

2. Open the AWS Management Console and go to the IAM service.

   <Image align="center" alt="IAMService.png" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/IAMService(2).png" />

3. While you are still in the IAM administration page, click on the **Users** link on the left side of the window.

4. Locate the Axonius user and click it.

5. Click **Add permissions**.

6. Click **Attach existing policies directly**.

7. Locate the IAM policy that you created or updated above.

8. Click the radio button to the left of the policy name to select it.

9. Click **Next: Review** to continue.

10. Click **Add permissions** to continue.

#### **IAM Role**

1. While you are still in the IAM administration page, click on the **Roles** link on the left side of the window.
2. Locate the Axonius role and click on it.
3. Click **Attach policies**.
4. Locate the IAM policy that you created or updated above.
5. Click the radio button to the left of the policy name to select it.
6. Click **Attach policy** to continue.