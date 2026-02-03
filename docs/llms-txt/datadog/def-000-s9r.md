# Source: https://docs.datadoghq.com/security/default_rules/def-000-s9r.md

---
title: Disable systemd-journal-remote Socket
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Disable systemd-journal-remote Socket
---

# Disable systemd-journal-remote Socket
 
## Description{% #description %}

Journald supports the ability to receive messages from remote hosts, thus acting as a log server. Clients should not receive data from other hosts. NOTE: The same package, systemd-journal-remote , is used for both sending logs to remote hosts and receiving incoming logs. With regards to receiving logs, there are two Systemd unit files; systemd-journal-remote.socket and systemd-journal-remote.service.

## Rationale{% #rationale %}

If a client is configured to also receive data, thus turning it into a server, the client system is acting outside it's operational boundary.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'linux-base' 2>/dev/null | grep -q '^installed$'; then

SOCKET_NAME="systemd-journal-remote.socket"
SYSTEMCTL_EXEC='/usr/bin/systemctl'

if "$SYSTEMCTL_EXEC" -q list-unit-files --type socket | grep -q "$SOCKET_NAME"; then
    if [[ $("$SYSTEMCTL_EXEC" is-system-running) != "offline" ]]; then
      "$SYSTEMCTL_EXEC" stop "$SOCKET_NAME"
    fi
    "$SYSTEMCTL_EXEC" mask "$SOCKET_NAME"
fi

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
  - socket_systemd-journal-remote_disabled

- name: Disable systemd-journal-remote Socket - Collect systemd Socket Units Present
    in the System
  ansible.builtin.command:
    cmd: systemctl -q list-unit-files --type socket
  register: result_systemd_unit_files
  changed_when: false
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - disable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - socket_systemd-journal-remote_disabled

- name: Disable systemd-journal-remote Socket - Ensure systemd-journal-remote.socket
    is Masked
  ansible.builtin.systemd:
    name: systemd-journal-remote.socket
    state: stopped
    enabled: false
    masked: true
  when:
  - '"linux-base" in ansible_facts.packages'
  - result_systemd_unit_files.stdout_lines is search("systemd-journal-remote.socket")
  tags:
  - disable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - socket_systemd-journal-remote_disabled
```
