# Source: https://docs.datadoghq.com/security/default_rules/def-000-3fs.md

---
title: The Chrony package is installed
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > The Chrony package is installed
---

# The Chrony package is installed

## Description{% #description %}

System time should be synchronized between all systems in an environment. This is typically done by establishing an authoritative time server or set of servers and having all systems synchronize their clocks to them. The `chrony` package can be installed with the following command:

```

$ apt-get install chrony
```

## Rationale{% #rationale %}

Time synchronization is important to support time sensitive security mechanisms like Kerberos and also ensures log files have consistent time records across the enterprise, which aids in forensic investigations.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'linux-base' 2>/dev/null | grep -q '^installed$'; then

DEBIAN_FRONTEND=noninteractive apt-get install -y "chrony"

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
  - DISA-STIG-UBTU-20-010435
  - PCI-DSS-Req-10.4
  - PCI-DSSv4-10.6
  - PCI-DSSv4-10.6.1
  - enable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - package_chrony_installed

- name: Ensure chrony is installed
  package:
    name: chrony
    state: present
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - DISA-STIG-UBTU-20-010435
  - PCI-DSS-Req-10.4
  - PCI-DSSv4-10.6
  - PCI-DSSv4-10.6.1
  - enable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - package_chrony_installed
```
