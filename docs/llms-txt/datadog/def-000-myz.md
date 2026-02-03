# Source: https://docs.datadoghq.com/security/default_rules/def-000-myz.md

---
title: Disable Avahi Server Software
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Disable Avahi Server Software
---

# Disable Avahi Server Software
 
## Description{% #description %}

The `avahi-daemon` service can be disabled with the following command:

```
$ sudo systemctl mask --now avahi-daemon.service
```

## Rationale{% #rationale %}

Because the Avahi daemon service keeps an open network port, it is subject to network attacks. Its functionality is convenient but is only appropriate if the local network can be trusted.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if ( dpkg-query --show --showformat='${db:Status-Status}' 'avahi-daemon' 2>/dev/null | grep -q '^installed$' && dpkg-query --show --showformat='${db:Status-Status}' 'linux-base' 2>/dev/null | grep -q '^installed$' ); then

SYSTEMCTL_EXEC='/usr/bin/systemctl'
if [[ $("$SYSTEMCTL_EXEC" is-system-running) != "offline" ]]; then
  "$SYSTEMCTL_EXEC" stop 'avahi-daemon.service'
fi
"$SYSTEMCTL_EXEC" disable 'avahi-daemon.service'
"$SYSTEMCTL_EXEC" mask 'avahi-daemon.service'
# Disable socket activation if we have a unit file for it
if "$SYSTEMCTL_EXEC" -q list-unit-files avahi-daemon.socket; then
    if [[ $("$SYSTEMCTL_EXEC" is-system-running) != "offline" ]]; then
      "$SYSTEMCTL_EXEC" stop 'avahi-daemon.socket'
    fi
    "$SYSTEMCTL_EXEC" mask 'avahi-daemon.socket'
fi
# The service may not be running because it has been started and failed,
# so let's reset the state so OVAL checks pass.
# Service should be 'inactive', not 'failed' after reboot though.
"$SYSTEMCTL_EXEC" reset-failed 'avahi-daemon.service' || true

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
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.4
  - disable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - service_avahi-daemon_disabled

- name: Disable Avahi Server Software - Collect systemd Services Present in the System
  ansible.builtin.command: systemctl -q list-unit-files --type service
  register: service_exists
  changed_when: false
  failed_when: service_exists.rc not in [0, 1]
  check_mode: false
  when: ( "avahi-daemon" in ansible_facts.packages and "linux-base" in ansible_facts.packages
    )
  tags:
  - NIST-800-53-CM-6(a)
  - NIST-800-53-CM-7(a)
  - NIST-800-53-CM-7(b)
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.4
  - disable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - service_avahi-daemon_disabled

- name: Disable Avahi Server Software - Ensure avahi-daemon.service is Masked
  ansible.builtin.systemd:
    name: avahi-daemon.service
    state: stopped
    enabled: false
    masked: true
  when:
  - ( "avahi-daemon" in ansible_facts.packages and "linux-base" in ansible_facts.packages
    )
  - service_exists.stdout_lines is search("avahi-daemon.service", multiline=True)
  tags:
  - NIST-800-53-CM-6(a)
  - NIST-800-53-CM-7(a)
  - NIST-800-53-CM-7(b)
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.4
  - disable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - service_avahi-daemon_disabled

- name: Unit Socket Exists - avahi-daemon.socket
  ansible.builtin.command: systemctl -q list-unit-files avahi-daemon.socket
  register: socket_file_exists
  changed_when: false
  failed_when: socket_file_exists.rc not in [0, 1]
  check_mode: false
  when: ( "avahi-daemon" in ansible_facts.packages and "linux-base" in ansible_facts.packages
    )
  tags:
  - NIST-800-53-CM-6(a)
  - NIST-800-53-CM-7(a)
  - NIST-800-53-CM-7(b)
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.4
  - disable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - service_avahi-daemon_disabled

- name: Disable Avahi Server Software - Disable Socket avahi-daemon
  ansible.builtin.systemd:
    name: avahi-daemon.socket
    enabled: false
    state: stopped
    masked: true
  when:
  - ( "avahi-daemon" in ansible_facts.packages and "linux-base" in ansible_facts.packages
    )
  - socket_file_exists.stdout_lines is search("avahi-daemon.socket", multiline=True)
  tags:
  - NIST-800-53-CM-6(a)
  - NIST-800-53-CM-7(a)
  - NIST-800-53-CM-7(b)
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.4
  - disable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - service_avahi-daemon_disabled
```
