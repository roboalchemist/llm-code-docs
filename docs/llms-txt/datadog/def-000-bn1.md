# Source: https://docs.datadoghq.com/security/default_rules/def-000-bn1.md

---
title: Verify that audit tools are owned by group root
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Verify that audit tools are owned by
  group root
---

# Verify that audit tools are owned by group root
 
## Description{% #description %}

The Ubuntu 20.04 operating system audit tools must have the proper ownership configured to protected against unauthorized access. Verify it by running the following command:

```
$ stat -c "%n %G" /sbin/auditctl /sbin/aureport /sbin/ausearch /sbin/autrace /sbin/auditd /sbin/audispd /sbin/augenrules

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

if getent group "0" >/dev/null 2>&1; then
  newgroup="0"
fi
if [[ -z ${newgroup} ]]; then
  echo "0 is not a defined group on the system"
  exit 1
fi
chgrp $newgroup /sbin/auditctl
chgrp $newgroup /sbin/aureport
chgrp $newgroup /sbin/ausearch
chgrp $newgroup /sbin/autrace
chgrp $newgroup /sbin/auditd
chgrp $newgroup /sbin/audispd
chgrp $newgroup /sbin/augenrules

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
  - DISA-STIG-UBTU-20-010201
  - configure_strategy
  - file_groupownership_audit_binaries
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Set the file_groupownership_audit_binaries_newgroup variable if represented
    by gid
  set_fact:
    file_groupownership_audit_binaries_newgroup: '0'
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - DISA-STIG-UBTU-20-010201
  - configure_strategy
  - file_groupownership_audit_binaries
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
  - DISA-STIG-UBTU-20-010201
  - configure_strategy
  - file_groupownership_audit_binaries
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Ensure group owner on /sbin/auditctl
  file:
    path: /sbin/auditctl
    group: '{{ file_groupownership_audit_binaries_newgroup }}'
  when:
  - '"linux-base" in ansible_facts.packages'
  - file_exists.stat is defined and file_exists.stat.exists
  tags:
  - DISA-STIG-UBTU-20-010201
  - configure_strategy
  - file_groupownership_audit_binaries
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
  - DISA-STIG-UBTU-20-010201
  - configure_strategy
  - file_groupownership_audit_binaries
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Ensure group owner on /sbin/aureport
  file:
    path: /sbin/aureport
    group: '{{ file_groupownership_audit_binaries_newgroup }}'
  when:
  - '"linux-base" in ansible_facts.packages'
  - file_exists.stat is defined and file_exists.stat.exists
  tags:
  - DISA-STIG-UBTU-20-010201
  - configure_strategy
  - file_groupownership_audit_binaries
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
  - DISA-STIG-UBTU-20-010201
  - configure_strategy
  - file_groupownership_audit_binaries
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Ensure group owner on /sbin/ausearch
  file:
    path: /sbin/ausearch
    group: '{{ file_groupownership_audit_binaries_newgroup }}'
  when:
  - '"linux-base" in ansible_facts.packages'
  - file_exists.stat is defined and file_exists.stat.exists
  tags:
  - DISA-STIG-UBTU-20-010201
  - configure_strategy
  - file_groupownership_audit_binaries
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
  - DISA-STIG-UBTU-20-010201
  - configure_strategy
  - file_groupownership_audit_binaries
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Ensure group owner on /sbin/autrace
  file:
    path: /sbin/autrace
    group: '{{ file_groupownership_audit_binaries_newgroup }}'
  when:
  - '"linux-base" in ansible_facts.packages'
  - file_exists.stat is defined and file_exists.stat.exists
  tags:
  - DISA-STIG-UBTU-20-010201
  - configure_strategy
  - file_groupownership_audit_binaries
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
  - DISA-STIG-UBTU-20-010201
  - configure_strategy
  - file_groupownership_audit_binaries
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Ensure group owner on /sbin/auditd
  file:
    path: /sbin/auditd
    group: '{{ file_groupownership_audit_binaries_newgroup }}'
  when:
  - '"linux-base" in ansible_facts.packages'
  - file_exists.stat is defined and file_exists.stat.exists
  tags:
  - DISA-STIG-UBTU-20-010201
  - configure_strategy
  - file_groupownership_audit_binaries
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
  - DISA-STIG-UBTU-20-010201
  - configure_strategy
  - file_groupownership_audit_binaries
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Ensure group owner on /sbin/audispd
  file:
    path: /sbin/audispd
    group: '{{ file_groupownership_audit_binaries_newgroup }}'
  when:
  - '"linux-base" in ansible_facts.packages'
  - file_exists.stat is defined and file_exists.stat.exists
  tags:
  - DISA-STIG-UBTU-20-010201
  - configure_strategy
  - file_groupownership_audit_binaries
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
  - DISA-STIG-UBTU-20-010201
  - configure_strategy
  - file_groupownership_audit_binaries
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Ensure group owner on /sbin/augenrules
  file:
    path: /sbin/augenrules
    group: '{{ file_groupownership_audit_binaries_newgroup }}'
  when:
  - '"linux-base" in ansible_facts.packages'
  - file_exists.stat is defined and file_exists.stat.exists
  tags:
  - DISA-STIG-UBTU-20-010201
  - configure_strategy
  - file_groupownership_audit_binaries
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
```
