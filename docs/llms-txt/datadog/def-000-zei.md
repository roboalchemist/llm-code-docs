# Source: https://docs.datadoghq.com/security/default_rules/def-000-zei.md

---
title: Ensure journald is configured to write log files to persistent disk
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Ensure journald is configured to write
  log files to persistent disk
---

# Ensure journald is configured to write log files to persistent disk
 
## Description{% #description %}

The journald system may store log files in volatile memory or locally on disk. If the logs are only stored in volatile memory they will be lost upon reboot.

## Rationale{% #rationale %}

Log files contain valuable data and need to be persistent to aid in possible investigations.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'linux-base' 2>/dev/null | grep -q '^installed$'; then

if [ -e "/etc/systemd/journald.conf" ] ; then
    
    LC_ALL=C sed -i "/^\s*Storage\s*=\s*/d" "/etc/systemd/journald.conf"
else
    touch "/etc/systemd/journald.conf"
fi
# make sure file has newline at the end
sed -i -e '$a\' "/etc/systemd/journald.conf"

cp "/etc/systemd/journald.conf" "/etc/systemd/journald.conf.bak"
# Insert before the line matching the regex '^#\s*Storage'.
line_number="$(LC_ALL=C grep -n "^#\s*Storage" "/etc/systemd/journald.conf.bak" | LC_ALL=C sed 's/:.*//g')"
if [ -z "$line_number" ]; then
    # There was no match of '^#\s*Storage', insert at
    # the end of the file.
    printf '%s\n' "Storage=persistent" >> "/etc/systemd/journald.conf"
else
    head -n "$(( line_number - 1 ))" "/etc/systemd/journald.conf.bak" > "/etc/systemd/journald.conf"
    printf '%s\n' "Storage=persistent" >> "/etc/systemd/journald.conf"
    tail -n "+$(( line_number ))" "/etc/systemd/journald.conf.bak" >> "/etc/systemd/journald.conf"
fi
# Clean up after ourselves.
rm "/etc/systemd/journald.conf.bak"

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
  - journald_storage
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy

- name: Setting unquoted shell-style assignment of 'Storage' to 'persistent' in '/etc/systemd/journald.conf'
  block:

  - name: Check for duplicate values
    lineinfile:
      path: /etc/systemd/journald.conf
      create: true
      regexp: (?i)^\s*Storage=
      state: absent
    check_mode: true
    changed_when: false
    register: dupes

  - name: Deduplicate values from /etc/systemd/journald.conf
    lineinfile:
      path: /etc/systemd/journald.conf
      create: true
      regexp: (?i)^\s*Storage=
      state: absent
    when: dupes.found is defined and dupes.found > 1

  - name: Insert correct line to /etc/systemd/journald.conf
    lineinfile:
      path: /etc/systemd/journald.conf
      create: true
      regexp: (?i)^\s*Storage=
      line: Storage=persistent
      state: present
      insertbefore: ^# Storage
      validate: /usr/bin/bash -n %s
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - journald_storage
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
```
