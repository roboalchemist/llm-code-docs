# Source: https://docs.datadoghq.com/security/default_rules/def-000-oqg.md

---
title: Set LogLevel to INFO
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Set LogLevel to INFO
---

# Set LogLevel to INFO

## Description{% #description %}

The INFO parameter specifices that record login and logout activity will be logged.

The default SSH configuration sets the log level to INFO. The appropriate configuration is used if no value is set for `LogLevel`.

To explicitly specify the log level in SSH, add or correct the following line in `/etc/ssh/sshd_config.d/00-complianceascode-hardening.conf`:

```
LogLevel INFO
```

## Rationale{% #rationale %}

SSH provides several logging levels with varying amounts of verbosity. `DEBUG` is specifically not recommended other than strictly for debugging SSH communications since it provides so much data that it is difficult to identify important security information. `INFO` level is the basic level that only records login activity of SSH users. In many situations, such as Incident Response, it is important to determine when a particular user was active on a system. The logout record can eliminate those users who disconnected, which helps narrow the field.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'linux-base' 2>/dev/null | grep -q '^installed$'; then

mkdir -p /etc/ssh/sshd_config.d
touch /etc/ssh/sshd_config.d/01-complianceascode-reinforce-os-defaults.conf
chmod 0600 /etc/ssh/sshd_config.d/01-complianceascode-reinforce-os-defaults.conf

LC_ALL=C sed -i "/^\s*LogLevel\s\+/Id" "/etc/ssh/sshd_config"
LC_ALL=C sed -i "/^\s*LogLevel\s\+/Id" "/etc/ssh/sshd_config.d"/*.conf
if [ -e "/etc/ssh/sshd_config.d/01-complianceascode-reinforce-os-defaults.conf" ] ; then

    LC_ALL=C sed -i "/^\s*LogLevel\s\+/Id" "/etc/ssh/sshd_config.d/01-complianceascode-reinforce-os-defaults.conf"
else
    touch "/etc/ssh/sshd_config.d/01-complianceascode-reinforce-os-defaults.conf"
fi
# make sure file has newline at the end
sed -i -e '$a\' "/etc/ssh/sshd_config.d/01-complianceascode-reinforce-os-defaults.conf"

cp "/etc/ssh/sshd_config.d/01-complianceascode-reinforce-os-defaults.conf" "/etc/ssh/sshd_config.d/01-complianceascode-reinforce-os-defaults.conf.bak"
# Insert at the beginning of the file
printf '%s\n' "LogLevel INFO" > "/etc/ssh/sshd_config.d/01-complianceascode-reinforce-os-defaults.conf"
cat "/etc/ssh/sshd_config.d/01-complianceascode-reinforce-os-defaults.conf.bak" >> "/etc/ssh/sshd_config.d/01-complianceascode-reinforce-os-defaults.conf"
# Clean up after ourselves.
rm "/etc/ssh/sshd_config.d/01-complianceascode-reinforce-os-defaults.conf.bak"

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
  - NIST-800-53-AC-17(a)
  - NIST-800-53-CM-6(a)
  - low_complexity
  - low_disruption
  - low_severity
  - no_reboot_needed
  - restrict_strategy
  - sshd_set_loglevel_info

- name: Set LogLevel to INFO
  block:

  - name: Deduplicate values from /etc/ssh/sshd_config
    lineinfile:
      path: /etc/ssh/sshd_config
      create: false
      regexp: (?i)(?i)^\s*{{ "LogLevel"| regex_escape }}\s+
      state: absent

  - name: Check if /etc/ssh/sshd_config.d exists
    stat:
      path: /etc/ssh/sshd_config.d
    register: _etc_ssh_sshd_config_d_exists

  - name: Check if the parameter LogLevel is present in /etc/ssh/sshd_config.d
    find:
      paths: /etc/ssh/sshd_config.d
      recurse: 'yes'
      follow: 'no'
      contains: (?i)^\s*{{ "LogLevel"| regex_escape }}\s+
    register: _etc_ssh_sshd_config_d_has_parameter
    when: _etc_ssh_sshd_config_d_exists.stat.isdir is defined and _etc_ssh_sshd_config_d_exists.stat.isdir

  - name: Remove parameter from files in /etc/ssh/sshd_config.d
    lineinfile:
      path: '{{ item.path }}'
      create: false
      regexp: (?i)(?i)^\s*{{ "LogLevel"| regex_escape }}\s+
      state: absent
    with_items: '{{ _etc_ssh_sshd_config_d_has_parameter.files }}'
    when: _etc_ssh_sshd_config_d_has_parameter.matched

  - name: Insert correct line to /etc/ssh/sshd_config.d/01-complianceascode-reinforce-os-defaults.conf
    lineinfile:
      path: /etc/ssh/sshd_config.d/01-complianceascode-reinforce-os-defaults.conf
      create: true
      regexp: (?i)(?i)^\s*{{ "LogLevel"| regex_escape }}\s+
      line: LogLevel INFO
      state: present
      insertbefore: BOF
      validate: /usr/sbin/sshd -t -f %s
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - NIST-800-53-AC-17(a)
  - NIST-800-53-CM-6(a)
  - low_complexity
  - low_disruption
  - low_severity
  - no_reboot_needed
  - restrict_strategy
  - sshd_set_loglevel_info

- name: Set LogLevel to INFO - set file mode for /etc/ssh/sshd_config.d/01-complianceascode-reinforce-os-defaults.conf
  ansible.builtin.file:
    path: /etc/ssh/sshd_config.d/01-complianceascode-reinforce-os-defaults.conf
    mode: '0600'
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - NIST-800-53-AC-17(a)
  - NIST-800-53-CM-6(a)
  - low_complexity
  - low_disruption
  - low_severity
  - no_reboot_needed
  - restrict_strategy
  - sshd_set_loglevel_info
```
