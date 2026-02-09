# Source: https://docs.datadoghq.com/security/default_rules/def-000-zrr.md

---
title: Install pam_pwquality Package
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Install pam_pwquality Package
---

# Install pam_pwquality Package
 
## Description{% #description %}

The `libpam-pwquality` package can be installed with the following command:

```

$ apt-get install libpam-pwquality
```

## Rationale{% #rationale %}

Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. "pwquality" enforces complex password construction configuration and has the ability to limit brute-force attacks on the system.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'libpam-runtime' 2>/dev/null | grep -q '^installed$'; then

DEBIAN_FRONTEND=noninteractive apt-get install -y "libpam-pwquality"

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
  - DISA-STIG-UBTU-20-010057
  - enable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - package_pam_pwquality_installed

- name: Ensure libpam-pwquality is installed
  package:
    name: libpam-pwquality
    state: present
  when: '"libpam-runtime" in ansible_facts.packages'
  tags:
  - DISA-STIG-UBTU-20-010057
  - enable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - package_pam_pwquality_installed
```
