# Source: https://docs.datadoghq.com/security/default_rules/def-000-l0z.md

---
title: Service accounts should only be bound to non-administrative roles
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Service accounts should only be bound
  to non-administrative roles
---

# Service accounts should only be bound to non-administrative roles
 
## Description{% #description %}

A service account is a special Google account that belongs to an application or a VM, instead of to an individual end-user. The application uses the service account to call the service's Google API so that users aren't directly involved. It's recommended not to use admin roles for ServiceAccount.

### Default value{% #default-value %}

User-managed (and not user-created) default service accounts have the `Editor` (`roles/editor`) role assigned to them to support GCP services they offer. By default, there are no roles assigned to user-managed, user-created service accounts.

## Rationale{% #rationale %}

Service accounts represent service-level security of the Resources (application or a VM) which can be determined by the roles assigned to it. Enrolling ServiceAccount with Admin rights gives full access to an assigned application or a VM. A ServiceAccount Access holder can perform critical actions like delete, update, and change settings, etc. without user intervention. For this reason, Datadog recommends that service accounts not have an Admin role.

### Impact{% #impact %}

Removing `*Admin or *admin`, `Editor`, or `Owner` role assignments from service accounts may break functionality that uses impacted service accounts. Required role(s) should be assigned to impacted service accounts in order to restore broken functionality.

- Note: This rule provides coverage for built in admin roles only and doesn't address scenarios where a custom role which has admin permissions is assigned to a service account.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

1. Go to `IAM & admin/IAM` using [https://console.cloud.google.com/iam-admin/iam](https://console.cloud.google.com/iam-admin/iam)
1. Go to the `Members`
1. Identify `User-Managed user created service account(s)` with roles containing `*Admin or *admin`, roles matching `Editor`, or roles matching `Owner`.
1. Click the `Delete bin` icon to remove the role from the member (service account in this case)

### From the command line{% #from-the-command-line %}

```bash
gcloud projects get-iam-policy PROJECT_ID --format json > iam.json
```

1. Using a text editor, Remove any `Role` which contains `roles/ *Admin` or `roles/ *admin`, or matches `roles/editor` or `roles/owner`. Add a role to the bindings array that defines the group members and the role for those members.

1. Update the project's IAM policy:

   ```bash
   gcloud projects set-iam-policy PROJECT_ID iam.json
   ```

## References{% #references %}

1. [https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/)
1. [https://cloud.google.com/iam/docs/understanding-roles](https://cloud.google.com/iam/docs/understanding-roles)
1. [https://cloud.google.com/iam/docs/understanding-service-accounts](https://cloud.google.com/iam/docs/understanding-service-accounts)
