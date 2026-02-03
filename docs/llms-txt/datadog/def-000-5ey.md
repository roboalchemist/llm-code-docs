# Source: https://docs.datadoghq.com/security/default_rules/def-000-5ey.md

---
title: >-
  SQL Database instances should only allow ingress traffic from specific IP
  addresses
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > SQL Database instances should only
  allow ingress traffic from specific IP addresses
---

# SQL Database instances should only allow ingress traffic from specific IP addresses
 
## Description{% #description %}

A database server should accept connections only from trusted networks and IPs and restrict access from public IP addresses.

## Rationale{% #rationale %}

To minimize attack surface on a database server instance, only trusted, known, and required IPs should be allowed to connect to it. An authorized network should not have IPs or networks configured to `0.0.0.0/0` which allows access to the instance from anywhere in the world. Authorized networks apply only to instances with public IPs.

## Impact{% #impact %}

The Cloud SQL database instance would not be available to public IP addresses.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

1. Go to the Cloud SQL Instances page in the Google Cloud Console by visiting [https://console.cloud.google.com/sql/instances](https://console.cloud.google.com/sql/instances).
1. Click the instance name to open its `Instance details` page.
1. Under the `Configuration` section click `Edit configurations`.
1. Under `Configuration options` expand the `Connectivity` section.
1. Click the `delete` icon for the authorized network `0.0.0.0/0`.
1. Click `Save` to update the instance.

### From the command line{% #from-the-command-line %}

Update the authorized network list by removing addresses:

```
gcloud sql instances patch <INSTANCE_NAME> --authorized-networks=IP_ADDR1,IP_ADDR2...
```

## Prevention{% #prevention %}

To prevent new SQL instances from being configured to accept incoming connections from any IP addresses, set up a `Restrict Authorized Networks on Cloud SQL instances` Organization Policy at: [https://console.cloud.google.com/iam-admin/orgpolicies/sql-restrictAuthorizedNetworks](https://console.cloud.google.com/iam-admin/orgpolicies/sql-restrictAuthorizedNetworks).

## Default value{% #default-value %}

By default, authorized networks are not configured. Remote connection to Cloud SQL database instance is not possible unless authorized networks are configured.

## References{% #references %}

1. [https://cloud.google.com/sql/docs/mysql/configure-ip](https://cloud.google.com/sql/docs/mysql/configure-ip)
1. [https://console.cloud.google.com/iam-admin/orgpolicies/sql-restrictAuthorizedNetworks](https://console.cloud.google.com/iam-admin/orgpolicies/sql-restrictAuthorizedNetworks)
1. [https://cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints](https://cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints)
1. [https://cloud.google.com/sql/docs/mysql/connection-org-policy](https://cloud.google.com/sql/docs/mysql/connection-org-policy)

## Additional information{% #additional-information %}

There is no IPv6 configuration found for Google cloud SQL server services.
