# Source: https://docs.datadoghq.com/security/default_rules/def-000-gyl.md

---
title: Install AIDE
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Install AIDE
---

# Install AIDE

## Description{% #description %}

The `aide` package can be installed with the following command:

```

$ apt-get install aide
```

## Rationale{% #rationale %}

The AIDE package must be installed if it is to be available for integrity checking.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'linux-base' 2>/dev/null | grep -q '^installed$'; then

DEBIAN_FRONTEND=noninteractive apt-get install -y "aide"

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
  - CJIS-5.10.1.3
  - DISA-STIG-UBTU-20-010450
  - NIST-800-53-CM-6(a)
  - PCI-DSS-Req-11.5
  - PCI-DSSv4-11.5.2
  - enable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - package_aide_installed

- name: Ensure aide is installed
  package:
    name: aide
    state: present
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - CJIS-5.10.1.3
  - DISA-STIG-UBTU-20-010450
  - NIST-800-53-CM-6(a)
  - PCI-DSS-Req-11.5
  - PCI-DSSv4-11.5.2
  - enable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - package_aide_installed
```
