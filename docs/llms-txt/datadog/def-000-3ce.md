# Source: https://docs.datadoghq.com/security/default_rules/def-000-3ce.md

---
title: Install libselinux Package
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Install libselinux Package
---

# Install libselinux Package

## Description{% #description %}

The `libselinux` package can be installed with the following command:

```

$ sudo yum install libselinux
```

## Rationale{% #rationale %}

Security-enhanced Linux is a feature of the Linux kernel and a number of utilities with enhanced security functionality designed to add mandatory access controls to Linux. The `libselinux` package contains the core library of the Security-enhanced Linux system.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if [ ! -f /.dockerenv ] && [ ! -f /run/.containerenv ]; then

if ! rpm -q --quiet "libselinux" ; then
    yum install -y "libselinux"
fi

else
    >&2 echo 'Remediation is not applicable, nothing was done'
fi
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```
- name: Ensure libselinux is installed
  package:
    name: libselinux
    state: present
  when: ansible_virtualization_type not in ["docker", "lxc", "openvz", "podman", "container"]
  tags:
  - CCE-82876-4
  - PCI-DSSv4-1.2.6
  - enable_strategy
  - high_severity
  - low_complexity
  - low_disruption
  - no_reboot_needed
  - package_libselinux_installed
```
