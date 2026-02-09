# Source: https://docs.datadoghq.com/security/default_rules/def-000-kol.md

---
title: Ensure Sudo Logfile Exists - sudo logfile
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Ensure Sudo Logfile Exists - sudo
  logfile
---

# Ensure Sudo Logfile Exists - sudo logfile
 
## Description{% #description %}

A custom log sudo file can be configured with the 'logfile' tag. This rule configures a sudo custom logfile at the default location suggested by CIS, which uses /var/log/sudo.log.

## Rationale{% #rationale %}

A sudo log file simplifies auditing of sudo commands.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'sudo' 2>/dev/null | grep -q '^installed$'; then

var_sudo_logfile='/var/log/sudo.log'


if /usr/sbin/visudo -qcf /etc/sudoers; then
    cp /etc/sudoers /etc/sudoers.bak
    if ! grep -P '^[\s]*Defaults\b[^!\n]*\blogfile\s*=\s*(?:"?([^",\s]+)"?).*$' /etc/sudoers; then
        # sudoers file doesn't define Option logfile
        echo "Defaults logfile=${var_sudo_logfile}" >> /etc/sudoers
    else
        # sudoers file defines Option logfile, remediate if appropriate value is not set
        if ! grep -P "^[\s]*Defaults.*\blogfile=${var_sudo_logfile}\b.*$" /etc/sudoers; then
            
            escaped_variable=${var_sudo_logfile//$'/'/$'\/'}
            sed -Ei "s/(^[\s]*Defaults.*\blogfile=)[-]?.+(\b.*$)/\1$escaped_variable\2/" /etc/sudoers
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
  - PCI-DSS-Req-10.2.5
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.6
  - low_complexity
  - low_disruption
  - low_severity
  - no_reboot_needed
  - restrict_strategy
  - sudo_custom_logfile
- name: XCCDF Value var_sudo_logfile # promote to variable
  set_fact:
    var_sudo_logfile: !!str /var/log/sudo.log
  tags:
    - always

- name: Ensure logfile is enabled with the appropriate value in /etc/sudoers
  lineinfile:
    path: /etc/sudoers
    regexp: ^[\s]*Defaults\s(.*)\blogfile=[-]?.+\b(.*)$
    line: Defaults \1logfile={{ var_sudo_logfile }}\2
    validate: /usr/sbin/visudo -cf %s
    backrefs: true
  register: edit_sudoers_logfile_option
  when: '"sudo" in ansible_facts.packages'
  tags:
  - PCI-DSS-Req-10.2.5
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.6
  - low_complexity
  - low_disruption
  - low_severity
  - no_reboot_needed
  - restrict_strategy
  - sudo_custom_logfile

- name: Enable logfile option with appropriate value in /etc/sudoers
  lineinfile:
    path: /etc/sudoers
    line: Defaults logfile={{ var_sudo_logfile }}
    validate: /usr/sbin/visudo -cf %s
  when:
  - '"sudo" in ansible_facts.packages'
  - edit_sudoers_logfile_option is defined and not edit_sudoers_logfile_option.changed
  tags:
  - PCI-DSS-Req-10.2.5
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.6
  - low_complexity
  - low_disruption
  - low_severity
  - no_reboot_needed
  - restrict_strategy
  - sudo_custom_logfile
```
