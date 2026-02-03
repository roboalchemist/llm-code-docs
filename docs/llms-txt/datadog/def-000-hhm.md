# Source: https://docs.datadoghq.com/security/default_rules/def-000-hhm.md

---
title: Disable SSH Support for .rhosts Files
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Disable SSH Support for .rhosts Files
---

# Disable SSH Support for .rhosts Files
 
## Description{% #description %}

SSH can emulate the behavior of the obsolete rsh command in allowing users to enable insecure access to their accounts via `.rhosts` files.

The default SSH configuration disables support for `.rhosts`. The appropriate configuration is used if no value is set for `IgnoreRhosts`.

To explicitly disable support for .rhosts files, add or correct the following line in `/etc/ssh/sshd_config.d/00-complianceascode-hardening.conf`:

```
IgnoreRhosts yes
```

## Rationale{% #rationale %}

SSH trust relationships mean a compromise on one host can allow an attacker to move trivially to other hosts.

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

LC_ALL=C sed -i "/^\s*IgnoreRhosts\s\+/Id" "/etc/ssh/sshd_config"
LC_ALL=C sed -i "/^\s*IgnoreRhosts\s\+/Id" "/etc/ssh/sshd_config.d"/*.conf
if [ -e "/etc/ssh/sshd_config.d/01-complianceascode-reinforce-os-defaults.conf" ] ; then
    
    LC_ALL=C sed -i "/^\s*IgnoreRhosts\s\+/Id" "/etc/ssh/sshd_config.d/01-complianceascode-reinforce-os-defaults.conf"
else
    touch "/etc/ssh/sshd_config.d/01-complianceascode-reinforce-os-defaults.conf"
fi
# make sure file has newline at the end
sed -i -e '$a\' "/etc/ssh/sshd_config.d/01-complianceascode-reinforce-os-defaults.conf"

cp "/etc/ssh/sshd_config.d/01-complianceascode-reinforce-os-defaults.conf" "/etc/ssh/sshd_config.d/01-complianceascode-reinforce-os-defaults.conf.bak"
# Insert at the beginning of the file
printf '%s\n' "IgnoreRhosts yes" > "/etc/ssh/sshd_config.d/01-complianceascode-reinforce-os-defaults.conf"
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
  - CJIS-5.5.6
  - NIST-800-171-3.1.12
  - NIST-800-53-AC-17(a)
  - NIST-800-53-CM-6(a)
  - NIST-800-53-CM-7(a)
  - NIST-800-53-CM-7(b)
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.6
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
  - sshd_disable_rhosts

- name: Disable SSH Support for .rhosts Files
  block:

  - name: Deduplicate values from /etc/ssh/sshd_config
    lineinfile:
      path: /etc/ssh/sshd_config
      create: false
      regexp: (?i)(?i)^\s*{{ "IgnoreRhosts"| regex_escape }}\s+
      state: absent

  - name: Check if /etc/ssh/sshd_config.d exists
    stat:
      path: /etc/ssh/sshd_config.d
    register: _etc_ssh_sshd_config_d_exists

  - name: Check if the parameter IgnoreRhosts is present in /etc/ssh/sshd_config.d
    find:
      paths: /etc/ssh/sshd_config.d
      recurse: 'yes'
      follow: 'no'
      contains: (?i)^\s*{{ "IgnoreRhosts"| regex_escape }}\s+
    register: _etc_ssh_sshd_config_d_has_parameter
    when: _etc_ssh_sshd_config_d_exists.stat.isdir is defined and _etc_ssh_sshd_config_d_exists.stat.isdir

  - name: Remove parameter from files in /etc/ssh/sshd_config.d
    lineinfile:
      path: '{{ item.path }}'
      create: false
      regexp: (?i)(?i)^\s*{{ "IgnoreRhosts"| regex_escape }}\s+
      state: absent
    with_items: '{{ _etc_ssh_sshd_config_d_has_parameter.files }}'
    when: _etc_ssh_sshd_config_d_has_parameter.matched

  - name: Insert correct line to /etc/ssh/sshd_config.d/01-complianceascode-reinforce-os-defaults.conf
    lineinfile:
      path: /etc/ssh/sshd_config.d/01-complianceascode-reinforce-os-defaults.conf
      create: true
      regexp: (?i)(?i)^\s*{{ "IgnoreRhosts"| regex_escape }}\s+
      line: IgnoreRhosts yes
      state: present
      insertbefore: BOF
      validate: /usr/sbin/sshd -t -f %s
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - CJIS-5.5.6
  - NIST-800-171-3.1.12
  - NIST-800-53-AC-17(a)
  - NIST-800-53-CM-6(a)
  - NIST-800-53-CM-7(a)
  - NIST-800-53-CM-7(b)
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.6
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
  - sshd_disable_rhosts

- name: Disable SSH Support for .rhosts Files - set file mode for /etc/ssh/sshd_config.d/01-complianceascode-reinforce-os-defaults.conf
  ansible.builtin.file:
    path: /etc/ssh/sshd_config.d/01-complianceascode-reinforce-os-defaults.conf
    mode: '0600'
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - CJIS-5.5.6
  - NIST-800-171-3.1.12
  - NIST-800-53-AC-17(a)
  - NIST-800-53-CM-6(a)
  - NIST-800-53-CM-7(a)
  - NIST-800-53-CM-7(b)
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.6
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
  - sshd_disable_rhosts
```
