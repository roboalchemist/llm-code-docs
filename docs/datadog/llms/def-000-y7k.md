# Source: https://docs.datadoghq.com/security/default_rules/def-000-y7k.md

---
title: Cloud Storage Bucket should not be anonymously or publicly accessible
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Cloud Storage Bucket should not be
  anonymously or publicly accessible
---

# Cloud Storage Bucket should not be anonymously or publicly accessible

## Description{% #description %}

It is recommended that IAM policies on Cloud Storage buckets do not allow anonymous or public access.

## Rationale{% #rationale %}

With anonymous or public access, anyone has permission to access bucket content. Such access might not be desired if you are storing sensitive data, so ensure that anonymous or public access to a bucket is not allowed.

### Additional Information{% #additional-information %}

To implement access restrictions on buckets, configuring Bucket IAM is preferred over configuring Bucket ACL. In the GCP console, the **Edit Permissions** button for a bucket exposes IAM configurations only. Bucket ACLs are configured to automatically implement and support user-enforced Bucket IAM policies. If an administrator changes a Bucket ACL using command-line gsutils or the API, the associated bucket IAM policy is also updated automatically.

### Impact{% #impact %}

Storage buckets are not publicly accessible. You have to explicitly administer bucket access.

### Prevention{% #prevention %}

You can prevent Storage buckets from becoming publicly accessible by setting up the `Domain restricted sharing` organization policy at: [https://console.cloud.google.com/iam-admin/orgpolicies/iam-allowedPolicyMemberDomains](https://console.cloud.google.com/iam-admin/orgpolicies/iam-allowedPolicyMemberDomains)

### Default value{% #default-value %}

By default, Storage buckets are not publicly accessible.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

1. Go to `Storage browser` at [https://console.cloud.google.com/storage/browser](https://console.cloud.google.com/storage/browser).
1. Click on the bucket name to access the `Bucket details` page.
1. Click on the `Permissions` tab.
1. Click the `Delete` button in front of `allUsers` and `allAuthenticatedUsers` to remove that particular role assignment.

### From the command line{% #from-the-command-line %}

Remove `allUsers` and `allAuthenticatedUsers` access.

```
gsutil iam ch -d allUsers gs://BUCKET_NAME
gsutil iam ch -d allAuthenticatedUsers gs://BUCKET_NAME
```

## References{% #references %}

1. [https://cloud.google.com/storage/docs/access-control/iam-reference](https://cloud.google.com/storage/docs/access-control/iam-reference)
1. [https://cloud.google.com/storage/docs/access-control/making-data-public](https://cloud.google.com/storage/docs/access-control/making-data-public)
1. [https://cloud.google.com/storage/docs/gsutil/commands/iam](https://cloud.google.com/storage/docs/gsutil/commands/iam)
