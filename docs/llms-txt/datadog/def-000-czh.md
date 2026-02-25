# Source: https://docs.datadoghq.com/security/default_rules/def-000-czh.md

---
title: Disable LDAP Server (slapd)
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Disable LDAP Server (slapd)
---

# Disable LDAP Server (slapd)

## Description{% #description %}

The Lightweight Directory Access Protocol (LDAP) is a service that provides a method for looking up information from a central database.

## Rationale{% #rationale %}

If the system will not need to act as an LDAP server, it is recommended that the software be disabled to reduce the potential attack surface.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'linux-base' 2>/dev/null | grep -q '^installed$'; then

SYSTEMCTL_EXEC='/usr/bin/systemctl'
if [[ $("$SYSTEMCTL_EXEC" is-system-running) != "offline" ]]; then
  "$SYSTEMCTL_EXEC" stop 'slapd.service'
fi
"$SYSTEMCTL_EXEC" disable 'slapd.service'
"$SYSTEMCTL_EXEC" mask 'slapd.service'
# Disable socket activation if we have a unit file for it
if "$SYSTEMCTL_EXEC" -q list-unit-files slapd.socket; then
    if [[ $("$SYSTEMCTL_EXEC" is-system-running) != "offline" ]]; then
      "$SYSTEMCTL_EXEC" stop 'slapd.socket'
    fi
    "$SYSTEMCTL_EXEC" mask 'slapd.socket'
fi
# The service may not be running because it has been started and failed,
# so let's reset the state so OVAL checks pass.
# Service should be 'inactive', not 'failed' after reboot though.
"$SYSTEMCTL_EXEC" reset-failed 'slapd.service' || true

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
  - service_slapd_disabled

- name: Disable LDAP Server (slapd) - Collect systemd Services Present in the System
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
  - service_slapd_disabled

- name: Disable LDAP Server (slapd) - Ensure slapd.service is Masked
  ansible.builtin.systemd:
    name: slapd.service
    state: stopped
    enabled: false
    masked: true
  when:
  - '"linux-base" in ansible_facts.packages'
  - service_exists.stdout_lines is search("slapd.service", multiline=True)
  tags:
  - disable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - service_slapd_disabled

- name: Unit Socket Exists - slapd.socket
  ansible.builtin.command: systemctl -q list-unit-files slapd.socket
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
  - service_slapd_disabled

- name: Disable LDAP Server (slapd) - Disable Socket slapd
  ansible.builtin.systemd:
    name: slapd.socket
    enabled: false
    state: stopped
    masked: true
  when:
  - '"linux-base" in ansible_facts.packages'
  - socket_file_exists.stdout_lines is search("slapd.socket", multiline=True)
  tags:
  - disable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - service_slapd_disabled
```
