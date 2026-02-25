# Source: https://docs.datadoghq.com/security/default_rules/def-000-epd.md

---
title: Disable Kernel Parameter for IP Forwarding on IPv4 Interfaces
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Disable Kernel Parameter for IP
  Forwarding on IPv4 Interfaces
---

# Disable Kernel Parameter for IP Forwarding on IPv4 Interfaces

## Description{% #description %}

To set the runtime status of the `net.ipv4.ip_forward` kernel parameter, run the following command:

```
$ sudo sysctl -w net.ipv4.ip_forward=0
```

To make sure that the setting is persistent, add the following line to a file in the directory `/etc/sysctl.d`:

```
net.ipv4.ip_forward = 0
```

## Rationale{% #rationale %}

Routing protocol daemons are typically used on routers to exchange network topology information with other routers. If this capability is used when not required, system network information may be unnecessarily transmitted across the network.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'linux-base' 2>/dev/null | grep -q '^installed$'; then

# Comment out any occurrences of net.ipv4.ip_forward from /etc/sysctl.d/*.conf files

for f in /etc/sysctl.d/*.conf /run/sysctl.d/*.conf /usr/local/lib/sysctl.d/*.conf /etc/ufw/sysctl.conf; do


  # skip systemd-sysctl symlink (/etc/sysctl.d/99-sysctl.conf -> /etc/sysctl.conf)
  if [[ "$(readlink -f "$f")" == "/etc/sysctl.conf" ]]; then continue; fi

  matching_list=$(grep -P '^(?!#).*[\s]*net.ipv4.ip_forward.*$' $f | uniq )
  if ! test -z "$matching_list"; then
    while IFS= read -r entry; do
      escaped_entry=$(sed -e 's|/|\\/|g' <<< "$entry")
      # comment out "net.ipv4.ip_forward" matches to preserve user data
      sed -i --follow-symlinks "s/^${escaped_entry}$/# &/g" $f
    done <<< "$matching_list"
  fi
done

#
# Set sysctl config file which to save the desired value
#

SYSCONFIG_FILE="/etc/sysctl.conf"


#
# Set runtime for net.ipv4.ip_forward
#
if ! { rpm --quiet -q kernel rpm-ostree bootc && ! rpm --quiet -q openshift-kubelet && { [ -f "/run/.containerenv" ] || [ -f "/.containerenv" ]; }; } ; then
    /sbin/sysctl -q -n -w net.ipv4.ip_forward="0"
fi

#
# If net.ipv4.ip_forward present in /etc/sysctl.conf, change value to "0"
#   else, add "net.ipv4.ip_forward = 0" to /etc/sysctl.conf
#

# Strip any search characters in the key arg so that the key can be replaced without
# adding any search characters to the config file.
stripped_key=$(sed 's/[\^=\$,;+]*//g' <<< "^net.ipv4.ip_forward")

# shellcheck disable=SC2059
printf -v formatted_output "%s = %s" "$stripped_key" "0"

# If the key exists, change it. Otherwise, add it to the config_file.
# We search for the key string followed by a word boundary (matched by \>),
# so if we search for 'setting', 'setting2' won't match.
if LC_ALL=C grep -q -m 1 -i -e "^net.ipv4.ip_forward\\>" "${SYSCONFIG_FILE}"; then
    escaped_formatted_output=$(sed -e 's|/|\\/|g' <<< "$formatted_output")
    LC_ALL=C sed -i --follow-symlinks "s/^net.ipv4.ip_forward\\>.*/$escaped_formatted_output/gi" "${SYSCONFIG_FILE}"
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
  - NIST-800-171-3.1.20
  - NIST-800-53-CM-6(a)
  - NIST-800-53-CM-7(a)
  - NIST-800-53-CM-7(b)
  - NIST-800-53-SC-5
  - NIST-800-53-SC-7(a)
  - PCI-DSS-Req-1.3.1
  - PCI-DSS-Req-1.3.2
  - PCI-DSSv4-1.4
  - PCI-DSSv4-1.4.3
  - disable_strategy
  - low_complexity
  - medium_disruption
  - medium_severity
  - reboot_required
  - sysctl_net_ipv4_ip_forward

- name: List /etc/sysctl.d/*.conf files
  find:
    paths:
    - /etc/sysctl.d/
    - /run/sysctl.d/
    - /usr/local/lib/sysctl.d/
    contains: ^[\s]*net.ipv4.ip_forward.*$
    patterns: '*.conf'
    file_type: any
  register: find_sysctl_d
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - NIST-800-171-3.1.20
  - NIST-800-53-CM-6(a)
  - NIST-800-53-CM-7(a)
  - NIST-800-53-CM-7(b)
  - NIST-800-53-SC-5
  - NIST-800-53-SC-7(a)
  - PCI-DSS-Req-1.3.1
  - PCI-DSS-Req-1.3.2
  - PCI-DSSv4-1.4
  - PCI-DSSv4-1.4.3
  - disable_strategy
  - low_complexity
  - medium_disruption
  - medium_severity
  - reboot_required
  - sysctl_net_ipv4_ip_forward

- name: Comment out any occurrences of net.ipv4.ip_forward from config files
  replace:
    path: '{{ item.path }}'
    regexp: ^[\s]*net.ipv4.ip_forward
    replace: '#net.ipv4.ip_forward'
  loop: '{{ find_sysctl_d.files }}'
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - NIST-800-171-3.1.20
  - NIST-800-53-CM-6(a)
  - NIST-800-53-CM-7(a)
  - NIST-800-53-CM-7(b)
  - NIST-800-53-SC-5
  - NIST-800-53-SC-7(a)
  - PCI-DSS-Req-1.3.1
  - PCI-DSS-Req-1.3.2
  - PCI-DSSv4-1.4
  - PCI-DSSv4-1.4.3
  - disable_strategy
  - low_complexity
  - medium_disruption
  - medium_severity
  - reboot_required
  - sysctl_net_ipv4_ip_forward

- name: Comment out any occurrences of net.ipv4.ip_forward from /etc/ufw/sysctl.conf
  replace:
    path: /etc/ufw/sysctl.conf
    regexp: (^[\s]*net.ipv4.ip_forward.*$)
    replace: '# \1'
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - NIST-800-171-3.1.20
  - NIST-800-53-CM-6(a)
  - NIST-800-53-CM-7(a)
  - NIST-800-53-CM-7(b)
  - NIST-800-53-SC-5
  - NIST-800-53-SC-7(a)
  - PCI-DSS-Req-1.3.1
  - PCI-DSS-Req-1.3.2
  - PCI-DSSv4-1.4
  - PCI-DSSv4-1.4.3
  - disable_strategy
  - low_complexity
  - medium_disruption
  - medium_severity
  - reboot_required
  - sysctl_net_ipv4_ip_forward

- name: Ensure sysctl net.ipv4.ip_forward is set to 0
  sysctl:
    name: net.ipv4.ip_forward
    value: '0'
    sysctl_file: /etc/sysctl.conf
    state: present
    reload: true
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - NIST-800-171-3.1.20
  - NIST-800-53-CM-6(a)
  - NIST-800-53-CM-7(a)
  - NIST-800-53-CM-7(b)
  - NIST-800-53-SC-5
  - NIST-800-53-SC-7(a)
  - PCI-DSS-Req-1.3.1
  - PCI-DSS-Req-1.3.2
  - PCI-DSSv4-1.4
  - PCI-DSSv4-1.4.3
  - disable_strategy
  - low_complexity
  - medium_disruption
  - medium_severity
  - reboot_required
  - sysctl_net_ipv4_ip_forward
```

## Warning{% #warning %}

Certain technologies such as virtual machines, containers, etc. rely on IPv4 forwarding to enable and use networking. Disabling IPv4 forwarding would cause those technologies to stop working. Therefore, this rule should not be used in profiles or benchmarks that target usage of IPv4 forwarding.
