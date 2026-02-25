# Source: https://docs.datadoghq.com/security/default_rules/def-000-kc6.md

---
title: >-
  Configure the Use of the pam_faillock.so Module in the
  /etc/pam.d/password-auth File.
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Configure the Use of the
  pam_faillock.so Module in the /etc/pam.d/password-auth File.
---

# Configure the Use of the pam_faillock.so Module in the /etc/pam.d/password-auth File.

## Description{% #description %}

The pam_faillock.so module must be loaded in preauth in /etc/pam.d/password-auth.

## Rationale{% #rationale %}

If the pam_faillock.so module is not loaded the system will not correctly lockout accounts to prevent password guessing attacks.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

if [ -f /usr/bin/authselect ]; then
    if ! authselect check; then
echo "
authselect integrity check failed. Remediation aborted!
This remediation could not be applied because an authselect profile was not selected or the selected profile is not intact.
It is not recommended to manually edit the PAM files when authselect tool is available.
In cases where the default authselect profile does not cover a specific demand, a custom authselect profile is recommended."
exit 1
fi
authselect enable-feature with-faillock

authselect apply-changes -b
else

AUTH_FILES=("/etc/pam.d/system-auth" "/etc/pam.d/password-auth")
for pam_file in "${AUTH_FILES[@]}"
do
    if ! grep -qE '^\s*auth\s+required\s+pam_faillock\.so\s+(preauth silent|authfail).*$' "$pam_file" ; then
        sed -i --follow-symlinks '/^auth.*sufficient.*pam_unix\.so.*/i auth        required      pam_faillock.so preauth silent' "$pam_file"
        sed -i --follow-symlinks '/^auth.*required.*pam_deny\.so.*/i auth        required      pam_faillock.so authfail' "$pam_file"
        sed -i --follow-symlinks '/^account.*required.*pam_unix\.so.*/i account     required      pam_faillock.so' "$pam_file"
    fi
    sed -Ei 's/(auth.*)(\[default=die\])(.*pam_faillock\.so)/\1required     \3/g' "$pam_file"
done

fi
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```gdscript3
- name: Configure the Use of the pam_faillock.so Module in the /etc/pam.d/password-auth
    File. - Check if system relies on authselect tool
  ansible.builtin.stat:
    path: /usr/bin/authselect
  register: result_authselect_present
  tags:
  - CCE-86931-3
  - DISA-STIG-RHEL-08-020026
  - NIST-800-53-AC-7 (a)
  - account_password_pam_faillock_password_auth
  - enable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Configure the Use of the pam_faillock.so Module in the /etc/pam.d/password-auth
    File. - Remediation where authselect tool is present
  block:

  - name: Configure the Use of the pam_faillock.so Module in the /etc/pam.d/password-auth
      File. - Check integrity of authselect current profile
    ansible.builtin.command:
      cmd: authselect check
    register: result_authselect_check_cmd
    changed_when: false
    failed_when: false

  - name: Configure the Use of the pam_faillock.so Module in the /etc/pam.d/password-auth
      File. - Informative message based on the authselect integrity check result
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

  - name: Configure the Use of the pam_faillock.so Module in the /etc/pam.d/password-auth
      File. - Get authselect current features
    ansible.builtin.shell:
      cmd: authselect current | tail -n+3 | awk '{ print $2 }'
    register: result_authselect_features
    changed_when: false
    when:
    - result_authselect_check_cmd is success

  - name: Configure the Use of the pam_faillock.so Module in the /etc/pam.d/password-auth
      File. - Ensure "with-faillock" feature is enabled using authselect tool
    ansible.builtin.command:
      cmd: authselect enable-feature with-faillock
    register: result_authselect_enable_feature_cmd
    when:
    - result_authselect_check_cmd is success
    - result_authselect_features.stdout is not search("with-faillock")

  - name: Configure the Use of the pam_faillock.so Module in the /etc/pam.d/password-auth
      File. - Ensure authselect changes are applied
    ansible.builtin.command:
      cmd: authselect apply-changes -b
    when:
    - result_authselect_enable_feature_cmd is not skipped
    - result_authselect_enable_feature_cmd is success
  when: result_authselect_present.stat.exists
  tags:
  - CCE-86931-3
  - DISA-STIG-RHEL-08-020026
  - NIST-800-53-AC-7 (a)
  - account_password_pam_faillock_password_auth
  - enable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Configure the Use of the pam_faillock.so Module in the /etc/pam.d/password-auth
    File. - Remediation where authselect tool is not present
  block:

  - name: Configure the Use of the pam_faillock.so Module in the /etc/pam.d/password-auth
      File. - Check if pam_faillock.so is already enabled
    ansible.builtin.lineinfile:
      path: /etc/pam.d/system-auth
      regexp: .*auth.*pam_faillock\.so (preauth|authfail)
      state: absent
    check_mode: true
    changed_when: false
    register: result_pam_faillock_is_enabled

  - name: Configure the Use of the pam_faillock.so Module in the /etc/pam.d/password-auth
      File. - Enable pam_faillock.so preauth editing PAM files
    ansible.builtin.lineinfile:
      path: '{{ item }}'
      line: auth        required      pam_faillock.so preauth
      insertbefore: ^auth.*sufficient.*pam_unix\.so.*
      state: present
    loop:
    - /etc/pam.d/system-auth
    - /etc/pam.d/password-auth
    when:
    - result_pam_faillock_is_enabled.found == 0

  - name: Configure the Use of the pam_faillock.so Module in the /etc/pam.d/password-auth
      File. - Enable pam_faillock.so authfail editing PAM files
    ansible.builtin.lineinfile:
      path: '{{ item }}'
      line: auth        required      pam_faillock.so authfail
      insertbefore: ^auth.*required.*pam_deny\.so.*
      state: present
    loop:
    - /etc/pam.d/system-auth
    - /etc/pam.d/password-auth
    when:
    - result_pam_faillock_is_enabled.found == 0

  - name: Configure the Use of the pam_faillock.so Module in the /etc/pam.d/password-auth
      File. - Enable pam_faillock.so account section editing PAM files
    ansible.builtin.lineinfile:
      path: '{{ item }}'
      line: account     required      pam_faillock.so
      insertbefore: ^account.*required.*pam_unix\.so.*
      state: present
    loop:
    - /etc/pam.d/system-auth
    - /etc/pam.d/password-auth
    when:
    - result_pam_faillock_is_enabled.found == 0
  when: not result_authselect_present.stat.exists
  tags:
  - CCE-86931-3
  - DISA-STIG-RHEL-08-020026
  - NIST-800-53-AC-7 (a)
  - account_password_pam_faillock_password_auth
  - enable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
```
