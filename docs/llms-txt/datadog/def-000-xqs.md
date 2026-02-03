# Source: https://docs.datadoghq.com/security/default_rules/def-000-xqs.md

---
title: Audit Configuration Files Must Be Owned By Group root
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Audit Configuration Files Must Be Owned
  By Group root
---

# Audit Configuration Files Must Be Owned By Group root
 
## Description{% #description %}

All audit configuration files must be owned by group root.

```
chown :root /etc/audit/audit*.{rules,conf} /etc/audit/rules.d/*
```

## Rationale{% #rationale %}

Without the capability to restrict which roles and individuals can select which events are audited, unauthorized personnel may be able to prevent the auditing of critical events. Misconfigured audits may degrade the system's performance by overwhelming the audit log. Misconfigured audits may also make it more difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'auditd' 2>/dev/null | grep -q '^installed$' && dpkg-query --show --showformat='${db:Status-Status}' 'linux-base' 2>/dev/null | grep -q '^installed$'; then

if getent group "0" >/dev/null 2>&1; then
  newgroup="0"
fi
if [[ -z ${newgroup} ]]; then
  echo "0 is not a defined group on the system"
  exit 1
fi

find -L /etc/audit/ -maxdepth 1 -type f  ! -group 0 -regextype posix-extended -regex '^.*audit(\.rules|d\.conf)$' -exec chgrp -L $newgroup {} \;

find -L /etc/audit/rules.d/ -maxdepth 1 -type f  ! -group 0 -regextype posix-extended -regex '^.*\.rules$' -exec chgrp -L $newgroup {} \;

else
    >&2 echo 'Remediation is not applicable, nothing was done'
fi
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```gdscript3
- name: Gather the package facts
  package_facts:
    manager: auto
  tags:
  - DISA-STIG-UBTU-20-010135
  - configure_strategy
  - file_groupownership_audit_configuration
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Set the file_groupownership_audit_configuration_newgroup variable if represented
    by gid
  set_fact:
    file_groupownership_audit_configuration_newgroup: '0'
  when:
  - '"auditd" in ansible_facts.packages'
  - '"linux-base" in ansible_facts.packages'
  tags:
  - DISA-STIG-UBTU-20-010135
  - configure_strategy
  - file_groupownership_audit_configuration
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Find /etc/audit/ file(s) matching ^.*audit(\.rules|d\.conf)$
  command: find -L /etc/audit/ -maxdepth 1 -type f  ! -group 0 -regextype posix-extended
    -regex "^.*audit(\.rules|d\.conf)$"
  register: files_found
  changed_when: false
  failed_when: false
  check_mode: false
  when:
  - '"auditd" in ansible_facts.packages'
  - '"linux-base" in ansible_facts.packages'
  tags:
  - DISA-STIG-UBTU-20-010135
  - configure_strategy
  - file_groupownership_audit_configuration
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Ensure group owner on /etc/audit/ file(s) matching ^.*audit(\.rules|d\.conf)$
  file:
    path: '{{ item }}'
    group: '{{ file_groupownership_audit_configuration_newgroup }}'
    state: file
  with_items:
  - '{{ files_found.stdout_lines }}'
  when:
  - '"auditd" in ansible_facts.packages'
  - '"linux-base" in ansible_facts.packages'
  tags:
  - DISA-STIG-UBTU-20-010135
  - configure_strategy
  - file_groupownership_audit_configuration
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Find /etc/audit/rules.d/ file(s) matching ^.*\.rules$
  command: find -L /etc/audit/rules.d/ -maxdepth 1 -type f  ! -group 0 -regextype
    posix-extended -regex "^.*\.rules$"
  register: files_found
  changed_when: false
  failed_when: false
  check_mode: false
  when:
  - '"auditd" in ansible_facts.packages'
  - '"linux-base" in ansible_facts.packages'
  tags:
  - DISA-STIG-UBTU-20-010135
  - configure_strategy
  - file_groupownership_audit_configuration
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Ensure group owner on /etc/audit/rules.d/ file(s) matching ^.*\.rules$
  file:
    path: '{{ item }}'
    group: '{{ file_groupownership_audit_configuration_newgroup }}'
    state: file
  with_items:
  - '{{ files_found.stdout_lines }}'
  when:
  - '"auditd" in ansible_facts.packages'
  - '"linux-base" in ansible_facts.packages'
  tags:
  - DISA-STIG-UBTU-20-010135
  - configure_strategy
  - file_groupownership_audit_configuration
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
```
