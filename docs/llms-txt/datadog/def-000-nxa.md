# Source: https://docs.datadoghq.com/security/default_rules/def-000-nxa.md

---
title: Install iptables Package
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Install iptables Package
---

# Install iptables Package

## Description{% #description %}

The `iptables` package can be installed with the following command:

```

$ apt-get install iptables
```

## Rationale{% #rationale %}

`iptables` controls the Linux kernel network packet filtering code. `iptables` allows system operators to set up firewalls and IP masquerading, etc.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if ( ! (systemctl is-active nftables &>/dev/null) && ! (systemctl is-active ufw &>/dev/null) && dpkg-query --show --showformat='${db:Status-Status}' 'linux-base' 2>/dev/null | grep -q '^installed$' ); then

DEBIAN_FRONTEND=noninteractive apt-get install -y "iptables"

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
  - PCI-DSS-Req-1.4.1
  - enable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - package_iptables_installed

- name: Ensure iptables is installed
  package:
    name: iptables
    state: present
  when: ( "linux-base" in ansible_facts.packages )
  tags:
  - NIST-800-53-CM-6(a)
  - PCI-DSS-Req-1.4.1
  - enable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - package_iptables_installed
```
