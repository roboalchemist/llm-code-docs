# Source: https://docs.datadoghq.com/security/default_rules/def-000-z3h.md

---
title: Instances should use a non-default service account
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Instances should use a non-default
  service account
---

# Instances should use a non-default service account
 
## Description{% #description %}

To follow the principle of least privileges and to prevent potential privilege escalation, assign instances to a service account other than the default Compute Engine service account.

## Rationale{% #rationale %}

Even when used with the default "Allow default access" scope, the default Compute Engine service account has sensitive read permissions. For instance, it can access data from all Google Cloud Storage buckets in the project.

To defend against data theft if your VM is compromised and prevent an attacker from gaining access to sensitive data in your project, it is recommended that you not use the default Compute Engine service account. Instead, create a new service account and assign only the permissions needed by your instance.

The default Compute Engine service account is named `[PROJECT_NUMBER]-compute@developer.gserviceaccount.com`.

## Exception{% #exception %}

VMs created by GKE are excluded from this guidance. These VMs have names that start with `gke-` and are labeled `goog-gke-node`.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

1. Go to the `VM instances` page by visiting: [https://console.cloud.google.com/compute/instances](https://console.cloud.google.com/compute/instances).
1. Click on the instance name to go to its `VM instance details` page.
1. Click `STOP` and then click `EDIT`.
1. Under the section `API and identity management`, select a service account other than the default Compute Engine service account. You may first need to create a new service account.
1. Click `Save` and then click `START`.

### From the command line{% #from-the-command-line %}

1. Stop the instance:
   ```
   gcloud compute instances stop <INSTANCE_NAME>
   ```
1. Update the instance:
   ```
   gcloud compute instances set-service-account <INSTANCE_NAME> --service-account=<SERVICE_ACCOUNT>
   ```
1. Restart the instance:
   ```
   gcloud compute instances start <INSTANCE_NAME>
   ```

## Default value{% #default-value %}

By default, Compute instances are configured to use the default Compute Engine service account.

## References{% #references %}

1. [https://cloud.google.com/compute/docs/access/service-accounts#default_service_account](https://cloud.google.com/compute/docs/access/service-accounts)
1. [https://cloud.google.com/compute/docs/access/service-accounts#accesscopesiam](https://cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances)
1. [https://cloud.google.com/compute/docs/access/service-accounts](https://cloud.google.com/sdk/gcloud/reference/compute/instances/set-service-account)
1. [https://cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances][5]
1. [https://cloud.google.com/sdk/gcloud/reference/compute/instances/set-service-account][6]

## CIS Controls{% #cis-controls %}

Version 8 - 4.7: Manage Default Accounts on Enterprise Assets and Software

- Manage default accounts on enterprise assets and software, such as root, administrator, and other pre-configured vendor accounts. Example implementations can include: disabling default accounts or making them unusable.

Version 7 - 4.7 Limit Access to Script Tools

- Limit access to scripting tools (such as Microsoft PowerShell and Python) to only administrative or development users with the need to access those capabilities.
