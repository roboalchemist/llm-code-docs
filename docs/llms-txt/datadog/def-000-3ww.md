# Source: https://docs.datadoghq.com/security/default_rules/def-000-3ww.md

---
title: Disable Apport Service
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Disable Apport Service
---

# Disable Apport Service

## Description{% #description %}

The Apport modifies certain kernel configuration values at runtime which may decrease the overall security of the system and expose sensitive data. The `apport` service can be disabled with the following command:

```
$ sudo systemctl mask --now apport.service
```

## Rationale{% #rationale %}

The Apport service modifies the kernel `fs.suid_dumpable` configuration at runtime which prevents other hardening from being persistent. Disabling the service prevents this behavior.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'apport' 2>/dev/null | grep -q '^installed$'; then

SYSTEMCTL_EXEC='/usr/bin/systemctl'
if [[ $("$SYSTEMCTL_EXEC" is-system-running) != "offline" ]]; then
  "$SYSTEMCTL_EXEC" stop 'apport.service'
fi
"$SYSTEMCTL_EXEC" disable 'apport.service'
"$SYSTEMCTL_EXEC" mask 'apport.service'
# Disable socket activation if we have a unit file for it
if "$SYSTEMCTL_EXEC" -q list-unit-files apport.socket; then
    if [[ $("$SYSTEMCTL_EXEC" is-system-running) != "offline" ]]; then
      "$SYSTEMCTL_EXEC" stop 'apport.socket'
    fi
    "$SYSTEMCTL_EXEC" mask 'apport.socket'
fi
# The service may not be running because it has been started and failed,
# so let's reset the state so OVAL checks pass.
# Service should be 'inactive', not 'failed' after reboot though.
"$SYSTEMCTL_EXEC" reset-failed 'apport.service' || true

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
  - no_reboot_needed
  - service_apport_disabled
  - unknown_severity

- name: Disable Apport Service - Collect systemd Services Present in the System
  ansible.builtin.command: systemctl -q list-unit-files --type service
  register: service_exists
  changed_when: false
  failed_when: service_exists.rc not in [0, 1]
  check_mode: false
  when: '"apport" in ansible_facts.packages'
  tags:
  - disable_strategy
  - low_complexity
  - low_disruption
  - no_reboot_needed
  - service_apport_disabled
  - unknown_severity

- name: Disable Apport Service - Ensure apport.service is Masked
  ansible.builtin.systemd:
    name: apport.service
    state: stopped
    enabled: false
    masked: true
  when:
  - '"apport" in ansible_facts.packages'
  - service_exists.stdout_lines is search("apport.service", multiline=True)
  tags:
  - disable_strategy
  - low_complexity
  - low_disruption
  - no_reboot_needed
  - service_apport_disabled
  - unknown_severity

- name: Unit Socket Exists - apport.socket
  ansible.builtin.command: systemctl -q list-unit-files apport.socket
  register: socket_file_exists
  changed_when: false
  failed_when: socket_file_exists.rc not in [0, 1]
  check_mode: false
  when: '"apport" in ansible_facts.packages'
  tags:
  - disable_strategy
  - low_complexity
  - low_disruption
  - no_reboot_needed
  - service_apport_disabled
  - unknown_severity

- name: Disable Apport Service - Disable Socket apport
  ansible.builtin.systemd:
    name: apport.socket
    enabled: false
    state: stopped
    masked: true
  when:
  - '"apport" in ansible_facts.packages'
  - socket_file_exists.stdout_lines is search("apport.socket", multiline=True)
  tags:
  - disable_strategy
  - low_complexity
  - low_disruption
  - no_reboot_needed
  - service_apport_disabled
  - unknown_severity
```
