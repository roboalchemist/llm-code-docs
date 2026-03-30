# Source: https://docs.datadoghq.com/security/default_rules/zib-w32-e2z.md

---
title: Virtual machines in Azure should use SSH authentication keys for security
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Virtual machines in Azure should use
  SSH authentication keys for security
---

# Virtual machines in Azure should use SSH authentication keys for security

## Description{% #description %}

Use SSH authentication keys to secure Linux virtual machines.

## Rationale{% #rationale %}

Using SSH to secure authentications is a security best practice, as traditional username and password authentication is vulnerable to malicious tactics such as brute-force attacks. SSH uses a combination of public and private key pairs to secure the authentication process. Access to the private key is automated and tightly controlled, without both keys SSH access will not be granted. This also eliminates the need for users to memorize complex passwords for virtual machine access.

## Remediation{% #remediation %}

### From the command line{% #from-the-command-line %}

1. Follow the steps listed at [Detailed steps: Create and manage SSH keys for authentication to a Linux VM in Azure](https://docs.microsoft.com/en-us/azure/virtual-machines/linux/create-ssh-keys-detailed) to create and deploy VMs using SSH.
1. If needing to transition from Username and Password authentication, to SSH, there is no way to transition directly. You must deprovision the current VM and create an image of it with SSH as the authentication method. Follow the steps on [How to create a managed image of a virtual machine or VHD](https://docs.microsoft.com/en-us/azure/virtual-machines/linux/capture-image).
