# Source: https://docs.datadoghq.com/security/default_rules/def-000-vrd.md

---
title: Uninstall CUPS Package
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Uninstall CUPS Package
---

# Uninstall CUPS Package

## Description{% #description %}

The `cups` package can be removed with the following command:

```

$ apt-get remove cups
```

## Rationale{% #rationale %}

If the system does not need to print jobs or accept print jobs from other systems, it is recommended that CUPS be removed to reduce the potential attack surface.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# CAUTION: This remediation script will remove cups
# from the system, and may remove any packages
# that depend on cups. Execute this
# remediation AFTER testing on a non-production
# system!


DEBIAN_FRONTEND=noninteractive apt-get remove -y "cups"
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```
- name: 'Uninstall CUPS Package: Ensure cups is removed'
  ansible.builtin.package:
    name: cups
    state: absent
  tags:
  - NIST-800-53-CM-6(a)
  - NIST-800-53-CM-7(a)
  - NIST-800-53-CM-7(b)
  - disable_strategy
  - low_complexity
  - low_disruption
  - no_reboot_needed
  - package_cups_removed
  - unknown_severity
```
