# Source: https://docs.datadoghq.com/security/default_rules/def-000-q7i.md

---
title: Configure AIDE to Verify the Audit Tools
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Configure AIDE to Verify the Audit
  Tools
---

# Configure AIDE to Verify the Audit Tools
 
## Description{% #description %}

The operating system file integrity tool must be configured to protect the integrity of the audit tools.

## Rationale{% #rationale %}

Protecting the integrity of the tools used for auditing purposes is a critical step toward ensuring the integrity of audit information. Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit information system activity. Audit tools include but are not limited to vendor-provided and open-source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators. It is not uncommon for attackers to replace the audit tools or inject code into the existing tools to provide the capability to hide or erase system activity from the audit logs. To address this risk, audit tools must be cryptographically signed to provide the capability to identify when the audit tools have been modified, manipulated, or replaced. An example is a checksum hash of the file or files.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'linux-base' 2>/dev/null | grep -q '^installed$'; then

DEBIAN_FRONTEND=noninteractive apt-get install -y "aide"










if grep -i '^.*/usr/sbin/auditctl.*$' /etc/aide/aide.conf; then
sed -i "s#.*/usr/sbin/auditctl.*#/usr/sbin/auditctl p+i+n+u+g+s+b+acl+xattrs+sha512#" /etc/aide/aide.conf
else
echo "/usr/sbin/auditctl p+i+n+u+g+s+b+acl+xattrs+sha512" >> /etc/aide/aide.conf
fi

if grep -i '^.*/usr/sbin/auditd.*$' /etc/aide/aide.conf; then
sed -i "s#.*/usr/sbin/auditd.*#/usr/sbin/auditd p+i+n+u+g+s+b+acl+xattrs+sha512#" /etc/aide/aide.conf
else
echo "/usr/sbin/auditd p+i+n+u+g+s+b+acl+xattrs+sha512" >> /etc/aide/aide.conf
fi

if grep -i '^.*/usr/sbin/ausearch.*$' /etc/aide/aide.conf; then
sed -i "s#.*/usr/sbin/ausearch.*#/usr/sbin/ausearch p+i+n+u+g+s+b+acl+xattrs+sha512#" /etc/aide/aide.conf
else
echo "/usr/sbin/ausearch p+i+n+u+g+s+b+acl+xattrs+sha512" >> /etc/aide/aide.conf
fi

if grep -i '^.*/usr/sbin/aureport.*$' /etc/aide/aide.conf; then
sed -i "s#.*/usr/sbin/aureport.*#/usr/sbin/aureport p+i+n+u+g+s+b+acl+xattrs+sha512#" /etc/aide/aide.conf
else
echo "/usr/sbin/aureport p+i+n+u+g+s+b+acl+xattrs+sha512" >> /etc/aide/aide.conf
fi

if grep -i '^.*/usr/sbin/autrace.*$' /etc/aide/aide.conf; then
sed -i "s#.*/usr/sbin/autrace.*#/usr/sbin/autrace p+i+n+u+g+s+b+acl+xattrs+sha512#" /etc/aide/aide.conf
else
echo "/usr/sbin/autrace p+i+n+u+g+s+b+acl+xattrs+sha512" >> /etc/aide/aide.conf
fi

if grep -i '^.*/usr/sbin/augenrules.*$' /etc/aide/aide.conf; then
sed -i "s#.*/usr/sbin/augenrules.*#/usr/sbin/augenrules p+i+n+u+g+s+b+acl+xattrs+sha512#" /etc/aide/aide.conf
else
echo "/usr/sbin/augenrules p+i+n+u+g+s+b+acl+xattrs+sha512" >> /etc/aide/aide.conf
fi

if grep -i '^.*/usr/sbin/audispd.*$' /etc/aide/aide.conf; then
sed -i "s#.*/usr/sbin/audispd.*#/usr/sbin/audispd p+i+n+u+g+s+b+acl+xattrs+sha512#" /etc/aide/aide.conf
else
echo "/usr/sbin/audispd p+i+n+u+g+s+b+acl+xattrs+sha512" >> /etc/aide/aide.conf
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
  - DISA-STIG-UBTU-20-010205
  - NIST-800-53-AU-9(3)
  - NIST-800-53-AU-9(3).1
  - aide_check_audit_tools
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy

- name: Configure AIDE to Verify the Audit Tools - Gather List of Packages
  tags:
  - DISA-STIG-UBTU-20-010205
  - NIST-800-53-AU-9(3)
  - NIST-800-53-AU-9(3).1
  - aide_check_audit_tools
  - aide_check_audit_tools
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
  ansible.builtin.package_facts:
    manager: auto
  when: '"linux-base" in ansible_facts.packages'

- name: Ensure aide is installed
  package:
    name: '{{ item }}'
    state: present
  with_items:
  - aide
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - DISA-STIG-UBTU-20-010205
  - NIST-800-53-AU-9(3)
  - NIST-800-53-AU-9(3).1
  - aide_check_audit_tools
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy

- name: Set audit_tools fact
  set_fact:
    audit_tools:
    - /usr/sbin/audispd
    - /usr/sbin/auditctl
    - /usr/sbin/auditd
    - /usr/sbin/augenrules
    - /usr/sbin/aureport
    - /usr/sbin/ausearch
    - /usr/sbin/autrace
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - DISA-STIG-UBTU-20-010205
  - NIST-800-53-AU-9(3)
  - NIST-800-53-AU-9(3).1
  - aide_check_audit_tools
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy

- name: Ensure existing AIDE configuration for audit tools are correct
  lineinfile:
    path: /etc/aide/aide.conf
    regexp: ^{{ item }}\s
    line: '{{ item }} p+i+n+u+g+s+b+acl+xattrs+sha512'
  with_items: '{{ audit_tools }}'
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - DISA-STIG-UBTU-20-010205
  - NIST-800-53-AU-9(3)
  - NIST-800-53-AU-9(3).1
  - aide_check_audit_tools
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy

- name: Configure AIDE to properly protect audit tools
  lineinfile:
    path: /etc/aide/aide.conf
    line: '{{ item }} p+i+n+u+g+s+b+acl+xattrs+sha512'
  with_items: '{{ audit_tools }}'
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - DISA-STIG-UBTU-20-010205
  - NIST-800-53-AU-9(3)
  - NIST-800-53-AU-9(3).1
  - aide_check_audit_tools
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
```
