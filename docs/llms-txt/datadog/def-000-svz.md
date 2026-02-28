# Source: https://docs.datadoghq.com/security/default_rules/def-000-svz.md

---
title: Remove iptables-persistent Package
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Remove iptables-persistent Package
---

# Remove iptables-persistent Package

## Description{% #description %}

The `iptables-persistent` package can be removed with the following command:

```

$ apt-get remove iptables-persistent
```

## Rationale{% #rationale %}

Running both `ufw` and the services included in the `iptables-persistent` package may lead to conflict.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'ufw' 2>/dev/null | grep -q '^installed$'; then

# CAUTION: This remediation script will remove iptables-persistent
# from the system, and may remove any packages
# that depend on iptables-persistent. Execute this
# remediation AFTER testing on a non-production
# system!


DEBIAN_FRONTEND=noninteractive apt-get remove -y "iptables-persistent"

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
  - disable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - package_iptables-persistent_removed

- name: 'Remove iptables-persistent Package: Ensure iptables-persistent is removed'
  ansible.builtin.package:
    name: iptables-persistent
    state: absent
  when: '"ufw" in ansible_facts.packages'
  tags:
  - disable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - package_iptables-persistent_removed
```
