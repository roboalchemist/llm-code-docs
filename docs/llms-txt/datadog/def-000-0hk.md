# Source: https://docs.datadoghq.com/security/default_rules/def-000-0hk.md

---
title: Uninstall nftables package
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Uninstall nftables package
---

# Uninstall nftables package

## Description{% #description %}

nftables is a subsystem of the Linux kernel providing filtering and classification of network packets/datagrams/frames and is the successor to iptables. The `nftables` package can be removed with the following command:

```

$ apt-get remove nftables
```

## Rationale{% #rationale %}

Running both `firewalld` and `nftables` may lead to conflict.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# CAUTION: This remediation script will remove nftables
# from the system, and may remove any packages
# that depend on nftables. Execute this
# remediation AFTER testing on a non-production
# system!


DEBIAN_FRONTEND=noninteractive apt-get remove -y "nftables"
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```
- name: 'Uninstall nftables package: Ensure nftables is removed'
  ansible.builtin.package:
    name: nftables
    state: absent
  tags:
  - disable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - package_nftables_removed
```
