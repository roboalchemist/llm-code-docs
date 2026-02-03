# Source: https://docs.datadoghq.com/security/default_rules/def-000-vvt.md

---
title: Limit the maximum number of sequential characters in passwords
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Limit the maximum number of sequential
  characters in passwords
---

# Limit the maximum number of sequential characters in passwords
 
## Description{% #description %}

The `pwquality maxsequence` setting defines the maximum allowable length for consecutive character sequences in a new password. Such sequences can be, e.g., 123 or abc. If the value is set to 0, this check will be turned off.

Note: Passwords that consist mainly of such sequences are unlikely to meet the simplicity criteria unless the sequence constitutes only a small portion of the overall password.

## Rationale{% #rationale %}

Use of a strong password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks.

Password complexity is one important factor that determines the duration required to crack it. A more intricate password results in a larger number of potential combinations that must be tested before successfully compromising the password.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'libpwquality1' 2>/dev/null | grep -q '^installed$'; then

var_password_pam_maxsequence='3'







conf_name=cac_pwquality
if [ ! -f /usr/share/pam-configs/"$conf_name" ]; then
    cat << EOF > /usr/share/pam-configs/"$conf_name"
Name: Pwquality password strength checking
Default: yes
Priority: 1025
Conflicts: cracklib, pwquality
Password-Type: Primary
Password:
    requisite                   pam_pwquality.so
EOF
fi

DEBIAN_FRONTEND=noninteractive pam-auth-update


# Strip any search characters in the key arg so that the key can be replaced without
# adding any search characters to the config file.
stripped_key=$(sed 's/[\^=\$,;+]*//g' <<< "^maxsequence")

# shellcheck disable=SC2059
printf -v formatted_output "%s = %s" "$stripped_key" "$var_password_pam_maxsequence"

# If the key exists, change it. Otherwise, add it to the config_file.
# We search for the key string followed by a word boundary (matched by \>),
# so if we search for 'setting', 'setting2' won't match.
if LC_ALL=C grep -q -m 1 -i -e "^maxsequence\\>" "/etc/security/pwquality.conf"; then
    escaped_formatted_output=$(sed -e 's|/|\\/|g' <<< "$formatted_output")
    LC_ALL=C sed -i --follow-symlinks "s/^maxsequence\\>.*/$escaped_formatted_output/gi" "/etc/security/pwquality.conf"
else
    if [[ -s "/etc/security/pwquality.conf" ]] && [[ -n "$(tail -c 1 -- "/etc/security/pwquality.conf" || true)" ]]; then
        LC_ALL=C sed -i --follow-symlinks '$a'\\ "/etc/security/pwquality.conf"
    fi
    printf '%s\n' "$formatted_output" >> "/etc/security/pwquality.conf"
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
  - accounts_password_pam_maxsequence
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
- name: XCCDF Value var_password_pam_maxsequence # promote to variable
  set_fact:
    var_password_pam_maxsequence: !!str 3
  tags:
    - always

- name: Limit the maximum number of sequential characters in passwords - Check if
    system relies on pam-auth-update tool
  ansible.builtin.stat:
    path: /usr/sbin/pam-auth-update
  register: result_pam_auth_update_present
  when: '"libpwquality1" in ansible_facts.packages'
  tags:
  - accounts_password_pam_maxsequence
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy

- name: Limit the maximum number of sequential characters in passwords - Remediation
    where pam-auth-update tool is present
  block:

  - name: Check if /usr/share/pam-configs/cac_pwquality exists
    stat:
      path: /usr/share/pam-configs/cac_pwquality
    register: pwquality_file_stat

  - name: Put the content into /usr/share/pam-configs/cac_pwquality if it does not
      exist
    copy:
      dest: /usr/share/pam-configs/cac_pwquality
      content: |
        Name: Pwquality password strength checking
        Default: yes
        Priority: 1024
        Conflicts: cracklib
        Password-Type: Primary
        Password:
          requisite           pam_pwquality.so retry=3
      force: true
    when: not pwquality_file_stat.stat.exists

  - name: Limit the maximum number of sequential characters in passwords - Ensure
      pam-auth-update profile changes are applied
    ansible.builtin.command:
      cmd: pam-auth-update --enable cac_pwquality
  when:
  - '"libpwquality1" in ansible_facts.packages'
  - result_pam_auth_update_present.stat.exists
  tags:
  - accounts_password_pam_maxsequence
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy

- name: Limit the maximum number of sequential characters in passwords - Ensure PAM
    variable maxsequence is set accordingly
  ansible.builtin.lineinfile:
    create: true
    dest: /etc/security/pwquality.conf
    regexp: ^#?\s*maxsequence
    line: maxsequence = {{ var_password_pam_maxsequence }}
  when: '"libpwquality1" in ansible_facts.packages'
  tags:
  - accounts_password_pam_maxsequence
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
```
