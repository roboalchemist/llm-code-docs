# Source: https://docs.datadoghq.com/security/default_rules/def-000-zqt.md

---
title: Ensure PAM Enforces Password Requirements - Minimum Different Characters
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Ensure PAM Enforces Password
  Requirements - Minimum Different Characters
---

# Ensure PAM Enforces Password Requirements - Minimum Different Characters
 
## Description{% #description %}

The pam_pwquality module's `difok` parameter sets the number of characters in a password that must not be present in and old password during a password change.

Modify the `difok` setting in `/etc/security/pwquality.conf` to equal 8 to require differing characters when changing passwords.

## Rationale{% #rationale %}

Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and bruteâforce attacks.

Password complexity is one factor of several that determines how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised.

Requiring a minimum number of different characters during password changes ensures that newly changed passwords should not resemble previously compromised ones. Note that passwords which are changed on compromised systems will still be compromised, however.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'libpwquality1' 2>/dev/null | grep -q '^installed$'; then

var_password_pam_difok='8'








# Strip any search characters in the key arg so that the key can be replaced without
# adding any search characters to the config file.
stripped_key=$(sed 's/[\^=\$,;+]*//g' <<< "^difok")

# shellcheck disable=SC2059
printf -v formatted_output "%s = %s" "$stripped_key" "$var_password_pam_difok"

# If the key exists, change it. Otherwise, add it to the config_file.
# We search for the key string followed by a word boundary (matched by \>),
# so if we search for 'setting', 'setting2' won't match.
if LC_ALL=C grep -q -m 1 -i -e "^difok\\>" "/etc/security/pwquality.conf"; then
    escaped_formatted_output=$(sed -e 's|/|\\/|g' <<< "$formatted_output")
    LC_ALL=C sed -i --follow-symlinks "s/^difok\\>.*/$escaped_formatted_output/gi" "/etc/security/pwquality.conf"
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
  - CJIS-5.6.2.1.1
  - DISA-STIG-UBTU-20-010053
  - NIST-800-53-CM-6(a)
  - NIST-800-53-IA-5(1)(b)
  - NIST-800-53-IA-5(4)
  - NIST-800-53-IA-5(c)
  - accounts_password_pam_difok
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
- name: XCCDF Value var_password_pam_difok # promote to variable
  set_fact:
    var_password_pam_difok: !!str 8
  tags:
    - always

- name: Ensure PAM Enforces Password Requirements - Minimum Different Characters -
    Check if system relies on pam-auth-update tool
  ansible.builtin.stat:
    path: /usr/sbin/pam-auth-update
  register: result_pam_auth_update_present
  when: '"libpwquality1" in ansible_facts.packages'
  tags:
  - CJIS-5.6.2.1.1
  - DISA-STIG-UBTU-20-010053
  - NIST-800-53-CM-6(a)
  - NIST-800-53-IA-5(1)(b)
  - NIST-800-53-IA-5(4)
  - NIST-800-53-IA-5(c)
  - accounts_password_pam_difok
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy

- name: Ensure PAM Enforces Password Requirements - Minimum Different Characters -
    Remediation where pam-auth-update tool is present
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

  - name: Ensure PAM Enforces Password Requirements - Minimum Different Characters
      - Ensure pam-auth-update profile changes are applied
    ansible.builtin.command:
      cmd: pam-auth-update --enable cac_pwquality
  when:
  - '"libpwquality1" in ansible_facts.packages'
  - result_pam_auth_update_present.stat.exists
  tags:
  - CJIS-5.6.2.1.1
  - DISA-STIG-UBTU-20-010053
  - NIST-800-53-CM-6(a)
  - NIST-800-53-IA-5(1)(b)
  - NIST-800-53-IA-5(4)
  - NIST-800-53-IA-5(c)
  - accounts_password_pam_difok
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy

- name: Ensure PAM Enforces Password Requirements - Minimum Different Characters -
    Ensure PAM variable difok is set accordingly
  ansible.builtin.lineinfile:
    create: true
    dest: /etc/security/pwquality.conf
    regexp: ^#?\s*difok
    line: difok = {{ var_password_pam_difok }}
  when: '"libpwquality1" in ansible_facts.packages'
  tags:
  - CJIS-5.6.2.1.1
  - DISA-STIG-UBTU-20-010053
  - NIST-800-53-CM-6(a)
  - NIST-800-53-IA-5(1)(b)
  - NIST-800-53-IA-5(4)
  - NIST-800-53-IA-5(c)
  - accounts_password_pam_difok
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
```
