# Source: https://docs.datadoghq.com/security/default_rules/def-000-ing.md

---
title: >-
  Publicly accessible Azure VM has privileged role and password-based SSH
  authentication
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Publicly accessible Azure VM has
  privileged role and password-based SSH authentication
---

# Publicly accessible Azure VM has privileged role and password-based SSH authentication

## Description{% #description %}

A publicly accessible compute instance with a privileged service principal has password-based SSH authentication. The usage of password-based SSH authentication increases the risk of brute-forcing username and passwords to gain access to the resource.

## Remediation{% #remediation %}

1. Identify the service principal attached to this instance.
1. Remove unnecessary privileges from the service principal. Consider using a role based on job function rather than a privileged role.
1. Review [Create and manage SSH keys for authentication to a Linux VM in Azure](https://learn.microsoft.com/en-us/azure/virtual-machines/linux/create-ssh-keys-detailed) for steps on creating and enablement of SSH keys for authentication to compute instances. To transition from Username and Password authentication to SSH, you must deprovision the current VM and create an image of it with SSH as the authentication method. There is no way to transition directly.
