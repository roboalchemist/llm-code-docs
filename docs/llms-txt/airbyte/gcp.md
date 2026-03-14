# Source: https://docs.airbyte.com/platform/deploying-airbyte/infrastructure/gcp.md

# Source: https://docs.airbyte.com/platform/2.0/deploying-airbyte/infrastructure/gcp.md

# Source: https://docs.airbyte.com/platform/1.8/deploying-airbyte/infrastructure/gcp.md

# Source: https://docs.airbyte.com/platform/1.7/deploying-airbyte/infrastructure/gcp.md

# Source: https://docs.airbyte.com/platform/1.6/deploying-airbyte/infrastructure/gcp.md

# Google Cloud Platform (GCP)

Copy Page

CoreStandardPlusProEnterprise FlexSelf-Managed Enterprise[ Compare](https://airbyte.com/product/features)

Installing Airbyte on GCP requires a service account. The service account must have the correct permissions to access Google Cloud Storage and Google Secrets Manager, if you those integrations are to be used in your installation. The documentation for creating a GCP Service Account can be found [here](https://cloud.google.com/iam/docs/service-accounts-create)

## Google Cloud Storage Roles[​](#google-cloud-storage-roles "Direct link to Google Cloud Storage Roles")

```
roles/storage.objectCreator
roles/storage.admin
```

## Google Secret Manager Roles[​](#google-secret-manager-roles "Direct link to Google Secret Manager Roles")

```
roles/secretmanager.secretAccessor
roles/secretmanager.secretVersionAdder
roles/secretmanager.secretVersionManager
roles/secretmanager.viewer
```
