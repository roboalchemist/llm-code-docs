# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.amplify_artifact.dataset.md

---
title: Amplify Artifact
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Amplify Artifact
---

# Amplify Artifact

Amplify Artifact in AWS represents the output files or build results generated during an Amplify app's build and deployment process. These artifacts can include compiled code, configuration files, or other assets that are produced by the Amplify build pipeline and are used to deploy and run the application in the cloud.

```
aws.amplify_artifact
```

## Fields

| Title              | ID   | Type       | Data Type                       | Description |
| ------------------ | ---- | ---------- | ------------------------------- | ----------- |
| _key               | core | string     |
| account_id         | core | string     |
| artifact_file_name | core | string     | The file name for the artifact. |
| artifact_id        | core | string     | The unique ID for the artifact. |
| tags               | core | hstore_csv |
