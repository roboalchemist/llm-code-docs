# Source: https://docs.datadoghq.com/security/default_rules/def-000-1wb.md

---
title: Set PAM''s Password Hashing Algorithm
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Set PAM''s Password Hashing Algorithm
---

# Set PAM''s Password Hashing Algorithm

## Description{% #description %}

The PAM system service can be configured to only store encrypted representations of passwords. In "/etc/pam.d/common-password", the `password` section of the file controls which PAM modules to execute during a password change. Set the `pam_unix.so` module in the `password` section to include the option `sha512` and no other hashing algorithms as shown below:

```
password    [success=1 default=ignore]   pam_unix.so sha512
          other arguments...

```

This will help ensure that new passwords for local users will be stored using the sha512 algorithm.

## Rationale{% #rationale %}

Passwords need to be protected at all times, and encryption is the standard method for protecting passwords. If passwords are not encrypted, they can be plainly read (i.e., clear text) and easily compromised. Passwords that are encrypted with a weak algorithm are no more protected than if they are kept in plain text.

This setting ensures user and group account administration utilities are configured to store only encrypted representations of passwords. Additionally, the `crypt_style` configuration option in `/etc/libuser.conf` ensures the use of a strong hashing algorithm that makes password cracking attacks more difficult.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'libpam-runtime' 2>/dev/null | grep -q '^installed$'; then

var_password_hashing_algorithm_pam='sha512'


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
PAM_FILE_PATH=/usr/share/pam-configs/cac_unix

# Ensure all the hashing algorithm option is removed.
declare -a HASHING_ALGORITHMS_OPTIONS=("sha512" "yescrypt" "gost_yescrypt" "blowfish" "sha256" "md5" "bigcrypt")

for hash_option in "${HASHING_ALGORITHMS_OPTIONS[@]}"; do
  sed -i -E '/^Password:/,/^[^[:space:]]/ {
    /pam_unix\.so/ {
      s/\s*\b'"$hash_option"'\b//g
    }
    }' "$PAM_FILE_PATH"
    sed -i -E '/^Password-Initial:/,/^[^[:space:]]/ {
    /pam_unix\.so/ {
      s/\s*\b'"$hash_option"'\b//g
    }
    }' "$PAM_FILE_PATH"
    DEBIAN_FRONTEND=noninteractive pam-auth-update
done

if ! grep -qzP "Password:\s*\n\s+.*\s+pam_unix.so\s+.*\b$var_password_hashing_algorithm_pam\b" "$PAM_FILE_PATH"; then
  sed -i -E '/^Password:/,/^[^[:space:]]/ {
    /pam_unix\.so/ {
        s/$/ '"$var_password_hashing_algorithm_pam"'/g
    }
}' "$PAM_FILE_PATH"
fi

if ! grep -qzP "Password-Initial:\s*\n\s+.*\s+pam_unix.so\s+.*\b$var_password_hashing_algorithm_pam\b" "$PAM_FILE_PATH"; then
  sed -i -E '/^Password-Initial:/,/^[^[:space:]]/ {
    /pam_unix\.so/ {
        s/$/ '"$var_password_hashing_algorithm_pam"'/g
    }
}' "$PAM_FILE_PATH"
fi

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
  - CJIS-5.6.2.2
  - DISA-STIG-UBTU-22-611055
  - NIST-800-171-3.13.11
  - NIST-800-53-CM-6(a)
  - NIST-800-53-IA-5(1)(c)
  - NIST-800-53-IA-5(c)
  - PCI-DSS-Req-8.2.1
  - PCI-DSSv4-8.3
  - PCI-DSSv4-8.3.2
  - configure_strategy
  - low_complexity
  - medium_disruption
  - medium_severity
  - no_reboot_needed
  - set_password_hashing_algorithm_systemauth
- name: XCCDF Value var_password_hashing_algorithm_pam # promote to variable
  set_fact:
    var_password_hashing_algorithm_pam: !!str sha512
  tags:
    - always

- name: Set PAM's Password Hashing Algorithm - Check if /etc/pam.d/system-auth file
    is present
  ansible.builtin.stat:
    path: /etc/pam.d/system-auth
  register: result_pam_file_present
  when: '"libpam-runtime" in ansible_facts.packages'
  tags:
  - CJIS-5.6.2.2
  - DISA-STIG-UBTU-22-611055
  - NIST-800-171-3.13.11
  - NIST-800-53-CM-6(a)
  - NIST-800-53-IA-5(1)(c)
  - NIST-800-53-IA-5(c)
  - PCI-DSS-Req-8.2.1
  - PCI-DSSv4-8.3
  - PCI-DSSv4-8.3.2
  - configure_strategy
  - low_complexity
  - medium_disruption
  - medium_severity
  - no_reboot_needed
  - set_password_hashing_algorithm_systemauth

- name: Set PAM's Password Hashing Algorithm - Check the proper remediation for the
    system
  block:

  - name: Set PAM's Password Hashing Algorithm - Define the PAM file to be edited
      as a local fact
    ansible.builtin.set_fact:
      pam_file_path: /etc/pam.d/system-auth

  - name: Set PAM's Password Hashing Algorithm - Check if system relies on authselect
      tool
    ansible.builtin.stat:
      path: /usr/bin/authselect
    register: result_authselect_present

  - name: Set PAM's Password Hashing Algorithm - Ensure authselect custom profile
      is used if authselect is present
    block:

    - name: Set PAM's Password Hashing Algorithm - Check integrity of authselect current
        profile
      ansible.builtin.command:
        cmd: authselect check
      register: result_authselect_check_cmd
      changed_when: false
      failed_when: false

    - name: Set PAM's Password Hashing Algorithm - Informative message based on the
        authselect integrity check result
      ansible.builtin.assert:
        that:
        - result_authselect_check_cmd.rc == 0
        fail_msg:
        - authselect integrity check failed. Remediation aborted!
        - This remediation could not be applied because an authselect profile was
          not selected or the selected profile is not intact.
        - It is not recommended to manually edit the PAM files when authselect tool
          is available.
        - In cases where the default authselect profile does not cover a specific
          demand, a custom authselect profile is recommended.
        success_msg:
        - authselect integrity check passed

    - name: Set PAM's Password Hashing Algorithm - Get authselect current profile
      ansible.builtin.shell:
        cmd: authselect current -r | awk '{ print $1 }'
      register: result_authselect_profile
      changed_when: false
      when:
      - result_authselect_check_cmd is success

    - name: Set PAM's Password Hashing Algorithm - Define the current authselect profile
        as a local fact
      ansible.builtin.set_fact:
        authselect_current_profile: '{{ result_authselect_profile.stdout }}'
        authselect_custom_profile: '{{ result_authselect_profile.stdout }}'
      when:
      - result_authselect_profile is not skipped
      - result_authselect_profile.stdout is match("custom/")

    - name: Set PAM's Password Hashing Algorithm - Define the new authselect custom
        profile as a local fact
      ansible.builtin.set_fact:
        authselect_current_profile: '{{ result_authselect_profile.stdout }}'
        authselect_custom_profile: custom/hardening
      when:
      - result_authselect_profile is not skipped
      - result_authselect_profile.stdout is not match("custom/")

    - name: Set PAM's Password Hashing Algorithm - Get authselect current features
        to also enable them in the custom profile
      ansible.builtin.shell:
        cmd: authselect current | tail -n+3 | awk '{ print $2 }'
      register: result_authselect_features
      changed_when: false
      when:
      - result_authselect_profile is not skipped
      - authselect_current_profile is not match("custom/")

    - name: Set PAM's Password Hashing Algorithm - Check if any custom profile with
        the same name was already created
      ansible.builtin.stat:
        path: /etc/authselect/{{ authselect_custom_profile }}
      register: result_authselect_custom_profile_present
      changed_when: false
      when:
      - authselect_current_profile is not match("custom/")

    - name: Set PAM's Password Hashing Algorithm - Create an authselect custom profile
        based on the current profile
      ansible.builtin.command:
        cmd: authselect create-profile hardening -b {{ authselect_current_profile
          }}
      when:
      - result_authselect_check_cmd is success
      - authselect_current_profile is not match("^(custom/|local)")
      - not result_authselect_custom_profile_present.stat.exists

    - name: Set PAM's Password Hashing Algorithm - Create an authselect custom profile
        based on sssd profile
      ansible.builtin.command:
        cmd: authselect create-profile hardening -b sssd
      when:
      - result_authselect_check_cmd is success
      - authselect_current_profile is match("local")
      - not result_authselect_custom_profile_present.stat.exists

    - name: Set PAM's Password Hashing Algorithm - Ensure authselect changes are applied
      ansible.builtin.command:
        cmd: authselect apply-changes -b --backup=before-hardening-custom-profile
      when:
      - result_authselect_check_cmd is success
      - result_authselect_profile is not skipped
      - authselect_current_profile is not match("custom/")
      - authselect_custom_profile is not match(authselect_current_profile)

    - name: Set PAM's Password Hashing Algorithm - Ensure the authselect custom profile
        is selected
      ansible.builtin.command:
        cmd: authselect select {{ authselect_custom_profile }}
      register: result_pam_authselect_select_profile
      when:
      - result_authselect_check_cmd is success
      - result_authselect_profile is not skipped
      - authselect_current_profile is not match("custom/")
      - authselect_custom_profile is not match(authselect_current_profile)

    - name: Set PAM's Password Hashing Algorithm - Restore the authselect features
        in the custom profile
      ansible.builtin.command:
        cmd: authselect enable-feature {{ item }}
      loop: '{{ result_authselect_features.stdout_lines }}'
      register: result_pam_authselect_restore_features
      when:
      - result_authselect_profile is not skipped
      - result_authselect_features is not skipped
      - result_pam_authselect_select_profile is not skipped

    - name: Set PAM's Password Hashing Algorithm - Ensure authselect changes are applied
      ansible.builtin.command:
        cmd: authselect apply-changes -b --backup=after-hardening-custom-profile
      when:
      - result_authselect_check_cmd is success
      - result_authselect_profile is not skipped
      - result_pam_authselect_restore_features is not skipped

    - name: Set PAM's Password Hashing Algorithm - Change the PAM file to be edited
        according to the custom authselect profile
      ansible.builtin.set_fact:
        pam_file_path: /etc/authselect/{{ authselect_custom_profile }}/{{ pam_file_path
          | basename }}
    when:
    - result_authselect_present.stat.exists

  - name: Set PAM's Password Hashing Algorithm - Define a fact for control already
      filtered in case filters are used
    ansible.builtin.set_fact:
      pam_module_control: sufficient

  - name: Set PAM's Password Hashing Algorithm - Check if expected PAM module line
      is present in {{ pam_file_path }}
    ansible.builtin.lineinfile:
      path: '{{ pam_file_path }}'
      regexp: ^\s*password\s+{{ pam_module_control | regex_escape() }}\s+pam_unix.so\s*.*
      state: absent
    check_mode: true
    changed_when: false
    register: result_pam_line_present

  - name: Set PAM's Password Hashing Algorithm - Include or update the PAM module
      line in {{ pam_file_path }}
    block:

    - name: Set PAM's Password Hashing Algorithm - Check if required PAM module line
        is present in {{ pam_file_path }} with different control
      ansible.builtin.lineinfile:
        path: '{{ pam_file_path }}'
        regexp: ^\s*password\s+.*\s+pam_unix.so\s*
        state: absent
      check_mode: true
      changed_when: false
      register: result_pam_line_other_control_present

    - name: Set PAM's Password Hashing Algorithm - Ensure the correct control for
        the required PAM module line in {{ pam_file_path }}
      ansible.builtin.replace:
        dest: '{{ pam_file_path }}'
        regexp: ^(\s*password\s+).*(\bpam_unix.so.*)
        replace: \1{{ pam_module_control }} \2
      register: result_pam_module_edit
      when:
      - result_pam_line_other_control_present.found == 1

    - name: Set PAM's Password Hashing Algorithm - Ensure the required PAM module
        line is included in {{ pam_file_path }}
      ansible.builtin.lineinfile:
        dest: '{{ pam_file_path }}'
        line: password    {{ pam_module_control }}    pam_unix.so
      register: result_pam_module_add
      when:
      - result_pam_line_other_control_present.found == 0 or result_pam_line_other_control_present.found
        > 1

    - name: Set PAM's Password Hashing Algorithm - Ensure authselect changes are applied
      ansible.builtin.command:
        cmd: authselect apply-changes -b
      when:
      - result_authselect_present is defined
      - result_authselect_present.stat.exists
      - |-
        (result_pam_module_add is defined and result_pam_module_add.changed)
         or (result_pam_module_edit is defined and result_pam_module_edit.changed)
    when:
    - result_pam_line_present.found is defined
    - result_pam_line_present.found == 0

  - name: Set PAM's Password Hashing Algorithm - Define a fact for control already
      filtered in case filters are used
    ansible.builtin.set_fact:
      pam_module_control: sufficient

  - name: Set PAM's Password Hashing Algorithm - Check if the required PAM module
      option is present in {{ pam_file_path }}
    ansible.builtin.lineinfile:
      path: '{{ pam_file_path }}'
      regexp: ^\s*password\s+{{ pam_module_control | regex_escape() }}\s+pam_unix.so\s*.*\s{{
        var_password_hashing_algorithm_pam }}\b
      state: absent
    check_mode: true
    changed_when: false
    register: result_pam_module_set_password_hashing_algorithm_systemauth_option_present

  - name: Set PAM's Password Hashing Algorithm - Ensure the "{{ var_password_hashing_algorithm_pam
      }}" PAM option for "pam_unix.so" is included in {{ pam_file_path }}
    ansible.builtin.lineinfile:
      path: '{{ pam_file_path }}'
      backrefs: true
      regexp: ^(\s*password\s+{{ pam_module_control | regex_escape() }}\s+pam_unix.so.*)
      line: \1 {{ var_password_hashing_algorithm_pam }}
      state: present
    register: result_pam_set_password_hashing_algorithm_systemauth_add
    when:
    - result_pam_module_set_password_hashing_algorithm_systemauth_option_present.found
      == 0

  - name: Set PAM's Password Hashing Algorithm - Ensure authselect changes are applied
    ansible.builtin.command:
      cmd: authselect apply-changes -b
    when:
    - result_authselect_present.stat.exists
    - |-
      (result_pam_set_password_hashing_algorithm_systemauth_add is defined and result_pam_set_password_hashing_algorithm_systemauth_add.changed)
       or (result_pam_set_password_hashing_algorithm_systemauth_edit is defined and result_pam_set_password_hashing_algorithm_systemauth_edit.changed)
  when:
  - '"libpam-runtime" in ansible_facts.packages'
  - result_pam_file_present.stat.exists
  tags:
  - CJIS-5.6.2.2
  - DISA-STIG-UBTU-22-611055
  - NIST-800-171-3.13.11
  - NIST-800-53-CM-6(a)
  - NIST-800-53-IA-5(1)(c)
  - NIST-800-53-IA-5(c)
  - PCI-DSS-Req-8.2.1
  - PCI-DSSv4-8.3
  - PCI-DSSv4-8.3.2
  - configure_strategy
  - low_complexity
  - medium_disruption
  - medium_severity
  - no_reboot_needed
  - set_password_hashing_algorithm_systemauth

- name: Set PAM's Password Hashing Algorithm - Check if /etc/pam.d/system-auth File
    is Present
  ansible.builtin.stat:
    path: /etc/pam.d/system-auth
  register: result_pam_file_present
  when: '"libpam-runtime" in ansible_facts.packages'
  tags:
  - CJIS-5.6.2.2
  - DISA-STIG-UBTU-22-611055
  - NIST-800-171-3.13.11
  - NIST-800-53-CM-6(a)
  - NIST-800-53-IA-5(1)(c)
  - NIST-800-53-IA-5(c)
  - PCI-DSS-Req-8.2.1
  - PCI-DSSv4-8.3
  - PCI-DSSv4-8.3.2
  - configure_strategy
  - low_complexity
  - medium_disruption
  - medium_severity
  - no_reboot_needed
  - set_password_hashing_algorithm_systemauth

- name: Set PAM's Password Hashing Algorithm - Check The Proper Remediation For The
    System
  block:

  - name: Set PAM's Password Hashing Algorithm - Define the PAM file to be edited
      as a local fact
    ansible.builtin.set_fact:
      pam_file_path: /etc/pam.d/system-auth

  - name: Set PAM's Password Hashing Algorithm - Check if system relies on authselect
      tool
    ansible.builtin.stat:
      path: /usr/bin/authselect
    register: result_authselect_present

  - name: Set PAM's Password Hashing Algorithm - Ensure authselect custom profile
      is used if authselect is present
    block:

    - name: Set PAM's Password Hashing Algorithm - Check integrity of authselect current
        profile
      ansible.builtin.command:
        cmd: authselect check
      register: result_authselect_check_cmd
      changed_when: false
      failed_when: false

    - name: Set PAM's Password Hashing Algorithm - Informative message based on the
        authselect integrity check result
      ansible.builtin.assert:
        that:
        - result_authselect_check_cmd.rc == 0
        fail_msg:
        - authselect integrity check failed. Remediation aborted!
        - This remediation could not be applied because an authselect profile was
          not selected or the selected profile is not intact.
        - It is not recommended to manually edit the PAM files when authselect tool
          is available.
        - In cases where the default authselect profile does not cover a specific
          demand, a custom authselect profile is recommended.
        success_msg:
        - authselect integrity check passed

    - name: Set PAM's Password Hashing Algorithm - Get authselect current profile
      ansible.builtin.shell:
        cmd: authselect current -r | awk '{ print $1 }'
      register: result_authselect_profile
      changed_when: false
      when:
      - result_authselect_check_cmd is success

    - name: Set PAM's Password Hashing Algorithm - Define the current authselect profile
        as a local fact
      ansible.builtin.set_fact:
        authselect_current_profile: '{{ result_authselect_profile.stdout }}'
        authselect_custom_profile: '{{ result_authselect_profile.stdout }}'
      when:
      - result_authselect_profile is not skipped
      - result_authselect_profile.stdout is match("custom/")

    - name: Set PAM's Password Hashing Algorithm - Define the new authselect custom
        profile as a local fact
      ansible.builtin.set_fact:
        authselect_current_profile: '{{ result_authselect_profile.stdout }}'
        authselect_custom_profile: custom/hardening
      when:
      - result_authselect_profile is not skipped
      - result_authselect_profile.stdout is not match("custom/")

    - name: Set PAM's Password Hashing Algorithm - Get authselect current features
        to also enable them in the custom profile
      ansible.builtin.shell:
        cmd: authselect current | tail -n+3 | awk '{ print $2 }'
      register: result_authselect_features
      changed_when: false
      when:
      - result_authselect_profile is not skipped
      - authselect_current_profile is not match("custom/")

    - name: Set PAM's Password Hashing Algorithm - Check if any custom profile with
        the same name was already created
      ansible.builtin.stat:
        path: /etc/authselect/{{ authselect_custom_profile }}
      register: result_authselect_custom_profile_present
      changed_when: false
      when:
      - authselect_current_profile is not match("custom/")

    - name: Set PAM's Password Hashing Algorithm - Create an authselect custom profile
        based on the current profile
      ansible.builtin.command:
        cmd: authselect create-profile hardening -b {{ authselect_current_profile
          }}
      when:
      - result_authselect_check_cmd is success
      - authselect_current_profile is not match("^(custom/|local)")
      - not result_authselect_custom_profile_present.stat.exists

    - name: Set PAM's Password Hashing Algorithm - Create an authselect custom profile
        based on sssd profile
      ansible.builtin.command:
        cmd: authselect create-profile hardening -b sssd
      when:
      - result_authselect_check_cmd is success
      - authselect_current_profile is match("local")
      - not result_authselect_custom_profile_present.stat.exists

    - name: Set PAM's Password Hashing Algorithm - Ensure authselect changes are applied
      ansible.builtin.command:
        cmd: authselect apply-changes -b --backup=before-hardening-custom-profile
      when:
      - result_authselect_check_cmd is success
      - result_authselect_profile is not skipped
      - authselect_current_profile is not match("custom/")
      - authselect_custom_profile is not match(authselect_current_profile)

    - name: Set PAM's Password Hashing Algorithm - Ensure the authselect custom profile
        is selected
      ansible.builtin.command:
        cmd: authselect select {{ authselect_custom_profile }}
      register: result_pam_authselect_select_profile
      when:
      - result_authselect_check_cmd is success
      - result_authselect_profile is not skipped
      - authselect_current_profile is not match("custom/")
      - authselect_custom_profile is not match(authselect_current_profile)

    - name: Set PAM's Password Hashing Algorithm - Restore the authselect features
        in the custom profile
      ansible.builtin.command:
        cmd: authselect enable-feature {{ item }}
      loop: '{{ result_authselect_features.stdout_lines }}'
      register: result_pam_authselect_restore_features
      when:
      - result_authselect_profile is not skipped
      - result_authselect_features is not skipped
      - result_pam_authselect_select_profile is not skipped

    - name: Set PAM's Password Hashing Algorithm - Ensure authselect changes are applied
      ansible.builtin.command:
        cmd: authselect apply-changes -b --backup=after-hardening-custom-profile
      when:
      - result_authselect_check_cmd is success
      - result_authselect_profile is not skipped
      - result_pam_authselect_restore_features is not skipped

    - name: Set PAM's Password Hashing Algorithm - Change the PAM file to be edited
        according to the custom authselect profile
      ansible.builtin.set_fact:
        pam_file_path: /etc/authselect/{{ authselect_custom_profile }}/{{ pam_file_path
          | basename }}
    when:
    - result_authselect_present.stat.exists

  - name: Set PAM's Password Hashing Algorithm - Ensure That Only the Correct Hashing
      Algorithm Option For pam_unix.so Is Used in /etc/pam.d/system-auth
    ansible.builtin.replace:
      dest: '{{ pam_file_path }}'
      regexp: (^\s*password.*pam_unix\.so.*)\b{{ item }}\b\s*(.*)
      replace: \1\2
    when: item != var_password_hashing_algorithm_pam
    loop:
    - sha512
    - yescrypt
    - gost_yescrypt
    - blowfish
    - sha256
    - md5
    - bigcrypt
    register: result_pam_hashing_options_removal

  - name: Set PAM's Password Hashing Algorithm - Ensure authselect changes are applied
    ansible.builtin.command:
      cmd: authselect apply-changes -b
    when:
    - result_authselect_present.stat.exists
    - result_pam_hashing_options_removal is changed
  when:
  - '"libpam-runtime" in ansible_facts.packages'
  - result_pam_file_present.stat.exists
  tags:
  - CJIS-5.6.2.2
  - DISA-STIG-UBTU-22-611055
  - NIST-800-171-3.13.11
  - NIST-800-53-CM-6(a)
  - NIST-800-53-IA-5(1)(c)
  - NIST-800-53-IA-5(c)
  - PCI-DSS-Req-8.2.1
  - PCI-DSSv4-8.3
  - PCI-DSSv4-8.3.2
  - configure_strategy
  - low_complexity
  - medium_disruption
  - medium_severity
  - no_reboot_needed
  - set_password_hashing_algorithm_systemauth
```

## Warning{% #warning %}

The hashing algorithms to be used with pam_unix.so are defined with independent module options. There are at least 7 possible algorithms and likely more algorithms will be introduced along the time. Due the the number of options and its possible combinations, the use of multiple hashing algorithm options may bring unexpected behaviors to the system. For this reason the check will pass only when one hashing algorithm option is defined and is aligned to the "var_password_hashing_algorithm_pam" variable. The remediation will ensure the correct option and remove any other extra hashing algorithm option.
