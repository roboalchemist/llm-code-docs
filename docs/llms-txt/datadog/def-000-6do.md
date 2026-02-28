# Source: https://docs.datadoghq.com/security/default_rules/def-000-6do.md

---
title: Prevent Login to Accounts With Empty Password
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Prevent Login to Accounts With Empty
  Password
---

# Prevent Login to Accounts With Empty Password

## Description{% #description %}

If an account is configured for password authentication but does not have an assigned password, it may be possible to log into the account without authentication. Remove any instances of the `nullok` in `/etc/pam.d/common-password` to prevent logins with empty passwords.

## Rationale{% #rationale %}

If an account has an empty password, anyone could log in and run commands with the privileges of that account. Accounts with empty passwords should never be used in operational environments.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'libpam-runtime' 2>/dev/null | grep -q '^installed$'; then

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
config_file="/usr/share/pam-configs/cac_unix"
sed -i -E '/^Password:/,/^[^[:space:]]/ {
    /pam_unix\.so/ {
        s/\s*nullok//g
    }
}' "$config_file"

sed -i -E '/^Password-Initial:/,/^[^[:space:]]/ {
    /pam_unix\.so/ {
        s/\s*nullok//g
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
  - CJIS-5.5.2
  - DISA-STIG-UBTU-20-010463
  - NIST-800-171-3.1.1
  - NIST-800-171-3.1.5
  - NIST-800-53-CM-6(a)
  - NIST-800-53-IA-5(1)(a)
  - NIST-800-53-IA-5(c)
  - PCI-DSS-Req-8.2.3
  - PCI-DSSv4-8.3
  - PCI-DSSv4-8.3.1
  - configure_strategy
  - high_severity
  - low_complexity
  - medium_disruption
  - no_empty_passwords
  - no_reboot_needed

- name: Prevent Login to Accounts With Empty Password - Check if system relies on
    authselect
  ansible.builtin.stat:
    path: /usr/bin/authselect
  register: result_authselect_present
  when: '"libpam-runtime" in ansible_facts.packages'
  tags:
  - CJIS-5.5.2
  - DISA-STIG-UBTU-20-010463
  - NIST-800-171-3.1.1
  - NIST-800-171-3.1.5
  - NIST-800-53-CM-6(a)
  - NIST-800-53-IA-5(1)(a)
  - NIST-800-53-IA-5(c)
  - PCI-DSS-Req-8.2.3
  - PCI-DSSv4-8.3
  - PCI-DSSv4-8.3.1
  - configure_strategy
  - high_severity
  - low_complexity
  - medium_disruption
  - no_empty_passwords
  - no_reboot_needed

- name: Prevent Login to Accounts With Empty Password - Remediate using authselect
  block:

  - name: Prevent Login to Accounts With Empty Password - Check integrity of authselect
      current profile
    ansible.builtin.command:
      cmd: authselect check
    register: result_authselect_check_cmd
    changed_when: false
    failed_when: false

  - name: Prevent Login to Accounts With Empty Password - Informative message based
      on the authselect integrity check result
    ansible.builtin.assert:
      that:
      - result_authselect_check_cmd.rc == 0
      fail_msg:
      - authselect integrity check failed. Remediation aborted!
      - This remediation could not be applied because an authselect profile was not
        selected or the selected profile is not intact.
      - It is not recommended to manually edit the PAM files when authselect tool
        is available.
      - In cases where the default authselect profile does not cover a specific demand,
        a custom authselect profile is recommended.
      success_msg:
      - authselect integrity check passed

  - name: Prevent Login to Accounts With Empty Password - Get authselect current features
    ansible.builtin.shell:
      cmd: authselect current | tail -n+3 | awk '{ print $2 }'
    register: result_authselect_features
    changed_when: false
    when:
    - result_authselect_check_cmd is success

  - name: Prevent Login to Accounts With Empty Password - Ensure "without-nullok"
      feature is enabled using authselect tool
    ansible.builtin.command:
      cmd: authselect enable-feature without-nullok
    register: result_authselect_enable_feature_cmd
    when:
    - result_authselect_check_cmd is success
    - result_authselect_features.stdout is not search("without-nullok")

  - name: Prevent Login to Accounts With Empty Password - Ensure authselect changes
      are applied
    ansible.builtin.command:
      cmd: authselect apply-changes -b
    when:
    - result_authselect_enable_feature_cmd is not skipped
    - result_authselect_enable_feature_cmd is success
  when:
  - '"libpam-runtime" in ansible_facts.packages'
  - result_authselect_present.stat.exists
  tags:
  - CJIS-5.5.2
  - DISA-STIG-UBTU-20-010463
  - NIST-800-171-3.1.1
  - NIST-800-171-3.1.5
  - NIST-800-53-CM-6(a)
  - NIST-800-53-IA-5(1)(a)
  - NIST-800-53-IA-5(c)
  - PCI-DSS-Req-8.2.3
  - PCI-DSSv4-8.3
  - PCI-DSSv4-8.3.1
  - configure_strategy
  - high_severity
  - low_complexity
  - medium_disruption
  - no_empty_passwords
  - no_reboot_needed

- name: Prevent Login to Accounts With Empty Password - Remediate directly editing
    PAM files
  ansible.builtin.replace:
    dest: '{{ item }}'
    regexp: nullok
  loop:
  - /etc/pam.d/common-password
  when:
  - '"libpam-runtime" in ansible_facts.packages'
  - not result_authselect_present.stat.exists
  tags:
  - CJIS-5.5.2
  - DISA-STIG-UBTU-20-010463
  - NIST-800-171-3.1.1
  - NIST-800-171-3.1.5
  - NIST-800-53-CM-6(a)
  - NIST-800-53-IA-5(1)(a)
  - NIST-800-53-IA-5(c)
  - PCI-DSS-Req-8.2.3
  - PCI-DSSv4-8.3
  - PCI-DSSv4-8.3.1
  - configure_strategy
  - high_severity
  - low_complexity
  - medium_disruption
  - no_empty_passwords
  - no_reboot_needed
```

## Warning{% #warning %}

If the system relies on `authselect` tool to manage PAM settings, the remediation will also use `authselect` tool. However, if any manual modification was made in PAM files, the `authselect` integrity check will fail and the remediation will be aborted in order to preserve intentional changes. In this case, an informative message will be shown in the remediation report. Note that this rule is not applicable for systems running within a container. Having user with empty password within a container is not considered a risk, because it should not be possible to directly login into a container anyway.
