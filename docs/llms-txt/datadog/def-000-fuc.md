# Source: https://docs.datadoghq.com/security/default_rules/def-000-fuc.md

---
title: Ensure Users Re-Authenticate for Privilege Escalation - sudo
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Ensure Users Re-Authenticate for
  Privilege Escalation - sudo
---

# Ensure Users Re-Authenticate for Privilege Escalation - sudo

## Description{% #description %}

The sudo `NOPASSWD` and `!authenticate` option, when specified, allows a user to execute commands using sudo without having to authenticate. This should be disabled by making sure that `NOPASSWD` and/or `!authenticate` do not exist in `/etc/sudoers` configuration file or any sudo configuration snippets in `/etc/sudoers.d/`."

## Rationale{% #rationale %}

Without re-authentication, users may access resources or perform tasks for which they do not have authorization.

When operating systems provide the capability to escalate a functional capability, it is critical that the user re-authenticate.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

for f in /etc/sudoers /etc/sudoers.d/* ; do
  if [ ! -e "$f" ] ; then
    continue
  fi
  matching_list=$(grep -P '^(?!#).*[\s]+NOPASSWD[\s]*\:.*$' $f | uniq )
  if ! test -z "$matching_list"; then
    while IFS= read -r entry; do
      # comment out "NOPASSWD" matches to preserve user data
      sed -i "s|^${entry}$|# &|g" $f
    done <<< "$matching_list"

    /usr/sbin/visudo -cf $f &> /dev/null || echo "Fail to validate $f with visudo"
  fi
done

for f in /etc/sudoers /etc/sudoers.d/* ; do
  if [ ! -e "$f" ] ; then
    continue
  fi
  matching_list=$(grep -P '^(?!#).*[\s]+\!authenticate.*$' $f | uniq )
  if ! test -z "$matching_list"; then
    while IFS= read -r entry; do
      # comment out "!authenticate" matches to preserve user data
      sed -i "s|^${entry}$|# &|g" $f
    done <<< "$matching_list"

    /usr/sbin/visudo -cf $f &> /dev/null || echo "Fail to validate $f with visudo"
  fi
done
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```
- name: Find /etc/sudoers.d/ files
  ansible.builtin.find:
    paths:
    - /etc/sudoers.d/
  register: sudoers
  tags:
  - DISA-STIG-UBTU-20-010014
  - NIST-800-53-CM-6(a)
  - NIST-800-53-IA-11
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.6
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
  - sudo_require_authentication

- name: Remove lines containing NOPASSWD from sudoers files
  ansible.builtin.replace:
    regexp: (^(?!#).*[\s]+NOPASSWD[\s]*\:.*$)
    replace: '# \g<1>'
    path: '{{ item.path }}'
    validate: /usr/sbin/visudo -cf %s
  with_items:
  - path: /etc/sudoers
  - '{{ sudoers.files }}'
  tags:
  - DISA-STIG-UBTU-20-010014
  - NIST-800-53-CM-6(a)
  - NIST-800-53-IA-11
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.6
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
  - sudo_require_authentication

- name: Find /etc/sudoers.d/ files
  ansible.builtin.find:
    paths:
    - /etc/sudoers.d/
  register: sudoers
  tags:
  - DISA-STIG-UBTU-20-010014
  - NIST-800-53-CM-6(a)
  - NIST-800-53-IA-11
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.6
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
  - sudo_require_authentication

- name: Remove lines containing !authenticate from sudoers files
  ansible.builtin.replace:
    regexp: (^(?!#).*[\s]+\!authenticate.*$)
    replace: '# \g<1>'
    path: '{{ item.path }}'
    validate: /usr/sbin/visudo -cf %s
  with_items:
  - path: /etc/sudoers
  - '{{ sudoers.files }}'
  tags:
  - DISA-STIG-UBTU-20-010014
  - NIST-800-53-CM-6(a)
  - NIST-800-53-IA-11
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.6
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
  - sudo_require_authentication
```
