# Source: https://docs.datadoghq.com/security/default_rules/def-000-ovy.md

---
title: System Audit Logs Must Be Group Owned By Root
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > System Audit Logs Must Be Group Owned
  By Root
---

# System Audit Logs Must Be Group Owned By Root
 
## Description{% #description %}

All audit logs must be group owned by root user. The path for audit log can be configured via `log_file` parameter in

```
/etc/audit/auditd.conf
```

or, by default, the path for audit log is

```gdscript3
/var/log/audit/
```

. To properly set the group owner of `/var/log/audit/*`, run the command:

```gdscript3
$ sudo chgrp root /var/log/audit/*
```

If `log_group` in `/etc/audit/auditd.conf` is set to a group other than the `root` group account, change the group ownership of the audit logs to this specific group.

## Rationale{% #rationale %}

Unauthorized disclosure of audit records can reveal system and configuration data to attackers, thus compromising its confidentiality.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'auditd' 2>/dev/null | grep -q '^installed$' && dpkg-query --show --showformat='${db:Status-Status}' 'linux-base' 2>/dev/null | grep -q '^installed$'; then

if LC_ALL=C grep -iw log_file /etc/audit/auditd.conf; then
  FILE=$(awk -F "=" '/^log_file/ {print $2}' /etc/audit/auditd.conf | tr -d ' ')
else
  FILE="/var/log/audit/audit.log"
fi


if LC_ALL=C grep -m 1 -q ^log_group /etc/audit/auditd.conf; then
  GROUP=$(awk -F "=" '/log_group/ {print $2}' /etc/audit/auditd.conf | tr -d ' ')
    if ! [ "${GROUP}" == 'root' ]; then
      chgrp ${GROUP} $FILE*
    else
      chgrp root $FILE*
    fi
else
  chgrp root $FILE*
fi

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
  - CJIS-5.4.1.1
  - DISA-STIG-UBTU-20-010124
  - NIST-800-171-3.3.1
  - NIST-800-53-AC-6(1)
  - NIST-800-53-AU-9(4)
  - NIST-800-53-CM-6(a)
  - PCI-DSS-Req-10.5.1
  - PCI-DSSv4-10.3
  - PCI-DSSv4-10.3.2
  - file_group_ownership_var_log_audit
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy

- name: System Audit Logs Must Be Group Owned By Root - Get Audit Log Files
  ansible.builtin.command: grep -iw ^log_file /etc/audit/auditd.conf
  failed_when: false
  register: log_file_exists
  when:
  - '"auditd" in ansible_facts.packages'
  - '"linux-base" in ansible_facts.packages'
  tags:
  - CJIS-5.4.1.1
  - DISA-STIG-UBTU-20-010124
  - NIST-800-171-3.3.1
  - NIST-800-53-AC-6(1)
  - NIST-800-53-AU-9(4)
  - NIST-800-53-CM-6(a)
  - PCI-DSS-Req-10.5.1
  - PCI-DSSv4-10.3
  - PCI-DSSv4-10.3.2
  - file_group_ownership_var_log_audit
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy

- name: System Audit Logs Must Be Group Owned By Root - Set Log File Facts
  ansible.builtin.set_fact:
    log_file_line: '{{ log_file_exists.stdout | split('' '') | last }}'
  when:
  - '"auditd" in ansible_facts.packages'
  - '"linux-base" in ansible_facts.packages'
  tags:
  - CJIS-5.4.1.1
  - DISA-STIG-UBTU-20-010124
  - NIST-800-171-3.3.1
  - NIST-800-53-AC-6(1)
  - NIST-800-53-AU-9(4)
  - NIST-800-53-CM-6(a)
  - PCI-DSS-Req-10.5.1
  - PCI-DSSv4-10.3
  - PCI-DSSv4-10.3.2
  - file_group_ownership_var_log_audit
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy

- name: System Audit Logs Must Be Group Owned By Root - Set Default log_file if Not
    Set
  ansible.builtin.set_fact:
    log_file: /var/log/audit/audit.log
  when:
  - '"auditd" in ansible_facts.packages'
  - '"linux-base" in ansible_facts.packages'
  - (log_file_exists is undefined) or (log_file_exists.stdout | length == 0)
  tags:
  - CJIS-5.4.1.1
  - DISA-STIG-UBTU-20-010124
  - NIST-800-171-3.3.1
  - NIST-800-53-AC-6(1)
  - NIST-800-53-AU-9(4)
  - NIST-800-53-CM-6(a)
  - PCI-DSS-Req-10.5.1
  - PCI-DSSv4-10.3
  - PCI-DSSv4-10.3.2
  - file_group_ownership_var_log_audit
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy

- name: System Audit Logs Must Be Group Owned By Root - Set log_file From log_file_line
    if Not Set Already
  ansible.builtin.set_fact:
    log_file: '{{ log_file_line }}'
  when:
  - '"auditd" in ansible_facts.packages'
  - '"linux-base" in ansible_facts.packages'
  - (log_file_line is defined) and (log_file_line | length > 0)
  tags:
  - CJIS-5.4.1.1
  - DISA-STIG-UBTU-20-010124
  - NIST-800-171-3.3.1
  - NIST-800-53-AC-6(1)
  - NIST-800-53-AU-9(4)
  - NIST-800-53-CM-6(a)
  - PCI-DSS-Req-10.5.1
  - PCI-DSSv4-10.3
  - PCI-DSSv4-10.3.2
  - file_group_ownership_var_log_audit
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy

- name: System Audit Logs Must Be Group Owned By Root - List All Log File Backups
  ansible.builtin.find:
    path: '{{ log_file | dirname }}'
    patterns: '{{ log_file | basename }}.*'
  register: backup_files
  when:
  - '"auditd" in ansible_facts.packages'
  - '"linux-base" in ansible_facts.packages'
  tags:
  - CJIS-5.4.1.1
  - DISA-STIG-UBTU-20-010124
  - NIST-800-171-3.3.1
  - NIST-800-53-AC-6(1)
  - NIST-800-53-AU-9(4)
  - NIST-800-53-CM-6(a)
  - PCI-DSS-Req-10.5.1
  - PCI-DSSv4-10.3
  - PCI-DSSv4-10.3.2
  - file_group_ownership_var_log_audit
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy

- name: System Audit Logs Must Be Group Owned By Root - Apply Mode to All Backup Log
    Files
  ansible.builtin.file:
    path: '{{ item }}'
    group: root
  failed_when: false
  loop: '{{ backup_files.files| map(attribute=''path'') | list }}'
  when:
  - '"auditd" in ansible_facts.packages'
  - '"linux-base" in ansible_facts.packages'
  tags:
  - CJIS-5.4.1.1
  - DISA-STIG-UBTU-20-010124
  - NIST-800-171-3.3.1
  - NIST-800-53-AC-6(1)
  - NIST-800-53-AU-9(4)
  - NIST-800-53-CM-6(a)
  - PCI-DSS-Req-10.5.1
  - PCI-DSSv4-10.3
  - PCI-DSSv4-10.3.2
  - file_group_ownership_var_log_audit
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy

- name: System Audit Logs Must Be Group Owned By Root - Apply Mode to Log File
  ansible.builtin.file:
    path: '{{ log_file }}'
    group: root
  failed_when: false
  when:
  - '"auditd" in ansible_facts.packages'
  - '"linux-base" in ansible_facts.packages'
  tags:
  - CJIS-5.4.1.1
  - DISA-STIG-UBTU-20-010124
  - NIST-800-171-3.3.1
  - NIST-800-53-AC-6(1)
  - NIST-800-53-AU-9(4)
  - NIST-800-53-CM-6(a)
  - PCI-DSS-Req-10.5.1
  - PCI-DSSv4-10.3
  - PCI-DSSv4-10.3.2
  - file_group_ownership_var_log_audit
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
```
