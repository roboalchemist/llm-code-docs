# Source: https://docs.datadoghq.com/security/default_rules/def-000-yvz.md

---
title: Uninstall the nis package
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Uninstall the nis package
---

# Uninstall the nis package
 
## Description{% #description %}

The support for Yellowpages should not be installed unless it is required.

## Rationale{% #rationale %}

NIS is the historical SUN service for central account management, more and more replaced by LDAP. NIS does not support efficiently security constraints, ACL, etc. and should not be used.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# CAUTION: This remediation script will remove nis
# from the system, and may remove any packages
# that depend on nis. Execute this
# remediation AFTER testing on a non-production
# system!


DEBIAN_FRONTEND=noninteractive apt-get remove -y "nis"
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```
- name: 'Uninstall the nis package: Ensure nis is removed'
  ansible.builtin.package:
    name: nis
    state: absent
  tags:
  - disable_strategy
  - low_complexity
  - low_disruption
  - low_severity
  - no_reboot_needed
  - package_nis_removed
```
