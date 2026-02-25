# Source: https://docs.datadoghq.com/security/default_rules/def-000-3lu.md

---
title: >-
  Disable Kernel Parameter for Accepting Source-Routed Packets on IPv6
  Interfaces by Default
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Disable Kernel Parameter for Accepting
  Source-Routed Packets on IPv6 Interfaces by Default
---

# Disable Kernel Parameter for Accepting Source-Routed Packets on IPv6 Interfaces by Default

## Description{% #description %}

To set the runtime status of the `net.ipv6.conf.default.accept_source_route` kernel parameter, run the following command:

```
$ sudo sysctl -w net.ipv6.conf.default.accept_source_route=0
```

To make sure that the setting is persistent, add the following line to a file in the directory `/etc/sysctl.d`:

```
net.ipv6.conf.default.accept_source_route = 0
```

## Rationale{% #rationale %}

Source-routed packets allow the source of the packet to suggest routers forward the packet along a different path than configured on the router, which can be used to bypass network security measures. This requirement applies only to the forwarding of source-routerd traffic, such as when IPv6 forwarding is enabled and the system is functioning as a router. Accepting source-routed packets in the IPv6 protocol has few legitimate uses. It should be disabled unless it is absolutely required.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'linux-base' 2>/dev/null | grep -q '^installed$'; then

# Comment out any occurrences of net.ipv6.conf.default.accept_source_route from /etc/sysctl.d/*.conf files

for f in /etc/sysctl.d/*.conf /run/sysctl.d/*.conf /usr/local/lib/sysctl.d/*.conf /etc/ufw/sysctl.conf; do


  # skip systemd-sysctl symlink (/etc/sysctl.d/99-sysctl.conf -> /etc/sysctl.conf)
  if [[ "$(readlink -f "$f")" == "/etc/sysctl.conf" ]]; then continue; fi

  matching_list=$(grep -P '^(?!#).*[\s]*net.ipv6.conf.default.accept_source_route.*$' $f | uniq )
  if ! test -z "$matching_list"; then
    while IFS= read -r entry; do
      escaped_entry=$(sed -e 's|/|\\/|g' <<< "$entry")
      # comment out "net.ipv6.conf.default.accept_source_route" matches to preserve user data
      sed -i --follow-symlinks "s/^${escaped_entry}$/# &/g" $f
    done <<< "$matching_list"
  fi
done

#
# Set sysctl config file which to save the desired value
#

SYSCONFIG_FILE="/etc/sysctl.conf"

sysctl_net_ipv6_conf_default_accept_source_route_value='0'


#
# Set runtime for net.ipv6.conf.default.accept_source_route
#
if ! { rpm --quiet -q kernel rpm-ostree bootc && ! rpm --quiet -q openshift-kubelet && { [ -f "/run/.containerenv" ] || [ -f "/.containerenv" ]; }; } ; then
    /sbin/sysctl -q -n -w net.ipv6.conf.default.accept_source_route="$sysctl_net_ipv6_conf_default_accept_source_route_value"
fi

#
# If net.ipv6.conf.default.accept_source_route present in /etc/sysctl.conf, change value to appropriate value
#   else, add "net.ipv6.conf.default.accept_source_route = value" to /etc/sysctl.conf
#

# Strip any search characters in the key arg so that the key can be replaced without
# adding any search characters to the config file.
stripped_key=$(sed 's/[\^=\$,;+]*//g' <<< "^net.ipv6.conf.default.accept_source_route")

# shellcheck disable=SC2059
printf -v formatted_output "%s = %s" "$stripped_key" "$sysctl_net_ipv6_conf_default_accept_source_route_value"

# If the key exists, change it. Otherwise, add it to the config_file.
# We search for the key string followed by a word boundary (matched by \>),
# so if we search for 'setting', 'setting2' won't match.
if LC_ALL=C grep -q -m 1 -i -e "^net.ipv6.conf.default.accept_source_route\\>" "${SYSCONFIG_FILE}"; then
    escaped_formatted_output=$(sed -e 's|/|\\/|g' <<< "$formatted_output")
    LC_ALL=C sed -i --follow-symlinks "s/^net.ipv6.conf.default.accept_source_route\\>.*/$escaped_formatted_output/gi" "${SYSCONFIG_FILE}"
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
  - NIST-800-53-CM-6(b)
  - NIST-800-53-CM-6.1(iv)
  - NIST-800-53-CM-7(a)
  - NIST-800-53-CM-7(b)
  - PCI-DSS-Req-1.4.3
  - PCI-DSSv4-1.4
  - PCI-DSSv4-1.4.2
  - disable_strategy
  - low_complexity
  - medium_disruption
  - medium_severity
  - reboot_required
  - sysctl_net_ipv6_conf_default_accept_source_route

- name: List /etc/sysctl.d/*.conf files
  find:
    paths:
    - /etc/sysctl.d/
    - /run/sysctl.d/
    - /usr/local/lib/sysctl.d/
    contains: ^[\s]*net.ipv6.conf.default.accept_source_route.*$
    patterns: '*.conf'
    file_type: any
  register: find_sysctl_d
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - NIST-800-171-3.1.20
  - NIST-800-53-CM-6(a)
  - NIST-800-53-CM-6(b)
  - NIST-800-53-CM-6.1(iv)
  - NIST-800-53-CM-7(a)
  - NIST-800-53-CM-7(b)
  - PCI-DSS-Req-1.4.3
  - PCI-DSSv4-1.4
  - PCI-DSSv4-1.4.2
  - disable_strategy
  - low_complexity
  - medium_disruption
  - medium_severity
  - reboot_required
  - sysctl_net_ipv6_conf_default_accept_source_route

- name: Comment out any occurrences of net.ipv6.conf.default.accept_source_route from
    config files
  replace:
    path: '{{ item.path }}'
    regexp: ^[\s]*net.ipv6.conf.default.accept_source_route
    replace: '#net.ipv6.conf.default.accept_source_route'
  loop: '{{ find_sysctl_d.files }}'
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - NIST-800-171-3.1.20
  - NIST-800-53-CM-6(a)
  - NIST-800-53-CM-6(b)
  - NIST-800-53-CM-6.1(iv)
  - NIST-800-53-CM-7(a)
  - NIST-800-53-CM-7(b)
  - PCI-DSS-Req-1.4.3
  - PCI-DSSv4-1.4
  - PCI-DSSv4-1.4.2
  - disable_strategy
  - low_complexity
  - medium_disruption
  - medium_severity
  - reboot_required
  - sysctl_net_ipv6_conf_default_accept_source_route

- name: Comment out any occurrences of net.ipv6.conf.default.accept_source_route from
    /etc/ufw/sysctl.conf
  replace:
    path: /etc/ufw/sysctl.conf
    regexp: (^[\s]*net.ipv6.conf.default.accept_source_route.*$)
    replace: '# \1'
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - NIST-800-171-3.1.20
  - NIST-800-53-CM-6(a)
  - NIST-800-53-CM-6(b)
  - NIST-800-53-CM-6.1(iv)
  - NIST-800-53-CM-7(a)
  - NIST-800-53-CM-7(b)
  - PCI-DSS-Req-1.4.3
  - PCI-DSSv4-1.4
  - PCI-DSSv4-1.4.2
  - disable_strategy
  - low_complexity
  - medium_disruption
  - medium_severity
  - reboot_required
  - sysctl_net_ipv6_conf_default_accept_source_route
- name: XCCDF Value sysctl_net_ipv6_conf_default_accept_source_route_value # promote to variable
  set_fact:
    sysctl_net_ipv6_conf_default_accept_source_route_value: !!str 0
  tags:
    - always

- name: Ensure sysctl net.ipv6.conf.default.accept_source_route is set
  sysctl:
    name: net.ipv6.conf.default.accept_source_route
    value: '{{ sysctl_net_ipv6_conf_default_accept_source_route_value }}'
    sysctl_file: /etc/sysctl.conf
    state: present
    reload: true
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - NIST-800-171-3.1.20
  - NIST-800-53-CM-6(a)
  - NIST-800-53-CM-6(b)
  - NIST-800-53-CM-6.1(iv)
  - NIST-800-53-CM-7(a)
  - NIST-800-53-CM-7(b)
  - PCI-DSS-Req-1.4.3
  - PCI-DSSv4-1.4
  - PCI-DSSv4-1.4.2
  - disable_strategy
  - low_complexity
  - medium_disruption
  - medium_severity
  - reboot_required
  - sysctl_net_ipv6_conf_default_accept_source_route
```
