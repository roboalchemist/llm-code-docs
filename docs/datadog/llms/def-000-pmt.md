# Source: https://docs.datadoghq.com/security/default_rules/def-000-pmt.md

---
title: Ensure SSH MaxStartups is configured
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Ensure SSH MaxStartups is configured
---

# Ensure SSH MaxStartups is configured

## Description{% #description %}

The MaxStartups parameter specifies the maximum number of concurrent unauthenticated connections to the SSH daemon. Additional connections will be dropped until authentication succeeds or the LoginGraceTime expires for a connection. To configure MaxStartups, you should add or edit the following line in the `/etc/ssh/sshd_config` file:

```
MaxStartups 10:30:60

```

## Rationale{% #rationale %}

To protect a system from denial of service due to a large number of pending authentication connection attempts, use the rate limiting function of MaxStartups to protect availability of sshd logins and prevent overwhelming the daemon.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'linux-base' 2>/dev/null | grep -q '^installed$'; then

var_sshd_set_maxstartups='10:30:60'


mkdir -p /etc/ssh/sshd_config.d
touch /etc/ssh/sshd_config.d/00-complianceascode-hardening.conf
chmod 0600 /etc/ssh/sshd_config.d/00-complianceascode-hardening.conf

LC_ALL=C sed -i "/^\s*MaxStartups\s\+/Id" "/etc/ssh/sshd_config"
LC_ALL=C sed -i "/^\s*MaxStartups\s\+/Id" "/etc/ssh/sshd_config.d"/*.conf
if [ -e "/etc/ssh/sshd_config.d/00-complianceascode-hardening.conf" ] ; then

    LC_ALL=C sed -i "/^\s*MaxStartups\s\+/Id" "/etc/ssh/sshd_config.d/00-complianceascode-hardening.conf"
else
    touch "/etc/ssh/sshd_config.d/00-complianceascode-hardening.conf"
fi
# make sure file has newline at the end
sed -i -e '$a\' "/etc/ssh/sshd_config.d/00-complianceascode-hardening.conf"

cp "/etc/ssh/sshd_config.d/00-complianceascode-hardening.conf" "/etc/ssh/sshd_config.d/00-complianceascode-hardening.conf.bak"
# Insert at the beginning of the file
printf '%s\n' "MaxStartups $var_sshd_set_maxstartups" > "/etc/ssh/sshd_config.d/00-complianceascode-hardening.conf"
cat "/etc/ssh/sshd_config.d/00-complianceascode-hardening.conf.bak" >> "/etc/ssh/sshd_config.d/00-complianceascode-hardening.conf"
# Clean up after ourselves.
rm "/etc/ssh/sshd_config.d/00-complianceascode-hardening.conf.bak"

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
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.6
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
  - sshd_set_maxstartups
- name: XCCDF Value var_sshd_set_maxstartups # promote to variable
  set_fact:
    var_sshd_set_maxstartups: !!str 10:30:60
  tags:
    - always

- name: Ensure SSH MaxStartups is configured
  block:

  - name: Deduplicate values from /etc/ssh/sshd_config
    lineinfile:
      path: /etc/ssh/sshd_config
      create: false
      regexp: (?i)(?i)^\s*{{ "MaxStartups"| regex_escape }}\s+
      state: absent

  - name: Check if /etc/ssh/sshd_config.d exists
    stat:
      path: /etc/ssh/sshd_config.d
    register: _etc_ssh_sshd_config_d_exists

  - name: Check if the parameter MaxStartups is present in /etc/ssh/sshd_config.d
    find:
      paths: /etc/ssh/sshd_config.d
      recurse: 'yes'
      follow: 'no'
      contains: (?i)^\s*{{ "MaxStartups"| regex_escape }}\s+
    register: _etc_ssh_sshd_config_d_has_parameter
    when: _etc_ssh_sshd_config_d_exists.stat.isdir is defined and _etc_ssh_sshd_config_d_exists.stat.isdir

  - name: Remove parameter from files in /etc/ssh/sshd_config.d
    lineinfile:
      path: '{{ item.path }}'
      create: false
      regexp: (?i)(?i)^\s*{{ "MaxStartups"| regex_escape }}\s+
      state: absent
    with_items: '{{ _etc_ssh_sshd_config_d_has_parameter.files }}'
    when: _etc_ssh_sshd_config_d_has_parameter.matched

  - name: Insert correct line to /etc/ssh/sshd_config.d/00-complianceascode-hardening.conf
    lineinfile:
      path: /etc/ssh/sshd_config.d/00-complianceascode-hardening.conf
      create: true
      regexp: (?i)(?i)^\s*{{ "MaxStartups"| regex_escape }}\s+
      line: MaxStartups {{ var_sshd_set_maxstartups }}
      state: present
      insertbefore: BOF
      validate: /usr/sbin/sshd -t -f %s
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.6
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
  - sshd_set_maxstartups

- name: Ensure SSH MaxStartups is configured - set file mode for /etc/ssh/sshd_config.d/00-complianceascode-hardening.conf
  ansible.builtin.file:
    path: /etc/ssh/sshd_config.d/00-complianceascode-hardening.conf
    mode: '0600'
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.6
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
  - sshd_set_maxstartups
```
