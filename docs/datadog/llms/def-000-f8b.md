# Source: https://docs.datadoghq.com/security/default_rules/def-000-f8b.md

---
title: Disable ypserv Service
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Disable ypserv Service
---

# Disable ypserv Service

## Description{% #description %}

The `ypserv` service, which allows the system to act as a client in a NIS or NIS+ domain, should be disabled. The `ypserv` service can be disabled with the following command:

```
$ sudo systemctl mask --now ypserv.service
```

## Rationale{% #rationale %}

Disabling the `ypserv` service ensures the system is not acting as a client in a NIS or NIS+ domain. This service should be disabled unless in use.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'linux-base' 2>/dev/null | grep -q '^installed$'; then

SYSTEMCTL_EXEC='/usr/bin/systemctl'
if [[ $("$SYSTEMCTL_EXEC" is-system-running) != "offline" ]]; then
  "$SYSTEMCTL_EXEC" stop 'ypserv.service'
fi
"$SYSTEMCTL_EXEC" disable 'ypserv.service'
"$SYSTEMCTL_EXEC" mask 'ypserv.service'
# Disable socket activation if we have a unit file for it
if "$SYSTEMCTL_EXEC" -q list-unit-files ypserv.socket; then
    if [[ $("$SYSTEMCTL_EXEC" is-system-running) != "offline" ]]; then
      "$SYSTEMCTL_EXEC" stop 'ypserv.socket'
    fi
    "$SYSTEMCTL_EXEC" mask 'ypserv.socket'
fi
# The service may not be running because it has been started and failed,
# so let's reset the state so OVAL checks pass.
# Service should be 'inactive', not 'failed' after reboot though.
"$SYSTEMCTL_EXEC" reset-failed 'ypserv.service' || true

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
  - disable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - service_ypserv_disabled

- name: Disable ypserv Service - Collect systemd Services Present in the System
  ansible.builtin.command: systemctl -q list-unit-files --type service
  register: service_exists
  changed_when: false
  failed_when: service_exists.rc not in [0, 1]
  check_mode: false
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - disable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - service_ypserv_disabled

- name: Disable ypserv Service - Ensure ypserv.service is Masked
  ansible.builtin.systemd:
    name: ypserv.service
    state: stopped
    enabled: false
    masked: true
  when:
  - '"linux-base" in ansible_facts.packages'
  - service_exists.stdout_lines is search("ypserv.service", multiline=True)
  tags:
  - disable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - service_ypserv_disabled

- name: Unit Socket Exists - ypserv.socket
  ansible.builtin.command: systemctl -q list-unit-files ypserv.socket
  register: socket_file_exists
  changed_when: false
  failed_when: socket_file_exists.rc not in [0, 1]
  check_mode: false
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - disable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - service_ypserv_disabled

- name: Disable ypserv Service - Disable Socket ypserv
  ansible.builtin.systemd:
    name: ypserv.socket
    enabled: false
    state: stopped
    masked: true
  when:
  - '"linux-base" in ansible_facts.packages'
  - socket_file_exists.stdout_lines is search("ypserv.socket", multiline=True)
  tags:
  - disable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - service_ypserv_disabled
```
