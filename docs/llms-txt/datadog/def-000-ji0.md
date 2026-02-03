# Source: https://docs.datadoghq.com/security/default_rules/def-000-ji0.md

---
title: Verify nftables Service is Disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Verify nftables Service is Disabled
---

# Verify nftables Service is Disabled
 
## Description{% #description %}

nftables is a subsystem of the Linux kernel providing filtering and classification of network packets/datagrams/frames and is the successor to iptables. The `nftables` service can be disabled with the following command:

```
systemctl disable nftables
```

## Rationale{% #rationale %}

nftables should be disabled if another firewall service is used as it may lead to conflict.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if ( dpkg-query --show --showformat='${db:Status-Status}' 'nftables' 2>/dev/null | grep -q '^installed$' && dpkg-query --show --showformat='${db:Status-Status}' 'linux-base' 2>/dev/null | grep -q '^installed$' ); then

SYSTEMCTL_EXEC='/usr/bin/systemctl'
if [[ $("$SYSTEMCTL_EXEC" is-system-running) != "offline" ]]; then
  "$SYSTEMCTL_EXEC" stop 'nftables.service'
fi
"$SYSTEMCTL_EXEC" disable 'nftables.service'
"$SYSTEMCTL_EXEC" mask 'nftables.service'
# Disable socket activation if we have a unit file for it
if "$SYSTEMCTL_EXEC" -q list-unit-files nftables.socket; then
    if [[ $("$SYSTEMCTL_EXEC" is-system-running) != "offline" ]]; then
      "$SYSTEMCTL_EXEC" stop 'nftables.socket'
    fi
    "$SYSTEMCTL_EXEC" mask 'nftables.socket'
fi
# The service may not be running because it has been started and failed,
# so let's reset the state so OVAL checks pass.
# Service should be 'inactive', not 'failed' after reboot though.
"$SYSTEMCTL_EXEC" reset-failed 'nftables.service' || true

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
  - PCI-DSSv4-1.2
  - PCI-DSSv4-1.2.1
  - disable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - service_nftables_disabled

- name: Verify nftables Service is Disabled - Collect systemd Services Present in
    the System
  ansible.builtin.command: systemctl -q list-unit-files --type service
  register: service_exists
  changed_when: false
  failed_when: service_exists.rc not in [0, 1]
  check_mode: false
  when: ( "nftables" in ansible_facts.packages and "linux-base" in ansible_facts.packages
    )
  tags:
  - PCI-DSSv4-1.2
  - PCI-DSSv4-1.2.1
  - disable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - service_nftables_disabled

- name: Verify nftables Service is Disabled - Ensure nftables.service is Masked
  ansible.builtin.systemd:
    name: nftables.service
    state: stopped
    enabled: false
    masked: true
  when:
  - ( "nftables" in ansible_facts.packages and "linux-base" in ansible_facts.packages
    )
  - service_exists.stdout_lines is search("nftables.service", multiline=True)
  tags:
  - PCI-DSSv4-1.2
  - PCI-DSSv4-1.2.1
  - disable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - service_nftables_disabled

- name: Unit Socket Exists - nftables.socket
  ansible.builtin.command: systemctl -q list-unit-files nftables.socket
  register: socket_file_exists
  changed_when: false
  failed_when: socket_file_exists.rc not in [0, 1]
  check_mode: false
  when: ( "nftables" in ansible_facts.packages and "linux-base" in ansible_facts.packages
    )
  tags:
  - PCI-DSSv4-1.2
  - PCI-DSSv4-1.2.1
  - disable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - service_nftables_disabled

- name: Verify nftables Service is Disabled - Disable Socket nftables
  ansible.builtin.systemd:
    name: nftables.socket
    enabled: false
    state: stopped
    masked: true
  when:
  - ( "nftables" in ansible_facts.packages and "linux-base" in ansible_facts.packages
    )
  - socket_file_exists.stdout_lines is search("nftables.socket", multiline=True)
  tags:
  - PCI-DSSv4-1.2
  - PCI-DSSv4-1.2.1
  - disable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - service_nftables_disabled
```
