# Source: https://docs.datadoghq.com/security/default_rules/def-000-mlz.md

---
title: Ensure AppArmor Utils is installed
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Ensure AppArmor Utils is installed
---

# Ensure AppArmor Utils is installed
 
## Description{% #description %}

AppArmor provide Mandatory Access Controls.

## Rationale{% #rationale %}

Without a Mandatory Access Control system installed only the default Discretionary Access Control system will be available.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if [ ! -f /.dockerenv ] && [ ! -f /run/.containerenv ]; then

DEBIAN_FRONTEND=noninteractive apt-get install -y "apparmor-utils"

else
    >&2 echo 'Remediation is not applicable, nothing was done'
fi
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```
- name: Ensure apparmor-utils is installed
  package:
    name: apparmor-utils
    state: present
  when: ansible_virtualization_type not in ["docker", "lxc", "openvz", "podman", "container"]
  tags:
  - enable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - package_apparmor-utils_installed
```
