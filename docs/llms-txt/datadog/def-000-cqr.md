# Source: https://docs.datadoghq.com/security/default_rules/def-000-cqr.md

---
title: Install iptables-persistent Package
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Install iptables-persistent Package
---

# Install iptables-persistent Package

## Description{% #description %}

The `iptables-persistent` package can be installed with the following command:

```

$ apt-get install iptables-persistent
```

## Rationale{% #rationale %}

A method of configuring and maintaining firewall rules is necessary to configure a Host Based Firewall.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'iptables' 2>/dev/null | grep -q '^installed$'; then

DEBIAN_FRONTEND=noninteractive apt-get install -y "iptables-persistent"

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
  - enable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - package_iptables-persistent_installed

- name: Ensure iptables-persistent is installed
  package:
    name: iptables-persistent
    state: present
  when: '"iptables" in ansible_facts.packages'
  tags:
  - enable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - package_iptables-persistent_installed
```
