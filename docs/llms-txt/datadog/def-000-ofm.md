# Source: https://docs.datadoghq.com/security/default_rules/def-000-ofm.md

---
title: Set Deny For Failed Password Attempts
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Set Deny For Failed Password Attempts
---

# Set Deny For Failed Password Attempts

## Description{% #description %}

The Ubuntu 20.04 operating system must lock an account after - at most - 5 consecutive invalid access attempts.

## Rationale{% #rationale %}

By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-force attacks, is reduced. Limits are imposed by locking the account. To configure the operating system to lock an account after three unsuccessful consecutive access attempts using `pam_tally2.so`, modify the content of both `/etc/pam.d/common-auth` and `/etc/pam.d/common-account` as follows:

- add or modify the `pam_tally2.so` module line in `/etc/pam.d/common-auth` to ensure both `onerr=fail` and `deny=5` are present. For example:
  ```
  auth required pam_tally2.so onerr=fail silent audit deny=5
  ```
- add or modify the following line in `/etc/pam.d/common-account`:
  ```
  account required pam_tally2.so
  ```

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'libpam-runtime' 2>/dev/null | grep -q '^installed$'; then

var_password_pam_tally2='5'

# Use a non-number regexp to force update of the value of the deny option






if ! grep -qP "^\s*auth\s+required\s+pam_tally2.so\s*.*" "/etc/pam.d/common-auth"; then
    # Line matching group + control + module was not found. Check group + module.
    if [ "$(grep -cP '^\s*auth\s+.*\s+pam_tally2.so\s*' "/etc/pam.d/common-auth")" -eq 1 ]; then
        # The control is updated only if one single line matches.
        sed -i -E --follow-symlinks "s/^(\s*auth\s+).*(\bpam_tally2.so.*)/\1required \2/" "/etc/pam.d/common-auth"
    else
        LAST_MATCH_LINE=$(grep -nP "(fail)" "/etc/pam.d/common-auth" | tail -n 1 | cut -d: -f 1)
        if [ ! -z $LAST_MATCH_LINE ]; then
            sed -i --follow-symlinks $LAST_MATCH_LINE" a auth     required    pam_tally2.so" "/etc/pam.d/common-auth"
        else
            echo "auth    required    pam_tally2.so" >> "/etc/pam.d/common-auth"
        fi
    fi
fi
# Check the option
if ! grep -qP "^\s*auth\s+required\s+pam_tally2.so\s*.*\sonerr\b" "/etc/pam.d/common-auth"; then
    sed -i -E --follow-symlinks "/\s*auth\s+required\s+pam_tally2.so.*/ s/$/ onerr=fail/" "/etc/pam.d/common-auth"
else
    sed -i -E --follow-symlinks "s/(\s*auth\s+required\s+pam_tally2.so\s+.*)(onerr=)[[:alnum:]]*\s*(.*)/\1\2fail \3/" "/etc/pam.d/common-auth"
fi


if ! grep -qP "^\s*auth\s+required\s+pam_tally2.so\s*.*" "/etc/pam.d/common-auth"; then
    # Line matching group + control + module was not found. Check group + module.
    if [ "$(grep -cP '^\s*auth\s+.*\s+pam_tally2.so\s*' "/etc/pam.d/common-auth")" -eq 1 ]; then
        # The control is updated only if one single line matches.
        sed -i -E --follow-symlinks "s/^(\s*auth\s+).*(\bpam_tally2.so.*)/\1required \2/" "/etc/pam.d/common-auth"
    else
        echo "auth    required    pam_tally2.so" >> "/etc/pam.d/common-auth"
    fi
fi
# Check the option
if ! grep -qP "^\s*auth\s+required\s+pam_tally2.so\s*.*\sdeny\b" "/etc/pam.d/common-auth"; then
    sed -i -E --follow-symlinks "/\s*auth\s+required\s+pam_tally2.so.*/ s/$/ deny=${var_password_pam_tally2}/" "/etc/pam.d/common-auth"
else
    sed -i -E --follow-symlinks "s/(\s*auth\s+required\s+pam_tally2.so\s+.*)(deny=)[[:alnum:]]*\s*(.*)/\1\2${var_password_pam_tally2} \3/" "/etc/pam.d/common-auth"
fi


if ! grep -qP "^\s*account\s+required\s+pam_tally2.so\s*.*" "/etc/pam.d/common-account"; then
    # Line matching group + control + module was not found. Check group + module.
    if [ "$(grep -cP '^\s*account\s+.*\s+pam_tally2.so\s*' "/etc/pam.d/common-account")" -eq 1 ]; then
        # The control is updated only if one single line matches.
        sed -i -E --follow-symlinks "s/^(\s*account\s+).*(\bpam_tally2.so.*)/\1required \2/" "/etc/pam.d/common-account"
    else
        echo "account    required    pam_tally2.so" >> "/etc/pam.d/common-account"
    fi
fi
# Check the option
if ! grep -qP "^\s*account\s+required\s+pam_tally2.so\s*.*\s\b" "/etc/pam.d/common-account"; then
    sed -i -E --follow-symlinks "/\s*account\s+required\s+pam_tally2.so.*/ s/$/ /" "/etc/pam.d/common-account"
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
  - PCI-DSS-Req-8.1.6
  - PCI-DSSv4-8.3
  - PCI-DSSv4-8.3.4
  - accounts_passwords_pam_tally2
  - configure_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
- name: XCCDF Value var_password_pam_tally2 # promote to variable
  set_fact:
    var_password_pam_tally2: !!str 5
  tags:
    - always

- name: Set Deny For Failed Password Attempts - Define a fact for control already
    filtered in case filters are used
  ansible.builtin.set_fact:
    pam_module_control: required
  when: '"libpam-runtime" in ansible_facts.packages'
  tags:
  - PCI-DSS-Req-8.1.6
  - PCI-DSSv4-8.3
  - PCI-DSSv4-8.3.4
  - accounts_passwords_pam_tally2
  - configure_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Set Deny For Failed Password Attempts - Check if expected PAM module line
    is present in /etc/pam.d/common-auth
  ansible.builtin.lineinfile:
    path: /etc/pam.d/common-auth
    regexp: ^\s*auth\s+{{ pam_module_control | regex_escape() }}\s+pam_tally2.so\s*.*
    state: absent
  check_mode: true
  changed_when: false
  register: result_pam_line_present
  when: '"libpam-runtime" in ansible_facts.packages'
  tags:
  - PCI-DSS-Req-8.1.6
  - PCI-DSSv4-8.3
  - PCI-DSSv4-8.3.4
  - accounts_passwords_pam_tally2
  - configure_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Set Deny For Failed Password Attempts - Include or update the PAM module line
    in /etc/pam.d/common-auth
  block:

  - name: Set Deny For Failed Password Attempts - Check if required PAM module line
      is present in /etc/pam.d/common-auth with different control
    ansible.builtin.lineinfile:
      path: /etc/pam.d/common-auth
      regexp: ^\s*auth\s+.*\s+pam_tally2.so\s*
      state: absent
    check_mode: true
    changed_when: false
    register: result_pam_line_other_control_present

  - name: Set Deny For Failed Password Attempts - Ensure the correct control for the
      required PAM module line in /etc/pam.d/common-auth
    ansible.builtin.replace:
      dest: /etc/pam.d/common-auth
      regexp: ^(\s*auth\s+).*(\bpam_tally2.so.*)
      replace: \1{{ pam_module_control }} \2
    register: result_pam_module_edit
    when:
    - result_pam_line_other_control_present.found == 1

  - name: Set Deny For Failed Password Attempts - Ensure the required PAM module line
      is included in /etc/pam.d/common-auth
    ansible.builtin.lineinfile:
      dest: /etc/pam.d/common-auth
      insertafter: (fail)
      line: auth    {{ pam_module_control }}    pam_tally2.so
    register: result_pam_module_add
    when:
    - result_pam_line_other_control_present.found == 0 or result_pam_line_other_control_present.found
      > 1

  - name: Set Deny For Failed Password Attempts - Ensure authselect changes are applied
    ansible.builtin.command:
      cmd: authselect apply-changes -b
    when:
    - result_authselect_present is defined
    - result_authselect_present.stat.exists
    - |-
      (result_pam_module_add is defined and result_pam_module_add.changed)
       or (result_pam_module_edit is defined and result_pam_module_edit.changed)
  when:
  - '"libpam-runtime" in ansible_facts.packages'
  - result_pam_line_present.found is defined
  - result_pam_line_present.found == 0
  tags:
  - PCI-DSS-Req-8.1.6
  - PCI-DSSv4-8.3
  - PCI-DSSv4-8.3.4
  - accounts_passwords_pam_tally2
  - configure_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Set Deny For Failed Password Attempts - Define a fact for control already
    filtered in case filters are used
  ansible.builtin.set_fact:
    pam_module_control: required
  when: '"libpam-runtime" in ansible_facts.packages'
  tags:
  - PCI-DSS-Req-8.1.6
  - PCI-DSSv4-8.3
  - PCI-DSSv4-8.3.4
  - accounts_passwords_pam_tally2
  - configure_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Set Deny For Failed Password Attempts - Check if the required PAM module option
    is present in /etc/pam.d/common-auth
  ansible.builtin.lineinfile:
    path: /etc/pam.d/common-auth
    regexp: ^\s*auth\s+{{ pam_module_control | regex_escape() }}\s+pam_tally2.so\s*.*\sonerr\b
    state: absent
  check_mode: true
  changed_when: false
  register: result_pam_module_accounts_passwords_pam_tally2_option_present
  when: '"libpam-runtime" in ansible_facts.packages'
  tags:
  - PCI-DSS-Req-8.1.6
  - PCI-DSSv4-8.3
  - PCI-DSSv4-8.3.4
  - accounts_passwords_pam_tally2
  - configure_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Set Deny For Failed Password Attempts - Ensure the "onerr" PAM option for
    "pam_tally2.so" is included in /etc/pam.d/common-auth
  ansible.builtin.lineinfile:
    path: /etc/pam.d/common-auth
    backrefs: true
    regexp: ^(\s*auth\s+{{ pam_module_control | regex_escape() }}\s+pam_tally2.so.*)
    line: \1 onerr=fail
    state: present
  register: result_pam_accounts_passwords_pam_tally2_add
  when:
  - '"libpam-runtime" in ansible_facts.packages'
  - result_pam_module_accounts_passwords_pam_tally2_option_present.found == 0
  tags:
  - PCI-DSS-Req-8.1.6
  - PCI-DSSv4-8.3
  - PCI-DSSv4-8.3.4
  - accounts_passwords_pam_tally2
  - configure_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Set Deny For Failed Password Attempts - Ensure the required value for "onerr"
    PAM option from "pam_tally2.so" in /etc/pam.d/common-auth
  ansible.builtin.lineinfile:
    path: /etc/pam.d/common-auth
    backrefs: true
    regexp: ^(\s*auth\s+{{ pam_module_control | regex_escape() }}\s+pam_tally2.so\s+.*)(onerr)=[0-9a-zA-Z]*\s*(.*)
    line: \1\2=fail \3
  register: result_pam_accounts_passwords_pam_tally2_edit
  when:
  - '"libpam-runtime" in ansible_facts.packages'
  - result_pam_module_accounts_passwords_pam_tally2_option_present.found > 0
  tags:
  - PCI-DSS-Req-8.1.6
  - PCI-DSSv4-8.3
  - PCI-DSSv4-8.3.4
  - accounts_passwords_pam_tally2
  - configure_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Set Deny For Failed Password Attempts - Define a fact for control already
    filtered in case filters are used
  ansible.builtin.set_fact:
    pam_module_control: required
  when: '"libpam-runtime" in ansible_facts.packages'
  tags:
  - PCI-DSS-Req-8.1.6
  - PCI-DSSv4-8.3
  - PCI-DSSv4-8.3.4
  - accounts_passwords_pam_tally2
  - configure_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Set Deny For Failed Password Attempts - Check if expected PAM module line
    is present in /etc/pam.d/common-auth
  ansible.builtin.lineinfile:
    path: /etc/pam.d/common-auth
    regexp: ^\s*auth\s+{{ pam_module_control | regex_escape() }}\s+pam_tally2.so\s*.*
    state: absent
  check_mode: true
  changed_when: false
  register: result_pam_line_present
  when: '"libpam-runtime" in ansible_facts.packages'
  tags:
  - PCI-DSS-Req-8.1.6
  - PCI-DSSv4-8.3
  - PCI-DSSv4-8.3.4
  - accounts_passwords_pam_tally2
  - configure_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Set Deny For Failed Password Attempts - Include or update the PAM module line
    in /etc/pam.d/common-auth
  block:

  - name: Set Deny For Failed Password Attempts - Check if required PAM module line
      is present in /etc/pam.d/common-auth with different control
    ansible.builtin.lineinfile:
      path: /etc/pam.d/common-auth
      regexp: ^\s*auth\s+.*\s+pam_tally2.so\s*
      state: absent
    check_mode: true
    changed_when: false
    register: result_pam_line_other_control_present

  - name: Set Deny For Failed Password Attempts - Ensure the correct control for the
      required PAM module line in /etc/pam.d/common-auth
    ansible.builtin.replace:
      dest: /etc/pam.d/common-auth
      regexp: ^(\s*auth\s+).*(\bpam_tally2.so.*)
      replace: \1{{ pam_module_control }} \2
    register: result_pam_module_edit
    when:
    - result_pam_line_other_control_present.found == 1

  - name: Set Deny For Failed Password Attempts - Ensure the required PAM module line
      is included in /etc/pam.d/common-auth
    ansible.builtin.lineinfile:
      dest: /etc/pam.d/common-auth
      line: auth    {{ pam_module_control }}    pam_tally2.so
    register: result_pam_module_add
    when:
    - result_pam_line_other_control_present.found == 0 or result_pam_line_other_control_present.found
      > 1

  - name: Set Deny For Failed Password Attempts - Ensure authselect changes are applied
    ansible.builtin.command:
      cmd: authselect apply-changes -b
    when:
    - result_authselect_present is defined
    - result_authselect_present.stat.exists
    - |-
      (result_pam_module_add is defined and result_pam_module_add.changed)
       or (result_pam_module_edit is defined and result_pam_module_edit.changed)
  when:
  - '"libpam-runtime" in ansible_facts.packages'
  - result_pam_line_present.found is defined
  - result_pam_line_present.found == 0
  tags:
  - PCI-DSS-Req-8.1.6
  - PCI-DSSv4-8.3
  - PCI-DSSv4-8.3.4
  - accounts_passwords_pam_tally2
  - configure_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Set Deny For Failed Password Attempts - Define a fact for control already
    filtered in case filters are used
  ansible.builtin.set_fact:
    pam_module_control: required
  when: '"libpam-runtime" in ansible_facts.packages'
  tags:
  - PCI-DSS-Req-8.1.6
  - PCI-DSSv4-8.3
  - PCI-DSSv4-8.3.4
  - accounts_passwords_pam_tally2
  - configure_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Set Deny For Failed Password Attempts - Check if the required PAM module option
    is present in /etc/pam.d/common-auth
  ansible.builtin.lineinfile:
    path: /etc/pam.d/common-auth
    regexp: ^\s*auth\s+{{ pam_module_control | regex_escape() }}\s+pam_tally2.so\s*.*\sdeny\b
    state: absent
  check_mode: true
  changed_when: false
  register: result_pam_module_accounts_passwords_pam_tally2_option_present
  when: '"libpam-runtime" in ansible_facts.packages'
  tags:
  - PCI-DSS-Req-8.1.6
  - PCI-DSSv4-8.3
  - PCI-DSSv4-8.3.4
  - accounts_passwords_pam_tally2
  - configure_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Set Deny For Failed Password Attempts - Ensure the "deny" PAM option for "pam_tally2.so"
    is included in /etc/pam.d/common-auth
  ansible.builtin.lineinfile:
    path: /etc/pam.d/common-auth
    backrefs: true
    regexp: ^(\s*auth\s+{{ pam_module_control | regex_escape() }}\s+pam_tally2.so.*)
    line: \1 deny={{ var_password_pam_tally2 }}
    state: present
  register: result_pam_accounts_passwords_pam_tally2_add
  when:
  - '"libpam-runtime" in ansible_facts.packages'
  - result_pam_module_accounts_passwords_pam_tally2_option_present.found == 0
  tags:
  - PCI-DSS-Req-8.1.6
  - PCI-DSSv4-8.3
  - PCI-DSSv4-8.3.4
  - accounts_passwords_pam_tally2
  - configure_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Set Deny For Failed Password Attempts - Ensure the required value for "deny"
    PAM option from "pam_tally2.so" in /etc/pam.d/common-auth
  ansible.builtin.lineinfile:
    path: /etc/pam.d/common-auth
    backrefs: true
    regexp: ^(\s*auth\s+{{ pam_module_control | regex_escape() }}\s+pam_tally2.so\s+.*)(deny)=[0-9a-zA-Z]*\s*(.*)
    line: \1\2={{ var_password_pam_tally2 }} \3
  register: result_pam_accounts_passwords_pam_tally2_edit
  when:
  - '"libpam-runtime" in ansible_facts.packages'
  - result_pam_module_accounts_passwords_pam_tally2_option_present.found > 0
  tags:
  - PCI-DSS-Req-8.1.6
  - PCI-DSSv4-8.3
  - PCI-DSSv4-8.3.4
  - accounts_passwords_pam_tally2
  - configure_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Set Deny For Failed Password Attempts - Define a fact for control already
    filtered in case filters are used
  ansible.builtin.set_fact:
    pam_module_control: required
  when: '"libpam-runtime" in ansible_facts.packages'
  tags:
  - PCI-DSS-Req-8.1.6
  - PCI-DSSv4-8.3
  - PCI-DSSv4-8.3.4
  - accounts_passwords_pam_tally2
  - configure_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Set Deny For Failed Password Attempts - Check if expected PAM module line
    is present in /etc/pam.d/common-account
  ansible.builtin.lineinfile:
    path: /etc/pam.d/common-account
    regexp: ^\s*account\s+{{ pam_module_control | regex_escape() }}\s+pam_tally2.so\s*.*
    state: absent
  check_mode: true
  changed_when: false
  register: result_pam_line_present
  when: '"libpam-runtime" in ansible_facts.packages'
  tags:
  - PCI-DSS-Req-8.1.6
  - PCI-DSSv4-8.3
  - PCI-DSSv4-8.3.4
  - accounts_passwords_pam_tally2
  - configure_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Set Deny For Failed Password Attempts - Include or update the PAM module line
    in /etc/pam.d/common-account
  block:

  - name: Set Deny For Failed Password Attempts - Check if required PAM module line
      is present in /etc/pam.d/common-account with different control
    ansible.builtin.lineinfile:
      path: /etc/pam.d/common-account
      regexp: ^\s*account\s+.*\s+pam_tally2.so\s*
      state: absent
    check_mode: true
    changed_when: false
    register: result_pam_line_other_control_present

  - name: Set Deny For Failed Password Attempts - Ensure the correct control for the
      required PAM module line in /etc/pam.d/common-account
    ansible.builtin.replace:
      dest: /etc/pam.d/common-account
      regexp: ^(\s*account\s+).*(\bpam_tally2.so.*)
      replace: \1{{ pam_module_control }} \2
    register: result_pam_module_edit
    when:
    - result_pam_line_other_control_present.found == 1

  - name: Set Deny For Failed Password Attempts - Ensure the required PAM module line
      is included in /etc/pam.d/common-account
    ansible.builtin.lineinfile:
      dest: /etc/pam.d/common-account
      line: account    {{ pam_module_control }}    pam_tally2.so
    register: result_pam_module_add
    when:
    - result_pam_line_other_control_present.found == 0 or result_pam_line_other_control_present.found
      > 1

  - name: Set Deny For Failed Password Attempts - Ensure authselect changes are applied
    ansible.builtin.command:
      cmd: authselect apply-changes -b
    when:
    - result_authselect_present is defined
    - result_authselect_present.stat.exists
    - |-
      (result_pam_module_add is defined and result_pam_module_add.changed)
       or (result_pam_module_edit is defined and result_pam_module_edit.changed)
  when:
  - '"libpam-runtime" in ansible_facts.packages'
  - result_pam_line_present.found is defined
  - result_pam_line_present.found == 0
  tags:
  - PCI-DSS-Req-8.1.6
  - PCI-DSSv4-8.3
  - PCI-DSSv4-8.3.4
  - accounts_passwords_pam_tally2
  - configure_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Set Deny For Failed Password Attempts - Define a fact for control already
    filtered in case filters are used
  ansible.builtin.set_fact:
    pam_module_control: required
  when: '"libpam-runtime" in ansible_facts.packages'
  tags:
  - PCI-DSS-Req-8.1.6
  - PCI-DSSv4-8.3
  - PCI-DSSv4-8.3.4
  - accounts_passwords_pam_tally2
  - configure_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Set Deny For Failed Password Attempts - Check if the required PAM module option
    is present in /etc/pam.d/common-account
  ansible.builtin.lineinfile:
    path: /etc/pam.d/common-account
    regexp: ^\s*account\s+{{ pam_module_control | regex_escape() }}\s+pam_tally2.so\s*.*\s\b
    state: absent
  check_mode: true
  changed_when: false
  register: result_pam_module_accounts_passwords_pam_tally2_option_present
  when: '"libpam-runtime" in ansible_facts.packages'
  tags:
  - PCI-DSS-Req-8.1.6
  - PCI-DSSv4-8.3
  - PCI-DSSv4-8.3.4
  - accounts_passwords_pam_tally2
  - configure_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Set Deny For Failed Password Attempts - Ensure the "" PAM option for "pam_tally2.so"
    is included in /etc/pam.d/common-account
  ansible.builtin.lineinfile:
    path: /etc/pam.d/common-account
    backrefs: true
    regexp: ^(\s*account\s+{{ pam_module_control | regex_escape() }}\s+pam_tally2.so.*)
    line: \1
    state: present
  register: result_pam_accounts_passwords_pam_tally2_add
  when:
  - '"libpam-runtime" in ansible_facts.packages'
  - result_pam_module_accounts_passwords_pam_tally2_option_present.found == 0
  tags:
  - PCI-DSS-Req-8.1.6
  - PCI-DSSv4-8.3
  - PCI-DSSv4-8.3.4
  - accounts_passwords_pam_tally2
  - configure_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
```
