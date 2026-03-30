# Source: https://docs.datadoghq.com/security/default_rules/def-000-udm.md

---
title: SQL database instances should only use private IP addresses
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > SQL database instances should only use
  private IP addresses
---

# SQL database instances should only use private IP addresses

## Description{% #description %}

Datadog recommends configuring the second generation SQL instance to use private IPs instead of public IPs.

## Rationale{% #rationale %}

To lower the organization's attack surface, ensure your Cloud SQL databases does not have public IPs. Private IPs provide improved network security and lower latency for your application.

## Impact{% #impact %}

Removing the public IP address on SQL instances may break applications that relied on it for database connectivity.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

1. Go to the Cloud SQL Instances page in the Google Cloud Console: [https://console.cloud.google.com/sql/instances](https://console.cloud.google.com/sql/instances)
1. Click the instance name to open its Instance details page.
1. Select the `Connections` tab.
1. Deselect the `Public IP` checkbox.
1. Click `Save` to update the instance.

### From the command line{% #from-the-command-line %}

1. For every instance, remove the public IP and assign a private IP instead:

   ```
   gcloud sql instances patch <INSTANCE_NAME> --network=<VPC_NETWORK_NAME> --no-assign-ip
   ```

1. Confirm the changes using the following command:

   ```
   gcloud sql instances describe <INSTANCE_NAME>
   ```

## Prevention{% #prevention %}

To prevent new SQL instances from getting configured with public IP addresses, set up a `Restrict Public IP access on Cloud SQL instances` Organization policy at:

[https://console.cloud.google.com/iam-admin/orgpolicies/sql-restrictPublicIp](https://console.cloud.google.com/iam-admin/orgpolicies/sql-restrictPublicIp)

## Default value{% #default-value %}

By default, Cloud Sql instances have a public IP.

## References{% #references %}

1. [https://cloud.google.com/sql/docs/mysql/configure-private-ip](https://cloud.google.com/sql/docs/mysql/configure-private-ip)
1. [https://cloud.google.com/sql/docs/mysql/private-ip](https://cloud.google.com/sql/docs/mysql/private-ip)
1. [https://cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints](https://cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints)
1. [https://console.cloud.google.com/iam-admin/orgpolicies/sql-restrictPublicIp](https://console.cloud.google.com/iam-admin/orgpolicies/sql-restrictPublicIp)

## Additional information{% #additional-information %}

Replicas inherit their private IP status from their primary instance. You cannot configure a private IP directly on a replica.
