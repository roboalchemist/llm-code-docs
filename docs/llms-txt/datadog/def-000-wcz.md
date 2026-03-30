# Source: https://docs.datadoghq.com/security/default_rules/def-000-wcz.md

---
title: Set existing passwords a period of inactivity before they been locked
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Set existing passwords a period of
  inactivity before they been locked
---

# Set existing passwords a period of inactivity before they been locked

## Description{% #description %}

Configure user accounts that have been inactive for over a given period of time to be automatically disabled by running the following command:

```
$ sudo chage --inactive 30USER

```

## Rationale{% #rationale %}

Inactive accounts pose a threat to system security since the users are not logging in to notice failed login attempts or other anomalies.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

var_account_disable_post_pw_expiration='30'


while IFS= read -r i; do
    chage --inactive $var_account_disable_post_pw_expiration $i
done <   <(awk -v var="$var_account_disable_post_pw_expiration" -F: '(($7 > var || $7 == "") && $2 ~ /^\$/) {print $1}' /etc/shadow)
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```gdscript3
- name: XCCDF Value var_account_disable_post_pw_expiration # promote to variable
  set_fact:
    var_account_disable_post_pw_expiration: !!str 30
  tags:
    - always

- name: Collect users with not correct INACTIVE parameter set
  ansible.builtin.command:
    cmd: awk -F':' '(($7 > {{ var_account_disable_post_pw_expiration }} || $7 == "")
      && $2 ~ /^\$/) {print $1}' /etc/shadow
  register: user_names
  changed_when: false
  tags:
  - CCE-86757-2
  - NIST-800-171-3.5.6
  - NIST-800-53-AC-2(3)
  - NIST-800-53-CM-6(a)
  - NIST-800-53-IA-4(e)
  - PCI-DSS-Req-8.1.4
  - PCI-DSSv4-8.2.6
  - accounts_set_post_pw_existing
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy

- name: Change the period of inactivity
  ansible.builtin.command:
    cmd: chage --inactive {{ var_account_disable_post_pw_expiration }} {{ item }}
  with_items: '{{ user_names.stdout_lines }}'
  when: user_names is not skipped and user_names.stdout_lines | length > 0
  tags:
  - CCE-86757-2
  - NIST-800-171-3.5.6
  - NIST-800-53-AC-2(3)
  - NIST-800-53-CM-6(a)
  - NIST-800-53-IA-4(e)
  - PCI-DSS-Req-8.1.4
  - PCI-DSSv4-8.2.6
  - accounts_set_post_pw_existing
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
```
