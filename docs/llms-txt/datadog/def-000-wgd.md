# Source: https://docs.datadoghq.com/security/default_rules/def-000-wgd.md

---
title: Ensure journald is configured to compress large log files
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Ensure journald is configured to
  compress large log files
---

# Ensure journald is configured to compress large log files
 
## Description{% #description %}

The journald system can compress large log files to avoid fill the system disk.

## Rationale{% #rationale %}

Log files that are not properly compressed run the risk of growing so large that they fill up the log partition. Valuable logging information could be lost if the log partition becomes full.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'linux-base' 2>/dev/null | grep -q '^installed$'; then

if [ -e "/etc/systemd/journald.conf" ] ; then
    
    LC_ALL=C sed -i "/^\s*Compress\s*=\s*/d" "/etc/systemd/journald.conf"
else
    touch "/etc/systemd/journald.conf"
fi
# make sure file has newline at the end
sed -i -e '$a\' "/etc/systemd/journald.conf"

cp "/etc/systemd/journald.conf" "/etc/systemd/journald.conf.bak"
# Insert before the line matching the regex '^#\s*Compress'.
line_number="$(LC_ALL=C grep -n "^#\s*Compress" "/etc/systemd/journald.conf.bak" | LC_ALL=C sed 's/:.*//g')"
if [ -z "$line_number" ]; then
    # There was no match of '^#\s*Compress', insert at
    # the end of the file.
    printf '%s\n' "Compress=yes" >> "/etc/systemd/journald.conf"
else
    head -n "$(( line_number - 1 ))" "/etc/systemd/journald.conf.bak" > "/etc/systemd/journald.conf"
    printf '%s\n' "Compress=yes" >> "/etc/systemd/journald.conf"
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
  - journald_compress
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy

- name: Setting unquoted shell-style assignment of 'Compress' to 'yes' in '/etc/systemd/journald.conf'
  block:

  - name: Check for duplicate values
    lineinfile:
      path: /etc/systemd/journald.conf
      create: true
      regexp: (?i)^\s*Compress=
      state: absent
    check_mode: true
    changed_when: false
    register: dupes

  - name: Deduplicate values from /etc/systemd/journald.conf
    lineinfile:
      path: /etc/systemd/journald.conf
      create: true
      regexp: (?i)^\s*Compress=
      state: absent
    when: dupes.found is defined and dupes.found > 1

  - name: Insert correct line to /etc/systemd/journald.conf
    lineinfile:
      path: /etc/systemd/journald.conf
      create: true
      regexp: (?i)^\s*Compress=
      line: Compress=yes
      state: present
      insertbefore: ^# Compress
      validate: /usr/bin/bash -n %s
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - journald_compress
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
```
