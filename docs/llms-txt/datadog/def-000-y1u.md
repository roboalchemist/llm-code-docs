# Source: https://docs.datadoghq.com/security/default_rules/def-000-y1u.md

---
title: Set SSH Daemon LogLevel to VERBOSE
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Set SSH Daemon LogLevel to VERBOSE
---

# Set SSH Daemon LogLevel to VERBOSE
 
## Description{% #description %}

The `VERBOSE` parameter configures the SSH daemon to record login and logout activity. To specify the log level in SSH, add or correct the following line in `/etc/ssh/sshd_config`:

```
LogLevel VERBOSE
```

## Rationale{% #rationale %}

SSH provides several logging levels with varying amounts of verbosity. `DEBUG` is specifically not recommended other than strictly for debugging SSH communications since it provides so much data that it is difficult to identify important security information. `INFO` or `VERBOSE` level is the basic level that only records login activity of SSH users. In many situations, such as Incident Response, it is important to determine when a particular user was active on a system. The logout record can eliminate those users who disconnected, which helps narrow the field.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if [ ! -f /.dockerenv ] && [ ! -f /run/.containerenv ]; then

if [ -e "/etc/ssh/sshd_config" ] ; then
    
    LC_ALL=C sed -i "/^\s*LogLevel\s\+/Id" "/etc/ssh/sshd_config"
else
    touch "/etc/ssh/sshd_config"
fi
# make sure file has newline at the end
sed -i -e '$a\' "/etc/ssh/sshd_config"

cp "/etc/ssh/sshd_config" "/etc/ssh/sshd_config.bak"
# Insert at the beginning of the file
printf '%s\n' "LogLevel VERBOSE" > "/etc/ssh/sshd_config"
cat "/etc/ssh/sshd_config.bak" >> "/etc/ssh/sshd_config"
# Clean up after ourselves.
rm "/etc/ssh/sshd_config.bak"

else
    >&2 echo 'Remediation is not applicable, nothing was done'
fi
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```
- name: Set SSH Daemon LogLevel to VERBOSE
  block:

  - name: Check for duplicate values
    lineinfile:
      path: /etc/ssh/sshd_config
      create: true
      regexp: (?i)^\s*LogLevel\s+
      state: absent
    check_mode: true
    changed_when: false
    register: dupes

  - name: Deduplicate values from /etc/ssh/sshd_config
    lineinfile:
      path: /etc/ssh/sshd_config
      create: true
      regexp: (?i)^\s*LogLevel\s+
      state: absent
    when: dupes.found is defined and dupes.found > 1

  - name: Insert correct line to /etc/ssh/sshd_config
    lineinfile:
      path: /etc/ssh/sshd_config
      create: true
      regexp: (?i)^\s*LogLevel\s+
      line: LogLevel VERBOSE
      state: present
      insertbefore: BOF
      validate: /usr/sbin/sshd -t -f %s
  when: ansible_virtualization_type not in ["docker", "lxc", "openvz", "podman", "container"]
  tags:
  - CCE-82419-3
  - NIST-800-53-AC-17(1)
  - NIST-800-53-AC-17(a)
  - NIST-800-53-CM-6(a)
  - PCI-DSS-Req-2.2.4
  - PCI-DSSv4-2.2.6
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
  - sshd_set_loglevel_verbose
```
