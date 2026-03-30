# Source: https://docs.startree.ai/corecapabilities/ingestdata/recipes/iam-role-s3.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# IAM-Role Based Access for S3

This document guides you through setting up an **AWS IAM role** that allows your StarTree Cloud environment to securely access data stored in your Amazon S3 buckets. This is crucial for enabling StarTree to ingest data directly from S3.

## Setting Up Your AWS IAM Role for S3 Access

Before you begin creating the role, please collect the following vital pieces of information:

* **StarTree Account ID** and **External ID**: You can find this when you initiate the process of creating an S3 connection within the StarTree Data Portal.
* **StarTree Environment Name**: This is visible in your StarTree Cloud Portal.

### Step 1: Verify AWS STS Configuration

To ensure cross-account access works correctly, the AWS Security Token Service (STS) must be active in the region where your S3 bucket is located.

1. Open the [AWS IAM console](https://console.aws.amazon.com/iam) and click on **Account settings** in the left navigation pane.
2. Locate the **Security Token Service (STS)** section. Make sure its status is **Active** for the AWS region where your S3 bucket resides. If it's not, please activate it.

### Step 2: Create the IAM Role

Now, let's create the IAM role that StarTree will assume to access your S3 bucket.

1. In the AWS IAM console, navigate to **Roles** and then click the **Create role** button.
2. Under **Trusted entity type**, select **AWS account**.
   * **If StarTree and S3 are in the same AWS account**: Select **This Account**.
   * **If StarTree and S3 are in different AWS accounts**:
     * From the StarTree Data Portal, copy the **StarTree AWS Account ID** and paste it into the **Another AWS Account** field.
     * Next, copy the **External ID** from the StarTree Data Portal and paste it into the **External ID** field.
3. **Attach Permissions**: Search for and select the IAM policy you've already created that grants access to your S3 bucket (e.g., `s3-my-bucket-policy` as used in our example). Click **Next**.
4. **Name Your Role**:
   * If your **External ID** has the `env-*` prefix (which is common for newer environments), you can skip this step, and the role will be named automatically based on the External ID.
   * Otherwise, provide a clear **Role name** (e.g., `startree-my-stream-role`) and consider adding descriptive **Tags** (key-value pairs) for organization.
5. Finally, click **Create role**.

### Step 3: Provide the Role ARN to StarTree

After the role is successfully created:

1. Go to the role's Summary page in the AWS IAM console.
2. Copy the **Role ARN** (Amazon Resource Name).
3. Paste this ARN into the **IAM Role ARN** field within the StarTree Data Portal when setting up your S3 connection. This tells StarTree which role to assume for accessing your S3 data. [More documentation here](/corecapabilities/ingestdata/dataportal/batch/s3).

Built with [Mintlify](https://mintlify.com).
