# Source: https://docs.datadoghq.com/security/default_rules/def-000-ixs.md

---
title: A remote time server for Chrony is configured
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > A remote time server for Chrony is
  configured
---

# A remote time server for Chrony is configured

## Description{% #description %}

`Chrony` is a daemon which implements the Network Time Protocol (NTP). It is designed to synchronize system clocks across a variety of systems and use a source that is highly accurate. More information on `chrony` can be found at [https://chrony-project.org/](https://chrony-project.org/). `Chrony` can be configured to be a client and/or a server. Add or edit server or pool lines to `/etc/chrony/chrony.conf` as appropriate:

```
server <remote-server>
```

Multiple servers may be configured.

## Rationale{% #rationale %}

If `chrony` is in use on the system proper configuration is vital to ensuring time synchronization is working properly.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'linux-base' 2>/dev/null | grep -q '^installed$' && { dpkg-query --show --showformat='${db:Status-Status}' 'chrony' 2>/dev/null | grep -q '^installed$'; }; then

var_multiple_time_servers='0.pool.ntp.org,1.pool.ntp.org,2.pool.ntp.org,3.pool.ntp.org'


config_file="/etc/chrony/chrony.conf"

if ! grep -q '^[[:space:]]*\(server\|pool\)[[:space:]]\+[[:graph:]]\+' "$config_file" ; then
  if ! grep -q '#[[:space:]]*server' "$config_file" ; then
    for server in $(echo "$var_multiple_time_servers" | tr ',' '\n') ; do
      printf '\nserver %s' "$server" >> "$config_file"
    done
  else
    sed -i 's/#[ \t]*server/server/g' "$config_file"
  fi
  if [[ -s "$config_file" ]] && [[ -n "$(tail -c 1 -- "$config_file" || true)" ]]; then
      LC_ALL=C sed -i --follow-symlinks '$a'\\ "$config_file"
  fi
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
  - NIST-800-53-AU-8(1)(a)
  - NIST-800-53-CM-6(a)
  - PCI-DSS-Req-10.4.3
  - PCI-DSSv4-10.6
  - PCI-DSSv4-10.6.2
  - chronyd_specify_remote_server
  - configure_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
- name: XCCDF Value var_multiple_time_servers # promote to variable
  set_fact:
    var_multiple_time_servers: !!str 0.pool.ntp.org,1.pool.ntp.org,2.pool.ntp.org,3.pool.ntp.org
  tags:
    - always

- name: Detect if chrony is already configured with pools or servers
  find:
    path: /etc
    patterns: chrony.conf
    contains: ^[\s]*(?:server|pool)[\s]+[\w]+
  register: chrony_servers
  when:
  - '"linux-base" in ansible_facts.packages'
  - '"chrony" in ansible_facts.packages'
  tags:
  - NIST-800-53-AU-8(1)(a)
  - NIST-800-53-CM-6(a)
  - PCI-DSS-Req-10.4.3
  - PCI-DSSv4-10.6
  - PCI-DSSv4-10.6.2
  - chronyd_specify_remote_server
  - configure_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Configure remote time servers
  lineinfile:
    path: /etc/chrony/chrony.conf
    line: server {{ item }}
    state: present
    create: true
  loop: '{{ var_multiple_time_servers.split(",") }}'
  when:
  - '"linux-base" in ansible_facts.packages'
  - '"chrony" in ansible_facts.packages'
  - chrony_servers.matched == 0
  tags:
  - NIST-800-53-AU-8(1)(a)
  - NIST-800-53-CM-6(a)
  - PCI-DSS-Req-10.4.3
  - PCI-DSSv4-10.6
  - PCI-DSSv4-10.6.2
  - chronyd_specify_remote_server
  - configure_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
```
