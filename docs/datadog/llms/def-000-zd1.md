# Source: https://docs.datadoghq.com/security/default_rules/def-000-zd1.md

---
title: Require Authentication for Single User Mode
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Require Authentication for Single User
  Mode
---

# Require Authentication for Single User Mode

## Description{% #description %}

Single-user mode is intended as a system recovery method, providing a single user root access to the system by providing a boot option at startup.

By default, single-user mode is protected by requiring a password and is set in `/usr/lib/systemd/system/rescue.service`.

## Rationale{% #rationale %}

This prevents attackers with physical access from trivially bypassing security on the machine and gaining root access. Such accesses are further prevented by configuring the bootloader password.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if [ ! -f /.dockerenv ] && [ ! -f /run/.containerenv ]; then

service_file="/usr/lib/systemd/system/rescue.service"

sulogin='/bin/sh -c "/usr/sbin/sulogin; /usr/bin/systemctl --fail --no-block default"'

if grep "^ExecStart=.*" "$service_file" ; then
    sed -i "s%^ExecStart=.*%ExecStart=-$sulogin%" "$service_file"
else
    echo "ExecStart=-$sulogin" >> "$service_file"
fi

else
    >&2 echo 'Remediation is not applicable, nothing was done'
fi
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```
- name: Require single user mode password
  lineinfile:
    create: true
    dest: /usr/lib/systemd/system/rescue.service
    regexp: ^#?ExecStart=
    line: ExecStart=-/bin/sh -c "/usr/sbin/sulogin; /usr/bin/systemctl --fail --no-block
      default"
  when: ansible_virtualization_type not in ["docker", "lxc", "openvz", "podman", "container"]
  tags:
  - CCE-27287-2
  - DISA-STIG-RHEL-07-010481
  - NIST-800-171-3.1.1
  - NIST-800-171-3.4.5
  - NIST-800-53-AC-3
  - NIST-800-53-CM-6(a)
  - NIST-800-53-IA-2
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - require_singleuser_auth
  - restrict_strategy
```
