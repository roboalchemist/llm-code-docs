# Source: https://docs.datadoghq.com/security/default_rules/def-000-h0j.md

---
title: Ensure rsyslog Default File Permissions Configured
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Ensure rsyslog Default File Permissions
  Configured
---

# Ensure rsyslog Default File Permissions Configured

## Description{% #description %}

rsyslog will create logfiles that do not already exist on the system. This settings controls what permissions will be applied to these newly created files.

## Rationale{% #rationale %}

It is important to ensure that log files have the correct permissions to ensure that sensitive data is archived and protected.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'linux-base' 2>/dev/null | grep -q '^installed$'; then

readarray -t targets < <(grep -H '^\s*$FileCreateMode' /etc/rsyslog.conf /etc/rsyslog.d/*)

# if $FileCreateMode set in multiple places
if [ ${#targets[@]} -gt 1 ]; then
    # delete all and create new entry with expected value
    sed -i '/^\s*$FileCreateMode/d' /etc/rsyslog.conf /etc/rsyslog.d/*
    echo '$FileCreateMode 0640' > /etc/rsyslog.d/99-rsyslog_filecreatemode.conf
# if $FileCreateMode set in only one place
elif [ "${#targets[@]}" -eq 1 ]; then
    filename=$(echo "${targets[0]}" | cut -d':' -f1)
    value=$(echo "${targets[0]}" | cut -d' ' -f2)
    #convert to decimal and bitwise or operation
    result=$((8#$value | 416))
    # if more permissive than expected, then set it to 0640
    if [ $result -ne 416 ]; then
        # if value is wrong remove it
        sed -i '/^\s*$FileCreateMode/d' $filename
        echo '$FileCreateMode 0640' > $filename
    fi
else
    echo '$FileCreateMode 0640' > /etc/rsyslog.d/99-rsyslog_filecreatemode.conf
fi

systemctl restart rsyslog.service

else
    >&2 echo 'Remediation is not applicable, nothing was done'
fi
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```go
- name: Gather the package facts
  package_facts:
    manager: auto
  tags:
  - configure_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - rsyslog_filecreatemode

- name: Ensure rsyslog Default File Permissions Configured - Search for $FileCreateMode
    Parameter in rsyslog Main Config File
  ansible.builtin.find:
    paths: /etc
    pattern: rsyslog.conf
    contains: ^\s*\$FileCreateMode\s*\d+
  register: rsyslog_main_file_with_filecreatemode
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - configure_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - rsyslog_filecreatemode

- name: Ensure rsyslog Default File Permissions Configured - Search for $FileCreateMode
    Parameter in rsyslog Include Files
  ansible.builtin.find:
    paths: /etc/rsyslog.d/
    pattern: '*.conf'
    contains: ^\s*\$FileCreateMode\s*\d+
  register: rsyslog_includes_with_filecreatemode
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - configure_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - rsyslog_filecreatemode

- name: Ensure rsyslog Default File Permissions Configured - Assemble List of rsyslog
    Configuration Files with $FileCreateMode Parameter
  ansible.builtin.set_fact:
    rsyslog_filecreatemode_files: '{{ rsyslog_main_file_with_filecreatemode.files
      | map(attribute=''path'') | list + rsyslog_includes_with_filecreatemode.files
      | map(attribute=''path'') | list }}'
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - configure_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - rsyslog_filecreatemode

- name: Ensure rsyslog Default File Permissions Configured - Remove $FileCreateMode
    Parameter from Multiple Files to Avoid Conflicts
  ansible.builtin.lineinfile:
    path: '{{ item }}'
    regexp: \$FileCreateMode.*
    state: absent
  register: result_rsyslog_filecreatemode_removed
  loop: '{{ rsyslog_filecreatemode_files }}'
  when:
  - '"linux-base" in ansible_facts.packages'
  - rsyslog_filecreatemode_files | length > 1
  tags:
  - configure_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - rsyslog_filecreatemode

- name: Ensure rsyslog Default File Permissions Configured - Add $FileCreateMode Parameter
    and Expected Value
  ansible.builtin.lineinfile:
    path: /etc/rsyslog.d/99-rsyslog_filecreatemode.conf
    line: $FileCreateMode 0640
    mode: 416
    create: true
  when:
  - '"linux-base" in ansible_facts.packages'
  - rsyslog_filecreatemode_files | length == 0 or result_rsyslog_filecreatemode_removed
    is not skipped
  tags:
  - configure_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - rsyslog_filecreatemode

- name: Ensure rsyslog Default File Permissions Configured - Ensure Correct Value
    of Existing $FileCreateMode Parameter
  ansible.builtin.lineinfile:
    path: '{{ item }}'
    regexp: ^\$FileCreateMode
    line: $FileCreateMode 0640
  loop: '{{ rsyslog_filecreatemode_files }}'
  when:
  - '"linux-base" in ansible_facts.packages'
  - rsyslog_filecreatemode_files | length == 1
  tags:
  - configure_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - rsyslog_filecreatemode
```
