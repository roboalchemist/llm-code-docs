# Source: https://docs.datadoghq.com/security/default_rules/def-000-frb.md

---
title: Uninstall vsftpd Package
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Uninstall vsftpd Package
---

# Uninstall vsftpd Package
 
## Description{% #description %}

The `vsftpd` package can be removed with the following command:

```
 $ apt-get remove vsftpd
```

## Rationale{% #rationale %}

Removing the `vsftpd` package decreases the risk of its accidental activation.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# CAUTION: This remediation script will remove vsftpd
# from the system, and may remove any packages
# that depend on vsftpd. Execute this
# remediation AFTER testing on a non-production
# system!


DEBIAN_FRONTEND=noninteractive apt-get remove -y "vsftpd"
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```
- name: 'Uninstall vsftpd Package: Ensure vsftpd is removed'
  ansible.builtin.package:
    name: vsftpd
    state: absent
  tags:
  - NIST-800-53-CM-6(a)
  - NIST-800-53-CM-7
  - NIST-800-53-CM-7(a)
  - NIST-800-53-CM-7(b)
  - NIST-800-53-CM-7.1(ii)
  - NIST-800-53-IA-5(1)(c)
  - NIST-800-53-IA-5(1).1(v)
  - disable_strategy
  - high_severity
  - low_complexity
  - low_disruption
  - no_reboot_needed
  - package_vsftpd_removed
```
