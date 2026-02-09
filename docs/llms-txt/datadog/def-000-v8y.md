# Source: https://docs.datadoghq.com/security/default_rules/def-000-v8y.md

---
title: Set SSH Client Alive Interval
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Set SSH Client Alive Interval
---

# Set SSH Client Alive Interval
 
## Description{% #description %}

SSH allows administrators to set a network responsiveness timeout interval. After this interval has passed, the unresponsive client will be automatically logged out.

To set this timeout interval, edit the following line in `/etc/ssh/sshd_config` as follows:

```
ClientAliveInterval 300
        
```

The timeout **interval** is given in seconds. For example, have a timeout of 10 minutes, set **interval** to 600.

If a shorter timeout has already been set for the login shell, that value will preempt any SSH setting made in `/etc/ssh/sshd_config`. Keep in mind that some processes may stop SSH from correctly detecting that the user is idle.

## Rationale{% #rationale %}

Terminating an idle ssh session within a short time period reduces the window of opportunity for unauthorized personnel to take control of a management session enabled on the console or console port that has been let unattended.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'linux-base' 2>/dev/null | grep -q '^installed$'; then

sshd_idle_timeout_value='300'


mkdir -p /etc/ssh/sshd_config.d
touch /etc/ssh/sshd_config.d/00-complianceascode-hardening.conf
chmod 0600 /etc/ssh/sshd_config.d/00-complianceascode-hardening.conf

LC_ALL=C sed -i "/^\s*ClientAliveInterval\s\+/Id" "/etc/ssh/sshd_config"
LC_ALL=C sed -i "/^\s*ClientAliveInterval\s\+/Id" "/etc/ssh/sshd_config.d"/*.conf
if [ -e "/etc/ssh/sshd_config.d/00-complianceascode-hardening.conf" ] ; then
    
    LC_ALL=C sed -i "/^\s*ClientAliveInterval\s\+/Id" "/etc/ssh/sshd_config.d/00-complianceascode-hardening.conf"
else
    touch "/etc/ssh/sshd_config.d/00-complianceascode-hardening.conf"
fi
# make sure file has newline at the end
sed -i -e '$a\' "/etc/ssh/sshd_config.d/00-complianceascode-hardening.conf"

cp "/etc/ssh/sshd_config.d/00-complianceascode-hardening.conf" "/etc/ssh/sshd_config.d/00-complianceascode-hardening.conf.bak"
# Insert at the beginning of the file
printf '%s\n' "ClientAliveInterval $sshd_idle_timeout_value" > "/etc/ssh/sshd_config.d/00-complianceascode-hardening.conf"
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
  - DISA-STIG-UBTU-20-010037
  - NIST-800-171-3.1.11
  - NIST-800-53-AC-12
  - NIST-800-53-AC-17(a)
  - NIST-800-53-AC-17(a)
  - NIST-800-53-AC-2(5)
  - NIST-800-53-CM-6(a)
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
  - sshd_set_idle_timeout
- name: XCCDF Value sshd_idle_timeout_value # promote to variable
  set_fact:
    sshd_idle_timeout_value: !!str 300
  tags:
    - always

- name: Set SSH Client Alive Interval
  block:

  - name: Deduplicate values from /etc/ssh/sshd_config
    lineinfile:
      path: /etc/ssh/sshd_config
      create: false
      regexp: (?i)(?i)^\s*{{ "ClientAliveInterval"| regex_escape }}\s+
      state: absent

  - name: Check if /etc/ssh/sshd_config.d exists
    stat:
      path: /etc/ssh/sshd_config.d
    register: _etc_ssh_sshd_config_d_exists

  - name: Check if the parameter ClientAliveInterval is present in /etc/ssh/sshd_config.d
    find:
      paths: /etc/ssh/sshd_config.d
      recurse: 'yes'
      follow: 'no'
      contains: (?i)^\s*{{ "ClientAliveInterval"| regex_escape }}\s+
    register: _etc_ssh_sshd_config_d_has_parameter
    when: _etc_ssh_sshd_config_d_exists.stat.isdir is defined and _etc_ssh_sshd_config_d_exists.stat.isdir

  - name: Remove parameter from files in /etc/ssh/sshd_config.d
    lineinfile:
      path: '{{ item.path }}'
      create: false
      regexp: (?i)(?i)^\s*{{ "ClientAliveInterval"| regex_escape }}\s+
      state: absent
    with_items: '{{ _etc_ssh_sshd_config_d_has_parameter.files }}'
    when: _etc_ssh_sshd_config_d_has_parameter.matched

  - name: Insert correct line to /etc/ssh/sshd_config.d/00-complianceascode-hardening.conf
    lineinfile:
      path: /etc/ssh/sshd_config.d/00-complianceascode-hardening.conf
      create: true
      regexp: (?i)(?i)^\s*{{ "ClientAliveInterval"| regex_escape }}\s+
      line: ClientAliveInterval {{ sshd_idle_timeout_value }}
      state: present
      insertbefore: BOF
      validate: /usr/sbin/sshd -t -f %s
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - CJIS-5.5.6
  - DISA-STIG-UBTU-20-010037
  - NIST-800-171-3.1.11
  - NIST-800-53-AC-12
  - NIST-800-53-AC-17(a)
  - NIST-800-53-AC-17(a)
  - NIST-800-53-AC-2(5)
  - NIST-800-53-CM-6(a)
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
  - sshd_set_idle_timeout

- name: Set SSH Client Alive Interval - set file mode for /etc/ssh/sshd_config.d/00-complianceascode-hardening.conf
  ansible.builtin.file:
    path: /etc/ssh/sshd_config.d/00-complianceascode-hardening.conf
    mode: '0600'
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - CJIS-5.5.6
  - DISA-STIG-UBTU-20-010037
  - NIST-800-171-3.1.11
  - NIST-800-53-AC-12
  - NIST-800-53-AC-17(a)
  - NIST-800-53-AC-17(a)
  - NIST-800-53-AC-2(5)
  - NIST-800-53-CM-6(a)
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
  - sshd_set_idle_timeout
```

## Warning{% #warning %}

SSH disconnecting unresponsive clients will not have desired effect without also configuring ClientAliveCountMax in the SSH service configuration.
