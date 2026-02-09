# Source: https://docs.datadoghq.com/security/default_rules/def-000-o8q.md

---
title: '''Unattached disks'' should be encrypted with Customer Managed Key (CMK)'
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > 'Unattached disks' should be encrypted
  with Customer Managed Key (CMK)
---

# 'Unattached disks' should be encrypted with Customer Managed Key (CMK)
 
## Description{% #description %}

To enhance security and meet regulatory requirements, it is essential to ensure that unattached disks in a subscription are encrypted using a Customer Managed Key (CMK). By default, managed disks are encrypted with a Platform Managed Key (PMK), but utilizing CMK can provide an additional level of security.

Encrypting unattached managed disks ensures that the entire content can only be accessed with the corresponding key, safeguarding the volume from unauthorized reads. It is crucial to consider the risk of compromised user accounts with administrative access to the VM service, as they can potentially mount or attach these data disks. By encrypting the disks with CMK, the risk of sensitive information disclosure and tampering is mitigated, providing a higher level of security.

## Remediation{% #remediation %}

If data stored in the disk is no longer useful, refer to Azure documentation to delete unattached data disks at:

[https://docs.microsoft.com/en-us/rest/api/compute/disks/delete](https://docs.microsoft.com/en-us/rest/api/compute/disks/delete)

[https://docs.microsoft.com/en-us/cli/azure/disk?view=azure-cli-latest#az-disk-delete](https://docs.microsoft.com/en-us/cli/azure/disk?view=azure-cli-latest#az-disk-delete)

If data stored in the disk is important, To encrypt the disk refer azure documentation at:

[https://docs.microsoft.com/en-us/azure/virtual-machines/disks-enable-customer-managed-keys-portal](https://docs.microsoft.com/en-us/azure/virtual-machines/disks-enable-customer-managed-keys-portal)

[https://docs.microsoft.com/en-us/rest/api/compute/disks/update#encryptionsettings](https://docs.microsoft.com/en-us/rest/api/compute/disks/update#encryptionsettings)
