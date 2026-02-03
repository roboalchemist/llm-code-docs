# Source: https://docs.datadoghq.com/security/default_rules/def-000-q8r.md

---
title: '''OS and Data'' disks should be encrypted with Customer Managed Key (CMK)'
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > 'OS and Data' disks should be encrypted
  with Customer Managed Key (CMK)
---

# 'OS and Data' disks should be encrypted with Customer Managed Key (CMK)
 
## Description{% #description %}

To enhance data security, it is important to ensure that both OS disks (boot volumes) and data disks (non-boot volumes) of IaaS VMs are encrypted using Customer Managed Keys (CMK). CMKs can be achieved through either Azure Disk Encryption (ADE) or Server Side Encryption (SSE).

Encrypting the OS disk and data disks with CMK ensures that the entire content can only be accessed with the corresponding key, preventing unauthorized access. While Azure-managed disks enable encryption at rest by default using Platform Managed Keys (PMKs), using CMK provides customers with the ability to have more control over the encryption and decryption processes, allowing for key rotation and increased security.

Organizations should evaluate their security requirements for the data stored on the disks. For high-risk data, the use of CMK is strongly recommended, as it offers additional layers of security. However, for low-risk data, PMK, which is enabled by default, provides sufficient data security.

## Remediation{% #remediation %}

### From Azure Portal{% #from-azure-portal %}

**Note**: Disks must be detached from VMs to change encryption.

1. Go to **Virtual machines**.
1. For each virtual machine, go to **Settings**.
1. Click on **Disks**.
1. Click the ellipsis (â¦), then click **Detach** to detach the disk from the VM.
1. Now search for **Disks** and locate the unattached disk.
1. Click the disk then select **Encryption**.
1. Change your encryption type, then select your encryption set.
1. Click **Save**.
1. Go back to the VM and re-attach the disk.
