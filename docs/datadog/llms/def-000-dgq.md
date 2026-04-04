# Source: https://docs.datadoghq.com/security/default_rules/def-000-dgq.md

---
title: Disable systemd_timesyncd Service
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Disable systemd_timesyncd Service
---

# Disable systemd_timesyncd Service

## Description{% #description %}

The `systemd_timesyncd` service can be disabled with the following command:

```
$ sudo systemctl mask --now systemd_timesyncd.service
```

## Rationale{% #rationale %}

Disabling the `systemd_timesyncd` service ensures that there is only single one time service running.

Additional information on Ubuntu network time protocol is available at [https://ubuntu.com/server/docs/about-time-synchronisation](https://ubuntu.com/server/docs/about-time-synchronisation).

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'linux-base' 2>/dev/null | grep -q '^installed$' && { dpkg-query --show --showformat='${db:Status-Status}' 'systemd-timesyncd' 2>/dev/null | grep -q '^installed$'; }; then

var_timesync_service='systemd-timesyncd'



if [ $var_timesync_service != systemd-timesyncd ]; then
  SYSTEMCTL_EXEC='/usr/bin/systemctl'
  "$SYSTEMCTL_EXEC" stop 'systemd-timesyncd.service'
  "$SYSTEMCTL_EXEC" disable 'systemd-timesyncd.service'
  "$SYSTEMCTL_EXEC" mask 'systemd-timesyncd.service'
  # Disable socket activation if we have a unit file for it
  if "$SYSTEMCTL_EXEC" -q list-unit-files systemd-timesyncd.socket; then
      "$SYSTEMCTL_EXEC" stop 'systemd-timesyncd.socket'
      "$SYSTEMCTL_EXEC" mask 'systemd-timesyncd.socket'
  fi
  # The service may not be running because it has been started and failed,
  # so let's reset the state so OVAL checks pass.
  # Service should be 'inactive', not 'failed' after reboot though.
  "$SYSTEMCTL_EXEC" reset-failed 'systemd-timesyncd.service' || true
fi

else
    >&2 echo 'Remediation is not applicable, nothing was done'
fi
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```gdscript3
- name: Gather the package facts
  package_facts:
    manager: auto
  tags:
  - disable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - service_timesyncd_disabled
- name: XCCDF Value var_timesync_service # promote to variable
  set_fact:
    var_timesync_service: !!str systemd-timesyncd
  tags:
    - always

- name: Disable systemd_timesyncd Service - Collect systemd Services Present in the
    System
  ansible.builtin.command: systemctl -q list-unit-files --type service
  register: service_exists
  changed_when: false
  failed_when: service_exists.rc not in [0, 1]
  check_mode: false
  when:
  - '"linux-base" in ansible_facts.packages'
  - '"systemd-timesyncd" in ansible_facts.packages'
  tags:
  - disable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - service_timesyncd_disabled

- name: Disable systemd_timesyncd Service - Ensure "systemd-timesyncd.service" is
    Masked
  ansible.builtin.systemd:
    name: systemd-timesyncd.service
    state: stopped
    enabled: false
    masked: true
  when:
  - '"linux-base" in ansible_facts.packages'
  - '"systemd-timesyncd" in ansible_facts.packages'
  - service_exists.stdout_lines is search("systemd-timesyncd.service",multiline=True)
  - var_timesync_service != "systemd-timesyncd"
  tags:
  - disable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - service_timesyncd_disabled

- name: Unit Socket Exists - systemd-timesyncd.socket
  ansible.builtin.command: systemctl -q list-unit-files systemd-timesyncd.socket
  register: socket_file_exists
  changed_when: false
  failed_when: socket_file_exists.rc not in [0, 1]
  check_mode: false
  when:
  - '"linux-base" in ansible_facts.packages'
  - '"systemd-timesyncd" in ansible_facts.packages'
  tags:
  - disable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - service_timesyncd_disabled

- name: Disable socket systemd-timesyncd
  ansible.builtin.systemd:
    name: systemd-timesyncd.socket
    enabled: 'no'
    state: stopped
    masked: 'yes'
  when:
  - '"linux-base" in ansible_facts.packages'
  - '"systemd-timesyncd" in ansible_facts.packages'
  - socket_file_exists.stdout_lines is search("systemd-timesyncd.socket",multiline=True)
  - var_timesync_service != "systemd-timesyncd"
  tags:
  - disable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - service_timesyncd_disabled
```
