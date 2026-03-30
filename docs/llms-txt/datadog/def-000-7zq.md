# Source: https://docs.datadoghq.com/security/default_rules/def-000-7zq.md

---
title: Disable DHCPD6 Service
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Disable DHCPD6 Service
---

# Disable DHCPD6 Service

## Description{% #description %}

The `dhcp6` service should be disabled on any system that does not need to act as a DHCP server. The `isc-dhcp-server6` service can be disabled with the following command:

```
$ sudo systemctl mask --now isc-dhcp-server6.service
```

## Rationale{% #rationale %}

Unmanaged or unintentionally activated DHCP servers may provide faulty information to clients, interfering with the operation of a legitimate site DHCP server if there is one.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'linux-base' 2>/dev/null | grep -q '^installed$'; then

SYSTEMCTL_EXEC='/usr/bin/systemctl'
if [[ $("$SYSTEMCTL_EXEC" is-system-running) != "offline" ]]; then
  "$SYSTEMCTL_EXEC" stop 'isc-dhcp-server6.service'
fi
"$SYSTEMCTL_EXEC" disable 'isc-dhcp-server6.service'
"$SYSTEMCTL_EXEC" mask 'isc-dhcp-server6.service'
# Disable socket activation if we have a unit file for it
if "$SYSTEMCTL_EXEC" -q list-unit-files isc-dhcp-server6.socket; then
    if [[ $("$SYSTEMCTL_EXEC" is-system-running) != "offline" ]]; then
      "$SYSTEMCTL_EXEC" stop 'isc-dhcp-server6.socket'
    fi
    "$SYSTEMCTL_EXEC" mask 'isc-dhcp-server6.socket'
fi
# The service may not be running because it has been started and failed,
# so let's reset the state so OVAL checks pass.
# Service should be 'inactive', not 'failed' after reboot though.
"$SYSTEMCTL_EXEC" reset-failed 'isc-dhcp-server6.service' || true

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
  - service_dhcpd6_disabled

- name: Disable DHCPD6 Service - Collect systemd Services Present in the System
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
  - service_dhcpd6_disabled

- name: Disable DHCPD6 Service - Ensure isc-dhcp-server6.service is Masked
  ansible.builtin.systemd:
    name: isc-dhcp-server6.service
    state: stopped
    enabled: false
    masked: true
  when:
  - '"linux-base" in ansible_facts.packages'
  - service_exists.stdout_lines is search("isc-dhcp-server6.service", multiline=True)
  tags:
  - disable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - service_dhcpd6_disabled

- name: Unit Socket Exists - isc-dhcp-server6.socket
  ansible.builtin.command: systemctl -q list-unit-files isc-dhcp-server6.socket
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
  - service_dhcpd6_disabled

- name: Disable DHCPD6 Service - Disable Socket isc-dhcp-server6
  ansible.builtin.systemd:
    name: isc-dhcp-server6.socket
    enabled: false
    state: stopped
    masked: true
  when:
  - '"linux-base" in ansible_facts.packages'
  - socket_file_exists.stdout_lines is search("isc-dhcp-server6.socket", multiline=True)
  tags:
  - disable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - service_dhcpd6_disabled
```
