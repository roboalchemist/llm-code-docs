# Source: https://docs.datadoghq.com/security/default_rules/def-000-6wc.md

---
title: Set SSH Client Alive Count Max
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Set SSH Client Alive Count Max
---

# Set SSH Client Alive Count Max
 
## Description{% #description %}

The SSH server sends at most `ClientAliveCountMax` messages during a SSH session and waits for a response from the SSH client. The option `ClientAliveInterval` configures timeout after each `ClientAliveCountMax` message. If the SSH server does not receive a response from the client, then the connection is considered unresponsive and terminated. For SSH earlier than v8.2, a `ClientAliveCountMax` value of `0` causes a timeout precisely when the `ClientAliveInterval` is set. Starting with v8.2, a value of `0` disables the timeout functionality completely. If the option is set to a number greater than `0`, then the session will be disconnected after `ClientAliveInterval * ClientAliveCountMax` seconds without receiving a keep alive message.

## Rationale{% #rationale %}

This ensures a user login will be terminated as soon as the `ClientAliveInterval` is reached.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'linux-base' 2>/dev/null | grep -q '^installed$'; then

var_sshd_set_keepalive='3'


mkdir -p /etc/ssh/sshd_config.d
touch /etc/ssh/sshd_config.d/00-complianceascode-hardening.conf
chmod 0600 /etc/ssh/sshd_config.d/00-complianceascode-hardening.conf

LC_ALL=C sed -i "/^\s*ClientAliveCountMax\s\+/Id" "/etc/ssh/sshd_config"
LC_ALL=C sed -i "/^\s*ClientAliveCountMax\s\+/Id" "/etc/ssh/sshd_config.d"/*.conf
if [ -e "/etc/ssh/sshd_config.d/00-complianceascode-hardening.conf" ] ; then
    
    LC_ALL=C sed -i "/^\s*ClientAliveCountMax\s\+/Id" "/etc/ssh/sshd_config.d/00-complianceascode-hardening.conf"
else
    touch "/etc/ssh/sshd_config.d/00-complianceascode-hardening.conf"
fi
# make sure file has newline at the end
sed -i -e '$a\' "/etc/ssh/sshd_config.d/00-complianceascode-hardening.conf"

cp "/etc/ssh/sshd_config.d/00-complianceascode-hardening.conf" "/etc/ssh/sshd_config.d/00-complianceascode-hardening.conf.bak"
# Insert at the beginning of the file
printf '%s\n' "ClientAliveCountMax $var_sshd_set_keepalive" > "/etc/ssh/sshd_config.d/00-complianceascode-hardening.conf"
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
  - CJIS-5.5.6
  - DISA-STIG-UBTU-20-010036
  - NIST-800-171-3.1.11
  - NIST-800-53-AC-12
  - NIST-800-53-AC-17(a)
  - NIST-800-53-AC-2(5)
  - NIST-800-53-CM-6(a)
  - NIST-800-53-SC-10
  - PCI-DSS-Req-8.1.8
  - PCI-DSSv4-8.2
  - PCI-DSSv4-8.2.8
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
  - sshd_set_keepalive
- name: XCCDF Value var_sshd_set_keepalive # promote to variable
  set_fact:
    var_sshd_set_keepalive: !!str 3
  tags:
    - always

- name: Set SSH Client Alive Count Max
  block:

  - name: Deduplicate values from /etc/ssh/sshd_config
    lineinfile:
      path: /etc/ssh/sshd_config
      create: false
      regexp: (?i)(?i)^\s*{{ "ClientAliveCountMax"| regex_escape }}\s+
      state: absent

  - name: Check if /etc/ssh/sshd_config.d exists
    stat:
      path: /etc/ssh/sshd_config.d
    register: _etc_ssh_sshd_config_d_exists

  - name: Check if the parameter ClientAliveCountMax is present in /etc/ssh/sshd_config.d
    find:
      paths: /etc/ssh/sshd_config.d
      recurse: 'yes'
      follow: 'no'
      contains: (?i)^\s*{{ "ClientAliveCountMax"| regex_escape }}\s+
    register: _etc_ssh_sshd_config_d_has_parameter
    when: _etc_ssh_sshd_config_d_exists.stat.isdir is defined and _etc_ssh_sshd_config_d_exists.stat.isdir

  - name: Remove parameter from files in /etc/ssh/sshd_config.d
    lineinfile:
      path: '{{ item.path }}'
      create: false
      regexp: (?i)(?i)^\s*{{ "ClientAliveCountMax"| regex_escape }}\s+
      state: absent
    with_items: '{{ _etc_ssh_sshd_config_d_has_parameter.files }}'
    when: _etc_ssh_sshd_config_d_has_parameter.matched

  - name: Insert correct line to /etc/ssh/sshd_config.d/00-complianceascode-hardening.conf
    lineinfile:
      path: /etc/ssh/sshd_config.d/00-complianceascode-hardening.conf
      create: true
      regexp: (?i)(?i)^\s*{{ "ClientAliveCountMax"| regex_escape }}\s+
      line: ClientAliveCountMax {{ var_sshd_set_keepalive }}
      state: present
      insertbefore: BOF
      validate: /usr/sbin/sshd -t -f %s
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - CJIS-5.5.6
  - DISA-STIG-UBTU-20-010036
  - NIST-800-171-3.1.11
  - NIST-800-53-AC-12
  - NIST-800-53-AC-17(a)
  - NIST-800-53-AC-2(5)
  - NIST-800-53-CM-6(a)
  - NIST-800-53-SC-10
  - PCI-DSS-Req-8.1.8
  - PCI-DSSv4-8.2
  - PCI-DSSv4-8.2.8
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
  - sshd_set_keepalive

- name: Set SSH Client Alive Count Max - set file mode for /etc/ssh/sshd_config.d/00-complianceascode-hardening.conf
  ansible.builtin.file:
    path: /etc/ssh/sshd_config.d/00-complianceascode-hardening.conf
    mode: '0600'
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - CJIS-5.5.6
  - DISA-STIG-UBTU-20-010036
  - NIST-800-171-3.1.11
  - NIST-800-53-AC-12
  - NIST-800-53-AC-17(a)
  - NIST-800-53-AC-2(5)
  - NIST-800-53-CM-6(a)
  - NIST-800-53-SC-10
  - PCI-DSS-Req-8.1.8
  - PCI-DSSv4-8.2
  - PCI-DSSv4-8.2.8
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
  - sshd_set_keepalive
```
