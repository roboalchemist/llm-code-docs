# Source: https://docs.datadoghq.com/security/default_rules/def-000-xkq.md

---
title: Install ufw Package
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Install ufw Package
---

# Install ufw Package

## Description{% #description %}

The `ufw` package can be installed with the following command:

```

$ apt-get install ufw
```

## Rationale{% #rationale %}

`ufw` controls the Linux kernel network packet filtering code. `ufw` allows system operators to set up firewalls and IP masquerading, etc.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'linux-base' 2>/dev/null | grep -q '^installed$'; then

DEBIAN_FRONTEND=noninteractive apt-get install -y "ufw"

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
  - DISA-STIG-UBTU-20-010433
  - enable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - package_ufw_installed

- name: Ensure ufw is installed
  package:
    name: ufw
    state: present
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - DISA-STIG-UBTU-20-010433
  - enable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - package_ufw_installed
```
