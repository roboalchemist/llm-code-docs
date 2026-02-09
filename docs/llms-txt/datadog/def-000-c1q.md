# Source: https://docs.datadoghq.com/security/default_rules/def-000-c1q.md

---
title: Require Re-Authentication When Using the sudo Command
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Require Re-Authentication When Using
  the sudo Command
---

# Require Re-Authentication When Using the sudo Command
 
## Description{% #description %}

The sudo `timestamp_timeout` tag sets the amount of time sudo password prompt waits. The default `timestamp_timeout` value is 5 minutes. The timestamp_timeout should be configured by making sure that the `timestamp_timeout` tag exists in `/etc/sudoers` configuration file or any sudo configuration snippets in `/etc/sudoers.d/`. If the value is set to an integer less than 0, the user's time stamp will not expire and the user will not have to re-authenticate for privileged actions until the user's session is terminated.

## Rationale{% #rationale %}

Without re-authentication, users may access resources or perform tasks for which they do not have authorization.

When operating systems provide the capability to escalate a functional capability, it is critical that the user re-authenticate.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'sudo' 2>/dev/null | grep -q '^installed$'; then

var_sudo_timestamp_timeout='15'


if grep -Px '^[\s]*Defaults.*timestamp_timeout[\s]*=.*' /etc/sudoers.d/*; then
    find /etc/sudoers.d/ -type f -exec sed -Ei "/^[[:blank:]]*Defaults.*timestamp_timeout[[:blank:]]*=.*/d" {} \;
fi

if /usr/sbin/visudo -qcf /etc/sudoers; then
    cp /etc/sudoers /etc/sudoers.bak
    if ! grep -P '^[\s]*Defaults.*timestamp_timeout[\s]*=[\s]*[-]?\w+.*$' /etc/sudoers; then
        # sudoers file doesn't define Option timestamp_timeout
        echo "Defaults timestamp_timeout=${var_sudo_timestamp_timeout}" >> /etc/sudoers
    else
        # sudoers file defines Option timestamp_timeout, remediate wrong values if present
        if grep -qP "^[\s]*Defaults\s.*\btimestamp_timeout[\s]*=[\s]*(?!${var_sudo_timestamp_timeout}\b)[-]?\w+\b.*$" /etc/sudoers; then
            sed -Ei "s/(^[[:blank:]]*Defaults.*timestamp_timeout[[:blank:]]*=)[[:blank:]]*[-]?\w+(.*$)/\1${var_sudo_timestamp_timeout}\2/" /etc/sudoers
        fi
    fi
    
    # Check validity of sudoers and cleanup bak
    if /usr/sbin/visudo -qcf /etc/sudoers; then
        rm -f /etc/sudoers.bak
    else
        echo "Fail to validate remediated /etc/sudoers, reverting to original file."
        mv /etc/sudoers.bak /etc/sudoers
        false
    fi
else
    echo "Skipping remediation, /etc/sudoers failed to validate"
    false
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
  - NIST-800-53-IA-11
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.6
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
  - sudo_require_reauthentication
- name: XCCDF Value var_sudo_timestamp_timeout # promote to variable
  set_fact:
    var_sudo_timestamp_timeout: !!str 15
  tags:
    - always

- name: Require Re-Authentication When Using the sudo Command - Find /etc/sudoers.d/*
    files containing 'Defaults timestamp_timeout'
  ansible.builtin.find:
    path: /etc/sudoers.d
    patterns: '*'
    contains: ^[\s]*Defaults\s.*\btimestamp_timeout[\s]*=.*
  register: sudoers_d_defaults_timestamp_timeout
  when: '"sudo" in ansible_facts.packages'
  tags:
  - NIST-800-53-IA-11
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.6
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
  - sudo_require_reauthentication

- name: Require Re-Authentication When Using the sudo Command - Remove 'Defaults timestamp_timeout'
    from /etc/sudoers.d/* files
  ansible.builtin.lineinfile:
    path: '{{ item.path }}'
    regexp: ^[\s]*Defaults\s.*\btimestamp_timeout[\s]*=.*
    state: absent
  with_items: '{{ sudoers_d_defaults_timestamp_timeout.files }}'
  when: '"sudo" in ansible_facts.packages'
  tags:
  - NIST-800-53-IA-11
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.6
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
  - sudo_require_reauthentication

- name: Require Re-Authentication When Using the sudo Command - Ensure timestamp_timeout
    has the appropriate value in /etc/sudoers
  ansible.builtin.lineinfile:
    path: /etc/sudoers
    regexp: ^[\s]*Defaults\s(.*)\btimestamp_timeout[\s]*=[\s]*[-]?\w+\b(.*)$
    line: Defaults \1timestamp_timeout={{ var_sudo_timestamp_timeout }}\2
    validate: /usr/sbin/visudo -cf %s
    backrefs: true
  register: edit_sudoers_timestamp_timeout_option
  when: '"sudo" in ansible_facts.packages'
  tags:
  - NIST-800-53-IA-11
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.6
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
  - sudo_require_reauthentication

- name: Require Re-Authentication When Using the sudo Command - Enable timestamp_timeout
    option with correct value in /etc/sudoers
  ansible.builtin.lineinfile:
    path: /etc/sudoers
    line: Defaults timestamp_timeout={{ var_sudo_timestamp_timeout }}
    validate: /usr/sbin/visudo -cf %s
  when:
  - '"sudo" in ansible_facts.packages'
  - |
    edit_sudoers_timestamp_timeout_option is defined and not edit_sudoers_timestamp_timeout_option.changed
  tags:
  - NIST-800-53-IA-11
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.6
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
  - sudo_require_reauthentication

- name: Require Re-Authentication When Using the sudo Command - Remove timestamp_timeout
    wrong values in /etc/sudoers
  ansible.builtin.lineinfile:
    path: /etc/sudoers
    regexp: ^[\s]*Defaults\s.*\btimestamp_timeout[\s]*=[\s]*(?!{{ var_sudo_timestamp_timeout
      }}\b)[-]?\w+\b.*$
    state: absent
    validate: /usr/sbin/visudo -cf %s
  when: '"sudo" in ansible_facts.packages'
  tags:
  - NIST-800-53-IA-11
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.6
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
  - sudo_require_reauthentication
```
