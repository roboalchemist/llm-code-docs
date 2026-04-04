# Source: https://docs.datadoghq.com/security/default_rules/def-000-fly.md

---
title: Verify that audit tools are owned by root
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Verify that audit tools are owned by
  root
---

# Verify that audit tools are owned by root

## Description{% #description %}

The Ubuntu 20.04 operating system audit tools must have the proper ownership configured to protected against unauthorized access. Verify it by running the following command:

```
$ stat -c "%n %U" /sbin/auditctl /sbin/aureport /sbin/ausearch /sbin/autrace /sbin/auditd /sbin/audispd /sbin/augenrules /sbin/audisp-syslog

/sbin/auditctl root
/sbin/aureport root
/sbin/ausearch root
/sbin/autrace root
/sbin/auditd root
/sbin/audispd root
/sbin/augenrules root
```

Audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators

## Rationale{% #rationale %}

Protecting audit information also includes identifying and protecting the tools used to view and manipulate log data. Therefore, protecting audit tools is necessary to prevent unauthorized operation on audit information. Operating systems providing tools to interface with audit information will leverage user permissions and roles identifying the user accessing the tools and the corresponding rights the user enjoys to make access decisions regarding the access to audit tools.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'linux-base' 2>/dev/null | grep -q '^installed$'; then

if id "0" >/dev/null 2>&1; then
  newown="0"
fi
if [[ -z ${newown} ]]; then
  echo "0 is not a defined user on the system"
  exit 1
fi
chown $newown /sbin/auditctl
chown $newown /sbin/aureport
chown $newown /sbin/ausearch
chown $newown /sbin/autrace
chown $newown /sbin/auditd
chown $newown /sbin/audispd
chown $newown /sbin/augenrules

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
  - DISA-STIG-UBTU-20-010200
  - configure_strategy
  - file_ownership_audit_binaries
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Set the file_ownership_audit_binaries_newown variable if represented by uid
  set_fact:
    file_ownership_audit_binaries_newown: '0'
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - DISA-STIG-UBTU-20-010200
  - configure_strategy
  - file_ownership_audit_binaries
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Test for existence /sbin/auditctl
  stat:
    path: /sbin/auditctl
  register: file_exists
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - DISA-STIG-UBTU-20-010200
  - configure_strategy
  - file_ownership_audit_binaries
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Ensure owner on /sbin/auditctl
  file:
    path: /sbin/auditctl
    owner: '{{ file_ownership_audit_binaries_newown }}'
  when:
  - '"linux-base" in ansible_facts.packages'
  - file_exists.stat is defined and file_exists.stat.exists
  tags:
  - DISA-STIG-UBTU-20-010200
  - configure_strategy
  - file_ownership_audit_binaries
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Test for existence /sbin/aureport
  stat:
    path: /sbin/aureport
  register: file_exists
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - DISA-STIG-UBTU-20-010200
  - configure_strategy
  - file_ownership_audit_binaries
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Ensure owner on /sbin/aureport
  file:
    path: /sbin/aureport
    owner: '{{ file_ownership_audit_binaries_newown }}'
  when:
  - '"linux-base" in ansible_facts.packages'
  - file_exists.stat is defined and file_exists.stat.exists
  tags:
  - DISA-STIG-UBTU-20-010200
  - configure_strategy
  - file_ownership_audit_binaries
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Test for existence /sbin/ausearch
  stat:
    path: /sbin/ausearch
  register: file_exists
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - DISA-STIG-UBTU-20-010200
  - configure_strategy
  - file_ownership_audit_binaries
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Ensure owner on /sbin/ausearch
  file:
    path: /sbin/ausearch
    owner: '{{ file_ownership_audit_binaries_newown }}'
  when:
  - '"linux-base" in ansible_facts.packages'
  - file_exists.stat is defined and file_exists.stat.exists
  tags:
  - DISA-STIG-UBTU-20-010200
  - configure_strategy
  - file_ownership_audit_binaries
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Test for existence /sbin/autrace
  stat:
    path: /sbin/autrace
  register: file_exists
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - DISA-STIG-UBTU-20-010200
  - configure_strategy
  - file_ownership_audit_binaries
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Ensure owner on /sbin/autrace
  file:
    path: /sbin/autrace
    owner: '{{ file_ownership_audit_binaries_newown }}'
  when:
  - '"linux-base" in ansible_facts.packages'
  - file_exists.stat is defined and file_exists.stat.exists
  tags:
  - DISA-STIG-UBTU-20-010200
  - configure_strategy
  - file_ownership_audit_binaries
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Test for existence /sbin/auditd
  stat:
    path: /sbin/auditd
  register: file_exists
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - DISA-STIG-UBTU-20-010200
  - configure_strategy
  - file_ownership_audit_binaries
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Ensure owner on /sbin/auditd
  file:
    path: /sbin/auditd
    owner: '{{ file_ownership_audit_binaries_newown }}'
  when:
  - '"linux-base" in ansible_facts.packages'
  - file_exists.stat is defined and file_exists.stat.exists
  tags:
  - DISA-STIG-UBTU-20-010200
  - configure_strategy
  - file_ownership_audit_binaries
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Test for existence /sbin/audispd
  stat:
    path: /sbin/audispd
  register: file_exists
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - DISA-STIG-UBTU-20-010200
  - configure_strategy
  - file_ownership_audit_binaries
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Ensure owner on /sbin/audispd
  file:
    path: /sbin/audispd
    owner: '{{ file_ownership_audit_binaries_newown }}'
  when:
  - '"linux-base" in ansible_facts.packages'
  - file_exists.stat is defined and file_exists.stat.exists
  tags:
  - DISA-STIG-UBTU-20-010200
  - configure_strategy
  - file_ownership_audit_binaries
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Test for existence /sbin/augenrules
  stat:
    path: /sbin/augenrules
  register: file_exists
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - DISA-STIG-UBTU-20-010200
  - configure_strategy
  - file_ownership_audit_binaries
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Ensure owner on /sbin/augenrules
  file:
    path: /sbin/augenrules
    owner: '{{ file_ownership_audit_binaries_newown }}'
  when:
  - '"linux-base" in ansible_facts.packages'
  - file_exists.stat is defined and file_exists.stat.exists
  tags:
  - DISA-STIG-UBTU-20-010200
  - configure_strategy
  - file_ownership_audit_binaries
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
```
