# Source: https://docs.datadoghq.com/security/default_rules/def-000-9rw.md

---
title: Limit Password Reuse (STIGs - ubuntu2004)
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Limit Password Reuse (STIGs -
  ubuntu2004)
---

# Limit Password Reuse (STIGs - ubuntu2004)

## Description{% #description %}

Do not allow users to reuse recent passwords. This can be accomplished by using the `remember` option for the `pam_unix` or `pam_pwhistory` PAM modules.

## Rationale{% #rationale %}

Preventing re-use of previous passwords helps ensure that a compromised password is not re-used by a user.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'libpwquality1' 2>/dev/null | grep -q '^installed$'; then

var_password_pam_unix_remember='5'



config_file="/usr/share/pam-configs/cac_unix"



conf_name=cac_unix
conf_path="/usr/share/pam-configs"

if [ ! -f "$conf_path"/"$conf_name" ]; then
    if [ -f "$conf_path"/unix ]; then
        if grep -q "$(md5sum "$conf_path"/unix | cut -d ' ' -f 1)" /var/lib/dpkg/info/libpam-runtime.md5sums;then
            cp "$conf_path"/unix "$conf_path"/"$conf_name"
            sed -i 's/Priority: [0-9]\+/Priority: 257\
Conflicts: unix/' "$conf_path"/"$conf_name"
            DEBIAN_FRONTEND=noninteractive pam-auth-update
        else
            echo "Not applicable - checksum of $conf_path/unix does not match the original." >&2
        fi
    else
        echo "Not applicable - $conf_path/unix does not exist" >&2
    fi
fi
sed -i -E '/^Password:/,/^[^[:space:]]/ {
    /pam_unix\.so/ {
        s/\s*remember=[^[:space:]]*//g
        s/$/ remember='"$var_password_pam_unix_remember"'/g
    }
}' "$config_file"

sed -i -E '/^Password-Initial:/,/^[^[:space:]]/ {
    /pam_unix\.so/ {
        s/\s*remember=[^[:space:]]*//g
        s/$/ remember='"$var_password_pam_unix_remember"'/g
    }
}' "$config_file"

DEBIAN_FRONTEND=noninteractive pam-auth-update

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
  - DISA-STIG-UBTU-20-010070
  - NIST-800-171-3.5.8
  - NIST-800-53-IA-5(1)(e)
  - NIST-800-53-IA-5(f)
  - PCI-DSS-Req-8.2.5
  - PCI-DSSv4-8.3
  - PCI-DSSv4-8.3.7
  - accounts_password_pam_unix_remember
  - configure_strategy
  - low_complexity
  - medium_disruption
  - medium_severity
  - no_reboot_needed
- name: XCCDF Value var_password_pam_unix_remember # promote to variable
  set_fact:
    var_password_pam_unix_remember: !!str 5
  tags:
    - always

- name: Limit Password Reuse - Check if the required PAM module option is present
    in /etc/pam.d/common-password
  ansible.builtin.lineinfile:
    path: /etc/pam.d/common-password
    regexp: ^\s*password\s+\[success=[A-Za-z0-9].*\]\s+pam_unix.so\s*.*\sremember\b
    state: absent
  check_mode: true
  changed_when: false
  register: result_pam_module_remember_option_present
  when: '"libpwquality1" in ansible_facts.packages'
  tags:
  - CJIS-5.6.2.1.1
  - DISA-STIG-UBTU-20-010070
  - NIST-800-171-3.5.8
  - NIST-800-53-IA-5(1)(e)
  - NIST-800-53-IA-5(f)
  - PCI-DSS-Req-8.2.5
  - PCI-DSSv4-8.3
  - PCI-DSSv4-8.3.7
  - accounts_password_pam_unix_remember
  - configure_strategy
  - low_complexity
  - medium_disruption
  - medium_severity
  - no_reboot_needed

- name: Limit Password Reuse - Ensure the "remember" PAM option for "pam_unix.so"
    is included in /etc/pam.d/common-password
  ansible.builtin.lineinfile:
    path: /etc/pam.d/common-password
    backrefs: true
    regexp: ^(\s*password\s+\[success=[A-Za-z0-9].*\]\s+pam_unix.so.*)
    line: \1 remember={{ var_password_pam_unix_remember }}
    state: present
  register: result_pam_remember_add
  when:
  - '"libpwquality1" in ansible_facts.packages'
  - result_pam_module_remember_option_present.found == 0
  tags:
  - CJIS-5.6.2.1.1
  - DISA-STIG-UBTU-20-010070
  - NIST-800-171-3.5.8
  - NIST-800-53-IA-5(1)(e)
  - NIST-800-53-IA-5(f)
  - PCI-DSS-Req-8.2.5
  - PCI-DSSv4-8.3
  - PCI-DSSv4-8.3.7
  - accounts_password_pam_unix_remember
  - configure_strategy
  - low_complexity
  - medium_disruption
  - medium_severity
  - no_reboot_needed

- name: Limit Password Reuse - Ensure the required value for "remember" PAM option
    from "pam_unix.so" in /etc/pam.d/common-password
  ansible.builtin.lineinfile:
    path: /etc/pam.d/common-password
    backrefs: true
    regexp: ^(\s*password\s+\[success=[A-Za-z0-9].*\]\s+pam_unix.so\s+.*)(remember)=[0-9a-zA-Z]+\s*(.*)
    line: \1\2={{ var_password_pam_unix_remember }} \3
  register: result_pam_remember_edit
  when:
  - '"libpwquality1" in ansible_facts.packages'
  - result_pam_module_remember_option_present.found > 0
  tags:
  - CJIS-5.6.2.1.1
  - DISA-STIG-UBTU-20-010070
  - NIST-800-171-3.5.8
  - NIST-800-53-IA-5(1)(e)
  - NIST-800-53-IA-5(f)
  - PCI-DSS-Req-8.2.5
  - PCI-DSSv4-8.3
  - PCI-DSSv4-8.3.7
  - accounts_password_pam_unix_remember
  - configure_strategy
  - low_complexity
  - medium_disruption
  - medium_severity
  - no_reboot_needed
```

## Warning{% #warning %}

If the system relies on `authselect` tool to manage PAM settings, the remediation will also use `authselect` tool. However, if any manual modification was made in PAM files, the `authselect` integrity check will fail and the remediation will be aborted in order to preserve intentional changes. In this case, an informative message will be shown in the remediation report.
