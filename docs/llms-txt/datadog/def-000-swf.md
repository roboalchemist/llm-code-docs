# Source: https://docs.datadoghq.com/security/default_rules/def-000-swf.md

---
title: Configure SSH to use System Crypto Policy
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Configure SSH to use System Crypto
  Policy
---

# Configure SSH to use System Crypto Policy

## Description{% #description %}

Crypto Policies provide a centralized control over crypto algorithms usage of many packages. SSH is supported by crypto policy, but the SSH configuration may be set up to ignore it. To check that Crypto Policies settings are configured correctly, ensure that the `CRYPTO_POLICY` variable is either commented or not set at all in the `/etc/sysconfig/sshd`.

## Rationale{% #rationale %}

Overriding the system crypto policy makes the behavior of the SSH service violate expectations, and makes system configuration more fragmented.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

SSH_CONF="/etc/sysconfig/sshd"

sed -i "/^\s*CRYPTO_POLICY.*$/Id" $SSH_CONF
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```
- name: Configure SSH to use System Crypto Policy
  lineinfile:
    dest: /etc/sysconfig/sshd
    state: absent
    regexp: (?i)^\s*CRYPTO_POLICY.*$
  tags:
  - CCE-80939-2
  - DISA-STIG-RHEL-08-010287
  - NIST-800-53-AC-17(2)
  - NIST-800-53-AC-17(a)
  - NIST-800-53-CM-6(a)
  - NIST-800-53-MA-4(6)
  - NIST-800-53-SC-13
  - PCI-DSS-Req-2.2
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.7
  - configure_ssh_crypto_policy
  - disable_strategy
  - low_complexity
  - medium_disruption
  - medium_severity
  - reboot_required
```
