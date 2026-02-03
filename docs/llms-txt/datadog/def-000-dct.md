# Source: https://docs.datadoghq.com/security/default_rules/def-000-dct.md

---
title: Ensure the Group Used by pam_wheel.so Module Exists on System and is Empty
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Ensure the Group Used by pam_wheel.so
  Module Exists on System and is Empty
---

# Ensure the Group Used by pam_wheel.so Module Exists on System and is Empty
 
## Description{% #description %}

Ensure that the group `sugroup` referenced by `var_pam_wheel_group_for_su` variable and used as value for the `pam_wheel.so` `group` option exists and has no members. This empty group used by `pam_wheel.so` in `/etc/pam.d/su` ensures that no user can run commands with altered privileges through the `su` command.

## Rationale{% #rationale %}

The `su` program allows to run commands with a substitute user and group ID. It is commonly used to run commands as the root user. Limiting access to such command is considered a good security practice.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'libpam-runtime' 2>/dev/null | grep -q '^installed$'; then

var_pam_wheel_group_for_su='sugroup'


if ! grep -q "^${var_pam_wheel_group_for_su}:[^:]*:[^:]*:[^:]*" /etc/group; then
    groupadd ${var_pam_wheel_group_for_su}
fi

# group must be empty
gpasswd -M '' ${var_pam_wheel_group_for_su}

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
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.6
  - ensure_pam_wheel_group_empty
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
- name: XCCDF Value var_pam_wheel_group_for_su # promote to variable
  set_fact:
    var_pam_wheel_group_for_su: !!str sugroup
  tags:
    - always

- name: Ensure the Group Used by pam_wheel.so Module Exists on System and is Empty
    - Ensure {{ var_pam_wheel_group_for_su }} Group Exists
  ansible.builtin.group:
    name: '{{ var_pam_wheel_group_for_su }}'
    state: present
  when: '"libpam-runtime" in ansible_facts.packages'
  tags:
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.6
  - ensure_pam_wheel_group_empty
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy

- name: Ensure the Group Used by pam_wheel.so Module Exists on System and is Empty
    - Ensure {{ var_pam_wheel_group_for_su }} Group is Empty
  ansible.builtin.lineinfile:
    path: /etc/group
    regexp: ^({{ var_pam_wheel_group_for_su }}:[^:]+:[0-9]+:).*$
    line: \1
    backrefs: true
  when: '"libpam-runtime" in ansible_facts.packages'
  tags:
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.6
  - ensure_pam_wheel_group_empty
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
```

## Warning{% #warning %}

Note that this rule just ensures the group exists and has no members. This rule does not configure `pam_wheel.so` module. The `pam_wheel.so` module configuration is accomplished by `use_pam_wheel_group_for_su` rule.
