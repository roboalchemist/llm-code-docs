# Source: https://docs.acceldata.io/documentation/cross---account-access-setup.md

# Cross‑Account Access Setup

This page explains how ADOC enables access to cloud storage and secret managers across different cloud accounts. In multi-account setups, common in enterprise environments, you often need the Data Plane (in one account) to access buckets or secrets in another account. ADOC fully supports this for both AWS and GCP, ensuring secure and scalable access.

**Cross‑Account Access** ties into your Data Plane configuration by allowing Data Plane pipelines and resources to fetch data or credentials from external cloud accounts while maintaining least-privilege access and auditability.

## AWS S3 Cross-Account Access

If your S3 data resides in a separate AWS account from the one hosting your Data Plane:

**In the S3-owner account (Account B)**

- Create a bucket policy to allow the Data Plane account (Account A) to:
- List the bucket contents (grant `s3:ListBucket)`
- Retrieve objects from the bucket (grant `s3:GetObject)`

**In the Data Plane account (Account A)**

- Assign a policy to the Data Plane’s IAM user or role to allow the same actions (list and retrieve) for the S3 bucket in Account B
- Register the S3 bucket in ADOC using credentials from Account A

Once setup, ADOC will seamlessly access the S3 bucket in Account B

## AWS Secrets Manager Cross-Account Access

If your credentials are stored in AWS Secrets Manager in a different AWS account, here’s what to do:

- In the Secrets Manager account (Account B)
- Add a resource policy to the secret, allowing the Data Plane’s IAM role or user in Account A to retrieve the secret (grant `secretsmanager:GetSecretValue)`
- Ensure the secret is encrypted with a customer-managed KMS key, and update the key’s policy to allow access from Account A.
- In the Data Plane account (Account A):
- Reference the Amazon Resource Name (ARN) in the Data Plane’s **`secretmanager.json`** configuration file.

ADOC will automatically retrieve the secret from Account B during operation.

## GCP Cross-Project Access (Buckets & Secret Manager)

If your data or secrets are in a different GCP project from the Data Plane project, follow the steps

- For buckets (e.g. GCS):
- In the project containing the bucket, grant the Data Plane’s  service account(from the other project) permissions to:
- Retrieve objects (grant `storage.objects.get)`,
- Get bucket details (grant `storage.buckets.get),` and
- List bucket contents (grant `storage.buckets.?list)`.
- For GCP Secret Manager
- Grant your Data Plane service account (often &lt;UserFlyteGSA&gt;) the Secret Manager Secret Accessor role in the project containing the secrets.

Once configured, the Data Plane can access GCS buckets or secrets in the other project directly.

## Configure the Data Plane Secret Manager

To enable cross-account access, update the Data Plane’s configuration:

| Step | Action | 
| ---- | ---- | 
| 1 | Edit secretmanager.json. Specify the secret manager type (AWS or GCP) in /opt/acceldata/secretmanager.json. | 
| 2 | Set up cross-account access. Follow the AWS or GCP steps above to configure permissions. | 
| 3 | Encode the configuration. Convert secretmanager.json (and gcp_cred.json if using GCP) to Base64 and update the Kubernetes secret (secret-manager and optionally gcp-cred). | 
| 4 | Restart Data Plane services to apply the changes to enable access to cross-account resources. | 


By doing this, Data Plane picks up the updated credentials mapping and automatically accesses resources across accounts using secure, managed mechanisms.

### Real-World Example

Imagine:

- Your Data Plane runs in AWS Account A.
- Your S3 is in Account B.
- Your credentials are in Secrets Manager in Account C.

You would:

- In Account B, set an S3 bucket policy to allow Account A to access the bucket.
- In Account C, set a Secrets Manager policy to allow Account A to retrieve secrets.
- In Account A, configure **`secretmanager.json`** to reference the secret and bucket.
- Update Kubernetes secrets and restart Data Plane services.

This setup ensures secure  access to the bucket and secrets across accounts. cross-account buckets securely.

**Why This Matters**

- Keeps  access permissions separate for each  account.
- Supports complex cloud setups where data and credentials are centralized
- Uses a single **`secretmanager.json`** file for consistent configuration.
- Ensures all access is logged and auditable.

## Integrating Data Sources with Cross-Account Access

When adding data sources like AWS S3 and Google Cloud Storage (GCS), cross-account access simplifies the process. During the Connection Details step, you provide authentication details, and if cross-account access is already configured, additional permission changes are needed.

**Example: Adding an AWS S3 Data Source**

When you're integrating an AWS S3 source, and you've already set up cross-account access in your Data Plane deployment, follow these steps during the Connection Details stage:

1. Enter the AWS Access Key and AWS Secret Key
2. Specify the AWS Region (e.g., us-east-1).
3. Enter the S3 Bucket Name that has cross-account access permissions.
4. You can click the ➕ icon to add more buckets.
5. Click **Test Connection**.
Note If the connection fails, check the bucket policies and IAM roles are correctly set up.

**Using AWS Secrets Manager?**

Ensure the IAM role assigned to your Data Plane service has the necessary permissions to access the secret in AWS Secrets Manager. For detailed setup instructions, refer to the Secret Manager Setup page.

**Example: Adding a GCS Data Source**

If you’ve already configured GCP cross-project access, here’s how to complete the Connection Details step when adding a GCS data source:

1. Upload your GCS Credentials File (service account key), or select a secret from GCP  Secret Manager.
2. Enter the GCP Project Name.
3. Enter the GCS Bucket Name for which you’ve granted cross-project access.
4. Click ➕ to add more buckets if needed.
5. Click **Test Connection**.

Note Ensure that the service account used here has the correct permissions (`storage.buckets.get`, `storage.objects.get`, `storage.objects.list`) on the bucket.

**Using GCP Secret Manager?**

Ensure the service account used by your Data Plane deployment has the appropriate permissions to access secrets in GCP Secret Manager. For detailed setup instructions, refer to the Secret Manager Setup page.

---

## Best Practices

- Always implement least privilege: only grant the minimal permissions needed.
- For AWS Secrets Manager cross-account access, remember that you also need the secret encrypted with a KMS key that allows access to your Data Plane role.
- For GCP, ensure your Data Plane runtime service account has the necessary roles in the other project.
- After configuring cross-account access, always test connections from ADOC by creating a test asset or data source and verifying success.