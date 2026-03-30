# Source: https://docs.datadoghq.com/security/default_rules/def-000-sbs.md

---
title: Enable systemd-journald Service
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Enable systemd-journald Service
---

# Enable systemd-journald Service

## Description{% #description %}

The `systemd-journald` service is an essential component of systemd. The `systemd-journald` service can be enabled with the following command:

```
$ sudo systemctl enable systemd-journald.service
```

## Rationale{% #rationale %}

In the event of a system failure, Ubuntu 22.04 must preserve any information necessary to determine cause of failure and any information necessary to return to operations with least disruption to system processes.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'linux-base' 2>/dev/null | grep -q '^installed$'; then

SYSTEMCTL_EXEC='/usr/bin/systemctl'
"$SYSTEMCTL_EXEC" unmask 'systemd-journald.service'
if [[ $("$SYSTEMCTL_EXEC" is-system-running) != "offline" ]]; then
  "$SYSTEMCTL_EXEC" start 'systemd-journald.service'
fi
"$SYSTEMCTL_EXEC" enable 'systemd-journald.service'

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
  - NIST-800-53-SC-24
  - enable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - service_systemd-journald_enabled

- name: Enable systemd-journald Service - Enable service systemd-journald
  block:

  - name: Gather the package facts
    package_facts:
      manager: auto

  - name: Enable systemd-journald Service - Enable Service systemd-journald
    ansible.builtin.systemd:
      name: systemd-journald
      enabled: true
      state: started
      masked: false
    when:
    - '"systemd" in ansible_facts.packages'
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - NIST-800-53-SC-24
  - enable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - service_systemd-journald_enabled
```
