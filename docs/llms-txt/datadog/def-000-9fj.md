# Source: https://docs.datadoghq.com/security/default_rules/def-000-9fj.md

---
title: >-
  Instances should be configured to use a non-default service account with
  restricted API access
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Instances should be configured to use a
  non-default service account with restricted API access
---

# Instances should be configured to use a non-default service account with restricted API access
 
## Description{% #description %}

To follow the principle of least privilege and to prevent potential privilege escalation, assign instances to a service account other than the default Compute Engine service account. These accounts have a scope option of `Allow full access to all Cloud APIs`, which grants Editor rights on the project.

## Rationale{% #rationale %}

When an instance is assigned the default compute engine and the non-default scope `Allow full access to all Cloud APIs` is selected, the instance has full Editor access on the Google Cloud project. This may allow users to perform malicious cloud operations and API calls leading to successful privilege escalation.

To defend against privilege escalation if your VM is compromised and prevent an attacker from gaining administrative rights to your project, it is recommended that you not use the default Compute Engine service account with an unrestricted scope. Instead, create a new service account and assign only the permissions needed by your instance.

The default Compute Engine service account is named `[PROJECT_NUMBER]-compute@developer.gserviceaccount.com`.

## Exception{% #exception %}

VMs created by GKE are excluded from this rule. These VMs have names that start with `gke-` and are labeled `goog-gke-node`.

## Impact{% #impact %}

To change a service account or scope for an instance, the instance must be stopped.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

1. Go to the `VM instances` page by visiting: [https://console.cloud.google.com/compute/instances](https://console.cloud.google.com/compute/instances).
1. Click on the impacted VM instance.
1. If the instance is not stopped, click the `Stop` button. Wait for the instance to stop.
1. Click the `Edit` button.
1. Scroll down to the `Service Account` section.
1. Select a different service account or ensure that `Allow full access to all Cloud APIs` is not selected.
1. Click the `Save` button to save your changes and then click `START`.

### From the command line{% #from-the-command-line %}

1. Stop the instance:
   ```
   gcloud compute instances stop <INSTANCE_NAME>
   ```
1. Update the instance:
   ```
   gcloud compute instances set-service-account <INSTANCE_NAME> --service-account=<SERVICE_ACCOUNT> --scopes [SCOPE1, SCOPE2...]
   ```
1. Restart the instance:
   ```
   gcloud compute instances start <INSTANCE_NAME>
   ```

## Default value{% #default-value %}

By default, Compute instances are configured to use the default Compute Engine service account, but with a limited access scope that has read-only access to data in the project.

## References{% #references %}

1. [https://cloud.google.com/compute/docs/access/service-accounts#default_service_account](https://cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances)
1. [https://cloud.google.com/compute/docs/access/service-accounts#accesscopesiam](https://cloud.google.com/compute/docs/access/service-accounts)
1. [https://cloud.google.com/compute/docs/access/service-accounts][4]
1. [https://cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances][5]
1. [https://cloud.google.com/sdk/gcloud/reference/compute/instances/set-service-account][6]

## CIS Controls{% #cis-controls %}

Version 8 - 4.7: Manage Default Accounts on Enterprise Assets and Software

- Manage default accounts on enterprise assets and software, such as root, administrator, and other pre-configured vendor accounts. Example implementations can include: disabling default accounts or making them unusable.

Version 7 - 4.7 Limit Access to Script Tools

- Limit access to scripting tools (such as Microsoft PowerShell and Python) to only administrative or development users with the need to access those capabilities.
