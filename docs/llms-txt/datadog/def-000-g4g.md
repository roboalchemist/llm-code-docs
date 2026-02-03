# Source: https://docs.datadoghq.com/security/default_rules/def-000-g4g.md

---
title: Enable authselect
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Enable authselect
---

# Enable authselect
 
## Description{% #description %}

Configure user authentication setup to use the `authselect` tool. If authselect profile is selected, the rule will enable the sssd profile.

## Rationale{% #rationale %}

Authselect is a successor to authconfig. It is a tool to select system authentication and identity sources from a list of supported profiles instead of letting the administrator manually build the PAM stack. That way, it avoids potential breakage of configuration, as it ships several tested profiles that are well tested and supported to solve different use-cases.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

var_authselect_profile='sssd'


authselect current

if test "$?" -ne 0; then
    if { rpm --quiet -q kernel rpm-ostree bootc && ! rpm --quiet -q openshift-kubelet && { [ -f "/run/.containerenv" ] || [ -f "/.containerenv" ]; }; }; then
        authselect select --force "$var_authselect_profile"
    else
        authselect select "$var_authselect_profile"
    fi

    if test "$?" -ne 0; then
        if rpm --quiet --verify pam; then
            authselect select --force "$var_authselect_profile"
        else
	        echo "authselect is not used but files from the 'pam' package have been altered, so the authselect configuration won't be forced." >&2
        fi
    fi
fi
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```gdscript3
- name: XCCDF Value var_authselect_profile # promote to variable
  set_fact:
    var_authselect_profile: !!str sssd
  tags:
    - always

- name: Enable authselect - Check Current authselect Profile
  ansible.builtin.command:
    cmd: authselect current
  register: result_authselect_current
  changed_when: false
  failed_when: false
  tags:
  - CCE-88248-0
  - NIST-800-53-AC-3
  - PCI-DSSv4-8.3
  - PCI-DSSv4-8.3.4
  - configure_strategy
  - enable_authselect
  - low_complexity
  - medium_disruption
  - medium_severity
  - no_reboot_needed

- name: Enable authselect - Try to Select an authselect Profile
  ansible.builtin.command:
    cmd: authselect select "{{ var_authselect_profile }}"
  register: result_authselect_select
  changed_when: result_authselect_select.rc == 0
  failed_when: false
  when: result_authselect_current.rc != 0
  tags:
  - CCE-88248-0
  - NIST-800-53-AC-3
  - PCI-DSSv4-8.3
  - PCI-DSSv4-8.3.4
  - configure_strategy
  - enable_authselect
  - low_complexity
  - medium_disruption
  - medium_severity
  - no_reboot_needed

- name: Enable authselect - Verify If pam Has Been Altered
  ansible.builtin.command:
    cmd: rpm -qV pam
  register: result_altered_authselect
  changed_when: false
  failed_when: false
  when:
  - result_authselect_select is not skipped
  - result_authselect_select.rc != 0
  tags:
  - CCE-88248-0
  - NIST-800-53-AC-3
  - PCI-DSSv4-8.3
  - PCI-DSSv4-8.3.4
  - configure_strategy
  - enable_authselect
  - low_complexity
  - medium_disruption
  - medium_severity
  - no_reboot_needed

- name: Enable authselect - Informative Message Based on authselect Integrity Check
  ansible.builtin.assert:
    that:
    - result_authselect_current.rc == 0 or result_altered_authselect is skipped or
      result_altered_authselect.rc == 0
    fail_msg:
    - authselect is not used but files from the 'pam' package have been altered, so
      the authselect configuration won't be forced.
  tags:
  - CCE-88248-0
  - NIST-800-53-AC-3
  - PCI-DSSv4-8.3
  - PCI-DSSv4-8.3.4
  - configure_strategy
  - enable_authselect
  - low_complexity
  - medium_disruption
  - medium_severity
  - no_reboot_needed

- name: Enable authselect - Force authselect Profile Selection
  ansible.builtin.command:
    cmd: authselect select --force "{{ var_authselect_profile }}"
  when:
  - result_authselect_current.rc != 0
  - result_authselect_select.rc != 0
  - result_altered_authselect.rc == 0
  tags:
  - CCE-88248-0
  - NIST-800-53-AC-3
  - PCI-DSSv4-8.3
  - PCI-DSSv4-8.3.4
  - configure_strategy
  - enable_authselect
  - low_complexity
  - medium_disruption
  - medium_severity
  - no_reboot_needed
```

## Warning{% #warning %}

If the `sudo authselect select` command returns an error informing that the chosen profile cannot be selected, it is probably because PAM files have already been modified by the administrator. If this is the case, in order to not overwrite the desired changes made by the administrator, the current PAM settings should be investigated before forcing the selection of the chosen authselect profile.
