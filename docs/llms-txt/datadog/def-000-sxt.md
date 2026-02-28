# Source: https://docs.datadoghq.com/security/default_rules/def-000-sxt.md

---
title: Remove the GDM Package Group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Remove the GDM Package Group
---

# Remove the GDM Package Group

## Description{% #description %}

By removing the `gdm3` package, the system no longer has GNOME installed installed. If X Windows is not installed then the system cannot boot into graphical user mode. This prevents the system from being accidentally or maliciously booted into a `graphical.target` mode. To do so, run the following command:

```
$ sudo apt remove gdm3
```

## Rationale{% #rationale %}

Unnecessary service packages must not be installed to decrease the attack surface of the system. A graphical environment is unnecessary for certain types of systems including a virtualization hypervisor.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'gdm3' 2>/dev/null | grep -q '^installed$'; then

# CAUTION: This remediation script will remove gdm3
# from the system, and may remove any packages
# that depend on gdm3. Execute this
# remediation AFTER testing on a non-production
# system!


DEBIAN_FRONTEND=noninteractive apt-get remove -y "gdm3"

else
    >&2 echo 'Remediation is not applicable, nothing was done'
fi
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```go
- name: Gather the package facts
  package_facts:
    manager: auto
  tags:
  - NIST-800-53-CM-6(a)
  - NIST-800-53-CM-7(a)
  - NIST-800-53-CM-7(b)
  - disable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - package_gdm_removed

- name: 'Remove the GDM Package Group: Ensure gdm3 is removed'
  ansible.builtin.package:
    name: gdm3
    state: absent
  when: '"gdm3" in ansible_facts.packages'
  tags:
  - NIST-800-53-CM-6(a)
  - NIST-800-53-CM-7(a)
  - NIST-800-53-CM-7(b)
  - disable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - package_gdm_removed
```
