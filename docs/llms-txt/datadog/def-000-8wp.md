# Source: https://docs.datadoghq.com/security/default_rules/def-000-8wp.md

---
title: Install pam-runtime Package
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Install pam-runtime Package
---

# Install pam-runtime Package
 
## Description{% #description %}

The `libpam-runtime` package can be installed with the following command:

```

$ apt-get install libpam-runtime
```

## Rationale{% #rationale %}

libpam-runtime contains configuration that is needed by other rules when configuring PAM options.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

DEBIAN_FRONTEND=noninteractive apt-get install -y "libpam-runtime"
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```
- name: Ensure libpam-runtime is installed
  package:
    name: libpam-runtime
    state: present
  tags:
  - enable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - package_pam_runtime_installed
```
