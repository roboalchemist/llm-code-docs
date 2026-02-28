# Source: https://docs.datadoghq.com/security/default_rules/def-000-z5a.md

---
title: Disable Dovecot Service
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Disable Dovecot Service
---

# Disable Dovecot Service

## Description{% #description %}

The `dovecot` service can be disabled with the following command:

```
$ sudo systemctl mask --now dovecot.service
```

## Rationale{% #rationale %}

Running an IMAP or POP3 server provides a network-based avenue of attack, and should be disabled if not needed.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'linux-base' 2>/dev/null | grep -q '^installed$'; then

SYSTEMCTL_EXEC='/usr/bin/systemctl'
if [[ $("$SYSTEMCTL_EXEC" is-system-running) != "offline" ]]; then
  "$SYSTEMCTL_EXEC" stop 'dovecot.service'
fi
"$SYSTEMCTL_EXEC" disable 'dovecot.service'
"$SYSTEMCTL_EXEC" mask 'dovecot.service'
# Disable socket activation if we have a unit file for it
if "$SYSTEMCTL_EXEC" -q list-unit-files dovecot.socket; then
    if [[ $("$SYSTEMCTL_EXEC" is-system-running) != "offline" ]]; then
      "$SYSTEMCTL_EXEC" stop 'dovecot.socket'
    fi
    "$SYSTEMCTL_EXEC" mask 'dovecot.socket'
fi
# The service may not be running because it has been started and failed,
# so let's reset the state so OVAL checks pass.
# Service should be 'inactive', not 'failed' after reboot though.
"$SYSTEMCTL_EXEC" reset-failed 'dovecot.service' || true

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
  - service_dovecot_disabled
  - unknown_severity

- name: Disable Dovecot Service - Collect systemd Services Present in the System
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
  - no_reboot_needed
  - service_dovecot_disabled
  - unknown_severity

- name: Disable Dovecot Service - Ensure dovecot.service is Masked
  ansible.builtin.systemd:
    name: dovecot.service
    state: stopped
    enabled: false
    masked: true
  when:
  - '"linux-base" in ansible_facts.packages'
  - service_exists.stdout_lines is search("dovecot.service", multiline=True)
  tags:
  - disable_strategy
  - low_complexity
  - low_disruption
  - no_reboot_needed
  - service_dovecot_disabled
  - unknown_severity

- name: Unit Socket Exists - dovecot.socket
  ansible.builtin.command: systemctl -q list-unit-files dovecot.socket
  register: socket_file_exists
  changed_when: false
  failed_when: socket_file_exists.rc not in [0, 1]
  check_mode: false
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - disable_strategy
  - low_complexity
  - low_disruption
  - no_reboot_needed
  - service_dovecot_disabled
  - unknown_severity

- name: Disable Dovecot Service - Disable Socket dovecot
  ansible.builtin.systemd:
    name: dovecot.socket
    enabled: false
    state: stopped
    masked: true
  when:
  - '"linux-base" in ansible_facts.packages'
  - socket_file_exists.stdout_lines is search("dovecot.socket", multiline=True)
  tags:
  - disable_strategy
  - low_complexity
  - low_disruption
  - no_reboot_needed
  - service_dovecot_disabled
  - unknown_severity
```
