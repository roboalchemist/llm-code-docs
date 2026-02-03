# Source: https://docs.datadoghq.com/security/default_rules/def-000-2rk.md

---
title: Service Accounts should only use GCP managed keys
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Service Accounts should only use GCP
  managed keys
---

# Service Accounts should only use GCP managed keys
 
## Description{% #description %}

User managed service accounts should not have user-managed keys.

## Rationale{% #rationale %}

Anyone who has access to the keys can access resources through the service account. GCP-managed keys are used by Cloud Platform services such as App Engine and Compute Engine. These keys cannot be downloaded. Google will keep the keys and automatically rotate them on an approximately weekly basis. User-managed keys are created, downloadable, and managed by users. They expire 10 years from creation. For user-managed keys, you are responsible for key management activities including:

- Key storage
- Key distribution
- Key revocation
- Key rotation
- Protecting the keys from unauthorized users
- Key recovery Even with key owner precautions, it's easy to leak keys through common development accidents such as checking keys into the source code, leaving them in the Downloads directory, or posting them on support blogs. For these reasons, it is recommended that you don't use user-managed service account keys.

## Impact{% #impact %}

Deleting user-managed service account keys may break communication with the applications using the keys.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

1. Go to the IAM page in the GCP Console at [https://console.cloud.google.com/iam-admin/iam](https://console.cloud.google.com/iam-admin/iam).
1. In the left navigation pane, click `Service accounts`. All service accounts and their corresponding keys are listed.
1. Click the service account.
1. Click `Edit` and delete the keys.

### From the command line{% #from-the-command-line %}

To delete a user-managed service account key run:

```
gcloud iam service-accounts keys delete --iam-account=<user-managed-service-account-EMAIL> <KEY-ID>
```

## Prevention{% #prevention %}

You can disable service account key creation through the `Disable service account key creation` Organization policy by visiting [https://console.cloud.google.com/iam-admin/orgpolicies/iam-disableServiceAccountKeyCreation](https://console.cloud.google.com/iam-admin/orgpolicies/iam-disableServiceAccountKeyCreation). Learn more at: [https://cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts](https://cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts).

In addition, if you do not need service accounts in your project, you can prevent the creation of service accounts through the `Disable service account creation` Organization policy: [https://console.cloud.google.com/iam-admin/orgpolicies/iam-disableServiceAccountCreation](https://console.cloud.google.com/iam-admin/orgpolicies/iam-disableServiceAccountCreation).

## Default value{% #default-value %}

By default, there are no user-managed keys created for user-managed service accounts.

## References{% #references %}

1. [https://cloud.google.com/iam/docs/understanding-service-accounts#managing_service_account_keys](https://cloud.google.com/iam/docs/understanding-service-accounts#managing_service_account_keys)
1. [https://cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts](https://cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts)

## Additional information{% #additional-information %}

A user-managed key cannot be created on GCP-Managed Service Accounts.
