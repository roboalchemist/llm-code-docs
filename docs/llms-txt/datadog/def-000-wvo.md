# Source: https://docs.datadoghq.com/security/default_rules/def-000-wvo.md

---
title: Enforce Usage of pam_wheel with Group Parameter for su Authentication
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Enforce Usage of pam_wheel with Group
  Parameter for su Authentication
---

# Enforce Usage of pam_wheel with Group Parameter for su Authentication

## Description{% #description %}

To ensure that only users who are members of the group set in the `group` option of `pam_wheel.so` module can run commands with altered privileges through the `su` command, make sure that the following line exists in the file `/etc/pam.d/su`:

```
auth required pam_wheel.so use_uid group=sugroup

```

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


PAM_CONF=/etc/pam.d/su

pamstr=$(grep -P '^auth\s+required\s+pam_wheel\.so\s+(?=[^#]*\buse_uid\b)(?=[^#]*\bgroup=)' ${PAM_CONF})
if [ -z "$pamstr" ]; then
    sed -Ei '/^auth\b.*\brequired\b.*\bpam_wheel\.so/d' ${PAM_CONF} # remove any remaining uncommented pam_wheel.so line
    sed -Ei "/^auth\s+sufficient\s+pam_rootok\.so.*$/a auth             required        pam_wheel.so use_uid group=${var_pam_wheel_group_for_su}" ${PAM_CONF}
else
    group_val=$(echo -n "$pamstr" | grep -Eo '\bgroup=[_a-z][-0-9_a-z]*' | cut -d '=' -f 2)
    if [ -z "${group_val}" ] || [ ${group_val} != ${var_pam_wheel_group_for_su} ]; then
        sed -Ei "s/(^auth\s+required\s+pam_wheel.so\s+[^#]*group=)[_a-z][-0-9_a-z]*/\1${var_pam_wheel_group_for_su}/" ${PAM_CONF}
    fi
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
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.6
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
  - use_pam_wheel_group_for_su
- name: XCCDF Value var_pam_wheel_group_for_su # promote to variable
  set_fact:
    var_pam_wheel_group_for_su: !!str sugroup
  tags:
    - always

- name: Enforce Usage of pam_wheel with Group Parameter for su Authentication - Add
    the group to the /etc/pam.d/su file
  ansible.builtin.lineinfile:
    path: /etc/pam.d/su
    state: present
    regexp: ^[\s]*#[\s]*auth[\s]+required[\s]+pam_wheel\.so[\s]+use_uid group=$
    line: auth             required        pam_wheel.so use_uid group={{ var_pam_wheel_group_for_su
      }}
  when: '"libpam-runtime" in ansible_facts.packages'
  tags:
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.6
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
  - use_pam_wheel_group_for_su
```

## Warning{% #warning %}

Note that `ensure_pam_wheel_group_empty` rule complements this requirement by ensuring the referenced group exists and has no members.
