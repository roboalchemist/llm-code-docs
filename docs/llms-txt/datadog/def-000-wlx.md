# Source: https://docs.datadoghq.com/security/default_rules/def-000-wlx.md

---
title: Remove the X Windows Package Group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Remove the X Windows Package Group
---

# Remove the X Windows Package Group

## Description{% #description %}

By removing the xorg-x11-server-common package, the system no longer has X Windows installed. If X Windows is not installed then the system cannot boot into graphical user mode. This prevents the system from being accidentally or maliciously booted into a `graphical.target` mode. To do so, run the following command:

```
$ sudo apt_get groupremove "X Window System"
```

```
$ sudo apt_get remove xorg-x11-server-common
```

## Rationale{% #rationale %}

Unnecessary service packages must not be installed to decrease the attack surface of the system. X windows has a long history of security vulnerabilities and should not be installed unless approved and documented.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# CAUTION: This remediation script will remove xserver-xorg
# from the system, and may remove any packages
# that depend on xserver-xorg. Execute this
# remediation AFTER testing on a non-production
# system!


DEBIAN_FRONTEND=noninteractive apt-get remove -y "xserver-xorg"
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```
- name: 'Remove the X Windows Package Group: Ensure xserver-xorg is removed'
  ansible.builtin.package:
    name: xserver-xorg
    state: absent
  tags:
  - NIST-800-53-CM-6(a)
  - NIST-800-53-CM-7(a)
  - NIST-800-53-CM-7(b)
  - disable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - package_xorg-x11-server-common_removed
```

## Warning{% #warning %}

The installation and use of a Graphical User Interface (GUI) increases your attack vector and decreases your overall security posture. Removing the package xorg-x11-server-common package will remove the graphical target which might bring your system to an inconsistent state requiring additional configuration to access the system again. If a GUI is an operational requirement, a tailored profile that removes this rule should used before continuing installation.
