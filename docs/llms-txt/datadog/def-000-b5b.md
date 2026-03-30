# Source: https://docs.datadoghq.com/security/default_rules/def-000-b5b.md

---
title: Enable rsyslog Service
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Enable rsyslog Service
---

# Enable rsyslog Service

## Description{% #description %}

The `rsyslog` service provides syslog-style logging by default on Ubuntu 20.04. The `rsyslog` service can be enabled with the following command:

```
$ sudo systemctl enable rsyslog.service
```

## Rationale{% #rationale %}

The `rsyslog` service must be running in order to provide logging services, which are essential to system administration.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'linux-base' 2>/dev/null | grep -q '^installed$'; then

SYSTEMCTL_EXEC='/usr/bin/systemctl'
"$SYSTEMCTL_EXEC" unmask 'rsyslog.service'
if [[ $("$SYSTEMCTL_EXEC" is-system-running) != "offline" ]]; then
  "$SYSTEMCTL_EXEC" start 'rsyslog.service'
fi
"$SYSTEMCTL_EXEC" enable 'rsyslog.service'

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
  - DISA-STIG-UBTU-20-010432
  - NIST-800-53-AU-4(1)
  - NIST-800-53-CM-6(a)
  - enable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - service_rsyslog_enabled

- name: Enable rsyslog Service - Enable service rsyslog
  block:

  - name: Gather the package facts
    package_facts:
      manager: auto

  - name: Enable rsyslog Service - Enable Service rsyslog
    ansible.builtin.systemd:
      name: rsyslog
      enabled: true
      state: started
      masked: false
    when:
    - '"rsyslog" in ansible_facts.packages'
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - DISA-STIG-UBTU-20-010432
  - NIST-800-53-AU-4(1)
  - NIST-800-53-CM-6(a)
  - enable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - service_rsyslog_enabled
```
