# Source: https://docs.datadoghq.com/security/default_rules/def-000-ibe.md

---
title: Install pam-modules Package
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Install pam-modules Package
---

# Install pam-modules Package

## Description{% #description %}

The `libpam-modules` package can be installed with the following command:

```

$ apt-get install libpam-modules
```

## Rationale{% #rationale %}

libpam-modules contains PAM modules that are needed by other rules when configuring PAM options.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'libpam-runtime' 2>/dev/null | grep -q '^installed$'; then

DEBIAN_FRONTEND=noninteractive apt-get install -y "libpam-modules"

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
  - package_pam_modules_installed

- name: Ensure libpam-modules is installed
  package:
    name: libpam-modules
    state: present
  when: '"libpam-runtime" in ansible_facts.packages'
  tags:
  - enable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - package_pam_modules_installed
```
