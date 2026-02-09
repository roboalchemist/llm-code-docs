# Source: https://docs.datadoghq.com/security/default_rules/def-000-rqm.md

---
title: Disable apache2 Service
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Disable apache2 Service
---

# Disable apache2 Service
 
## Description{% #description %}

The `apache2` service can be disabled with the following command:

```
$ sudo systemctl mask --now apache2.service
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
  "$SYSTEMCTL_EXEC" stop 'apache2.service'
fi
"$SYSTEMCTL_EXEC" disable 'apache2.service'
"$SYSTEMCTL_EXEC" mask 'apache2.service'
# Disable socket activation if we have a unit file for it
if "$SYSTEMCTL_EXEC" -q list-unit-files apache2.socket; then
    if [[ $("$SYSTEMCTL_EXEC" is-system-running) != "offline" ]]; then
      "$SYSTEMCTL_EXEC" stop 'apache2.socket'
    fi
    "$SYSTEMCTL_EXEC" mask 'apache2.socket'
fi
# The service may not be running because it has been started and failed,
# so let's reset the state so OVAL checks pass.
# Service should be 'inactive', not 'failed' after reboot though.
"$SYSTEMCTL_EXEC" reset-failed 'apache2.service' || true

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
  - service_httpd_disabled
  - unknown_severity

- name: Disable apache2 Service - Collect systemd Services Present in the System
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
  - service_httpd_disabled
  - unknown_severity

- name: Disable apache2 Service - Ensure apache2.service is Masked
  ansible.builtin.systemd:
    name: apache2.service
    state: stopped
    enabled: false
    masked: true
  when:
  - '"linux-base" in ansible_facts.packages'
  - service_exists.stdout_lines is search("apache2.service", multiline=True)
  tags:
  - NIST-800-53-CM-6(a)
  - NIST-800-53-CM-7(a)
  - NIST-800-53-CM-7(b)
  - disable_strategy
  - low_complexity
  - low_disruption
  - no_reboot_needed
  - service_httpd_disabled
  - unknown_severity

- name: Unit Socket Exists - apache2.socket
  ansible.builtin.command: systemctl -q list-unit-files apache2.socket
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
  - service_httpd_disabled
  - unknown_severity

- name: Disable apache2 Service - Disable Socket apache2
  ansible.builtin.systemd:
    name: apache2.socket
    enabled: false
    state: stopped
    masked: true
  when:
  - '"linux-base" in ansible_facts.packages'
  - socket_file_exists.stdout_lines is search("apache2.socket", multiline=True)
  tags:
  - NIST-800-53-CM-6(a)
  - NIST-800-53-CM-7(a)
  - NIST-800-53-CM-7(b)
  - disable_strategy
  - low_complexity
  - low_disruption
  - no_reboot_needed
  - service_httpd_disabled
  - unknown_severity
```
