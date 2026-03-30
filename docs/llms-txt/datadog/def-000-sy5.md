# Source: https://docs.datadoghq.com/security/default_rules/def-000-sy5.md

---
title: Enable Randomized Layout of Virtual Address Space
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Enable Randomized Layout of Virtual
  Address Space
---

# Enable Randomized Layout of Virtual Address Space

## Description{% #description %}

To set the runtime status of the `kernel.randomize_va_space` kernel parameter, run the following command:

```
$ sudo sysctl -w kernel.randomize_va_space=2
```

To make sure that the setting is persistent, add the following line to a file in the directory `/etc/sysctl.d`:

```
kernel.randomize_va_space = 2
```

## Rationale{% #rationale %}

Address space layout randomization (ASLR) makes it more difficult for an attacker to predict the location of attack code they have introduced into a process's address space during an attempt at exploitation. Additionally, ASLR makes it more difficult for an attacker to know the location of existing code in order to re-purpose it using return oriented programming (ROP) techniques.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'linux-base' 2>/dev/null | grep -q '^installed$'; then

# Comment out any occurrences of kernel.randomize_va_space from /etc/sysctl.d/*.conf files

for f in /etc/sysctl.d/*.conf /run/sysctl.d/*.conf /usr/local/lib/sysctl.d/*.conf /etc/ufw/sysctl.conf; do


  # skip systemd-sysctl symlink (/etc/sysctl.d/99-sysctl.conf -> /etc/sysctl.conf)
  if [[ "$(readlink -f "$f")" == "/etc/sysctl.conf" ]]; then continue; fi

  matching_list=$(grep -P '^(?!#).*[\s]*kernel.randomize_va_space.*$' $f | uniq )
  if ! test -z "$matching_list"; then
    while IFS= read -r entry; do
      escaped_entry=$(sed -e 's|/|\\/|g' <<< "$entry")
      # comment out "kernel.randomize_va_space" matches to preserve user data
      sed -i --follow-symlinks "s/^${escaped_entry}$/# &/g" $f
    done <<< "$matching_list"
  fi
done

#
# Set sysctl config file which to save the desired value
#

SYSCONFIG_FILE="/etc/sysctl.conf"


#
# Set runtime for kernel.randomize_va_space
#
if ! { rpm --quiet -q kernel rpm-ostree bootc && ! rpm --quiet -q openshift-kubelet && { [ -f "/run/.containerenv" ] || [ -f "/.containerenv" ]; }; } ; then
    /sbin/sysctl -q -n -w kernel.randomize_va_space="2"
fi

#
# If kernel.randomize_va_space present in /etc/sysctl.conf, change value to "2"
#   else, add "kernel.randomize_va_space = 2" to /etc/sysctl.conf
#

# Strip any search characters in the key arg so that the key can be replaced without
# adding any search characters to the config file.
stripped_key=$(sed 's/[\^=\$,;+]*//g' <<< "^kernel.randomize_va_space")

# shellcheck disable=SC2059
printf -v formatted_output "%s = %s" "$stripped_key" "2"

# If the key exists, change it. Otherwise, add it to the config_file.
# We search for the key string followed by a word boundary (matched by \>),
# so if we search for 'setting', 'setting2' won't match.
if LC_ALL=C grep -q -m 1 -i -e "^kernel.randomize_va_space\\>" "${SYSCONFIG_FILE}"; then
    escaped_formatted_output=$(sed -e 's|/|\\/|g' <<< "$formatted_output")
    LC_ALL=C sed -i --follow-symlinks "s/^kernel.randomize_va_space\\>.*/$escaped_formatted_output/gi" "${SYSCONFIG_FILE}"
else
    if [[ -s "${SYSCONFIG_FILE}" ]] && [[ -n "$(tail -c 1 -- "${SYSCONFIG_FILE}" || true)" ]]; then
        LC_ALL=C sed -i --follow-symlinks '$a'\\ "${SYSCONFIG_FILE}"
    fi
    printf '%s\n' "$formatted_output" >> "${SYSCONFIG_FILE}"
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
  - DISA-STIG-UBTU-20-010448
  - NIST-800-171-3.1.7
  - NIST-800-53-CM-6(a)
  - NIST-800-53-SC-30
  - NIST-800-53-SC-30(2)
  - PCI-DSS-Req-2.2.1
  - PCI-DSSv4-3.3
  - PCI-DSSv4-3.3.1
  - PCI-DSSv4-3.3.1.1
  - disable_strategy
  - low_complexity
  - medium_disruption
  - medium_severity
  - reboot_required
  - sysctl_kernel_randomize_va_space

- name: List /etc/sysctl.d/*.conf files
  find:
    paths:
    - /etc/sysctl.d/
    - /run/sysctl.d/
    - /usr/local/lib/sysctl.d/
    contains: ^[\s]*kernel.randomize_va_space.*$
    patterns: '*.conf'
    file_type: any
  register: find_sysctl_d
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - DISA-STIG-UBTU-20-010448
  - NIST-800-171-3.1.7
  - NIST-800-53-CM-6(a)
  - NIST-800-53-SC-30
  - NIST-800-53-SC-30(2)
  - PCI-DSS-Req-2.2.1
  - PCI-DSSv4-3.3
  - PCI-DSSv4-3.3.1
  - PCI-DSSv4-3.3.1.1
  - disable_strategy
  - low_complexity
  - medium_disruption
  - medium_severity
  - reboot_required
  - sysctl_kernel_randomize_va_space

- name: Comment out any occurrences of kernel.randomize_va_space from config files
  replace:
    path: '{{ item.path }}'
    regexp: ^[\s]*kernel.randomize_va_space
    replace: '#kernel.randomize_va_space'
  loop: '{{ find_sysctl_d.files }}'
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - DISA-STIG-UBTU-20-010448
  - NIST-800-171-3.1.7
  - NIST-800-53-CM-6(a)
  - NIST-800-53-SC-30
  - NIST-800-53-SC-30(2)
  - PCI-DSS-Req-2.2.1
  - PCI-DSSv4-3.3
  - PCI-DSSv4-3.3.1
  - PCI-DSSv4-3.3.1.1
  - disable_strategy
  - low_complexity
  - medium_disruption
  - medium_severity
  - reboot_required
  - sysctl_kernel_randomize_va_space

- name: Comment out any occurrences of kernel.randomize_va_space from /etc/ufw/sysctl.conf
  replace:
    path: /etc/ufw/sysctl.conf
    regexp: (^[\s]*kernel.randomize_va_space.*$)
    replace: '# \1'
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - DISA-STIG-UBTU-20-010448
  - NIST-800-171-3.1.7
  - NIST-800-53-CM-6(a)
  - NIST-800-53-SC-30
  - NIST-800-53-SC-30(2)
  - PCI-DSS-Req-2.2.1
  - PCI-DSSv4-3.3
  - PCI-DSSv4-3.3.1
  - PCI-DSSv4-3.3.1.1
  - disable_strategy
  - low_complexity
  - medium_disruption
  - medium_severity
  - reboot_required
  - sysctl_kernel_randomize_va_space

- name: Ensure sysctl kernel.randomize_va_space is set to 2
  sysctl:
    name: kernel.randomize_va_space
    value: '2'
    sysctl_file: /etc/sysctl.conf
    state: present
    reload: true
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - DISA-STIG-UBTU-20-010448
  - NIST-800-171-3.1.7
  - NIST-800-53-CM-6(a)
  - NIST-800-53-SC-30
  - NIST-800-53-SC-30(2)
  - PCI-DSS-Req-2.2.1
  - PCI-DSSv4-3.3
  - PCI-DSSv4-3.3.1
  - PCI-DSSv4-3.3.1.1
  - disable_strategy
  - low_complexity
  - medium_disruption
  - medium_severity
  - reboot_required
  - sysctl_kernel_randomize_va_space
```
