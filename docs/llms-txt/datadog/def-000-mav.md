# Source: https://docs.datadoghq.com/security/default_rules/def-000-mav.md

---
title: Set Interactive Session Timeout
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Set Interactive Session Timeout
---

# Set Interactive Session Timeout
 
## Description{% #description %}

Setting the `TMOUT` option in `/etc/profile` ensures that all user sessions will terminate based on inactivity. The value of TMOUT should be exported and read only. The `TMOUT` setting in a file loaded by `/etc/profile`, e.g. `/etc/profile.d/tmout.sh` should read as follows:

```
TMOUT=900
        
```

readonly TMOUT export TMOUT

## Rationale{% #rationale %}

Terminating an idle session within a short time period reduces the window of opportunity for unauthorized personnel to take control of a management session enabled on the console or console port that has been left unattended.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'linux-base' 2>/dev/null | grep -q '^installed$'; then

var_accounts_tmout='900'


# if 0, no occurence of tmout found, if 1, occurence found
tmout_found=0

for f in /etc/bash.bashrc /etc/profile /etc/profile.d/*.sh; do
    if grep --silent '^\s*TMOUT' $f; then
        sed -i -E "s/^(\s*)TMOUT\s*=\s*(\w|\$)*(.*)$/\1TMOUT=$var_accounts_tmout\3/g" $f
        tmout_found=1
        if ! grep --silent '^\s*readonly TMOUT' $f ; then
            echo "readonly TMOUT" >> $f
        fi
        if ! grep --silent '^\s*export TMOUT' $f ; then
            echo "export TMOUT" >> $f
        fi
    fi
done

if [ $tmout_found -eq 0 ]; then
        echo -e "\n# Set TMOUT to $var_accounts_tmout per security requirements" >> /etc/profile.d/tmout.sh
        echo "TMOUT=$var_accounts_tmout" >> /etc/profile.d/tmout.sh
        echo "readonly TMOUT" >> /etc/profile.d/tmout.sh
        echo "export TMOUT" >> /etc/profile.d/tmout.sh
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
  - DISA-STIG-UBTU-20-010013
  - NIST-800-171-3.1.11
  - NIST-800-53-AC-12
  - NIST-800-53-AC-2(5)
  - NIST-800-53-CM-6(a)
  - NIST-800-53-SC-10
  - PCI-DSSv4-8.6
  - PCI-DSSv4-8.6.1
  - accounts_tmout
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
- name: XCCDF Value var_accounts_tmout # promote to variable
  set_fact:
    var_accounts_tmout: !!str 900
  tags:
    - always

- name: Correct any occurrence of TMOUT in /etc/profile
  replace:
    path: /etc/profile
    regexp: ^[^#].*TMOUT=.*
    replace: typeset -xr TMOUT={{ var_accounts_tmout }}
  register: profile_replaced
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - DISA-STIG-UBTU-20-010013
  - NIST-800-171-3.1.11
  - NIST-800-53-AC-12
  - NIST-800-53-AC-2(5)
  - NIST-800-53-CM-6(a)
  - NIST-800-53-SC-10
  - PCI-DSSv4-8.6
  - PCI-DSSv4-8.6.1
  - accounts_tmout
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy

- name: Set Interactive Session Timeout
  lineinfile:
    path: /etc/profile.d/tmout.sh
    create: true
    regexp: TMOUT=
    line: typeset -xr TMOUT={{ var_accounts_tmout }}
    state: present
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - DISA-STIG-UBTU-20-010013
  - NIST-800-171-3.1.11
  - NIST-800-53-AC-12
  - NIST-800-53-AC-2(5)
  - NIST-800-53-CM-6(a)
  - NIST-800-53-SC-10
  - PCI-DSSv4-8.6
  - PCI-DSSv4-8.6.1
  - accounts_tmout
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
```
