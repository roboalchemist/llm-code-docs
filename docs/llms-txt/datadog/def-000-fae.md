# Source: https://docs.datadoghq.com/security/default_rules/def-000-fae.md

---
title: Install the cron service
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Install the cron service
---

# Install the cron service
 
## Description{% #description %}

The Cron service should be installed.

## Rationale{% #rationale %}

The cron service allow periodic job execution, needed for almost all administrative tasks and services (software update, log rotating, etc.). Access to cron service should be restricted to administrative accounts only.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'linux-base' 2>/dev/null | grep -q '^installed$'; then

DEBIAN_FRONTEND=noninteractive apt-get install -y "cron"

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
  - package_cron_installed

- name: Ensure cron is installed
  package:
    name: cron
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
  - package_cron_installed
```
