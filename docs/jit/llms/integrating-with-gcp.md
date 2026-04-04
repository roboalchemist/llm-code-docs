# Source: https://docs.jit.io/docs/integrating-with-gcp.md

# GCP Integration

Integrating with GCP

Google Cloud Platform integration enables you to scan your GCP infrastructure for [runtime misconfigurations](https://docs.jit.io/docs/scan-runtime-infra#google-cloud-platform-checklist). Though it does not require the integration steps below, Jit recommends that you also activate the [Scan IaC for Misconfigurations](https://docs.jit.io/docs/scan-iac-for-static-misconfigurations) security requirement for complete infrastructure protection.

***

## Two Integration Methods

You can connect your GCP project to Jit using one of two supported approaches:

### Option 1 (Recommended): Using Workload Identity Federation (WIF)

This is the preferred and more secure method. It avoids storing static credentials by leveraging federation from AWS (e.g., Lambda, EC2, Fargate) to impersonate a GCP Service Account.

### Option 2: Using a GCP Service Account (Key File)

This is the traditional and simplest method. It uses static JSON key for the service account to authenticate.

ℹ️ **Navigate to Jit → Integrations and select the GCP card to begin setup**

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/1fd190994d7b7f3a9f75cec514c3825459baae1e121a5b1638e6d67187284c65-Screenshot_2025-06-08_at_13.31.49.png",
        "",
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]

***

## Before You Start

To integrate with GCP, you'll need:

* A GCP project with billing enabled. This ensures all required APIs function correctly—even free-tier ones.
* IAM permissions to create service accounts.
* For **Option 1 (WIF)**: Additional IAM permissions to create Workload Identity Pools.

***

### Shared Setup

These steps apply to both integration methods:

1. Create a new service account in your Google Cloud project. See [Google Cloud documentation](https://cloud.google.com/iam/docs/creating-managing-service-accounts) for details.

2. Ensure the following roles are assigned to the service account:

   * Viewer
   * Security Reviewer
   * Stackdriver Account Viewer

   ℹ️ Jit will only scan GCP projects where the service account or federated identity has been granted access.

3. Make sure the **Google Cloud Resource Manager API** is enabled on the account.

***

## Detailed Setup Instructions

### Option 1 (Recommended): Using Workload Identity Federation (WIF)

#### Steps:

4. Create a new Workload Identity Pool in your GCP project to enable federation from JIT. See [instructions to create a Workload Identity Pool](https://cloud.google.com/iam/docs/workload-identity-federation-with-other-clouds#create_a_pool) for instructions.

5. Create a new AWS provider within that pool.

6. **Get the JIT AWS Account ID**: Go to Jit → Integrations → GCP and start the integration setup. The required AWS Account ID will be displayed in the integration modal. Copy this Account ID - you'll need it for the next step.

[block:image]{"images":[{"image":["https://files.readme.io/331c22a3b545154e74e519a36cf84ddac24d6665678079d3812c92e09a1b8fa1-Screenshot_2025-06-08_at_13.22.50.png","",""],"align":"left","sizing":"600px"}]}[/block]

7. Bind the `roles/iam.workloadIdentityUser` role to all identities from your JIT AWS account so they can impersonate the service account. See [Google Cloud documentation](https://cloud.google.com/iam/docs/workload-identity-federation-with-other-clouds#authenticate). Use the AWS Account ID from the previous step.

8. Create WIF file that enables JIT workloads to authenticate with GCP using the created provider. Use [this command](https://cloud.google.com/iam/docs/workload-identity-federation-with-other-clouds#create-cred-config).

⚠️ This file is a WIF credential configuration, not a service account key. It contains no secrets and enables token exchange from AWS.

#### Example WIF Credential Configuration File

```json
{
  "type": "external_account",
  "audience": "//iam.googleapis.com/projects/123456789/locations/global/workloadIdentityPools/my-pool/providers/my-provider",
  "subject_token_type": "urn:ietf:params:aws:token-type:aws4_request",
  "token_url": "https://sts.googleapis.com/v1/token",
  "credential_source": {
    "environment_id": "aws1",
    "region_url": "http://169.254.169.254/latest/meta-data/placement/region",
    "url": "http://169.254.169.254/latest/meta-data/iam/security-credentials",
    "regional_cred_verification_url": "https://sts.{region}.amazonaws.com?Action=GetCallerIdentity&Version=2011-06-15"
  }
}
```

9. Go to Jit → Integrations → GCP and paste your WIF credential configuration.

10. Confirm connectivity in the Jit UI using the "Connect" button to validate access.

***

### Option 2: Using a GCP Service Account (Key File)

#### Steps:

4. Create a new service account in your Google Cloud project. See  [Google Cloud documentation](https://cloud.google.com/iam/docs/service-accounts-create) for instructions.

5. Go to Jit → Integrations → GCP and upload your JSON key.

[block:image]{"images":[{"image":["https://files.readme.io/bfc4c9ed7cfcf98a698c54eb98a3392aba864ceca0cf3606808ee1ae5e0c3ac8-Screenshot_2025-06-08_at_13.44.27.png","",""],"align":"left","sizing":"600px"}]}[/block]

6. Confirm connectivity in the Jit UI using the "Connect" button to validate access.
   ***
   ## Integration Complete
   Once successfully connected, Jit will begin scanning your GCP infrastructure for runtime misconfigurations. The integration enables continuous monitoring of your cloud resources to identify security vulnerabilities and compliance issues across your GCP projects.
   ***
   ## Managing Your Integration
   ### Disconnecting from GCP
   To disconnect your GCP integration:
   1. Go to Jit → Integrations → GCP
   2. Click on the connected GCP card
   3. Select "Disconnect" to remove the integration