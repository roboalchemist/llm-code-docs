# Source: https://docs.datadoghq.com/security/default_rules/def-000-hca.md

---
title: Uninstall kea Package
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Uninstall kea Package
---

# Uninstall kea Package

## Description{% #description %}

If the system does not need to act as a DHCP server, the kea package can be uninstalled.

## Rationale{% #rationale %}

Removing the DHCP server ensures that it cannot be easily or accidentally reactivated and disrupt network operation.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# CAUTION: This remediation script will remove kea
# from the system, and may remove any packages
# that depend on kea. Execute this
# remediation AFTER testing on a non-production
# system!


if rpm -q --quiet "kea" ; then
dnf remove -y --noautoremove "kea"
fi
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```
- name: 'Uninstall kea Package: Ensure kea is removed'
  ansible.builtin.package:
    name: kea
    state: absent
  tags:
  - CCE-86596-4
  - disable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - package_kea_removed
```
