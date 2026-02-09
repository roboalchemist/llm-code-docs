# Source: https://docs.datadoghq.com/security/default_rules/def-000-4mc.md

---
title: Projects should have OS Login enabled for SSH authentication
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Projects should have OS Login enabled
  for SSH authentication
---

# Projects should have OS Login enabled for SSH authentication
 
## Description{% #description %}

Enabling OS Login binds SSH certificates to IAM users and facilitates effective SSH certificate management.

## Rationale{% #rationale %}

Enabling OS Login ensures that SSH keys used to connect to instances are mapped to IAM users. Revoking access to an IAM user will revoke all the SSH keys associated with that particular user. It facilitates centralized and automated SSH key pair management, which is useful in handling cases like compromised SSH key pairs and/or revocation of external, third-party, vendor users.

To use OS Login, the instance using Custom Images must have the latest version of the Linux Guest Environment installed. The following image families do not support OS Login:

- Project cos-cloud (Container-Optimized OS) image family cos-stable.
- All project coreos-cloud (CoreOS) image families
- Project suse-cloud (SLES) image family sles-11
- All Windows Server and SQL Server image families

The project's `enable-oslogin` can be overridden by setting the `enable-oslogin` parameter to an instance metadata individually.

### Impact{% #impact %}

Enabling OS Login on a project disables metadata-based SSH key configurations on all instances of a project. Disabling OS Login restores SSH keys that you have configured in a project's or an instance's metadata.

### Exception{% #exception %}

VMs created by GKE should be excluded. These VMs have names that start with `gke-` and are labeled `goog-gke-node`.

### Default value{% #default-value %}

By default, the parameter `enable-oslogin` is not set, which is equivalent to setting it to `FALSE`.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

1. Go to the [VM compute metadata](https://console.cloud.google.com/compute/metadata) page.
1. Click **Edit**.
1. Add a metadata entry for the key `enable-oslogin` with the value `TRUE`.
1. Click **Save** to apply the changes.
1. For every instance that overrides the project setting, go to the VM Instance's page at [https://console.cloud.google.com/compute/instances](https://console.cloud.google.com/compute/instances).
1. Click the name of the instance from which you want to remove the metadata value.
1. At the top of the instance's details page, click **Edit** to edit the instance's settings.
1. Under Custom Metadata, remove any entries with the key `enable-oslogin` set to `FALSE`.
1. At the bottom of the instance's details page, click **Save** to apply your changes to the instance.

### From the command line{% #from-the-command-line %}

1. Configure OS Login for the project by running the following command:

   ```
   gcloud compute project-info add-metadata --metadata enable-oslogin=TRUE
   ```

1. Use the following command to remove instance metadata that overrides the project setting:

   ```
   gcloud compute instances remove-metadata <INSTANCE_NAME> --keys=enable-oslogin
   ```

Optionally, you can enable two-factor authentication for OS Login. See [Setting up OS Login with 2-step verification ](https://cloud.google.com/compute/docs/oslogin/setup-two-factor-authentication)for more information.

## References{% #references %}

1. [https://cloud.google.com/compute/docs/instances/managing-instance-access](https://cloud.google.com/compute/docs/instances/managing-instance-access)
1. [https://cloud.google.com/compute/docs/instances/managing-instance-access#enable_oslogin](https://cloud.google.com/compute/docs/instances/managing-instance-access#enable_oslogin)
1. [https://cloud.google.com/sdk/gcloud/reference/compute/instances/remove-metadata](https://cloud.google.com/sdk/gcloud/reference/compute/instances/remove-metadata)
1. [https://cloud.google.com/compute/docs/oslogin/setup-two-factor-authentication](https://cloud.google.com/compute/docs/oslogin/setup-two-factor-authentication)
