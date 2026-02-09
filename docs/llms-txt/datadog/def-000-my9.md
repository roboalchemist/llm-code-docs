# Source: https://docs.datadoghq.com/security/default_rules/def-000-my9.md

---
title: Disable nginx Service
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Disable nginx Service
---

# Disable nginx Service
 
## Description{% #description %}

The `nginx` service can be disabled with the following command:

```
$ sudo systemctl mask --now nginx.service
```

## Rationale{% #rationale %}

Running web server software provides a network-based avenue of attack, and should be disabled if not needed.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'linux-base' 2>/dev/null | grep -q '^installed$'; then

SYSTEMCTL_EXEC='/usr/bin/systemctl'
if [[ $("$SYSTEMCTL_EXEC" is-system-running) != "offline" ]]; then
  "$SYSTEMCTL_EXEC" stop 'nginx.service'
fi
"$SYSTEMCTL_EXEC" disable 'nginx.service'
"$SYSTEMCTL_EXEC" mask 'nginx.service'
# Disable socket activation if we have a unit file for it
if "$SYSTEMCTL_EXEC" -q list-unit-files nginx.socket; then
    if [[ $("$SYSTEMCTL_EXEC" is-system-running) != "offline" ]]; then
      "$SYSTEMCTL_EXEC" stop 'nginx.socket'
    fi
    "$SYSTEMCTL_EXEC" mask 'nginx.socket'
fi
# The service may not be running because it has been started and failed,
# so let's reset the state so OVAL checks pass.
# Service should be 'inactive', not 'failed' after reboot though.
"$SYSTEMCTL_EXEC" reset-failed 'nginx.service' || true

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
  - service_nginx_disabled
  - unknown_severity

- name: Disable nginx Service - Collect systemd Services Present in the System
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
  - service_nginx_disabled
  - unknown_severity

- name: Disable nginx Service - Ensure nginx.service is Masked
  ansible.builtin.systemd:
    name: nginx.service
    state: stopped
    enabled: false
    masked: true
  when:
  - '"linux-base" in ansible_facts.packages'
  - service_exists.stdout_lines is search("nginx.service", multiline=True)
  tags:
  - disable_strategy
  - low_complexity
  - low_disruption
  - no_reboot_needed
  - service_nginx_disabled
  - unknown_severity

- name: Unit Socket Exists - nginx.socket
  ansible.builtin.command: systemctl -q list-unit-files nginx.socket
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
  - service_nginx_disabled
  - unknown_severity

- name: Disable nginx Service - Disable Socket nginx
  ansible.builtin.systemd:
    name: nginx.socket
    enabled: false
    state: stopped
    masked: true
  when:
  - '"linux-base" in ansible_facts.packages'
  - socket_file_exists.stdout_lines is search("nginx.socket", multiline=True)
  tags:
  - disable_strategy
  - low_complexity
  - low_disruption
  - no_reboot_needed
  - service_nginx_disabled
  - unknown_severity
```
