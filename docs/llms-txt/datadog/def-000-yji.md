# Source: https://docs.datadoghq.com/security/default_rules/def-000-yji.md

---
title: Ensure journald is configured to send logs to rsyslog
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Ensure journald is configured to send
  logs to rsyslog
---

# Ensure journald is configured to send logs to rsyslog
 
## Description{% #description %}

Data from journald may be stored in volatile memory or persisted locally. Utilities exist to accept remote export of journald logs.

## Rationale{% #rationale %}

Storing log data on a remote host protects log integrity from local attacks. If an attacker gains root access on the local system, they could tamper with or remove log data that is stored on the local system.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'linux-base' 2>/dev/null | grep -q '^installed$'; then

if [ -e "/etc/systemd/journald.conf" ] ; then
    
    LC_ALL=C sed -i "/^\s*ForwardToSyslog\s*=\s*/d" "/etc/systemd/journald.conf"
else
    touch "/etc/systemd/journald.conf"
fi
# make sure file has newline at the end
sed -i -e '$a\' "/etc/systemd/journald.conf"

cp "/etc/systemd/journald.conf" "/etc/systemd/journald.conf.bak"
# Insert before the line matching the regex '^#\s*ForwardToSyslog'.
line_number="$(LC_ALL=C grep -n "^#\s*ForwardToSyslog" "/etc/systemd/journald.conf.bak" | LC_ALL=C sed 's/:.*//g')"
if [ -z "$line_number" ]; then
    # There was no match of '^#\s*ForwardToSyslog', insert at
    # the end of the file.
    printf '%s\n' "ForwardToSyslog=yes" >> "/etc/systemd/journald.conf"
else
    head -n "$(( line_number - 1 ))" "/etc/systemd/journald.conf.bak" > "/etc/systemd/journald.conf"
    printf '%s\n' "ForwardToSyslog=yes" >> "/etc/systemd/journald.conf"
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
  - journald_forward_to_syslog
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy

- name: Setting unquoted shell-style assignment of 'ForwardToSyslog' to 'yes' in '/etc/systemd/journald.conf'
  block:

  - name: Check for duplicate values
    lineinfile:
      path: /etc/systemd/journald.conf
      create: true
      regexp: (?i)^\s*ForwardToSyslog=
      state: absent
    check_mode: true
    changed_when: false
    register: dupes

  - name: Deduplicate values from /etc/systemd/journald.conf
    lineinfile:
      path: /etc/systemd/journald.conf
      create: true
      regexp: (?i)^\s*ForwardToSyslog=
      state: absent
    when: dupes.found is defined and dupes.found > 1

  - name: Insert correct line to /etc/systemd/journald.conf
    lineinfile:
      path: /etc/systemd/journald.conf
      create: true
      regexp: (?i)^\s*ForwardToSyslog=
      line: ForwardToSyslog=yes
      state: present
      insertbefore: ^# ForwardToSyslog
      validate: /usr/bin/bash -n %s
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - journald_forward_to_syslog
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
```
