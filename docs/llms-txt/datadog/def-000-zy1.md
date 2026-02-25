# Source: https://docs.datadoghq.com/security/default_rules/def-000-zy1.md

---
title: Install sudo Package
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Install sudo Package
---

# Install sudo Package

## Description{% #description %}

The `sudo` package can be installed with the following command:

```

$ apt-get install sudo
```

## Rationale{% #rationale %}

`sudo` is a program designed to allow a system administrator to give limited root privileges to users and log root activity. The basic philosophy is to give as few privileges as possible but still allow system users to get their work done.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'linux-base' 2>/dev/null | grep -q '^installed$'; then

DEBIAN_FRONTEND=noninteractive apt-get install -y "sudo"

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
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.6
  - enable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - package_sudo_installed

- name: Ensure sudo is installed
  package:
    name: sudo
    state: present
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - NIST-800-53-CM-6(a)
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.6
  - enable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - package_sudo_installed
```
