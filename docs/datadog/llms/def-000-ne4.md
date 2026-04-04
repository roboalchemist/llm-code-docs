# Source: https://docs.datadoghq.com/security/default_rules/def-000-ne4.md

---
title: Install nftables Package
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Install nftables Package
---

# Install nftables Package

## Description{% #description %}

nftables provides a new in-kernel packet classification framework that is based on a network-specific Virtual Machine (VM) and a new nft userspace command line tool. nftables reuses the existing Netfilter subsystems such as the existing hook infrastructure, the connection tracking system, NAT, userspace queuing and logging subsystem. The `nftables` package can be installed with the following command:

```

$ apt-get install nftables
```

## Rationale{% #rationale %}

`nftables` is a subsystem of the Linux kernel that can protect against threats originating from within a corporate network to include malicious mobile code and poorly configured software on a host.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if ( ! (systemctl is-active iptables &>/dev/null) && ! (systemctl is-active ufw &>/dev/null) && dpkg-query --show --showformat='${db:Status-Status}' 'linux-base' 2>/dev/null | grep -q '^installed$' ); then

DEBIAN_FRONTEND=noninteractive apt-get install -y "nftables"

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
  - PCI-DSSv4-1.2
  - PCI-DSSv4-1.2.1
  - enable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - package_nftables_installed

- name: Ensure nftables is installed
  package:
    name: nftables
    state: present
  when: ( "linux-base" in ansible_facts.packages )
  tags:
  - PCI-DSSv4-1.2
  - PCI-DSSv4-1.2.1
  - enable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - package_nftables_installed
```
