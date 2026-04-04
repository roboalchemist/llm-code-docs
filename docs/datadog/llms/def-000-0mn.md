# Source: https://docs.datadoghq.com/security/default_rules/def-000-0mn.md

---
title: Restrict usage of ptrace to descendant processes
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Restrict usage of ptrace to descendant
  processes
---

# Restrict usage of ptrace to descendant processes

## Description{% #description %}

To set the runtime status of the `kernel.yama.ptrace_scope` kernel parameter, run the following command:

```
$ sudo sysctl -w kernel.yama.ptrace_scope=1
```

To make sure that the setting is persistent, add the following line to a file in the directory `/etc/sysctl.d`:

```
kernel.yama.ptrace_scope = 1
```

## Rationale{% #rationale %}

Unrestricted usage of ptrace allows compromised binaries to run ptrace on another processes of the user. Like this, the attacker can steal sensitive information from the target processes (e.g. SSH sessions, web browser, â¦) without any additional assistance from the user (i.e. without resorting to phishing).

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'linux-base' 2>/dev/null | grep -q '^installed$'; then

# Comment out any occurrences of kernel.yama.ptrace_scope from /etc/sysctl.d/*.conf files

for f in /etc/sysctl.d/*.conf /run/sysctl.d/*.conf /usr/local/lib/sysctl.d/*.conf /etc/ufw/sysctl.conf; do


  # skip systemd-sysctl symlink (/etc/sysctl.d/99-sysctl.conf -> /etc/sysctl.conf)
  if [[ "$(readlink -f "$f")" == "/etc/sysctl.conf" ]]; then continue; fi

  matching_list=$(grep -P '^(?!#).*[\s]*kernel.yama.ptrace_scope.*$' $f | uniq )
  if ! test -z "$matching_list"; then
    while IFS= read -r entry; do
      escaped_entry=$(sed -e 's|/|\\/|g' <<< "$entry")
      # comment out "kernel.yama.ptrace_scope" matches to preserve user data
      sed -i --follow-symlinks "s/^${escaped_entry}$/# &/g" $f
    done <<< "$matching_list"
  fi
done

#
# Set sysctl config file which to save the desired value
#

SYSCONFIG_FILE="/etc/sysctl.conf"

sysctl_kernel_yama_ptrace_scope_value='1'


#
# Set runtime for kernel.yama.ptrace_scope
#
if ! { rpm --quiet -q kernel rpm-ostree bootc && ! rpm --quiet -q openshift-kubelet && { [ -f "/run/.containerenv" ] || [ -f "/.containerenv" ]; }; } ; then
    /sbin/sysctl -q -n -w kernel.yama.ptrace_scope="$sysctl_kernel_yama_ptrace_scope_value"
fi

#
# If kernel.yama.ptrace_scope present in /etc/sysctl.conf, change value to appropriate value
#   else, add "kernel.yama.ptrace_scope = value" to /etc/sysctl.conf
#

# Strip any search characters in the key arg so that the key can be replaced without
# adding any search characters to the config file.
stripped_key=$(sed 's/[\^=\$,;+]*//g' <<< "^kernel.yama.ptrace_scope")

# shellcheck disable=SC2059
printf -v formatted_output "%s = %s" "$stripped_key" "$sysctl_kernel_yama_ptrace_scope_value"

# If the key exists, change it. Otherwise, add it to the config_file.
# We search for the key string followed by a word boundary (matched by \>),
# so if we search for 'setting', 'setting2' won't match.
if LC_ALL=C grep -q -m 1 -i -e "^kernel.yama.ptrace_scope\\>" "${SYSCONFIG_FILE}"; then
    escaped_formatted_output=$(sed -e 's|/|\\/|g' <<< "$formatted_output")
    LC_ALL=C sed -i --follow-symlinks "s/^kernel.yama.ptrace_scope\\>.*/$escaped_formatted_output/gi" "${SYSCONFIG_FILE}"
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
  - NIST-800-53-SC-7(10)
  - disable_strategy
  - low_complexity
  - medium_disruption
  - medium_severity
  - reboot_required
  - sysctl_kernel_yama_ptrace_scope

- name: List /etc/sysctl.d/*.conf files
  find:
    paths:
    - /etc/sysctl.d/
    - /run/sysctl.d/
    - /usr/local/lib/sysctl.d/
    contains: ^[\s]*kernel.yama.ptrace_scope.*$
    patterns: '*.conf'
    file_type: any
  register: find_sysctl_d
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - NIST-800-53-SC-7(10)
  - disable_strategy
  - low_complexity
  - medium_disruption
  - medium_severity
  - reboot_required
  - sysctl_kernel_yama_ptrace_scope

- name: Comment out any occurrences of kernel.yama.ptrace_scope from config files
  replace:
    path: '{{ item.path }}'
    regexp: ^[\s]*kernel.yama.ptrace_scope
    replace: '#kernel.yama.ptrace_scope'
  loop: '{{ find_sysctl_d.files }}'
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - NIST-800-53-SC-7(10)
  - disable_strategy
  - low_complexity
  - medium_disruption
  - medium_severity
  - reboot_required
  - sysctl_kernel_yama_ptrace_scope

- name: Comment out any occurrences of kernel.yama.ptrace_scope from /etc/ufw/sysctl.conf
  replace:
    path: /etc/ufw/sysctl.conf
    regexp: (^[\s]*kernel.yama.ptrace_scope.*$)
    replace: '# \1'
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - NIST-800-53-SC-7(10)
  - disable_strategy
  - low_complexity
  - medium_disruption
  - medium_severity
  - reboot_required
  - sysctl_kernel_yama_ptrace_scope
- name: XCCDF Value sysctl_kernel_yama_ptrace_scope_value # promote to variable
  set_fact:
    sysctl_kernel_yama_ptrace_scope_value: !!str 1
  tags:
    - always

- name: Ensure sysctl kernel.yama.ptrace_scope is set
  sysctl:
    name: kernel.yama.ptrace_scope
    value: '{{ sysctl_kernel_yama_ptrace_scope_value }}'
    sysctl_file: /etc/sysctl.conf
    state: present
    reload: true
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - NIST-800-53-SC-7(10)
  - disable_strategy
  - low_complexity
  - medium_disruption
  - medium_severity
  - reboot_required
  - sysctl_kernel_yama_ptrace_scope
```
