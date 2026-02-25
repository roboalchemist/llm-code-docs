# Source: https://docs.datadoghq.com/security/default_rules/def-000-x2k.md

---
title: Verify that audit tools Have Mode 0755 or less
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Verify that audit tools Have Mode 0755
  or less
---

# Verify that audit tools Have Mode 0755 or less

## Description{% #description %}

The Ubuntu 20.04 operating system audit tools must have the proper permissions configured to protected against unauthorized access. Verify it by running the following command:

```
$ stat -c "%n %a" /sbin/auditctl /sbin/aureport /sbin/ausearch /sbin/autrace /sbin/auditd /sbin/audispd /sbin/augenrules

/sbin/auditctl 755
/sbin/aureport 755
/sbin/ausearch 755
/sbin/autrace 755
/sbin/auditd 755
/sbin/audispd 755
/sbin/augenrules 755
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

chmod u-s,g-ws,o-wt /sbin/auditctl

chmod u-s,g-ws,o-wt /sbin/aureport

chmod u-s,g-ws,o-wt /sbin/ausearch

chmod u-s,g-ws,o-wt /sbin/autrace

chmod u-s,g-ws,o-wt /sbin/auditd

chmod u-s,g-ws,o-wt /sbin/audispd

chmod u-s,g-ws,o-wt /sbin/augenrules

else
    >&2 echo 'Remediation is not applicable, nothing was done'
fi
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```zed
- name: Gather the package facts
  package_facts:
    manager: auto
  tags:
  - DISA-STIG-UBTU-20-010199
  - configure_strategy
  - file_permissions_audit_binaries
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
  - DISA-STIG-UBTU-20-010199
  - configure_strategy
  - file_permissions_audit_binaries
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Ensure permission u-s,g-ws,o-wt on /sbin/auditctl
  file:
    path: /sbin/auditctl
    mode: u-s,g-ws,o-wt
  when:
  - '"linux-base" in ansible_facts.packages'
  - file_exists.stat is defined and file_exists.stat.exists
  tags:
  - DISA-STIG-UBTU-20-010199
  - configure_strategy
  - file_permissions_audit_binaries
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
  - DISA-STIG-UBTU-20-010199
  - configure_strategy
  - file_permissions_audit_binaries
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Ensure permission u-s,g-ws,o-wt on /sbin/aureport
  file:
    path: /sbin/aureport
    mode: u-s,g-ws,o-wt
  when:
  - '"linux-base" in ansible_facts.packages'
  - file_exists.stat is defined and file_exists.stat.exists
  tags:
  - DISA-STIG-UBTU-20-010199
  - configure_strategy
  - file_permissions_audit_binaries
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
  - DISA-STIG-UBTU-20-010199
  - configure_strategy
  - file_permissions_audit_binaries
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Ensure permission u-s,g-ws,o-wt on /sbin/ausearch
  file:
    path: /sbin/ausearch
    mode: u-s,g-ws,o-wt
  when:
  - '"linux-base" in ansible_facts.packages'
  - file_exists.stat is defined and file_exists.stat.exists
  tags:
  - DISA-STIG-UBTU-20-010199
  - configure_strategy
  - file_permissions_audit_binaries
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
  - DISA-STIG-UBTU-20-010199
  - configure_strategy
  - file_permissions_audit_binaries
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Ensure permission u-s,g-ws,o-wt on /sbin/autrace
  file:
    path: /sbin/autrace
    mode: u-s,g-ws,o-wt
  when:
  - '"linux-base" in ansible_facts.packages'
  - file_exists.stat is defined and file_exists.stat.exists
  tags:
  - DISA-STIG-UBTU-20-010199
  - configure_strategy
  - file_permissions_audit_binaries
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
  - DISA-STIG-UBTU-20-010199
  - configure_strategy
  - file_permissions_audit_binaries
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Ensure permission u-s,g-ws,o-wt on /sbin/auditd
  file:
    path: /sbin/auditd
    mode: u-s,g-ws,o-wt
  when:
  - '"linux-base" in ansible_facts.packages'
  - file_exists.stat is defined and file_exists.stat.exists
  tags:
  - DISA-STIG-UBTU-20-010199
  - configure_strategy
  - file_permissions_audit_binaries
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
  - DISA-STIG-UBTU-20-010199
  - configure_strategy
  - file_permissions_audit_binaries
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Ensure permission u-s,g-ws,o-wt on /sbin/audispd
  file:
    path: /sbin/audispd
    mode: u-s,g-ws,o-wt
  when:
  - '"linux-base" in ansible_facts.packages'
  - file_exists.stat is defined and file_exists.stat.exists
  tags:
  - DISA-STIG-UBTU-20-010199
  - configure_strategy
  - file_permissions_audit_binaries
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
  - DISA-STIG-UBTU-20-010199
  - configure_strategy
  - file_permissions_audit_binaries
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Ensure permission u-s,g-ws,o-wt on /sbin/augenrules
  file:
    path: /sbin/augenrules
    mode: u-s,g-ws,o-wt
  when:
  - '"linux-base" in ansible_facts.packages'
  - file_exists.stat is defined and file_exists.stat.exists
  tags:
  - DISA-STIG-UBTU-20-010199
  - configure_strategy
  - file_permissions_audit_binaries
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
```
