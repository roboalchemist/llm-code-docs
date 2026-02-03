# Source: https://docs.datadoghq.com/security/default_rules/def-000-u2v.md

---
title: Ensure the Default Umask is Set Correctly in login.defs
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Ensure the Default Umask is Set
  Correctly in login.defs
---

# Ensure the Default Umask is Set Correctly in login.defs
 
## Description{% #description %}

To ensure the default umask controlled by `/etc/login.defs` is set properly, add or correct the `UMASK` setting in `/etc/login.defs` to read as follows:

```
UMASK 027
         
```

## Rationale{% #rationale %}

The umask value influences the permissions assigned to files when they are created. A misconfigured umask value could result in files with excessive permissions that can be read and written to by unauthorized users.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'login' 2>/dev/null | grep -q '^installed$'; then

var_accounts_user_umask='027'


# Strip any search characters in the key arg so that the key can be replaced without
# adding any search characters to the config file.
stripped_key=$(sed 's/[\^=\$,;+]*//g' <<< "^UMASK")

# shellcheck disable=SC2059
printf -v formatted_output "%s %s" "$stripped_key" "$var_accounts_user_umask"

# If the key exists, change it. Otherwise, add it to the config_file.
# We search for the key string followed by a word boundary (matched by \>),
# so if we search for 'setting', 'setting2' won't match.
if LC_ALL=C grep -q -m 1 -i -e "^UMASK\\>" "/etc/login.defs"; then
    escaped_formatted_output=$(sed -e 's|/|\\/|g' <<< "$formatted_output")
    LC_ALL=C sed -i --follow-symlinks "s/^UMASK\\>.*/$escaped_formatted_output/gi" "/etc/login.defs"
else
    if [[ -s "/etc/login.defs" ]] && [[ -n "$(tail -c 1 -- "/etc/login.defs" || true)" ]]; then
        LC_ALL=C sed -i --follow-symlinks '$a'\\ "/etc/login.defs"
    fi
    printf '%s\n' "$formatted_output" >> "/etc/login.defs"
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
  - DISA-STIG-UBTU-20-010016
  - NIST-800-53-AC-6(1)
  - NIST-800-53-CM-6(a)
  - accounts_umask_etc_login_defs
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
- name: XCCDF Value var_accounts_user_umask # promote to variable
  set_fact:
    var_accounts_user_umask: !!str 027
  tags:
    - always

- name: Check if UMASK is already set
  ansible.builtin.lineinfile:
    path: /etc/login.defs
    regexp: ^(\s*)UMASK\s+.*
    state: absent
  check_mode: true
  changed_when: false
  register: result_umask_is_set
  when: '"login" in ansible_facts.packages'
  tags:
  - DISA-STIG-UBTU-20-010016
  - NIST-800-53-AC-6(1)
  - NIST-800-53-CM-6(a)
  - accounts_umask_etc_login_defs
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy

- name: Replace user UMASK in /etc/login.defs
  ansible.builtin.replace:
    path: /etc/login.defs
    regexp: ^(\s*)UMASK(\s+).*
    replace: \g<1>UMASK\g<2>{{ var_accounts_user_umask }}
  when:
  - '"login" in ansible_facts.packages'
  - result_umask_is_set.found > 0
  tags:
  - DISA-STIG-UBTU-20-010016
  - NIST-800-53-AC-6(1)
  - NIST-800-53-CM-6(a)
  - accounts_umask_etc_login_defs
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy

- name: Ensure the Default UMASK is Appended Correctly
  ansible.builtin.lineinfile:
    create: true
    path: /etc/login.defs
    line: UMASK {{ var_accounts_user_umask }}
  when:
  - '"login" in ansible_facts.packages'
  - result_umask_is_set.found == 0
  tags:
  - DISA-STIG-UBTU-20-010016
  - NIST-800-53-AC-6(1)
  - NIST-800-53-CM-6(a)
  - accounts_umask_etc_login_defs
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
```
