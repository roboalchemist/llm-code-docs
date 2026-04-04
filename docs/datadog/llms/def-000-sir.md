# Source: https://docs.datadoghq.com/security/default_rules/def-000-sir.md

---
title: Uninstall tftpd-hpa Package
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Uninstall tftpd-hpa Package
---

# Uninstall tftpd-hpa Package

## Description{% #description %}

The `tftpd-hpa` package can be removed with the following command:

```
 $ apt-get remove tftpd-hpa
```

## Rationale{% #rationale %}

Removing the `tftpd-hpa` package decreases the risk of the accidental (or intentional) activation of tftp services.

If TFTP is required for operational support (such as transmission of router configurations), its use must be documented with the Information Systems Securty Manager (ISSM), restricted to only authorized personnel, and have access control rules established.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# CAUTION: This remediation script will remove tftpd-hpa
# from the system, and may remove any packages
# that depend on tftpd-hpa. Execute this
# remediation AFTER testing on a non-production
# system!


DEBIAN_FRONTEND=noninteractive apt-get remove -y "tftpd-hpa"
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```
- name: 'Uninstall tftpd-hpa Package: Ensure tftpd-hpa is removed'
  ansible.builtin.package:
    name: tftpd-hpa
    state: absent
  tags:
  - NIST-800-53-CM-6(a)
  - NIST-800-53-CM-7(a)
  - NIST-800-53-CM-7(b)
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.4
  - disable_strategy
  - high_severity
  - low_complexity
  - low_disruption
  - no_reboot_needed
  - package_tftp-server_removed
```
