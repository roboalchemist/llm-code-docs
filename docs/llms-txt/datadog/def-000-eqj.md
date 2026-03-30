# Source: https://docs.datadoghq.com/security/default_rules/def-000-eqj.md

---
title: Disable Core Dumps for SUID programs
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Disable Core Dumps for SUID programs
---

# Disable Core Dumps for SUID programs

## Description{% #description %}

To set the runtime status of the `fs.suid_dumpable` kernel parameter, run the following command:

```
$ sudo sysctl -w fs.suid_dumpable=0
```

To make sure that the setting is persistent, add the following line to a file in the directory `/etc/sysctl.d`:

```
fs.suid_dumpable = 0
```

## Rationale{% #rationale %}

The core dump of a setuid program is more likely to contain sensitive data, as the program itself runs with greater privileges than the user who initiated execution of the program. Disabling the ability for any setuid program to write a core file decreases the risk of unauthorized access of such data.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'linux-base' 2>/dev/null | grep -q '^installed$'; then

# Comment out any occurrences of fs.suid_dumpable from /etc/sysctl.d/*.conf files

for f in /etc/sysctl.d/*.conf /run/sysctl.d/*.conf /usr/local/lib/sysctl.d/*.conf /etc/ufw/sysctl.conf; do


  # skip systemd-sysctl symlink (/etc/sysctl.d/99-sysctl.conf -> /etc/sysctl.conf)
  if [[ "$(readlink -f "$f")" == "/etc/sysctl.conf" ]]; then continue; fi

  matching_list=$(grep -P '^(?!#).*[\s]*fs.suid_dumpable.*$' $f | uniq )
  if ! test -z "$matching_list"; then
    while IFS= read -r entry; do
      escaped_entry=$(sed -e 's|/|\\/|g' <<< "$entry")
      # comment out "fs.suid_dumpable" matches to preserve user data
      sed -i --follow-symlinks "s/^${escaped_entry}$/# &/g" $f
    done <<< "$matching_list"
  fi
done

#
# Set sysctl config file which to save the desired value
#

SYSCONFIG_FILE="/etc/sysctl.conf"


#
# Set runtime for fs.suid_dumpable
#
if ! { rpm --quiet -q kernel rpm-ostree bootc && ! rpm --quiet -q openshift-kubelet && { [ -f "/run/.containerenv" ] || [ -f "/.containerenv" ]; }; } ; then
    /sbin/sysctl -q -n -w fs.suid_dumpable="0"
fi

#
# If fs.suid_dumpable present in /etc/sysctl.conf, change value to "0"
#   else, add "fs.suid_dumpable = 0" to /etc/sysctl.conf
#

# Strip any search characters in the key arg so that the key can be replaced without
# adding any search characters to the config file.
stripped_key=$(sed 's/[\^=\$,;+]*//g' <<< "^fs.suid_dumpable")

# shellcheck disable=SC2059
printf -v formatted_output "%s = %s" "$stripped_key" "0"

# If the key exists, change it. Otherwise, add it to the config_file.
# We search for the key string followed by a word boundary (matched by \>),
# so if we search for 'setting', 'setting2' won't match.
if LC_ALL=C grep -q -m 1 -i -e "^fs.suid_dumpable\\>" "${SYSCONFIG_FILE}"; then
    escaped_formatted_output=$(sed -e 's|/|\\/|g' <<< "$formatted_output")
    LC_ALL=C sed -i --follow-symlinks "s/^fs.suid_dumpable\\>.*/$escaped_formatted_output/gi" "${SYSCONFIG_FILE}"
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
  - NIST-800-53-SI-11(a)
  - NIST-800-53-SI-11(b)
  - PCI-DSSv4-3.3
  - PCI-DSSv4-3.3.1
  - PCI-DSSv4-3.3.1.1
  - disable_strategy
  - low_complexity
  - medium_disruption
  - medium_severity
  - reboot_required
  - sysctl_fs_suid_dumpable

- name: List /etc/sysctl.d/*.conf files
  find:
    paths:
    - /etc/sysctl.d/
    - /run/sysctl.d/
    - /usr/local/lib/sysctl.d/
    contains: ^[\s]*fs.suid_dumpable.*$
    patterns: '*.conf'
    file_type: any
  register: find_sysctl_d
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - NIST-800-53-SI-11(a)
  - NIST-800-53-SI-11(b)
  - PCI-DSSv4-3.3
  - PCI-DSSv4-3.3.1
  - PCI-DSSv4-3.3.1.1
  - disable_strategy
  - low_complexity
  - medium_disruption
  - medium_severity
  - reboot_required
  - sysctl_fs_suid_dumpable

- name: Comment out any occurrences of fs.suid_dumpable from config files
  replace:
    path: '{{ item.path }}'
    regexp: ^[\s]*fs.suid_dumpable
    replace: '#fs.suid_dumpable'
  loop: '{{ find_sysctl_d.files }}'
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - NIST-800-53-SI-11(a)
  - NIST-800-53-SI-11(b)
  - PCI-DSSv4-3.3
  - PCI-DSSv4-3.3.1
  - PCI-DSSv4-3.3.1.1
  - disable_strategy
  - low_complexity
  - medium_disruption
  - medium_severity
  - reboot_required
  - sysctl_fs_suid_dumpable

- name: Comment out any occurrences of fs.suid_dumpable from /etc/ufw/sysctl.conf
  replace:
    path: /etc/ufw/sysctl.conf
    regexp: (^[\s]*fs.suid_dumpable.*$)
    replace: '# \1'
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - NIST-800-53-SI-11(a)
  - NIST-800-53-SI-11(b)
  - PCI-DSSv4-3.3
  - PCI-DSSv4-3.3.1
  - PCI-DSSv4-3.3.1.1
  - disable_strategy
  - low_complexity
  - medium_disruption
  - medium_severity
  - reboot_required
  - sysctl_fs_suid_dumpable

- name: Ensure sysctl fs.suid_dumpable is set to 0
  sysctl:
    name: fs.suid_dumpable
    value: '0'
    sysctl_file: /etc/sysctl.conf
    state: present
    reload: true
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - NIST-800-53-SI-11(a)
  - NIST-800-53-SI-11(b)
  - PCI-DSSv4-3.3
  - PCI-DSSv4-3.3.1
  - PCI-DSSv4-3.3.1.1
  - disable_strategy
  - low_complexity
  - medium_disruption
  - medium_severity
  - reboot_required
  - sysctl_fs_suid_dumpable
```
