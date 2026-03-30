# Source: https://docs.datadoghq.com/security/default_rules/def-000-dif.md

---
title: >-
  Disable Kernel Parameter for Sending ICMP Redirects on all IPv4 Interfaces by
  Default
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Disable Kernel Parameter for Sending
  ICMP Redirects on all IPv4 Interfaces by Default
---

# Disable Kernel Parameter for Sending ICMP Redirects on all IPv4 Interfaces by Default

## Description{% #description %}

To set the runtime status of the `net.ipv4.conf.default.send_redirects` kernel parameter, run the following command:

```
$ sudo sysctl -w net.ipv4.conf.default.send_redirects=0
```

To make sure that the setting is persistent, add the following line to a file in the directory `/etc/sysctl.d`:

```
net.ipv4.conf.default.send_redirects = 0
```

## Rationale{% #rationale %}

ICMP redirect messages are used by routers to inform hosts that a more direct route exists for a particular destination. These messages contain information from the system's route table possibly revealing portions of the network topology.

The ability to send ICMP redirects is only appropriate for systems acting as routers.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'linux-base' 2>/dev/null | grep -q '^installed$'; then

# Comment out any occurrences of net.ipv4.conf.default.send_redirects from /etc/sysctl.d/*.conf files

for f in /etc/sysctl.d/*.conf /run/sysctl.d/*.conf /usr/local/lib/sysctl.d/*.conf /etc/ufw/sysctl.conf; do


  # skip systemd-sysctl symlink (/etc/sysctl.d/99-sysctl.conf -> /etc/sysctl.conf)
  if [[ "$(readlink -f "$f")" == "/etc/sysctl.conf" ]]; then continue; fi

  matching_list=$(grep -P '^(?!#).*[\s]*net.ipv4.conf.default.send_redirects.*$' $f | uniq )
  if ! test -z "$matching_list"; then
    while IFS= read -r entry; do
      escaped_entry=$(sed -e 's|/|\\/|g' <<< "$entry")
      # comment out "net.ipv4.conf.default.send_redirects" matches to preserve user data
      sed -i --follow-symlinks "s/^${escaped_entry}$/# &/g" $f
    done <<< "$matching_list"
  fi
done

#
# Set sysctl config file which to save the desired value
#

SYSCONFIG_FILE="/etc/sysctl.conf"


#
# Set runtime for net.ipv4.conf.default.send_redirects
#
if ! { rpm --quiet -q kernel rpm-ostree bootc && ! rpm --quiet -q openshift-kubelet && { [ -f "/run/.containerenv" ] || [ -f "/.containerenv" ]; }; } ; then
    /sbin/sysctl -q -n -w net.ipv4.conf.default.send_redirects="0"
fi

#
# If net.ipv4.conf.default.send_redirects present in /etc/sysctl.conf, change value to "0"
#   else, add "net.ipv4.conf.default.send_redirects = 0" to /etc/sysctl.conf
#

# Strip any search characters in the key arg so that the key can be replaced without
# adding any search characters to the config file.
stripped_key=$(sed 's/[\^=\$,;+]*//g' <<< "^net.ipv4.conf.default.send_redirects")

# shellcheck disable=SC2059
printf -v formatted_output "%s = %s" "$stripped_key" "0"

# If the key exists, change it. Otherwise, add it to the config_file.
# We search for the key string followed by a word boundary (matched by \>),
# so if we search for 'setting', 'setting2' won't match.
if LC_ALL=C grep -q -m 1 -i -e "^net.ipv4.conf.default.send_redirects\\>" "${SYSCONFIG_FILE}"; then
    escaped_formatted_output=$(sed -e 's|/|\\/|g' <<< "$formatted_output")
    LC_ALL=C sed -i --follow-symlinks "s/^net.ipv4.conf.default.send_redirects\\>.*/$escaped_formatted_output/gi" "${SYSCONFIG_FILE}"
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
  - CJIS-5.10.1.1
  - NIST-800-171-3.1.20
  - NIST-800-53-CM-6(a)
  - NIST-800-53-CM-7(a)
  - NIST-800-53-CM-7(b)
  - NIST-800-53-SC-5
  - NIST-800-53-SC-7(a)
  - PCI-DSSv4-1.4
  - PCI-DSSv4-1.4.5
  - disable_strategy
  - low_complexity
  - medium_disruption
  - medium_severity
  - reboot_required
  - sysctl_net_ipv4_conf_default_send_redirects

- name: List /etc/sysctl.d/*.conf files
  find:
    paths:
    - /etc/sysctl.d/
    - /run/sysctl.d/
    - /usr/local/lib/sysctl.d/
    contains: ^[\s]*net.ipv4.conf.default.send_redirects.*$
    patterns: '*.conf'
    file_type: any
  register: find_sysctl_d
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - CJIS-5.10.1.1
  - NIST-800-171-3.1.20
  - NIST-800-53-CM-6(a)
  - NIST-800-53-CM-7(a)
  - NIST-800-53-CM-7(b)
  - NIST-800-53-SC-5
  - NIST-800-53-SC-7(a)
  - PCI-DSSv4-1.4
  - PCI-DSSv4-1.4.5
  - disable_strategy
  - low_complexity
  - medium_disruption
  - medium_severity
  - reboot_required
  - sysctl_net_ipv4_conf_default_send_redirects

- name: Comment out any occurrences of net.ipv4.conf.default.send_redirects from config
    files
  replace:
    path: '{{ item.path }}'
    regexp: ^[\s]*net.ipv4.conf.default.send_redirects
    replace: '#net.ipv4.conf.default.send_redirects'
  loop: '{{ find_sysctl_d.files }}'
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - CJIS-5.10.1.1
  - NIST-800-171-3.1.20
  - NIST-800-53-CM-6(a)
  - NIST-800-53-CM-7(a)
  - NIST-800-53-CM-7(b)
  - NIST-800-53-SC-5
  - NIST-800-53-SC-7(a)
  - PCI-DSSv4-1.4
  - PCI-DSSv4-1.4.5
  - disable_strategy
  - low_complexity
  - medium_disruption
  - medium_severity
  - reboot_required
  - sysctl_net_ipv4_conf_default_send_redirects

- name: Comment out any occurrences of net.ipv4.conf.default.send_redirects from /etc/ufw/sysctl.conf
  replace:
    path: /etc/ufw/sysctl.conf
    regexp: (^[\s]*net.ipv4.conf.default.send_redirects.*$)
    replace: '# \1'
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - CJIS-5.10.1.1
  - NIST-800-171-3.1.20
  - NIST-800-53-CM-6(a)
  - NIST-800-53-CM-7(a)
  - NIST-800-53-CM-7(b)
  - NIST-800-53-SC-5
  - NIST-800-53-SC-7(a)
  - PCI-DSSv4-1.4
  - PCI-DSSv4-1.4.5
  - disable_strategy
  - low_complexity
  - medium_disruption
  - medium_severity
  - reboot_required
  - sysctl_net_ipv4_conf_default_send_redirects

- name: Ensure sysctl net.ipv4.conf.default.send_redirects is set to 0
  sysctl:
    name: net.ipv4.conf.default.send_redirects
    value: '0'
    sysctl_file: /etc/sysctl.conf
    state: present
    reload: true
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - CJIS-5.10.1.1
  - NIST-800-171-3.1.20
  - NIST-800-53-CM-6(a)
  - NIST-800-53-CM-7(a)
  - NIST-800-53-CM-7(b)
  - NIST-800-53-SC-5
  - NIST-800-53-SC-7(a)
  - PCI-DSSv4-1.4
  - PCI-DSSv4-1.4.5
  - disable_strategy
  - low_complexity
  - medium_disruption
  - medium_severity
  - reboot_required
  - sysctl_net_ipv4_conf_default_send_redirects
```
