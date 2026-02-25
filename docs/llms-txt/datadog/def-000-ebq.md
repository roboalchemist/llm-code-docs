# Source: https://docs.datadoghq.com/security/default_rules/def-000-ebq.md

---
title: Disable vsftpd Service
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Disable vsftpd Service
---

# Disable vsftpd Service

## Description{% #description %}

The `vsftpd` service can be disabled with the following command:

```
$ sudo systemctl mask --now vsftpd.service
```

## Rationale{% #rationale %}

Running FTP server software provides a network-based avenue of attack, and should be disabled if not needed. Furthermore, the FTP protocol is unencrypted and creates a risk of compromising sensitive information.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'linux-base' 2>/dev/null | grep -q '^installed$'; then

SYSTEMCTL_EXEC='/usr/bin/systemctl'
if [[ $("$SYSTEMCTL_EXEC" is-system-running) != "offline" ]]; then
  "$SYSTEMCTL_EXEC" stop 'vsftpd.service'
fi
"$SYSTEMCTL_EXEC" disable 'vsftpd.service'
"$SYSTEMCTL_EXEC" mask 'vsftpd.service'
# Disable socket activation if we have a unit file for it
if "$SYSTEMCTL_EXEC" -q list-unit-files vsftpd.socket; then
    if [[ $("$SYSTEMCTL_EXEC" is-system-running) != "offline" ]]; then
      "$SYSTEMCTL_EXEC" stop 'vsftpd.socket'
    fi
    "$SYSTEMCTL_EXEC" mask 'vsftpd.socket'
fi
# The service may not be running because it has been started and failed,
# so let's reset the state so OVAL checks pass.
# Service should be 'inactive', not 'failed' after reboot though.
"$SYSTEMCTL_EXEC" reset-failed 'vsftpd.service' || true

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
  - NIST-800-53-CM-7(a)
  - NIST-800-53-CM-7(b)
  - disable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - service_vsftpd_disabled

- name: Disable vsftpd Service - Collect systemd Services Present in the System
  ansible.builtin.command: systemctl -q list-unit-files --type service
  register: service_exists
  changed_when: false
  failed_when: service_exists.rc not in [0, 1]
  check_mode: false
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - NIST-800-53-CM-6(a)
  - NIST-800-53-CM-7(a)
  - NIST-800-53-CM-7(b)
  - disable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - service_vsftpd_disabled

- name: Disable vsftpd Service - Ensure vsftpd.service is Masked
  ansible.builtin.systemd:
    name: vsftpd.service
    state: stopped
    enabled: false
    masked: true
  when:
  - '"linux-base" in ansible_facts.packages'
  - service_exists.stdout_lines is search("vsftpd.service", multiline=True)
  tags:
  - NIST-800-53-CM-6(a)
  - NIST-800-53-CM-7(a)
  - NIST-800-53-CM-7(b)
  - disable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - service_vsftpd_disabled

- name: Unit Socket Exists - vsftpd.socket
  ansible.builtin.command: systemctl -q list-unit-files vsftpd.socket
  register: socket_file_exists
  changed_when: false
  failed_when: socket_file_exists.rc not in [0, 1]
  check_mode: false
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - NIST-800-53-CM-6(a)
  - NIST-800-53-CM-7(a)
  - NIST-800-53-CM-7(b)
  - disable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - service_vsftpd_disabled

- name: Disable vsftpd Service - Disable Socket vsftpd
  ansible.builtin.systemd:
    name: vsftpd.socket
    enabled: false
    state: stopped
    masked: true
  when:
  - '"linux-base" in ansible_facts.packages'
  - socket_file_exists.stdout_lines is search("vsftpd.socket", multiline=True)
  tags:
  - NIST-800-53-CM-6(a)
  - NIST-800-53-CM-7(a)
  - NIST-800-53-CM-7(b)
  - disable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - service_vsftpd_disabled
```
