# Source: https://docs.axonius.com/docs/gcp-configuration-for-cloud-asset-compliance.md

# GCP Configuration for Cloud Asset Compliance

All of the Cloud Asset Compliance calculations are done as part of your discovery cycle using the same Google Cloud Platform accounts that were configured as part of the existing Google Cloud Platform adapters.

## Enabling Cloud APIs

In order to check all benchmark rules, the following additional APIs need to be enabled.
Follow these instructions for enabling APIs:[Enable Cloud APIs for GCP](/docs/google-cloud-platform-gcp#1-enable-cloud-apis).

* IAM API (Cloud Resource Manager API)

* Database (Cloud SQL API)

* Storage (Cloud Storage/Buckets API)

* Compute API

* BigQuery API

* Cloud Key Management Service (KMS)

* APICloud Logging API

## Permissions

Follow the instructions in [Creating a Service Account](/docs/google-cloud-platform-gcp#2-create-a-service-account-and-grant-permissions-to-that-service-account) to give the Axonius Service Account the  'role:roles/iam.securityReviewer' permission.

![GCPPErmissions.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/GCPPErmissions.png)