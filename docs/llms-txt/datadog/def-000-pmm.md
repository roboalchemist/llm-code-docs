# Source: https://docs.datadoghq.com/security/default_rules/def-000-pmm.md

---
title: Ensure rsyslog is Installed
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Ensure rsyslog is Installed
---

# Ensure rsyslog is Installed
 
## Description{% #description %}

Rsyslog is installed by default. The `rsyslog` package can be installed with the following command:

```
 $ apt-get install rsyslog
```

## Rationale{% #rationale %}

The rsyslog package provides the rsyslog daemon, which provides system logging services.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'linux-base' 2>/dev/null | grep -q '^installed$'; then

DEBIAN_FRONTEND=noninteractive apt-get install -y "rsyslog"

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
  - enable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - package_rsyslog_installed

- name: Ensure rsyslog is installed
  package:
    name: rsyslog
    state: present
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - NIST-800-53-CM-6(a)
  - enable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - package_rsyslog_installed
```
