# Source: https://docs.datadoghq.com/security/default_rules/def-000-1jd.md

---
title: >-
  Users should be assigned the 'Service Account User' or 'Service Account Token
  Creator' roles at the Service Account level
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Users should be assigned the 'Service
  Account User' or 'Service Account Token Creator' roles at the Service Account
  level
---

# Users should be assigned the 'Service Account User' or 'Service Account Token Creator' roles at the Service Account level
 
## Description{% #description %}

Verify that users have the Service Account User (`iam.serviceAccountUser`) and Service Account Token Creator (`iam.serviceAccountTokenCreator`) roles for a specific service account rather than at the project level.

## Rationale{% #rationale %}

A service account is a special Google account that belongs to an application or a virtual machine (VM), instead of to an individual end user. Application/VM-Instance uses the service account to call the service's Google API so that users aren't directly involved. In addition to being an identity, a service account is a resource that has IAM policies attached to it. These policies determine who can use the service account. Users with IAM roles to update the App Engine and Compute Engine instances (such as App Engine Deployer or Compute Instance Admin) can effectively run code as the service accounts used to run these instances, and indirectly gain access to all the resources for which the service accounts have access. Similarly, SSH access to a Compute Engine instance may also provide the ability to execute code as that instance/service account. Based on business needs, there can be multiple user-managed service accounts configured for a project. Granting the `iam.serviceAccountUser` or `iam.serviceAccountTokenCreator` roles to a user for a project gives the user access to all service accounts in the project, including service accounts that may be created in the future. These roles can result in an elevation of privileges when someone uses a service account and corresponding Compute Engine instances. In order to implement least privileges best practices, IAM users should not be assigned the Service Account User or Service Account Token Creator roles at the project level. Instead, these roles should be assigned to a user for a specific service account, giving that user access to the service account. The Service Account User role allows a user to bind a service account to a long-running job service, whereas the Service Account Token Creator role allows a user to directly impersonate (or assert) the identity of a service account.

## Impact{% #impact %}

After revoking Service Account User or Service Account Token Creator roles at the project level from all impacted user accounts, these roles should be assigned to users for specific service accounts according to business needs.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

1. Go to the [IAM page](https://console.cloud.google.com/iam-admin/iam) in the GCP Console.
1. In the filter table text bar, enter the text `Role: Service Account User`.
1. Click the delete bin icon in front of the role `Service Account User` for every user listed as a result of the filter.
1. In the filter table text bar, enter the text `Role: Service Account Token Creator`.
1. Click the delete bin icon in front of the role `Service Account Token Creator` for every user listed as a result of the filter.

### From the command line{% #from-the-command-line %}

1. Using a text editor, remove the bindings with the `roles/iam.serviceAccountUser` or `roles/iam.serviceAccountTokenCreator`. For example, you can use the iam.json file shown below as follows:
   ```
   {
    "bindings": [
    {
    "members": [ "serviceAccount:our-project-123@appspot.gserviceaccount.com",
    ],
    "role": "roles/appengine.appViewer" },
    {
        "members": [
        "user:email1@gmail.com"
        ],
    "role": "roles/owner"
    },
    {
        "members": [
    "serviceAccount:our-project-123@appspot.gserviceaccount.com",
    "serviceAccount:123456789012-compute@developer.gserviceaccount.com" ],
        "role": "roles/editor"
    }
    ],
    "etag": "BwUjMhCsNvY="
    }
   ```
1. Update the project's IAM policy:
   ```
   gcloud projects set-iam-policy PROJECT_ID iam.json
   ```

## Default value{% #default-value %}

By default, users do not have the Service Account User or Service Account Token Creator role assigned at the project level.

## References{% #references %}

1. [https://cloud.google.com/iam/docs/service-accounts](https://cloud.google.com/iam/docs/service-accounts)
1. [https://cloud.google.com/iam/docs/granting-roles-to-service-accounts](https://cloud.google.com/iam/docs/granting-roles-to-service-accounts)
1. [https://cloud.google.com/iam/docs/understanding-roles](https://cloud.google.com/iam/docs/understanding-roles)
1. [https://cloud.google.com/iam/docs/granting-changing-revoking-access](https://cloud.google.com/iam/docs/granting-changing-revoking-access)
1. [https://console.cloud.google.com/iam-admin/iam](https://console.cloud.google.com/iam-admin/iam)

## Additional Information{% #additional-information %}

A user-managed key cannot be created on GCP-Managed Service Accounts.
