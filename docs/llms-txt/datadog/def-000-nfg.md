# Source: https://docs.datadoghq.com/security/default_rules/def-000-nfg.md

---
title: BigQuery Dataset should not be anonymously or publicly accessible
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > BigQuery Dataset should not be
  anonymously or publicly accessible
---

# BigQuery Dataset should not be anonymously or publicly accessible
 
## Description{% #description %}

It is recommended that the IAM policy on BigQuery datasets does not allow anonymous or public access.

## Rationale{% #rationale %}

Granting permissions to `allUsers` or `allAuthenticatedUsers` allows any user access to the dataset. Such access might not be desirable if sensitive data is being stored in the dataset. Therefore, ensure that anonymous or public access to a dataset is not allowed.

## Impact{% #impact %}

The dataset is publicly accessible. Explicit modification of IAM privileges would be necessary to make them publicly accessible.

## Remediation{% #remediation %}

1. Go to BigQuery by visiting: [https://console.cloud.google.com/bigquery](https://console.cloud.google.com/bigquery).
1. Select the dataset from **Resources**.
1. Click **Sharing** near the right side of the window and select **Permissions**.
1. Review each attached role.
1. Click the delete icon for each member `allUsers` or `allAuthenticatedUsers`. On the popup, click **Remove**.

### From Google Cloud Console{% #from-google-cloud-console %}

List the name of all datasets.

```
bq ls
```

Retrieve each dataset details using the following command:

```
bq show --format=prettyjson PROJECT_ID:DATASET_NAME > PATH_TO_FILE
```

In the access section of the JSON file, update the dataset information to remove all roles containing `allUsers` or `allAuthenticatedUsers`.

```
bq update --source PATH_TO_FILE PROJECT_ID:DATASET_NAME
```

## References{% #references %}

1. [https://cloud.google.com/bigquery/docs/control-access-to-resources-iam](https://cloud.google.com/bigquery/docs/control-access-to-resources-iam)
