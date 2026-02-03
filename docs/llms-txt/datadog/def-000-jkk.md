# Source: https://docs.datadoghq.com/security/default_rules/def-000-jkk.md

---
title: Disable Bluetooth Service
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Disable Bluetooth Service
---

# Disable Bluetooth Service
 
## Description{% #description %}

The `bluetooth` service can be disabled with the following command:

```
$ sudo systemctl mask --now bluetooth.service
```

```
$ sudo service bluetooth stop
```

## Rationale{% #rationale %}

Disabling the `bluetooth` service prevents the system from attempting connections to Bluetooth devices, which entails some security risk. Nevertheless, variation in this risk decision may be expected due to the utility of Bluetooth connectivity and its limited range.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'linux-base' 2>/dev/null | grep -q '^installed$'; then

SYSTEMCTL_EXEC='/usr/bin/systemctl'
if [[ $("$SYSTEMCTL_EXEC" is-system-running) != "offline" ]]; then
  "$SYSTEMCTL_EXEC" stop 'bluetooth.service'
fi
"$SYSTEMCTL_EXEC" disable 'bluetooth.service'
"$SYSTEMCTL_EXEC" mask 'bluetooth.service'
# Disable socket activation if we have a unit file for it
if "$SYSTEMCTL_EXEC" -q list-unit-files bluetooth.socket; then
    if [[ $("$SYSTEMCTL_EXEC" is-system-running) != "offline" ]]; then
      "$SYSTEMCTL_EXEC" stop 'bluetooth.socket'
    fi
    "$SYSTEMCTL_EXEC" mask 'bluetooth.socket'
fi
# The service may not be running because it has been started and failed,
# so let's reset the state so OVAL checks pass.
# Service should be 'inactive', not 'failed' after reboot though.
"$SYSTEMCTL_EXEC" reset-failed 'bluetooth.service' || true

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
  - NIST-800-171-3.1.16
  - NIST-800-53-AC-18(3)
  - NIST-800-53-AC-18(a)
  - NIST-800-53-CM-6(a)
  - NIST-800-53-CM-7(a)
  - NIST-800-53-CM-7(b)
  - NIST-800-53-MP-7
  - disable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - service_bluetooth_disabled

- name: Disable Bluetooth Service - Collect systemd Services Present in the System
  ansible.builtin.command: systemctl -q list-unit-files --type service
  register: service_exists
  changed_when: false
  failed_when: service_exists.rc not in [0, 1]
  check_mode: false
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - NIST-800-171-3.1.16
  - NIST-800-53-AC-18(3)
  - NIST-800-53-AC-18(a)
  - NIST-800-53-CM-6(a)
  - NIST-800-53-CM-7(a)
  - NIST-800-53-CM-7(b)
  - NIST-800-53-MP-7
  - disable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - service_bluetooth_disabled

- name: Disable Bluetooth Service - Ensure bluetooth.service is Masked
  ansible.builtin.systemd:
    name: bluetooth.service
    state: stopped
    enabled: false
    masked: true
  when:
  - '"linux-base" in ansible_facts.packages'
  - service_exists.stdout_lines is search("bluetooth.service", multiline=True)
  tags:
  - NIST-800-171-3.1.16
  - NIST-800-53-AC-18(3)
  - NIST-800-53-AC-18(a)
  - NIST-800-53-CM-6(a)
  - NIST-800-53-CM-7(a)
  - NIST-800-53-CM-7(b)
  - NIST-800-53-MP-7
  - disable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - service_bluetooth_disabled

- name: Unit Socket Exists - bluetooth.socket
  ansible.builtin.command: systemctl -q list-unit-files bluetooth.socket
  register: socket_file_exists
  changed_when: false
  failed_when: socket_file_exists.rc not in [0, 1]
  check_mode: false
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - NIST-800-171-3.1.16
  - NIST-800-53-AC-18(3)
  - NIST-800-53-AC-18(a)
  - NIST-800-53-CM-6(a)
  - NIST-800-53-CM-7(a)
  - NIST-800-53-CM-7(b)
  - NIST-800-53-MP-7
  - disable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - service_bluetooth_disabled

- name: Disable Bluetooth Service - Disable Socket bluetooth
  ansible.builtin.systemd:
    name: bluetooth.socket
    enabled: false
    state: stopped
    masked: true
  when:
  - '"linux-base" in ansible_facts.packages'
  - socket_file_exists.stdout_lines is search("bluetooth.socket", multiline=True)
  tags:
  - NIST-800-171-3.1.16
  - NIST-800-53-AC-18(3)
  - NIST-800-53-AC-18(a)
  - NIST-800-53-CM-6(a)
  - NIST-800-53-CM-7(a)
  - NIST-800-53-CM-7(b)
  - NIST-800-53-MP-7
  - disable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - service_bluetooth_disabled
```
