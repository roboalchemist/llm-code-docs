# Source: https://docs.datadoghq.com/security/default_rules/def-000-jr3.md

---
title: >-
  Service accounts should keep the 'Service Account Admin' and 'Service Account
  User' roles separate
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Service accounts should keep the
  'Service Account Admin' and 'Service Account User' roles separate
---

# Service accounts should keep the 'Service Account Admin' and 'Service Account User' roles separate
 
## Description{% #description %}

Security best practices recommend that the principle of 'Separation of Duties' is enforced while assigning service-account related roles to users. This is achieved by ensuring that no user has the Service Account Admin and Service Account User roles assigned at the same time.

## Rationale{% #rationale %}

The predefined IAM role `Service Account admin` allows the user/identity to create, delete, and manage service account(s). The predefined IAM role `Service Account User` allows the user/identity (with adequate privileges on Compute and App Engine) to assign service account(s) to Apps/Compute instances.

Separation of duties is the concept of ensuring that one individual does not have all necessary permissions to be able to complete a malicious action. Using Cloud IAM service accounts, a malicious user could assume the identity of a service account to access resources that they otherwise cannot access.

Separation of duties is a business control typically used in larger organizations, meant to help avoid security or privacy incidents and errors. It is considered a best practice.

No user should have `Service Account Admin` and `Service Account User` roles assigned at the same time.

## Remediation{% #remediation %}

1. Go to `IAM & Admin/IAM` using [https://console.cloud.google.com/iam-admin/iam](https://console.cloud.google.com/iam-admin/iam)
1. For any member having both `Service Account Admin` and `Service Account User` roles granted/assigned, click the `Delete Bin` icon to remove either role from the member.

Removal of a role should be done based on the business requirements.

## Impact{% #impact %}

The removed role should be assigned to a different user based on business needs.

## References{% #references %}

1. [https://cloud.google.com/iam/docs/service-accounts](https://cloud.google.com/iam/docs/service-accounts)
1. [https://cloud.google.com/iam/docs/understanding-roles](https://cloud.google.com/iam/docs/understanding-roles)
1. [https://cloud.google.com/iam/docs/granting-roles-to-service-accounts](https://cloud.google.com/iam/docs/granting-roles-to-service-accounts)

## Additional information{% #additional-information %}

Users granted the Owner (roles/owner) and Editor (roles/editor) roles have privileges equivalent to Service Account Admin and Service Account User. To avoid misuse, Owner and Editor roles should be granted to a very limited number of users. Use of these primitive privileges should be minimal. These requirements are addressed in separate recommendations.
