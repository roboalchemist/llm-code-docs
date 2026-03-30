# Source: https://docs.datadoghq.com/security/default_rules/def-000-f1n.md

---
title: Enable cron Service
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Enable cron Service
---

# Enable cron Service

## Description{% #description %}

The `crond` service is used to execute commands at preconfigured times. It is required by almost all systems to perform necessary maintenance tasks, such as notifying root of system activity. The `cron` service can be enabled with the following command:

```
$ sudo systemctl enable cron.service
```

## Rationale{% #rationale %}

Due to its usage for maintenance and security-supporting tasks, enabling the cron daemon is essential.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'linux-base' 2>/dev/null | grep -q '^installed$'; then

SYSTEMCTL_EXEC='/usr/bin/systemctl'
"$SYSTEMCTL_EXEC" unmask 'cron.service'
if [[ $("$SYSTEMCTL_EXEC" is-system-running) != "offline" ]]; then
  "$SYSTEMCTL_EXEC" start 'cron.service'
fi
"$SYSTEMCTL_EXEC" enable 'cron.service'

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
  - service_cron_enabled

- name: Enable cron Service - Enable service cron
  block:

  - name: Gather the package facts
    package_facts:
      manager: auto

  - name: Enable cron Service - Enable Service cron
    ansible.builtin.systemd:
      name: cron
      enabled: true
      state: started
      masked: false
    when:
    - '"cron" in ansible_facts.packages'
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - NIST-800-53-CM-6(a)
  - enable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - service_cron_enabled
```
