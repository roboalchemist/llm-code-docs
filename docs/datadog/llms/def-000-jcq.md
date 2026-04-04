# Source: https://docs.datadoghq.com/security/default_rules/def-000-jcq.md

---
title: Disable Network File System (nfs)
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Disable Network File System (nfs)
---

# Disable Network File System (nfs)

## Description{% #description %}

The Network File System (NFS) service allows remote hosts to mount and interact with shared filesystems on the local system. If the local system is not designated as a NFS server then this service should be disabled. The `nfs-server` service can be disabled with the following command:

```
$ sudo systemctl mask --now nfs-server.service
```

## Rationale{% #rationale %}

Unnecessary services should be disabled to decrease the attack surface of the system.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'linux-base' 2>/dev/null | grep -q '^installed$'; then

SYSTEMCTL_EXEC='/usr/bin/systemctl'
if [[ $("$SYSTEMCTL_EXEC" is-system-running) != "offline" ]]; then
  "$SYSTEMCTL_EXEC" stop 'nfs-server.service'
fi
"$SYSTEMCTL_EXEC" disable 'nfs-server.service'
"$SYSTEMCTL_EXEC" mask 'nfs-server.service'
# Disable socket activation if we have a unit file for it
if "$SYSTEMCTL_EXEC" -q list-unit-files nfs-server.socket; then
    if [[ $("$SYSTEMCTL_EXEC" is-system-running) != "offline" ]]; then
      "$SYSTEMCTL_EXEC" stop 'nfs-server.socket'
    fi
    "$SYSTEMCTL_EXEC" mask 'nfs-server.socket'
fi
# The service may not be running because it has been started and failed,
# so let's reset the state so OVAL checks pass.
# Service should be 'inactive', not 'failed' after reboot though.
"$SYSTEMCTL_EXEC" reset-failed 'nfs-server.service' || true

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
  - no_reboot_needed
  - service_nfs_disabled
  - unknown_severity

- name: Disable Network File System (nfs) - Collect systemd Services Present in the
    System
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
  - no_reboot_needed
  - service_nfs_disabled
  - unknown_severity

- name: Disable Network File System (nfs) - Ensure nfs-server.service is Masked
  ansible.builtin.systemd:
    name: nfs-server.service
    state: stopped
    enabled: false
    masked: true
  when:
  - '"linux-base" in ansible_facts.packages'
  - service_exists.stdout_lines is search("nfs-server.service", multiline=True)
  tags:
  - NIST-800-53-CM-6(a)
  - NIST-800-53-CM-7(a)
  - NIST-800-53-CM-7(b)
  - disable_strategy
  - low_complexity
  - low_disruption
  - no_reboot_needed
  - service_nfs_disabled
  - unknown_severity

- name: Unit Socket Exists - nfs-server.socket
  ansible.builtin.command: systemctl -q list-unit-files nfs-server.socket
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
  - no_reboot_needed
  - service_nfs_disabled
  - unknown_severity

- name: Disable Network File System (nfs) - Disable Socket nfs-server
  ansible.builtin.systemd:
    name: nfs-server.socket
    enabled: false
    state: stopped
    masked: true
  when:
  - '"linux-base" in ansible_facts.packages'
  - socket_file_exists.stdout_lines is search("nfs-server.socket", multiline=True)
  tags:
  - NIST-800-53-CM-6(a)
  - NIST-800-53-CM-7(a)
  - NIST-800-53-CM-7(b)
  - disable_strategy
  - low_complexity
  - low_disruption
  - no_reboot_needed
  - service_nfs_disabled
  - unknown_severity
```
